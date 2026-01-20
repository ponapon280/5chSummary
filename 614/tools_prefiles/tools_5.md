### 抽出された「ツール」に関する話題

ログ全体をスキャンし、指定されたツール（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなど）に該当する話題のみを抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）関連の話題は一切除外。ツールの選ばれている理由（利便性、機能、問題点など）が明記されている場合も併記。

#### ComfyUI (comfy) 関連
- **843**: ComfyUIワイ、出力した画像にタグだけ画像に記録させてワークフローは記録させない方法を模索  
  *(ComfyUI使用者の悩み: タグのみ記録、WF非記録の方法探し)*
- **847**: >>843 ComfyUI-D2SendEagleとかComfyUI-SaveWithMetaDataとか多機能な出力ノードではタグとワークフローの保存は別トグルで選べた気がする うろおぼえだから違ってたらすまぬ  
  *(ComfyUI拡張ノード: ComfyUI-D2SendEagle, ComfyUI-SaveWithMetaData。理由: タグとWF保存を別トグルで制御可能、多機能)*
- **848**: >>843 ↓のSD Prompt SaverとSD Prompt Readerを使ってるけどWF保存機能はないんで うっかり触ってしまっていつのまにかWF保存設定になってたなんて事故は発生しないなんで安心して使える ただ古くて更新されていないんで愛用しながらも誰かこれ系で新しい拡張ノードを作ってほしいとは思ってる  
  *(ComfyUI拡張ノード: SD Prompt Saver, SD Prompt Reader。理由: WF保存なしで事故防止、安心して使用可能。ただし古く更新停止)*
- **841**: チャッピーに言えばpnginfoもexifに残すjpeg変換スクプリトも作ってくれるで ただjpegのexifは仕様的に64KB超えるとエラーになったはず comfyとかWFによっては超えちゃうからjpegからwebp派になったわ  
  *(comfy: WFがメタデータ64KB超え問題を引き起こすため、jpeg→webp移行の理由)*
- **853**: 昨日まで普通に使えていたTensortRT関連のノードが急に使えなくなったぞ アプデしてないしWFも弄ってないのになぜ  
  *(TensorRT関連ノード: ComfyUIのノードで突然使用不可)*
- **855**: fatal: destination path 'ComfyUI-Rife-Tensorrt' already exists and is not an empty directory. って出てgit cloneも出来なくなってる どういうことや  
  *(ComfyUI拡張: ComfyUI-Rife-Tensorrt。インストールエラー発生)*
- **857-858**: >>855 そのまま書いてる通りやろ チャッピーにでもコピペして対応を仰げると良い  
  *(ComfyUI-Rife-Tensorrtのエラー対応策としてチャッピー活用提案)*
- **901**: (一部ComfyUI言及なしだが関連文脈で)  
  *(間接: ComfyUI環境でのモデル載せ替え問題)*
- **911**: EasyWan22のブロックスワップノードとComfyUI最新のメモリ制御で全然挙動違うから 「動画」といったときに古いEasyWan22環境と今最新のComfyUI環境で話合わねえんだよな  
  *(ComfyUI最新のメモリ制御: EasyWan22のBlockSwapノードと挙動違い。理由: 最新版でメモリ制御改善、旧環境との互換性問題)*
- **939**: >>911 なんならBlockSwapはコミュニティの方で強制的に廃止されとるからな 今は入れても使えないようになってる 親切なこっちゃで  
  *(BlockSwapノード: ComfyUIコミュニティで廃止。理由: 強制廃止で使用不可)*
- **957**: >>901 実際この意見は方向は正しいと思うで ComyiUIのメモリマネジメントが過渡期なのは明らかやんコードにあるargが無視されたりするし ・Pro6000みたいな潤沢なメモリのグラボ ・Unifiedメモリのマシン ・グラボに乗り切る小さいモデルを使う時 ・複数グラボで合計VRAMがモデルサイズを上回る のときは.to('cpu')に一旦落とす必要が無いのに毎回落としてるからIO待ちが無駄に長い 根本的にはhuggingfaceのsafetensorsライブラリがCPUオフロード前提なのがあんまりよくない（pytorchデフォのローダなら直接cuda指定も出来る） 一旦RAMに落とす戦略はどのパターンでも一番バグなく実装出来そうから先にやっただけやろから>>901が総出で叩かれてる理由がよくわからない  
  *(ComfyUIのメモリマネジメント: 過渡期でCPUオフロード強制によるIO待ち問題。理由: バグ少なく実装された苦肉の策、huggingface safetensorsの制約)*

#### その他のツール関連（指定例に準ずるもの）
- **840**: としあきだかたかあきだかが作ったツールにはご丁寧にPNGのPNGInfoからJPGのEXIFに情報引き継ぐようなツールあった記憶が あと彼のオートモザイクもご丁寧にモザイク処理後に情報を引き継ぐ(わざわざ書き込む)仕様になっていたみたい  
  *(特定ツール: PNG→JPGメタデータ引き継ぎツール、オートモザイクツール。理由: メタデータ/モザイク処理後に情報保持仕様)*

#### 抽出外（モデル関連のため除外）
- Wan, Qwen, リアスなどの言及多数（例: 844,850,899など）はモデルとして除外。
- チャッピー（ChatGPTの愛称？）は生成AIツールとして曖昧だが、ComfyUI拡張作成支援として補助的にのみ言及。

**総括**: 主にComfyUIとその拡張ノード（D2SendEagle, SaveWithMetaData, SD Prompt Saver/Reader, Rife-Tensorrt, TensorRT, BlockSwapなど）の話題が集中。選好理由は「タグ/WF制御の柔軟性」「事故防止」「メモリ管理の進化/問題点」「メタデータ処理」など実用面。A1111/webUI/SUPIR/nano-bananaなどは未言及。