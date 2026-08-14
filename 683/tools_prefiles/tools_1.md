**抽出結果（ツール関連のみ）**

### 1. ComfyUIのインストール・運用形態の比較
- **venv版 / portable版**
  - 最新の対応が早い
  - カスタムノードや新機能への追従が速い
  - ギップル（？）に聞けば全部教えてくれる
- **stabilitymatrix版**
  - インストールが一番簡単
  - 昔はトラブルがあったが現在はほぼない
  - ComfyUI本体が比較的まともに管理されている
- **desktop版**
  - ComfyUI本体が比較的安定してきている
- **全体の傾向**
  - 「どれでもいいけど最新対応の速さ」でvenv/portableを選ぶ人が多い
  - stabilitymatrixは「楽に始めたい人向け」と評価されている

### 2. ComfyUI内の高速化・最適化ツール
- **Sage Attention / Kitchen Attention**
  - 実行時間の比較検証が行われており（17.80s vs 17.58s）、微差でSage Attentionの方が速いケースも報告
  - `--use-ck-attention`オプションとの併用検証も行われている
- **comfy-kitchen**
  - 「これだけで十分」という声あり（高速化ノードを他に探さなくなった）
- **spectrum（contex loop系）**
  - 一時期使っていたがcontext loopで使えないため早々に離脱したという報告
- **Adaptive Cache系ノード**
  - まだ知名度が低いが効果があるという指摘
- **Patch Sage Attention / Memory Efficient Sage Attention Patch**
  - 有効/無効での速度比較が行われている

### 3. ワークフロー構築・管理ツール
- **stabilitymatrix**
  - ComfyUIのインストールだけでなく、全体の管理のしやすさで評価
- **runpod**
  - 5090を借りて生成を試した報告あり
  - network volumeの転送速度が遅いという欠点も指摘

### 4. その他ツール関連の言及
- **Anima LoRA Factory**
  - GPTと連携させて学習を行うツールとして言及（モデル自体ではなく学習環境としての言及）
- **GGUF関連**
  - Unet Loader (GGUF) ノード
  - 現在は非推奨という意見が多数（重くて遅くなるため）

### 5. Qwenシリーズ（画像生成以外）
- **Qwen3.6 / Qwen3vl（LLM/TE用途）**
  - LLMとして「Gemma4 / Qwen3.6」と併記して使われている
  - TE（Text Encoder）としての使用（qwen3vl_32b_minimax_h3_int8_convrot vs bf16の比較）
  - 画像生成以外の用途（主にプロンプト生成やTE強化）として話題に上がっている

**補足**
- モデル名（Anima, H3, LTX, Z-Imageなど）の性能比較や話題はすべて除外
- ツールとして「なぜそのツールを選んでいるか」の理由が明記されているものを優先して抽出
- ComfyUI関連のインストール形態と高速化ノードの選定理由が最も多く語られていた