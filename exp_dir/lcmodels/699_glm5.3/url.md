# 1. https://huggingface.co/
## No.101:	2026/09/21(月) 11:14:50.83 ID:KfHNugMh0
 サンイチ <br> もう10日も前やけど、Training Adapter LoraをCircleStone Labsが出しとるんやね <br> 動画周りのlora作りはさっぱりやけど…anima作ったとこのだから気になっただけで <br> <a href='https://huggingface.co/circlestone-labs/MiniMax-H3-Image-Training-Adapter'>https://huggingface.co/circlestone-labs/MiniMax-H3-Image-Training-Adapter</a> 
<br>

## No.271:	2026/09/21(月) 19:59:47.01 ID:Nw7IDxdT0
 \>\>210 <br> ここの6に書いてあるように基本的にはsubject_definitionsで<Subject 1>とかに<Picture 1>とかのアンカーなしで定義付けするだけやで <br> <a href='https://huggingface.co/datasets/malcolmrey/various/blob/main/h3-center/docs/MINIMAX_H3_REFMODS_INSTALLATION_AND_USAGE_GUIDE.md'>https://huggingface.co/datasets/malcolmrey/various/blob/main/h3-center/docs/MINIMAX_H3_REFMODS_INSTALLATION_AND_USAGE_GUIDE.md</a> <br> VLMでプロンプト作りたい場合は、参照画像としてrefmodに梱包した画像のどれかを渡してプロンプトを作らせ、<Picture 1>の部分を手動もしくはAIで修正するのがいいんじゃないか <br> ↓は立ち絵をVLMに渡してプロンプトを書かせた後、<Picture 1>を&quot;the woman, light brown hair, wearing navy school uniform&quot;と手で書き換えたやつ <br> 普通のref2vaでよくね？とか言ってはいけない <br> <a href='https://tadaup.jp/9LZXTkVh.mp4'>https://tadaup.jp/9LZXTkVh.mp4</a> 
<br>

## No.853:	2026/09/23(水) 18:47:23.77 ID:R1VNS7wZ0
 God KijaiがMing-Image始めてる <br> <a href='https://huggingface.co/Kijai/Ming-Image-ComfyUI'>https://huggingface.co/Kijai/Ming-Image-ComfyUI</a> 
<br>

# 2. https://mega.nz/
## No.513:	2026/09/22(火) 16:05:33.80 ID:mdA9PYkw0
 ニキらにちょいと実証試験のお願いやで。 <br> minimax ref2va 1f Lora学習の試験で、いわゆる上下運動的なアレの改善で使えないかと試作してみたんや。 <br> animaで正常位と騎乗位で上下したり何か赤かったり白かったりするアレが流れたりしてる素材作って学習させてみた。 <br> 一応、ヴァ〇ナやペ〇スといった直接表現で動いてくれるはず。さっき焼けたばかりでワイもテストしてるんやけど、なかなか大変でな。 <br> 本家ref2va基準で効能として今まで確認したのは、動きが本家よりねっちょりするのと、アソコまわりの表現が淡いアニメ調になるくらいやな。 <br> あと素材が少なくて想定してない動きになるかもしれん。化け物出たらごめんな。 <br> これがうまくいけば、RTX4090以上でワイ以上の素材持ってるニキがもっと良いLoraを作れる道ができたことになる。 <br>  <br> 最後に、ref2va用なことに注意と、Megaなんで制限いっぱいになったらごめんな。 <br>  <br> <a href='https://mega.nz/folder/lClyxA6L#NrbgLwTotsu8vh8uKqy6YQ'>https://mega.nz/folder/lClyxA6L#NrbgLwTotsu8vh8uKqy6YQ</a> 
<br>

## No.968:	2026/09/23(水) 23:57:04.39 ID:owih4C0w0
 minimax h3 ref2va 1f学習再びやで。 <br> 前回紹介したチ〇コLoraの疑いがあるマ〇コLoraの改善版作ってみたで。フォルダのv2が最新や。 <br>  <br> <a href='https://mega.nz/folder/lClyxA6L#NrbgLwTotsu8vh8uKqy6YQ'>https://mega.nz/folder/lClyxA6L#NrbgLwTotsu8vh8uKqy6YQ</a> <br>  <br> ・ 学習画像素材を全部見直してanimaで再生成および追加。10組20枚から16組32枚に増加。 <br> ・ 前回と同様に騎乗位と正常位のピストンと射精に対応、ただしまだ騎乗位しか確認してない。 <br> ・ 素材改善の結果としてアソコの挿入表現が少しだけ改善されたはず。 <br> ・ なお背景情報書き忘れにより背景へのLora浸食が酷い。白浸食する上に同じ白背景の参照素材まで動画に引っ張り上げようとするのは驚いた。 <br> ・ 過学習気味でもあるので、使う場合はまず強度0.6くらいから調整をお勧めするで。 <br> ・ AI素材でこれだけ安定させられるならリアル素材だともっと良いものになるのか、な？ 
<br>

# 3. https://civitai(com/red 共用)
