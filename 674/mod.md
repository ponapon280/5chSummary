# 🆕 新規トピック（前回からの差分）
### レポート冒頭まとめ（流行しているモデルの推測）
- NovelAI（特にNAIv5）が圧倒的人気で日常使い・日本語対応・エロ表現力で支持を集める
- ローカルではAnima＋Illustriousの役割分担ワークフローが定着
- 動画生成ではWanが主力でKrea2とMiniMax H3が注目

### NovelAI（NAI / NAIv4 / NAIv5 / NAI5）
- 手軽さ・サブスク利便性が高くスマホ生成から投稿まで簡単
- 日本語プロンプトの自然さ・セリフ・背景・位置指定で優位
- エロ表現力・NSFW性能が高くローカルでは難しい領域をカバー
- キャラクター再現性が高くマイナーキャラや新規キャラにも強い
- マンガ生成や台詞連動の表情変化が豊富
- NAIv5はテスター画像で高評価「ローカルを抜き去った」との声あり

### Anima
- NAIに近いDanbooruタグ＋自然文のプロンプト制御が可能

### Wan（Wan2.2 / Wan2.7など）
- 動画生成（i2v）で現在最も使われておりHigh/Lowモデル分担が特徴
- 既存LoRA資産の蓄積と複雑な動き・物理表現への対応力
- MiniMax H3登場で陳腐化の可能性が指摘されている

### Krea2（Krea 2）
- 背景・装飾品の情報量が高くローカルでは追いつけない領域
- 3DCG風・ゲーム系生成やLoRA作成ベースとしての相性が良い
- 長文プロンプト理解力や尖った要求への対応力が高い
- エロ表現はまだ弱くSFW寄りとの指摘あり

### MiniMax H3（H3 / Hailuo 3.0）
- 次世代オープンウェイト動画モデルとして性能が高くWan2.2上回る可能性
- オープンウェイト＋緩いライセンスでローカル運用・商用利用しやすい
- マルチモーダル対応でテキスト・画像・動画・音声の統一コンテキストを実現
- WanやSeedanceの後継候補として「ゲームチェンジャー」と期待

### その他のモデル
- LTX（LTX-2.3）は動作の重さで敬遠され言及が少ない
- Gemma4 / Grokはエロプロンプト作成ツールや代替クラウドとしてニッチに言及
- Bernini-R / Seedanceは動画編集用途で散発的に言及

### ## Web検索による参考情報
- NovelAIはAnlatan社運営のクラウドサービスで日本語・NSFW強みが特徴
- IllustriousはSDXLベースのアニメ特化ローカルモデルで高解像度・キャラ精度に優れる
- Wan2.2はAlibaba製オープンソース動画モデルでHigh/Lowノイズ専門家分離が特徴
- Krea2はKrea.aiの独自モデルでリアルタイム生成・背景詳細に強い
- MiniMax H3はMiniMax製オープンウェイトマルチモーダル動画モデルで2K・音声同期対応

