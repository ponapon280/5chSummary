# 1. https://huggingface.co/
## No.277:	2025/08/16(土) 17:30:54.72 ID:4vdNXaL00
 Wan 2.2用のFastMixを公開してEasyWan22で対応しといたで <br> <a href='https://huggingface.co/Zuntan/Wan22-FastMix'>https://huggingface.co/Zuntan/Wan22-FastMix</a> <br>  <br> ガチャ生成時のゴーストと動きの品質が手元では改善されとる <br> 利用LoRAに合わせて動きや加減速を調整するためのEnhanceMotionノードも追加しといたで <br>  <br> あとPyTorch 2.8.0でトラブル起きとるニキがおるっぽいんで2.7.1に巻き戻したわ <br> 2.8.1待ちやろかな 
<br>

## No.478:	2025/08/17(日) 00:36:17.45 ID:y+MfCnAA0
 ■Qwan Lora作成終わった（ほぼ5090下画像設定でほぼ1時間丁度）　<a href='https://files.catbox.moe/r93bpr.png'>https://files.catbox.moe/r93bpr.png</a> <br>  <br> ■学習時設定（学習素材はなんか乱交正常位っぽいエロいAI製画像4枚、自然言語無しDanbooruタグ付け） <br> <a href='https://files.catbox.moe/pdj1hz.png'>https://files.catbox.moe/pdj1hz.png</a> <br> （一番下のsample configurationは単に「途中経過の出来映えを確認するための画像生成」なだけなので生成しないように適当に設定） <br>  <br> ■成果物例（左がLora無し、右がLoraあり） <br> <a href='https://files.catbox.moe/io9sy1.jpg'>https://files.catbox.moe/io9sy1.jpg</a> <br> ※右のモザイクは勝手に入ったｗ <br>  <br> ■Qwan超適当Lora（多分近いうちに消す）<a href='https://huggingface.co/datasets/mokyu2106/iroiro_data/tree/main/LoRA/Qwan'>https://huggingface.co/datasets/mokyu2106/iroiro_data/tree/main/LoRA/Qwan</a> 
<br>

## No.728:	2025/08/17(日) 17:36:47.32 ID:1AJRP5Um0
 SageAttention3来てるやんけ！！！！！111 <br> <a href='https://huggingface.co/jt-zhang/SageAttention3'>https://huggingface.co/jt-zhang/SageAttention3</a> <br>  <br> 現在、SageAttention3は以下に適しています。 <br>  <br>     ビデオ生成モデル:CogVideoX-2B、HunyuanVideo、餅。 <br>     FluxとStable-Diffusionを含むほぼすべての画像生成モデル。 <br>  <br>  python>=3.13 , torch>=2.8.0, CUDA >=12.8 <br>  <br>  <br> QwenもSageAttention対応しねーかな 
<br>

## No.738:	2025/08/17(日) 18:10:58.64 ID:TS05jShp0
 生成した画像を指定タグでフォルダに一括でコピーや移動したりできる、 <br> 生成画像一括分類ツール作ったから公開するで <br>  <br> 最初に非表示にする「品質タグ」や分類するトリガーの「キャラタグ」や「シチュエーションタグ」を選んで、 <br> 分類ポチーで一括でフォルダに分類できる便利ツールや <br> キャラタグで作成したフォルダの下に複数のシチュフォルダを作って分類したりできるで <br> クオリティタグとか、非表示にしたいタグは分類して保存しておけば次回以降も非表示にできるで <br> ワイが個人的に使うために作っただけの奴やから細かいことは堪忍やで <br> A1111で作った画像用やから、comfy生成画像の動作は未確認や。 <br> comfyで使えんかったらchatGPTに投げつけてcomfyタグ対応するように各々好きに改造してクレメンス <br>  <br> <a href='https://huggingface.co/14matsu/image_tag_sorter/tree/main'>https://huggingface.co/14matsu/image_tag_sorter/tree/main</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.308:	2025/08/16(土) 18:22:56.52 ID:odpIo3WL0
 新型コロナもほとぼり冷めたし、フェルニアのコロナ（副花冠）を出すためのLoRAやで <br> <a href='https://civitai.com/models/1871794'>https://civitai.com/models/1871794</a> <br>  <br> 念のためgape好きな人が装備できるようにしておいたやで <br> <a href='https://files.catbox.moe/ljzudg.png'>https://files.catbox.moe/ljzudg.png</a> <br> <a href='https://files.catbox.moe/4qd4as.png'>https://files.catbox.moe/4qd4as.png</a> <br> <a href='https://files.catbox.moe/9cn9qa.png'>https://files.catbox.moe/9cn9qa.png</a> <br> <a href='https://files.catbox.moe/cfjluc.png'>https://files.catbox.moe/cfjluc.png</a> 
