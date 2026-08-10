# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI（およびカスタムノード・ワークフロー）
- カスタムノード（sage attention、Spectrum、Turbo、Sol、effi、Kijaiノード、LMstudio/llama.cpp呼び出し系、ComfyUI-H3-Motion-Context、ref_image_size対応）

### ツール: Stability Matrix
- ComfyUI環境の構築・拡張機能インストールに使用
- 選ばれている理由: sage attention導入が比較的簡単で、複数UI管理や依存関係の扱いが容易

### ツール: Runpod（レンタルGPU）
- レンタルGPU選択肢として言及
- 選ばれている理由: 従量課金で試しやすいが、コマンド操作・ストレージ維持費・セットアップの手間・Windows Explorer非対応がネック

### ツール: その他のツール
- IrodoriTTS: 動画生成への音声組み込み・自動化用途
- OpenRouter / nanogpt / Deepseek API: プロンプト生成用外部LLM切り出し
- 選ばれている理由: ローカル運用より快適で、性能・価格のバランスが良い
- ffmpeg: フレーム補完による動画滑らかさ向上
- Tripo: 3Dモデル作成
- AntiGravity: 自作アプリ保守・エロ動画生成/評価用途
- 選ばれている理由: 評価がストレートで使いやすい
- ROCm（AMD GPU向け） / 複数GPU環境: AMD GPUユーザー向け環境構築

### ツール: 全体の傾向（選ばれている理由のまとめ）
- 日本語/細かい制御: TTSやプロンプト扱いのしやすさ

### ツール: Web検索による参考情報
- Sage Attentionノード: ComfyUI向けattention計算効率化・速度向上（2-5x程度）
- Stability Matrix: 複数AI UIのインストール・管理・拡張機能追加を簡略化するパッケージマネージャー/ランチャー
- IrodoriTTS: 日本語特化のFlow MatchingベースTTSモデル（ローカル実行可能、参照音声・感情制御対応）
- AntiGravity: agentic開発プラットフォーム/IDE（Gemini/Claude/GPT対応のAIエージェント機能）
- これらの情報は2026年8月時点の検索に基づく

---
# 元の本文
**ComfyUIを中心とした生成AI関連ツールのレポート**

提供されたテキストから抽出された主なツールは、**ComfyUI**（およびそのカスタムノード・ワークフロー・起動オプション）が圧倒的に中心となっています。モデル名（H3、Wan2.2、MiniMax、Anima、Qwen-Imageなど）は除外し、ツール・環境・運用関連の話題のみを対象としています。選ばれている主な理由は、**ワークフローの柔軟性・ノード単位の細かい制御・参照画像/動画の扱いやすさ・速度/VRAM最適化・JSONベースによるAI連携のしやすさ**です。

### 1. ComfyUI（およびカスタムノード・ワークフロー）
- **主な言及内容**: 
  - ワークフロー構築の主力環境。`H3 Motion Context`ノード、`Patch Sage Attention KJ`ノード、`load image batch`、`Model Preview Override`、`contact_sheet`、`qwen edit`、`Single frame edit basic`、`I2Vワークフロー`などのノード/機能が活用。
  - 起動オプション（`--fast-disk`、`--disable-pinned-memory`、`--cache-none`、`--reserve-vram`、`--enable-manager`）や最小化実行による高速化・安定化。
  - カスタムノード（sage attention、Spectrum、Turbo、Sol、effi、Kijaiノード、LMstudio/llama.cpp呼び出し系、ComfyUI-H3-Motion-Context、ref_image_size対応）。
  - アップデートによる速度向上事例（例: 低VRAM対策の`low vram attention` + `chunk feedforward`）。
  - ノード接続の複雑さをAI（Codex/Claude Code）に任せる運用。
- **選ばれている理由**:
  - ワークフローの柔軟性が高く、参照画像・動画を組み合わせた複雑な制御がしやすい。
  - ノード単位でSage Attentionなどの最適化をオン/オフ切り替え可能。
  - JSON形式のため言語モデルが理解・編集しやすく、新しいノードへの対応が容易。
  - シンプルなワークフローの方が高品質が出やすい傾向。
  - VRAM16GB環境での安定運用や速度短縮（動画参照時のリサイズなど）に強い。
- **その他の関連**: ComfyUI Managerのロード問題（`--enable-manager`必要）、diffusersとの使い分け（画面操作を避けたい場合の代替）。

