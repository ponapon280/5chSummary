# 1. https://huggingface.co/
## No.6:	2025/10/24(金) 10:30:24.48 ID:I9BEnSDe0
 サンイチ <br> 音声の新しいオモチャが出たで <br> <a href='https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo'>https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo</a> 
<br>

## No.38:	2025/10/24(金) 14:22:49.15 ID:P+w3ew/l0
 \>\>6 <br> <a href='https://huggingface.co/NandemoGHS/Anime-Llasa-3B-Captions'>https://huggingface.co/NandemoGHS/Anime-Llasa-3B-Captions</a> <br> モデルはこれか <br> システムプロンプトにメタデータを入れたり、（囁き）って入れたりして制御できるらしいな 
<br>

## No.106:	2025/10/24(金) 18:39:28.51 ID:dv699yFA0
 \>\>6 のローカルでの動かし方メモ(cu129は使いたいCUDAのバージョンに合わせる) <br> git clone <a href='https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo/'>https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo/</a> <br> cd Anime-Llasa-3B-Captions-Demo <br> pip install torch torchaudio --index-url <a href='https://download.pytorch.org/whl/cu129'>https://download.pytorch.org/whl/cu129</a> <br> pip install -r requirements.txt <br> pip install spaces <br> python app.py 
<br>

## No.377:	2025/10/25(土) 17:18:19.36 ID:y/21J2eP0
 Anime-lasa-3Bの参照できたんやけど喘ぎ声ってどう指定するんやろ？ <br> <a href='https://litter.catbox.moe/zco1o52qr0o2asql.wav'>https://litter.catbox.moe/zco1o52qr0o2asql.wav</a> <br> ちな \>\>106,111,151 でできたんやけど \>\>106 はvenv切った方がええやろね <br> git clone <a href='https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo/'>https://huggingface.co/spaces/OmniAICreator/Anime-Llasa-3B-Captions-Demo/</a> <br> cd Anime-Llasa-3B-Captions-Demo <br> py -3.12 -m venv venv <br> venv\Scripts\activate <br> pip install torch torchaudio --index-url <a href='https://download.pytorch.org/whl/cu128'>https://download.pytorch.org/whl/cu128</a> <br> pip install -r requirements.txt <br> pip install spaces <br> python app.py <br> あとffmpegは  ffmpeg-7.1.1-full_build-shared.7z 落さんとDLLに分離されてないで 
<br>

## No.418:	2025/10/25(土) 19:11:16.30 ID:uspKOoeg0
 \>\>403 <br> すまん素の環境てのがわからんのやが、\>\>106のはrequestにはこのアドレス指定されてるから44kやないんか？正直アドレスを指定しての導入はよく分かってなくてな… <br> ベースラインのは確かに16kらしいやが、そっちはNandemoGHS/Anime-XCodec2らしいやし <br>  <br> ニキの音質良くて感動したから当環境にも音質向上のを導入したいんや <br>  <br> <a href='https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz/'>https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz/</a> 
<br>

## No.422:	2025/10/25(土) 19:29:38.49 ID:FjqmvrA/0
 一応python_embededを使ったAnime-Llasa-3B-Captions-DemoのWindows用パッケージ作ってみたよ <br> <a href='https://huggingface.co/asfdrwe/WAI14DMD2-GGUF/blob/main/Anime-Llasa-3B-Captions-Demo.zip'>https://huggingface.co/asfdrwe/WAI14DMD2-GGUF/blob/main/Anime-Llasa-3B-Captions-Demo.zip</a> <br> 展開したらAnime-Llasa-3B-Captions-Demoフォルダ開いてrun.batをダブルクリックしてね <br>  <br> 元のライセンスがわからんから怒られたら消す <br> \>\>224のパッチは好きに使ってね 
<br>

## No.425:	2025/10/25(土) 19:42:50.14 ID:FjqmvrA/0
 参照音声を使う場合、元のAnime-XCodec2-44.1kHzは <br> <a href='https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz?not-for-all-audiences=true#1-model-summary'>https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz?not-for-all-audiences=true#1-model-summary</a> <br> - Input Sampling rate: 16 kHz (for encoding, same as XCodec2). <br> - Output Sampling rate: 44.1 kHz (decoded audio). <br> となっているんだけど、この辺の処理がおかしい気がしたので <br> - Sampling rate: 16 kHz (XCodec2 operates at 16 kHz). <br> のみのAnime-XCodec2にしてsr_codec=16000にしたのが　\>\>224　のパッチ <br>  <br> 参照音声を使わないならAnime-XCodec2-44.1kHz modelにsr_codec=44100で動く 
