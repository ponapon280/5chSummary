# 1. https://huggingface.co/
## No.69:	2026/01/14(水) 02:26:55.67 ID:cJj/qY/I0
 Sharpという技術で画像から3D画像を作って動かして、ぐちゃった部分をこのloraで修復する事で別視点の画像を作れるっぽい <br> <a href='https://huggingface.co/dx8152/Qwen-Edit-2511-Sharp'>https://huggingface.co/dx8152/Qwen-Edit-2511-Sharp</a>  <br> <a href='https://www.youtube.com/watch?v=9Vyxjty9Qao'>https://www.youtube.com/watch?v=9Vyxjty9Qao</a> 
<br>

## No.117:	2026/01/14(水) 09:27:46.71 ID:zQaspQh/a
 \>\>107 <br> 一応Wan 2.2も非公式にnvfp4化したモデルは出とるで <br> <a href='https://huggingface.co/GitMylo/Wan_2.2_nvfp4/tree/main'>https://huggingface.co/GitMylo/Wan_2.2_nvfp4/tree/main</a> <br> FP8モデルより25%速くなるようやな 
<br>

## No.138:	2026/01/14(水) 11:36:42.07 ID:/W1QQKE30
 LLMで高性能なGLM4-7出してるZ.aiがGLM-Image出したらしい <br>  <br> <a href='https://x.com/Zai_org/status/2011247591825068314'>https://x.com/Zai_org/status/2011247591825068314</a> <br>  <br> HFにもう来てる <br> <a href='https://huggingface.co/zai-org/GLM-Image'>https://huggingface.co/zai-org/GLM-Image</a> <br> <a href='https://raw.githubusercontent.com/zai-org/GLM-Image/refs/heads/main/resources/show_case_t2i.jpeg'>https://raw.githubusercontent.com/zai-org/GLM-Image/refs/heads/main/resources/show_case_t2i.jpeg</a> <br> <a href='https://raw.githubusercontent.com/zai-org/GLM-Image/refs/heads/main/resources/show_case_i2i.jpeg'>https://raw.githubusercontent.com/zai-org/GLM-Image/refs/heads/main/resources/show_case_i2i.jpeg</a> 
<br>

## No.231:	2026/01/14(水) 15:54:28.62 ID:ngCdK63r0
 \>\>225 <br> whlあるでー <br> <a href='https://huggingface.co/ussoewwin/Flash-Attention-2_for_Windows/tree/main'>https://huggingface.co/ussoewwin/Flash-Attention-2_for_Windows/tree/main</a> <br> 日本人の人が公開してくれてはる 
<br>

## No.249:	2026/01/14(水) 17:25:43.37 ID:NbTey5r40
 nvfp4使ってみたい50xxのニキはComfyUIフォルダで.\venv\Scripts\activateして↓でええんやないかな <br> pip3 install -U torch==2.9.1+cu130 torchvision==0.24.1+cu130 torchaudio==2.9.1+cu130 --index-url <a href='https://download.pytorch.org/whl/cu130'>https://download.pytorch.org/whl/cu130</a> <br>  <br> pip install -U triton-windows <br>  <br> curl -L <a href='https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post3/sageattention-2.2.0+cu130torch2.9.0.post3-cp39-abi3-win_amd64.whl'>https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post3/sageattention-2.2.0+cu130torch2.9.0.post3-cp39-abi3-win_amd64.whl</a> > sageattention-2.2.0+cu130torch2.9.0.post3-cp39-abi3-win_amd64.whl <br> pip uninstall sageattention <br> pip install sageattention-2.2.0+cu130torch2.9.0.post3-cp39-abi3-win_amd64.whl <br>  <br> curl -L <a href='https://huggingface.co/ussoewwin/Flash-Attention-2_for_Windows/resolve/main/flash_attn-2.8.3%2Bcu130torch2.9.1cxx11abiTRUE-cp312-cp312-win_amd64.whl?download=true'>https://huggingface.co/ussoewwin/Flash-Attention-2_for_Windows/resolve/main/flash_attn-2.8.3%2Bcu130torch2.9.1cxx11abiTRUE-cp312-cp312-win_amd64.whl?download=true</a> > flash_attn-2.8.3%2Bcu130torch2.9.1cxx11abiTRUE-cp312-cp312-win_amd64.whl <br> pip uninstall flash_attn <br> pip install flash_attn-2.8.3+cu130torch2.9.1cxx11abiTRUE-cp312-cp312-win_amd64.whl 
<br>

