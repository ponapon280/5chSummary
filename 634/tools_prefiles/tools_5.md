### 生成AI関連「ツール」に関する話題抽出結果

ログから「ツール」（ComfyUI(comfy), webUI, nano-bananaなどフロントエンド/ワークフロー/拡張ノード/タグger類など生成AI運用ツール）に関する話題をすべて抽出。モデル（NAI, illustrious, FLUX, Wan, Qwen-Image, anima, Z-Image, LTXなど）は除外。Qwenシリーズは画像生成以外の話題のみ抽出（本ログでは該当なし）。ツール選定理由が明記されているものは強調。

#### 847: ComfyUI
- 「Comfyくん生成した画像の履歴がAssetsパネルにあったりなかったりするバグどうにかならんか」
  - ComfyUIのAssetsパネルバグ指摘。

#### 858: easywan22, civitai
- 「今更ローカル動画に手出そうかと思ってeasywan22ってのを導入しようと思ったんだけど civitaiでのAPIキー入れてもダウンロードが全部弾かれちゃう」
  - easywan22導入時のcivitai APIキー問題、手動LoRAダウンロード必要か？と悩み。

#### 861: ComfyUI (公式WF), easywan22
- 「comfyuiの公式wfに手を出したほうがいい Easyとは書かれているけど 最終的な学習コストはcomfyuiの方が低い Easywan22を使っても得られるものが少ない」
  - **ComfyUI公式WF推奨理由**: Easywan22より学習コスト低く、得られるものが少ないためComfyUIを推奨。

#### 866: ComfyUI
- 「1からcomfyui学んでフロー繋げていってと考えると…」
  - ComfyUI新規導入のハードル高さを嘆く（easywan更新停止のため）。

#### 867: SeeThrough (ノード/拡張)
- 「UsageみるとAdd SeeThrough Load LayerDiff Model and SeeThrough Load Depth Model nodes ってかいてるけどmodelもnodeもライブラリにないや てかアプデしたらあかんかったかな？」
  - SeeThroughノード/モデル使用時のライブラリ欠如とanima使用不能問題。

#### 868: ComfyUI (ポータブル版/公式テンプレート)
- 「ポータブル版ダウンロードして最初から入ってる公式のテンプレートから欲しいの選ぶだけ」
  - ComfyUIポータブル版の公式テンプレート簡単使用を推奨。

#### 869: easywan
- 「今更easywanは罠やろ」
  - easywanを罠扱い（古いため）。

#### 870: easywan
- 「スペックが足りないからもう少し経ったらやろう ↓数ヶ月後 動画やれるようなスペックになったぞ！easywan使おう！と思ったら使えない」
  - easywanの陳腐化を嘆く。

#### 873: ForgeNeo (webui系)
- 「webui系で画像生成したことあるなら同系のUIでWAN動画作れるForgeNeoってのがある さすがにcomfyほどの柔軟性はないけどeasy使おうとする人なら先にこっち使ってもいいかも」
  - **ForgeNeo推奨理由**: webui系UIに慣れた人向け、easywan代替として柔軟性は劣るが使いやすい。

#### 874-877: Claude (インストール相談ツールとして), ComfyUI Manager
- 「インストール関係のお悩み相談はclaudeに聞けばあっという間に解決」「claudeに聞こう」「claudeにも聞いたけど結局comfy UI manager入れてもManageボタンどこにあるんかわからん アプデのせいやろか？」
  - Claudeをインストール相談ツールとして使用、ComfyUI ManagerのManageボタン位置不明（アプデ影響？）。

#### 881: SillyTavern
- 「SillyTavernおすすめ Live2DやVRMモデルとかも読み込めるし面白いよ」
  - SillyTavernをiPhone連携推奨（Live2D/VRM対応で面白い）。

#### 882: LM Studio
- 「LM StudioでGemma4 26B A4B使ってるけど…プリセットにエロ設定書いてthinkingオフにしたら倫理アウトなのも喋ってくれる」
  - LM StudioでGemma使用時のNSFW設定方法。

#### 884: unsloth studio
- 「unsloth studioでunsloth謹製の量子化モデル試したら動く…turboquantでもっと動くようになるとええな」
  - unsloth studioで量子化モデル動作確認。

#### 885: ComfyUI (ポータブル版/バージョン指定)
- 「easywanは消されたloraや本体が古過ぎる しかし、最新のcomfyuiでも互換性問題で動作が不安定中 一番良さそうなのはcomfyuiポータブルの0.17.0あたりの導入だと思う 0.18.0あたりから互換性がバグり散らし始めてる」
  - **ComfyUIポータブル0.17.0推奨理由**: easywan古すぎ、最新ComfyUI不安定のため0.17.0安定。

#### 891: ComfyUI (バージョン管理)
- 「マイナーバージョンが最新１個手前の0.17.xでxの値が最新のを入れてる xの部分は大きい方がバグフィックス進んでる…0.18.0は新機能でバグてんこ盛り」
  - **ComfyUI 0.17.x最新推奨理由**: バグフィックス進み安定、0.18.0バグ多め。

#### 893-898,905: ComfyUI (安定版議論)
- 「comfyの安定版は意見がバラバラ >>720 v0.17.2 >>885 0.17.0あたり >>891 0.17.xでxの値が最新」「少なくとも現状ではcomfyuiのv0.17.xのどれかが一番マシ」「一度でもv0.18.0以上にすると仮想環境が変わってお手上げ」「動画と静止画でも違うんやなかったっけ？ SDXL系のノードが0.17で使えなくなった」
  - ComfyUI安定版としてv0.17.x系を複数推奨（0.18.xで仮想環境破壊/SDXLノード不具合）。

