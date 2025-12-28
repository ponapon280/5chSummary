### 抽出されたツール関連話題

ログ全体をスキャンし、生成AI関連の「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR, nano-banana などのUI/ノード/ワークフロー/環境ツール）に関する話題のみを抽出。指定モデル（NAI, Pony, illustrious/イラストリアス/リアス/ill/IL, Noobai, FLUX, Wan, Qwen）に関する話題は除外。ツール選定理由が明記されている場合を強調。

#### ComfyUI (comfy) 関連
- **893**: 「自力comfy試してみたけどやっぱeasyから逃れられそうにない」  
  → ComfyUIを自力で試したが、Easy系ツールから移行しにくい。
- **923**: 「動画はPainterLongVideoがスタンダードになってきてるから過去Ver固定のEasyWanだと無理 SimpleComfyUIもアプデ周りがちょいと使いにくいし、自分で調べてComfyUI環境構築しようねルート」  
  → EasyWan/SimpleComfyUIの限界からComfyUI環境構築を推奨（アプデ対応の柔軟性）。
- **924**: 「浦島ニキは今やとComfyUI+ComfyUI-Managerとか入れればええんか？」  
  → ComfyUI + ComfyUI-Managerの導入を提案。
- **925**: 「せやな 一生赤ちゃん続けるつもりが無いならComfyUIも可能ならvenv版っていうのにした方がええで」  
  → ComfyUIのvenv版を推奨（長期利用の融通性）。
- **938**: 「comfyuiの環境を全部統合させるためにeasywan卒業したところやしWF公開してくれるのはありがたいンゴねぇ」  
  → EasyWan卒業してComfyUIへ移行（環境統合の利便性）。
- **943**: 「ワイネイティブのFLF2Vノードで十分じゃねと思ってたけどpainterも使って見たくなったわ」  
  → ComfyUIのPainter系ノード（PainterLongVideo）を試用。
- **949**: 「PainterLongVideoはinitial_reference_imageが機能してない気がする」  
  → ComfyUIのPainterLongVideoノードの機能指摘。
- **958**: 「ComfyUIはstability matrixで常にアップデートしているんですが venv版はちがう作業必要なんでしょうか？」  
  → ComfyUIのvenv版アップデート方法の相談。
- **960**: 「venvのPythonバージョンは12より上には上げられないよ」  
  → ComfyUI venv環境のPythonバージョン制限。
- **962**: 「一番簡単なのはComfyUI Managerから本体の更新かな」  
  → ComfyUI Managerを使った更新方法。
- **963**: 「venv&quot版&quotて、Stability MatrixでインストールしたComfyUIのvenvじゃなくて手動インストールのComfyUIのことか それくらいはComfyUI Managerを使う方法が公式Gitに書いてあるし」  
  → ComfyUI Managerの活用、手動インストール推奨。
- **964**: 「あまりおすすめされてるのを見たことがないポータブル版ComfyUI、そして完全に謎に包まれているデスクトップ版ComfyUI ワイもStabilityMatirx→自分でvenv環境の流れだけどさ」  
  → ComfyUIの各種版（ポータブル/デスクトップ/vnev）の比較。
- **965**: 「何だかんだローカル生成は敷居が高いね gitインストールの時点でかなり弾かれるから」  
  → ComfyUI導入時のgit必要性指摘。
- **966**: 「ワイのComfyUI遍歴はデスクトップ版→ポータブル版→Stability Matrix版→venv版 結局いろいろ融通が利くのはvenv環境なんよな 導入が一番面倒だけど･･･」  
  → ComfyUI venv版が融通利くため最終推奨（導入面倒だが最適）。
- **967**: 「forgecoupleみたいに、領域を指定して二人以上のキャラをかき分けるのを comfyuiでできるカスタムノードの紹介を過去スレのどこかで見た気がするんやが」  
  → ComfyUIカスタムノード（領域指定系）の相談。
- **972**: 「comfyuiデスクトップ版入れて2月ぐらい使ってるけど特に問題は感じないな」  
  → ComfyUIデスクトップ版の安定性。
- **973**: （画像？）ComfyUI関連ノード/WFの共有と思われる。
- **981**: 「Cond Pair Set Propsのことなら標準ノードなんで特にカスタムノード必要ないで WF全体は↑に梱包」  
  → ComfyUI標準ノード（Cond Pair Set Props）の活用。
- **982**: 「prompt-controlはSSSノードだよ これなしでスケジューリングは地獄」  
  → ComfyUIのprompt-control SSSノード必須（スケジューリング容易化）。
