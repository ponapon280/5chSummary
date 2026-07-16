# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI系中心の生成AI関連ツールレポート
- ComfyUIのワークフロー管理・保存・最適化・UI改善に焦点を当て、保存信頼性・互換性・速度向上・簡素化を主な選定理由とする

### ツール: その他のComfyUI関連ツール・機能
- ComfyUIターミナルを左サイドバーから開きエラーログを確認可能

### ツール: comfy-kitchen / 最適化関連
- comfy-kitchen（0.2.18など）を手動更新しNative opsを有効化してint4/int8/ConvRotモデルの安定動作と生成速度向上を実現
- RTX 50シリーズなどハードウェアに応じたint8フォールバックを含む精度・互換性確保が更新の主な目的

### ツール: その他
- ControlNet / KJNodesを一貫性のあるアニメーション生成やConditioning用途で活用

### ツール: Web検索による参考情報
- comfy-kitchenはComfy-Org/comfy-kitchenリポジトリの高速カーネルライブラリでquantization/RoPE最適化を提供
- ComfyUI PowerPanelはワークフローに統一コントロールパネルを追加しWebApp化を可能にする
- ComfyUI v0.28.0はConvRot int4対応を含む
- 情報は2026年7月16日時点に基づく

---
# 元の本文
**ComfyUI系中心の生成AI関連ツールレポート**

ログから抽出されたツール関連の話題は、主にComfyUIのワークフロー管理・保存・最適化・UI改善に焦点を当てています。モデル（anima、krea2など）に関する記述は除外し、ツールの選定理由が明記されている点を中心にまとめました。ツール選択の主な動機は、**ワークフローの保存信頼性・互換性**、**最適化（int4/int8/ConvRot対応）による安定性・速度向上**、**ワークフロー簡素化・UI改善**、**自動更新の利便性**です。

### 1. Save Image系カスタムノード（ワークフロー埋め込み・保存ツール）
- **audioscavenger/save-image-extended-comfyui（Save Image Extended）**  
  現在最も推奨されている保存ノード。webp/avif両対応で、メタデータとワークフローを確実に保存可能。インストールしていないComfyUI環境でもwebp画像をドラッグ&ドロップしてワークフローを読み込める互換性が優れている。Save Image PlusやSaveImage-PPで発生していた「後からワークフローが読み込めなくなる」問題を回避できる点が評価されています。

- **comifyui-saveimage-plus（ID 1516） / ComfyUI-SaveImage-PP（ID4117）**  
  以前使用されていたが、生成したwebpのワークフローが後から読み込めなくなる不具合が複数報告され、敬遠されています。Save Image Extendedへの移行が推奨されています。

- **ComfyUI-Custom-Scripts**  
  ワークフロー入りの画像を出力する際に必要となるノード。

**選定理由のまとめ**：Save Image Extendedは「保存信頼性が高く、未インストール環境でも互換性が高い」点で支持されています。一方、Plus/PP系は読み込み不具合により不評です。

### 2. ワークフロー読み込み関連のトラブルと対処
Save Image Plus使用時でもwebpワークフローが読めないケースが報告されており、対処として「png出力」「imgbb.comアップロード」「Save Image Extendedへの切り替え」が提案されています。

### 3. その他のComfyUI関連ツール・機能
- **NoofyUI**：ComfyUIの中身を維持しつつインターフェースを見やすくするツール。「配線工事不要」との触れ込みですが、実際はワークフローを読み込んで使用するため根本的な配線不要にはならないとの指摘あり。
- **app mode**：ComfyUIの標準機能として簡易的なワークフロー実行に言及。
- **ComfyUIのターミナル（コンソール）**：エラーログ確認用に左サイドバーから開ける。

### 4. comfy-kitchen / 最適化関連
- **comfy-kitchen（0.2.18など最新版）**  
  ComfyUIのNative ops（float8_e4m3fn、int8_tensorwise、mxfp8、nvfp4など）を有効化し、int4convrotモデルの動作を安定させるために必要。`pip install --upgrade comfy-kitchen`で手動更新。Portable版/Desktop版/Stability Matrixなどでは自動更新の挙動が異なるため、手動更新が推奨されるケースがあります。生成速度向上（int8化、sage attention、compile model、easy cacheノード併用）にも寄与。

- **webui-user.bat**：使用していればcomfy-kitchenが自動インストール・更新される利点あり。

- **Forge Neo**：SD WebUIの派生版。Anima Edit拡張の対応やLoRA Block Weight neoの互換性問題が言及。comfy-kitchenとの組み合わせで使用される文脈も。

**選定理由**：特定精度（int4/int8/ConvRot）の動作安定性とバージョン互換性の確保。RTX 50シリーズはint4非対応のためint8フォールバックが必要などのハードウェア考慮も。

### 5. ワークフロー簡素化・編集関連ツール
- **ComfyUI PowerPanel**：すべてのノードを一つのクリーンなコントロールパネルに折りたたむ機能。ノードだらけのワークフローを整理・簡素化できる点で選ばれています。
- **ComfyUI-Cosmos-Referenceノード**：Anima Edit LoRAと組み合わせ、領域指定・参照ベース編集（マスク不要で着替えなど）を実現。従来のinpaintより「マスク不要で自然に差し替えやすい」点を評価。
- **ParamGui**：最新版を常用し、学習解像度プリセット（1024 vs 512）などの利便性を重視。
- **ComfyUI v0.28.0**：ConvRot int4対応を含むリリースで、ワークフロー組み直しを待たずに利用可能になった点が言及。

**選定理由のまとめ**：低スペック環境での速度・安定性、マスク不要の編集効率、ワークフローの再現性・自動化、視認性・モデル管理のスムーズさ。

### その他
- **ControlNet / KJNodes**：一貫性のあるアニメーション生成やConditioning用途で言及。
- Qwenシリーズやnano-bananaなどの指定ツールの言及はログ内にありませんでした。

全体として、ComfyUIエコシステムのツールは「信頼性・互換性・最適化・簡素化」を重視して選択されており、Forge NeoなどのWebUI派生ツールも併用されています。

## Web検索による参考情報
- **comfy-kitchen**：Comfy-Org/comfy-kitchenリポジトリの高速カーネルライブラリ（Diffusion推論向け、多様なバックエンド対応）。バージョン例として0.2.18が確認され、quantizationやRoPEなどの最適化を提供。ComfyUIのNative ops有効化に寄与。[[1]](https://github.com/Comfy-Org/comfy-kitchen)[[2]](https://www.freshports.org/misc/py-comfy-kitchen/)
- **ComfyUI PowerPanel**：lihaoyun6/ComfyUI-PowerPanelとしてGitHubで公開。ワークフローに統一コントロールパネルを追加し、Node 2.0を使わずにWebApp化可能。[[3]](https://github.com/lihaoyun6/ComfyUI-PowerPanel)
- **Forge Neo**：Haoming02/sd-webui-forge-classicのneoブランチ。Stable Diffusion WebUIのアップデート版で、Flux/Qwen/wan対応などの新機能追加。GradioベースでAPIサポートあり。[[4]](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)[[5]](https://www.stablediffusiontutorials.com/2025/11/forge-neo-installation.html)
- **ComfyUI v0.28.0**：ConvRot int4対応を含むバージョンとしてログで言及されたが、検索時点で具体的なリリース詳細は追加確認できず（一般的なComfyUI進化として最適化が進んでいる）。[[6]](https://comfy.org/)

（検索日：2026年7月16日時点の情報に基づく）