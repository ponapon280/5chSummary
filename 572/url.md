# 1. https://huggingface.co/
## No.141:	2025/08/25(月) 20:36:17.67 ID:5+wn1hrA0
 \>\>129 <br> モデル　少しサイズ大きいけど。 <br> loraも紹介されてますね。 <br>  <br> 自己責任で。 <br>  <br> <a href='https://huggingface.co/GuangyuanSD/Qwen-image-NSFW_RED-Q-Queen_of_Diamonds_fp8_e4m3fn'>https://huggingface.co/GuangyuanSD/Qwen-image-NSFW_RED-Q-Queen_of_Diamonds_fp8_e4m3fn</a> 
<br>

## No.471:	2025/08/26(火) 23:19:57.79 ID:+pf0p/2w0
 要る人おるか知らんけど、透過pngに関するbatにドラッグドロップするだけツール作ったで <br> （1）アルファチャンネルを無視してRGBのみの画像を出力するツール <br> （2）透過pngの透過処理されている部分を黒か白に塗りつぶすツール <br> pythonとpillow使ってて、ローカル生成環境ある人はpillowインストールすればそれだけでおｋ <br> 背景削除のツールによっては不要だったりするけど、さくっと上記の処理が複数ファイルで一括処理できる感じ <br> コードからreadmeからgeminiに出してもらったけど、ちゃんと機能しることは確認済み、何かあったら教えて <br> <a href='https://huggingface.co/skybear0719/png-image-tools'>https://huggingface.co/skybear0719/png-image-tools</a> 
<br>

## No.698:	2025/08/27(水) 20:40:14.56 ID:uq5qAV5Y0
 Wan2.2のS2Vが来てたから試してみたで <br> <a href='https://files.catbox.moe/yk5w7k.mp4'>https://files.catbox.moe/yk5w7k.mp4</a> <br> 動画を81フレームで出力するなら当然やけど音声も5秒のファイルを読み込ませた方がええな <br>  <br> Wan2.2 S2Vモデル(fp8) <br> <a href='https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/S2V'>https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/S2V</a> <br> オーディオエンコーダー(※要ComfyUIアップデート) <br> <a href='https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/audio_encoders'>https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/audio_encoders</a> 
<br>

## No.726:	2025/08/27(水) 23:28:28.29 ID:uq5qAV5Y0
 s2vのgguf来たでー <br> <a href='https://huggingface.co/QuantStack/Wan2.2-S2V-14B-GGUF'>https://huggingface.co/QuantStack/Wan2.2-S2V-14B-GGUF</a> 
<br>

## No.757:	2025/08/28(木) 01:31:19.75 ID:Nb+MSa2t0
 と、そんな事を言いながら最近また寝てる間にLECO量産し始めた模様 <br>  <br> ■hakushiMix_v14.1 用LECO格納場所 <br> （※解像度1280、個人的によく使うものは学習ステップ2倍、主にワイの性癖優先で増えてくでぇ。illustriousのLECOより大分効果強めやでー） <br> <a href='https://huggingface.co/datasets/mokyu2106/iroiro_data/tree/main/LECO/hakushiMix_v141'>https://huggingface.co/datasets/mokyu2106/iroiro_data/tree/main/LECO/hakushiMix_v141</a> <br>  <br> 流石に家に居ないときは学習放置するのが怖いので生成ペースゆっくりめ <br> 3090tiの時すら夏場に24時間学習放置とかまぁやってたんやけどなぁ <br> 冬早よぉ来んかなぁ <br>  <br> \>\>756 <br> 最近マザボ買い換えたばっかやでぇー <br> DDR6主流になるまでワイはDDR4で凌ぐんや…… 
<br>

# 2. https://mega.nz/
## No.676:	2025/08/27(水) 19:31:28.76 ID:clo3AFbJa
 QWEN-IMAGEのLoRa学習CAMEちゃんとRAdamScheduleFree動いたで <br> <a href='https://litter.catbox.moe/m773d9ml2nbav447.jpg'>https://litter.catbox.moe/m773d9ml2nbav447.jpg</a> <br> <a href='https://litter.catbox.moe/bw8gey56vl3tciic.jpg'>https://litter.catbox.moe/bw8gey56vl3tciic.jpg</a> <br> 学習が進むことは確認できたわ <br> RAdamScheduleFreeはちょっといじらんといかんけど… <br>  <br> リアスで生成したAI画像10枚4リピート5エポック <br> 動作確認用に解像度は512x512 <br> データセットはこれやで <br> <a href='https://mega.nz/folder/fcs1GDjA#5YdmoAHDrnaM0oJF34ZwzQ'>https://mega.nz/folder/fcs1GDjA#5YdmoAHDrnaM0oJF34ZwzQ</a> 
<br>

# 3. https://civitai.com/
## No.147:	2025/08/25(月) 21:11:30.75 ID:qSgMcBo20
 \>\>141 <br> これってlightx2vとコレ;をマージしたって書いてあるからMCNL使うんでも良いんじゃないかな？ <br> <a href='https://civitai.com/models/1851673?modelVersionId=2105899'>https://civitai.com/models/1851673?modelVersionId=2105899</a> <br>  <br> Flux NSFW MasterもFluxが出てから一月もかからずに出てたし結構データセット持って待ち構えている御仁がいるんじゃないかな 