### 2. Stability Matrix
- ComfyUI環境の構築・拡張機能（sage attentionなど）のインストールに使用。
- **選ばれている理由**: sage attention導入が比較的簡単で、複数UI管理や依存関係の扱いが容易。

### 3. Sage Attention（sage-attn / ApplySageAttentionノードなど）
- ComfyUIカスタムノードとして速度向上に活用（他の手法との併用/使い分け）。
- **選ばれている理由**: 速度が大幅に向上しつつ、質の劣化が少ない。質重視時は他をオフにする運用も。

### 4. LM Studio / LLM連携ツール
- ComfyUIと連携したプロンプト生成・自動化（バックグラウンド常時起動）。
- **選ばれている理由**: 手動unload不要で運用効率化。ローカルLLMをComfyUIワークフローに組み込みやすい。

### 5. Runpod（レンタルGPU）
- レンタルGPU選択肢として言及。
- **選ばれている理由 / 評価**: 従量課金で試しやすいが、「一番使いやすい」とされつつもコマンド操作・ストレージ維持費・セットアップの手間・Windows Explorer非対応などがネック。

### 6. その他のツール
- **IrodoriTTS**: 動画生成への音声組み込み・自動化用途。
  - **選ばれている理由**: 日本語対応のローカルTTSとして、動画ワークフローとの統合が求められる。
- **OpenRouter / nanogpt / Deepseek API**: プロンプト生成用外部LLM切り出し。
  - **選ばれている理由**: ローカル運用より快適で、性能・価格のバランスが良い。
- **ffmpeg**: フレーム補完（例: 24fps→48fps）による動画滑らかさ向上。
- **Tripo**: 3Dモデル作成。
- **AntiGravity**: 自作アプリ保守・エロ動画生成/評価用途。
  - **選ばれている理由**: 評価がストレートで使いやすい。
- **ROCm（AMD GPU向け） / 複数GPU環境（ライザーケーブル + PCIeスプリッター）**: AMD GPUユーザー向け環境構築。
- **Codex / Claude Code**: ノード接続・UI作成・プロンプト生成の自動化。スマホ用UI作成事例あり。
- **webUI**: 内部処理の例として1回のみ言及（積極的活用はなし）。

### 全体の傾向（選ばれている理由のまとめ）
- **速度・安定性・VRAM管理**: 起動オプション、最小化実行、最適化ノードの組み合わせが重視（16GB環境対応）。
- **柔軟性・制御性**: ComfyUIのノード/ワークフロー中心。参照機能やAI連携の強み。
- **運用効率化**: LLM連携やカスタムノードによる自動化。
- **日本語/細かい制御**: TTSやプロンプト扱いのしやすさ。

## Web検索による参考情報
- **ComfyUI v0.31.0**（2026年8月7日頃リリース）：MiniMax H3 VAE関連の修正（int8_convrot対応含む）、メモリ最適化（Linux swapなし環境でのpinned memory抑制）、新モデルサポート追加。VRAM/速度関連の改善が確認される。[[1]](https://freedom.tech/posts/2026-08-08-comfyui-0-31-0/)
- **Sage Attentionノード**: ComfyUI向けにApplySageAttentionなどのカスタムノードが存在し、attention計算の効率化・速度向上（2-5x程度の報告あり）で活用。Triton/SageAttentionインストールが必要な場合が多い。[[2]](https://www.runcomfy.com/comfyui-nodes/ComfyUI-Lightning/apply-sage-attention)
- **Stability Matrix**: ComfyUIを含む複数AI UIのインストール・管理・拡張機能追加を簡略化するパッケージマネージャー/ランチャー。依存関係やプラグイン管理が容易。[[3]](https://github.com/LykosAI/StabilityMatrix)
- **IrodoriTTS**: 2026年頃に登場した日本語特化のFlow MatchingベースTTSモデル（ローカル実行可能、参照音声・感情制御対応）。ComfyUIなどへの統合事例が見られる。[[4]](https://github.com/Aratako/Irodori-TTS)
- **AntiGravity**: Googleが2025年に公開したagentic開発プラットフォーム/IDE（Gemini/Claude/GPT対応のAIエージェント機能）。コード保守やタスク自動化に用いられる。[[5]](https://antigravity.google/blog/introducing-google-antigravity)

これらの情報は2026年8月時点の検索に基づきます。
