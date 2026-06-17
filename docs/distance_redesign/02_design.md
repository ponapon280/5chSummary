# distance.py 新規トピック抽出 — 設計ドキュメント

> 作成日: 2026-06-15
> ステータス: ドラフト（実装前）
> 関連: [01_proposal.md](./01_proposal.md)

本ドキュメントは「直近窓 × トピック再出現スコアリング」を実装に落とすための詳細設計をまとめる。提案の背景・診断は `01_proposal.md` を参照。

---

## 1. ゴールと非ゴール

### ゴール
- **R1**: 過去の要約記事に対して新規な内容を、記事冒頭に簡潔に提示する。
- **R2**: 直近スレで繰り返し話題になっている要素（例: 流行期のAnima）を新規トピックから排除する。
- 判定をできるだけ決定論的にし、実行ごとの出力ブレを抑える。

### 非ゴール
- 要約本文（sum/mod/tools 本体）の生成ロジックの変更。
- 埋め込みモデル・ChromaDBスキーマの大規模変更（既存メタデータの範囲で実現する）。
- 過去に格納済みレコードの再生成（必要なら別タスク）。

---

## 2. 現状のデータ・処理フロー（前提）

### パイプライン（`scripts/main.py`）
```
summarize → table_split → distance(新規判定) → store_to_chroma(DB投入) → movefile
```
`distance.py` は store_to_chroma より前に走るため、判定時点では当該スレはまだDB未投入（＝本来は自己マッチしない設計）。

### ChromaDB コレクション
| ファイル | コレクション | チャンカー |
|---|---|---|
| sum.md | `5ch_summaries` | `sum_chunker2` |
| mod.md | `5ch_ai_models` | `mod_chunker2` |
| tools.md | `5ch_tools` | `tool_chunker2` |

### チャンク・メタデータ（`store_to_chroma.py`）
- `documents`: `"検索文書:【ラベル: 見出し】 本文"`
- `metadata`（主なもの）:
  - `thread_num`: ゼロ埋め3桁文字列（例 `"659"`）
  - `source`: `sum.md` / `mod.md` / `tools.md`
  - `chunk_index`: int
  - 見出し: `summary` / `model` / `tool`
  - `keywords`: カンマ区切り文字列
  - `models`: カンマ区切り文字列（mod系で有用、例 `"Anima, Anim, anim"`）
  - `date`: 文字列日時
- `id`: `"{thread_num}_{file_name}_chunk_{i}"`（例 `"659_mod.md_chunk_0"`）

> 注意: クエリ時は `"検索クエリ:" + text`、格納時は `"検索文書:" + text` という非対称プレフィックスを付けている（ruri系の規約）。現行 distance.py の挙動を踏襲する。

---

## 3. アルゴリズム詳細

### 3.1 直近窓の決定（欠番・非連番に強い形）
```
all_threads = collection から thread_num の distinct を取得
prior = sorted({t for t in all_threads if int(t) < int(current)}, key=int, reverse=True)
recent_threads = prior[:N]
```
- 算術範囲（current-1..current-N）ではなく「実在する手前のスレ上位N」を使う。欠番・再生成・飛び番に強い。
- `recent_threads` は現在スレを構造的に含まない → **自己マッチ不可能**。

### 3.2 チャンクごとの再出現スコア
```
for chunk in current_chunks:
    res = collection.query(
        query_texts = ["検索クエリ:" + chunk["text"]],
        n_results   = K,                       # 窓内の十分な近傍を取る（例 50）
        where       = {"thread_num": {"$in": recent_threads}},
        include     = ["distances", "metadatas"],
    )
    hit_threads = { md["thread_num"]
                    for d, md in zip(res.distances, res.metadatas)
                    if d <= r }
    recurrence = len(hit_threads)        # 「直近窓で何スレに出たか」= DF
    nearest    = min(res.distances) if res.distances else +inf
```

### 3.3 採否ルール
```
if recurrence >= ceil(SAT * len(recent_threads)):
    → 飽和（背景ノイズ）として除外          # R2: Animaを殺す
elif recurrence == 0:
    → 完全新規として採用（priority = "new")  # R1
else:
    → 新興として採用（priority = "emerging")
```
- 追加の near-duplicate ガード（任意）: `recurrence` が低くても `nearest <= r_dup`（ごく小さい半径）なら「直前スレでほぼ逐語的に既出」とみなして除外。
- 窓が空（初期スレ）なら全件採用に縮退。

