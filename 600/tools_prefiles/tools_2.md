### 抽出された「ツール」関連話題一覧

ログから生成AI関連の**ツール**（ComfyUI/comfy, A1111, webUI, SUPIR, nano-bananaなど、拡張機能やカスタムノードを含む画像生成ツール）に関する話題をすべて抽出。**モデル関連（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）は一切除外**。ツールが選ばれている理由（利便性、安定性、機能追加など）が明記されている場合のみ記載。各話題はログ番号順にまとめ、原文に近い形で引用・要約。

#### ComfyUI (comfy) 関連
- **239-245, 268**: ComfyUIのUI担当がアホ、中止ボタン削除（frontend 1.33.1以降で右上の進行状況オーバーレイと被るため削除）。実行ボタンやカーソル位置を無視した謎のUI圧迫・狭小化。requirements.txtでfrontend-package==1.30.6にバージョンダウンしてpip installで回避可能。ただし本体のアプデで一定以下バージョンのfrontend拒否される。**理由: 中止ボタン削除が改悪で使い勝手悪化（ガタガタ騒ぐほどではないが不満大）**。
- **278**: ComfyUI更新でjob queueが右上に浮いて行方不明に。
- **281**: ComfyUI update allしたらタスク状況がオシャレ（いらん）に変化。
- **284**: ComfyUIの「Use new menu」をdisabledにするとUI変化ほぼなし。
- **287**: comfy-frontendでscripts/ui.jsのimport警告。UI系拡張機能全滅の恐れ。
- **292**: ComfyUIアプデでComfyUI-MultiGPUが全部使えなくなる（めんどくさすぎ）。
- **359-360**: Comfyのstable版は定期スナップショット。クソUI受け入れるかアプデ放置か。frontendバージョン下げて様子見、キャンセル機能はカスタムノードで対応可。**理由: stable版で安定運用（アプデ放置推奨）**。
- **362**: ComfyUIのPRで中止ボタン「他の場所に置くから消す」。フロントエンドがVueでカスタムノード側もVue依存必要でUI改修しにくい。
- **366-373, 385, 389**: ComfyUIアプデで中止ボタン削除（実行ボタン横から右上のjob history/プログレスバー/ポップアップに移動）。連打で事故りやすい。Ctrl+Enterで実行可、キャンセルもショートカット可（一覧に書け）。frontend version 1.30.6推奨。**理由: ショートカット使用で回避可だがデフォルトUI改悪（省スペース化の流行り？）**。
- **370, 394**: ComfyUIアプデで画面狭く・中止ボタン無くなる（狭くなったのを我慢してたがアカン）。キャンセルは右上進捗フロート/履歴/ポップアップに移動。Tensorrt/VideoCombine高速化（UI軽量化？）。
- **387, 402, 411**: ComfyUIで現アセット(旧キュー)からファイル削除しても実データ消えず（おま環？ webブラウザからローカルファイル削除はセキュリティ上不可）。プレビューノードでキュー履歴残る。**理由: UIで生成ファイル削除できれば便利だが不可（フォルダ検品推奨）**。
- **392**: ComfyUIでgrok/gemini（複数LLM同時質問）。

#### EasyImageEdit 関連
- **265**: EasyImageEditにZITによるアップスケール/プロンプト強化/画像からのプロンプト生成追加（Easy/ZIT/ZIT-TextToImage.jsonワークフロー）。Latent HiresFix代替Upscaler使用。VLMはComfyui-Z-Image-Utilitiesの4bit仮対応（LM Studioでlocal_endpoint設定）。エラー時はFree model/node cache。ComfyUI-EulerDiscreteScheduler追加（euler/simple/9stepがド安定）。**理由: LLM必需で高速・安定アップスケール/強化（ZIT覇権勢い）**。
- **282**: EasyImageEditいつもありがと。
- **393**: EasyImageEdit新workflowでVAEDecodeTiledエラー（Updateパッチ警告原因）。
- **401**: EasyImageEditエラー修正（Muteノード未設定が原因、パッチ警告も修正）。

#### Comfyui-Z-Image-Utilities (ZIT/Z-Image Utilities) 関連
- **265, 286**: Comfyui-Z-Image-Utilitiesのノードグループ（ZITアップスケール/プロンプト強化、VLM 4bit/LM Studio対応）。**理由: LLM連携でZIT実戦フロー、Base/Editリリース遅れで覇権（画像生成にLLM必需）**。
- **311**: Comfyui-Z-Image-Utilitiesのネーミング上手い（既存ノード同等だがマーケティング抜群）。

#### その他のツール関連
- **398**: Antigravityで複数LLM組み合わせ（Comfy辛いのでforge neo扱いやすい）。**理由: API経由生成でForge NeoがComfyより扱いやすい**。

### 抽出まとめ
- **主なツール**: ComfyUI（UI/アプデ/拡張最多）、EasyImageEdit、Comfyui-Z-Image-Utilities（ZIT/Z-Image）。これらがログの中心で、UI改悪/アプデ不満/拡張機能追加が話題の9割。
- **選ばれている理由の傾向**: 安定運用（stable版/バージョン固定）、高速化/軽量化（EulerDiscreteScheduler/Tensorrt）、LLM連携便利（ZIT/EasyImageEdit）、代替回避（frontendダウングレード/ショートカット）。不満点（UI改悪、中止ボタン削除）が目立つが、回避策共有多し。
- **非抽出対象確認**: NAI（240/244）、リアス（248/397/399）、Wan（267/272/276/308/342/343/352/358/419）、Z-image turbo/base（279/304/338/342/376/378/380/396/397/398/403/405/407/412/414/417/418/432、モデル寄りで除外）、Qwen（407/426）、smoothmix/easywan（272/276/330、モデル）、forge neo（398、Comfy代替として抽出）、LM Studio（265/352/357、LLMツールだが画像生成補助）。モデル混在話題はツール部分のみ抽出。