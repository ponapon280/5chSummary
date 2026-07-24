# 🆕 新規トピック（前回からの差分）
### 生成AIモデルに関するレポート（2026年7月時点）
- Animaとillustriousが主力として活発に比較され、高解像度・安定性・タグ制御で支持を集める
- WanとLTXが動画生成で注目され、NovelAI v5はゲームチェンジャー候補として期待される
- Krea2が液体表現やリファイン用途で補完的に評価される

### モデル: Wan（Wan2.2 / WAN22系）
- ローカルNSFW動画生成で中程度の言及があり、LTXよりVRAM要件が緩やかで扱いやすい
- int8量子化による速度向上やSmoothmixなどの派生モデルが話題

### モデル: LTX（LTX-2.3 / ltx2.3）
- NSFW生成能力が高い一方、VRAM要求が非常に高く使用ハードルが高い
- Wanとの比較で二次元動画では劣るとの指摘あり

### モデル: NovelAI（NAI / NAIv5）
- エロ生成ツールとして規制耐性と安定性で評価され、v5で日本語対応・複数キャラ位置指定・漫画コマ生成が期待される
- Anima陳腐化の懸念も出ている

### モデル: その他のモデル
- Gemini/Grok/Claudeがテキスト用途で言及され、Grokは検閲緩さ、Claudeはコーディング信頼性で選ばれる

### モデル: Web検索による参考情報
- Wan2.2は2025〜2026年登場のtext/image-to-videoモデルで、NSFW対応Uncensored版がComfyUIで人気
- LTX-2.3は2026年3月リリースのDiTベース動画モデルで、ネイティブ4K/オーディオ対応
- NovelAIはV4.5が主力でV5は開発中、多キャラ対応や自然言語理解が強化される
- Krea 2は2026年5月リリースの美学重視画像モデルで、スタイル参照に強くオープンソース版も公開
- illustriousは公式情報が少なく、コミュニティ固有のファインチューニング/派生モデルとみられる

---
# 元の本文
**生成AIモデルに関するレポート（2026年7月時点）**

ログ抽出結果から、コミュニティ（主にローカル/ComfyUIベースのアニメ・NSFW生成スレッド）で最も活発に議論され、比較されているモデルは**Anima**と**illustrious（リアス/IL）**です。これらが「主力」として位置づけられ、高頻度で相互比較されています。次点で動画生成分野の**Wan（Wan2.2）**と**LTX（LTX-2.3）**、クラウド/日本語・NSFW用途の**NovelAI（特にNAIv5）**、そして除外対象外の文脈で**Krea2**が実用的評価を集めています。全体の傾向として、Animaが「高解像度・安定性・ControlNet相性」で勢いがあり、illustriousは「タグ制御（特に体型）」の強みで根強い支持を得ています。Wanは動画で優勢、NovelAI v5は「ゲームチェンジャー」候補として期待値が高いです。Krea2は液体表現やリファイン用途で補完的に人気です。