<br>

## No.203:	2025/08/26(火) 02:13:29.13 ID:+pf0p/2w0
 サンイチ <br> リアスやけど鼻のスタイルを弄るLoRA <br> メイン目的はリアリスティックをフラットにすることだけど鼻を強調することも可 <br> catbox4んどるし、サンプルはcivitaiの方みてな <br> <a href='https://civitai.com/models/1896399/'>https://civitai.com/models/1896399/</a> <br>  <br> 前スレかその前かであったキャラLoRAにおける背景透過の話 <br> あれ透過後の画像、taggerでタグ付けするとwhite backgroundとされるんだけど <br> 透過は学習上黒色として扱われているから、black backgroundとタグ付けを修正しないと多分コンフリクトしてるわ <br> 今作ってたLoRAでタグのみをwhite→blackと変えて学習したら背景に無駄な要素引っ張ってくるのが明らかに減った <br> ガチるなら透過させて、単一色背景を複数色で作るとより良いはず、画像は同プロンプト同シードでの比較 <br> <a href='https://litter.catbox.moe/exyatgr8huxf4rd6.jpg'>https://litter.catbox.moe/exyatgr8huxf4rd6.jpg</a> <a href='https://litter.catbox.moe/0kt2t0yo0848wbez.jpg'>https://litter.catbox.moe/0kt2t0yo0848wbez.jpg</a> 
<br>

## No.293:	2025/08/26(火) 14:57:22.75 ID:wukn3cYq0
 Qwen image用「電話猫LoRA」を画像修正及びキャプションを適正にして学習し直しました <br> <a href='https://civitai.com/models/1893027/denwanekotelephone-cat'>https://civitai.com/models/1893027/denwanekotelephone-cat</a> <br> <a href='https://files.catbox.moe/swh0ms.webp'>https://files.catbox.moe/swh0ms.webp</a> <br> <a href='https://files.catbox.moe/nu3yf8.webp'>https://files.catbox.moe/nu3yf8.webp</a> <br> <a href='https://files.catbox.moe/rlyqfc.webp'>https://files.catbox.moe/rlyqfc.webp</a> 
<br>

## No.470:	2025/08/26(火) 23:18:19.05 ID:kmlnSXuH0
 \>\>359 <br> ほいよ <br> ワイも好きだからloraにした <br> <a href='https://litter.catbox.moe/lyb9u94ld4q3iiob.png'>https://litter.catbox.moe/lyb9u94ld4q3iiob.png</a> <br> <a href='https://civitai.com/models/1900414?modelVersionId=2151104'>https://civitai.com/models/1900414?modelVersionId=2151104</a> <br>  <br> dim8で作ったら <br> 瞳の中が一筆書きの星にならなくて作り直した <br> これは失敗版 <br> <a href='https://litter.catbox.moe/m7skp0xg9iviwx8o.png'>https://litter.catbox.moe/m7skp0xg9iviwx8o.png</a> 
<br>

## No.478:	2025/08/26(火) 23:53:30.98 ID:kmlnSXuH0
 髪型だけ欲しいよ;って人用 <br> <a href='https://litter.catbox.moe/2dnjicemjchrabzu.png'>https://litter.catbox.moe/2dnjicemjchrabzu.png</a> <br> <a href='https://litter.catbox.moe/zhzlsxbrmqph8keh.png'>https://litter.catbox.moe/zhzlsxbrmqph8keh.png</a> <br> <a href='https://civitai.com/models/1900414?modelVersionId=2151208'>https://civitai.com/models/1900414?modelVersionId=2151208</a> <br>  <br> \>\>475 <br> サンガツ！ 
<br>

## No.790:	2025/08/28(木) 08:42:56.69 ID:zDwTmL3E0
 銅鏡のLoRAやで。新版は鏡の外側に玉のついたやつ（鈴鏡）も出せるやで。 <br> <a href='https://civitai.com/models/184385'>https://civitai.com/models/184385</a> <br>  <br> おまけ機能としてchromatic_aberrationとかsymmetrical dockingの効きがよくなり <br> 棒がでにくくなるはずやで… <br> <a href='https://files.catbox.moe/qeso2q.png'>https://files.catbox.moe/qeso2q.png</a> <br> <a href='https://files.catbox.moe/7q0jtm.png'>https://files.catbox.moe/7q0jtm.png</a> <br> <a href='https://files.catbox.moe/k08itp.png'>https://files.catbox.moe/k08itp.png</a> <br> <a href='https://files.catbox.moe/dhxnzc.png'>https://files.catbox.moe/dhxnzc.png</a> <br> <a href='https://files.catbox.moe/cksnkj.png'>https://files.catbox.moe/cksnkj.png</a> <br> <a href='https://files.catbox.moe/0ewrpy.png'>https://files.catbox.moe/0ewrpy.png</a> 
<br>

