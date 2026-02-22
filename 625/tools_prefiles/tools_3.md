### 抽出された「ツール」関連話題

以下は、ログから生成AI関連の「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR/nano-bananaなど）に関する話題をすべて抽出したものです。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）に関する言及は除外。animaなどのリスト外項目はモデル扱いとみなし抽出対象外としました。各話題でツールが選ばれている理由（例: 使いやすさ、重さ、互換性、拡張性など）が明記されている場合のみ、その点を括弧内に記載。レス番号順にまとめ、重複は統合。

- **443**: comfy系やanimaの話題多いからなんやろか 諦めて触るかneo使うかすれば良いのに（comfy系が話題が多い理由として触れられているが、選好理由なし）。
- **457**: Animaの制御ムズいな ... A1111互換でプロンプト書いて保存してみた SDXLのWFで使ってた**comfyui-prompt-control**と**comfyui-image-saver**を流用できた 自作ノードが入っているのでWFは入れてない LoRAはちびたいから適当にお借りしたで（ComfyUIのノードをSDXL WFで流用可能で便利）。
- **460**: Detailer使ってみたいんやけどUltralyticsDetectorProvidorってどこにあるんや？ **ComfyUI Impact Pack**挿れてもないし**ComfyUI Impact Subpack**は古くてインストールエラーが出るんや（Detailerのインストール問題、ComfyUI拡張パック使用）。
- **462**: 前スレ >>333 の animaの高速化WFのksamperを（advanced）てのに差し替えて... 「リアスの単純なi2i」がどんなのかわからん 誰か助けてクレメンス（ComfyUI WFの再現質問、comfy赤ちゃん=ComfyUI初心者）。
- **464**: >>462 i2iならこうやろ 画像→vae encode→**Ksampler**→vae decode→画像（ComfyUIのi2i基本WF説明）。
- **466**: FaceDetailerで各種face yoloモデル全て動いてるけどな WF見れば何か分かるかもやけど（FaceDetailerのWF使用、ComfyUI拡張）。
- **468**: ComfyUI-frame-interpolationノードのckpt_nameのメニューに入ってる「rife49.pth」ってどこにあるんや？（**ComfyUI-frame-interpolation**ノードのファイル問題）。
- **477**: seedance2が**comfyui**で使えるように。
- **479-480**: >>477 comfy上でAPI叩くんでしょ？（ComfyUI上でAPI使用）。
- **481**: Package Commandが見つからず... **ComfyUI**のvenvにPython.hを入れたら正常動作した（ComfyUIのインストール/エラー解決、StabilityMatrix使用、sageattention手動インストール）。
- **482**: >>474 ... **ComfyUI-frame-interpolation**ノード... rife47.pth使えばいい（フレーム補完でrife47推奨、環境再構築時のnodes消去失敗）。
- **483**: 最初のフレーム数少なくてもこんなヌルヌル動画にできるんやねぇ 便利やな（ComfyUI-frame-interpolationの動画補完便利さ）。
- **508**: Detailerのやり方が分からんくて**ComfyUI**諦めて**ForgeNEO**使うことにするわ SageAttensionまではできたんやけど（ComfyUIのDetailer難しくForgeNEOへ移行）。
- **509**: comfyui face detailer、でググったところの一番上あたりを参考にしてやれば多分できるよ（**comfyui face detailer**推奨）。
- **510**: **SAM3 detailer**でググればWF出てくるやろ（SAM3 detailerのWF）。
- **543**: **webui**で出した画像からメタデータ拾って**comfyui**で再現するためのノードって存在しない……？（WebUI→ComfyUI再現ノード質問）。
- **544**: **webui**で生成した画像を**ComfyUI**にドラッグ&ドロップすると... webuiと同じ処理にするカスタムノードがあるよ（WebUI画像のComfyUI D&D互換性、カスタムノードで同一処理再現）。
- **546**: 今は**WebUI**で生成した画像を**ComfyUI**にドラッグ&ドロップしても最低限のワークフローに変換したりしてくれないみたい?? jpgだと「画像を読み込む」ノードに、PNGならWF変換（WebUI PNGのComfyUI WF変換便利、JPG/WebPは不可）。

### まとめ
- **主なツール**: ComfyUI（最も頻出、WF/ノード/拡張/動画処理で多用。理由: 互換性高く流用可能、Detailer/フレーム補完便利だが初心者難易度高め、インストールエラー多発）、A1111（互換プロンプト使用）、webUI/WebUI（メタデータ再現/D&D互換）、ForgeNEO（ComfyUI代替として簡単？）、Detailer系（FaceDetailer/SAM3/comfyui face detailer/Impact Pack: 検出/描き直し用）。
- 選好理由の傾向: ComfyUIは拡張性/カスタムWF強いが重く初心者泣かせ、WebUIはメタデータ共有しやすい。全体的にComfyUI中心の技術雑談。