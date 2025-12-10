# 1. https://huggingface.co/
## No.18:	2025/12/07(日) 18:41:53.47 ID:CPr0PqHL0
 サンイチNewBie-image <br> <a href='https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1'>https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1</a> 
<br>

## No.310:	2025/12/08(月) 19:28:09.61 ID:loY7XWVj0
 <a href='https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1'>https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1</a> <br> NewBieは説明見る限りだと <br> XMLでのプロンプトで描き分けできるよ、従来のタガー方式と違って混ざらいよ <br> が売りっぽいんだけど、Zimageが自然言語or適当フォーマットでちゃんと描き分けられちゃってるのでうーんという状況 <br>  <br> ZimageTurboにNewBieのサンプルにあるXMLをコピペしたらちゃんと描き分けられてるし　<a href='https://files.catbox.moe/od1zz9.png'>https://files.catbox.moe/od1zz9.png</a> <br> ZimageTurboで1万ステップで試しに作った某エロゲ画風LoRAも割と素直にのる　<a href='https://files.catbox.moe/d0i0ro.png'>https://files.catbox.moe/d0i0ro.png</a> 
<br>

## No.360:	2025/12/08(月) 21:40:07.07 ID:PjZn3YK40
 zimageのfp8とQ8試した（4080s 1024x1024 8steps euler_ancestral_beta） <br> - bf16(公式TE): 11.5秒 <br> - Q8(公式TE): 11秒 <br> - Q8(Q8TE): 9.7秒（16GB VRAMに収まる）バランス◎ <br> 画質の谷／速度の谷 <br> - fp8(公式TE): 7.8秒 <br> - fp8(Q8TE): 7.2秒（16GB VRAMに収まる）速度重視ならこれ <br> Q8はbf16と比べて変化がわずかで画質の劣化や細部のつぶれもわずか（ほぼ同等） <br> fp8は変化する度合いが多く比較すると画質の差は明らかで細部のつぶれも気になる <br> Q8(Q8TE)はbf16とほぼ同等レベルで15%高速かつVRAM安定で画面操作（マウス操作）に支障が出ない（オヌヌメ） <br> リンクのQ8TEはカスタムノード「gguf」で使用可能（comfyui-ggufでは使用できない） <br> <a href='https://huggingface.co/drbaph/Z-Image-Turbo-FP8/tree/main'>https://huggingface.co/drbaph/Z-Image-Turbo-FP8/tree/main</a>　<a href='https://huggingface.co/jayn7/Z-Image-Turbo-GGUF/tree/main'>https://huggingface.co/jayn7/Z-Image-Turbo-GGUF/tree/main</a>　<a href='https://huggingface.co/worstplayer/Z-Image_Qwen_3_4b_text_encoder_GGUF/tree/main'>https://huggingface.co/worstplayer/Z-Image_Qwen_3_4b_text_encoder_GGUF/tree/main</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.426:	2025/12/09(火) 05:52:52.99 ID:XjveZ+F00
 マイナスも効くね <br> <a href='https://civitai.com/models/2201058/luisap-zimage-the-damn-age-slider?modelVersionId=2483834'>https://civitai.com/models/2201058/luisap-zimage-the-damn-age-slider?modelVersionId=2483834</a> <br>  <br> 強度0 <br> <a href='https://files.catbox.moe/fu1bde.webp'>https://files.catbox.moe/fu1bde.webp</a> <br>  <br> 強度-1.0 <br> <a href='https://files.catbox.moe/3fmx0w.webp'>https://files.catbox.moe/3fmx0w.webp</a> <br>  <br> 強度-2.0 <br> <a href='https://files.catbox.moe/r5w2fb.webp'>https://files.catbox.moe/r5w2fb.webp</a> 
<br>

## No.438:	2025/12/09(火) 08:35:01.67 ID:j2pLP96T0
 \>\>434 <br> このWF試しとるんや C-AIO v1.7 <br> <a href='https://civitai.com/models/1823089/dasiwa-wan22-workflows'>https://civitai.com/models/1823089/dasiwa-wan22-workflows</a> <br> 通常とggufでモデルローダーが違うのは分かるんや <br> ggufはアーリーやから通常モデルをダウンロードしてモデルフォルダにちゃんと入れとるがgguf側offにして通常版を有効化しても読み込みリストにモデルが出てこない <br> 他のwanとかsmoothmixのWFを開けばモデル読み込めてるから <br> DaSiWa Wan2.2WFの種類が多すぎてワイが変なの使って間違っとるだけかもしれんが 
<br>

## No.445:	2025/12/09(火) 08:57:41.03 ID:F+2XrGak0
 <a href='https://civitai.com/models/2190659'>https://civitai.com/models/2190659</a> <br> DaSiWaは一週間待ってフラグシップモデルとやらを触ろうかと思ってる <br> DaSiWa公式WFはGetSet多用で使う気にならないからSmoothmix公式のシンプルなやつでモデルとステップ数変えるだけでいけると嬉しい 
<br>

## No.526:	2025/12/09(火) 12:57:57.88 ID:X5lytatD0
 <a href='https://civitai.com/articles/23423/comfyui-workflow-text-2-image-with-regional-lora-prompting-sdxl'>https://civitai.com/articles/23423/comfyui-workflow-text-2-image-with-regional-lora-prompting-sdxl</a> <br>  <br> SDXLで複数人のかき分けができるようになったと言っているが <br> 単にリージョナルプロンプター的な発想か？ 
<br>

## No.642:	2025/12/09(火) 17:58:56.54 ID:jZvIKeO50
 \>\>607 <br> DaSiWa作者の記事や <br> <a href='https://civitai.com/articles/23271'>https://civitai.com/articles/23271</a> <br> 今まで作者の技術的にfp8モデルしか出せんかったけどそのfp8から出来たパチモンggufが出回ってたから <br> 作者が頑張ってfp16ベースのgguf作ったってことやね 
<br>

## No.744:	2025/12/09(火) 23:04:58.46 ID:26NfK4Le0
 <a href='https://civitai.com/models/2100349?modelVersionId=2483014'>https://civitai.com/models/2100349?modelVersionId=2483014</a> <br> 読む限りではすごそうやけど <br> 実際はどうなんやろな… 
<br>