### 3.4 mod.md 用エンティティ再出現（オプション・推奨）
意味的recurrenceに加え、`models` メタデータで補強する。
```
# 直近窓のモデル出現スレ数を集計
model_df = {}   # model_name -> set(thread_num)
for rec in collection.get(where={"thread_num": {"$in": recent_threads}}):
    for m in split(rec.meta["models"]):
        model_df.setdefault(norm(m), set()).add(rec.meta["thread_num"])

# チャンクの主モデルが飽和していれば除外、窓に初出なら新規ブースト
```
- `norm()` は大小・表記ゆれの正規化（例 `Anima/anim/Anim` を束ねる）。`models` 値が既にゆれ表記を含むため、その範囲で集約。
- 効果: 「新モデルだけ」をほぼ決定論的に抽出。Animaのような定番モデルは確実に除外。

### 3.5 LLM 凝縮段（既存 `summarize_novel_topics` を踏襲）
- 役割は **凝縮のみ**（選別はしない。改訂2の方針）。
- 入力に priority（new / emerging）を付与し、「新登場」「直近で話題化」のような温度感ある表現を許可。
- 異常時（空・極端に短い・API例外）は決定論整形 `format_novel_topics` にフォールバック。

---

## 4. 設定（環境変数）

既存の `CHROMA_PREFILTER*` に倣う。未設定時は安全側（後述の互換モード）で動作させる。

| 変数 | 意味 | 既定（案） |
|---|---|---|
| `NOVELTY_MODE` | `recurrence`（新）/ `legacy`（現行の単純距離） | `legacy`（段階導入）|
| `NOVELTY_WINDOW` | 直近窓スレ数 N | 6 |
| `NOVELTY_RADIUS` | トピック一致半径 r | sum/mod=0.15, tools=0.08（要調整）|
| `NOVELTY_SATURATION` | 飽和比率 SAT（0〜1） | 0.5 |
| `NOVELTY_DUP_RADIUS` | near-dup 除外半径（任意） | 0.05 |
| `NOVELTY_ENTITY_MOD` | mod.md でエンティティ再出現を併用 | true |

> r / SAT / N はファイル別に最適値が異なる可能性が高い。§6 の検証で実測して既定値を確定する。

---

## 5. 後方互換・移行

- `NOVELTY_MODE=legacy`（既定）の間は現行の単純距離判定を維持。`recurrence` に切替えて段階導入。
- store_to_chroma は id upsert で冪等。再実行時の「事前にスレを削除」運用は recurrence モードでは不要（自己マッチが構造的に起きないため）。
- 既存の関数 `format_novel_topics`（決定論整形）・`summarize_novel_topics`（LLM凝縮）はそのまま再利用。新規判定部分（`process_new_topics_for_thread` 内のクエリ＋閾値）だけ差し替える。

---

## 6. 検証計画（実装前のプロトタイプ）

本実装に入る前に、過去スレでオフライン検証して r / SAT / N を決める。

### 6.1 データ
- 検証対象: 直近の連続スレ（例 654〜659）。各スレの sum/mod/tools。
- 各スレ S を評価する際、窓は「S より前のスレのみ」で構成（リーク防止）。

### 6.2 指標
- **Anima抑制率**: 定常トピック（Anima等の既知の定番）が新規欄に出ない割合。
- **新規再現率**: 既知の新トピック（例 659: Ideogram4, seedance2.0, Gemma4）が採用される割合。
- **digest件数**: 採用チャンク数（過多/過少のバランス）。
- legacy版との差分（どのチャンクが新たに除外/採用されたか）。

### 6.3 出力
- パラメータ格子（N×r×SAT）に対する上記指標の表を `docs/distance_redesign/03_eval_results.md` に記録。
- 既定値を確定し、本ドキュメント §4 を更新。

---

## 7. リスクと留意点

- **半径 r の感度**: 広すぎると別トピックを同一視して過剰除外、狭すぎるとAnimaの言い換えを取りこぼす。検証で確定必須。
- **窓 N の感度**: 小さいと数スレ周期の話題がフラップ、大きいと「再燃した旧話題」を新規と見なしにくくなる。
- **エンティティ正規化**: `models` の表記ゆれ集約が不完全だと飽和判定が緩む。mod.md限定の補助なので影響は限定的。
- **クエリ件数 K**: 窓内近傍を取りこぼさない十分な K が必要（窓内チャンク総数次第）。必要なら `collection.get(where=...)` で窓内全件を取り、ローカルで距離計算する方式も検討。
- **コレクション規模**: 現状 数千件規模。窓フィルタクエリの追加コストは無視可能。

---

## 8. 作業ステップ（想定）

1. [ ] プロトタイプ・スクリプトで §6 のオフライン検証（legacy vs recurrence）。
2. [ ] r / SAT / N の既定値確定、§4 更新、結果を `03_eval_results.md` に記録。
3. [ ] `distance.py` に recurrence モードを実装（env切替・legacyフォールバック維持）。
4. [ ] mod.md エンティティ再出現の併用（オプション）。
5. [ ] 直近スレで本番相当の出力を目視確認。
6. [ ] 既定 `NOVELTY_MODE=recurrence` へ切替（移行完了）。
