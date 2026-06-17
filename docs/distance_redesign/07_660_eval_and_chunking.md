# 660スレ 新旧比較・しきい値・チャンク粒度の検証と方針決定

> 作成日: 2026-06-17
> 関連: [05_impl_validation.md](./05_impl_validation.md), [06_maturity_ratio.md](./06_maturity_ratio.md)
> 成果物: `test/comparison*.md`, `test/chunk_granularity_experiment.md`, `test/*.py`

本番切替の判断材料として、実スレ 660 で旧版/新版の比較、しきい値追試、チャンク粒度の検証を行った。結論として **「チャンカーは行単位を維持し、精度改善は辞書カバレッジで行う」** 方針を採用する。

---

## 0. 検証セットアップ

- 660（url: liveuranus/1781360913）を取得→reducing→分割→summarize し、`summarize/660/{sum,mod,tools}.md` を生成。
- **`store_to_chroma` は実行せず**、660 をDB未投入のままにした。これにより旧版/新版とも比較対象は ≤659 となりリークが無い。
- 旧版＝`distance.py`（全履歴・最近傍距離 > 閾値: sum/mod=0.07, tools=0.02）。
- 新版＝`novelty_filter.py`（エンティティ全履歴DF）。凝縮段（`summarize_novel_topics`）は両者共通で、**選択方式の差のみ**を比較。

---

## 1. 旧版 vs 新版（maturity=0.40）

| ファイル | 総チャンク | 旧版 採用 | 新版 採用 |
|---|---|---|---|
| sum.md | 15 | 14 | 7 |
| mod.md | 8 | 4 | 3 |
| tools.md | 11 | 11 | 8 |

質的評価:
- **mod.md は新版の明確な勝ち**。旧版は定番 Anima を「台頭」「まとめ」として誤って新規化。新版は Anima を抑制し、実際に新しい LTX / SCAIL-2 / Ideogram 4 のみを残した。
- **tools.md は概ね良好**。PixAI・nano-banana・ffmpeg 等の新ツールを保持しつつ、Forge Neo（Forgeが定番）と Gemma4 併記の補足を抑制。
- **sum.md でトレードオフが顕在化**。Anima評価・LoRA学習などの定番ベースを抑制（良い）一方、「他モデル比較（PixAI/SCAIL-2/Wan/LTX/Rias）」チャンクも落ちた。**新情報(PixAI/SCAIL-2)と定番(Wan/LTX)が同一チャンクに同居**したのが原因。

---

## 2. しきい値追試（NOVELTY_MATURITY_SUM/TOOLS = 0.45 / 0.50, mod=0.40据置）

| ファイル | 旧版 | 新@0.40 | 新@0.45 | 新@0.50 |
|---|---|---|---|---|
| sum.md | 14 | 7 | 7 | 7 |
| mod.md | 4 | 3 | 3 | 3 |
| tools.md | 11 | 8 | 8 | 9 |

**所見: しきい値は混在チャンク問題の有効なレバーではない。**
- sum.md は 0.50 でも 7 のまま変化なし。落ちている「PixAI/SCAIL-2 比較」チャンクは、同居する **Wan/LTX/Anima/illustrious（DF 0.8〜0.98）** が平均を押し上げ、平均DF ≥ 0.50 のため救済不可。
- tools.md は 0.50 で +1 だが、救済されたのは「LM Studio×Gemma4 補足」で、狙った **Forge Neo は0.50でも抑制のまま**（Forge DF0.88）。
- 超定番（DF>0.8）が同居する限り、しきい値を上げても平均が下がらない。

---

## 3. チャンク粒度の検証

現行は「1行＝1チャンク」（低コスト・最近傍距離方式で細粒度の利得が無かった経緯）。660 で 行 / 文(。) / 節(。、) 単位の採否を比較した（maturity=0.40, LLM不使用）。

**sum.md**
| 粒度 | 採用単位 | 除外単位 | 救済された注目新情報 |
|---|---|---|---|
| line（現行） | 7 | 8 | なし |
| sentence（。） | 12 | 13 | なし |
| clause（。、） | 28 | 20 | PixAI, Rias, Tsubaki |

**tools.md**
| 粒度 | 採用単位 | 除外単位 |
|---|---|---|
| line | 8 | 3 |
| sentence | 14 | 6 |
| clause | 28 | 9 |

**所見: 細分化は大きな精度向上の手段にならない。**
- **文単位（。）では救済ゼロ**。混在は「`SCAIL-2は…、Wanは…、LTXは…`」のように1文内に読点で複数モデルが並ぶ形のため、句点分割では分離できない。
- **節単位（。、）でようやく一部救済**（PixAI/Rias/Tsubaki）だが、**採用単位が約4倍に爆発**（7→28, 8→28）。これは (a) store時の埋め込み・GiNZA抽出のコスト増、(b) digest断片化によるR1（簡潔性）の悪化、を招く。しかも救済は不完全・不安定（SCAIL-2やtools対象は節単位でも拾えない）。

---

## 4. 根本原因と方針決定

### 根本原因は「粒度」ではなく「辞書カバレッジ」
混在チャンクで新情報が落ちるのは、**新エンティティが辞書未登録で不可視 → 同居する定番だけが認識される**ため。
- 例: PixAI が辞書にあれば歴史的DF≈0 がチャンク平均を押し下げ、**粒度を変えずに同じチャンクが採用される**（`mean(PixAI=0, Anima=0.45)=0.23 < 0.40`）。
- これは既存の仕組み（`csv/*_additions.csv` ＋ `flooding_detect.py`）で、**コスト増なし・digest品質維持**のまま対処できる。

### 決定（2026-06-17）
1. **チャンカーは現行の「行単位」を維持**。細分化は費用対効果が低いと実証された（§3）。
2. **精度改善は辞書カバレッジで行う**。`flooding_detect.py` で未登録の高DFエンティティを定期抽出し、`csv/*_additions.csv` に追記する運用を主軸とする。
3. **MATURITY_RATIO は 0.40 を維持**。しきい値調整は混在チャンクに無力（§2）であり、上げると定番ベースの取りこぼしが増えるだけ。
4. 混在チャンクの残存トレードオフ（新情報と定番の同居）は、辞書カバレッジ向上により逓減する見込みとして受容する。

---

## 5. 成果物
- `test/comparison.md` — 旧版 vs 新版@0.40（digest全文）
- `test/comparison_m045.md` / `test/comparison_m050.md` — しきい値追試
- `test/chunk_granularity_experiment.md` — 粒度検証
- `test/compare_660.py` / `compare_660_m045.py` / `compare_660_m050.py` / `chunk_granularity_experiment.py` — 再実行用スクリプト
- `summarize/660/{sum,mod,tools}.md` — 660本文（DB未投入）

## 6. 残課題（本番切替の最終判断用）
- `main.py` の `distance` → `novelty_filter` 切替（保留中。これが設計変更を有効化する最後の一手）。
- 切替後、初回数スレは新規欄を目視し、`flooding_detect.py` で辞書追記候補を確認する。