## No.298:	2026/01/14(水) 21:47:17.05 ID:gDN614Yq0
 \>\>288 <br> QI2512は高速化LoRA使っても意外と画質落ちないし4step LoRAならZITより速いまであるよ <br> リアル系しか試してないけど <br>  <br> <a href='https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/tree/main'>https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/tree/main</a> <br>  <br> ワイは普段は8step LoRAでやっているけどPromptチェックとかは4stepでも十分 <br> あとZITよりPromptにはよく反応する気がする 
<br>

## No.335:	2026/01/15(木) 06:06:07.14 ID:7H/A/c9E0
 LTX2のVAEが間違ってたとかで公式やkijaiが修正版を上げ直してるんやな  <br> <a href='https://huggingface.co/Lightricks/LTX-2/commits/main'>https://huggingface.co/Lightricks/LTX-2/commits/main</a>  <br> <a href='https://huggingface.co/Kijai/LTXV2_comfy/commits/main'>https://huggingface.co/Kijai/LTXV2_comfy/commits/main</a> 
<br>

## No.529:	2026/01/15(木) 21:55:20.45 ID:2eQbrEbz0
 LTX-2の公式チェックポイント配布のファイル名が「ltx-2-19b-dev-fp4」 <br> 一方でモデルカードの説明を見ると「The full model in nvfp4 quantization」 <br> <a href='https://huggingface.co/Lightricks/LTX-2?utm_source=chatgpt.com'>https://huggingface.co/Lightricks/LTX-2?utm_source=chatgpt.com</a> <br>  <br> 「nvfp4」を略して「fp4」とファイル名を付けてるからだいぶ混乱してるけど <br> これからは「fp4」といったらもっぱら「nvfp4」のことを指すようになっていくのでGPTも察してくれるようになるはず 
<br>

## No.593:	2026/01/16(金) 02:17:47.15 ID:SfPp+Cr60
 Flux.2-klein 4bのdiffusion_modelsが7.5GBでtext_encoderが8GB(qwen_3_4b) <br> 9bと4bが出て4bだけapache LICENSE-2.0 <br> これテキストエンコーダー強化したSDXLくらいの立ち位置狙ってんのかな <br>  <br> <a href='https://huggingface.co/black-forest-labs/FLUX.2-klein-4B'>https://huggingface.co/black-forest-labs/FLUX.2-klein-4B</a> <br> <a href='https://huggingface.co/Comfy-Org/flux2-klein-4B'>https://huggingface.co/Comfy-Org/flux2-klein-4B</a> 
<br>

## No.627:	2026/01/16(金) 08:38:02.86 ID:GbbgRtP00
 \>\>579 <br> nvfp8という規格は今のところはないので合ってる <br> 実用的にfp4は精度落ちが激しいので新しく作ったのがnvfp4で、fp8はそのままで実用ラインにいるから新規格は今のところ作ってない <br>  <br> ただ、nvfp4のことをfp4と省略するのが多くて、その影響でfp8のことをnvfp8という存在しないという理解をする場合があるらしい <br> nvidiaの日本語公式HPでなんか間違えてる <br> <a href='https://blogs.nvidia.co.jp/blog/rtx-ai-garage-ces-2026-open-models-video-generation/'>https://blogs.nvidia.co.jp/blog/rtx-ai-garage-ces-2026-open-models-video-generation/</a> <br>  <br> LTX-2が配布してるのはBF16とFP8とNVFP4(ただし、ファイル名はfp4と省略) <br> <a href='https://huggingface.co/Lightricks/LTX-2'>https://huggingface.co/Lightricks/LTX-2</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.308:	2026/01/14(水) 22:19:05.62 ID:FcfWS+n10
 これマイナス適用したら貧乳の乳揺れ抑制できるんだろうか <br> <a href='https://civitai.com/models/1581186?modelVersionId=2595899'>https://civitai.com/models/1581186?modelVersionId=2595899</a> 
<br>

## No.506:	2026/01/15(木) 20:39:36.26 ID:faVmLthG0
 \>\>503 <br> 公式モデル以外でよく使われてるのはこの辺やな <br> これらを使う際はWFのlora「lightx2v」っていうのをバイパスかけて無効化するんやで <br>  <br> Smooth Mix（t2v／i2v） <br> <a href='https://civitai.com/models/1995784'>https://civitai.com/models/1995784</a> <br>  <br> DeSiWa（i2v） <br> <a href='https://civitai.com/models/1981116'>https://civitai.com/models/1981116</a> 
<br>

