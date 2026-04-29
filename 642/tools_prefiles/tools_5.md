### 抽出された「ツール」に関する話題

ログから生成AI関連の**ツール**（ComfyUI, webUI系, Krita, Detailer系ノードなど）のみを抽出。モデル（リアス, anima, NAI, Wanなど）の話題は除外。ツールの選択理由や利点が言及されたものは強調。

#### ComfyUI関連
- **852**: ComfyUIで同じ場所にあるノードをワンクリックで表示切り替える方法を質問（Couple系ノードが場所を取るので非表示にしたい）。Claudeに聞いたが標準機能なしと回答され、画面スペース不足を悩む。
- **861**: >>852に対し、「そんな時の為のサブグラフ」を提案。
- **864**: comfyuiのdetailerを推奨。小さいもの（乳首など）に使う時はcrop factorを34に設定。理由: crop factorを大きくすると切り抜き範囲が広がり、プロンプトが曖昧でも推測しやすくなる。
- **952**: animaやるならcomfyにしたほうがええで（理由明記なし）。
- **953**: AnimaはcomfyUI以外選択肢事実上ない。NVIDIA Driver 566.36ではNeo使えない（安定版を求める）。
- **959**: kritaのグラフモードからworkflow読み込んでAnima対応。inpainting用にkritaのキャンバスをinput/outputするworkflowを紹介（メタ情報は消える）。
- **962**: Forge NeoにNVIDIA Driverのバージョン制約なし。ComfyUIのPortable版はtorch cu130で古いドライバ非対応の話あり（>>193参照）。
- **970**: comfyuiのポータブル版の仮想環境を1から作り直した（cu130/torch2.11.0を避けるため）。
- **975**: >>970に対し、portable版ではなくgit cloneで手動インストール推奨。開発者が新バージョンを親切に対応（テストはボランティアのため自己責任）。
- **977**: Wan2.2環境はVer上げで不具合が出やすいが、Anima用は基本ネイティブ+カスタムノードで済むので現推奨CU130が良い。
- **986**: wan2.2点滅再発時は以前のComfyUIバージョンに戻すか、最新を別環境で（ComfyUIバージョン表記が急進）。
- **990**: Krita/comfyUIの差はあまりない。
- **995**: Kritaライブ生成について、PyQtでKrita画面操作+ComfyUIのwebsocketノード使用（krita-ai-diffusion参照）。コード生成モデルでプログラム作成可能。

#### Detailer系ノード関連
- **846**: >>821に対し、マスク+アップスケール+再描画+ダウンスケールはDetailerがやっていること。
- **864**: adetailer/comfyuiのdetailerのパラメータ説明（上記参照）。
- **943**: facedetailerが上手くいかない（upscaleで別人化）。
- **948**: >>943に対し、Detailerを先に実行（upscale後だと不可）。Detailerは小さい顔を拡大描画→縮小貼り付け。大きい顔はLoRA差し替え可能設定あり。
- **958**: >>943に対し、DMD（latent upscale）使用で絵柄が変わる。Ultrasharpモデルupscale推奨。最後にdetailerかけるならupscale時の書き込みが無駄。

#### A1111系/webUI関連
- **951**: A1111系の方が綺麗に出る？（anima文脈）。
- **988**: A1111系はTORCH_COMMANDでtorchバージョン指定可能（dev:2.7.0+cu128）。reForge:2.9.0+cu128、Forge Neo:2.11.0+cu130。Stability Matrix使用で最新化（問題発生も）。

#### Krita関連
- **916**: krita使ってる人？ anima対応してないよね。
- **945**: >>916 kritaのpythonからwebsocketを使えばどんなworkflowでも対応。生成モデルでコード書ける。
- **950**: >>916 Krita開発陣は海外で実写メイン、安価対応怪しい。
- **959**: 上記ComfyUI内でKrita workflow紹介。
- **987**: KritaのライブモードでAnima使いたい（カスタムグラフでライブ生成？）。
- **989**: >>987 無理。
- **990**: Krita/comfyUI変わらん。
- **995**: 上記ComfyUI内でKrita詳細。

#### その他のツール/ノード
- **968**: Coupleノード使いにくいのでClaudeに頼んで自作すると良い。
- **972**: Couple/ConditioningSetMaskの内部動作不明、雰囲気で使用。
- **988**: Stability Matrixでインストールすると最新torch化（問題も）。
- **994**: お絵かきノード？（>>991への返信、具体名不明）。

#### ツール選択理由のまとめ（抽出文脈から）
- **ComfyUI**: Animaの事実上唯一選択肢（953）。A1111より優位（952）。カスタムノード/サブグラフで柔軟（861,968）。バージョン管理しやすく環境分離可能（977,986）。
- **Detailer系**: 顔/小部位修復に特化（846,864,948）。crop factor調整で精度向上。
- **Krita+ComfyUI連携**: websocket/Pythonでworkflow対応（945,959,995）。ライブ/inpaint可能だが手間。
- **手動インストール（git clone）**: portableより安定制御可能（975）。

これでログの全ツール話題を網羅。モデル単独話題（例: animaのsound effects, NAIの弱点）は除外。