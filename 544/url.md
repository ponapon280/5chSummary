# 1. https://huggingface.co/
## No.40:	2025/05/17(土) 18:27:15.62 ID:I3NbCA2t0
 サンイチ <br> 前スレのwanvideo蒸留lora（高速化） <br> <a href='https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors'>https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors</a> <br> 推奨設定は lora weight 0.5、CFG 1、step 4、scheduler flowmatch_causvid <br>  <br> schedulerは unipc 等でも使えなくもない、CFG1だとネガティブが効かない？ <br> 低stepでの生成なので条件によっては通常生成より品質（動き）が落ちる <br> 標準が8;stepに対して4stepで済むので生成時間は劇的に縮む <br> Kijai版以外であるNative版のGGUFでも使用可能 <br> 前スレ >923 <br> >そこらへんてcausvidのblock調整で改善したりしないかな <br> >そういやVACEとcausvid lora同時に使う場合はcausvidの0,5,10,15,20,25,30,35のblockをオフにしなきゃいけないらしい 
<br>

## No.41:	2025/05/17(土) 18:29:46.89 ID:O6XWhnQJ0
 plumMix_v1.0DSや <br> <a href='https://huggingface.co/yyy1026/songMix/tree/main'>https://huggingface.co/yyy1026/songMix/tree/main</a>  <br> ワイ得な銀髪x褐色モデルや <br> <a href='https://files.catbox.moe/chbeym.webp'>https://files.catbox.moe/chbeym.webp</a> <br> <a href='https://files.catbox.moe/lwz0px.webp'>https://files.catbox.moe/lwz0px.webp</a> <br> <a href='https://files.catbox.moe/a1dqji.webp'>https://files.catbox.moe/a1dqji.webp</a> <br> <a href='https://files.catbox.moe/k32goj.webp'>https://files.catbox.moe/k32goj.webp</a> <br> もうちょいギラつかせてもよかったかもしれん <br>  <br> とりあえずすんなり追加出来るんはここまでや <br> PDはもうちょいかかりそうや 
<br>

## No.124:	2025/05/18(日) 00:30:54.36 ID:VIDtnMqK0
 EasyReforgeアップデートしたらぶっこわれちゃた… <br> 1. Navigate to your 'stable-diffusion-webui-reForge' folder <br> 2. Activate the virtual environment with: venv\Scripts\activate <br> 3. Run: pip install <a href='https://huggingface.co/Panchovix/torchvision-windows-blackwell2.0-nightly/resolve/main/torchvision-0.22.0a0%2Bd28001e-cp310-cp310-win_amd64.whl'>https://huggingface.co/Panchovix/torchvision-windows-blackwell2.0-nightly/resolve/main/torchvision-0.22.0a0%2Bd28001e-cp310-cp310-win_amd64.whl</a> --force-reinstall <br> 4. Restart the WebUI <br> この表示出たから実行しただけなのに <br> 余計なことせんかったらよかった 
<br>

## No.182:	2025/05/18(日) 11:13:15.99 ID:wBtUIXmP0
 \>\>174 <br> 0.2alphaをDLして試してみてるけど <br> ワイ環(RTX3080：12GB/RAM128GB)だと1枚生成に20分かかるわこれ・・・ <br>  <br> テキストエンコーダー <br> <a href='https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/text_encoders'>https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/text_encoders</a> <br> VAE <br> <a href='https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/vae'>https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/vae</a> <br>  <br> これらで生成しとるんやが高速化出来る方法あるんか？ 
<br>

## No.215:	2025/05/18(日) 14:19:33.56 ID:yUFi7wEU0
 さっきどんぐりLV足らんかったのに元に戻っとるな <br>  <br> 再度発色調整したplum v1.2無印、AD、LOとv1.1DS、MIの5つをhugにアップしたで <br> <a href='https://huggingface.co/yyy1026/songMix/tree/main'>https://huggingface.co/yyy1026/songMix/tree/main</a> <br> 使うてみて気になるとこあったら遠慮せんと言うてや 
<br>

## No.288:	2025/05/18(日) 20:05:56.12 ID:8IrCd3Ml0
 vace用の四角形動画作れるツール作ったんで置いときますね <br> <a href='https://huggingface.co/nims1/my_test_model/tree/main/mouse2rect'>https://huggingface.co/nims1/my_test_model/tree/main/mouse2rect</a> <br> <a href='https://files.catbox.moe/jo9i5s.mp4'>https://files.catbox.moe/jo9i5s.mp4</a> <br> <a href='https://files.catbox.moe/a6be8e.mp4'>https://files.catbox.moe/a6be8e.mp4</a> <br> 動きはopen poseかdepth 絵の崩れにくさと手軽さはこっちが上みたいな感じ <br> 単純な動きならこっちもありかも 
<br>

