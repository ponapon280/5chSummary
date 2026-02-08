### 抽出された「ツール」に関する話題一覧

ログから生成AI関連の「ツール」（ComfyUI/comfy、A1111、LM-Studio、nano-banana、Stability Matrix、SimpleComfyUI、AceMusic/Ace-Step、diffusion-pipe、sd-scripts、Kohya、xformers、sage attention、photoshopなど）のみを抽出。モデル（NAI、Pony、illustrious/リアス/Noobai/FLUX/Wan/Qwenなど）に関する言及は除外。Anima/Zimage/Zitなどの文脈上モデル寄りのものはツールとして扱わずスキップ。ツールが選ばれている理由やインストール/使用に関する具体的な話題を中心に抽出。各レス番号と該当抜粋を記載。

#### ComfyUI (comfy) 関連
- **>>23**: Install via git使ったで（公式のnode-list.jsonに載ってないノードのインストール）。
- **>>40**: なんやカバー機能は公式配布のワークフローは使えないんか…ワイミジンコやから有志待ちや。
- **>>44**: >>20をインストールすれば使えるらしいで が、ワイはインストールに苦戦中…！
- **>>46**: >>20やけど手動インストールの次の pip install git+ これはどのディレクトリで実行するんやろか･･･ComfyUI/custom_nodesフォルダ内？
- **>>47**: AceMusicが依存しとるAce-Stepが古いpeftライブラリに依存してて これ用のComfyUI環境作らんとワイ赤ちゃんには解決出来ない。
- **>>48**: わいはcustom_nodes内でやったで（pip install）。
- **>>52**: pip installやからvenvなのかなと思ったけどcustom_nodes内でええんか。
- **>>55**: 実際のところComfyUIじゃなくて(venvの)pythonにライブラリとして入れるんやからどこでやっても構わんはずや ワイは一旦インストールを諦めるけども上手く行ったら顛末を教えてクレメンス。
- **>>61**: >>55 どうやら成功したが･･･これACE-Step 1.5じゃなくてv1じゃね･･･？ 生成時にDLされるモデルがv1の3.5bモデルだわ（ComfyUIカスタムノードの挙動）。
- **>>66**: animaはタグ入力にadaptive prompt使って今までのwildcard活用しつつ、自然言語はtextノード使ってconcatしたら使いやすそうかな（ComfyUIノード活用）。
- **>>67**: 作者のブログ貼っておくわ ここ見ると1.5で使えてるように見えるんだがなぁ（AceMusic関連ComfyUIノード）。
- **>>68**: AceMusic Model Loaderノードさえあればモデル自体は1.5を拾ってきて入れればいいんとちゃうん？ 公式WFだとturboしか使えないからbaseをいれるために導入してみようかと。
- **>>71**: カスタムノード内のacemusic_handler.pyをメモ帳とかで開いて見ると自動DLのモデルも読み込み指定のモデルもACE-Step-v1-3.5Bになっとるんよなぁ･･･ これを単純に1.5のモデルになるように書き換えればええのかもしれん（ComfyUIカスタムノード修正）。
- **>>76**: >>71 こちらでも昼休み使って調べてたがなんかおかしいよな ワイも一旦見なかったことにするわ。
- **>>136**: あれ、comfyアプデしたらanimaが砂嵐になった。
- **>>140**: リアス用と動画用でcomfy分けてるけど 新しいcomfy試したいんで分けていれよQwenVL gguf用にしよう。
- **>>146**: 4070tisでzuntanニキのsimplecomfy使ってて...これからanimaとzitで遊ぶにはどこから環境構築したほうがええんやろか ここ見てるとsimplecomfyで普通にcomfy最新版にアプデするとまずそうやけど 手っ取り早いのはstability matrixかな？
- **>>147**: 別途simple comfyインスコして最新にアプデしてみては？ simpleは余計な事してない分、楽だぞ（SimpleComfyUI経由のComfyUI更新）。
- **>>149**: simpleComfyUIはPythonとPytorchのバージョンが古いので固定されてた気がしてそこが厄介そう。
- **>>150**: 今更simplecomfy勧めるの全く意味分からんわ 公式のポータブル版でええやろが。
- **>>151-152**: simplecomfyuiあかんのか？ → 悪いところはないが良いところもない だったらComfy-Org公式を使ったほうがいいよね（ComfyUIのインストール方法比較、公式推奨）。
- **>>155**: simple以外となるとsageアテンションやっけ？ 高速化系とか環境構築を自分でやらなあかんのやないの？
- **>>157**: 今「animaとzitで遊ぶ」のが目的なら...素直にPortable版かstability matrixで入れるのが早い SageAttentionなんかもとりあえずはいらないからなんの工夫も必要ない、その辺工夫入れてるSimpleComfyUIのほうが変になるリスク高い（ComfyUI環境構築の推奨：Portable/Stability Matrixが簡単）。
- **>>163**: SimpleComfyUiIでインストールしたComfyUIを普通のComfyUIとして起動して使うにはどうしたらええんやろ？
- **>>164**: >>146やけど...ポータブル版かstability matrixで試してみるわ これまで使ってたsimplecomfyはSDXL用として取っておくンゴ。
- **>>165**: SimpleComfyUIの存在は無視する...ComfyUI公式から最新のComfyUIPortable版を持ってくる（ComfyUI公式Portable推奨）。
- **>>180**: SimpleComfyUiはアプデでおかしくなったからStabilityMatrixに移行したで sage attentionはStabilityMatrixの指示に従ってインストールできた（ComfyUI環境移行）。
- **>>181**: SimpleComfyUIフォルダにある「ComfyUIフォルダ」はComfyUIのgitからclone/pullしただけのものだからComfyUIを手動インストールしたのと同じ状態 （Portable ComfyUIは別の要素もあるので別物）（ComfyUI起動方法）。
- **>>184**: comfyUIは色んな導入方法と環境あるから同じアプデ入れてもおま環の不具合出ることしばしばあるからな ぶっちゃけノード操作なんかよりこれが一番のハードルやろ（ComfyUIの環境依存性が高い理由）。
- **>>186**: もう数ヶ月ぐらいmatrixで作ったportable環境で更新ボタン見かける毎に即押すノーガード運用してるけど問題無いわ（Stability Matrix + Portable ComfyUIの安定運用理由）。
- **>>207**: >>146 animaもzitもQIEも simpleComfyUIで何一つ困ってないで（SimpleComfyUIで問題なし）。
- **>>215**: 昨日SimpleComfyUiのバージョンアップでAnimaが動かんかったから StabilityMatrixを導入したで ...最新バージョンはStabilityMatrixを軸にすることにしたわ（SimpleComfyUIの不安定さからStability Matrix移行理由：Git/Python不要で楽）。
- **>>226**: ワイはsimple comfyUIをmanagerでアプデしたら branch切り替わって動かなくなったから git checkout master でマスターブランチに戻した後 git pullでアプデして venv/Scripts/activate pip install -r requirements.txt 実行で復活したで（ComfyUI復旧手順）。
- **>>227**: ここ連日アプデしてるな やはりAce Step関連が多い（ComfyUIの頻繁な更新）。

