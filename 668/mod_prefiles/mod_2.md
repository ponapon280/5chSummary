**抽出結果（指定モデルのみ）**

指定されたモデル名（NovelAI/NAI, illustrious/リアス/ill/IL, FLUX, Wan, Qwen-Image, anima, Z-Image/ZIT/ZIE, LTX系）に関連する話題を、ログからすべて抽出・整理しました。  
特に「なぜそのモデルを選ぶ／多用するのか」の理由が明確な箇所を優先して抜き出しています。該当なしのモデルも明記します。

### 1. anima（Anima / Anima turbo / Anima base / Aesthetic / Turbo-ANIMAv3 など）
最も多く言及されており、中心的な話題。

- **Anima turbo / TurboLora / Turbo-ANIMAv3 の多用理由**
  - aesthetic + anima-turbov0.2 だと線がブツ切れ・彩度がかなり低くなるが、Turbo-ANIMAv3 だと「ええ塩梅」になる。シコるにはこれで十分。
  - Anima turbo は「ガチャ楽過ぎて多用したくなる」。HDサイズでLoRAモリモリ積んでも生成1.16秒程度とおかず適性が高い。
  - TurboLora の方が Anima の派生モデルにも適用できるため、そっちを多用してしまう。
  - 新しい Anima は「みんな大好き乳柱の鬼滅勢」にとって再現性が「天元」レベル。クオリティ的に anima1.2 くらいは名乗ってもいい。

- **Aesthetic の選択理由（b vs 無印）**
  - Aesthetic b の方が使いやすい。画風LoRAを使うならこれ。
  - 無印は実写が中途半端に混じって彩度が低くガビる。b の方が比較的安定して尿道からおしっこしてくれる。ただし構図の汎用性は b が豊か。
  - turboLORA無しだと aesthetic b と turbo モデルは尿が膣から出たりするケースがあるが、aesthetic は比較的安定。

- **その他の Anima 関連**
  - Anima base は二段サンプラーの一段目で「構図担当」として使っているため、最近の祭りにあまり乗れない。
  - Anima で気に入った絵柄の checkpoint をマージすると、SEXL（SDXL）までのモデルみたいに特に指示書かなくても勝手に多彩なポーズが出るようになる（仕組みは不明だが不思議）。
  - full FT は SDXL の約1/3速度（4090で SDXL 3 samples/s に対し Anima 0.75~1 samples/s）。
  - DiT式の Anima の方が高解像度に強く、SDXL で2段階アップスケするより Anima 1発の方が早く品質も良い（ガチャ回数・確率を上げた方が結果的に早い段階）。
  - kohya_ss v26.0.0 で Anima 完全対応（LoRA / full fine-tune / ControlNet-LLLite / Native LoHa/LoKr / torch.compile / Qwen-Image VAE 2D など）。LoHa はすでに試していたので楽しみ。
  - int8 convrot のおかげで VRAM 容量を減らせるので、もっとファイルサイズの大きい Anima の上位互換が来てほしい。
  - 変換時の exclude プリセット（--anima）が用意されている。

### 2. illustrious（イラストリアス / リアス / ill / IL）
- 「リアスにしがみつく人って何なんやろ」という疑問が出ている。
  - 理由として挙げられたもの：絵柄再現できないから。
  - 批判的意見：「1girlでシコれればそれ以外の全部がグチャってても満足」な層、ピクセルシフトの話題でも「？」が出るような連中。
- 実用的な使い方：マイナーキャラでシコりたい時に、その辺に LoRA が転がっているリアスが便利（自分で LoRA を作るほどでもない場合）。
- パイプライン例：リアスで画像を作って → Flux で魚眼アングルに変更 → wan で i2v → 編集 → VR化、という流れで使われている。

### 3. FLUX
- 上記パイプライン内で言及：リアスで作った画像を「Fluxで魚眼アングルに変更」する用途。

### 4. Wan
- wan2.2 の int8 convrot が「軽すぎて草」。モデルと TE を昆布変換したら VRAM16GB + RAM32GB で、解像度次第ではスワップなしでいけそう。生成も早すぎ。
- 公式の wan2.2 が対応しただけで、smoothmix や dasiwa はまだ対応していない。
- パイプライン例：リアス → Flux → **wan で i2v** → 編集 → VR化、という動画化用途で使われている。
- high だけ fp16 で4ステップ、low を Dasiwa 6ステップなどの組み合わせも議論されている（画質優先 vs 動き優先）。

