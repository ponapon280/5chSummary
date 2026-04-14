### 抽出された「ツール」に関する話題

以下は、提供されたログ（247〜447）から、生成AIに関連する「ツール」（ComfyUI/comfy、webUI、nano-banana、Stability Matrix、ForgeNeo、LM Studio、litVideoなど）に関する話題をすべて抽出・整理したものです。モデル（anima、リアス/ill/IL、Z-Image/ZIT/ZIE、LTX/LTX-2.3、FLUX、Wan、NAI、Qwen-Imageなど）中心の話題は除外。Qwenシリーズは画像生成以外の文脈（例: LLMとしての使用）のみ抽出。ツールが選ばれている理由や関連する言及を可能な限り含め、各投稿番号付きで引用・要約形式で記載。重複や文脈的にツール非関連はスキップ。

#### Stability Matrix関連
- **258**: Stability Matrixがuvバグで起動もパッケージ入れ直しもできなくなっちまったんだが同じ症状の人いる？
- **267**: >>258 ワイも昨日から起きてるで。Geminiでは解決できんかった。githubをみると他にもいるみたいで、解決するまで環境いじらんほうがいいかも。ForgeNeoを単独でインストールすれば使えるから、**Stability Matrixの問題やろな**（理由: バグ多発で信頼性低く、単独インストールの代替推奨）。
- **269**: >>267 やってくれたのぅStability Matrix……って感じだわ うちもチャッピーに聞きまくったけど解決できなくて「旧バージョンインスコしなおしたら？（笑）」とか言い始めたぜ（理由: バグ解決策が旧バージョンに戻す程度で非効率）。
- **275**: Stability Matrix君はもう何回もやらかしてるから動いてるなら迂闊にアプデしちゃいかんで（理由: 過去に複数回の重大バグ履歴あり、アップデート避けるべき）。
- **276**: StabilityMatrixは過去に「modelsフォルダの中身を無条件で全削除」もやらかしてるンゴね･･･（理由: 過去の致命的バグでデータ消失リスク高）。
- **336**: animaのモデル等データの保存場所について... Stability MatrixのPackages配下に保存... Package配下ではなく↓を参照するような設定にすることってできる？（Stability Matrixのモデル管理パス設定の柔軟性疑問）。
- **338**: >>336 パスの指定は素の**ComfyUI**なら \ComfyUI_windows_portable\ComfyUI\extra_model_paths.yaml に書くんだけど、**Stability Matrix**の管理下にあるComfyUIが同じようにextra_model_paths.yamlを参照するかは知らない（理由: Stability Matrixはカスタムパス管理が制限されやすい）。
- **340**: >>336 実際にやってみればそれで出来るってすぐ分かるだろ... >>338のようにextra_model_paths.yamlに書いてあると言ってもチンプンカンプンなんだろ（Stability Matrixのデフォルト設定で可能）。
- **342**: **Stability Matrix**は管理をよろしく任せるツールなのでそういうのは無理と割り切ったほうがいい気がする カスタマイズして使えるようにしたところでStability Matrixのアプデですぐ死ぬ（理由: 管理特化ツールゆえカスタム非推奨、アップデートで破壊的）。
- **344**: >>342 デフォで出来るよ >>336（Stability Matrixのデフォルトでモデルパス設定可能）。
- **413**: >>336についてだけどデフォルトでStabilityMatrix\Dataの方に設定されてたわ この間までそうじゃなかったからアプデで変わったっぽい C:\StabilityMatrix\Data\Packages\ComfyUI\extra_model_paths.yaml（アップデートでパス設定改善）。