### Anima（Anima LLLite / Anima Edit / Anima V1系）
最も言及が多く、主力モデルとして扱われています。高解像度（1536×1536など）での一発生成が強く、hires.fixの必要性が低い点や、指の破綻・位置指定のしやすさ、ControlNet-LLLiteとの相性の良さが評価されています。服変更・編集用途（Denoising Strength=1推奨）や概念LoRAとの親和性も高く、「SDXL時代からの乗り換えで快適になった」という声が多数です。ネガティブプロンプトの効きにくさや性器表現の弱点（陶器のような質感など）も指摘されますが、全体的な使い勝手の良さから支持を集めています。[[1]](https://www.reddit.com/r/StableDiffusion/comments/1totumo/anima_can_edit_images_and_this_is_possible_in_two/)[[2]](https://hyper.ai/en/news/51501)

### illustrious（リアス / ill / IL）
Animaと並んで非常に多く言及され、直接比較されるモデルです。Danbooruタグの理解度が高く、特に胸サイズや体型制御が強い点、線が細く綺麗な作風が出やすい点が選ばれる理由です。Anima画風LoRA作成の元画像としても使われており、タグ制御の強さでAnima移行を検討しつつ継続するユーザーもいます。過去の主力モデルとしての位置づけが強く、Anima登場後もハイブリッド運用（anima＋illustrious）で不自由がないという意見が見られます。

### Wan（Wan2.2 / WAN22系）
ローカルNSFW動画・画像生成の代表格として中程度の言及があります。LTXよりVRAM要件が緩やか（32〜64GB程度）で扱いやすい点、int8量子化による速度向上（FP8→INT8で7%高速化など）が評価されています。二次元動画生成でLTXより優位という声が多く、Smoothmixやdasiwaなどの派生モデルも話題です。細部（舌と亀頭の区別など）の課題はありますが、実用性で支持されています。[[3]](https://www.reddit.com/r/comfyui/comments/1ow2ghw/wan_video_22_is_herethis_uncensored_model_is_a/)[[4]](https://www.youtube.com/watch?v=MSzZ_gThIUU)

### LTX（LTX-2.3 / ltx2.3）
NSFW生成能力が高いとされ、公式でエロモデル開発が進んでいる点が注目されますが、VRAM要求が非常に高い（96GB推奨という声も）ため使用ハードルが高く、実際の報告は少ないです。Wanとの比較で言及され、Distil版のaesthetic寄り評価やint8対応の利点が挙げられます。二次元動画ではWanに劣るという指摘もあります。[[5]](https://ltx.io/model/ltx-2-3)[[6]](https://fal.ai/models/fal-ai/ltx-2.3/image-to-video)

### NovelAI（NAI / NAIv5）
言及は比較的少ないものの、「エロ生成ツール」としてWAN/LTXと並んで名前が上がり、規制耐性（知名度の低さ）や安定性で評価されます。v5では日本語完全対応、複数キャラの位置指定（ドラッグ&ドロップ風）、漫画コマ生成機能、プロンプト追従性の高さが「ゲームチェンジャー」として期待されており、Anima陳腐化の懸念も出ています。修正用途やクラウド手軽さも強みです。[[7]](https://x.com/novelaiofficial/status/2072941162193879330)

### Krea2（Krea 2 / krea2_turboなど）
除外対象外の文脈で最も具体的に話題になるモデルです。エロ（特に触手・液体/ヌルヌル表現）が出しやすく、Prompt Weightとの相性、Anima出力のリファイン（低denoise）用途で選ばれています。自然言語理解度が高く、サブカル作品名・キャラ名の雰囲気再現が強い点や、量子化（INT4）によるVRAM12GB環境での実用性も評価されています。LoRA学習のハードルは高いものの、スタイル再現性で支持されています。[[8]](https://www.krea.ai/)[[9]](https://www.krea.ai/krea-2)

### その他のモデル
- **FLUX / Qwen-Image / Z-Image**: 言及は少なく、二次エロでの完成度でAnimaなどに劣るという位置づけ。Qwenは中国語プロンプトの強さや版権耐性が特徴的ですが、まだ発展途上。
- **Gemini / Grok / Claude**: テキスト/会話用途で言及され、Grokは検閲の緩さ（エロ用途）、Claudeはコーディング信頼性で選ばれる声あり。

**全体傾向**: Anima vs illustriousの比較が中心で、動画はWan優勢、クラウド/日本語はNovelAI v5への期待が高まっています。量子化（int8/INT4）やControlNet/LoRAの相性が実用選定の鍵となっています。

## Web検索による参考情報
- **Anima**: 2026年にCircleStone Labsからリリースされたアニメ特化の画像生成モデル（Anima V1）。ControlNet-LLLite（kohya-ssなど）との組み合わせで編集・姿勢制御に強い。ComfyUIワークフローで広く使われている。[[2]](https://hyper.ai/en/news/51501)[[10]](https://modelscope.ai/models/LaxharLAB/Anima_Tile_and_Repair_ControlNet-LLLite)
- **Wan2.2**: 2025〜2026年頃に登場したテキスト/画像-to-videoモデル。NSFW対応のUncensored版やRemixモデルがComfyUIで人気。int8量子化やVACEワークフローで低VRAM・長尺生成に対応。[[3]](https://www.reddit.com/r/comfyui/comments/1ow2ghw/wan_video_22_is_herethis_uncensored_model_is_a/)[[11]](https://www.nextdiffusion.ai/tutorials/create-uncensored-videos-with-wan22-remix-in-comfyui-t2v)
- **LTX-2.3**: Lightricks社が2026年3月頃にリリースした動画生成モデル。DiTベースで、VAE改善・プロンプト追従性向上・ネイティブ4K/オーディオ対応。Pro/Fast版あり。[[5]](https://ltx.io/model/ltx-2-3)[[12]](https://en.wikipedia.org/wiki/LTX_(text-to-video_model))
- **NovelAI**: Diffusion V4.5が最新の主力（V5は開発中/期待段階）。多キャラ対応、自然言語理解、アクションタグ強化。v5サンプルで内部/背景生成例が公開されている。[[13]](https://novelai.net/v4)
- **Krea 2**: Krea AIが2026年5月頃にリリースした美学重視の画像基盤モデル（RAW/Turbo版）。スタイル参照・ムードボードに強く、独立系T2Iモデルとして高評価。オープンソース版も公開。[[9]](https://www.krea.ai/krea-2)[[14]](https://github.com/krea-ai/krea-2)

illustriousについては具体的な公式情報が少なく、コミュニティ固有のファインチューニング/派生モデルとみられます。
