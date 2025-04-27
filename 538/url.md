# 1. https://huggingface.co/
## No.312:	2025/04/25(金) 20:56:47.94 ID:9Oy3hQ+Y0
 wanを改良したSkyReels-V2がベース24fpsでwanモデルと交換するだけで <br> 同じワークフローで使えるし今までのloraも使えて動きも安定するしええ感じなのに <br> reddit位でしか話題になってないのが意味分からんで <br> もちろんKijai神が量子化してるから720Pモデルでもサイズも一緒で試しやすい <br> <a href='https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels'>https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels</a> 
<br>

## No.342:	2025/04/25(金) 22:47:37.82 ID:c0GbygxY0
 Canary-TTS-0.5Bをつまんでみたで <br> プロンプトで声を指定できるんでヤンデレとツンデレの声をChatGPTに説明してもろて生成してもろた <br> シードの振れ幅が大きかったりコントロールがむずかったりやが可能性は感じるで <br> サンプルコードからの変更はmax_new_tokensを512にして長くしただけや <br>  <br> <a href='https://yyy.wpx.jp/2025/04/CanaryTts_0_Tundere.mp3'>https://yyy.wpx.jp/2025/04/CanaryTts_0_Tundere.mp3</a> <br> <a href='https://yyy.wpx.jp/2025/04/CanaryTts_0_Yandere.mp3'>https://yyy.wpx.jp/2025/04/CanaryTts_0_Yandere.mp3</a> <br>  <br> <a href='https://yyy.wpx.jp/2025/04/CanaryTts_1_Tundere.mp3'>https://yyy.wpx.jp/2025/04/CanaryTts_1_Tundere.mp3</a> <br> <a href='https://yyy.wpx.jp/2025/04/CanaryTts_1_Yandere.mp3'>https://yyy.wpx.jp/2025/04/CanaryTts_1_Yandere.mp3</a> <br>  <br> <a href='https://huggingface.co/2121-8/canary-tts-0.5b'>https://huggingface.co/2121-8/canary-tts-0.5b</a> 
<br>

## No.628:	2025/04/26(土) 22:33:11.70 ID:s6fuhg6C0
 \>\>590 <br> 実は元画像の方の緑のシャリアブルおじさんの方がLoRA込みで手間掛かっとったりするで <br>  <br> \>\>601 <br> 元はコレやが顔がリアルに持ってかれるんでイラストでは使わんほうが良さげやったで <br> <a href='https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs'>https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs</a> 
<br>

## No.880:	2025/04/27(日) 20:26:06.68 ID:mlNwb/CA0
 \>\>852 <br> ComfyUIの最新版が対応しているからCofmyUIとしてはごく標準的な、モデルとClip, VAEのロード、ClipText Endocder(PosとNeg)、KSampler(Advanced)->VaeDecode->Imageという流れは基本的に他のモノとおなじやね。 <br> ただClipを４つ使うのでQuadrupleClipLoaderを使うのとModel LoaderとSamplerの間にModelSamplingSD3を挟むのが特殊な程度（ModelSamplingSD3はSD3以降のFlow系は標準的に使っているけど） <br> 面倒なのはモデルロードかもね <br> 多分こちらに従ってモデル落としてきてサンプルワークフロー入れれば使えるはず（自分は別ルートでセットアップしたので細かいところは未確認） <br> <a href='https://comfyui-wiki.com/ja/tutorial/advanced/image/hidream/i1-t2i'>https://comfyui-wiki.com/ja/tutorial/advanced/image/hidream/i1-t2i</a> <br> 量子化はfp8_e4m3fnで4090なら溢れない　5090ならfp16でいけるらしい <br>  <br> ただUncensoredモデル(Llamaとかモデルとか）を使いたい時はちょっと面倒になる。 <br> モデルはこのあたりで良いだけど <a href='https://civitai.com/models/1498292?modelVersionId=1701111'>https://civitai.com/models/1498292?modelVersionId=1701111</a> <br> Llamaは <a href='https://huggingface.co/John6666/Llama-3.1-8B-Lexi-Uncensored-V2-nf4/tree/main'>https://huggingface.co/John6666/Llama-3.1-8B-Lexi-Uncensored-V2-nf4/tree/main</a> か\>\>310のモデルを使うと良いんだけど自分でsafetensors一個に纏めないといけない <br> あとClipもGGUF版使う場合はGGUF Cutom NodeにGGUF Quadruple Clip Loaderがあるよ 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.114:	2025/04/24(木) 17:36:16.98 ID:AE5fJKPo0
 lillyMix更新したで<a href='https://civitai.com/user/yyy1026'>https://civitai.com/user/yyy1026</a> <br> これもIL2.0ベースで自然言語推奨＆ネガポジタグいらずや <br> <a href='https://files.catbox.moe/uxdfdf.webp'>https://files.catbox.moe/uxdfdf.webp</a> <br> <a href='https://files.catbox.moe/z2jl7j.webp'>https://files.catbox.moe/z2jl7j.webp</a> 
<br>

## No.153:	2025/04/24(木) 20:01:58.93 ID:hjNMR9a10
 思いから使っている人少ないと思うけどHiDreamも下を脱いでくれるモデル出てきたね <br>  <br> <a href='https://civitai.com/models/1498292/hidream-i1-fp8-uncensored-fulldevfast?modelVersionId=1701111'>https://civitai.com/models/1498292/hidream-i1-fp8-uncensored-fulldevfast?modelVersionId=1701111</a> <br>  <br> <a href='https://files.catbox.moe/sb2nah.webp'>https://files.catbox.moe/sb2nah.webp</a> <br> <a href='https://files.catbox.moe/gi8et6.webp'>https://files.catbox.moe/gi8et6.webp</a> <br> ガチエロは未だだけどdiffusion-pipeで学習できるようになったらしいのでこれからに期待 <br>  <br> あとpytorch 2.7に上げたら生成が少し早くなった（85秒くらい->63秒くらい@4090) 
