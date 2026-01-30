### 抽出されたツール関連話題

ログから生成AI関連の**ツール**（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana などの画像生成/学習ツールやUI、ノード、カスタム拡張）をすべて抽出。モデル（NovelAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen など）に関する言及は除外。ツールの選定理由が明記されている場合のみ、その理由を併記。各レス番号と該当文を引用し、まとめ。

#### ai-toolkit (LoRA学習ツール)
- **23**: 「Zimageでai-toolkitで試しにLora作成、初期設定で解像度1024の範囲で回した VRAMは15.0使用、16GBならギリギリかな、1536は24GBクラスじゃないと無理だね 生成にえらい時間かかるし、turbo使えないなら触りだけして様子見で良いかなと」  
  → VRAM使用量の目安として言及（16GBでギリギリ可能）。
- **61**: 「てかみんなai-toolkitで学習回しとるんやな qwenの時はmusubi tunerと半々ぐらいやった気がするんやけども」  
  → 学習ツールとして主流（qwen時よりシェア増加？）。
- **149**: 「なんかAi-toolkitでZ-imageのLora学習してたら1時間半で終わる予定と表示されてたやつがしばらくして見直したら5時間かかることになってたんだけどこれなんでなんだろ」  
  → 学習時間予測の不具合言及。
- **150**: 「ai-toolkitで50枚をbatch size 4で300ステップ、3090で画風LoRA作ってみたが約1時間程度かかった 結果としては使い物にならなかったので今日はグラボに徹夜してもらって3000ステップくらい回すで」  
  → 3090でbatch size 4/300ステップで1時間程度（画風LoRA作成）。
- **208**: 「Zimageの学習用にAITOOLKITをアプデ こっちもComfyUIと同じく積極的にRAM使うように制御してるんかな？共有メモリに出ても処理が落ちないという状況になってる(前は共有メモリにはみ出ると処理速度が一桁さがってた) 5070Tiで1024学習が3.5s/it、同条件でSDXLは1.0s/itだったから34倍ほど学習時間が必要だけど実用圏内なのが非常によろしい」  
  → アプデでRAM活用改善（共有メモリ時速度低下解消）、5070Tiで1024学習3.5s/it（SDXL比34倍時間だが実用的）。
- **212**: 「ワイがデフォルト設定でAi-toolkit使ったときはサンプルが500stepあたりからもうおかしくなって人体構造がめちゃくちゃ破綻しまくってたんやけどこれはワイ環なんかな」  
  → デフォルト設定で500step以降破綻（ユーザー設定ミス疑い）。

#### musubi tuner (LoRA学習ツール)
- **53**: 「zimageの学習回してみたけどmusubi tunerでblockswapすれば12GBでも1536サイズなら余裕のよっちゃんやな…軽すぎる(VRAM使用量10GB未満) かなり敷居は低いと思うわ」  
  → blockswap併用でVRAM12GB/1536サイズ可能（VRAM10GB未満、敷居低い理由）。
- **61**: 「qwenの時はmusubi tunerと半々ぐらいやった気がするんやけども」  
  → qwen時とai-toolkitのシェア半々だった過去言及。

#### ComfyUI (comfy) および関連ノード/機能
- **37**: 「12gbユーザーは出力するだけならできるんちゃうか foooocusみたいなのやcomfyでどうにかしてもろて」  
  → VRAM12GBユーザー向け出力ツールとして。
- **155**: 「comfyのテンプレ使ったらノイズ消えたわ」  
  → 公式テンプレでノイズ解消。
- **162**: 「VRAM12GB民ならRAM64GB積んでればUnetLoaderDisTorch2MultiGPUノードでvirtual_vram_gbの値を5にしたらZ-Imageのbf16も回せるで 1280x720/cfg4.0/step28で約1分30秒や」  
  → UnetLoaderDisTorch2MultiGPUノードでVRAM12GB+RAM64GBでbf16対応（1280x720/28stepで1分30秒）。
