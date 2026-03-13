### 抽出されたツール関連話題（ComfyUI, webUI, Forge neo, Stability Matrix など）

ログから生成AIツール（ComfyUI/comfy, webUI, Forge neo, Stability Matrix, TensorRT, ComfyUI-Easy-Install, その他拡張ノード/WF/アップスケーラー関連）に関する話題をすべて抽出。モデル（NAI, illustrious, FLUX, Wan, Qwen-Image, anima, Z-Imageなど）は除外。Qwenシリーズの画像生成以外（例: LLM/VRAM話）はツール文脈で一部含むが、ツール中心に抽出。選ばれている理由（速さ、使いやすさ、VRAM効率など）が明記されたものは強調。

#### ComfyUI (comfy) 関連
- **452**: 自作拡張ノードでSD Prompt Readerみたいなメタデータ保存/読込関連ノードとXY Plot機能の組み合わせ。拡張ノード自体は近いうち公開。XY Plot Endノードに流れた画像を使って生成するタイプなんでSDXL以外でも使える見込み。
- **453**: XY Plotはループとバッチ両方のモードを実装。バッチモードでもモデル切り替えで出力出来る。
- **454**: 分けない方が推論速いしメインRAM使用量も少ない（ComfyUIの分割処理比較）。
- **471**: ModelScopeのXで紹介されているQwen-Image-Layered-Controlにブラシ機能がついたQwen-Image-Layered-Control-V2が切り抜きに良さそう。**comfyui内で使えるようにならないかな**（ComfyUIで使えることを期待）。
- **490**: comfyに関してはチャッピーgrok geminiはエラー直しで沼った記憶しかないからな。claude師匠一択（ComfyUIのエラー直しでClaude推奨）。
- **510**: civitaiにAnimaでcontrolnetのCannyみたいに使えるLoraがあるな。**専用に作られたフォークのcomfyuiが必要**。
- **519**: WFのいじり方が全然わからん、公式は動作速いけど画質がいまいち（ComfyUI Workflow）。
- **520**: CG板の**Comufyスレ**で知障が暴れて酷いことになってた（ComfyUIスレタイポ）。
- **521**: KJnodesノードのデフォルトは1152*832。マンガのページとかで使われてる1:14比率なら1280*896の方が近い。色々試しててもどっちも大差はない（ComfyUIノードの画像サイズ設定）。
- **525**: dynamic vram試してみるかと**comfy更新**したけどdynamic vram使うとhook機能使えなくなる。
- **526**: トレーニング時は64の倍数らしいけど出力時は32で良さそう。中途半端なサイズだと画面端が明るくなったり（ComfyUI画像サイズ）。
- **541**: animaでQwen3.5を使うやつワイらでも使えそうなやつが出てた（後続でComfyUI対応言及）。
- **551**: **forge neo民**ワイ、低みの見物（Forge neo使用）。
- **583**: 1ファイルにマージして**comfyui-qwen35-anima**で動作確認した検閲解除版をアップロード（ComfyUIカスタムノード/WF）。
- **587**: 誰か**easyanima**作って……
- **588**: AnimaはEasyやろ（Easy用ツール？）。
- **589**: animaは普通に**neo**で使えるで（Forge neo）。
- **605**: 公式ワークフローだとSDXLと同じぐらいシンプルでこれ以上ないぐらいイージー（ComfyUI WFの簡単さ理由）。
- **608**: **stability matrix**が実質easy comfyやん？
- **609**: **ComfyUI-Easy-Install**が一番楽。**stability matrix**は便利やけど全任せになるから一切成長出来ん（**Stability Matrixは便利だが成長阻害の理由でComfyUI-Easy-Install推奨**）。
- **610**: 全任せでええねん（Stability Matrixの全任せ利便性）。
- **612**: comfy使ってる人は環境構築に事に生を実感するヘンタイさん（ComfyUI環境構築の魅力/難しさ）。
- **613**: ComfyUI使いこんでくと、一枚の生成を一回こなすのに当初はエラーまみれ。一日一万枚、感謝の生成… ノードを整え、拝み、祈り（ComfyUIの学習曲線と成長過程）。
- **615**: 初心者ほど「Ultimate Workflow」とか「All in One Workflow」とかDLして秒速で投げ出すのが**ComfyUI**（ComfyUI WFの初心者あるある）。
- **617**: 謎にディティーラー→アップスケーラーを20回くらい繰り返してる「やってる感フロー」（ComfyUI WFのDetailer/アップスケーラー）。
- **640**: **ComfyUI**のあのワークフローにビビる人多いけど基本的なことするならそんなに難しくはない。マインクラフトと同じくらいの難易度（ComfyUIの難易度低評価理由）。
- **644**: 拡張をgithubからインストールするだけで使える**WebUI**と比べると、インストール後に自分でノード追加して数本とはいえ線をつなぐ必要がある**ComfyUI**は難しそうに見えてしまう。移行後にみんな一番使いたいだろうDetailerがかなり複雑。ワイはもう**WebUI**には戻れない（**WebUIの簡単インストール vs ComfyUIのノード接続難易度比較。ComfyUIのDetailer複雑だが戻れない理由**）。

#### その他ツール関連
- **513**: **wan2.2とTensorRT** でアプスケとフレーム生成して動かす（TensorRTの動画処理使用）。
- **514**: **lightx2v**や低ステップ生成（Lightx2vアップスケーラー、品質低下理由）。
- **517-518**: **lightx2v**使って品質上げるならrank128か256のlightx2v使って6x6の12step（Lightx2vの推奨設定理由: 品質向上）。
- **571**: **irodori-TTS**のフォーク版入れてみたんだが、生成された音声ガビガビ（TTSツールのフォーク使用/問題）。
- **582**: 親切な人が動画の顔修正**WF**あげてくれてた（ComfyUI動画WF）。
- **600**: 音駆動のノードはローカルでも色々（音連動ノード）。
- **648**: **nvidiaの動画アップスケール**くっそ軽い（静止画用途でも良さそう）（NVIDIA動画アップスケーラーの軽さ理由）。

これでログ全体のツール関連話題を網羅。ComfyUIが最多で、使いやすさ（Easy-Install/WFシンプル）、速さ（dynamic VRAM）、成長性（Stability Matrix比）、ノード拡張（XY Plot, KJnodes, Detailer）が選好理由として頻出。WebUIはインストール簡単だがComfyUIに戻れない満足度が高い。