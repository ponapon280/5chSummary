### 抽出された「ツール」関連話題一覧

ログから生成AI（主に画像/動画生成関連）に関連する「ツール」（ComfyUI, webUI, nano-bananaなど）の話題をすべて抽出。モデル（NAI, illustrious, FLUX, Wan, Qwen-Image, anima, Z-Image/ZIT/ZIE, LTX/LTX-2.3など）関連話題は除外。Qwenシリーズは画像生成以外の話題のみ抽出（該当なし）。ツール選定理由が明記されているものは強調。

#### ComfyUI (comfy/comfyui/comfy運営/ComfyORG/ComfyUI本体/Front End/frontend)
- **239**: RedditにComfyORGが声明出しとる（安定性に関する最新情報と取り組み）。
- **242**: comfy運営も最近のアプデに問題多数認識。新機能開発4月末まで凍結。
- **250**: ComfyUI本体もFront Endも毎日大量Commit。新しいモデルzero day supportなくなる。TurboQuantも当分サポートなし。Kijai氏custom nodeで対応期待。
- **252**: 最新版でカスタムノード調子悪い。node2.0未完成でアプリモード/UI変更実装し悪い癖。
- **253**: frontendのissues大盛況。
- **256**: comfy精力的に頑張りすぎてついていけない。安定版で足踏み推奨。
- **257**: comfyuiシンプルモードは肩透かし。ON/OFF不可で使いにくい。
- **259**: Nightly版で挑戦→問題なければRelease版反映の手順踏んでない？
- **260**: マンパワー足りない感じ。
- **291**: comfyui起動で終了時開いていたワークフロータブが1つ残して消える対処法？
- **310**: ComfyUIアップデートでタブ復元祈る。1.18.1で複数タブ復元確認したが1つだけに。
- **421**: EasyWanのWFからComfy触って卒業。チャッピー（おそらくComfy関連ツール？）のおかげ。
- **432**: pointseditor使えばeasyのポイントモザイク簡単実装（カスタムノード）。ベータ版挙動おかしいがComfyUIカスタムノード。

#### Stability Matrix / LykosAI
- **236**: Stability Matrixのpatreonページ消えると支援（コーヒー奢り）できなくなる。
- **244**: Patreon削除でLykosAI支援者減って困る。ベータ/プレリリース利用権失う。
- **255**: 作者支援口減る。

#### nano-banana (Nano Banana / nano banana pro)
- **332**: **Nano Bananaが圧倒的に漫画作りやすい**（エロなしなら）。最近1ページ数ページ漫画にハマる。FramePlanner/DESUより優位。
- **339**: nano banana proでも棒人間ベースのまともなネーム微妙（学習データ溢れてるのに）。

#### llama.cpp
- **235**: コンパイル20分かかった。
- **246**: 5700Xで(@SYCL)コンパイルすぐ終わるイメージ。

#### Kohya系ツール (Kohya_LoRA_param_GUI / Kohya HRFix)
- **302**: Kohya_LoRA_param_GUIでRedRayzニキ汎用プリセット学習。
- **313**: reForgeならKohya HRFix使え（生成序盤小解像度→拡大）。

#### RunPod (クラウドGPUレンタル)
- **299**: **ローカル弱すぎるからLoRA作る時だけRunPod使用**。どっちもcomfy使えるので便利。

#### TTS/音声ツール (irodori / emoji / Style-Bert-VITS2 / litagin / zuntan / Easy / Emojiv2 / gradio_app.py)
- **308**: 音声AI irodoriとemoji別物？ chatgptにGitHub見せても適当回答。
- **311**: **emojiは本家irodori拡張版（自作）**。バグ潰し/モデルv2対応中。スライス/絵文字自動キャプション（LM studio等LLM連携必要）、マージ/変換/パラメータ調整可。gradio_app.py解析で機能把握。
- **318**: Emojiv2対応。素材少ないファインチューン学習。絵文字キャプションでqwenに公式38種以外使わず指示（マシになったが混ぜる）。
- **330**: 上位互換でemojiいい？ 本家弄ってみる。
- **355**: Style-Bert-VITS2起動しなくなってる。zuntan金取っても修正希望。無料ツール長続きしない。
- **357**: sbv2にEasyあり。Zuntan「litaginさんのStyle-Bert-VITS2使え」と。
- **358**: litagin02/Style-Bert-VITS2使用。Zuntan関係なし。
- **380**: Style-Bert-VITS2修正有料でも買う（100人買ったら50万）。

#### EasyWan22 / EasyWAN / zuntan WF / Wan2.x WF (ComfyUIワークフロー)
- **372**: zuntan EasyWan22お世話に。クリックだけで仮想環境/必須ファイル/欲しいものまで至れり尽くせりで依存。
- **374**: civitai WFメンテ放置多数。**EasyWan22は動く状態凍結で動かしやすい**（離れられない）。
- **375**: **日本でzuntanより簡単ツールなし。3千/5千円でも買う**。
- **395**: EasyWan22スレでzuntan細かく説明書くのに質問多発。民「説明読め」。
- **399**: EasyWan22スレ回答側経験。学ぶことなくな去った。
- **407**: EasyWANモザイク専用に。**WF+説明ぎっしりで情報量多く目滑る**（初心者脳拒否）。
- **409**: zuntan Wan2.1にMP4読み込みモザイクWFあり。読む/覚える努力必要。

#### その他のツール
- **249**: MMaudio同梱サンプルワークフロー動かず。AIにnodes.py弄れ言われてもダメ。変更入った？
- **294/297/300**: Comic Book Markup Language (CBML)。LLM/コーディング補助AI連携で漫画自動化アプローチ。
- **314/316/321/325**: MangaEditorDESU!（コマ割り/吹き出し配置ツール）。最近アップデート。ページ機能/コマ割り/吹き出し追加便利（クリスタより）。
- **332**: FramePlanner（時々使用）。DESUわかりにくい。
- **377/381**: dasiwa WF / Smoothmix WF（高速化LoRA込みシンプルWF）。cfg1.0でモデルクセ把握早い。
- **376/388**: Patreon高性能WF（有償アプデあり）。要望すぐ追加。
- **390**: ハカセ アイ（外人WFパクってオリジナル風配布）。
- **430**: エージェントに丸投げ環境構築可能。
- **275**: Kling AI（最低プラン加入で毎日5秒動画x3無料安い。日本語対応希望）。

#### 技術ツール（ツールとして言及）
- **TurboQuant**: 複数言及（247,250,254,324,343,366）。KVキャッシュ圧縮でLLM/DiT/長コンテキスト/高解像度動画高速化。誤解訂正（モデルウェイト圧縮×、KVキャッシュ圧縮〇）。

抽出はツール名/話題に直接言及したもののみ。理由明記時は太字。ComfyUI関連が最多で開発/安定性/使い勝手中心。nano-banana/zuntan系は「簡単/漫画向き/依存性」で選好理由明確。