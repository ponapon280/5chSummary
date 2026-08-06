# 🆕 新規トピック（前回からの差分）
### モデル: MiniMax H3（MiniMax H3 / H3 / minimax_h3 / Hailuo 3.0）
- 話題量が非常に多く、ログの中心
- 動画生成（t2v/i2v/ref2v）で多用され、参照機能・動きの自然さ・日本語プロンプト対応・音声/口パク再現・LoRA親和性が評価
- 高速化技術（Sage Attention、Sol-Attn、Spectrum/H3Cache、TurboLoRA/int8量子化など）と組み合わせた実用運用が活発
- NSFWではSexGod系LoRA併用が標準的
- リファレンス能力が高く、複数画像によるキャラ一貫性やシーン転換が安定
- プロンプト追従性が高く、細かい指示（セリフ・タイミング・カメラワーク・複雑動作）を実現しやすい
- エロ/過激表現への適性が高く、LoRAとの相性が良い
- 実用的な生成速度・画質バランス（低ステップでも見栄えが良く、長尺対応）
- ローカル（ComfyUI）での運用しやすさ

### モデル: Wan（Wan2.1 / Wan2.2 / WAN）
- 話題量は中程度（過去モデルとして）
- 以前の主力モデルで、Sage Attentionノードやワークフローの流用、過去のエロ動画生成経験が現在のMiniMax運用に活かされている
- 高速化LoRAなしでも実用範囲だった点が回顧される
- 既存ワークフロー/ノード資産の流用しやすさ（現在はMiniMaxへ移行中）

### モデル: LTX（LTX-2.3 / ltx2.3）
- 話題量が多い
- VAEエンコードを活用した音声リップシンクワークフローが特に評価され、動画生成用途で頻出
- リップシンク性能の優位性（直接エンコード手法）

### モデル: その他のモデル
- NovelAI (NAI / NAI5): 日本語フォント性能の高評価。新バージョン（V5）への期待あり。参照素材用途の前評判
- SexGod / PinkFluffyBunny（Naughty Times LoRAなど）: MiniMax向けNSFW特化LoRAとして高評価（削除リスクの話題も）
- Gemma4 / Grok / Claude Opusなど: 主にMiniMax向けプロンプト作成ツールとして活用

### モデル: Web検索による参考情報
- MiniMax H3: MiniMax（旧Hailuo）社の2026年頃リリースのオープン/マルチモーダル動画生成モデル。テキスト・画像・動画・音声入力を統合的に扱い、ネイティブ2K解像度、5–15秒クリップ、ステレオ音声対応、リファレンス機能が特徴。APIやローカル運用で利用可能
- LTX-2.3: Lightricks社のオープンソース動画モデル（2026年3月頃）。VAE改善による高精細化、プロンプト追従強化、ネイティブ音声対応。ローカル実行可能
- Wan2.1 / Wan2.2: Wan AI（中国系）の大規模オープン動画生成モデル。MoEアーキテクチャ採用で複雑動作・審美性向上。720p/24fps対応、ComfyUIなどでローカル運用例多数
- NovelAI (NAI): Anlatan社のサブスクリプション型AIサービス。画像生成モデルはV4.5が最新公開版で、V5は未リリースまたは計画段階の言及多数。日本語対応やキャラ参照機能が強み
- 検索結果は2026年8月時点の公開情報に基づく。ログ内の「H3」「Wan2.2」などはこれら実在/公開モデルと一致する文脈で語られている

---
# 元の本文
**レポート: 生成AIモデルに関する話題のまとめ（ログ抽出ベース）**

