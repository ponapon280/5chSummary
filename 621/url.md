# 1. https://huggingface.co/
## No.193:	2026/02/08(日) 18:24:15.34 ID:FHP/UNu70
 \>\>192 <br> 生成の解像度って意味なら1Mピクセルやで <br> <a href='https://huggingface.co/circlestone-labs/Anima#generation-settings'>https://huggingface.co/circlestone-labs/Anima#generation-settings</a> 
<br>

## No.197:	2026/02/08(日) 18:38:26.53 ID:Sh3dTayw0
 \>\>192 <br> モデルカードには中解像度メイン+少量の高解像度画像でトレーニングされてるって書いてあるね <br> 中解像度の定義は512x512 <br> <a href='https://huggingface.co/circlestone-labs/Anima/discussions/5#697ea15d7914fe81f46d8a55'>https://huggingface.co/circlestone-labs/Anima/discussions/5#697ea15d7914fe81f46d8a55</a> 
<br>

## No.510:	2026/02/09(月) 13:31:49.86 ID:X92DkCWv0
 \>\>505 <br> \>\>506 <br> さっそくサンガツやで！ <br> いやこれAnima公式ワークフローなんや…もういちどDLしなおしてくるで… <br> <a href='https://huggingface.co/circlestone-labs/Anima/tree/main'>https://huggingface.co/circlestone-labs/Anima/tree/main</a> <br> のanima_comparison.jsonなんや… 
<br>

## No.516:	2026/02/09(月) 13:35:15.53 ID:0yYDyQEw0
 \>\>510 <br> Model Cardのトップにある画像↓をComfyUIにドラッグ&ドロップするんやで <br> <a href='https://huggingface.co/circlestone-labs/Anima/resolve/main/example.png'>https://huggingface.co/circlestone-labs/Anima/resolve/main/example.png</a> 
<br>

## No.518:	2026/02/09(月) 13:36:19.59 ID:yO5Uw/VM0
 \>\>510 <br> それは名前の通り比較(comparison)用の中級者向けWFや <br> 正しい公式WFはこれ <br> <a href='https://huggingface.co/circlestone-labs/Anima/blob/main/example.png'>https://huggingface.co/circlestone-labs/Anima/blob/main/example.png</a> <br> このpngをDLしてComfyUIの画面にD&Dでおｋやで 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.662:	2026/02/09(月) 19:50:25.45 ID:wEI1MufC0
 Civitaiの新着で出てきたEast Asian Ai Influencerっての大丈夫なやつなんかな <br> こういう地味顔にドスケベな衣装着させるとしこり甲斐あるんやが <br> <a href='https://civitai.com/models/2369352'>https://civitai.com/models/2369352</a> 
<br>

## No.715:	2026/02/09(月) 22:47:58.59 ID:86+kvVWc0
 ZIBアニメモデルなんかこんなのが来た <br> <a href='https://civitai.com/models/2354972/nayelina-z-anime'>https://civitai.com/models/2354972/nayelina-z-anime</a> 
<br>

## No.733:	2026/02/10(火) 00:33:02.99 ID:WYNaA5nj0
 <a href='https://civitai.com/models/2364703/rdbt-anima'>https://civitai.com/models/2364703/rdbt-anima</a> <br>  <br> animaを高速化するやつ <br> 確かに速くなるけど生成物はいまいちだった 
<br>

## No.813:	2026/02/10(火) 12:48:39.20 ID:ws7DANIW0
 高速化は今でも簡単に導入できる手段があるけど品質は落ちる <br>  <br> ・civiitaiのこれを使ってcfg1.0で生成 <br> <a href='https://civitai.com/models/2364703/rdbt-anima'>https://civitai.com/models/2364703/rdbt-anima</a> <br>  <br> ・comfyuiにデフォルトで入ってるEasyCacheノードで品質とスキップのバランスを探る 
<br>

