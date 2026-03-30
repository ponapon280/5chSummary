### 抽出された「ツール」に関する話題一覧

ログから生成AI関連の「ツール」（ComfyUI, webUI, easywan/nano-banana系, Stability Matrix, Forge/reForge/forgeneo系, A1111系, was node suite, KJNodes, Ultimate SD Upscale, VSR, RealESRGAN, Antigraintyノード, Node2.0, Everywhere, Dynamic Prompt, gradioなど）のみを抽出。モデル名（anima, illustrious/リアス/ill/ILなど指定リスト）は一切含めず、ツールの話題に限定。ツールが選ばれている理由や関連コメントも併記。Qwenシリーズの画像生成以外（例: TTS関連キャプション）は含むが、本ログでは該当なし。

#### ComfyUI関連
- **436**: Comfy UIのテンプレから入れたら基本的にNSFW出せないの？ easywanからComfy ui移行しようと思ったけど出力できねえわ  
  *(easywanからComfyUIへの移行を試みたが、出力できない問題)*
- **455**: ノードスッキリさせるためにAntigrabityに作ってもらった独自ノードがどんどん増えてイク…  
  *(ComfyUIでAntigravity製独自ノードを活用中)*
- **456**: 複数のstringを結合できるノードを探してるんだが、最新comfyuiで使える奴ある？ v0.18.2にしたらwas node suiteのtext concatenateが動かなくなってね...  
  *(ComfyUI最新版v0.18.2でwas node suiteのtext concatenateが使えなくなった問題)*
- **460**: ComfyUI本体側のメモリ制御効率が発展しまくりだからな 本体ノードだけでめちゃくちゃ効率化されてるのはすごいんだけど、カスタムノードへの干渉大きすぎて駄目なやつは駄目ンゴとなる アプデでメモリ効率アップは素直にすごいと思うけど、UI周りはなんじゃコリャアプデが進行中なのはまあまあいただけない  
  *(ComfyUI本体のメモリ効率向上を高評価。ただしカスタムノード干渉とUIアプデの不安定さを指摘)*
- **461**: 最近追加されたのがあったはず でも配布しないなら難易度ベリーイージーだからノードを自分で作っちゃった方が探すより速いと思う LLMなら秒でやってくれるだろうし  
  *(ComfyUIノード作成を推奨、LLM活用で容易)*
- **465**: was nodeは動かないノードが激増した 配布WFでwas node使ってるのが多いから困る  
  *(ComfyUIのwas nodeが動かなくなった問題)*
- **466**: KJNodesのJoin Stringsはどうやろう  
  *(ComfyUIのKJNodes「Join Strings」ノードを提案)*
- **467**: 本体に内蔵されてる連結ってノードでええんやないか？  
  *(ComfyUI本体の連結ノードを提案)*
- **481**: ComfyUI側のアプデがあると、更新されてないノードは使えない部分があり、不具合出すからあきらめるのが一番 今の大体の多くの人はRAM辺りが改善されたんだ！ComfyUIアプデしよ！ え、このノード赤くなってつかえねーじゃんってなってる  
  *(ComfyUIアプデによるノード不具合を指摘)*
- **482**: 一時期Everywhereが逝ったときはこの世の終わりだと思った  
  *(ComfyUIのEverywhereノードが壊れた経験)*
- **523**: Forge・A1111系だと困難だけど、ComfyUIにおけるi2iとアップスケールの組み合わせが一番いいと思う [...] 普段これでやってるわ  
  *(ComfyUIのi2i+アプスケを最高評価。Forge/A1111系より構図/色維持・微調整しやすく、モデル/LoRA変更も可能)*
- **525**: forgeneoで出力した画像をcomfyにぶち込んだらワークフローが見れるぞ Hiresが何やってるかはそれ見ればわかりやすい  
  *(forgeneo出力画像をComfyUIにドラッグでWF確認)*
- **545**: ComfyUIで右クリックからのワークフローエクスポートしても出てくるpng画像に生成画像のプレビューが出てこないんだけどなんか直す方法ある？  
  *(ComfyUIのWFエクスポートPNGプレビュー非表示問題)*
- **589**: node2.0対応してない拡張はよ絶滅しねえかなあ はよ全面移行したいわ せめて切り替えスイッチの場所変える機能でも書くか  
  *(ComfyUIのNode2.0非対応拡張の絶滅を望む)*

#### easywan/nano-banana系（Easy系ツール）
- **436**: easywanからComfy ui移行しようと思ったけど出力できねえわ  
  *(easywan → ComfyUI移行失敗)*
- **457**: Style-Bert-VITS2もEasywanも半年ぐらいで使えなくなってるけど なんでこんなにダメになるのが早いんだ  
  *(Easywanの陳腐化の速さを指摘)*
- **485**: easy系は環境を更新しなければ未だに使えるんやろ？ 最新環境とeasy系を別々で管理すればええと思うんやけど  
  *(Easy系は環境固定で継続使用可能)*
- **486**: 自前PCに入ってる既存のやつはVer固定で勝手なアップデートもしないからちゃんと大丈夫だけど batファイルでダウンロードしてくる先の配布リンク死んでる(代替が別URLに変わってる)ので、新規では無理という状況 [...] その辺やるともうeasyじゃないし 現配布に対応してるフォーク版もあるけど検索エンジンの都合からそこにたどり着くのが容易ではない  
  *(Easy系の新規インストール不可、batファイルURL死、フォーク版存在も発見しにくい)*
- **487**: Easy系はインストール済み、ダウンロード済みなら環境が固定されるので余計なことをしなければ問題なく使い続けられるよ 問題は新規インストール ダウンロードするものがなくなってたり、バージョンが上がって競合が起きたりしてエラーになる  
  *(Easy系の既存環境は安定、新規が問題)*