### 5. Qwen-Image（QIE など）
- QIE のピクセルシフト防止について：去年からあった ReferenceLatent ノードを使う方法じゃダメなのか？という質問。
- 「QIEのピクセルシフト解消したし益々 BIE 不要になった」。
- kohya_ss の Anima 対応項目に「Qwen-Image VAE 2D」が含まれる。
- ピクセルシフトを直した人もフォロー済みのネームドだった、という言及。

### 6. Z-Image（Z-Image Turbo / ZIT / ZIE）
- zit の int8convrot で遅くなった人がいる（ノードを変えてオプション指定しても1割ぐらい遅い。数秒なので致命的ではないが）。「モデルが違うってことか？」「--dynamic-convrot を使っていないか？」という指摘（固定グループサイズの --convrot を使うべき）。
- 「zimage のこのスレ向け FT が実用レベルできたらようやくワンチャン考えられるレベル」（krea2 のこのスレ向けが来るかの議論の中で）。

### 7. NovelAI (NAI)
- 該当する言及なし。

### 8. LTX (LTX-2.3 / ltx2.3)
- 該当する言及なし。

**補足**
- 全体的に int8 convrot（昆布変換）が Anima / Wan / ZIT 周りで非常にホットな話題で、VRAM削減・速度向上・品質維持（fp16相当 or それ以上になるケースあり）の文脈で語られている。
- モデル選択の主な軸は「生成速度（ガチャ効率）」「おかず適性（エロ・再現性）」「高解像度耐性」「LoRA適用のしやすさ」「VRAM効率」になっている。

---

**抽出された生成AI「モデル」関連の話題**（除外指定モデル・ツールを除く）

### 主なモデルと話題
- **Krea2（krea2 / Omusubi_Krea2）**
  - identity_editが1.1に更新された。
  - 版権キャラが名前だけで生成されるアニメ系に強いチェックポイントを待つ声。
  - 4B/6Bクラスのこのスレ向けFTすら来ない状況で、krea2のこのスレ向けFTが来る可能性は低いとの見方。
  - SAM3+Krea2でComfyUIオンリーの手書き文字合成（同人誌風エロ文字など）が可能そう、との言及。
  - 理由：版権キャラ再現性・アニメ系適性が期待されている。GUIツールも言及。

- **Grok（Grok4.5）**
  - 主要モデル更新の一環で登場。無料との乖離が激しくなっているとの指摘。
  - エロが緩い以外の取り柄が薄い。慣れればGeminiやClaudeの方がエロくなる。
  - Grok4.5は繰り返しタスク向けでコンテキストが小さく、創作系はイマイチ。見た目変化が少なく地味。
  - 理由：エロ規制の緩さが主な利点として挙げられているが、創作・総合性能では他に劣るとの評価。

- **GPT / ChatGPT（ChatGPT5.6 / チャッピー / GPT-live / GPT音声）**
  - ChatGPT5.6は順当に賢くなり、気が利きつつミスも減っている。
  - GPT-live（音声会話）が流暢すぎてコミュ障が出る・人見知り発動するレベル。相槌やトーンの自動調整が人間らしい。
  - リアルタイム過ぎて驚き屋になりそう。パーソナライズ影響か「草生える」への反応なども。
  - 音声に声指定（Irodori-TTS的）や手元音声ファイル参照ができたら良いがコンプライアンス的に無理そう。
  - 無料版に広告が出るように。ステマ懸念。
  - Grok/Claudeと組み合わせて「リアルマギシステム」的に使う案（トークン食い過ぎ懸念）。
  - 理由：賢さ・気が利く・会話の自然さ（特にlive音声）が評価され、契約検討や英会話レッスン用途が挙がる。

- **Claude**
  - Grok/GPTとセットで契約する案。
  - 慣れればGeminiやClaudeの方がエロくなる（Grok比較）。
  - 過去に圧迫面接させて絶交した経験談。
  - 理由：エロ適性や総合性能でGrokより優れるとの比較。

