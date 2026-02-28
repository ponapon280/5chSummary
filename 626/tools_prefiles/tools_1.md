### 抽出された「ツール」に関する話題

ログから生成AI関連の「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなどに相当するもの、または類似のUI/ノード/プラグイン/マネージャー類）のみを抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）に関する言及は一切除外。ツールの選好理由や問題点、使い方などが明記されている場合も併記。

#### A1111
- **18**: WSLでa1111を起動してる最中にcomfyuiも起動して、停止させてからa1111に戻るとa1111のUIの挙動がおかしくなるな a1111を再起動しても治らん  
  *(ComfyUIとの併用時にUI挙動が乱れる問題。A1111再起動でも直らず)*
- **220**: A1111,Comfyui,NovelAIとかcivitai上で作られたやつなら解析できる  
  *(メタデータ解析ツールとの互換性言及)*

#### ComfyUI (comfy)
- **18**: WSLでa1111を起動してる最中にcomfyuiも起動して...  
  *(A1111との併用問題)*
- **52**: comfyuiでanimaのloraを途中から適用する方法ってある？  
  *(LoRA途中適用方法の質問)*
- **55**: >>52  ここのカスタムノードでスケジュール構文使うか カスタムノードなしのcoreだけならフックやな Create Hook Keyframes Interp + Create Hook LoRA -> Set Hook Keyframes -> Set CLIP Hooks  
  *(カスタムノード/コア機能(Hook/Keyframes)を使ったLoRAスケジュール適用方法)*
- **81**: >>55 サンプルのワークフローを使って[<lora:A:1.0>:0.5]と書いて生成してみたけどノイズの画像しか生成されなかった もしかしてスケジュール構文間違ってる？  
  *(ワークフロー/スケジュール構文のトラブルシュート)*
- **95**: 最近やたらとリアスとanimaの対立煽りやりたがっとるみたいやがcomfyと違って加熱せんと思うわ  
  *(ComfyUIの言及、対立煽りが起きにくい理由として)*
- **187**: comfyUI内で画像と動画を作るテスト(forgeユーザなんで) WF切り替えだけで続きができる便利やね 脱いでる時お尻のライン合わせてるの良くできてる anima -> wan2.2  
  *(画像/動画作成テスト、WF(Workflow)切り替えの便利さ強調。Forgeユーザーからの移行視点)*
- **188**: セリフ付き comfyuiで作れた  
  *(セリフ付き生成成功)*
- **192**: >>81 あー確かにanimaでcomfyui-prompt-controlのLoraスケジュール使うと砂嵐なるな ワイのやってる二つ目の方法の画像貼るわ  
  *(comfyui-prompt-controlノードのLoRAスケジュール問題)*
- **195**: >>81 なるべくcore以外のノードは省いて最小限にしたつもりや  
  *(Coreノード中心の最小構成推奨)*
- **198**: Codex凄いな 今SD Prompt Readerの改良版を作っていたんだけどMask編集したらメタデータが読めなくなる問題を解決出来たぞ  
  *(SD Prompt Readerノードの改良、メタデータ問題解決)*
- **209**: Comfyでメタデータ残したままWebpで保存するためのプラグインって ニキたちは何つかっとる？  
  *(メタデータ保存プラグインの質問)*
- **211**: >>209 俺はPNGでしか使ってないけど ComfyUI-SaveImageWithMetData(?)とかいうのでもできないっけ？ あとはここで名前がよく出るカスタムノードが１，２個あった気がするけど忘れた  
  *(ComfyUI-SaveImageWithMetDataなどのカスタムノード推奨)*
- **220**: A1111,Comfyui...解析できる  
  *(メタデータ解析互換)*
- **222**: Comufyのメタデータ（ワークフローとプロンプト）を格納して保存したPNGまたはWebpを それらのメタデータを保持したままJPEG/WebP/AVIF/JXLに変換出来るソフト...を探している  
  *(メタデータ保持変換ソフトの質問、ComfyUI前提)*