#### 907: Claude (Oppenheimer? Claude Opus), LoRAマネージャー
- 「easywanでロラマネージャーのせいで動かなかったんだけど クロードオーパスに聞いて一時的にオフにしたらいけたわ コードは入ってる場所指定したらクロードが書いてくれた」
  - Claude OpusでeasywanのLoRAマネージャーオフコード生成成功。

#### 908,917-918,923,926,929,937: ComfyUI (バージョン/Frontend/Core/アップデート)
- 「ComfyUI Frontendのように複数バージョンを並行…Coreはほぼ毎週マイナーバージョンが上がる」「0.18.1使ってエラー出たらClaude codeで修正」「ComfyUI v0.18.2（git版）で妙な不具合やWanで生成出来なくなるとかにはなっとらんな」「ComfyUIデスクトップ版も脳死でアップデートし続けてるけど サブグラフが壊滅以外問題なし」「動画も画像も出力が違う…気にならんのなら最新でええ」「Gradio版に乗っかってる機能だと歌詞の書き起こしが適当すぎて困る」
  - ComfyUIバージョン管理議論、0.18.x修正・Claude活用、最新版脳死更新OK（一部問題）、Gradio版歌詞書き起こし不満。

#### 921: workflows (ComfyUIサンプル)
- 「workflowsにサンプルワークフローあるやろ」
  - ComfyUI workflowsサンプル使用推奨。

#### 933: smZnodes (ComfyUI拡張ノード)
- 「LTXに手をつけてみたが見事にsmZnodesトラップに引っかかって issues見つけるまで数時間無駄」
  - smZnodesトラップ（互換性問題）で時間浪費、新技術時は船団（スレ議論）活用推奨。

#### 942-943: SD Prompt Saver (メタデータ保存ノード)
- 「SD Prompt Saverに代わるメタデータ保存ノード無いんか？ SD Prompt Saverが1年以上更新止まったせいかAnything Everywhereの無線通信が届かなくなった」「リアス生成だけならAnything Everywhereの通信が通るバージョンまで戻せばいい」
  - SD Prompt Saver更新停止/Anything Everywhere通信不具合、代替ノード求む。

#### 945-946,948-949,951-952,957,960-961: gazou kiritori, banana (nano-banana?), PixAI tagger, WD14-Tagger
- 「gazou kiritoriの作者ニキスレにおるんかな 画風LoRA作るために久しぶりに使ったんやけどめちゃくちゃ進化しててすっごい使いやすくて感動」「なにそれ便利そう、ググっても見つからんのやが正式名称なんて言うん？」「PixAI taggerなんてあるんか WD14ノードが逝ったから代わり探してた」「PixAI TaggerはComfy立ち上げなくても単独で動くアプリ版…軽快で安定」「WD14-Taggerはonnxruntimeに依存で壊れやすいがPixAI Taggerは依存なしで安定、NSFW/キャラタグ対応」「bananaでやっとるな 会話長くなると失敗するけどピクセル補完/高画質化もしてくれるから便利」「トリミングはペイントで力技」
  - **gazou kiritori推奨理由**: 進化で使いやすい。
  - **PixAI tagger推奨理由**: WD14代替、安定（依存なし）、NSFW/キャラタグ対応、単独アプリ版軽快。
  - **nano-banana? (banana)**: 切り抜き/補完/高画質化便利（会話長で失敗）。

#### 947: 拡張ノード群 (リリース予定)
- 「拡張ノード自体はもう出来ているんで来週末リリース…ノードの総数は50くらい」
  - 新拡張ノード群（画像/動画生成用）リリース予定。

#### 968: kobold, LM Studio
- 「kobold起動しよかと思たらGemma4未対応…LM Studioデビュー」
  - kobold Gemma未対応のためLM Studioへ移行。

#### 980: litellm, Unsloth
- 「litellmでUnslothのローカルモデルにapi飛ばしたら動いた…量子化効いて速い」
  - **litellm + Unsloth推奨理由**: gemini無料APIレートリミット回避、ローカル速い。

#### 987,991,995: ComfyUI Manager, See-through
- 「nodesが入れられない Unresolved Missing Nodes…managerちゃんと入ってるのか？拡張機能の管理ってボタンがあればOK？」「READMEのInstallationやったんか？」「用途ごとにComfy環境作る…See-throughだけ入れたらノード表示されん…geminiにログ放り込んだらmatplotlib足らんでエラー」
  - ComfyUI Managerインストール/ボタン確認、See-throughノードエラー（matplotlib/scipy等pip install解決、AIログ解析推奨）。

#### その他関連言及（軽微）
- 881: Live2D/VRM（SillyTavern対応）。
- 936: Gradio版（歌詞書き起こし不満）。

**抽出まとめ**: 主にComfyUI（バージョン安定議論/easewan代替最多）、easywan（陳腐化罠）、タグger/切り抜きツール（PixAI/gazou kiritori/banana安定推奨）が目立つ。Claude/LM Studio/litellm等補助ツールも散見。理由は主に「安定性」「学習コスト低」「依存少/軽快」「代替容易」。