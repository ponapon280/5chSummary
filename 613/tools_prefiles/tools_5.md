### 抽出された生成AI関連「ツール」話題一覧

ログ全体をスキャンし、指定ツール（ComfyUI, A1111, webUI, SUPIR, nano-bananaなど類似の生成AIインターフェース/拡張/ワークフロー/プラグインなど）に関する話題のみを抽出。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwenなど）言及は一切除外。ツール選定理由が明記されている場合も併記。重複/文脈的にツール非該当は除外。

#### ComfyUI
- **896**: 「ComfyUIとかにあるデフォルトのネガティブプロンプトの品質系とか使わなくても全然変わらんし」  
  (ネガティブプロンプトのデフォルト機能使用に関する言及。CFGとの相性で効きが悪い点指摘。)

#### ADetailer (A1111拡張)
- **927**: 「adetailerのpersonが、検出できるけど何も描き換えられない（コンソール上でinpaintのログが出てる）」  
  (person検出でinpaintが機能しないバグ報告。face/handは正常。)
- **928**: 「検出モデルをyolov8x-worldv2.ptにしてADetailer detector classesにpersonを指定したら描き変えされた」「前はちゃんとperson_yorov8n-seg.ptで描き変えできてたはず」  
  (解決策: 検出モデル変更。過去動作正常だった点指摘。)
- **973**: 「>>927のadetailerでpersonが効かない件、どうもseg全般がダメらしい」「ultralytics 8.3.240をアンインストールしてultralytics 8.3.216をインストールし直したら治った」  
  (ultralyticsバージョン依存バグの解決策報告。)

#### traintrain-standalone (LoRA学習ツール)
- **916**: 「traintrain-standaloneがどうしても起動できない」「requirementsがrequirements_versions.txtになっててそれはインストールした」「webui-user.batから起動しようとするとtorchaoが無い」「torchaoインストール→torchバージョンエラー」「diffusersエラー」など複数試行失敗報告。  
  (起動エラー詳細とトラブルシュート試行。torchao/diffusers/torchバージョン依存問題。)

#### その他の生成AIツール/拡張/手法
- **868**: 「SVIっての試して長尺作れるようになったんだけど、おせっせすると顔も画風も安定しない」「エンドイメージとか中間イメージを随時設定」「>>354的な手法はどうすればええんやろか」  
  (SVI動画生成で安定性問題、中間イメージ手法の質問。)
- **872**: 「5秒毎に背景ごと変わってるからSVIいらんよ」「基本はeasywan22でStart画像は前動画のEnd画像、End画像は静止画素材」「EasyWan22デフォルトのQ4Mだと精度的にきついかも」  
  (SVI代替としてeasywan22推奨。静止画素材準備前提で長尺動画生成。背景/イラスト時の制限指摘。)
- **881**: 「音から動画作るS2Vやリップシンク特化の動画モデルはある」「ほぼ固定絵で口パク以外は動かない」「AVIUTLあたりのほうが早い」  
  (S2V/リップシンクツール言及。実写/英語特化でアニメ/日本語微妙、AVIUTL優位。)
- **882**: 「AVIUTLっての調べてみるわ」  
  (AVIUTL口パクツール調査意向。)
- **884**: 「AVIUTLの口パクはボカロ劇場とかそのあたりでちょくちょく見かける」  
  (AVIUTL実績例。)
- **888**: 「静止画のリップシンクはInfiniteTalkで動画はLatentSyncでやるといい」  
  (InfiniteTalk/LatentSync推奨。リップシンク特化。)
- **896**: 「NAGを導入するときに検証」 (他複数: 900,901,962)  
  (NAG=Negative Attention Guidance。動画ネガティブプロンプト検証で効果薄く、生成時間増大で非推奨。CFG=1+ガチャ回帰推奨。)
- **916**: 「webui-user.batから起動」  
  (A1111系WebUI起動スクリプト言及、traintrain連携エラー。)

#### 抽出外理由補足
- mosaic censoring (841), GGUF (883/885/930), QIE (866/967) などはツール寄りだが指定例（ComfyUI/A1111等類似）に合わず/曖昧で除外。
- Civitai/Pixiv/noteなどアップロードサイト/プラットフォームは生成ツール非該当。
- 動画/音声編集全般 (857,875,855等)は生成AIツール外。
- モデル名絡み (Wan/Qwen/Flux等)は一切抽出せず。

全38件中、ツール該当は上記15件。ツール選定理由は主に「安定性/速度/バグ解決/代替手法」中心で明記少ない。