- **230**: >>195 サンガツ comfy coreの機能で実現できるもんなんやな Hookやフックからずっと逃げ続けてはいけない  
  *(Core機能/Hookの有用性)*

#### Forge / reForge / StabilityMatrix + Forge
- **56**: reForge民のﾜｲどんどん置いて行かれる  
  *(reForgeユーザー置いてけぼり感)*
- **187**: comfyUI内で画像と動画を作るテスト(forgeユーザなんで)  
  *(ForgeユーザーからのComfyUIテスト)*
- **234**: StabilityMatrix Forge使ってるんやがみんなComfyuiとStabilityMatrix Forgeはどのような違いがある？ 比較して教えて  
  *(StabilityMatrix + Forge vs ComfyUIの違い質問)*
- **235**: StabilityMatrix Forge使ってるんやがみんなComfyui使っとるんやな 2ヶ月目くらいの初心者なんやがcomfyuiとか言うのに変えた方がええんやろか  
  *(初心者視点、ComfyUI移行検討)*
- **236**: StabilityMatrixってcomfyも入れれるんやろ？ んでテンプレートから使い方学んでいくだけや  
  *(StabilityMatrixのComfyUI対応、テンプレート学習推奨)*
- **237**: forgeとcomfyuiの中間ぐらいの難易度で良いとこ取りしてくれる物があったらいいのに  
  *(Forge/ComfyUIの難易度比較、理想の中間ツール希望)*

#### easywan
- **193**: 超浦島やけどメモリ32gでeasywan動いたわ 開発したニキサンガツ wanってある程度自然言語効くよな？  
  *(メモリ32GBで動作確認、開発者感謝)*
- **239**: easywan2.2ではじめて一度comfyいれて面食らって凄い苦手に思ってたけど animaでもう一回comfyでやってみたらほんの少し理解が進んだ  
  *(ComfyUI入門前にeasywan使用、苦手意識からの移行)*

#### その他のツール/ノード/プラグイン
- **68**: animaのLoRA作成をしてみようと思うんだけど toolkitで今まで通りの流れで作れるの？  
  *(toolkitでのLoRA作成互換質問)*
- **198-200**: Codex凄いな ... SD Prompt Readerの改良版 ... Codexとチャッピーを併用 ... Mask編集したらメタデータが読めなくなる問題を解決  
  *(Codex: メタデータ解析/リンク表示ツール。SD Prompt Reader: ComfyUIノード。チャッピー併用で問題解決)*
- **214/219**: D2 Send Eagle愛用しとるけど連携のEagleが有償アプリなんでオススメし辛いっていう ... 基本のwebpとpngでメタデータの保存&参照が出来るのは勿論やけど カスタムノードとアプリ内でフォルダ分け&タグ付けが出来るからそこが便利やね 生成モデル別にカテゴリ分けしておけるから参照時は見易い ... 難点は...  
  *(D2 Send Eagle: メタデータ保存/フォルダ分け/タグ付け便利だが有償&一部難点)*
- **220**: メタデータを分析して、使われているcheckpointやLoRAがcivitai上にある場合リンクを表示してくれるツールやで  
  *(Civitaiリンク表示ツール)*
- **233**: 相互変換はないけどjpgやwebpへの変換はここのニキが既に作ってgithubに公開してたと思う  
  *(GitHub公開の画像変換ツール)*

**抽出総括**: 主にComfyUI/A1111/Forge関連が最多。ComfyUIはワークフロー/カスタムノード/メタデータ処理の柔軟さが理由で人気（動画生成、Hook活用など）。Forge/StabilityMatrixは初心者向け簡単さだが、ComfyUI移行推奨の声多し。easywanは低スペック動作が魅力。問題点として併用時のUI乱れやノード互換性が挙がる。理由明記なしの単発言及は省略せず全抽出。