**冒頭まとめ：流行しているモデル**  
ログ全体を通じて、**MiniMax H3（MiniMax H3 / Hailuo 3.0相当）**が圧倒的に中心的な話題となっており、現在最も活発に使用・議論されているモデルです。参照画像/動画/音声との親和性、プロンプト追従性（特に日本語）、NSFW表現のしやすさ、長尺生成の実用性などが高く評価され、「Sora2級」「実用レベル」との声が複数見られます。過去の主力モデル（Wan2.1/2.2、LTX-2.3、Animaなど）は、ワークフロー資産や知見の源泉、補助ツールとして言及されるにとどまり、移行先としてMiniMax H3が主流となっています。NSFW用途ではSexGod/PinkFluffyBunny系LoRAとの組み合わせが頻出です。[[1]](https://platform.minimax.io/docs/guides/video-generation)[[2]](https://www.krea.ai/models/minimax-h3)

### 1. MiniMax H3（MiniMax H3 / H3 / minimax_h3 / Hailuo 3.0）
- **話題の量**: 非常に多い（ログの中心）。
- **主な内容**: 動画生成（t2v/i2v/ref2v）で多用。参照機能の強さ、動きの自然さ、日本語プロンプト対応、音声/口パク再現、LoRA親和性が評価。高速化（Sage Attention、Sol-Attn、Spectrum/H3Cache、TurboLoRA/int8量子化など）と組み合わせた実用運用が活発。NSFWではSexGod系LoRA併用が標準的。
- **選ばれている理由（ログ内）**:
  - リファレンス能力が非常に高く、複数画像でキャラ一貫性やシーン転換が安定。
  - プロンプト追従性が高く、細かい指示（セリフ、タイミング、カメラワーク、複雑動作）を実現しやすい。
  - エロ/過激表現への適性が高く、LoRAとの相性が良い。
  - 実用的な生成速度・画質バランス（低ステップでも見栄えが良い、長尺対応）。
  - ローカル（ComfyUI）での運用しやすさ。

### 2. Wan（Wan2.1 / Wan2.2 / WAN）
- **話題の量**: 中程度（過去モデルとして）。
- **主な内容**: 以前の主力モデル。Sage Attentionノードやワークフローの流用、過去のエロ動画生成経験が現在のMiniMax運用に活かされている。高速化LoRAなしでも実用範囲だった点が回顧される。
- **選ばれている理由**: 既存ワークフロー/ノード資産の流用しやすさ（現在はMiniMaxへ移行中）。

### 3. LTX（LTX-2.3 / ltx2.3）
- **話題の量**: 多い。
- **主な内容**: VAEエンコードを活用した音声リップシンクワークフローが特に評価。動画生成用途で頻出。
- **選ばれている理由**: リップシンク性能の優位性（直接エンコード手法）。

### 4. Anima
- **話題の量**: 少なめ～中程度。
- **主な内容**: 画像生成・LoRA適用用途。テキストエンコーダー変更（Qwen系へ）や、手軽な生成速度が言及。MiniMaxとの組み合わせ例あり。
- **選ばれている理由**: LoRAの適用しやすさ・カスタマイズ性、手軽さ・速度面。

### 5. Qwen系（Qwen-Image / Qwen3-VL / Qwen3.5など、TE/LLM用途）
- **話題の量**: 少なめ。
- **主な内容**: MiniMax H3向けText Encoder（heretic/検閲解除版）やプロンプト生成LLMとして使用。
- **選ばれている理由**: NSFW強化（性器描写など）や性能向上のためのTE置き換え、プロンプト作成用途。

### 6. その他のモデル
- **NovelAI (NAI / NAI5)**: 日本語フォント性能の高評価。新バージョン（V5）への期待あり。参照素材用途の前評判。
- **Illustrious (リアス / ill / IL)**: 過去の使用経験（Forgeなど）からの移行事例。
- **FLUX**: 大型エロ派生モデル（SexGod/10Eros系）のサイズ・性能議論。
- **SexGod / PinkFluffyBunny（Naughty Times LoRAなど）**: MiniMax向けNSFW特化LoRAとして高評価（ただし削除リスクの話題も）。
- **Gemma4 / Grok / Claude Opusなど**: 主にMiniMax向けプロンプト作成ツールとして活用。

**選ばれている理由の全体傾向**  
MiniMax H3が現在の主流で、「参照制御性」「プロンプト理解度」「NSFW/LoRA相性」「実用速度」が主な選定理由。過去モデル（Wan、LTX、Anima）は「資産流用」や「特定機能（リップシンク・手軽さ）」で残存。高速化パッチの品質劣化（特に音声）を許容するかが運用上の判断材料となっています。

## Web検索による参考情報
- **MiniMax H3**: MiniMax（旧Hailuo）社の2026年頃リリースのオープン/マルチモーダル動画生成モデル。テキスト・画像・動画・音声入力を統合的に扱い、ネイティブ2K解像度、5–15秒クリップ、ステレオ音声対応、リファレンス機能が特徴。APIやローカル運用で利用可能。[[1]](https://platform.minimax.io/docs/guides/video-generation)[[3]](https://www.minimax.io/blog/minimax-h3)
- **LTX-2.3**: Lightricks社のオープンソース動画モデル（2026年3月頃）。VAE改善による高精細化、プロンプト追従強化、ネイティブ音声対応。ローカル実行可能。[[4]](https://ltx.io/model/ltx-2-3)[[5]](https://en.wikipedia.org/wiki/LTX_(text-to-video_model))
- **Wan2.1 / Wan2.2**: Wan AI（中国系）の大規模オープン動画生成モデル。MoEアーキテクチャ採用で複雑動作・審美性向上。720p/24fps対応、ComfyUIなどでローカル運用例多数。[[6]](https://github.com/Wan-Video/Wan2.2)[[7]](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- **Anima**: CircleStone Labs / Comfy Org共同の2Bパラメータアニメ特化テキスト-to-画像モデル。Qwen系TE使用、ComfyUIネイティブ対応。[[8]](https://docs.comfy.org/tutorials/image/anima/anima)[[9]](https://huggingface.co/circlestone-labs/Anima)
- **NovelAI (NAI)**: Anlatan社のサブスクリプション型AIサービス。画像生成モデルはV4.5が最新公開版で、V5は未リリースまたは計画段階の言及多数。日本語対応やキャラ参照機能が強み。[[10]](https://www.reddit.com/r/NovelAi/comments/1qr9l0z/when_nai_diffusion_v5/)[[11]](https://novelai.net/v4)

（検索結果は2026年8月時点の公開情報に基づく。ログ内の「H3」「Wan2.2」などはこれら実在/公開モデルと一致する文脈で語られている。）
