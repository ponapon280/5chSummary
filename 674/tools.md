# 🆕 新規トピック（前回からの差分）
### ツール: 主な話題
- バージョンアップデートによる不具合（インペイントバグ、Autocomplete-Plus表示問題、動作重化）
- カスタムノードのバージョン追従遅れ
- Anima Base v1での日常使用やText-to-Imageテスト
- 領域制御（Forge Couple / Regional Prompterなど）
- Comfyとの比較（Forgeでできない場合のラグ）
- 背景の細かさ・実写寄り表現、3DCG風出力の強み
- LoRA作成時のベースとしての利用（アニメ・イラストキャラ学習）
- エロ表現の弱さ（特に二次元）

### ツール: 不満・課題
- UIの安定性低下（時間経過で重くなる、再起動で回復）

### ツール: 選ばれる理由
- 手軽な生成や即時性が高い場面
- 拡張機能による細かい領域制御のしやすさ
- 特定の画風・品質（人間の耳描写など）が優れている
- LoRA作成時のクオリティの高さ
- 3DCG寄りの出力が必要な場面で有用

### ツール: その他のツール
- AI-Toolkit: Krea2向けLoRA学習環境構築
- LMStudio / LLMStudio: APIサーバーとして画像バッチキャプショニングやエロプロンプト生成
- Cursor: AIコーディングツール
- 自作プロンプト変換ツール: NAIv4→v5対応
- クラウドAPI（Claude系など）: エロRP用途
- Codex: ブラウザ直ツール作成との比較

### ツール: 選ばれる主なポイント（全体）
- 柔軟なカスタマイズ・制御が必要 → ComfyUI
- 手軽さ・即時性 → Forge系
- 特定画風・LoRA学習品質 → Krea 2 + AI-Toolkit
- ローカルAPI化・バッチ処理 → LMStudio
- コーディング効率 → Cursor

### ツール: ## Web検索による参考情報
- Krea 2: Krea.ai提供の基礎画像生成モデル（美学・スタイル重視、機能多数、オープンソース推論コード公開）
- Forge Neo: sd-webui-forge-classicのneoブランチ（新機能サポート、メモリ管理・API安定性向上）

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出に基づく）**

ログから抽出された生成AIツール関連の話題は、**ComfyUI**を中心に集中しており、UIの安定性・拡張機能・ワークフローの柔軟性が主な焦点です。その他、Forge系webUI、Krea 2、LoRA学習ツール、LLMツール、AIコーディングツールなどが言及されています。モデル性能の話は完全に除外し、ツール・環境・ワークフロー関連のみをまとめます。

### 1. ComfyUI（comfy）
**主な話題**
- バージョンアップデート（0.27以前→最新版、0.28以降、0.29.2）による不具合：インペイントバグ、Autocomplete-Plusの表示問題（Whiteテーマ固定）、長時間使用時の動作重化・操作不能。
- カスタムノード（ImpactPack、rgthree、Autocomplete-Plusなど）のバージョン追従遅れ。
- ワークフロー管理：Bernini公式ワークフローの不親切さ、lightx2v用簡易r2vワークフローの共有、Wan2.2のネイティブサポート。
- Civitaiアップロード時のメタデータ復元挙動（シンプルなKSampler構成で復元可能、複雑ノード経由で不可）。
- 生成過程の視覚確認機能や、ドラッグ&ドロップによるワークフロー復元利便性。

**選ばれる理由**
- Forgeで未対応の機能や細かいノード制御が必要な場合に選択。
- ワークフローの柔軟性・編集機能（画像→動画編集など）。
- ネイティブサポートの速さ（Wan2.2初期のカスタムノード依存から脱却）。
- インストールの容易さ（10分程度）とカスタマイズ性（テンプレにノードを足すだけ）。

**不満・課題**
- UIの安定性低下（時間経過で重くなる、再起動で回復）。
- カスタムノードの追従遅れによるバージョン互換問題。

