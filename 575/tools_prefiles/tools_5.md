以下は、提供されたなんJ（5ch）のログから、生成AIに関連する「ツール」に関する話題をすべて抽出したものです。抽出の基準は指示通りで、ツール（例: ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなど）を指し、モデル（NovelAI (NAI), Pony, illustrious(イラストリアス, リアス,ill,IL), Noobai, FLUX, Wan, Qwenなど）に関する話題は除外しています。特に、そのツールが選ばれている理由が言及されている場合、それを明記して抽出しました。抽出はログの番号順にまとめ、関連する発言を引用・要約しています。

### ComfyUI (comfy) 関連
- 853: Matrixで昨日あたりからcomfy更新かけたらuv.exeが追加されてキャッシュが作られるようになったんや  ほんでで巨大なキャッシュ容量占有してるから気になってなー
  - (StabilityMatrix経由でのComfyUI更新とuv.exeの追加、キャッシュ管理の話題。理由の言及なし。)
- 855: comfyは覚えたほうが良い
  - (理由: 二次生成で主流のため、覚えることを推奨。)
- 857: qwenなら公式のWFにblocktoswapノード挟むだけでええで
  - (ComfyUIのワークフロー(WF)とBlockSwapノードの使用。理由の言及なし。)
- 873: qwen-imageの公式WF+blockswap
  - (ComfyUIの公式WFとBlockSwapノードの組み合わせ。理由: SSDスワップなしで動かせる安定性。)
- 876: fp8モデルならBlockSwap、ggufモデルならUnetLoaderGGUFDisTorch2MultiGPUで仮想Vramがいいって書いてあるの見たで
  - (ComfyUIのBlockSwapノードとUnetLoaderGGUFDisTorch2MultiGPUノード。理由: 仮想VRAMでメモリ管理が良い。)
- 877: ワイ環やとWanやFlux、QwenなどのClipローダーはデバイスCPUが早くて安定してるんやけど  Qwen-Image-EditだけはClipローダーのデバイスCUDAにしないとバチクソに遅い
  - (ComfyUIのClipローダーノードのデバイス設定。理由: CPUが速くて安定、ただし特定の場合CUDAが必要で遅延回避。)
- 879: ちゃっぴーがfp8モデルを読み込むノードの後にBlockSwapノードを入れて次にModel Patch Torch Settingsノードを繋いでtrueにしたらfp8モデルでも問題ないよって言ってたんやけど違うんやろか・・・？
  - (ComfyUIのBlockSwapノードとModel Patch Torch Settingsノード。理由: fp8モデル対応で問題回避。)
- 883: ComfyUIがhunyuan image 2.1に対応してたで
  - (ComfyUIのモデル対応更新。理由の言及なし。)
- 899: comfyのプルリクにはSupport hunyuan image 2.1 regular modelって書かれてるけど  既に出てる8ステップ推奨の蒸留モデルにはまだ対応してないんか？
  - (ComfyUIのプルリクエストによる対応。理由の言及なし。)
- 901: リファイナーと蒸留モデルはまだcomfyでは使用できないみたいやね
  - (ComfyUIの機能制限。理由の言及なし。)
- 945: easywan22環境だとcomfyバージョン上げろ言われて試せないやね、様子見や
  - (EasyWan22とComfyUIのバージョン互換性。理由の言及なし。)

### StabilityMatrix 関連
- 848: StabilityMatrix\Data\Assets\uv\cacheに7.2GBも溜まってるからキャッシュ消したらまたダウンロードが始まった  消しても問題なく動くが消したら駄目なんかこれ
  - (キャッシュ管理の話題。理由の言及なし。)
- 849: uvはvenvのような仮想環境やな  容量的にそれぐらいやろうし、torchとか消したらまた起動時に環境構築するやろな  cacheと言う名前だけに「一時的な用途だし消してもええやろ」と思ってしまうやろうな
  - (uvを仮想環境として扱う。理由: 消しても再構築可能で一時的用途。)
