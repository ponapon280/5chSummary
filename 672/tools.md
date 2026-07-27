# 🆕 新規トピック（前回からの差分）
### ツール: Forge / ForgeNeo / EasyForgeNeo（Automatic1111系webUI）
- Anima Edit LoRAの二重強度指定やLow Bits設定、Denoising Strength=1.0などのTips共有
- forge coupleの効きにくさやDynamicPromptの不具合報告
- Animaとの相性の良さやLoRA強度調整の細かさが評価される一方、DynamicPrompt制限でComfyUI移行のきっかけにも

### ツール: ComfyUI（ワークフロー / カスタムノード / 運用）
- サーバー運用向きの仕様とAnima/Krea2向けワークフローの豊富さ
- Docker相性、VRAM管理ノード、クリスタ直接送り、webp保存、特定カスタムノード活用例
- 複数インスタンス分離によるカスタムノード競合回避

### ツール: sd-scripts（kohya）
- subsetごとのtimestepずらし新機能追加とtoml設定での利用
- 手間が少なくtimestep offsetによるLoRA品質向上を評価

### ツール: nano-banana
- Qwen Image Edit機能との比較で独立した使い勝手の良さを評価
- 直感的で自然なEdit機能と複雑構図生成の柔軟性が注目

### ツール: その他の学習・生成ツール
- OneTrainerをKrea2 LoRA作成に使用し、Hugging Faceキャッシュ重複事例あり
- VACE Prepによる複数動画結合処理

### ツール: 環境・運用関連ツール
- Linux + Docker / WSL2をComfyUIサーバー運用に推奨し、依存管理・再現性・リモート性を重視
- ComfyUIが最も言及され、Forgeからの移行先や高機能運用ツールとして位置づけ

### ツール: Web検索による参考情報
- ComfyUI + Docker/WSL2の運用事例とGPUパススルー・依存管理の利点
- sd-scriptsのtimestep関連機能とtoml設定の柔軟性
- nano-bananaのGeminiアプリ内画像編集機能の特徴
- OneTrainerのGUI搭載LoRA/ファインチューニングツールとしての位置づけ

---
# 元の本文
**生成AI関連ツールレポート（ツール・運用関連のみ抽出）**

本レポートは、提供されたテキストからモデル名・性能議論を除外し、画像生成・学習・運用に用いられるツール・環境・ワークフローツールを中心にまとめました。各ツールの言及内容と選ばれている主な理由を記載しています。モデル名・バージョン・新サービス等についてはweb検索で事実確認を行い、末尾に参考情報をまとめています。

### 1. Forge / ForgeNeo / EasyForgeNeo（Automatic1111系webUI）
- **言及内容**: Anima Edit LoRAの二重強度指定（`<lora:AnimeEditV2:1:1>`）やDiffusion in Low Bits設定、Denoising Strength=1.0推奨などのTips共有。forge coupleの効きにくさやDynamicPromptの不具合報告もあり、EasyForgeNeo更新時の情報交換が活発。
- **選ばれている理由**: 以前の手軽さやAnimaとの相性の良さ（LoRA強度調整の細かさ、Low Bits設定によるプロンプト効きの向上）が評価される一方、最近のアップデートでDynamicPromptなどの機能制限が発生し「限界」との声からComfyUI移行のきっかけにもなっている。

### 2. ComfyUI（ワークフロー / カスタムノード / 運用）
- **言及内容**: サーバー運用向きのウェブアプリ仕様、リモートアクセス容易性、Anima/Krea2向けワークフロー（Image Inpainting、Depth Control、Any Control、Image Style Reference、Mage-flow対応）の豊富さ。Dockerとの相性、VRAM管理（Clean VRAM Usedノード、pinned memory、起動オプション）、クリスタ直接送り自作機能、webp保存推奨、特定ノード（Save Image Extended、negpip、Krea2T Enhancer Advanced）活用例。複数ComfyUIインスタンス分離によるカスタムノード競合回避の議論も。
- **選ばれている理由**: Forgeの限界を突破する次の選択肢として、ワークフローの柔軟性・カスタマイズ性、ウェブアプリ仕様による遠隔操作・サーバー運用しやすさ、Dockerによる環境構築・再現性の高さ、VRAM管理の柔軟性が主な理由。速度向上（turbo/int8併用）やLLM連携（LM Studioノード）も強み。