- **Gemini（GEMI子 / Google AI Pro / gemini-3.1-flash-live-preview / Google Live）**
  - Google AI Proのau割引終了で「geminiちゃん…」との反応。
  - 有料版を使わせたいからか文字入れをわざと間違える印象。
  - Live APIは応答を音声にしただけっぽく人間らしさ薄い（ChatGPT liveと比較）。調整すれば自然トーン可能で、割り込み検知・応答速度50ms級で自然。裏で思考専用Geminiを併走させる設計で業務利用も視野。
  - 手書き吹き出しエロ文字デザイン生成に使用例（黒い背景に白い吹き出し＋同人誌風震えた手書き文字）。
  - 理由：会話自然さ（調整後）、エロ適性、文字/デザイン生成の実用性。ChatGPT liveと比較されつつも業務応用可能性が評価。

- **SDXL / SD1.5**
  - SD1.5時代から気に入った絵柄checkpointをマージするのが好きで、Anima比較で言及（除外モデル絡みだがSD自体は対象）。
  - SDXLのUnetは低性能だが早い。DiT式との比較で、高解像度耐性や到達速度、ガチャ回数・確率、品質確保後の低step turbo増加が議論。
  - Anima full FTはSDXLの1/3程度の速度（4090でSDXL 3 samples/s vs 0.75~1）。
  - 理由：速度・マージ適性・既存資産としての使いやすさ。品質より高速化/ガチャ重視の文脈。

- **Lumina Image 2.0**
  - kohya_ss v26.0.0でLoRA・full fine-tune対応が追加されたとの報告。

- **HunyuanImage-2.1**
  - kohya_ss v26.0.0でLoRA training support追加。

- **seedream5pro**
  - 使ってみたが検閲が酷いとの評価。

- **smoothmix / dasiwa / 10eros / lightx2v**
  - smoothmixのint8convrot希望（特にv1）。dasiwa/smoothも元々fp8なのでベースint8convでfp16相当品質+速度。
  - highをfp16（4step）+low Dasiwa（6step）で画質向上。動き重視か画質優先か。
  - 10eros v1.4よりint8 convrotの方が容量大きいケース。
  - lightx2vはPCメモリ許す限り重いもの（rank256など）推奨。fp16 vs conv8intで速度向上あるが陰部詳細が潰れる場合あり。
  - 理由：画質・速度バランス、VRAM効率、既存fp8からの品質向上。

- **HiDream（hidream-O1）**
  - int8 convrot変換設定の精度確認で言及（FP16/BF16同等か部分的に上回る）。

- **その他関連**
  - Aesthetic b（無印より彩度・ガビりが少なく安定。画風LoRA使うならこちら。構図汎用性でbが豊かとの比較。尿道描写の安定性など）。
  - int8/int4 convrot技術全般（VRAM削減・速度向上。fp8_scaledよりFP32→INT8の方が精度出る可能性。自前変換はBF16から。Radeon対応やComfyUI int4対応の話）。用途としてマネタイズ初心者ガイドでのトラブル懸念も。
  - LECO（concept erasure/editing）training for SD1.x/2.x and SDXL。
  - Inpainting model training for SD1.5/SDXL。

### 選定理由の傾向まとめ
- **エロ/NSFW適性・規制緩さ**：Grok（緩いが他に劣る）、Claude/Gemini（慣れれば強い）。
- **速度・VRAM効率・ガチャ適性**：SDXL（早いが低性能）、int8/int4 convrot適用モデル群（VRAM削減で大モデル希望）、high/low分割ステップ。
- **再現性・特定用途**：Krea2（版権キャラ・アニメ系）、Gemini（文字/デザイン・Live会話自然さ）。
- **賢さ・会話自然さ**：ChatGPT5.6 / GPT-live（気が利く・流暢・人間らしい）、Gemini Live（調整後で業務可能）。
- **トレーニング対応**：kohya_ss更新でLumina/Hunyuanなどが注目。

除外指定（Anima系全般・Illustrious/リアス・FLUX・Wan・Qwen-Image系・Z-Image系・LTX・NovelAI）はすべて無視しています。ログ全体が画像生成（特にNSFW）・量子化・ComfyUI周辺が中心で、LLMは会話/補助用途として登場しています。