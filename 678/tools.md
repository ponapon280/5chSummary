# 🆕 新規トピック（前回からの差分）
### ComfyUI（最も多く言及・中心ツール）
- 中心ツールとして最も多く言及されている
- プレビュー機能により生成前に確認でき失敗を減らせる

### Stability Matrix / Forge Neo（NeoForge）
- 2年以上のブランクがあるユーザー向けの簡単セットアップツール
- パッケージ管理が優秀で導入しやすくComfyUI移行後も運用しやすい

### Ostris（ai-toolkit）
- LoRA作成ツールとしてMiniMax対応で言及
- ローカル高スペック環境で短期間のLoRA学習が可能

### クラウド・外部ツール
- runpodが低スペック環境向けでComfyUIテンプレートによりA100を低価格で利用可能
- ローカル貧弱環境でもMiniMaxなどを快適に試せる
- Colab（irodoritts）は時間つぶしや簡単実験に適する

### 動画編集・音声処理ツール
- Davinci Resolveは本格動画編集・音声分離に使用
- トラック編集で音声分離がしやすくUltimate Vocal Removerの代替としても評価
- OBS + Lossless Scalingは動画保存・アップスケール/フレーム補完に用いる
- RTX Video Super Resolution / RTX Super Resolutionはブラウザ/動画の高解像度画質向上に有効
- Premiere / Maya / Blenderはプロ級映像制作の補完ツールとして活用

### その他のツール・ノード
- simpleComfyUIは旧バージョン固定用途に利用

### Web検索による参考情報
- ComfyUIのpinned memoryは高速ロードとメモリ効率向上に寄与
- Stability MatrixはComfyUIなどを一括管理できるオープンソースランチャー
- Ostris / ai-toolkitは拡散モデル向けLoRA学習スイートでMiniMax対応
- nano-bananaはAI画像生成・Image-to-Video向けクラウドサービス
- runpod + ComfyUIテンプレートはMiniMax H3向けに即時利用可能
- 情報は2026年8月時点の検索に基づく

---
# 元の本文
**生成AI関連ツールレポート（抽出テキストに基づく）**

抽出されたテキストは、主にローカル/クラウド環境での画像・動画生成（特にR2I/R2Vワークフロー）に関する議論から、モデル本体を除外したツール・ノード・ワークフロー関連の話題をまとめたものです。中心となるのは**ComfyUI**とそのエコシステムで、柔軟性・高速化・メモリ効率化が繰り返し評価されています。他にローカルLLMツール、クラウドGPU、動画編集ツールなどが挙げられています。以下に主なツールを整理し、選ばれている理由を明記します。

### 1. ComfyUI（最も多く言及・中心ツール）
ComfyUIはノードベースのワークフロー構築ツールで、カスタムノードの追加・更新が容易な点が特徴です。portable版や最新版の導入が簡易化されており、WF共有の活発さも強みです。

- **選ばれている主な理由**:
  - ワークフローの柔軟性が高く、画像/動画生成の細かい制御（サブグラフ/入れ子WF、ref接続、音声処理、フレーム抽出など）が可能。複雑な処理を整理・再利用しやすい。
  - 最新の高速化・メモリ効率化ノードを組み合わせやすい（例: MemoryEfficient Sage Attention Patch、Sol-Attn、Spectrum、EasyCache、H3Cache、pinned memory）。VRAM使用量低減や生成時間短縮（例: 4割削減事例）が実現し、低スペック環境や長時間生成でも安定。
  - プレビュー機能（Model Preview Override + taeh3.safetensorsなど）で生成前に確認でき、失敗を減らせる。
  - 公式推奨バージョンやGitHub情報が充実し、導入が容易（2年ブランクユーザー向け提案も）。ノード操作に苦手な人も「慣れる価値あり」と前向き。
  - RAM_DISK活用や自動RAM調整機能で、32GB RAM環境でも実用的。hf downloadコマンドとの併用で大容量ファイルの安定DLが可能。

- **具体的な活用例**: Sage Attention系パッチ + Spectrumの組み合わせ、Mel-Band RoFormerノード（音声分離）、rife（フレーム補間）、KJノード群、video inputノードなど。マルチGPU時はpinned memoryのON/OFF検証が必要。

### 2. Stability Matrix / Forge Neo（NeoForge）
- **主な言及**: 2年以上のブランクがあるユーザー向けの簡単セットアップツール。ComfyUIやForgeのインストール・管理を一元化。
- **選ばれている理由**: 導入のしやすさ（パッケージ管理が優秀）。ComfyUI移行後の運用で困りにくいが、「素のComfyUI/Forgeの方が簡単」という意見も。一部でForgeリアスからの移行ツールとして評価。

