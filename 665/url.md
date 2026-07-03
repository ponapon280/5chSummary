# 1. https://huggingface.co/
## No.130:	2026/06/30(火) 10:16:17.73 ID:NYcLUewP0
 \>\>57 <br> krea2TurboRawINT8_krea2Turbo.safetensorsはこれかな? → <a href='https://civitai.com/models/2724771/krea2-turboraw-int8'>https://civitai.com/models/2724771/krea2-turboraw-int8</a> <br>  <br> しかしノイズしか出力されなかった（ComfyUIはさっきアップデートして0.26.0 / frontendは1.45.19） <br>  <br> Krea2-Turbo-Int8-ConvRot.safetensors → <a href='https://huggingface.co/lilcheaty/Krea2-INT8-ConvRot/tree/main'>https://huggingface.co/lilcheaty/Krea2-INT8-ConvRot/tree/main</a> <br> でも同様 <br> しかも0.3s/itくらいしか早くならない <br>  <br> どこが悪いのかわかるニキ教えておくれー <br> <a href='https://i.ibb.co/DD7JdhmT/workflow.png'>https://i.ibb.co/DD7JdhmT/workflow.png</a> 
<br>

## No.174:	2026/06/30(火) 13:31:21.26 ID:VrnUZN6r0
 krea2のint8関連の情報が出てきて3060のワイはウレシイ… <br> <a href='https://huggingface.co/Winnougan/Krea-2-Base-Turbo-NVFP4-FP8-INT8'>https://huggingface.co/Winnougan/Krea-2-Base-Turbo-NVFP4-FP8-INT8</a> <br> ここのノード使っとるけどワイのつまづいた点をあげとく…誰かの参考になれば <br> ・comfyuiは現時点での最新版にする <br> ・comfyuiネイティブはINT8モデルのみ対応、 <br> convrot INT8は上記ノードを使うなどする <br> ・Lora使う場合は上記ノードのLora modeはdynamicがいいらしい？ 
<br>

## No.829:	2026/07/02(木) 13:11:48.34 ID:aGjD6tyc0
 他の人のがあるとは思うんやが一応置いとくで <br> AIエージェントでスキル化して自分で作れるようにしとくほうがええで <br> <a href='https://huggingface.co/sylvanian/anima-INT8/tree/main'>https://huggingface.co/sylvanian/anima-INT8/tree/main</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai(com/red 共用)
## No.83:	2026/06/30(火) 01:45:09.37 ID:XSvEgn9q0
 さんいち <br>  <br> 同シード、同プロンプトでのKrea2のリアル系Loraの比較実験 <br> <a href='https://tadaup.jp/6ZiITyzP.png'>https://tadaup.jp/6ZiITyzP.png</a> (Strength=1.0) <br> <a href='https://tadaup.jp/6dIoSHcy.png'>https://tadaup.jp/6dIoSHcy.png</a> (Strength=1.5) <br> 左上：Loraなし <br> 右上：KNPV3_1 (<a href='https://civitai.red/models/2725430/krea-2-nsfw-v3)'>https://civitai.red/models/2725430/krea-2-nsfw-v3)</a> <br> 左下：MysticXXX_KREA2_v1 (<a href='https://civitai.red/models/2728644/krea-2-mystic-xxx)'>https://civitai.red/models/2728644/krea-2-mystic-xxx)</a> <br> 右下：realism_engine_krea2_v2 (<a href='https://civitai.red/models/2688234/realism-engine-ideogram-4-krea-2)'>https://civitai.red/models/2688234/realism-engine-ideogram-4-krea-2)</a> <br>  <br> 指示の概要：草むら、両脚を広げる、胸を出す、服と体の汚れ、流れ出る精液、脱ぎ捨てられた下着、ピンク発光する白い毛筆文字でマンコを隠す 
<br>

## No.130:	2026/06/30(火) 10:16:17.73 ID:NYcLUewP0
 \>\>57 <br> krea2TurboRawINT8_krea2Turbo.safetensorsはこれかな? → <a href='https://civitai.com/models/2724771/krea2-turboraw-int8'>https://civitai.com/models/2724771/krea2-turboraw-int8</a> <br>  <br> しかしノイズしか出力されなかった（ComfyUIはさっきアップデートして0.26.0 / frontendは1.45.19） <br>  <br> Krea2-Turbo-Int8-ConvRot.safetensors → <a href='https://huggingface.co/lilcheaty/Krea2-INT8-ConvRot/tree/main'>https://huggingface.co/lilcheaty/Krea2-INT8-ConvRot/tree/main</a> <br> でも同様 <br> しかも0.3s/itくらいしか早くならない <br>  <br> どこが悪いのかわかるニキ教えておくれー <br> <a href='https://i.ibb.co/DD7JdhmT/workflow.png'>https://i.ibb.co/DD7JdhmT/workflow.png</a> 
<br>

## No.156:	2026/06/30(火) 12:29:47.04 ID:floC/Glu0
 \>\>141 <br> EasyWanは古いComfyUIでしか動かないので今使うのはあり得ない <br> しばらくWanを触ってないから最近の事情は知らんけど、DasiwaかSmoothmix作者のWFを「簡単なものから」使って理解していくのがいいんじゃないか？ <br> いきなりAIOを使っても構わんがEasyWanのWFを理解できなかったのならAIOも理解できない <br> <a href='https://civitai.red/models/1847730'>https://civitai.red/models/1847730</a> <br> <a href='https://civitai.com/models/1823089'>https://civitai.com/models/1823089</a> 
<br>

## No.694:	2026/07/02(木) 01:59:16.95 ID:GKQLt+qE0
 Animaでポーズ作ってKREA2で仕上げるためのワークフローやで <br> よかったらつかってみてや <br> <a href='https://civitai.com/models/2745645'>https://civitai.com/models/2745645</a> 
<br>

## No.776:	2026/07/02(木) 10:50:30.68 ID:GKQLt+qE0
 同人っぽい文字だすやつのKREA2版やで <br> <a href='https://civitai.com/models/118003'>https://civitai.com/models/118003</a> <br>  <br> 念のため、NSFWなシチュエーションで <br> 「あ゛っ;」「ぱんっ;」「ぐちゅ;」みたいな文字を入れたら <br> 主に顔の横か性器の横にピンクの文字がでるようにしておいたやで <br> <a href='https://tadaup.jp/7PePyQYR.png'>https://tadaup.jp/7PePyQYR.png</a> <br> <a href='https://tadaup.jp/7ptsYBwR.png'>https://tadaup.jp/7ptsYBwR.png</a> 
<br>

## No.948:	2026/07/02(木) 21:05:13.76 ID:aci66UVR0
 \>\>945 <br> これつこてるで <br> <a href='https://civitai.red/models/2540187/breast-size-slider-krea-2-zit'>https://civitai.red/models/2540187/breast-size-slider-krea-2-zit</a> 
<br>

