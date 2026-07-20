# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI（最も頻出）
- Schedule Promptノードによる画風・タグ混ぜワークフロー構築と0.28.0前後のバージョン互換性管理
- lllite・SeedVR2などのネイティブ機能対応およびcomfyui-rocmによるROCm・マルチGPU対応
- custom node依存低減・テンプレート充実・漫画作成ワークフロー完結・ゲームエンジン/マイコン連携
- テンプレートの充実により初心者でも始めやすい
- ROCm公式/サードパーティ対応が厚くsageattention等をまとめてインストール可能でRadeonユーザーの手間を軽減
- SeedVR2・llliteなど新機能のネイティブサポートが早く最新機能を使いやすい

### ツール: Stability Matrix
- Forge Neo / reForgeの管理・表示（NVIDIA/ROCm/macOS対応）とmodelsフォルダ問題・ROCmサポート拡大
- パッケージ管理が便利でForge Neoなどのインストール・切り替えがしやすい

### ツール: LoRA学習ツール群
- sd-scriptsは細かい制御が可能だがPyTorchバージョン問題（50XX系エラー）が出やすくトラブルシューティングが必要でAI支援によりハードル低下
- AI-Toolkitはオールインワンで心理的ハードルが低い一方Anima（二次元）対応の弱さがネック
- OneTrainerはプリセットが最も簡単で初心者向けハードルが最も低くLoRA alpha調整などのポイントも指摘
- 制御の細かさ・簡単さ・心理的負担の低さで使い分けられOneTrainerは特に一番簡単そうなプリセットとして選ばれやすい

### ツール: その他のツール
- comfyui-mcpによる指示ベースの自動化
- LLM補助ツール（Gemini・Kimi/Qwen・ChatGPT）によるエロプロンプト作成・ストーリー生成・ComfyUIトラブルシューティング
- ComfyUIはワークフロー柔軟性・機能強化・ROCm環境適合性で選好度が高く学習ツールは簡単さ vs 制御性のトレードオフで使い分け

### ツール: Web検索による参考情報
- ComfyUIはAMD ROCm公式サポートをWindows向けに強化しcomfyui-rocmリポジトリで公式ライブラリ＋Triton/Sage Attention等をまとめてインストール可能（RDNA1〜4対応）
- AMD公式ドキュメントでComfyUIのROCmインストール手順が公開されPyTorch ROCm wheels使用を推奨
- Stability MatrixはForge NeoをパッケージとしてサポートしWindows ROCm対応を拡大（Vega〜RDNA4）
- ComfyUI 0.28.0やllliteネイティブ対応の具体的な公式発表は検索時点で直接ヒットせずログ固有の進捗を示すものと解釈

---
# 元の本文
**生成AI関連ツールのレポート**

ログから抽出された生成AIツールは、主にStable Diffusion系画像/動画生成ワークフローとLoRA学習環境に集中しています。ComfyUIが圧倒的に言及が多く、ノードベースの柔軟性・ワークフロー制御性・最近のネイティブ機能強化により選ばれている点が特徴です。以下、ツールごとに概要・選ばれている理由（ログ記載のものがあれば明記）をまとめます。モデル名（Anima、Krea2など）は除外し、ツール関連のみを対象としています。

### 1. ComfyUI（最も頻出）
- **主な話題**: ワークフロー構築（Schedule Promptノードによる画風/タグ混ぜ）、バージョン管理・更新（0.28.0前後での互換性）、ネイティブ機能（lllite、SeedVR2対応）、ROCm対応（comfyui-rocm）、マルチGPU、custom node依存低減、テンプレート充実、漫画作成ワークフロー完結、外部連携（ゲームエンジン/マイコン）。
- **選ばれている理由**:
  - ワークフローの柔軟性と制御性（ノードベースで細かく調整可能）。
  - 本家ノードの充実によりカスタムノード依存が減り、学習難易度が低下・扱いやすくなった。
  - テンプレートが充実し、初心者でも始めやすい。
  - ROCm公式/サードパーティ対応が厚く（sageattention等をまとめてインストール可能）、Radeonユーザー向けにインストールの手間が省ける。
  - マルチGPU対応の進捗により生成速度向上・コスパが良い（特に2枚挿し環境）。
  - 新機能（SeedVR2、llliteなど）のネイティブサポートが早く、最新機能を使いやすい。