### 3. sd-scripts（kohya）
- **言及内容**: subsetごとにtimestepをずらす新機能追加。tomlファイル追記で利用可能で、質の悪い素材でのLoRA学習検証例あり。GUI未対応時のTOML直接編集やコンソール実行も。
- **選ばれている理由**: 手間が少なく、細かい学習制御（timestep offset）でLoRA品質向上を期待できる点が評価。

### 4. nano-banana
- **言及内容**: Qwen ImageのEdit機能と比較され、「Editの独立した使い勝手がnano-bananaに近づいている」とポジティブ評価。ローカル無検閲版への期待声も。
- **選ばれている理由**: 直感的で自然なEdit機能の使い勝手が近く、複雑な構図生成の柔軟性が注目。

### 5. その他の学習・生成ツール
- **OneTrainer**: Krea2 LoRA作成に使用。Hugging Faceキャッシュ重複問題の事例あり。GUIを備えた柔軟なトレーニングツールとして言及。
- **DrawThings**: HTTP APIサーバー機能により、スマホからの画像生成WebUI自作が可能。
- **Kohya_lora_param_gui**: LoRA作成補助ツール（有料note記事化事例あり）。
- **としあきツール（モザイクツール）**: 2026/3/15スクリプト版がwiki更新済み。ワークフローを消さずにモザイク適用可能で評価。
- **VACE Prep**: 複数動画の結合処理ツール。
- **Local LLM / LM Studio**: プロンプト翻訳（ドスケベ日本語→英語）やComfyUIノード連携用。検閲回避版（heretic版Qwen3.6、Gemma4など）活用例。VRAM消費がネックになるケースも。

### 6. 環境・運用関連ツール
- **Linux + Docker / WSL2**: ComfyUIなどのサーバー運用に推奨。依存関係管理・再現性が高く、リモート操作・AIサーバー分離に適する。Windows GUIよりCLI中心が安定しやすいとの意見。
- **Mage-Flow / benjiさんのワークフロー**: ComfyUI上での動画生成・編集ワークフローとして言及（テンプレート未収録のものもあり）。

**全体傾向**: ComfyUIが最も言及が多く、Forgeからの移行先や高機能運用ツールとして位置づけ。学習面ではsd-scriptsやOneTrainerが品質向上・柔軟性で選ばれ、運用面ではDocker/WSL2による安定性・リモート性が重視されています。理由の多くは「手軽さ vs 柔軟性・制御性」のトレードオフや、特定機能（Edit、timestep制御、VRAM管理）の優位性です。

## Web検索による参考情報
- **Forge Neo**: Forge UIの積極的にメンテナンスされている最新版フォーク。2026年時点でモデルサポート拡大・現代ワークフロー統合が進み、ComfyUIよりシンプルな体験を提供。Automatic1111系ベースで新機能追加中。[[1]](https://www.thundercompute.com/blog/forge-ui-ai-image-generation)[[2]](https://github.com/Haoming02/sd-webui-forge-classic)
- **ComfyUI + Docker/WSL2**: Dockerコンテナ上での運用事例が多く、WSL2経由のGPUパススルーや依存管理のしやすさが確認。サーバー運用・再現性向上に適する。[[3]](https://www.reddit.com/r/comfyui/comments/1ndgt5p/success_stories_hosting_comfyui_in_docker_on_wsl2/)[[4]](https://github.com/YanWenKun/ComfyUI-Docker/blob/main/cu126-slim/README.adoc)
- **sd-scripts (kohya)**: timestep関連機能（noise offset、subset別制御など）の議論が継続。toml設定で柔軟に調整可能。[[5]](https://github.com/kohya-ss/sd-scripts/discussions/294)
- **nano-banana**: Google Geminiアプリ内の画像生成・編集機能（Nano Banana / Nano Banana 2）。テキストプロンプトによる直感的編集・高品質変換が特徴。[[6]](https://aistudio.google.com/models/nano-banana)[[7]](https://gemini.google/overview/image-generation/)
- **OneTrainer**: オープンソースのLoRA/ファインチューニングツール。GUI搭載でkohya系代替として人気。各種最適化オプションが豊富。[[8]](https://github.com/nerogar/OneTrainer)

（その他ツールの詳細バージョン情報はコミュニティ依存のため、検索で一般的な位置づけを確認しました。）