### 2. Forge / Forge Neo / easy forge neo（webUI系）
**主な話題**
- Anima Base v1での日常使用やText-to-Imageテスト。
- 領域制御（Forge Couple / Regional Prompterなど）や特定位置の非描写制御。
- Comfyとの比較（Forgeでできない場合のラグ）。

**選ばれる理由**
- 手軽な生成や即時性が高い場面。
- 拡張機能による細かい領域制御のしやすさ。

### 3. Krea 2（Krea 2 / Krea2系）
**主な話題**
- 背景の細かさ・実写寄り表現、3DCG風出力の強み。
- LoRA作成時のベースとしての利用（アニメ・イラストキャラ学習）。
- エロ表現の弱さ（特に二次元）。

**選ばれる理由**
- 特定の画風・品質（人間の耳描写など）が優れている。
- LoRA作成時のクオリティの高さ。
- 3DCG寄りの出力が必要な場面で有用。

### 4. その他のツール
- **AI-Toolkit**: Krea2向けLoRA学習環境構築。VRAM16GB環境でもRAM逃がし設定で学習可能（RAM96GB推奨）。
- **LMStudio / LLMStudio**: APIサーバーとして画像バッチキャプショニングやGemma4系（heretic/uncen版）のエロプロンプト生成に使用。ローカルでの手軽なAPI化とバッチ処理連携が容易。
- **Cursor**: AIコーディングツール。Grok4.5などの高性能モデルを安価に大量利用可能（トークン単価の安さ）。
- **自作プロンプト変換ツール**: NAIv4→v5対応のためユーザー作成。公式対応の遅れに対する自前対応。
- **lightx2v**: Wan2.2向けの高速画像/テキスト→動画ワークフロー。ComfyUIで利用され、蒸留LoRAによる高速化が特徴。
- **クラウドAPI（Claude系など）**: エロRP用途でローカルLLMより賢さ・利便性で優位。
- **Codex（推定コーディングツール）**: ブラウザ直ツール作成との比較で言及。

**選ばれる主なポイント（全体）**
- 柔軟なカスタマイズ・制御が必要 → ComfyUI
- 手軽さ・即時性 → Forge系
- 特定画風・LoRA学習品質 → Krea 2 + AI-Toolkit
- ローカルAPI化・バッチ処理 → LMStudio
- コーディング効率 → Cursor

### ## Web検索による参考情報
- **Krea 2**: Krea.aiが提供する独自の基礎画像生成モデル（Krea 2 / Krea 2 Medium / Krea 2 Large）。美学・スタイル重視で構築され、スタイル転送、ムードボード、クリエイティビティダイヤルなどの機能を持つ。オープンソース版の推論コードもGitHubで公開されており、独立系ラボとして高評価。[[1]](https://www.krea.ai/)[[2]](https://github.com/krea-ai/krea-2)
- **Forge Neo**: sd-webui-forge-classicのneoブランチとして提供されるStable Diffusion WebUIのフォーク。Wan 2.2、Nunchaku、Flux-Kontextなどの新機能サポートを追加。Classic版とは異なり最新Forgeベースで、メモリ管理や拡張APIの安定性を向上。[[3]](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)[[4]](https://www.reddit.com/r/StableDiffusion/comments/1n7fd2v/introducing_sdwebuiforgeneo/)
- **lightx2v**: Wan 2.2向けの蒸留LoRAおよびComfyUIワークフロー。8〜14ステップでの高速画像/テキスト→動画生成を実現するカスタムノード/ラッパーも存在。[[5]](https://www.runcomfy.com/comfyui-workflows/wan-2-2-lightx2v-v2-comfyui-workflow-fast-image-text-to-video)[[6]](https://github.com/ModelTC/ComfyUI-Lightx2vWrapper)

ComfyUI関連の具体的なバージョン0.29.2などの公式リリース情報は検索時点で直接確認できなかったが、ログ内の言及に基づきUI/ワークフロー改善の文脈で扱っています。