### 2. Forge / reForge / Forge Neo（webUI系）
- **主な話題**: 速度比較（Forge Neoが「早い」）、線質の違い（reForgeよりForge Neoの方が線が細い場合あり）、ROCm対応状況、Stability Matrix上での表示・管理。
- **選ばれている理由**: 速度と出力特性（線質）のバランスが良いためForge Neoを選択する事例あり。Stability MatrixでROCm表示があるため選ばれやすいが、公式対応の薄さが指摘されるケースも。

### 3. Stability Matrix
- **主な話題**: Forge Neo / reForgeの管理・表示（NVIDIA/ROCm/macOS対応）、modelsフォルダ問題、ROCmサポート拡大。
- **選ばれている理由**: パッケージ管理が便利で、Forge Neoなどのインストール・切り替えがしやすい。

### 4. LoRA学習ツール群
- **sd-scripts**: 細かい制御が可能だが、PyTorchバージョン問題（50XX系エラー）が出やすくトラブルシューティングが必要。AIによる環境構築支援でハードル低下。
- **AI-Toolkit**: オールインワンで「細かいことわからなくても全部やってくれる」ため心理的ハードルが低い。ただしAnima（二次元）対応の弱さがネック。
- **OneTrainer**: プリセットが最も簡単で、初心者向けにLoRA作成のハードルが最も低い。LoRA alpha調整などのポイントも指摘。
- **選ばれている理由**: それぞれ「制御の細かさ」「簡単さ」「心理的負担の低さ」で使い分け。OneTrainerは特に「一番簡単そうなプリセット」として選ばれやすい。

### 5. その他のツール
- **comfyui-mcp**: 指示ベースの自動化。
- **Schedule Promptノード**（ComfyUI内）: Anima環境での画風混ぜ方で「現時点で一番マシ」と評価。
- **LLM補助ツール**（Gemini、Kimi/Qwen、ChatGPT）: エロプロンプト作成、ストーリー生成、ComfyUIトラブルシューティング・解説。手軽な補助として活用。

全体として、**ComfyUI**はワークフロー柔軟性・機能強化・環境適合性（特にROCm）で選好度が高く、学習ツールは「簡単さ vs 制御性」のトレードオフで使い分けられています。バージョン更新による互換性問題やネイティブ対応の進展が実用性を高めている点がログの傾向です。

## Web検索による参考情報
- ComfyUIはAMD ROCm公式サポートをWindows向けに強化しており、comfyui-rocmリポジトリ（patientx-cfz/comfyui-rocm）で公式ROCmライブラリ使用＋Triton/Sage Attention等の最適化パッケージをまとめてインストール可能。RDNA1〜4対応のWindows専用ビルドとして提供。[[1]](https://github.com/patientx-cfz/comfyui-rocm)[[2]](https://www.youtube.com/watch?v=6LOqJdKe6zI)
- AMD公式ドキュメントでもComfyUIのROCmインストール手順が公開されており、PyTorch ROCm wheels使用を推奨。[[3]](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/windows/comfyui/installcomfyui.html)
- Stability MatrixはForge Neo（Stable Diffusion WebUI ForgeのNeoブランチ）をパッケージとしてサポートし、Windows ROCm対応を拡大（Vega〜RDNA4）。Forge Neoは速度向上版として別パッケージ化されている。[[4]](https://github.com/LykosAI/StabilityMatrix/releases)[[5]](https://www.youtube.com/watch?v=Oc_4OvRX3qI)
- Forge Neoはsd-webui-forge-classicのneoブランチとして開発・配布されており、Stability Matrix経由のインストール事例が多い。[[6]](https://github.com/LykosAI/StabilityMatrix/issues/1648)

（ComfyUI 0.28.0やllliteネイティブ対応の具体的な公式発表は検索時点で直接ヒットせず、ログ固有のバージョン/機能進捗を示すものと解釈。OneTrainer/AI-Toolkit/sd-scriptsはLoRA学習ツールとして一般的に知られるが、詳細比較はログの主観に基づく。）