## No.335:	2025/05/18(日) 23:33:30.90 ID:TTsjEz+Ta
 \>\>330 <br> ワイ環でFASTじゃないFULLのFP8やと15秒くらいやな <br> HiDreamのエロモデルUncencerdのFP8に効果あるんかわからんけど検閲解除版llamaに差し替え <br> <a href='https://files.catbox.moe/hhnndt.jpg'>https://files.catbox.moe/hhnndt.jpg</a> <br> <a href='https://files.catbox.moe/v3teug.webp'>https://files.catbox.moe/v3teug.webp</a> <br> <a href='https://huggingface.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF/tree/main'>https://huggingface.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF/tree/main</a> 
<br>

## No.349:	2025/05/19(月) 02:30:29.44 ID:cd4VRe9y0
 \>\>320 <br> 綺麗に整ったフローやな、美を感じるで <br>  <br> アドバイスっつーか情報共有っつーか他所様の丸パクリなんやけど、テキストエンコーダは以下のものを使うと画質が向上するらしいで <br> <a href='https://huggingface.co/easygoing0114/HiDream_HQ-models/tree/main'>https://huggingface.co/easygoing0114/HiDream_HQ-models/tree/main</a> <br> clip_lはCLIP-SAE-VIT-L;に、clip_gはCLIP-VIT-bigG;に、t5xxlはflan-t5-xxl;に差し替えや <br> llamaは\>\>335ニキのものか、RAM128GBやったらそれのsafetensor版でも大丈夫やで <br> これらはファイル名の通りFP32やから、ComfyUIの起動オプションに「--fp32-text-enc」を追加や 
<br>

## No.395:	2025/05/19(月) 15:20:16.71 ID:iX8rQxKy0
 \>\>349 <br> テキストエンコーダーのllamaやけどsafetensor版はfp32のsafetesnsorsファイルが見付からんかったから <br> <a href='https://huggingface.co/GuangyuanSD/REDiDreamviaHiDreami1Uncensored/tree/main'>https://huggingface.co/GuangyuanSD/REDiDreamviaHiDreami1Uncensored/tree/main</a> <br> Meta-Llama-3.1-8B-Instruct-abliterated-fp16.safetensors <br> これを入れてみたんやけどこいつを読み込ませるとプロンプトガン無視の謎模様とかお菓子の画像とか出てくるわ・・・ 
<br>

## No.485:	2025/05/19(月) 23:46:44.93 ID:sLHEQbbD0
 \>\>395 <br> 情報サンガツ <br> RAMもストレージもカツカツなんで余分なの消したCLIP-Gを置いておく　多分厳密なTE-onlyになってない <br> <a href='https://huggingface.co/AX1Y2JP/my_test2_model4/tree/main'>https://huggingface.co/AX1Y2JP/my_test2_model4/tree/main</a> <br>  <br> TEはDarkIdol+↑のCLIP-Gのみ　Distance_n サンプラー、JKニキのプロンプトで試してみた結果↓　llama-abliteratedだと崩壊するという人もいるみたいだから、このモデルにも相性問題あるかも <br> <a href='https://files.catbox.moe/vf5ppd.jpg'>https://files.catbox.moe/vf5ppd.jpg</a> 
<br>

## No.600:	2025/05/20(火) 17:30:53.55 ID:XugtdVIc0
 plumMix_v1.0PDや <br> <a href='https://huggingface.co/yyy1026/songMix/tree/main'>https://huggingface.co/yyy1026/songMix/tree/main</a>  <br> なかなか固定出来んでホンマ手間取ったわ <br> <a href='https://files.catbox.moe/zdlczk.webp'>https://files.catbox.moe/zdlczk.webp</a> <br> <a href='https://files.catbox.moe/hkchlk.webp'>https://files.catbox.moe/hkchlk.webp</a> <br> <a href='https://files.catbox.moe/na9m4z.webp'>https://files.catbox.moe/na9m4z.webp</a> <br> 分身やチビキャラ出るときあるけどそこはガチャってや <br> エロはどうしてもLO寄りになるからガチPDニキはtoddlerconで調整してやで 
<br>

## No.741:	2025/05/21(水) 01:59:13.28 ID:EGMNjWTW0
 たぶんこの辺のメッセージが関係ありそうな気がするんやけど、この手順やっても <br> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.ていわれて解決せんのや。GPTちゃんに相談してもいまいち解決せんくてなぁ…ちょっとアドバイスほしいで <br>  <br> WARNING: Official nightly torchvision packages may have compatibility issues with some extensions like ADetailer. <br> If you experience problems, you can replace the official package with a custom compatible version: <br>  <br> 1. Navigate to your 'stable-diffusion-webui-reForge' folder <br> 2. Activate the virtual environment with: venv\Scripts\activate <br> 3. Run: pip install <a href='https://huggingface.co/Panchovix/torchvision-windows-blackwell2.0-nightly/resolve/main/torchvision-0.22.0a0%2Bd28001e-cp310-cp310-win_amd64.whl'>https://huggingface.co/Panchovix/torchvision-windows-blackwell2.0-nightly/resolve/main/torchvision-0.22.0a0%2Bd28001e-cp310-cp310-win_amd64.whl</a> --force-reinstall <br> 4. Restart the WebUI <br>  <br> <a href='https://litter.catbox.moe/jy0asl.png'>https://litter.catbox.moe/jy0asl.png</a> 