#### ComfyUI/comfy関連
- **321**: >>320 **ComfyUI**にLM studioとのAPI連携ノードがあるから、LM studio起動しながらで**ComfyUI**のWFだけで完結するはず（理由: API連携でLLMと画像生成をComfyUI内で一元化可能）。
- **326**: >>320,323 **ComfyUI-QwenVL**とか**comfyUI-image-to-text-node**だとLLMのmodelをunloadするオプションがあるからLLM側の処理が終わったらVRAM解放してくれるので**Comfy側だけで作業できるよ**（理由: VRAM自動解放機能で並行処理効率化）。
- **338**: パスの指定は素の**ComfyUI**なら \ComfyUI_windows_portable\ComfyUI\extra_model_paths.yaml（ComfyUIの標準パス設定機能）。
- **351**: **comfyUI**いじってて始めて知ったんやが **webUI**でよく使ってたRealESRGAN_x4Plus Anime 6Bとかのアップスケールモデルは デフォで4倍になるモデルらしく、「モデルを使って画像を拡大」ノードにぶち込むと4倍になって凄い負荷がかかる...（ComfyUIとwebUIのアップスケール処理違いの気づき）。
- **364**: forgeneoとかなら作った画像を**ComfyUI**にぶち込んだらワークフロー見れるで（ComfyUIのWF解析機能）。
- **369**: 前から書いてた自作拡張ノードを一部アップロードしたわ **Dynamic Prompts**とwildcardsとSAM3とPixAI Taggertあと... **comfyui manager**経由だとinfo-prompt-toolkitで検索すれば出てくる（ComfyUI拡張ノードのアップロードとmanager経由インストール）。
- **417**: >>323 ワイはlihaoyun6/**ComfyUI-llama-cpp_vlm**って拡張機能使ってるわ **comfyui manager**ではなんか警告出てるけどね（理由: ComfyUI内でllama.cpp VLM連携、manager警告あっても動作安定）。

#### webUI関連
- **351**: **comfyUI**いじってて... **webUI**でよく使ってたRealESRGAN_x4Plus Anime 6Bとかのアップスケールモデルは... 逆に**webUI**のhireFIXとかの処理ってどうなってたんや？（webUIのhires.fix処理の内部挙動疑問、ComfyUI比較）。

#### ForgeNeo/reforge関連
- **267**: ForgeNeoを単独でインストールすれば使えるから（Stability Matrix代替として単独インストール推奨、理由: 安定性高）。
- **352**: reforgeとかも同じように内部では一旦4倍にしてからリサイズしてると思ってたんやが違うんか？（reforgeのアップスケール処理）。
- **364**: **forgeneo**とかなら作った画像をComfyUIにぶち込んだらワークフロー見れるで（forgeneoのWF共有・解析）。

#### LM Studio関連
- **320**: LLMにプロンプト聞きながらanima生成するにはどうすりゃいいんや？ **LM studio**のモデルをメモリから取り出しをこまめに押していくんか？（LM Studioのメモリ管理手間）。
- **321**: **ComfyUI**に**LM studio**とのAPI連携ノードがあるから（LM StudioとComfyUI連携で効率化、理由: WF完結）。

#### litVideo関連
- **301**: **litVideo**でseedance2.0の動画生成が順番待ち全然しなくなったんだけど、もしかしてもっとお得に生成できるサービスを他のサイトでやってたりするの？（litVideoの待ち時間短縮、代替サービス探し）。
- **303**: **litVideo**でseedance2.0の動画生成が順番待ち全然しなくなったんだけど...（同上）。

#### nano-banana関連
- **379**: まあ**nanobanana**なら四コマ位は実用範囲内やからな（理由: 四コマ漫画生成の実用性高）。

#### その他のツール（ollama, openRouter, nanoGPTなど）
- **341**: llmはsfwなら**ollama**のcloudモデルを使えばvram要らず（理由: VRAM不要でSFW LLM運用）。
- **347**: >>323 ある程度コストかけて良いんなら下のチャットUIみたいなの導入して、**openRouter**なり**nanoGPT**なりのAPIと紐づければプロンプト生成と画像生成両立できるで（理由: API連携でプロンプト生成+画像生成両立）。

#### Qwenシリーズ（画像生成以外: LLM文脈）
- **314**: 構図のお手本の画像を**QWEN3.5** とかに渡して画像生成用の説明英文吐かせた上で...（Qwen3.5 LLMとして画像説明英文生成、理由: 自然言語プロンプト補助でCN相当の構図制御）。
- **323**: 片方ずつなら出来るが並行は無理やから**QWEN**に聞く→メモリ解放→anima生成という地獄のような手間（Qwen LLMの逐次使用手間）。
- **326**: **ComfyUI-QwenVL**とか...（QwenVLノードで画像-to-text、VRAM解放機能）。

これでログ内の全ツール関連話題を網羅。ツール選好理由は主に「VRAM効率」「バグ耐性」「連携容易さ」「管理簡便さ」「待ち時間短縮」など。モデル比較内でもツール言及は抽出済み。