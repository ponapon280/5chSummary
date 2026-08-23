# 🆕 新規トピック（前回からの差分）
### 生成AI関連ツールレポート
- 生成AI向けUI・ワークフロー・クラウド/ローカルツールを抽出・整理（モデル名除外）

### ComfyUI（および関連ノード・ワークフロー）
- ComfyUI関連ノード・ワークフローの各種言及を整理

### PixAI
- LoRA作成・R-18対応のWeb版ツールとして位置づけ
- PC非保有層向けクラウド高機能利用で選定

### nano-banana（Nano Banana）
- flowとAPIの挙動差・英訳補正の指摘を整理
- 最先端ツールとして文脈読み取りの自然さでAPI優位と評価

### MiniMax H3関連（minimaxH3_latentupscaler、ComfyUI-MiniMax-H3-Image-Studioなど）
- アップスケーラー・Ref2I機能・NAI素材との相性を言及

### Krea（Krea2 / Krea3）
- 少女画像生成・高品質期待のツールとして言及
- 品質・日本語表現の期待値の高さで選定

### その他のツール
- webUI / Forge Neoをadetailer定番ツールとして言及
- runpodを大量生成時のローカル負荷回避策として言及
- SageAttentionを高負荷時の安定性懸念で言及

### Web検索による参考情報
- nano-bananaをGemini系画像生成・編集モデルとして整理
- MiniMax H3をオムニモーダル動画生成モデルとして整理
- Krea (Krea2)を美学重視のテキスト-to-画像モデルとして整理
- 検索日時点の情報に基づく変動可能性を注記

---
# 元の本文
**生成AI関連ツールレポート**

提供されたテキスト（フォーラムログなどの抽出結果）から、生成AI（主に画像・動画生成向け）の関連ツールを抽出・整理しました。モデル名（NAI、Animaなど）は除外し、UI・ワークフロー・クラウド/ローカルツールに焦点を当てています。ツールが選ばれている理由が明記されている場合は明記しています。複雑なワークフローやAPI/ローカル比較の話題が多く見られました。

### 1. ComfyUI（および関連ノード・ワークフロー）
- **主な言及**: ComfyUI-MiniMax-H3-Image-Studio、Ref2VA/Ref2v/fl2va（画像参照動画生成）、アルファ化ノード（透過画像）、1F生成ノード、SAM3（adetailer代替）、ファイル名自動追記ノードなど。
- **選ばれている理由**:
  - VRAM/速度面の挙動が安定（prunedモデル使用時やGPU変更時でも「ComfyUIがよろしくやってくれる」）。
  - 専用ノードが充実（NAIちゃん用ノード更新、透過画像生成など）。
  - エラー対処のしやすさ（ChatGPTに構築させ、fable神にログ投げの2段構え）。
  - QIEより品質が高いワークフローとして評価。
  - 動き・構図制御が必要なRef2V系で活用。
- **その他の特徴**: 他人のワークフローはウイルスリスクが高いため自分で組む必要があり難易度高め。画面バグの報告あり。webUIのadetailerと並行して言及される定番ツール。

### 2. PixAI
- **主な特徴**: LoRA作成可能、Web版でR-18生成対応、NAIよりローカルに近い操作・機能を実現。
- **選ばれている理由**: PCを持っていない層にとって特に強い（クラウドで高機能が利用可能）。

### 3. nano-banana（Nano Banana）
- **主な言及**: flow（LLM補正が入る）とAPI（原文そのまま）の挙動差。flowの英訳/補正が「くっそ邪魔」との指摘。NAIとは路線が違い、巨大LLMによる整合性・解釈を活かした生成。
- **選ばれている理由**: 最先端ツールとしてGrok系で位置づけられ、文脈読み取りの自然さでAPIが優位。半年後ローカル/他クラウドが追いつくレベルと評価。

### 4. MiniMax H3関連（minimaxH3_latentupscaler、ComfyUI-MiniMax-H3-Image-Studioなど）
- **主な言及**: アップスケーラーとして使用（綺麗だが2倍で時間がかかる）。静止画版のRef2I機能期待。NAI素材との組み合わせ相性良し。
- **選ばれている理由**: Ref2I（画像参照）機能が強く、機能面で優位。静止画版が出たら動画とセットで覇権を取ってほしいとの期待。

### 5. Krea（Krea2 / Krea3）
- **主な言及**: 少女画像生成や高品質期待。Krea3リリース待ち。
- **選ばれている理由**: 品質や日本語表現の期待値が高い。

### 6. その他のツール
- **webUI / Forge Neo**: adetailerによる部分拡大・合成の定番。Forge Neo拡張の不具合報告あり。
- **Contex-Loop / Ref2Vワークフロー**: 動画生成（Ref2V）で使用。色ムラやLoRA切り替えの問題あり。複雑すぎて「AI先生に操作してもらう」ユーザーも。
- **runpod**: 大量生成時のローカルPC負荷回避に推奨。
- **LM Studio / llama-ui**: ローカルLLM用。llama-uiはMTP（推論高速化）で速度向上のため選択。
- **Local-Prompt-Studio v2.0**: プロンプト作成・管理用新バージョン。
- **SageAttention**: 高負荷時の安定性に懸念あり。

**全体の傾向**: クラウドツール（nano-banana、Krea、PixAI）の利便性・品質 vs ローカルツール（ComfyUI、webUI、llama-ui）の速度・カスタマイズ性の比較が目立つ。Ref2系参照機能やAPI/フローの挙動差が実用的な選定ポイント。

## Web検索による参考情報
- **nano-banana**: GoogleのGemini系画像生成・編集モデル/ツール（Nano Banana 2 / Nano Banana Proなど）。GeminiアプリやAI Studioで利用可能で、高品質画像生成・編集（特にin-context editing）に強い。SynthID透かし入り。[[1]](https://aistudio.google.com/models/nano-banana)[[2]](https://gemini.google/overview/image-generation/)
- **MiniMax H3**: MiniMax社のオムニモーダル動画生成モデル（Hailuo 3.0相当）。テキスト・画像・動画・音声を単一コンテキストで扱い、ネイティブステレオ音声付き2K動画（最大15秒）を生成。オープンウェイト版あり、ComfyUIでネイティブサポート（T2V/I2V/R2Vワークフロー）。Ref2I機能も関連。[[3]](https://www.minimax.io/blog/minimax-h3)[[4]](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- **Krea (Krea2)**: Krea.aiのクリエイティブAIスイートおよび同社製画像モデル（Krea 2）。美学重視のテキスト-to-画像モデルで、Krea 2 Turbo版なども存在。画像・動画・3D生成をサポート。[[5]](https://www.krea.ai/)[[6]](https://github.com/krea-ai/krea-2)
- **ComfyUI-MiniMax-H3-Image-Studio**: MiniMax H3をComfyUIで静止画生成・参照編集向けにカスタマイズしたノード/ワークフロー（GitHubリポジトリあり）。動画モデルを画像用途に適応させた実験的拡張。[[7]](https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio)
- **Local-Prompt-Studio**: プロンプト管理ツールの文脈で言及されたが、検索では類似のPrompt Studio系アプリ（Electronベースのプロンプト整理ツール）が見つかる程度。v2.0の具体的な新機能確認は限定的。

（検索日: 2026年8月時点の情報に基づく。モデル/サービスのバージョン・新機能は変動する可能性あり。）
