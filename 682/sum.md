# 🆕 新規トピック（前回からの差分）
### モデル比較・移行傾向
- ref2vaは参照機能に強く、fl2vaはt2vの安定性・画質で優勢。ハイブリッド運用も増加。
- LTX 2.5比でH3が画質・音声・エロ・動きで優位、LTXは速度で圧倒的。「H3最低ライン」「速度LTX、品質H3」の棲み分け。
- Sora2は過去の技術、中国製モデルの規制耐性・実用性が評価。

### 高速化・最適化
- Turbo LoRA（8step）の活用が定着。
- Sage Attentionで大幅高速化、特にH3。新たにComfy Kitchen Attention（CK Attn）が登場し導入しやすく注目。
- ノード接続順で速度が変わる、INT8 ConvRotでVRAM節約、VAE Decode Audio切断、`ref_image_size=max`回避、キャッシュ整理でストレージ節約。
- 0.5MPで数分〜10分台生成。解像度・尺増加で急激に重くなる。

### 音声・参照制御の課題と対策
- 音声の不満：周辺モブのホラー化、余計なSE混入、音量の大きさ。
- 対策：プロンプト末尾に`non_diegetic_music: N/A`、VAE Decode Audio切断、リップシンクノード活用。
- 複数参照（立ち絵→動作→性行為）が主流。段階的生成やマスクで制御、貧乳・巨乳制御は難易度高め。
- Context Loopは長尺で自然だが画質劣化・繋ぎ目不明瞭。Review Gateでscene別seedガチャ可能。

### ハードウェア・環境
- VRAM 12〜16GBでH3動作可能だが余裕なし。16GBでも480pが実用的。
- RAM 64GB以上推奨。RAMディスク活用も。
- 高スペック比較、ストレージ対策、大型LLMとの競合。低スペックでも「まだ遅い」声。

### ワークフロー・その他
- ComfyUI更新：バージョン戻り、OOM対策、新ノード（Spectrum Apply、Model Preview Override）検証。
- NSFW話題：フェラLoRA、セリフガチャ、キャラ参照エロ動画共有多いが自粛意識高まる。

### コミュニティの空気感・傾向
- 中毒性高く「沼」「時間溶ける」声。一方開発者依存の脆弱さも。
- 情報交換活発だが規制意識向上で画像貼り減少。

### 総評
- H3登場でローカル動画生成の最低ラインが引き上がった。現在はref2va/fl2va併用、Attention、音声制御、長尺化を軸に試行錯誤中。

### Web検索による参考情報
- LTX 2.5: Lightricks製高速動画モデル、ComfyUI統合、速度重視。
- ComfyUI Attentionバックエンド: Sage Attentionが速度向上に使用、CK Attnは新バックエンドで導入しやすくSageと併用不可の場合多し。

---
# 元の本文
**なんJ（5ch） AI動画生成スレッド 統合レポート**

### 概要
このスレッド群は、主にComfyUI環境でのローカルAI動画生成（特にエロ動画含む）をテーマとした技術共有・実践議論の場です。中心は**MiniMax H3（H3 / fl2va / ref2va）**の登場によるモデル移行とワークフロー最適化で、「大動画時代」と呼ばれる活況の中で、生成速度・画質・音声のバランスを追求する声が多数を占めます。Wan2.1時代からの移行組が多く、H3の性能向上により旧モデル（Wan2.2/2.3、LTX2.3など）の断捨離が進んでいます。全体として実用的な情報交換が活発で、技術的深掘りとハードウェア最適化が主な焦点です。

### 主要トピック

**1. モデル比較・移行傾向**
- **主流構成**：MiniMax H3（fl2va/ref2va）を軸に、Rias + Anima + Krea2の3〜4モデル体制へ移行する人が多数。Wanシリーズ、LTX2.3、Pony、Illustriousなどは容量の観点からほぼ全消しされるケースが多い。
- ref2vaは参照機能（画像・音声）に強く、fl2vaはt2v単体での安定性・画質で優勢という意見が主流。ハイブリッド運用（ref2vaワークフロー内でfl2vaモデル使用）も広がっています。
- LTX 2.5との比較では、H3が画質・日本語音声・エロ表現・動きの理解度で優位。一方LTXは速度で圧倒的（H3の数十倍クラス）だが、崩れやすさやエロの弱さが指摘されます。「H3が現時点の最低ライン」「速度はLTX、品質はH3」の棲み分けが定着しつつあります。
- その他：Sora2は既に「過去の技術」との見方が強く、中国製モデルの規制耐性・実用性が評価されています。