- **163**: 「--use-sage-attention消したらノイズも消えたで」 / **165**: 「--use-sage-attention外して必要なものに手動設定すればいいだけ てか--use-sage-attentionは最初だけ効いて後は効いてないことがあるし」  
  → 起動引数--use-sage-attentionでノイズ発生（オフ推奨、手動設定で対応）。
- **168**: 「サゲアテンションはきじゃいノードで都度有効がよろし」  
  → sage attentionはKijaiノードで都度有効化推奨。
- **172**: 「MultiGPUノード使わんでもVRAM12GBあれば公式のテンプレートでもbf16いけるやろ」 / **177**: 「通常のUnetLoaderでも出来るか出来ないかで言えば『出来る』が時間は倍になる」 / **181**: 「MultiGPUって単語使う奴1人しかいないはず」 / **183**: 「MultiGPU使わんと動画生成やQIEは時々VRAM100％のまま止まるわね」 / **184**: 「生成出来るならMultiGPUノード使う必要あらへんやろ」 / **204**: 「MultiGPU使った方がメモリ管理が安定する環境があるのは確かや --reserve-vram入れてもvram食いつくされてブラックアウトしたこと何度かあるし」  
  → MultiGPUノード（DistorchmultiGPU?）でメモリ安定（ブラックアウト回避、動画生成安定）。
- **196**: 「DistorchmultiGPUってComfyUIがnvfp4に対応したあたり(Ver0.9.0ぐらい)から完全に死んでね？ ... Z-imageをどっちに入れるか迷ってたけどZimageがSageAttention使えないならLTX-2用のSageAttentionなしの最新環境で構築するか」  
  → DistorchmultiGPUノード不安定（ComfyUI Ver0.9.0以降、SageAttention非対応時使用検討）。
- **199**: 「完全に非推奨になったのはBlock Swapの方やな」 / **203**: 「Block Swapは非推奨どころかdeprecated扱いでノード入れても機能しなくさせられてる BANやで」  
  → Block Swapノード非推奨/deprecated。
- **202**: 「DistorchmultiGPUはComfyUI本体がRAM活用する前はもはや必須レベルだったけど ComfyUIがそれなりに対応してる＆DistorchmultiGPUのアプデがされてない」  
  → 過去必須だったが現在非推奨（ComfyUI本体のRAM活用で代替）。
- **205**: 「ComfUI v0.11.0に上げてZ-Image公式レンプレからモデル導入したわ」  
  → Ver0.11.0アップデートと公式テンプレ使用。
- **215**: 「VLMにお願いすればいい comfy上でやればバッチ処理も簡単」 / **219**: 「comfyui上でタグ付けできるんです？」  
  → ComfyUI上でVLMキャプション/タグ付けバッチ処理可能。
- **216**: 「キャプションはQwenVLとWDに任せたらええ」  
  → WD（WD14 tagger?）でキャプション。

#### foooocus (UIツール)
- **37**: 「foooocusみたいなのやcomfyでどうにかしてもろて」  
  → VRAM12GBユーザー向け簡易出力ツール例。

#### その他ツール言及
- **105**: 「ワイはeasyreforgeneoでziでポチーして4545したいんや」  
  → easyreforgeneo（UI/ツール?）で簡易生成希望。

**抽出まとめ**:  
- 主力ツールは**ai-toolkit**（LoRA学習主流、RAM改善で実用的）と**ComfyUI**（ノード/引数多用、VRAM低減・安定化で低スペ対応）。**musubi tuner**は過去シェア高。**foooocus**は簡易代替。選定理由は主に**VRAM/RAM効率**（12GB対応、速度安定）、**ノイズ/不安定解消**、**学習時間実用性**。ComfyUI関連ノード（MultiGPU, sage attention, Block Swap）はメモリ管理/速度最適化で議論多。