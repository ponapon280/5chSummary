# 1. https://huggingface.co/
## No.379:	2026/07/21(火) 19:59:04.43 ID:fEioOpl80
 \>\>345 <br> 二次ならchinmanニキのNSFW LoRA使えばそれなりのものが出るで <br> 三次は知らん <br> <a href='https://huggingface.co/chinmankokumin/AnimeNSFW3'>https://huggingface.co/chinmankokumin/AnimeNSFW3</a> 
<br>

## No.520:	2026/07/22(水) 11:55:47.61 ID:+EEAxHzq0
 <a href='https://huggingface.co/microsoft/Mage-Flow-Base'>https://huggingface.co/microsoft/Mage-Flow-Base</a> <br> Microsoftの4Bパラメータ、画像生成、画像編集モデルらしい 
<br>

# 2. https://mega.nz/
# 3. https://civitai(com/red 共用)
## No.28:	2026/07/20(月) 15:35:04.79 ID:TYGKSJWQ0
 サンイチ <br> Krea2用のcheckpointを更新したやでよかったら使ってみてや <br> SDXL時代の塗りに近いのが出ると思うやで <br> <a href='https://civitai.com/models/2739202'>https://civitai.com/models/2739202</a> <br>  <br> NSFWとケモナー要素を追加学習させとるせいで、 <br> 指定がないとすぐ脱いだり吐いたりするから注意してや <br> <a href='https://tadaup.jp/7apQNed5.png'>https://tadaup.jp/7apQNed5.png</a> <br> <a href='https://tadaup.jp/7HIiz2Ld.png'>https://tadaup.jp/7HIiz2Ld.png</a> <br>  <br> 画像の行為は窒息の危険を伴なうから真似したらあかんで 
<br>

## No.208:	2026/07/21(火) 05:04:13.10 ID:qS1Zdk2c0
 \>\>205 <br> anima baseやで <br> loraはこれ <br> <a href='https://civitai.red/models/2745224/anima-prim-fiorire-kuroinu-kedakaki-seijo-wa-hakudaku-ni-somaru?modelVersionId=3087797'>https://civitai.red/models/2745224/anima-prim-fiorire-kuroinu-kedakaki-seijo-wa-hakudaku-ni-somaru?modelVersionId=3087797</a> 
<br>

## No.586:	2026/07/22(水) 16:13:29.43 ID:1pn0dVl50
 恐らくこれ <br> <a href='https://civitai.red/models/2797050/capcom-vs-snk-2-millionaire-fighting-2001-style?modelVersionId=3152765'>https://civitai.red/models/2797050/capcom-vs-snk-2-millionaire-fighting-2001-style?modelVersionId=3152765</a> 
<br>

## No.624:	2026/07/22(水) 18:55:32.05 ID:bIEBqze60
 Noobがキャラクターリファレンス系っぽいの公開してくれてるな <br> <a href='https://civitai.red/models/2797093/noob2-project-character-reference-bypass-injector-research'>https://civitai.red/models/2797093/noob2-project-character-reference-bypass-injector-research</a> 
<br>

## No.703:	2026/07/23(木) 05:14:50.26 ID:3TKRewPm0
 \>\>586 <br> 外人ニキから「俺もKOFで学習してみたんだけど高解像度になってドット絵にならん」ってわざわざチャットで質問きてたから以下のような回答した <br>  <br> 150x150のピクセルアートを、ニアレストネイバー（補間なし）で8倍（1200x1200）に拡大して教師画像に使用。Animaだと2倍や4倍拡大ではAIがピクセルアートとして認識するのに不十分に感じることが多く、8倍にしてようやく「ピクセルグリッド表現」が画風として学習され始めた。 <br> ここにある &quot;v0.0.0&quot; と &quot;v0.0.1&quot; がそれぞれ 4倍、2倍で学習して「失敗」と感じた→ <a href='https://civitai.red/models/2689816'>https://civitai.red/models/2689816</a> <br> <a href='https://fate.5ch.io/test/read.cgi/liveuranus/1781100167/791'>https://fate.5ch.io/test/read.cgi/liveuranus/1781100167/791</a> にも書いたが、過学習気味にやるとピクセルパーフェクトに近い画風になる。 <br> ドット絵としてジャギーを際立たせる場合cosineじゃなくてconstantの1e-04でガシガシやったほうがいい。 <br> もちろん副作用もある。格ゲードット絵の場合、教師画像が低いとポージングが固くなる（右手を上げたものが頻出する）、過学習しすぎると男性キャラクターが筋肉質なものしか出なくなる。上条当麻や緋村剣心のような比較的細身な男性キャラクターを生成しようとしてもガッシリとした筋肉質なキャラクターで出てしまったりした。 <br> dim/alphaはどうなんだろう……32/32で高めに取れとか外人ニキには回答しちゃったけど、肌感普通に低dimでもイケそうな感じするんだよな。めんどいから試してないけど <br> 参考元の &quot;Anima - Ragnarok Online Monsters&quot; はdim32/alpha32だった <br>  <br> ああ……こういうケースに使うのがいいのかな？redditの住人が言ってた「constantでガシガシ学習させた後に過学習手前のエポックからcosineに切り替えて仕上げる」みたいな焼き方 
<br>

## No.812:	2026/07/23(木) 16:49:59.86 ID:+Z+Qy4T/0
 \>\>783 <br> Dasiwaの作者自身がFP8 MixedのほうがINT8 ConvRotより品質が上と評価してるな <br> DasiwaのFP8 MixedはただのFP8ではなく多くのレイヤーをBF16/FP16で残してるみたいで、ファイルサイズが普通のFP8の1.3倍ある <br> INT8 ConvRotはそういう工夫はしてないみたいで普通のFP8と同じくらいのファイルサイズしかない <br> <a href='https://civitai.red/articles/27174/comparison-safetensors-vs-gguf'>https://civitai.red/articles/27174/comparison-safetensors-vs-gguf</a> 
<br>

## No.833:	2026/07/23(木) 17:51:39.42 ID:C62IKhNT0
 <a href='https://civitai.red/models/2799559/hitomikrea2?modelVersionId=3155942'>https://civitai.red/models/2799559/hitomikrea2?modelVersionId=3155942</a> <br> ファイル名間違って一回やり直してもうた同じファイルやが <br> 瞳と麗子を別のキャプションで学習 <br> それぞれちょっとだけ違う顔が出るで <br> <a href='https://ul.h3z.jp/X44iJ2z7.webp'>https://ul.h3z.jp/X44iJ2z7.webp</a> <br> <a href='https://ul.h3z.jp/0FxCh2hs.webp'>https://ul.h3z.jp/0FxCh2hs.webp</a> 
<br>