### 3. LM Studio
- **主な言及**: Gemma4（12B）やQwen3.5/3.6シリーズをローカルで動作させ、プロンプト生成やテキストエンコーダーとして使用。
- **選ばれている理由**: 日本語で自然な指示が可能で、公式プロンプトガイドをシステムプロンプトに組み込んで高品質・指定フォーマットのプロンプトを自動生成できる。Anima系ワークフローでの実験に適する。

### 4. Ostris（ai-toolkit）
- **主な言及**: LoRA作成ツール（特にMiniMax対応）。
- **選ばれている理由**: ローカル高スペック環境で短期間のLoRA学習が可能。早期対応により実用的。

### 5. クラウド・外部ツール
- **runpod**: 低スペック環境向け。ComfyUIテンプレート（ワンクリックでモデルDL対応）でA100などを$1.5程度で利用可能。
  - **選ばれている理由**: ローカル貧弱環境でも快適にMiniMax等を試せる。
- **Colab（irodoritts）**: 時間つぶしや簡単実験用。

### 6. 動画編集・音声処理ツール
- **Davinci Resolve**: 本格動画編集・音声分離に使用（姫騎士ニキ言及例あり）。
  - **選ばれている理由**: トラック編集で音声分離がしやすい。Ultimate Vocal Removerの代替としても言及。
- **OBS + Lossless Scaling（Steam）**: 動画保存・アップスケール/フレーム補完の組み合わせ。
- **RTX Video Super Resolution / RTX Super Resolution**: ブラウザ/動画プレイヤーでの高解像度向け画質向上（1080p以上推奨）。
- **Premiere / Maya / Blender**: プロ級映像制作の補完ツール（3Dコンテ作成など）。

### 7. その他のツール・ノード
- **Grok**: MiniMaxプロンプト作成補助（X連携でコスパ良く高品質）。
- **AG（Gemini/Opus系エージェント）**: エロプロンプトの自然な拡張・詳細化に強い（Opusの方が安定）。
- **nano-banana**: 画像生成後のI2V（画風維持に優位）。
- **Torrent（μtorrent/bittorrent）**: モデル共有・消去対策。
- **huggingface_hub + PowerShell curl.exe**: 大容量DLの安定性。
- **simpleComfyUI**: 旧バージョン固定用途（ただし最新効率化が反映されにくい）。

**全体の傾向**: ComfyUI推奨派が多く、Forge/ Stability Matrixは「覚えやすい/簡単」派向け。高速化ノード（Sage系、Spectrum、pinned memory）の存在やWF共有の活発さがComfyUIの優位性として挙げられています。低スペック対応やプロンプト品質向上ツールの併用も特徴です。

## Web検索による参考情報
- **ComfyUIのpinned memory**: 2025年頃にGitHubで高評価の機能として議論されており、ディスクからの高速ロード、RAM/VRAM利用効率向上に寄与。SageAttentionパッチ（KJNodesなど）と組み合わせたメモリ効率化ノードが複数存在し、VRAM削減・速度向上に用いられる。[[1]](https://github.com/Comfy-Org/ComfyUI/issues/10555)
- **Stability Matrix**: AIアート用オープンソースランチャー/マネージャー。ComfyUI、Automatic1111、Forge（Forge Neo含む）などを一括管理・インストール可能。共有モデルリポジトリやCivitAI連携が特徴。[[2]](https://lykos.ai/)
- **Ostris / ai-toolkit**: 拡散モデル向けLoRA学習スイート（GUI/CLI対応）。MiniMax H3など複数モデル対応で人気。RunPodテンプレートとしても提供されている。[[3]](https://github.com/ostris/ai-toolkit)
- **nano-banana**: AI画像生成・編集・Image-to-Videoツール（Nano Banana Pro/2など）。Gemini系エンジンとの関連が指摘され、画風維持の動画生成に適するクラウドサービスとして言及。[[4]](https://nanobananas.ai/)
- **runpod + ComfyUIテンプレート**: MiniMax H3などのモデル向けComfyUIテンプレートが公式に提供され、クラウドGPU（A100など）での即時利用が可能。[[5]](https://www.runpod.io/blog/minimax-h3-the-open-weight-omni-modal-video-model-and-what-it-takes-to-run-it)

これらの情報は2026年8月時点の検索に基づき、ツールの事実関係を確認したものです。