- **488**: 新規には無理やなぁ ワイらはurl書き換えるだけやけど、赤ちゃんにはそれすら面倒やろうな  
  *(Easy系新規インストールの難易度高、URL修正必要)*

#### Stability Matrix / Forge / reForge / A1111 / forgeneo / WebUI関連
- **459**: Stability MatrixでreForge更新したら起動しなくなった ダウングレード等で修正できたけどクソ面倒くさかったので一応周知しておく  
  *(Stability MatrixのreForge更新で起動不能)*
- **468**: Stability MatrixでreForgeなどのパッケージを更新するとpip install -r requirements.txtも実行されるので、更新の間にpythonライブラリ構成が変わってると次の更新の時にで影響が出ることがあるよ  
  *(Stability Matrix + reForgeのpip不整合問題)*
- **469**: そういうときはreForgeをダウングレードしただけでは起動するようにならないので詰む  
  *(reForgeダウングレードだけでは復旧不可)*
- **471**: 起動するときに pip freeze > ファイル名 でライブラリ構成を記録しておけば復旧が楽なんだけどな  
  *(Stability Matrix系復旧Tips: pip freeze記録)*
- **493**: 昨日Dynamic Promptを導入してワイルドカード書き足したりしたけどそのせいなのかなあ…… ChatGPTに聞いてダウングレードとvenv再インストールしたら起動した  
  *(Dynamic Prompt導入でreForge起動不能、ダウングレード+venv再インストールで復旧)*
- **523**: Forge・A1111系だと困難だけど、[...]  
  *(Forge/A1111系はComfyUIより劣ると指摘)*
- **525**: forgeneoで出力した画像をcomfyにぶち込んだらワークフローが見れるぞ  
  *(forgeneoの画像ドラッグ機能)*
- **632**: Stability MatrixのパッケージランチャーのreForgeの設定（歯車マーク）で--skip-installのチェックを外すこと A1111系は起動時にrequirements_versions.txtとの相違があるとpip install -r requirements_versions.txtで復旧する仕組みがあるんだけど --skip-installが付いてるとその処理をスキップしてしまう Stability Matrixはデフォルトで--skip-installにチェックが付いてるんだけど罠だと思うわ  
  *(Stability Matrix + reForge/A1111復旧法: --skip-install解除)*

#### アプスケ/アップスケール関連ツール・ノード
- **440**: 普通にUltimate SD Upscaleでimageを、同じanimaのmodelアップスケールしているかなぁ  
  *(Ultimate SD Upscale使用)*
- **443**: アプスケはVSRちゃんできまり  
  *(VSRをアプスケ定番と推奨)*
- **454**: とりあえず安定のRealESRGAN系統でやってはいるけど、もうちょい進化してるのが出てる気がする  
  *(RealESRGAN系統を安定ツールとして使用中)*
- **521**: AnimaでUltimate SD Upscaleでのアプスケが上手くいかないのってSD用だからなん？[...]  
  *(Ultimate SD Upscaleのtileサイズ/スケジューラー問題)*
- **524**: 変なノイズがのるとなると、タイルのサイズがでかすぎるのでは？ タイルは1024前後くらいまでにしないとノイズが乗ってしまう  
  *(Ultimate SD UpscaleのtileサイズTips)*
- **526**: Ultimate SD Upscaleがほんとに中身なにやってるかはいまいちわからんけど Denoiseがパラメータとしてある以上やってることはアプスケしてからi2iで再生成だろうから、[...] 実験として最終解像度を低く(アプスケ後を512ｘ512サイズでやってみる)  
  *(Ultimate SD Upscaleの内部動作推測 + 解像度Tips)*
- **529**: animaのアプスケはredditにこんなのあった (タイルごとにプロンプト作ってアプスケ)  
  *(RedditのComfyUIアプスケWF共有)*
- **531**: よく分からんけどアプスケなら ・Upscale TensorRT ・SeedVR2 ・RTX Super Resolution このへんじゃあかんの？  
  *(Upscale TensorRT, SeedVR2, RTX Super Resolution提案)*
- **532**: それはアップスケールじゃなくてただの拡大だろバーカ  
  *(上記をただの拡大と批判)*
- **534**: タイルごとにプロンプト作ってアプスケするんだな 考えてはみたことはあるけどほんとにやってる奴いるとはｗ [...] ２パスｋサンプラー、UltimateSDupscale、SEEDVR2、で思考停止して煮詰まってたとこや SEGSがあったかぁ。ワイSEGSの仕組みほんとわかってないから使いこなせんのよなぁ  
  *(SEGS, Ultimate SD Upscale, SEEDVR2使用中、SEGSの仕組み不明)*
- **536**: tileを各1024にしたらスケジューラーがnormalでも2倍のHiresでもノイズなくシャキっとした絵になってくれた  
  *(Ultimate SD Upscaleのtile=1024で成功)*

#### その他ツール・ノード
- **458**: 知らないの？Node2.0は全てを破壊する  
  *(Node2.0の破壊力指摘)*
- **591**: gradio立ち上げて生成してる場合は /gradio_app.py:22 FIXED_SECONDS = 30.0 で最大秒数設定されてるから起動するまえにここの数値60とかにすれば30秒の制限は撤廃できるよ  
  *(gradioの生成時間制限解除法)*

**抽出まとめ**: 主にComfyUIとそのノード（was node suite, KJNodes, Ultimate SD Upscaleなど）が最多。Easy系は新規インストール難が共通問題。Stability Matrix + Forge系は更新時のpip不整合多発。アプスケツールはtileサイズ調整が鍵。ComfyUIはメモリ効率向上を評価しつつアプデ不安定を指摘する声多し。