<br>

## No.330:	2025/08/16(土) 19:05:56.41 ID:9YbfiBsAa
 画像2枚をWAN2.2で動かしてLoRa作ってみたけど割と実用的やな <br> <a href='https://files.catbox.moe/s3s9t0.mp4'>https://files.catbox.moe/s3s9t0.mp4</a> <br>  <br> <a href='https://files.catbox.moe/zsmyvv.webp'>https://files.catbox.moe/zsmyvv.webp</a> <br> <a href='https://files.catbox.moe/9josuc.jpg'>https://files.catbox.moe/9josuc.jpg</a> <br> CIVITAI健全設定やないと見えないかもしれんサンプル画像の判定真っ赤になってたから消えたらごめんな <br> <a href='https://civitai.com/models/1871827/miyu-edelfelt-swimsuit-costumelancer'>https://civitai.com/models/1871827/miyu-edelfelt-swimsuit-costumelancer</a> 
<br>

## No.490:	2025/08/17(日) 01:04:30.56 ID:wubuE/uw0
 回してるLoRAがあるけどこれが手っ取り早いんちゃう？ <br> <a href='https://civitai.com/models/1865925'>https://civitai.com/models/1865925</a> <br> あと回すのはframepackが得意というのを聞いた 
<br>

## No.601:	2025/08/17(日) 11:17:08.76 ID:w+BHt2kPa
 QWEN-IMAGE学習を自然文とBooluタグで生成比較したで <br> <a href='https://files.catbox.moe/5faff1.jpg'>https://files.catbox.moe/5faff1.jpg</a> <br> おなじ画像12枚,学習率2e-4,オプティマイザーadamw8bit <br> ツールはMusubi-Tuner,学習時間はRTX5090を使って1時間20分程度 <br> タグとキャプションはこんな感じ自然文はJoyCaptionで自動生成や <br> <a href='https://files.catbox.moe/17tw0l.jpg'>https://files.catbox.moe/17tw0l.jpg</a> <br> <a href='https://files.catbox.moe/dx03v6.jpg'>https://files.catbox.moe/dx03v6.jpg</a> <br>  <br> LoRaはCivitaiや <br> <a href='https://civitai.com/models/1871827?modelVersionId=2120952'>https://civitai.com/models/1871827?modelVersionId=2120952</a> 
<br>

## No.636:	2025/08/17(日) 13:06:05.86 ID:epNxVwHd0
 \>\>615 <br> wan21用だが、22でも使ってる、Hi/Low両方に適用させ、強度は0.8ぐらいかな <br> <a href='https://civitai.com/models/1796502?modelVersionId=2033053'>https://civitai.com/models/1796502?modelVersionId=2033053</a> 
<br>

## No.772:	2025/08/17(日) 19:03:56.60 ID:uaDCFMn10
 CG板で話題に出てたLoRAを使ってみた <br> 4step生成やから画質はあれやけど次の動画の内容を考えて足して最後に音入れるの楽しいわ <br>  <br> ただプロンプトで2人動きや車からカメラすべて指示しないと動かないのは自由文の定めやな <br> 棒人間しか書けん人間やが絵コンテとか演出とか考える人がホント凄いと思う <br>  <br> ♪音出ます <br> <a href='https://files.catbox.moe/him8to.mp4'>https://files.catbox.moe/him8to.mp4</a> <br>  <br> <a href='https://civitai.com/models/1872525/wan22-simple-and-pure-color-anime-style'>https://civitai.com/models/1872525/wan22-simple-and-pure-color-anime-style</a> 
<br>

## No.895:	2025/08/18(月) 11:05:15.52 ID:p9zVx1v20
 \>\>883 <br> かなりキモいんで使ったこと無い＝無責任モードやけどこういうLoRAが効くかもしれない <br>  <br> <a href='https://civitai.com/models/1814871?modelVersionId=2054618'>https://civitai.com/models/1814871?modelVersionId=2054618</a> 
<br>