- **983**: 「毎度思うがこういう形式のcoupleはmaskの画像を自分で作らねばならんのか」  
  → ComfyUI coupleノードのmask作成必要性。
- **984**: 「公式Gitに書いてあるのはDesktop Application、Windows Portable Package、Manual Installの3つだけど、Stability MatrixはManual Install版をvenvにインストールしてくれてるよ」  
  → ComfyUIインストール方法の説明。
- **985**: （お礼、関連ノード共有）
- **986**: 「2領域だけならcomfycoupleが手軽やで」  
  → ComfyUIのcomfycoupleノードの手軽さ。
- **988**: 「ComfyUI_MiraのCreate Tilling PNG Maskを使えば数値入力だけで指定できる」  
  → ComfyUI_Miraノードのmask作成容易化。

#### EasyWan / EasyWan22 関連
- **851**: 「EasyWan22内の亀頭舐めってプリセットにあるpenis play LoRAってのをコピーして使ったら」  
  → EasyWan22のプリセット活用。
- **921**: 「>>740 >>868 とかはEasyWanですか？」  
  → EasyWanの使用確認。
- **935**: 「>>740のWFのスクショ貼っとくわ 動きが滑らかなのはhighにsmoothmixでlowにdasiwa入れたのとpainter系のノードのおかげやと思う」  
  → EasyWan系WFの共有（Painterノード併用）。
- **938**: 「easywan卒業したところ」  
  → EasyWan卒業（ComfyUIへ）。
- **941**: 「ワイもeasywan22卒業して爆速になったよ 起動だけ」  
  → EasyWan22卒業で起動高速化（ComfyUIへ）。

#### EasyReforge 関連
- **893**: 「easyから逃れられそうにない」  
  → Easy系（EasyReforge含む？）。
- **908**: 「ワイもEasyReforgeつこてるけど便利機能がComfyUI側でどんどん増えとるからなぁ」  
  → EasyReforge使用中だがComfyUIの機能増加を指摘。
- **929**: 「知り合いが画像生成始めたからeasyreforge勧めたんだけど、起動が上手くいかないみたい。新規環境インストールしていよいよ！って思ったら1～4の項目？が出てhuggingfaceへのサインイン？みたいなのを求められる。」  
  → EasyReforgeの新規インストール/起動トラブル相談。
- **939**: 「EasyReforgeのGit Issueに書いてあるけどZuntanニキが忙しいのか未対応なんよ」  
  → EasyReforgeのGit Issue未対応。
- **940**: 「前スレでも書き込みあったけど今EasyReforgeは新規インストールでエラーが出るんよな」  
  → EasyReforge新規インストールエラー。
- **942**: 「としあきwikiのEasyReforgeページに具体的な対応手順を書いてあるから読めば分かると思う」  
  → EasyReforge修正手順（としあきwiki）。
- **944**: 「5000番台のグラボ使ってるんよね、としあきwiki見てリトライします」  
  → EasyReforge wiki対応。
- **955**: 「としあきに修正方法書いてくれて助かったわ」  
  → EasyReforge修正完了。

#### nano-banana 関連
- **894**: 「今年はWan2.2の動画生成と、nanobananaなどの画像編集の年だったなー」  
  → nano-bananaを画像編集ツールとして言及（今年のトレンド）。

#### Stability Matrix 関連
- **928**: 「StabilityMatrixからインストールしたら楽だよ」  
  → ComfyUIインストールの容易さ。
- **958**: 「ComfyUIはstability matrixで常にアップデートしている」  
  → Stability MatrixでComfyUI管理。
- **964**: 「StabilityMatirx→自分でvenv環境」  
  → Stability Matrix使用歴。
- **966**: 「Stability Matrix版」  
  → ComfyUI Stability Matrix版。
- **970**: 「Stability Matrixをやめてcomfyuiの個別インストールが必要なのか」  
  → Stability Matrixからの移行相談。
- **984**: 「Stability MatrixはManual Install版をvenvにインストールしてくれてるよ」  
  → Stability Matrixのvenv対応。

#### その他ツール/ノード
- **967**: 「forgecoupleみたいに」  
  → forgecouple（領域指定ツール、ComfyUI代替相談）。
- **968**: 「リージョナルプロンプターのことかな？」  
  → Regional Prompter（ComfyUIカスタムノード）。
- **981**: 「comfycouple」  
  → comfycouple（ComfyUIノード）。
- **988**: 「ComfyUI_MiraのCreate Tilling PNG Mask」  
  → ComfyUI_Miraノード。

これで全ツール関連話題を網羅。モデル（DaSiWa, Smoothmix, PainterLongVideoのモデル部分など）は除外。理由明記のものは太字強調。