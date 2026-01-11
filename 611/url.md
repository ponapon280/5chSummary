# 1. https://huggingface.co/
## No.218:	2026/01/08(木) 10:38:08.86 ID:aXA60gaX0
 \>\>213 <br> ノードが複数あってわかりにくいんやけど、そっちのノードの場合は、gemma-3のggufとかfp8じゃなく、↓の分割ファイルやら一式をそのままDLしてこないとあかんみたいやで <br>  <br> <a href='https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/'>https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/</a> 
<br>

## No.229:	2026/01/08(木) 11:09:01.19 ID:uS5E7v9u0
 \>\>221 <br> \>\>225が「分割ファイル以外も全部DLして同じ階層に入れてても」と書いているように、 <a href='https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main'>https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main</a> にあるほかのファイルも同じフォルダに入れなきゃいけない気がするで 
<br>

## No.288:	2026/01/08(木) 13:25:28.78 ID:HgMNt6+0d
 \>\>283 <br> 今確認できないがワイはたしかここのfp8 e4m3fn使ってるで <br> <a href='https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/tree/main'>https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/tree/main</a> 
<br>

## No.576:	2026/01/09(金) 10:47:19.24 ID:wqQBxk1i0
 \>\>569 <br> 全部ローカルやね　リップシンクはWanベースで動かしてるInfiniteTalkノードで <br> TTSは上にもあるようにT5Gemma-TTSのフォーク版のT5Gemma-TTS-2b-2bやね <br> こんな感じでデモページと同じにしてある <br> <a href='https://files.catbox.moe/hf06b1.jpg'>https://files.catbox.moe/hf06b1.jpg</a> <br>  <br> 本体は <br> <a href='https://huggingface.co/Aratako/T5Gemma-TTS-2b-2b'>https://huggingface.co/Aratako/T5Gemma-TTS-2b-2b</a> <br> XCodec2はAnime-XCodec2-44.1kHz-v2使ってるよ 
<br>

## No.593:	2026/01/09(金) 12:49:32.18 ID:WojjHoCt0
 <a href='https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA'>https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA</a> <br>  <br> QIE2511版multipie angles来てるぞ 
<br>

## No.764:	2026/01/09(金) 20:13:14.78 ID:3Ght73Rb0
 \>\>750 <br> 自分で組んだわ <br> <a href='https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA'>https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA</a> <br> こいつのWFの画像読み込みにグルグルノード繋いでグルグルからプロンプトに繋ぐだけ <br> グルグルするLoRAは消すかバイパスすればシンプルでいい <br> プロンプトは自動生成されるので余計なものない方がええよ 
<br>

## No.799:	2026/01/09(金) 23:00:21.84 ID:6hhAvdNl0
 storymen mm2v_high_noise.safetensorsは <br> <a href='https://huggingface.co/Kevin-thu/StoryMem/commit/8b74183abb404dab74b6df04ef09fa88156e5193'>https://huggingface.co/Kevin-thu/StoryMem/commit/8b74183abb404dab74b6df04ef09fa88156e5193</a> <br> のWan2.2-MM2V-A14B/backbone_high_noise.safetensorsであってるんやろか？ 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.465:	2026/01/08(木) 22:22:17.89 ID:skyzAw6O0
 \>\>395 <br> これ使おうとして悪戦苦闘しとる赤ちゃんなんやけど <br> VHS_SelectFilename <br> 'NoneType' object is not subscriptable <br> ってなるのは何が原因なん？ <br>  <br> smoothMixWan22I2V14B_i2vHigh.safetensorsて <br> <a href='https://civitai.com/models/1995784?modelVersionId=2260110'>https://civitai.com/models/1995784?modelVersionId=2260110</a> <br> と同じもんなん？ 
<br>

## No.750:	2026/01/09(金) 19:58:17.80 ID:k/jI1JKa0
 Qwenの画像クルクルのやつをComfyUIで実行するの来てるで <br>  <br> <a href='https://civitai.com/models/2252071'>https://civitai.com/models/2252071</a> <br> <a href='https://github.com/jtydhr88/ComfyUI-qwenmultiangle'>https://github.com/jtydhr88/ComfyUI-qwenmultiangle</a> 
<br>

## No.763:	2026/01/09(金) 20:12:55.63 ID:av/67OcG0
 LTX-2 NSFW Text Encoder - Gemma 3 12b Abliterated <br> <a href='https://civitai.com/models/2292336/ltx-2-nsfw-text-encoder-gemma-3-12b-abliterated?modelVersionId=2579572'>https://civitai.com/models/2292336/ltx-2-nsfw-text-encoder-gemma-3-12b-abliterated?modelVersionId=2579572</a> 
<br>

## No.929:	2026/01/10(土) 10:55:17.53 ID:geSWBeUh0
 \>\>924 <br> To Much Movementの抑制、なにもしてなくても乳揺れが抑制されるのはいいねえ <br> <a href='https://civitai.com/articles/24249'>https://civitai.com/articles/24249</a> 
<br>