- 853: Matrixで昨日あたりからcomfy更新かけたらuv.exeが追加されてキャッシュが作られるようになったんや
  - (StabilityMatrix経由の更新とuv.exe追加。理由の言及なし。)

### EasyWan2.2 (easywan22) 関連
- 915: easywan2.2でfastmixのF16.ggufモデルダウンロードして生成しようとしたらinvalidになってしまうんやが
  - (生成時のエラー対応。理由の言及なし。)
- 945: easywan22環境だとcomfyバージョン上げろ言われて試せないやね、様子見や
  - (ComfyUIとの互換性。理由の言及なし。)
- 982: EasyWan22なんだけども、モザイク処理が上手くいかねー  たまにpointmosaicでサクッと決まることもあるんだけど  大体は関係ないとこにモザイクかかってしまう
  - (モザイク処理の不具合。理由の言及なし。)
- 985: 正常位はAutoで大体いけるけどチラつきが多い  無理ならpoint+mask  pointは陰核包皮までモザ掛けてくれんのよな…
  - (pointmosaicやAuto/point+maskの使用。理由: 正常位でAutoが大体いけるがチラつき対策にpoint+mask。)

### LM Studio 関連
- 970: LM Studioで「Force Model Expert Weights onto CPU」の設定を利用する際に気を付けることはって聞いてみたけどいろいろ返ってきた
  - (CPU設定の使用。理由の言及なし。)

### 動画編集ツール (Premiere Pro, Kdenlive, DaVinci Resolve) 関連
- 984: 動画編集ソフトでつけてる
  - (モザイク処理用。理由の言及なし。)
- 986: ワイは早朝ピンポン怖いからプレミアプロで手動モザイクやな・・・
  - (Premiere Proの手動モザイク。理由: 自動化のリスク回避。)
- 987: ワイも静止画動画問わず手動モザイクや
  - (手動モザイク一般。理由の言及なし。)
- 989: 動画はちょっと前までubuntuでやってたからkdenliveつことる
  - (Kdenliveの使用。理由: Ubuntu環境での動画編集。)
- 993: davinci resolveのMagicMaskって機能が気になってるやが、 お試しできひんし、5万近い出費なるからなぁ…  モザイクかけるだけでやで…
  - (DaVinci ResolveのMagicMask機能。理由: モザイク自動化の可能性だが高額のため様子見。)

### Pythonツール / YOLO 関連
- 990: ちゃっぴーに手伝ってもらってyolov8モデルのbboxやsegm両方を複数使えてそのANDをとった領域に自動でモザイクをかけるpythonツール(静止画/動画両対応)作ったことあるけど  どのモデルの組み合わせがいちばんいいかってのがモザイクを掛けにいく対象によって変わってくるので、そこ自動化できないなら自動化の意味なくね？ってとこでおしまいだった
  - (YOLOv8ベースのPythonツールで自動モザイク。理由: bbox/segmのANDで領域特定だが、対象依存で自動化の限界あり。)
- 991: ワイもほぼ同じようなツール作ったことあるけどリアル系とアニメ系それぞれで学習したモデルをマージしたのが一番検出効率良かったな  今ならyolov11のobb対応の素材で学習すると精度上がりそうだから試してるところやわ
  - (YOLOv11ベースのツール。理由: リアル/アニメマージで検出効率向上、obb対応で精度向上期待。)

### その他のツール関連
- 925: 自決した！LECO作ってなんとか解決できた
  - (LECOツールの作成・使用。理由: 猫耳バンドと動物の猫の混在問題解決。)

上記がログから抽出されたすべてのツール関連話題です。抽出対象外のモデル関連（例: Qwen, Wan, Hunyuan Imageなどの具体的なモデル名や量子化の詳細）は意図的に除外しています。もし追加のログや уточненияが必要でしたら、お知らせください。