<br>

## No.292:	2025/04/25(金) 19:05:59.00 ID:c0GbygxY0
 EasyWanVideoに1枚の画像から動画を量産するサンプルと手順を追加しといたで <br>  <br> <a href='https://files.catbox.moe/9xuoj1.webp'>https://files.catbox.moe/9xuoj1.webp</a> <br> <a href='https://yyy.wpx.jp/2025/04/20250425_doublejob_1_s.mp4'>https://yyy.wpx.jp/2025/04/20250425_doublejob_1_s.mp4</a> <br> <a href='https://yyy.wpx.jp/2025/04/20250425_doublejob_2_s.mp4'>https://yyy.wpx.jp/2025/04/20250425_doublejob_2_s.mp4</a> <br> <a href='https://yyy.wpx.jp/2025/04/20250425_doublejob_3_s.mp4'>https://yyy.wpx.jp/2025/04/20250425_doublejob_3_s.mp4</a> <br> <a href='https://yyy.wpx.jp/2025/04/20250425_doublejob_4_s.mp4'>https://yyy.wpx.jp/2025/04/20250425_doublejob_4_s.mp4</a> <br>  <br> ワイ環ではこのLoRAの打率が高めやったわ <br> <a href='https://civitai.com/models/1395313?modelVersionId=1610465'>https://civitai.com/models/1395313?modelVersionId=1610465</a> 
<br>

## No.294:	2025/04/25(金) 19:25:35.34 ID:BPgBf2Rc0
 あんまりここでは需要はないと思うけどHiDream I1のLoRA学習がdiffusion-pipe出来るというのでお試し <br> <a href='https://civitai.com/articles/13882'>https://civitai.com/articles/13882</a> <br> 概ね書いてある方法でいけたけどHuggingFaceのtokenの設定（readonlyとかにしとかないといけない）で少しハマった <br>  <br> あとVScodeは入れてない<-入れるほどのテキスト編集じゃない <br>  <br> Epoc170くらいまで回したけど絵が汚くなるのでEpoc60くらいでLoRA強度で微調整が良いみたい <br> <a href='https://files.catbox.moe/ws29tr.webp'>https://files.catbox.moe/ws29tr.webp</a> <br>  <br> ただ顔への影響も結構出ているのでLR下げてEpoc増やしたほうが良いのかなあ 
<br>

## No.330:	2025/04/25(金) 22:05:13.46 ID:BPgBf2Rc0
 \>\>310 <br> ワイかもしれん　サンガツ　明日にでも試してみるわ　GGUF版のほうがお手軽そうやね <br>  <br> コレにClip/TextEncoder等のGGUF版も入っていたので使ってみているけど違いがよくわからんかった <br> <a href='https://civitai.com/models/1496362/hidream-full-gguf-q5km-uncensored?modelVersionId=1692682'>https://civitai.com/models/1496362/hidream-full-gguf-q5km-uncensored?modelVersionId=1692682</a> 
<br>

## No.591:	2025/04/26(土) 20:17:24.98 ID:XEKJWiff0
 Uncensored の Text Encoder 試してみるんご <br> <a href='https://civitai.com/articles/13522/hunyuan-video-what-model-to-use-for-8gb-24gb'>https://civitai.com/articles/13522/hunyuan-video-what-model-to-use-for-8gb-24gb</a> 
<br>

## No.880:	2025/04/27(日) 20:26:06.68 ID:mlNwb/CA0
 \>\>852 <br> ComfyUIの最新版が対応しているからCofmyUIとしてはごく標準的な、モデルとClip, VAEのロード、ClipText Endocder(PosとNeg)、KSampler(Advanced)->VaeDecode->Imageという流れは基本的に他のモノとおなじやね。 <br> ただClipを４つ使うのでQuadrupleClipLoaderを使うのとModel LoaderとSamplerの間にModelSamplingSD3を挟むのが特殊な程度（ModelSamplingSD3はSD3以降のFlow系は標準的に使っているけど） <br> 面倒なのはモデルロードかもね <br> 多分こちらに従ってモデル落としてきてサンプルワークフロー入れれば使えるはず（自分は別ルートでセットアップしたので細かいところは未確認） <br> <a href='https://comfyui-wiki.com/ja/tutorial/advanced/image/hidream/i1-t2i'>https://comfyui-wiki.com/ja/tutorial/advanced/image/hidream/i1-t2i</a> <br> 量子化はfp8_e4m3fnで4090なら溢れない　5090ならfp16でいけるらしい <br>  <br> ただUncensoredモデル(Llamaとかモデルとか）を使いたい時はちょっと面倒になる。 <br> モデルはこのあたりで良いだけど <a href='https://civitai.com/models/1498292?modelVersionId=1701111'>https://civitai.com/models/1498292?modelVersionId=1701111</a> <br> Llamaは <a href='https://huggingface.co/John6666/Llama-3.1-8B-Lexi-Uncensored-V2-nf4/tree/main'>https://huggingface.co/John6666/Llama-3.1-8B-Lexi-Uncensored-V2-nf4/tree/main</a> か\>\>310のモデルを使うと良いんだけど自分でsafetensors一個に纏めないといけない <br> あとClipもGGUF版使う場合はGGUF Cutom NodeにGGUF Quadruple Clip Loaderがあるよ 
<br>

