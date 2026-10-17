# 1. https://huggingface.co/
## No.101:	2026/10/16(金) 00:27:43.72 ID:D/Ni0vVy0
 nvidiaから新LLM <br> NVIDIA-Nemotron-3.5-Super-VL-120B-A12B　と <br> NVIDIA-Nemotron-3.5-Bolt-74B-A9B <br> <a href='https://huggingface.co/nvidia/models'>https://huggingface.co/nvidia/models</a> <br>  <br> 74Bの方はなんとQ2向けのQATも用意されとるな <br> モデルサイズ22GB <br>  <br> あとmicrosoftも近々でLLM出すって情報でまわっとるなぁ <br> いろんな会社から出るのはええことや 
<br>

## No.114:	2026/10/16(金) 00:48:22.71 ID:F28kM1jl0
 公式でINT8ConvRot用意してるのが良いな <br> <a href='https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy'>https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy</a> 
<br>

## No.314:	2026/10/16(金) 20:52:35.81 ID:YDDkJbfua
 omfyUI用 MOSS-Image SFT (INT8 ConvRot) (従来のローダーで読み込むタイプ <br> <a href='https://huggingface.co/XCEED123/MOSS-Image-SFT-INT8-ComfyUI'>https://huggingface.co/XCEED123/MOSS-Image-SFT-INT8-ComfyUI</a> 
<br>

## No.345:	2026/10/16(金) 21:49:13.94 ID:YDDkJbfua
 MOSS ComfyUI本体の対応が進んでいる <br> <a href='https://github.com/Comfy-Org/ComfyUI/pull/17095'>https://github.com/Comfy-Org/ComfyUI/pull/17095</a> <br>  <br> chromaニキが8step loraを作ってるもよう <br> <a href='https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd'>https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd</a> 
<br>

## No.352:	2026/10/16(金) 22:11:12.41 ID:CYLO+wM70
 ComfyUI公式来てるで <br> <a href='https://huggingface.co/Comfy-Org/MOSS-Image/tree/main'>https://huggingface.co/Comfy-Org/MOSS-Image/tree/main</a> 
<br>

## No.452:	2026/10/17(土) 00:30:05.68 ID:7Hbs2ko80
 SFTだけど8step DMD LoRAが出てたからCodexにインストールさせてRadeon 8060Sでも120秒でこれ生成できるようになったンゴ <br> 1週間も経たずにComfyネイティブ対応のTurboモデル来てゲームエンドしそうや <br>  <br> <a href='https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd'>https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd</a> <br> <a href='https://i.ibb.co/HDXZzXFM/a6985ed5c7ff.png'>https://i.ibb.co/HDXZzXFM/a6985ed5c7ff.png</a> 
<br>

## No.461:	2026/10/17(土) 00:48:04.76 ID:7Hbs2ko80
 というかHFの公式Spaceで落とさなくてもBaseを2MP80秒程度で試せるな <br> 1MPにしたら1枚30秒で出たわ <br> 公式サンプルのプロンプトもコピペ可で読める <br> <a href='https://huggingface.co/spaces/OpenMOSS-Team/MOSS-Image'>https://huggingface.co/spaces/OpenMOSS-Team/MOSS-Image</a> <br>  <br> <a href='https://i.ibb.co/wZ6xYKrV/b99463cee03b.png'>https://i.ibb.co/wZ6xYKrV/b99463cee03b.png</a> <br>  <br> 「30歳です…;」と伝えてGrok 4.6に剥かせた奴 <br> <a href='https://i.ibb.co/7dF3XS3v/a4a0d38e6e8e.png'>https://i.ibb.co/7dF3XS3v/a4a0d38e6e8e.png</a> 
<br>

## No.578:	2026/10/17(土) 10:46:49.38 ID:U9z3b1zd0
 おっぱいの鷲掴みがMiniMaxH3でも微妙だったのでLoRA学習したのをアップしたで <br> <a href='https://huggingface.co/nashikone/iroiroLoRA/tree/main/minimax_h3_fl2va/W'>https://huggingface.co/nashikone/iroiroLoRA/tree/main/minimax_h3_fl2va/W</a> <br> ■washizukami_minimax_h3_v2_phe(おっぱい鷲掴みLoRA) <br> サンプルは偽乳やがなガハハ <br> <a href='https://tadaup.jp/At2h8P6w.mp4'>https://tadaup.jp/At2h8P6w.mp4</a> <br>  <br> 学習サンプル内に声つきが少数だけ入ってた場合（今回は1/4）、音声がそっちに強く引っ張られる事象がある知見が得られた <br> なのでvideo_onlyで学習し直ししたやね 
<br>

## No.603:	2026/10/17(土) 11:19:47.42 ID:XPczhfjE0
 MOSS-Image-SFTの8step Lora <br> <a href='https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd'>https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd</a> <br> を、\>\>453 \>\>504　で試した <br> <a href='https://tadaup.jp/Azwsf0k5.webp'>https://tadaup.jp/Azwsf0k5.webp</a> <br> <a href='https://tadaup.jp/AOnQ8Soy.webp'>https://tadaup.jp/AOnQ8Soy.webp</a> <br> <a href='https://tadaup.jp/AL7NyGsg.webp'>https://tadaup.jp/AL7NyGsg.webp</a> <br>  <br> 元が50stepで120秒だったのが、20秒まで高速化。 <br> 細部は潰れるが、仕上げまではこっちでええかもな 
<br>

## No.803:	2026/10/17(土) 18:23:31.67 ID:naZ06p4F0
 sft用の8step DMDならもう来てる <br> <a href='https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd'>https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai(com/red 共用)
## No.24:	2026/10/15(木) 20:54:42.02 ID:Msg/E3Je0
 スレ跨いだけど宣伝する！ <br>  <br> <a href='https://civitai.red/models/1125348'>https://civitai.red/models/1125348</a> <br> susamixEX v4 animaをよろしく！ 
<br>

## No.90:	2026/10/16(金) 00:07:49.30 ID:MSd1IBsY0
 サンイチ <br> 一応作ったはいいけど今更感の凄いCottonAnimaの2.9Bや <br> カスタムノード必須な筈やから気を付けてな <br> <a href='https://civitai.red/models/2382223/cottonanima?modelVersionId=3406559'>https://civitai.red/models/2382223/cottonanima?modelVersionId=3406559</a> <br> 出しといて言うのもなんやが、生成時間伸ばしてまでこっちを使う意味をそこまで感じてないってのが本音では有る <br> base1の出来が個人的に完璧過ぎたってのも有るんやけど…まあ新キャラ出したいとか　こっちにしか出せん物を感じたニキはどうぞって感じや <br> そろそろ欲しいやねえ…animaに変わるローカルのbooru学習モデル <br> <a href='https://tadaup.jp/Az79efNi.png'>https://tadaup.jp/Az79efNi.png</a> <br> <a href='https://tadaup.jp/ApoWAQux.png'>https://tadaup.jp/ApoWAQux.png</a> <br> <a href='https://tadaup.jp/AMaX7PCB.png'>https://tadaup.jp/AMaX7PCB.png</a> 
<br>

