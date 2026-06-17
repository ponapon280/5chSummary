# 実装（novelty_filter.py）の検証結果

> 作成日: 2026-06-15
> 対象: `src/novelty_filter.py`（mod=エンティティ`models`DF / sum,tools=キーワード`keywords`DF）
> 検証: 659 を dry-run（prior=<659 でリークなし）

## 結論サマリ

| ファイル | 採用方式 | 結果 | 評価 |
|---|---|---|---|
| mod.md | エンティティ（models）DF | 11→9採用（2除外） | ✓ 機能。Anima等の定番recapを抑制。ただし軽微な誤抑制あり |
| sum.md | キーワード（keywords）DF | 18→18採用（0除外） | ✗ **無効。何も抑制されない** |
| tools.md | キーワード（keywords）DF | 17→17採用（0除外） | ✗ **無効。何も抑制されない** |

## 1. mod.md（エンティティDF）= 機能する

- 除外された2件のうち1件は **「変化の少ないモデル（Anima、illustrious、NovelAI、FLUX、WAN、Qwen…）」** の定番recapチャンク。狙い通り（R2達成）。
- 残り1件は **PLaMo / LLM-jp** チャンクの誤抑制。原因: PLaMo/LLM-jp が `model_checked.csv`（MODEL_LIST）に未登録で、チャンク中の「Anima構文」だけが認識され、Anima(DF0.45)が定番判定されたため。
  - **対策**: 新モデルを `model_checked.csv` に追記する運用（このCSVは元々メンテ前提の辞書）。seedance / Fable 等は未登録でも「認識トークン無し→採用」になり問題ないが、PLaMoのように定番モデル名を併記すると誤抑制が起きる。

## 2. sum.md / tools.md（キーワードDF）= 無効

dry-run で **1件も抑制されず**、現状維持（全採用）と同じ結果になった。

**根本原因**: `keywords` メタデータの品質。`extract_metadata.py` のキーワード抽出は
```python
nouns = [token.text for token in doc if token.pos_ in ["NOUN","PROPN"] and len(token.text)>1]
metadata["keywords"] = list(set(nouns))[:5]   # ← set() で順序非決定 + 任意の5語
```
であり、**「GiNZAが拾った名詞の集合から任意の5語」** に過ぎない。`set()` の反復順序はプロセス毎に変わるため、

- 格納済みキーワードと、現チャンクの再抽出キーワードが一致しない
- 重要語ではなく偶発的な5語が選ばれる

→ DFを計算しても**ノイズ**にしかならず、定番チャンク（毎スレ繰り返す「スレッド概要」boilerplate等）を抑制できない。

## 3. 代替検証：sum/tools もエンティティDFにすると機能する

sum.md は store 時に `models` も抽出されており、tools.md は `tools`（curated TOOL_LIST）を持つ。これらの**エンティティ**フィールドでDF判定すると有効だった（maturity=0.4, dry-run 659）:

| ファイル | field | 結果 | 抑制された主なチャンク |
|---|---|---|---|
| sum.md | models | 18→13（5除外） | スレッド概要(boilerplate, LoRA1.0/Anima)、技術的知見のAnima/WAI/Mix・Qwen系、全体の空気感(Anima) |
| tools.md | tools | 17→14（3除外） | Forge Neo関連(ComfyUI0.98/Forge0.88)、まとめ |

- **sum.md**: 狙い通り boilerplate の「スレッド概要」や定番技術ベースを抑制。一部に新Tipsを含むが定番モデル名併記で誤抑制される borderline あり（LoRA Tips, Qwen/Gemma）。
- **tools.md**: Forge系（DF0.88で準定番）が抑制される。Forge Neo は「位置づけ変化」見出しの注目ツールでもあり、再燃・進化の扱いは要検討。

→ **キーワードDFよりエンティティ（models/tools）DFの方が一貫して有効**。理由は、エンティティ抽出が curated CSV による決定論的な部分一致であるのに対し、keywords は非決定的で任意の名詞だから。

## 4. 推奨

1. **mod.md**: エンティティ`models`DF を採用（実装済み・機能）。運用として `model_checked.csv` に新モデルを追記。
2. **sum.md / tools.md**: **キーワードDFは無効**のため、**エンティティDF（sum→`models`, tools→`tools`）へ切替**を推奨。
3. `MATURITY_RATIO` 既定 0.4（mod/sum）/ tools 0.4。borderline 誤抑制が気になる場合は 0.45〜0.5 へ上げて保守的に。
4. 「再燃トピック」（HiDream, Forge Neo 等、旧くからあるが再注目）の扱いは別途方針が必要（global-DFだけだと準定番として抑制されうる）。

## 未決事項

- sum/tools を キーワードDF のまま（実質フィルタ無効）にするか、エンティティDF へ切替えるか。
