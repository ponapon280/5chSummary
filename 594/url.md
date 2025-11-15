# 1. https://huggingface.co/
## No.777:	2025/11/14(金) 10:21:34.08 ID:ZYPdj2qa0
 \>\>723 <br> もとめてるのとは違うっぽいがここのを使ってるわ <br> <a href='https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/tree/main'>https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/tree/main</a> 
<br>

## No.780:	2025/11/14(金) 11:00:10.45 ID:ZYPdj2qa0
 \>\>723 <br> そのcivitaiのBF16と中身同じだと思うがここにもあります。ワイはスペックの関係でGGUFしか使えないよく分からんが <br> <a href='https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models'>https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models</a> 
<br>

# 2. https://mega.nz/
## No.893:	2025/11/14(金) 20:25:48.02 ID:79Ta6arG0
 なんか新しいモデルがでているみたいだけど素のQwen Image Edit 2509用にアニメキャラをかわいそうな <br> NSFW画像にするLoraを作ったよ <br>  <br> 3060だと30時間経っても学習が終わっていないけど、200エポックでも公式サイトのキャラクタ紹介の <br> スクリーンショットからある程度変換できるようになったので公開 <br> <a href='https://mega.nz/file/Et92RR7I#os-GLA-tlvJseZOQlC_AADJXZ5ggq5TeuylPSojoIA0'>https://mega.nz/file/Et92RR7I#os-GLA-tlvJseZOQlC_AADJXZ5ggq5TeuylPSojoIA0</a> <br>  <br> プロンプトは「A girl is raped by men.」 <br>  <br> 学習方法もREADME.mdに入れておいたから、誰かもっといいGPU持っている人こういうLoraの作成おながいします 
<br>

## No.967:	2025/11/15(土) 10:31:32.08 ID:c+fAHcAg0
 \>\>893 <br> 250エポック(1500ステップ)版できたよ <br> <a href='https://mega.nz/file/1xNGXBjb#T64Pmb3PzGMGOQW9aO_WbLuWcK5MpUaCRYHHLNYpAqo'>https://mega.nz/file/1xNGXBjb#T64Pmb3PzGMGOQW9aO_WbLuWcK5MpUaCRYHHLNYpAqo</a> <br> 200エポック版で背景が残ってしまう場合が多かった点が改善されている <br>  <br> 元の学習データ全部anime coloringで生成したせいか漫画やラノベの表紙でもアニメ調に <br> 変換されるから学習データの画風は固定化しないほうがいいかも <br> ポーズや表情は収束しやすいようにあえて固定化したけど、いろいろなものを用意して <br> 学習用プロンプトも細かく変えて対応した方が汎用性は高まりそう <br>  <br> まだまだ実験しないと細かいところはわからない 
<br>

# 3. https://civitai.com/
## No.105:	2025/11/11(火) 14:49:37.98 ID:3u5HObxd0
 \>\>102 <br> 2509のFP16はHagefaceなんかなかったからCivitaiにあったこれを使ってる <br> <a href='https://civitai.com/models/1981702/qwen-edit-2509-new-version'>https://civitai.com/models/1981702/qwen-edit-2509-new-version</a> <br>  <br> 今見たらコメントで「FP16じゃなくてBF16だぞ」ってあったから、嘘つかれてるだけかもしれない 
<br>

## No.704:	2025/11/13(木) 22:19:09.74 ID:YYyefdML0
 Qwenの追加学習モデルが出とった <br> bf16とfp8があってRapid-AIOに速度面では劣るが、格子状ノイズが出ずに画質が良い <br> NSFWにも対応で、試した中では一番ちゃんと出てるかもしれん <br> 二次とfp8はまだ試してない <br> <a href='https://civitai.com/models/2120166/'>https://civitai.com/models/2120166/</a> <br>  <br> もう一つは、 <br> Qwenのプロンプトが中国語以外でも、より効くようにするLora、だそうや <br> 簡単なnsfwプロンプトで試した限りでは、画質が少し良くなった程度やったけど <br> 込み入ったプロンプトなら差が出てくるんかな？ <br> <a href='https://civitai.com/models/2122341'>https://civitai.com/models/2122341</a> 
<br>

## No.723:	2025/11/13(木) 23:49:43.49 ID:ORE1x5vf0
 Wan2.2 Animateのfp16が配布されてるのはここだけかな？ <br> kijai氏のはfp8しかない <br> <a href='https://civitai.com/models/1974861?modelVersionId=2238586'>https://civitai.com/models/1974861?modelVersionId=2238586</a> 
<br>

## No.726:	2025/11/13(木) 23:59:22.65 ID:MRSL8gBw0
 わりとアニメもいけそうなんやね <br> <a href='https://civitai.com/articles/22143/qwen-anime-loras-a-quick-and-dirty-comparison'>https://civitai.com/articles/22143/qwen-anime-loras-a-quick-and-dirty-comparison</a> 
<br>

## No.730:	2025/11/14(金) 00:34:16.20 ID:1qa8yHbv0
 \>\>727 <br> <a href='https://civitai.com/models/1906441/qwen-edit-reality-transform-by-aldniki'>https://civitai.com/models/1906441/qwen-edit-reality-transform-by-aldniki</a> <br> これ？確かに面白そう 
<br>

## No.731:	2025/11/14(金) 00:48:33.16 ID:MkMtZrLw0
 \>\>730 <br> そっちは試してなかったな <br> ワイの試したのははこっちや <br> <a href='https://civitai.com/models/2121900'>https://civitai.com/models/2121900</a> 
<br>

## No.743:	2025/11/14(金) 02:24:32.63 ID:3nuqe3pj0
 \>\>742 <br> つこうたんは↓やけど、QwenEditUtilが必要やったわ <br> 他のニキにとっては普通なんやろうけどミトコンドリアやからワイは知らんノードやった… <br> でも無事できて満足や。これで抜いて明日頑張るんやワイは <br> <a href='https://civitai.com/models/2110229/qwen-editanime2real?modelVersionId=2396073'>https://civitai.com/models/2110229/qwen-editanime2real?modelVersionId=2396073</a> 
<br>

## No.874:	2025/11/14(金) 18:27:24.89 ID:MkMtZrLw0
 Qwen image edit 2509 の二次専門学習済モデル <br> Danbooruタグと自然言語に対応しているらしい <br>  <br> <a href='https://civitai.com/models/2122738/'>https://civitai.com/models/2122738/</a> 
<br>

## No.876:	2025/11/14(金) 18:38:44.92 ID:Q75Ygs/r0
 \>\>874 <br> ええな <br> ワイ感やと40GBのダウソに1時間以上かかるから <br> 同じ作者のリアス風LoRAを先に試すで <br> <a href='https://civitai.com/models/1994924/chromaqwen-anime'>https://civitai.com/models/1994924/chromaqwen-anime</a> 
<br>

