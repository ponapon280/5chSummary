# 1. https://huggingface.co/
## No.464:	2026/08/07(金) 15:02:19.62 ID:uqdRcnt40
 CUDAもPythonも使わない超軽量MiniMax H3 <br> <a href='https://huggingface.co/infosave/MiniMax-H3-Turbo-cmf'>https://huggingface.co/infosave/MiniMax-H3-Turbo-cmf</a> <br>  <br> 詳しいことは分からんけど低スペ民でも満足に使えるのかもしれない <br> no Python, no PyTorch, no CUDA toolkit, no ffmpeg.だそうだ 
<br>

## No.473:	2026/08/07(金) 15:19:53.51 ID:GruOBSTO0
 \>\>470 <br> 公式のhfコマンドつかおう <br>  <br> <a href='https://huggingface.co/docs/huggingface_hub/guides/cli'>https://huggingface.co/docs/huggingface_hub/guides/cli</a> 
<br>

## No.483:	2026/08/07(金) 15:42:31.44 ID:i549iAbu0
 <a href='https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo'>https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo</a> <br> これのTurboLoRAを試してるんだけど、音のガビガビが取れんのや <br> モデルは <a href='https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora/tree/main'>https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora/tree/main</a> から落としたminimax_h3_turbo_4step_ema_ckpt850.safetensorsを使用 <br> ComfyUIはデスクトップ版で3.10.2＋22コミット（2340099） <br>  <br> TurboLoRAなし <a href='https://tadaup.jp/8EkW3eqL.mp4'>https://tadaup.jp/8EkW3eqL.mp4</a> <br> TurboLoRAあり（12step） <a href='https://tadaup.jp/8VzmrTW1.mp4'>https://tadaup.jp/8VzmrTW1.mp4</a> <br>  <br> LoRAの強度を0.7に下げてもあまり変わらず <br> ほかに見落としがあるんやろか 
<br>

## No.528:	2026/08/07(金) 16:59:10.79 ID:oE5aTBDL0
 H3-Context-IRっぽいものを再現するLoRAらしい <br> <a href='https://huggingface.co/lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA'>https://huggingface.co/lightx2v/MiniMax-H3-Prompt-Rewriter-LoRA</a> 
<br>

## No.783:	2026/08/07(金) 22:28:48.47 ID:z82E7iDu0
 <a href='https://huggingface.co/lightx2v/Minimax-h3-Turbo/tree/main'>https://huggingface.co/lightx2v/Minimax-h3-Turbo/tree/main</a> 
<br>

## No.799:	2026/08/07(金) 22:40:04.86 ID:qJ+0NS0i0
 <a href='https://huggingface.co/Kijai/MiniMax-H3_comfy'>https://huggingface.co/Kijai/MiniMax-H3_comfy</a> <br>  <br> lightx2vはcomfyではこっち使わないとダメじゃねえの？？？ 
<br>

## No.809:	2026/08/07(金) 22:58:36.17 ID:sPvpGYBIa
 >FL2V(T2V)をベースに蒸留しており、R2V-turboは後日リリース予定です。続報をお待ちください。  <br> <a href='https://huggingface.co/lightx2v/Minimax-h3-Turbo/discussions/1'>https://huggingface.co/lightx2v/Minimax-h3-Turbo/discussions/1</a> 
<br>

## No.907:	2026/08/08(土) 02:22:50.20 ID:xrsmFEY80
 チャッピーのおかげで注目度高まってるか？ <br> aratakoさんがfull duplexに挑戦したらスレ民のチンコ擦り切れそうやな <br> <a href='https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B'>https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B</a> 
<br>

# 2. https://mega.nz/
# 3. https://civitai(com/red 共用)
## No.692:	2026/08/07(金) 20:45:15.36 ID:QdjUXdS50
 <a href='https://civitai.red/models/2839091/minimax-workflow-or-auto-prompt-r2v-anime?modelVersionId=3204591'>https://civitai.red/models/2839091/minimax-workflow-or-auto-prompt-r2v-anime?modelVersionId=3204591</a> <br>  <br> このワークフロー面白いな <br> 参照画像からLLMにプロンプト書かせて生成してくれる <br> 標準ではLMstudioとgemma4 12b使ってたけど、koboldにgemma4_31b_heretic_Q8で接続してうまく動いた。 <br> 日本語で、簡単にシチュを指示するだけでいいからかなり遊べるわ 
<br>