**ComfyUI選ばれている理由の抽出**:
- 公式Portable版/Stability Matrixが初心者向けで簡単・安定（>>150, >>152, >>157, >>164, >>165, >>186, >>215）。
- SimpleComfyUIは余計な工夫でリスク高く、公式/Portableが無難（>>147, >>152, >>155, >>157, >>181）。
- 環境依存性が高くおま環多発が最大ハードル（>>184）。
- カスタムノードインストールが柔軟（git/pip/custom_nodes）だが初心者苦戦（>>23, >>44-48, >>52, >>55）。

#### LM-Studio 関連
- **>>24**: LM-Studio (Text Gen) ノードでqwen3-vl-32b-instruct-hereticとかに渡して... LM Studio (Image to Text)でベースを作ることの方が多い（ComfyUI内ノードとしてプロンプト生成/画像toテキスト用）。

#### nano-banana 関連
- **>>26**: 前スレでnanobanana proがおかしいって言ってた人いたけど うちも変だったわ 過去の生成物が表示されなかった。
- **>>85**: うちのbananaは言語モデルですぅ出せませんってすぐ拗ねる（出力制限の挙動）。

#### A1111 関連
- **>>156**: A1111で生成した画像用やからcomfyUIで生成した画像への適用は ChatGPTちゃんなりに頼んで好きに改造してクレメンス（タグ分類ツールがA1111生成画像向け）。

