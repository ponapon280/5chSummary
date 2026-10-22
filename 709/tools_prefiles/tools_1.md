# 生成AI関連「ツール」話題抽出レポート

## ComfyUI / ComfyUI関連
- **MOSS Image BBOXノード**: BBOX拡張をクラシックモードでも使えるようにしたfix版が作成された。幅・高さの即時反映、Alt+左クリックで重なりボックス選択、ダブルクリックで直接プロンプト入力が可能。クラシック・Nodes2.0両対応。DLパス: jnva（レス124）
- **MOSS BBOXノード対応状況**: 非公式だがForgeNeoでもMOSSのBBOX拡張が使える状態（レス42）。BBOXを使った生成は「ポン出し」と呼べるかという議論があった（レス92）
- **MOSS用途別ワークフロー**: MOSSは用途ごとにシステムプロンプトだけ変えたWF（ワークフロー）を分けて使うのが良さげというスレ上の見解（レス104）
- **Python直書きでのノード作成**: ワイルドカード内でのフラグ分岐が分からないため、プロンプト作成用ノードをPythonで直書きしているユーザーがいる。comfyでもforgeneoでもなく非UIでやりたいとのこと（レス152）。ComfyUIをバックエンドにAPI利用するか、pythonから直でDiffusionPipeを呼ぶ方法がMOSSのQuick startに載っているとのアドバイスあり（レス154）
- **Power Puter**: ワイルドカード等の処理に「Power Puter」で大抵のことができるという言及（レス156）
- **AI謹製コードの共有問題**: AIが生成したノーメンテコードがgitを汚染し続けているのではという懸念（レス220）。コードではなくAIへの指示で共有する時代が来るというスレ上の見解（レス223）

## ForgeNeo (Forge系WebUI)
- **MOSS対応**: ForgeNeoでもMOSSが使える（非公式）（レス41-42）。ただし公式対応とMOSS LoRA設定テンプレが出るまで待つべきとの意見あり（レス44）
- **ユーザー層の限界**: MOSS専用UIを作っても、comfyUIを使えずforgeneoも使っていないニッチな層向けにしかならないとの指摘（レス142）
- **宗教法人forgeneo**: 一部ユーザーがcomfyのスパゲッティノードアレルギーからforgeneo信奉者を自称（レス147）

## sd-scripts / LoRA学習ツール
- **sd-scripts MOSS LoRA学習**: VRAMに収めても結構重い。block swapでなくunslothのoffloadでもうちょっと速くなるかと思ったが伸びなかった（レス19）。kohyaニキ曰く最適化は全然できていない状態。VRAM不足ならblock_swapのほうがunsloth_offloadより速くなる（レス53）
- **sd-scripts更新**: anima用テンプレートを最小限の書き換えでMOSSのキャラ学習に試用。CAME使用でanimaの倍くらい処理時間がかかりLossも0.34から始まったが学習できている（レス127）
- **MOSS LoRA学習時間**: 4070s 1000step 1024×1024で大体1時間20分程度（レス168）。5時間回してもLossが下がりっぱなしで底打ちしなかった例あり（レス171）

## Fizgig / ai-toolkit / Kohya_lora_param_gui (LoRA学習ツール)
- **Fizgig**: 環境依存（おま環）で動かなかったユーザーがおり、代わりにai-toolkitが動いた（レス116）
- **ai-toolkit**: came実装がないため以下の改造が必要だった（レス116）:
  - requirements.txtに"came-pytorch==0.1.3"を追加
  - ui/src/app/jobs/new/SimpleJob.tsxに"{ value: 'came', label: 'CAME' }"を追加
  - ai-toolkit/toolkit/optimizer.pyのcame実装をチャッピーに全文見せて追加してもらう
  - toolkit/util/convrot_quant.pyに"and torch.cuda.get_device_capability(x.device)[0] >= 8"を追加
  - 現在はLoKR+CAMEでトレーニングできている
- **Kohya_lora_param_gui**: おま環で動かなかった（レス116）
- **Fizgig画風LoRA**: 7000ステップで平均Lossずっと0.67だった。コヒャパラムグイも試す予定（レス218）

## RedRayz (ツール)
- **MOSS暫定対応**: RedRayzニキがMOSSに暫定対応した（レス179）

## LMStudio
- **VRAM溢れ**: LMStudioを起動しながらMOSS生成をやるとVRAMから溢れまくった。31Bでは無理との報告（レス138）

## MOSS専用UI (自作ツール)
- **自作MOSS専用UI**: MOSS専用UIを自作して使用中。エージェントに頼めば簡単に作れるが、提供しても文句言われるだけなので緩やかに終わらせるほうがcomfyUIの発展に寄与するというスレ上の見解（レス140）
- **専用ソフトの需要**: コマごとにキャラ3人指定・動き指定できるソフトなら超絶需要があるというスレ上の意見（レス165）

## MOSS JSONフォーマット整備ツール
- **MOSS JSON流し込み用フォーマット整備**: MOSSをJSONで流し込んでいる人向けにフォーマットを整えるツールが作成された。Gemini3.8fに一言頼んで全部やってもらった。修正はしない（できない）（レス219）

## プロンプト共有・UIの未来
- **UI共有から指示共有へ**: 画像共有がプロンプトで行われるように、UIもUIそのものよりエージェントへの指示で共有してくれたほうがありがたい時代になるというスレ上の見解（レス167、レス223）

## 生成UI全般の学習遍歴
- **ツール学習ステップ**: NAIで部族語を学び→SDWebUIでControlNetやLoRAを学び→sd-scriptsで自作LoRAを学び→ComfyUIで画像生成の流れを学んできたというスレ上の経験（レス199）

## A1111 (WebUI)
- **歴史**: A1111の登場からまだ4年しか経っていないが体感12年くらい（レス115）

## クラウドLLMサービス
- **MiniMax / SpaceBunny**: MiniMaxがLLMで1位になりそう。SpaceBunnyの時はそこまで凄くなかったとの印象（レス97、レス107）。23日にウェイト公開予定、エージェント用特化型（レス110）

## チャットツール
- **ChatGPT UI変更**: うちのchatGPTから一時チャットを永続チャットにするボタンが消えた（レス37）※チャッピー関連のツールUI話題

## Qwenシリーズ（画像生成以外）
- **Qwen2.1文字レンダリング**: qwen2.1では一応文字入れできるが文字というか字体が残念すぎる。MOSSのオタク理解力で文字入れしたいという文脈での言及（レス185）