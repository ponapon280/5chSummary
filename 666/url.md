# 1. https://huggingface.co/
## No.94:	2026/07/03(金) 10:39:26.52 ID:hzLFTgjC0
 <a href='https://huggingface.co/Bedovyy/Anima-INT8'>https://huggingface.co/Bedovyy/Anima-INT8</a> <br> ここのINT8なanimaを使ってみたんやけど、これはAnima-ControlNet-LLLiteに非対応みたいやね <br> 元画像を参照していない画像が生成されてしまうわ <br>  <br> 元画像　<a href='https://i.ibb.co/nNJdLW60/Booguturbo.webp'>https://i.ibb.co/nNJdLW60/Booguturbo.webp</a> <br> LLLite-depth　<a href='https://i.ibb.co/0V61hXwn/lllite-depth.webp'>https://i.ibb.co/0V61hXwn/lllite-depth.webp</a> <br> Anima baseで生成（depth画像を参照している）　<a href='https://i.ibb.co/3yysH18M/anima-base-lllite-depth.webp'>https://i.ibb.co/3yysH18M/anima-base-lllite-depth.webp</a> <br> Anima INT8rowwiseで生成（depth画像を参照していない）　<a href='https://i.ibb.co/QjKf0YDy/anima-int8rowwise-lllite-depth.webp'>https://i.ibb.co/QjKf0YDy/anima-int8rowwise-lllite-depth.webp</a> 
<br>

## No.137:	2026/07/03(金) 13:20:31.95 ID:acCoG88C0
 \>\>125 <br> ガチで使うなら実行時じゃなくてモデル自体をConvRotで保存した方がええなこれ <br> INT8-Fastの作者がAnima p3や10ErosのINT8 ConvRot版公開してたわ <br>  <br> <a href='https://huggingface.co/bertbobson/ComfyUI-INT8_ConvRot/tree/main'>https://huggingface.co/bertbobson/ComfyUI-INT8_ConvRot/tree/main</a> 
<br>

## No.166:	2026/07/03(金) 16:04:34.80 ID:jS66WGdr0
 3060で動かないのはComfyUIを0.27.0に上げていない、ComfyUI謹製の昆布を使っていないのどちらかでは？ <br>  <br> <a href='https://huggingface.co/Comfy-Org/Krea-2/blob/main/diffusion_models/krea2_turbo_int8_convrot.safetensors'>https://huggingface.co/Comfy-Org/Krea-2/blob/main/diffusion_models/krea2_turbo_int8_convrot.safetensors</a> 
<br>

## No.288:	2026/07/03(金) 23:12:07.54 ID:EsGdht380
 \>\>203 <br> 既出かもしれない <br> 見るからに実験的なLoRAだが、bboxに反応しそう <br> <a href='https://huggingface.co/Aitrepreneur/IdeoKrea'>https://huggingface.co/Aitrepreneur/IdeoKrea</a> 
<br>

## No.392:	2026/07/04(土) 12:15:31.55 ID:FE1tM7wf0
 <a href='https://huggingface.co/Comfy-Org'>https://huggingface.co/Comfy-Org</a> <br>  <br> comfyの;見たらkijaiが物凄い勢いで過去モデルのint8 昆布を上げ始めてるやん; <br> kijaiのグラボちゃんは仕事が尽きなくて大変やね; 
<br>

# 2. https://mega.nz/
# 3. https://civitai(com/red 共用)
## No.317:	2026/07/04(土) 04:07:26.36 ID:srGqAjXW0
 Krea2のテンプレートWF使って、RTX5080でINT8 Convrot試した。 <br> krea2_turbo_fp8_scaledだと1536 * 2048の生成が28秒だったのが、↓だと21秒になるから、結構効果あるな。品質の違いはワイの節穴ではわからぬ <br> <a href='https://civitai.com/models/2746798/krea-2-turbo-int8convrot-works-with-comfyui-default-model-loader'>https://civitai.com/models/2746798/krea-2-turbo-int8convrot-works-with-comfyui-default-model-loader</a> <br>  <br> Krea2のキャラ出力サンプル見たけど、二次元キャラも結構いるのな。海外ﾆｷが作ったからか日本のキャラはあんまいないけど、 <br> <a href='https://photos.google.com/share/AF1QipNXkBpo4r3bMai11RDfLeBz6XMRg72PcxFdeefs-FIi_YjMn00zjOKShkw7uvzfhw?key=eUt4Z0NSdGVtZUhsck1ycWZNRWtrZnVjMGVid2hn'>https://photos.google.com/share/AF1QipNXkBpo4r3bMai11RDfLeBz6XMRg72PcxFdeefs-FIi_YjMn00zjOKShkw7uvzfhw?key=eUt4Z0NSdGVtZUhsck1ycWZNRWtrZnVjMGVid2hn</a> 
<br>

## No.410:	2026/07/04(土) 13:16:01.48 ID:srGqAjXW0
 Krea2のBBOX対応カスタムノードを試す <br> <a href='https://civitai.com/models/2742034/krea2-bbox-prompter-suite'>https://civitai.com/models/2742034/krea2-bbox-prompter-suite</a> <br>  <br> BBOX機能も使いやすいけど、作風やアングルなんかを選択して指定できるので、BBOX必要ない時でも使い勝手がいい <br> <a href='https://i.ibb.co/8gyzQXjC/Krea2-123341-00001.webp'>https://i.ibb.co/8gyzQXjC/Krea2-123341-00001.webp</a> <br> <a href='https://i.ibb.co/VYHsWy1C/Krea2-111825-00001.webp'>https://i.ibb.co/VYHsWy1C/Krea2-111825-00001.webp</a> <br> <a href='https://i.ibb.co/NgdMGWFZ/Krea2-112511-00001.webp'>https://i.ibb.co/NgdMGWFZ/Krea2-112511-00001.webp</a> 
<br>

## No.612:	2026/07/05(日) 01:32:26.93 ID:19oeMZ0r0
 ↓にあるWFを参考にKrea2のcontrolnetをテスト <br> <a href='https://civitai.com/models/2752799/krea-2-depth-controlnet-lora'>https://civitai.com/models/2752799/krea-2-depth-controlnet-lora</a> <br>  <br> ノード構成をシンプルにしたWF付サンプル画像 <br> <a href='https://i.ibb.co/pvfMPcNK/Krea2-25.webp'>https://i.ibb.co/pvfMPcNK/Krea2-25.webp</a> <br>  <br> 元のWFから、Depthのノードとモデルはkijaiﾆｷのに差し替え <br> <a href='https://github.com/kijai/ComfyUI-DepthAnythingV2'>https://github.com/kijai/ComfyUI-DepthAnythingV2</a> 
<br>