<br>

## No.589:	2025/10/26(日) 11:22:08.74 ID:mAlH18SP0
 <a href='https://huggingface.co/pixai-labs/pixai-tagger-v0.9'>https://huggingface.co/pixai-labs/pixai-tagger-v0.9</a> <br> こいつreforge拡張のtaggerで使えはせんのやろか 
<br>

## No.619:	2025/10/26(日) 13:06:10.76 ID:BCTzQ0Ro0
 需要があるか分らんけど、 <br> QwenImage用のリアル系のおしっこloraを学習してみたからよければ使って <br> <a href='https://huggingface.co/Yanagi099/My_Loras/tree/main/QwenImage'>https://huggingface.co/Yanagi099/My_Loras/tree/main/QwenImage</a> 
<br>

## No.638:	2025/10/26(日) 14:10:38.27 ID:WIh+spn50
 Qwen-Image-Edit-Rapid-AIOを試したくてはじめてcomfyuiのワークフローを触ります <br> 以下ページの説明にある画像と同じワークフローを作りたいですが、jsonが配布されて無い場合は目視で真似するしかないんですかね？ <br>  <br> <a href='https://huggingface.co/Phr00t/Qwen-Image-Edit-Rapid-AIO'>https://huggingface.co/Phr00t/Qwen-Image-Edit-Rapid-AIO</a> 
<br>

## No.665:	2025/10/26(日) 16:59:28.64 ID:PFEreJbM0
 <a href='https://huggingface.co/meituan-longcat/LongCat-Video'>https://huggingface.co/meituan-longcat/LongCat-Video</a> <br>  <br> 5分弱生成できるんやと 
<br>

## No.963:	2025/10/27(月) 15:49:57.65 ID:dV+ma7J90
 <a href='https://huggingface.co/valiantcat/Qwen-Image-Edit-MeiTu'>https://huggingface.co/valiantcat/Qwen-Image-Edit-MeiTu</a> <br> 一貫性が上がったファインチューニングモデル。まだ改善の余地あるけどこの手のモデルまだ出るのかな 
<br>

# 2. https://mega.nz/
# 3. https://civitai.com/
## No.70:	2025/10/24(金) 17:23:12.53 ID:P+w3ew/l0
 qwenベースのよさげなリアルモデルを見つけた <br> NSFWは含まれてないらしいけど造形がアジア系で良い感じ <br> <a href='https://civitai.com/models/2064895?modelVersionId=2336581'>https://civitai.com/models/2064895?modelVersionId=2336581</a> 
<br>

## No.72:	2025/10/24(金) 17:27:05.55 ID:V/GRYyG10
 <a href='https://civitai.com/models/1901521?modelVersionId=2152373&dialog=commentThread&commentId=985535'>https://civitai.com/models/1901521?modelVersionId=2152373&dialog=commentThread&commentId=985535</a> <br> Pony開発者「Too many mean comments, we decided not to release it.（あまりに意地悪なコメントが多いので、公開しないことにした。）」 <br>  <br> V7はもう終わり！閉廷！以上！みんな解散！ 
<br>

## No.440:	2025/10/25(土) 21:08:23.65 ID:ebA8RaVN0
 ちびたいのponyから作者の公開モデルから行けばすぐやで <br> 直なら<a href='https://civitai.com/models/1901521/pony-v7-base'>https://civitai.com/models/1901521/pony-v7-base</a> 
<br>

## No.522:	2025/10/26(日) 01:13:18.68 ID:4eMpMHPP0
 \>\>518 <br> ライティング関係のLoRAやとこれが好きだけど明るくなるってよりコントラストが強くなるって感じかも <br> <a href='https://civitai.com/models/1697073?modelVersionId=1967210'>https://civitai.com/models/1697073?modelVersionId=1967210</a> 
<br>

## No.978:	2025/10/27(月) 16:40:11.13 ID:E9rzlxi50
 ちょっとだけクオリティが上がる系のやつはワイの腐った目だと違いがわからないのでlora化したやつでええかなって <br> <a href='https://civitai.com/models/2075957'>https://civitai.com/models/2075957</a> 
<br>

