# 1. https://huggingface.co/
## No.43:	2026/10/09(金) 23:24:12.62 ID:I25OXLX60
 <a href='https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo'>https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo</a> <br> ComfyUI対応まだぁ？ 
<br>

## No.57:	2026/10/10(土) 00:01:07.68 ID:CypW7Iig0
 \>\>43 <br> <a href='https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/diffusion_models'>https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/diffusion_models</a> 
<br>

## No.659:	2026/10/11(日) 12:14:19.33 ID:Pe+3pQNe0
 \>\>635 <br> ちょっと古いデータやけど試しまくるならこれがええかも <br> <a href='https://huggingface.co/datasets/Takenoko3333/danbooru-artist/tree/main/wildcard/portrait'>https://huggingface.co/datasets/Takenoko3333/danbooru-artist/tree/main/wildcard/portrait</a> <br> <a href='https://huggingface.co/datasets/Takenoko3333/danbooru-artist/tree/main/wildcard/artist'>https://huggingface.co/datasets/Takenoko3333/danbooru-artist/tree/main/wildcard/artist</a> 
<br>

# 2. https://mega.nz/
## No.27:	2026/10/09(金) 22:33:47.95 ID:4tfntU8F0
 minimax h3 1f学習、ワイは盛大に間違っていた。 <br> 学習でgradient_checkpointingフラグっていうのがあって、メモリ効率化のかわりに学習速度が落ちるってやつがあるんや。 <br> 速度低下を嫌ってワイは使ってなかったんだが、kohyaニキのDocにblocks_to_swap使うなら入れろとあって使ってみた。 <br> うは、劇的に学習メモリ減って、それでblocks_to_swapを減らしたら学習時間が短縮しおったわ。どんだけ転送がボトルネックになっとるんじゃ。 <br> さらに400サイズ画像1セット2枚組構成だとblocks_to_swapを最大48にしたらVRAM12GBも視野に入るじゃんか。 <br> もちろん相応に通常RAMやら学習時間がお察しな話にはなるんだが。 <br> ということでそのお試しで作ったfl2va dim32 alpha32の騎乗位Loraやで。強度0.7くらいお勧め。 <br>  <br> <a href='https://mega.nz/folder/RXcU0DxL#NrbgLwTotsu8vh8uKqy6YQ'>https://mega.nz/folder/RXcU0DxL#NrbgLwTotsu8vh8uKqy6YQ</a> <br> pussy_test_fV4.safetensors 
<br>

## No.386:	2026/10/10(土) 16:06:51.65 ID:vvG3yLyu0
 なんやスレがワープしてると思ったら。仕方ない、まだ調整中だがアレを出すしかないか。 <br>  <br> minimax h3 ref2va用の改善版触手Loraが焼けたので連携するで。強度0.7くらいから試してみてや。 <br>  <br> なお素材に使ったのと同じ嘘つき妖精でしか動確してなくて、他だとどうなるかサッパリやで。 <br> 参照画像の切り替え病とかワンパターン病の可能性もあるかもしれん。 <br> とはいえ前回と比べてもここに出せる程度にはレベルが上がったと思うので、まあ楽しんでみてや。 <br>  <br> <a href='https://mega.nz/folder/RXcU0DxL#NrbgLwTotsu8vh8uKqy6YQ'>https://mega.nz/folder/RXcU0DxL#NrbgLwTotsu8vh8uKqy6YQ</a> <br> tentacle_test_rv2.safetensors 
<br>

## No.454:	2026/10/10(土) 18:58:40.27 ID:CpiiXkue0
 pixivに動画をうごイラとして投稿する時に投稿容量上限16MBギリギリを攻めやすくできるようにツール作ったで <br> 完全にローカルで動く <br> <a href='https://mega.nz/file/Y2cwmLSJ#0NhDxUk439oOegWCF0ddNgu4gqCg2bscHKV4NLNv7Ic'>https://mega.nz/file/Y2cwmLSJ#0NhDxUk439oOegWCF0ddNgu4gqCg2bscHKV4NLNv7Ic</a> <br>  <br> 解像度5％;100％、FPS1;30が選べて動画の一部だけ切り出すクリップ機能も付けた <br> 変換前に予想ファイルサイズが表示されるから15MBくらいになるように品質上げていけばOKや <br> <a href='https://tadaup.jp/Afl5nBuC.png'>https://tadaup.jp/Afl5nBuC.png</a> 
<br>

## No.511:	2026/10/10(土) 21:08:24.26 ID:CpiiXkue0
 3スレ前で出した簡易minimax h3のUIの新バージョンや　comfyUI勉強するの面倒だったりUIが使い勝手よくないなって思ってるニキ向け <br> 新規導入はInstall.batを起動してACCEPTと入力、前バージョン導入済みの場合はUpdate.batを起動して前バージョンがあるフォルダを指定 <br> <a href='https://mega.nz/file/ZylxQJqR#dBBZTYY0xO8uYGDfrWtZp8hnICNQFh4ggP9hXl1k4OE'>https://mega.nz/file/ZylxQJqR#dBBZTYY0xO8uYGDfrWtZp8hnICNQFh4ggP9hXl1k4OE</a> <br> <a href='https://tadaup.jp/AxiRcQb7.png'>https://tadaup.jp/AxiRcQb7.png</a> <br>  <br> 元からある機能 <br> 日本語プロンプトをLLMで適したプロンプトに変換・画像縦横比をそのままに適した解像度を算出・最初の画像を最後の画像と同一にできる <br>  <br> 新機能 <br> UI内にスタジオを終了ボタンを導入・入力済みプロンプトの消去ボタン・生成完了時SE鳴らす機能（任意）・生成時間測定 <br> 画面比率を維持したまま解像度を自動で算出する際に小サイズと中サイズから選べるように・R2Vとmotion contextにも対応 <br> R2Vのプロンプトも日本語で書けばLLMでminimax h3に適したものに書き換えてくれるで（画像や動画を読み込んだ上で書いてくれる） 
<br>

## No.539:	2026/10/10(土) 22:53:35.68 ID:n6zYw2fD0
 サンイチ <br> これはピチスーエージェントがスライム姦されるAI産の漫画や <br> <a href='https://mega.nz/file/0ytwETTY#PwlBd12qS8QrevjVSUKXKpVCpUaO5UFM6Q-X0gPzh6o'>https://mega.nz/file/0ytwETTY#PwlBd12qS8QrevjVSUKXKpVCpUaO5UFM6Q-X0gPzh6o</a> <br> ショタ優位的なやつが作りたかったのか、スライムモノが作りたかったのかはワイにもようわからん <br> 竿役の見た目が不定形なら楽じゃね？って思いながらやったけど、結局手や触手よりアホ手間かかるのは確かやった <br> <a href='https://tadaup.jp/AtuYzHmC.png'>https://tadaup.jp/AtuYzHmC.png</a> <br> <a href='https://tadaup.jp/Apu9tPlQ.png'>https://tadaup.jp/Apu9tPlQ.png</a> <br> <a href='https://tadaup.jp/AR3jzd9F.png'>https://tadaup.jp/AR3jzd9F.png</a> <br> <a href='https://tadaup.jp/AwPGeQa3.png'>https://tadaup.jp/AwPGeQa3.png</a> <br> <a href='https://tadaup.jp/AOtfovgE.png'>https://tadaup.jp/AOtfovgE.png</a> <br> <a href='https://tadaup.jp/ABMUF4Vt.png'>https://tadaup.jp/ABMUF4Vt.png</a> 
<br>

# 3. https://civitai(com/red 共用)