#### AceMusic / Ace-Step 関連（ComfyUIカスタムノード）
- **>>40,44,47,48,52,55,61,65,67,68,71,76,82**: インストール苦戦/依存ライブラリ問題/v1 vs 1.5モデル自動DL挙動/コード修正提案/venv依存（古いpeft/transformers要求）。ブログ参照で1.5対応確認も仕様上v1固定。
- **>>88**: ACE-StepはComfyでやらんでも公式のgit cloneでええとおもうけどな。 ACE-Step UI という使いやすいUIもある（ComfyUI外UI推奨）。
- **>>166**: Ace-stepってturbo,sft,baseの順に性能が良くなっていくみたいだけど、プロンプトを突き詰めていかない限りturboの方が良い物できそう（turboが手軽）。
- **>>167**: 最後のACE-Step V1.5作業用BGM上げるファイル間違ってた。
- **>>185**: ACE-Step1.5にも対応してくれたんやね 相変わらず更新履歴が一年前やけど。

#### Stability Matrix 関連
- **>>154**: 今後サポートも見込めない物を素人が使う意味はないわな 大人しくワイのような赤達ちゃんはStabilityMatrixで管理するのが楽やで（初心者向け管理ツールとして楽）。
- **>>157,164,180,186,215**: Portable環境作成/更新簡単/ sage attention自動インストール（ComfyUI管理に最適）。

#### diffusion-pipe 関連
- **>>183**: AnimaのLora学習ってdiffusion-pipeじゃないとできんのか しんどいな（LoRA学習ツールとして使用、難易度高）。
- **>>189**: animaのLoRA学習 ちな学習率はSDXL感覚で行くとぶっ壊れる...肌感覚的には1/10にするのが安全（学習設定アドバイス）。
- **>>199**: diffusion-pipeあれやねepoch毎のsampling機能ないのがキツイわね サンプル出力見て人力early-stoppingができない（欠点：early stopping不可）。

#### その他のツール
- **>>88**: ACE-Step UI という使いやすいUIもある（Ace-Step専用UI）。
- **>>92,94**: photoshopに参照画像AI生成機能ついてたわ firefly限定だったわ ...フォトショで使うにしてもNAIのインペイント法の要領で置き換えてほしい物を指定すればええだけやしな。フォトショbananaはCNのような使い方もできる（Firefly限定AI機能、インペイント/CN代替）。
- **>>111,115,117,118,119,123,140,141,155,180**: xformers（RTX5000シリーズ対応版pip/venvインストール、SDPAより質向上？ Sage attention/pytorch attention代替推奨）。
- **>>211**: AnimaのLora学習ってdiffusion-pipeじゃないとできんのか ...はよKohyaでもできるようにならんかな WSLとかややこしくてよくわからんのよな（sd-scripts/Kohyaを代替希望、WSL複雑）。
- **>>226**: managerでアプデ（ComfyUI Manager言及）。 

**全体の傾向**: ComfyUIが圧倒的に中心で、環境構築/カスタムノードインストールのトラブル多発。初心者向けにStability Matrix/Portable公式版推奨理由が明確（楽・安定・自動更新）。AceMusic系ノードの依存問題が頻出。