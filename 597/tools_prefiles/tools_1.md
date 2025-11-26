### 抽出されたツール関連話題一覧

以下は、提供されたログ（4〜241）から「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana など）に関する話題をすべて抽出・整理したものです。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwen など）に関する言及は除外。ツールが選ばれている理由や比較点は明記。レス番号順にまとめ、重複は統合。

#### ComfyUI (comfy) 関連
- **26**: nanobananaやべえな。Lora学習してプロンプトがcomfyuiがみたいな知識はどんどん不要になるんやろうな。（nanobananaがComfyUIの知識を不要にする理由で言及）
- **39**: Forge NeoってComfyよりQwenの処理遅かったりしないんかな。もし変化なかったらForgeNeoに乗り換えようかな。Comfyはノード管理ダルいんだよな。（ノード管理がダルいためForge Neoへの乗り換え検討）
- **42**: Comfyは潔癖症には辛いUIや。間違ってノードをズラしてしまったとき相当イラッとくるし元の位置にピタリと戻せるまでは生成したくない。（UIのノード位置ずれがイラつく）
- **44**: ワイ環境だとPyTorchを2.8.0以降に上げるとLoRA入れてWANを動かした時にLow側でComfyUIが強制終了。（PyTorchバージョンによる強制終了問題）
- **45**: >>42 設定>Lite Graph>常にグリッドにスナップでマス目に沿うように配置できるで。（UI改善策提案）
- **46**: >>42 右下のハンドアイコンを有効にする（矢印で編集）。画面を動かす時にスペースキーを押し続けるといいよ。それでも入力ノードあたりはピン止めした方が安心だけど。（操作改善策）
- **48**: >>42 わかる。いつもピン止めするけど全選択してピン止めしても外の枠？みたいのがピン止め出来て無くて一つ一つピン止めすることもある。easywanの文字とかも全選択じゃピン止めできないのも悲しい。（ピン止め機能の不便さ）
- **50**: ComfyUIはおかしなカスタムノードが1個でもあると起動してもブラウザから入れなくなるからほんまに手がかかるで。（カスタムノードによる起動不安定）
- **54**: ComfyUIは生成に集中できなくなる。ノードを弄るのが楽しいんや…なお深い知識はない模様。（ノード弄りが楽しく生成に集中しにくい）
- **57**: >>39 Forge Neoはカスタムノード的なのが無理。ComfyUIでそういうのを多く使っているなら速度が落ちたり使い勝手は変わるだろうね。xformersとsageattentionには対応してるから基本的な速度は問題ないと思うよ。（カスタムノード非対応のためComfyUI継続検討、速度比較）
- **58-59**: ComfyUIワークフロー紹介。custom script（オートコンプリート、テキスト/計算ノード）、rgthree（seed, power lora loader, 自動化スイッチ）、Impact-Pack（ワイルドカード、ディティーラー、webui系拡張）。全部乗せ系は分かりづらい。（必須カスタムノード推奨、webui系拡張との類似）
- **62**: ComfyUIノードリンク表示をストレートにしたら見辛い。線ずらす方法ないんやっけ。（リンク表示の不便さ）
- **64**: PainterLongVideoとSamplerをまとめてsubgraph化。シード値固定でも最初から生成し直しに。（subgraph化のトラブル）
- **65**: Qwen-Image-Edit-Rapid-AIOを実行するとエラーで動かない。ComfyUI_windows_portable。（エラー報告）
- **66**: >>58,59 その3つ（custom script, rgthree, Impact-Pack）は入れとった。シンプルいずざベスト。（カスタムノード既入）
- **67**: Quick Connectionというcustom nodeを入れるとcirciut board connectionが回路図風。hide linesで消せなくなる欠点。Settings -> circuit-board-lines で戻せる。（カスタムノードでリンク表示改善）
- **70**: >>42 ctrl + zで戻せる。（Undo機能）
- **71,73,76,79,86**: ComfyUI/Qwenエラー関連のやり取り（ドライバ、バージョン確認推奨）。
- **87**: Forge NeoがQwen-Rapid-AIO対応。ComfyUIじゃなくてもいいなら使ってみたら。（Forge Neo推奨）
- **96**: UnloadAllノード挟んだらキャッシュパージでミス。今のComfyは要らんモデルだけパージ。（UnloadAllノード廃止提案）
- **97-98**: 生成時にA1111仕様を選べるKsamplerが使えるInspirePack（訂正: InspirePack）入れとくとええ。プロンプト通りに出来上がらない場合にA1111で生成するとうまくいったりする。（A1111互換Ksamplerでプロンプト改善）
- **108**: LongVideoのコード確認、previous_video接続時のみ処理。実装漏れか。（PainterLongVideo内処理）
- **124**: webui用のブラウザにzen browserオススメしてるが、WF内の移動/ズームがカックカク。（ブラウザ互換性問題、webui関連）
- **152-153**: PainterLongVideoを6段30秒に。MotionFrames増やす/End image指定で改善。（PainterLongVideo使用法）
- **191-196**: 動画続き生成ワークフロー（最終フレーム自動切り出し）。フレーム展開でメモリ次第で長尺可能。アプスケ/補間別途。（ComfyUI動画WF）
- **214**: ワークフローが複雑になりすぎて生成の喜びがなくなった。WF弄りが目的に。（複雑化デメリット）
- **215**: 自作ノードまで行くとさらに楽しい。（カスタムノード作成）
- **233**: 今のcomfyUIの仕様ならメモリ出し入れ多め。（メモリ管理仕様）

