# 1. https://huggingface.co/
## No.419:	2026/05/09(土) 14:34:26.54 ID:JLFKrpPy0
 vae無しのピクセル空間で推論するモデルで初めて実用的かも？ <br> <a href='https://huggingface.co/HiDream-ai/HiDream-O1-Image'>https://huggingface.co/HiDream-ai/HiDream-O1-Image</a> 
<br>

## No.456:	2026/05/09(土) 16:34:08.57 ID:GPhl/s4J0
 \>\>455 <br> 使い方によるで <br> イラスト風やフィギュア風学習されてるからLoRAやファインチューニング作れたらGPT-Image-2や;2くらいの追従性でイラストも出せる健全絵ゲームエンドになりそうや <br>  <br>  <br> <a href='https://huggingface.co/HiDream-ai/HiDream-O1-Image/resolve/main/assets/general.webp'>https://huggingface.co/HiDream-ai/HiDream-O1-Image/resolve/main/assets/general.webp</a> <br>  <br> <a href='https://huggingface.co/HiDream-ai/HiDream-O1-Image/resolve/main/assets/text-layout.webp'>https://huggingface.co/HiDream-ai/HiDream-O1-Image/resolve/main/assets/text-layout.webp</a> 
<br>

## No.659:	2026/05/10(日) 03:30:45.25 ID:09a9vlLd0
 新しいtag付けモデルですって <br> <a href='https://www.reddit.com/r/StableDiffusion/comments/1t8bzb3'>https://www.reddit.com/r/StableDiffusion/comments/1t8bzb3</a> <br> <a href='https://huggingface.co/Grio43/OppaiOracle'>https://huggingface.co/Grio43/OppaiOracle</a> 
<br>

## No.738:	2026/05/10(日) 13:08:26.18 ID:HrK1rpEm0
 hidream o1 imageのfp8版があった <br> vram10GBで行けるらしい <br> <a href='https://huggingface.co/drbaph/HiDream-O1-Image-FP8'>https://huggingface.co/drbaph/HiDream-O1-Image-FP8</a> 
<br>

## No.810:	2026/05/10(日) 18:58:52.31 ID:1cHd7jCu0
 \>\>809 <br> 赤civitaiで10erosで検索かけて案内を見つけた<a href='https://huggingface.co/TenStrip/LTX2.3-10Eros_Workflowsにあった10Eros_10SNodes_TripleSample_I2V.jsonをそのまま使ってる'>https://huggingface.co/TenStrip/LTX2.3-10Eros_Workflowsにあった10Eros_10SNodes_TripleSample_I2V.jsonをそのまま使ってる</a> <br> LTX2.3だから12GBだとギリギリな気もするけどその辺はサイズとか落としていけばなんとかなるかもしらんけど、試してみないことにはわからんやろね 
<br>

## No.813:	2026/05/10(日) 19:13:11.28 ID:6bVhXAtv0
 \>\>809, 810 <br> HuggingFaceの10Eros（<a href='https://huggingface.co/TenStrip/LTX2.3-10Eros）を見ればわかるけど10Eros作った人自身の手によるWFですね'>https://huggingface.co/TenStrip/LTX2.3-10Eros）を見ればわかるけど10Eros作った人自身の手によるWFですね</a> 使われている10SNodes（<a href='https://github.com/TenStrip/10S-Comfy-nodes）も同じ'>https://github.com/TenStrip/10S-Comfy-nodes）も同じ</a> <br> デフォのpixelサイズが1.4MPxとか1.5MPxとか大きめなので0.8MPxあたりに下げたりLengthを短くしたりすると良いかも <br>  <br> あと10Eros_10SNodes_I2V_v2.jsonの方が少し速いらしい <br>  <br> まだ試せてないけど半日ほど前にTiled samplerとそれを使うWFも追加されていて改良が続いているのでしばらくは時々チェックしたほうが良さそう 
<br>

## No.823:	2026/05/10(日) 19:43:08.68 ID:ayVdVHFt0
 LTX2.3のモデルはここでええんか？ <br> <a href='https://huggingface.co/unsloth/LTX-2.3-GGUF/tree/main'>https://huggingface.co/unsloth/LTX-2.3-GGUF/tree/main</a> <br> ltx-2.3-22b-dev-Q6_K.ggufくらいがちょうどいいんやろか？ <br> VRAMに乗せきらないとあかんのならワイの4070ちゃんやと ltx-2.3-22b-dev-Q3_K_M.gguf 10.8 GBしかあかんが 
<br>

## No.832:	2026/05/10(日) 20:06:19.98 ID:6bVhXAtv0
 \>\>828 <br> これをcustom_nodesフォルダでgit pull <br> <a href='https://github.com/TenStrip/10S-Comfy-nodes'>https://github.com/TenStrip/10S-Comfy-nodes</a> <br>  <br> huggingfaceの情報は有用だから一度目を通しておくと良い <br> <a href='https://huggingface.co/TenStrip/LTX2.3-10Eros'>https://huggingface.co/TenStrip/LTX2.3-10Eros</a> 
<br>

## No.851:	2026/05/10(日) 21:15:20.72 ID:ZyXugCJb0
 \>\>849 <br> ぐぐったら一発で出て来たで <br> <a href='https://huggingface.co/TenStrip/LTX2.3_Distilled_Lora_1.1_Experiments/blob/main/ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors'>https://huggingface.co/TenStrip/LTX2.3_Distilled_Lora_1.1_Experiments/blob/main/ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors</a> 
<br>

## No.852:	2026/05/10(日) 21:15:49.96 ID:z1tal4V40
 <a href='https://huggingface.co/TenStrip/LTX2.3_Distilled_Lora_1.1_Experiments/blob/main/ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors'>https://huggingface.co/TenStrip/LTX2.3_Distilled_Lora_1.1_Experiments/blob/main/ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors</a> <br> これでは？ 
<br>

## No.862:	2026/05/10(日) 21:23:59.67 ID:6bVhXAtv0
 いや10Eros使うんならマジで大本の情報をまず見ようよ <br>  <br> <a href='https://huggingface.co/TenStrip/LTX2.3-10Eros'>https://huggingface.co/TenStrip/LTX2.3-10Eros</a> <br>  <br> Workflowもcustom_nodeもDistilled LoRAも全部ポインタあるよ <br> あとプロンプトの書き方や注意点も 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.936:	2026/05/11(月) 01:39:56.29 ID:MFsQlzM60
 ここやな <br> P1だけCivitaiに上がってない <br> <a href='https://civitai.com/user/circlestone_labs'>https://civitai.com/user/circlestone_labs</a> 
<br>

## No.938:	2026/05/11(月) 01:50:06.48 ID:o3+/eo4f0
 \>\>935 <br> うちではcomでもredでも引っ掛かるけど <br> p1はここかなunoffcialだと思うけど上がった当時もファイル名が云々みたいな話が合ったけどハッシュは同じだったので中身は同じだろって話で落ち着いてた筈 <br> <a href='https://civitai.com/models/2359125/anima'>https://civitai.com/models/2359125/anima</a> 
<br>