**2. 高速化・最適化**
- Turbo LoRA（8stepなど）の活用が定着。8step LoRA追加の評価も。
- Attentionバックエンド：Sage Attention導入で大幅高速化報告多数（特にH3）。新たに**Comfy Kitchen Attention（CK Attn）**が登場し、導入のしやすさ（`--use-ck-attention`フラグや専用ノード）と品質向上の可能性で注目。Sageと同等〜やや劣る速度だが、古いGPUでは価値が高い。
- その他のTips：高速化ノードの接続順で速度が倍近く変わる事例、INT8 ConvRotによるVRAM節約、VAE Decode Audioの切断、`ref_image_size=max`の回避（match推奨）、`pip cache purge` + `uv cache clean`によるストレージ整理。
- 生成時間例：0.5MPで数分〜10分台。解像度・尺の増加で急激に重くなる。

**3. 音声・参照制御の課題と対策**
- 音声の主な不満：周辺モブのホラー化、余計なSEの混入、全体的な音量の大きさ。
- 対策：プロンプト末尾に `non_diegetic_music: N/A`、VAE Decode Audio切断、リップシンクノードの活用。
- 参照画像：複数参照（立ち絵→動作→性行為の流れ）の組み合わせが主流。透けブラ/脱衣の段階的生成（全裸→ブラ→ワイシャツ）やマスク処理で制御。貧乳・巨乳制御は依然として難易度高め。
- Context Loop（H3の目玉機能）：長尺化でMotion Contextより自然だが、画質劣化や繋ぎ目の不明瞭さが指摘。Review Gateノードでscene別seedガチャが可能。

**4. ハードウェア・環境**
- VRAM：12〜16GB（3060Ti/4070など）でH3は動作可能だが余裕なし。16GBでも480p程度が実用的。
- RAM：64GB以上が強く推奨（32GBでは厳しい報告多数）。RAMディスク活用も話題。
- その他：RTX 5090やDGX Sparkなどの高スペック比較、ストレージ対策、大型LLMとの容量競合。低スペック勢でも「まだ遅い」との声あり。

**5. ワークフロー・その他**
- H3 context loopの実用化、LoRA学習（MiniMaxで静止画量産→Anima LoRA作成）、リップシンクのref差し替え手法が活発。
- ComfyUI更新関連：バージョン戻り現象やOOM対策、新ノード（Spectrum Apply、Model Preview Overrideなど）の検証。
- NSFW寄りの話題：フェラLoRA、セリフガチャ、キャラ参照エロ動画の共有が多いが、自粛意識も高まっています。

### コミュニティの空気感・傾向
- 中毒性が高く、「沼」「時間溶ける」といった声が目立つ一方、kijai氏活動停止への反応など開発者依存の脆弱さも感じられます。
- 情報交換は活発だが、規制意識向上で画像貼りが減少傾向。
- 将来展望：H3 turboモデルやFlux3登場によるさらなる流動化、速度 vs 品質の棲み分け定着、メモリ/VRAM価格高騰の長期課題。

### 総評
H3の登場により「ローカル動画生成の最低ライン」が一気に引き上がったスレッド群です。現在はref2va/fl2va併用、Kitchen/Sage Attention、音声制御、長尺化（Context Loop）を軸とした実用ワークフロー構築段階。まだ完成形ではなく、試行錯誤が続いています。技術的深さとハードウェア最適化のバランスが特徴で、今後も新モデルリリースごとに同様の議論が続きそうです。

## Web検索による参考情報
- **MiniMax H3（H3）**: Hailuo AI / MiniMaxのオープンウェイト動画生成モデル（2026年頃リリース）。ComfyUIネイティブ対応でT2V/I2V/R2V（ref2va）、ネイティブステレオ音声生成が可能。最大2K解像度、5〜15秒程度の生成。Hugging FaceのComfy-Org/MiniMax-H3リポジトリでモデル提供。[[1]](https://www.youtube.com/watch?v=d_wEd-fZcdg)[[2]](https://comfy.org/minimax/)[[3]](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- **LTX 2.5**: LTX（Lightricks）製のオープンウェイト動画モデル。高速生成（例: 10秒動画を数秒で）が特徴でComfyUI統合。H3と比較して速度重視。[[4]](https://ltx.io/)[[5]](https://venturebeat.com/technology/ltx-2-5-can-generate-a-10-second-ai-video-from-an-image-in-just-6-8-seconds-on-nvidia-superchips-and-its-open-weights)
- **Wan2.1**: Alibaba系Wan-Videoのオープン動画モデル。中国語・英語テキスト生成対応、T2V/I2Vタスクで高性能。軽量版もあり。[[6]](https://github.com/Wan-Video/Wan2.1)[[7]](https://docs.comfy.org/tutorials/video/wan/wan-video)
- **ComfyUI Attentionバックエンド**: Sage AttentionはH3などで速度向上に広く使われる。Comfy Kitchen Attention（CK Attn）は最近マージされた新バックエンドで、導入しやすく品質向上の可能性あり（Sageと併用不可の場合が多い）。[[8]](https://www.reddit.com/r/StableDiffusion/comments/1vl8wqw/comfyui_comfykitchen_attention_speed_up/)

（その他Rias/Anima/Krea2などはコミュニティ特化のファインチューン/LoRAと推定され、公式情報は限定的。）
