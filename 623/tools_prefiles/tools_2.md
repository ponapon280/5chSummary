### 抽出されたツール関連話題

ログから生成AIの「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-banana などのインターフェース、カスタムノード、ワークフロー、スクリプト、プラグインなど）に関する話題をすべて抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen など）関連は除外。ツールの選択理由が明記されている場合を強調。

#### ComfyUI (comfy) 関連
- **244**: ComfyUI Lora managerでDLする時にフォルダ分けしたらLora managerの画面に反映されてるんだけど元からあったLoraをそのフォルダに移動しても反映されないのってどうしたらええん？
- **251**: とりあえず「Edit」→「Refresh Node Definitions」を押してみる（ComfyUIの操作）。
- **255**: それもcomfyの再起動もしたけど無理だった。
- **256**: lora managerを開いて「更新」→「取得」はどやろか（ComfyUI Lora manager）。
- **257**: モデルのダウンロードはSave Pathってパラメータがあるみたいで、別ディレクトリ切ってるのはそこの指定がそのディレクトリになってるっぽい（ComfyUI Lora manager）。
- **269**: easy cache で生成が元々12秒ぐらいだったのが8秒になったわ（ComfyUIのEasyCacheノード、初回生成が180秒近くかかる問題）。
  - **理由**: 生成高速化のため。
- **270-271, 275, 285-287, 289, 316**: torch compile（ComfyUI coreのTorchCompile, KJnodes版, wavespeed版）の初回生成時間や速度向上（例: 40秒→9秒, 23秒→18秒）。
  - **理由**: 生成高速化（初回遅延解消、2回目以降高速化）。
- **277**: wavespeedの使ってるけどcomfy本体に入ってるの方でも同じように動いた（ComfyUIのwavespeedノード）。
  - **理由**: 生成高速化WFで使用、ComfyUI本体版でも動作。
- **280, 293, 295, 301-304**: Anima高速化WF（モデルローダーとKSampler間にノード挿入, sage attention + 起動オプションfast全部盛り）。
  - **理由**: 生成速度向上（例: 25秒→13秒, 60秒→20秒, SDXL並み高速化）。絵柄変化少ないWavespeed推奨（305）。カーキ色ノード群はSDXL系互換（303）。
- **285-289**: KJnodesのTorchCompile, comfy core, wavespeed, sage attention。
  - **理由**: 生成高速化（28stepで5秒後半）。
- **292**: 生成高速化って EasyCache 使うか Compile Model+ 使うか2択？
  - **理由**: 生成高速化選択肢として。
- **299**: カスタムノードをWAS LMStudio EasyQueryに変えたら通るようになったわ（ComfyUIカスタムノード）。Anime Captionのタスクファイル。
- **305**: EasyCacheよりWavespeedの方が絵の崩壊が少ないからそっちつこてる。
  - **理由**: Wavespeed選択（絵の崩壊少ないため）。
- **307-309, 311-313, 315, 318, 321-322**: TorchCompileModelエラーとwavespeedのCompile Model+代用（初回73秒→10秒）。
  - **理由**: TorchCompileエラー回避と高速化（25%速く）。キャッシュクリア必要。
- **336**: Danbooru語のTaggerって何が最新なんやろ eva02ってもう二年前（ComfyUI Taggerノード）。
- **339**: 今回のワークフローはカスタムがKJNodeしかないからええけど（ComfyUIカスタムノードKJNode）。
- **343**: ワイ：この項目の説明もう一回見たいな(マウスホバー) ComfyUI：２度目はねえ、失せろ（ComfyUIのUI挙動）。
- **373**: ZIで2倍tiled diffusionを3回かけて8Kにするの（ZI=ComfyUI関連ツール? tiled diffusion, easy cacheエラー）。
  - **理由**: 高解像度生成（easy cacheはtiled diffusionでエラー）。
- **377, 380**: tile（tiled diffusion）。
  - **理由**: 高解像度描き込み（denoising高めで再描画）。
- **385**: InfiniteTalk_I2V（ComfyUI関連ノード?）。
- **394, 408, 433**: comfyuiのプロンプト欄の,って行の最後やと消える（ComfyUI-Autocomplete-Plus拡張が原因）。
  - **理由**: プロンプト入力問題解決のため類似拡張探し。
- **405, 410-413, 416**: stabilitymatrix（StabilityMatrix, 北=北米版?, zuntanエディション, neo更新, Python 3.13.12アプデ）。
  - **理由**: 環境管理・更新（環境壊れやすいため別々管理推奨412）。
- **412**: スタビって色々追加すると環境壊れるから結局1111とcomfyui別々に入れるようになった（StabilityMatrix問題）。
  - **理由**: 安定性（環境壊れ防止）。
- **418**: ComfyUI-Easy-Install使ってcomfyだけ触っとけばええやん。
  - **理由**: 簡単インストール・運用。
- **421**: ComfyUIだと公式の改善早過ぎるからEasyよりもWF配布程度で良い。
  - **理由**: 公式改善速いためWF配布優先。

#### A1111 (Automatic1111) 関連
- **412**: 結局1111とcomfyui別々に入れるようになった。
  - **理由**: StabilityMatrixで環境壊れやすいため別管理。

#### sd-scripts / LoRA学習スクリプト関連
- **238**: sd-scriptsでAnima用のキャラLoRAを全自動で学習するスクリプト（rentry.co/qxtg2iun, MinGitとPython Embed使用, wd14タガーでdanbooruタグ）。
  - **理由**: Windows上でGit/Python不要で動く、SDXL用スクリプトベース（245, 272, 276で好評）。
- **327, 334, 349, 368, 424**: setup-anima.bat / setup-anima.ps1実行エラー（pip install失敗, accelerate/hugginface_hub未インストール, PATH警告）。
  - **解決**: ファイル削除再実行（349）, PATH設定（426）。

#### Kohya_ss 関連
- **387**: Kohya_ss更新まだか（LoRA学習ツール）。

#### その他ツール・ノード
- **442**: A1111のvariationみたいな機能はComfyUIにはないんかの？（機能比較）。

**抽出まとめ**: 主にComfyUI中心（Lora manager, 高速化ノード: EasyCache/Wavespeed/TorchCompile/Compile Model+/sage attention/KJnodes, WF, カスタムノード）。高速化・安定性・UI改善が選択理由の多く。LoRA学習スクリプト(sd-scripts)はWindows互換性で好評。StabilityMatrixは環境破壊多発で避けられる傾向。A1111はComfyUI併用で言及のみ。