<br>

# 2. https://mega.nz/
## No.244:	2025/05/18(日) 16:36:47.12 ID:ALDAV6ev0 BE:434877256-2BP(0)
 今日のパンツ <br> は無地パンツのハイウエスト版 <br> パンツというかブルマっぽい <br> <a href='https://files.catbox.moe/5zw9c9.webp'>https://files.catbox.moe/5zw9c9.webp</a>　<a href='https://files.catbox.moe/iqg3ju.webp'>https://files.catbox.moe/iqg3ju.webp</a>　<a href='https://files.catbox.moe/8znvav.webp'>https://files.catbox.moe/8znvav.webp</a>　<a href='https://files.catbox.moe/adensl.webp'>https://files.catbox.moe/adensl.webp</a> <br>  <br> LoRAにしたので使ってみてくだされ <br> MEGA：<a href='https://mega.nz/folder/O3xnHBaZ#L1tk8oOJjD23Dr7VYUfuSw'>https://mega.nz/folder/O3xnHBaZ#L1tk8oOJjD23Dr7VYUfuSw</a> <br> civitai：<a href='https://civitai.com/models/1592865/plain-high-waisted-panties-lora'>https://civitai.com/models/1592865/plain-high-waisted-panties-lora</a> 
<br>

# 3. https://civitai.com/
## No.206:	2025/05/18(日) 13:30:50.13 ID:wZqflbww0
 \>\>182 <br> VRAM 12Gはきついなあ　なんせ過去一重いLocalモデルやから <br> 4090で960x1536を出すのに90秒前後かかるんで相当重いのは確か <br>  <br> DeVかFastの蒸留モデルを使ったほうが速くなる(CFG=1, DeVだとStep 28）　画質は落ちるけどDeVなら供用範囲じゃないかな <br> あとテキストエンコーダーはコレに入っているGGUFのほうが小さくて済むかもしれない <br> <a href='https://civitai.com/models/1496362/hidream-full-gguf-q5km-uncensored?modelVersionId=1692682'>https://civitai.com/models/1496362/hidream-full-gguf-q5km-uncensored?modelVersionId=1692682</a> <br>  <br> メジャーになれば高速化軽量化が進むかもしれないけど 
<br>

## No.214:	2025/05/18(日) 14:12:45.80 ID:RMrNiTBr0
 \>\>191 <br> One obsessionの1.1気に入って使ってるな <br> 1344×1792くらいはほぼ破綻なくポン出しできる <br> 1.2は微妙だったのですぐ1.1に戻したで <br> <a href='https://civitai.com/models/1318945?modelVersionId=1734437'>https://civitai.com/models/1318945?modelVersionId=1734437</a> 
<br>

## No.244:	2025/05/18(日) 16:36:47.12 ID:ALDAV6ev0 BE:434877256-2BP(0)
 今日のパンツ <br> は無地パンツのハイウエスト版 <br> パンツというかブルマっぽい <br> <a href='https://files.catbox.moe/5zw9c9.webp'>https://files.catbox.moe/5zw9c9.webp</a>　<a href='https://files.catbox.moe/iqg3ju.webp'>https://files.catbox.moe/iqg3ju.webp</a>　<a href='https://files.catbox.moe/8znvav.webp'>https://files.catbox.moe/8znvav.webp</a>　<a href='https://files.catbox.moe/adensl.webp'>https://files.catbox.moe/adensl.webp</a> <br>  <br> LoRAにしたので使ってみてくだされ <br> MEGA：<a href='https://mega.nz/folder/O3xnHBaZ#L1tk8oOJjD23Dr7VYUfuSw'>https://mega.nz/folder/O3xnHBaZ#L1tk8oOJjD23Dr7VYUfuSw</a> <br> civitai：<a href='https://civitai.com/models/1592865/plain-high-waisted-panties-lora'>https://civitai.com/models/1592865/plain-high-waisted-panties-lora</a> 
<br>

## No.472:	2025/05/19(月) 22:57:51.67 ID:mpPds0xQ0
 \>\>470 <br> 使ったワークフローの中略にlora未対応と記載があった <br> <a href='https://civitai.com/models/1583832/gguf-model-coupled-with-kj-nodes-for-high-quality-first-and-last-frame-wan-video-workflow'>https://civitai.com/models/1583832/gguf-model-coupled-with-kj-nodes-for-high-quality-first-and-last-frame-wan-video-workflow</a> <br>  <br> 恐らくGUFFの量子化モデルも変わらないと思うから <br> 動きが悪いというより動作補完をしているloraが機能してないぽい <br> 乳揺れとか腰振り程度の動きなら通常i2vを回した方が良さそう <br> ただi2vを最終フレームで連結し続けると画像崩れが心配になる 
<br>

## No.618:	2025/05/20(火) 18:47:04.94 ID:N/zfX5SX0
 これはどうでしょう <br> HunyuanVideo POV Missionary <br> <a href='https://civitai.com/models/1087616/hunyuanvideo-pov-missionary'>https://civitai.com/models/1087616/hunyuanvideo-pov-missionary</a> 
<br>

## No.624:	2025/05/20(火) 19:33:19.49 ID:YmbROL4L0
 <a href='https://civitai.com/articles/13990/join-the-nsfw-ai-archives'>https://civitai.com/articles/13990/join-the-nsfw-ai-archives</a> <br> 5月23日が最終日とかあるけどマジなの？ 
<br>

## No.656:	2025/05/20(火) 20:38:27.35 ID:N/zfX5SX0
 こういう謎のLoraなんなんやろうね <br> 時期が時期だから隠れキリシタン感ある <br> <a href='https://civitai.com/models/1597638/36?modelVersionId=1807911'>https://civitai.com/models/1597638/36?modelVersionId=1807911</a> 
<br>

## No.661:	2025/05/20(火) 20:58:04.81 ID:gdYHBd3z0
 \>\>656 <br> WAIで,1girl, 1boyにトリガー合わせてやってみたやが <br> タグ不足とは言え無地の画風やfacelessなbaldも出てくるぐらいやな <br> WOTM=Woman on the Manあたりの略称かなと思ったけど思ってたのとは違う感じやった <br> <a href='https://litter.catbox.moe/zoc6d8.jpg'>https://litter.catbox.moe/zoc6d8.jpg</a> <br>  <br> <a href='https://civitai.com/user/alexshen123456914'>https://civitai.com/user/alexshen123456914</a> <br> これを見るとmodel, post, imageが黒一色で1つずつしか出ないからこのユーザの情報が壊れてるだけの可能性あり 
<br>

## No.801:	2025/05/21(水) 13:19:11.99 ID:iOLMry8N0
 We're updating our policies to comply with increasing scrutiny around AI content.  <br> New rules ban certain categories of content including incest, self-harm, diaper, and a number of bodily excretions.  <br> All NSFW uploads now require metadata to stay visible. A new moderation system aims to improve content tagging and safety. <br>  <br> 私たちは、AIコンテンツに関する監視の強化に対応するため、ポリシーを更新しています。  <br> 新しいルールでは、近親相姦、自傷行為、おむつ、多くの排泄物を含む特定のカテゴリのコンテンツを禁止しています。  <br> すべてのNSFWアップロードは、表示された状態を維持するためにメタデータを必要とするようになりました。 新しいモデレーションシステムは、コンテンツのタグ付けと安全性の向上を目指している。 <br>  <br> Policy & Content Adjustments <br> <a href='https://civitai.com/articles/13632/policy-and-content-adjustments'>https://civitai.com/articles/13632/policy-and-content-adjustments</a> 
<br>

## No.821:	2025/05/21(水) 14:14:13.18 ID:Q3dm/zDR0
 <a href='https://civitai.com/articles/13632/policy-and-content-adjustments'>https://civitai.com/articles/13632/policy-and-content-adjustments</a>　見てきたけど <br> 「子供テーマやマイナーな話題のコンテンツはフィードに表示されません。」　とあるけど <br> 子供は二次絵でも実写系でも以前から駄目になってたと思うけど、「マイナーな話題」って何よ 
<br>

## No.885:	2025/05/21(水) 17:47:23.75 ID:YI5pPCIc0
 やっぱり包茎チンポがどーしてもうまくいかん…なんでだ？ <br> 何度も生成してたまにうまくいったかな、程度でしかできない <br> <a href='https://litter.catbox.moe/r5d1av.jpg'>https://litter.catbox.moe/r5d1av.jpg</a> <br>  <br> プロンプトはこんな感じ <br> (shota,small penis,foreskin:1.0), <br> blush,sweat,fellatio,saliva, steam, tongue_out, looking_down,uvula, open_mouth, from_side,  <br>  <br>  <br> ↓のLoRA使っても変わらず <br> <a href='https://civitai.com/models/1514972?modelVersionId=1738881'>https://civitai.com/models/1514972?modelVersionId=1738881</a> 
<br>

