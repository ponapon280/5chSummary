# 生成AI関連「ツール」話題抽出レポート

## ComfyUI (comfy)

- **FL2VAワークフローでの音声リファレンス適用**: comfyuiのFL2VAテンプレWFにrefmodを挟むことで、irodoriで作った音声をそのまま映像に出力できる。プロンプトでセリフを変更して喋らせるテストを実施（725）
- **ComfyKittinAttentionと--fast fp16_accumulationの競合**: 起動batに`--fast fp16_accumulation`を入れた状態でComfyKittinAttentionを有効にしてKrea2やQI2.1で生成すると、プロンプトガン無視になるバグが発生（814）
- **--fast fp16_accumulationの個別設定推奨**: 起動オプションは全体に影響するため、`fp16_accumulation`はKJ NodesのModel Patch Torch Settingsで個別に設定する方が安牌（824）

## AI Toolkit

- **Qwen2.1の画風LoRA作成における破綻**: AItoolkitでQwen2.1の画風LoRAを作成したが破綻絵しか出ない。強度を弱めると破綻しなくなるが画風再現できず、原因不明。Musubi tunerの対応を待つ予定（660）
- **VAEの代替利用**: VAEのバグ（#15416）に引っかかっていたため、遅めのAI ToolkitのVAEを使用中（756）

## Musubi tuner

- **Qwen2.1対応待ち**: AItoolkitでのLoRA作成が破綻するため、Musubi tunerあたりが対応するのを待つという状況（660）

## kohya

- **Qwen2.1対応の優先順位が低い**: kohyaのTwitterでQwen2.1対応の優先順位は下げめで、と書かれており、スレ上で絶望の声がある（661）

## Live2D

- **Live2Dの裏側の泥臭さ**: ゲーム作りでLive2Dに手を出したが、絵を無理やりぐにょぐにょ動かす泥臭い努力が必要。See-throughや自動機能を触ったが、まばたき1つ良い感じにやってくれない。大きい動作は動画生成してシームレスに再生した方が早いかもしれないが、動画は細部の不一致や透過編集の手間が問題になる（651）

## nanobanana (nano-banana)

- **Krea2＋QI2.1との比較**: krea2＋QI2.1の組み合わせでGPT-Image2.0とまでは言わないが、nanobananaはさすがに超えたというスレ上の評価（758）

## Krea2 / Krea2-turbo

- **QI2.1との接写比較**: QI2.1とKrea2-turboで同一プロンプトでの接写比較を実施。両方2.3mpで比較し、左がQI2.1／右がKrea2-turbo（707）
- **Krea2-turboの4mp非対応**: Krea2-turboが4mpに対応していないため、比較は2.3mpで実施（707）
- **QI2.1とKrea2の組み合わせ評価**: krea2＋QI2.1でnanobananaを超えたというスレ上の評価（758）
- **Krea2の用途**: おおまかなポーズや形はQIで整えて最終仕上げはfluxやkreaを使う流れが変わらないという見方（701）
- **AnimaのEditとの比較**: QIE2511は遅く、AnimaやKrea2を使ったEditでは元画像が微妙に変化して違和感が大きかったがQIE2.1は良い感じ（699）

## webUI

- ログ内にwebUIに関する直接的な言及なし

## その他ツール関連話題

### 環境・起動オプション

- **--fast fp16_accumulation**: 起動batに`--fast fp16_accumulation`を付けてvaeをint8にしたらデコード爆速になった。画質はfp16と見分けが付かない（747）。ただし環境によってはエラー吐いてpython落とせなくなりPC再起動するしかなくなる事例も（815）
- **nvfp4 vs INT8の比較**: NVFP4の計算エミュレーションの遅さ vs INT8の巨大なモデルをPCIe経由でRAMから持ってくる遅さの比較。4060程度の低VRAM環境では実際に動かして比較した方がよい（770）
- **nvfp4の印象**: LTX2で触った際「クッソ速いけど順当に劣化する」という感覚でアップデートできていない（773）

### minimax (動画生成ツールとしての言及)

- **minimaxH3のI2V/R2V使い分け**: mp3音声を参照させる方法と、参照画像から逸脱させずLive2Dアニメーション風に固定する方法について議論。ref2vaでmp3を参照、i2vaで元画像をそのまま動かすのが正しい用途（679, 680）
- **minimaxH3の最大尺**: H3なら15秒が公式の言う最大尺（742）
- **minimaxとQIの使い分け**: minimaxはめっちゃ強いがイラストの画風指定ではやや劣る。QIが洗練されれば良いが、現状はflux2 kleinの方が強い面があるというスレ上の評価（695）

### Vast（PC貸出）

- **推論で貸す用途**: vastでPCを貸出する用途があるが、好きなタイミングで計算資源を引き戻せない契約で、マルウェアの踏み台にされるリスクがあるため基本やめたほうが良い（783, 810）

### irodori（音声生成ツール）

- **FL2VAでの音声利用**: irodoriで作った音声をそのままcomfyuiのFL2VAワークフローで出力できている（725）

### Computer Use（ツール操作）

- **AstraでのComputer Use**: AstraでComputer Useを使って3Dモデリングをすると$20の枠が秒で使い切る（645）
- **opus5.5の動画制作**: opus5.5は画像生成や動画生成をせずに動画を作れる。各種ツールやソフトを動かして作っている（Computer Use）。文字とアイコンが動くアニメは直接ベクターデータで作っている可能性があるが、人物が出てくると酷い品質になる（834, 835, 840）

### ハードウェア関連（ツール動作環境）

- **RTX 6000 Ada 48GB**: civitaでワークフローを配布しているユーザーの検証環境がRTX 6000 Ada（VRAM 48GB）、システムRAM 128GB（706）
- **1.2MP・20秒動画のOOM**: 1.2MPで20秒動画作ろうとすると5090でもOOMが発生するという報告（731）
- **Mac mini M6**: メモリ32GBで購入しGemma4 31Bをローカル動作。応答に数分かかる（650）
- **RTX 5000向け2GB GDDR7生産終了**: Micronが2GB GDDR7を生産終了、供給元が再び2社に減少（794）

---

**注**: モデル（NovelAI, illustrious, FLUX, Wan, Qwen-Image, anima, Z-Image, LTX）に関する話題は除外指定に従い抽出していません。ただし、Qwenシリーズの画像生成以外の話題およびツール動作環境としての言及は含めています。