---
# 元の本文
**レポート冒頭まとめ（流行しているモデルの推測）**  
テキスト全体から、**NovelAI（特にNAIv5/NAI5）**が圧倒的に話題の中心で最も流行している。日常使い・手軽さ・日本語対応・エロ表現力・キャラクター再現性で支持が厚く、「NAIさえあればいい」「ローカルと併用しつつ一番好き」という声が多数。次にローカル勢では**Anima＋Illustrious（リアス/ill/IL）**の役割分担ワークフロー（構図→仕上げ）が定着。動画生成では**Wan（Wan2.2など）**が現在主力で、**Krea2**（クラウド、特に背景・LoRA作成用途）と**MiniMax H3**（次世代オープンウェイト動画モデルとしての期待）が注目を集めている。全体の傾向として「エロ（特に二次元NSFW）」と「日本語/プロンプト制御」「手軽さ vs ローカル制御」の軸で評価されており、NAIがクラウド勢の代表、Anima/Illustriousがローカル上級者向けの完成形として語られることが多い。[[1]](https://www.reddit.com/r/NovelAi/)[[2]](https://x.com/novelaiofficial?lang=en)

**NovelAI（NAI / NAIv4 / NAIv5 / NAI5）**  
最も言及が多く、ログのメイン話題。選ばれている主な理由は以下の通り：  
- 手軽さ・サブスクの利便性（スマホで生成→pixiv投稿が簡単、高プラン一時契約で大量生成後解約）。  
- 日本語プロンプトの強さ（自然なセリフ・吹き出し・オノマトペ対応、背景の強さ、キャラクター位置指定のしやすさ）。  
- エロ表現力・NSFW性能の高さ（ローカルでは難しい領域）。  
- キャラクター再現性（マイナーキャラや新規キャラの精度が高い、Danbooruタグ＋自然文の両対応）。  
- マンガ生成や表情の豊かさ（台詞に連動した表情変化）。  
NAIv5はテスター画像で高評価が出ており、「ローカルを抜き去った」「NAI3以来のワクワク」との声あり。一方でメタデータ漏洩対策（JPG変換など）も話題に。ローカル勢との併用が一般的で、「PCスペックを問わず高品質」な点が強み。[[3]](https://novelai.net/updates)[[4]](https://blog.novelai.net/release-novelai-anime-diffusion-v4-curated-preview-en-ca4b0b11e671)

**Illustrious（リアス / ill / IL / Illustrious XL）**  
Animaとの併用が主流。「構図はAnima、仕上げはリアス」という役割分担が定着。選ばれている理由：  
- タグ入力との相性の良さ（1girlなどの普通の構図で破綻しにくい）。  
- エロ表現の完成度・絵柄の安定感。  
- v4時点でのイラスト完成度が高く、「v4-リアス時代でイラストは完結」という評価。  
単独よりAnimaとの組み合わせで語られることが多い。[[5]](https://www.reddit.com/r/StableDiffusion/comments/1gk6jtr/a_new_model_illustrious/)[[6]](https://morphic.com/tr/ai-glossary/Illustrious)

**Anima**  
構図・レイアウトの安定性で高評価。特に変構図や複雑な要求への対応力。選ばれている理由：  
- ベースモデルの完成度が高く、派生モデルの必要性が低い。  
- NAIに近いプロンプト制御（Danbooruタグ＋自然文）が可能になった点。  
- ComfyUIでのbatch生成の扱いやすさ。  
ただし英語プロンプトの理解力や影・光の暴れやすさが指摘され、単独ではなくIllustriousとの併用が前提。krea2のLoRA作成元としても言及あり。[[7]](https://www.reddit.com/r/StableDiffusion/comments/1qsf3lb/some_images_with_anima_using_feafult_workflow_on/)[[8]](https://huggingface.co/circlestone-labs/Anima)

**Wan（Wan2.2 / Wan2.7など）**  
動画生成（特にi2v）で現在最も使われているモデル。High/Lowモデルの役割分担（Highで大まかな動き、Lowで仕上げ）が話題。選ばれている理由：  
- 既存LoRA資産の蓄積（乗り換えにくい要因にも）。  
- 複雑な動きや物理表現（例: ゼリーの揺れ）への対応力。  
ただしMiniMax H3登場で陳腐化の可能性が指摘されている。[[9]](https://github.com/Wan-Video/Wan2.2)[[10]](https://wan22.io/)

**Krea2（Krea 2）**  
クラウドモデルとして「最も勢いがある」とワークショップテーマになるほど言及多め。選ばれている理由：  
- 背景・装飾品の細かさ・情報量の高さ（ローカルでは追いつけない領域）。  
- 3DCG風・ゲーム系生成やLoRA作成のベースとしての相性。  
- 長文プロンプト理解力や尖った要求への対応力。  
エロ表現はまだ弱いという指摘あり（SFW寄り）。[[11]](https://www.krea.ai/)

**MiniMax H3（H3 / Hailuo 3.0）**  
次世代オープンウェイト動画モデルとして期待値が高い。選ばれている/期待されている理由：  
- 性能の高さ（特に2Dアニメ調、Wan2.2上回る可能性）。  
- オープンウェイト＋比較的緩いライセンス（ローカル運用しやすく商用利用も可）。  
- マルチモーダル対応（テキスト・画像・動画・音声の統一コンテキスト、ネイティブ音声付き2K動画）。  
WanやSeedanceの後継候補として「ゲームチェンジャー」との声多数。[[12]](https://www.minimax.io/blog/minimax-h3)[[13]](https://fal.ai/minimax-h3)

**その他のモデル**  
- **LTX（LTX-2.3）**：動作の重さがネックで敬遠されやすく、言及少ない。  
- **FLUX / Qwen-Image / Z-Image**：ほぼ言及なし（2次元エロでは弱いという文脈のみ）。  
- **Gemma4 / Grok**：エロプロンプト作成ツールや代替クラウドとしてニッチに言及。  
- **Bernini-R / Seedance**：動画編集用途で散発的。  
全体として、除外対象外のモデルはKrea2やMiniMax H3が相対的に目立つが、話題の中心はNAIとAnima/Illustrious/Wanに集中。

**## Web検索による参考情報**  
- **NovelAI**: Anlatan社運営のクラウドサービス。画像生成はDanbooru系データセットで訓練された独自Diffusionモデル。V4.5が2025年にリリースされ、V5は2026年時点でテスター画像や新機能（キャラクター参照など）が話題。日本語対応やNSFWの強みが特徴。[[1]](https://www.reddit.com/r/NovelAi/)[[14]](https://blog.novelai.net/novelai-diffusion-v4-5-full-release-678318c86205)  
- **Illustrious (Illustrious XL)**: OnomaAI Researchなどによるアニメ特化のオープン/ローカルモデル（SDXLベース）。高解像度・キャラクター精度に優れ、Civitaiなどで人気。v1/v2/v3シリーズあり。[[15]](https://www.youtube.com/watch?v=MeS3MfBjpP4)[[16]](https://www.illustrious-xl.ai/)  
- **Anima**: CircleStone Labs製の2Bパラメータアニメ特化text-to-imageモデル（2026年頃リリース）。非商用ライセンスでHugging Face公開。イラスト・キャラクター生成に強い。[[8]](https://huggingface.co/circlestone-labs/Anima)  
- **Wan2.2**: Alibaba（Wan AI）製のオープンソース動画生成モデル（MoEアーキテクチャ）。2025年7月リリース。720p/24fpsのT2V/I2V対応、消費者向けGPUで動作。High/Lowノイズ専門家モデル分離が特徴。[[9]](https://github.com/Wan-Video/Wan2.2)[[10]](https://wan22.io/)  
- **Krea2 (Krea 2)**: Krea.aiの独自画像生成モデル。リアルタイム生成・背景詳細に強く、Turbo/Medium/Largeバリエーションあり。オープンソース版も存在。[[11]](https://www.krea.ai/)  
- **MiniMax H3**: MiniMax（Hailuo）製のオープンウェイトマルチモーダル動画モデル（2026年7月下旬リリース）。2K解像度・最大15秒・音声同期対応。テキスト/画像/動画/音声の統一入力が可能で、商用利用向け。[[12]](https://www.minimax.io/blog/minimax-h3)[[13]](https://fal.ai/minimax-h3)

（検索結果は2026年8月1日時点の情報に基づく。モデルは急速に更新されるため、最新版は公式サイトで確認を推奨。）