#### Forge Neo 関連
- **39,57,82,87**: ComfyUI代替として検討。カスタムノード非対応だが速度OK。Qwen対応でComfyUIより乗り換え推奨。（ノード管理ダルさ回避、カスタムノード不要時速度/使い勝手良し）

#### nano-banana / banana / Nano Banana Pro 関連
- **26**: nanobananaやべえな。Lora学習してプロンプトがcomfyuiがみたいな知識はどんどん不要になる。（ComfyUI知識不要化）
- **72**: 商品写真に「SAMPLE」って書いてあるやつbananaで消せるな。
- **223**: Nano Banana Pro 1日100画像。Gemini3/Nano Banana Pro破壊力過小評価できない。（クラウドツール、月2900円Google AI Proで高頻度生成）
- **225**: エロくするにはローカルPCで...nano-bananaのえげつない能力が必要。（エロ前作り込みに有用）
- **232**: bananaヤベーな。プロット書いたらマンガ1ページ描いてくれる。

#### easywan / EasyWan22 関連
- **48**: easywanの文字も全選択じゃピン止めできない。（ComfyUIピン止め不便）
- **69**: easywanしか触ってなかったからPainterLongVideoってなんや状態。ローカルで5秒の壁突破。
- **210-213**: easywan22環境ならanimateが一番楽、長尺出来る。EasyWan22からAnimateへ。SmoothMix卒業でZuntan依存。（動画生成楽、長尺対応）
- **225**: Wan 2.2(EasyWan+エロLoRA)。

#### Painter系ツール (PainterLongVideo, PainterFLF2V, PainterI2V, LongVideo) 関連
- **64,69,75,78,95,108,152-153,181**: PainterLongVideo/FLF2V/I2V/LongVideoの使い分け（内部処理違い、previous_video接続時のみmotion_amplitude計算）。6段30秒、End image/MotionFramesで改善。FLF2V/LongVideo中身似ててLongVideoあれば不要。（動画延長/強力不思議動画、用途別使い分け）

#### A1111 関連
- **97-98**: InspirePackでA1111仕様Ksampler使用。プロンプト通りに出来上がらない場合にA1111で生成するとうまくいく。（プロンプト互換改善）

#### webUI 関連
- **59**: Impact-Packにwebui系の拡張（ワイルドカード、ディティーラー）。
- **124**: webui用ブラウザzen browserカックカク。（UIブラウザ互換）

#### その他ツール
- **67**: Quick Connection (custom node)。
- **223**: Veo 3.1 fast（クラウド動画生成）。
- **228**: APIキーノード/環境変数でキー管理（Gemini作成カスタムノード）。

これでログ内の全ツール関連話題を網羅。主にComfyUIのUI/カスタムノード/動画ツールが中心で、Forge Neo/nano-bananaは代替/簡易化理由で人気。