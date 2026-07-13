# 🆕 新規トピック（前回からの差分）
### モデル: 冒頭まとめ：流行しているモデルの推測
- Krea2が実写・背景・高解像度・edit用途で覇権、低スペでもエロく高速なWFが求められる
- 主要モデルを選択理由中心に整理

### モデル: Krea2（Krea / クレア / Omusubi_Krea2など）
- 選択理由の主なポイント
- 低スペでも早くエロい、高解像度優秀、テキストエンコーダーが優秀
- edit（脱衣・顔変更）が素直、identity_edit/カスタムノード活用、turbo LoRAで立体感向上
- 実写ハーレム/カップルで没入感高、版権・アニメ特化版に期待
- 負荷高く低スペで重い、顔/プッシー画一化の指摘、二次元特化軽量版（450MB級LoRA）も話題
- LoRA学習は時間かかるがトレーナー機能（問題画像検出等）あり

### モデル: Wan（Wan2.2など）
- 動画生成（i2v）用途
- int8 convrotで大幅高速化（RTX5090で約半分）、VRAM/RAM効率良く低スペ実用、チューンモデル組合せで画質/動き調整、MoE構造で速度期待、ComfyUI更新での速度向上議論

### モデル: NovelAI (NAI)
- 話題少なく残念の声、v5予告に期待、Anima/Krea2で過去化認識、制御しやすさでNAIA検討も

### モデル: その他画像関連
- Lumina Image 2.0/HunyuanImageはkohya_ss対応でLoRA/FT注目、HunyuanImage-3.0-Instructは編集で強力だが80Bと巨大

### モデル: クラウドLLM / 関連
- Grok：エロ規制緩い最大利点、エロ小説高質・安価高速、実写エロ/CSAMリスク警告、創作はGemini/Claude優位の場合、繰り返し向きだがコンテキスト小
- GPT系：TerraはGPT-5.5相当で半額、Luna高速安価、GPT-Imageで教師画像/絵コンテ、GPT Liveは極めて流暢、エロ規制厳しく解禁断念、オーバースペック声、ComfyUI WF修正能力向上
- Claude：量子化/ComfyUI支援優秀、エロ適性でGrokより優れる場合
- Gemini：会話自然、文字/デザイン生成、技術相談/検索、Live APIは速度優秀だが人間らしさでGPT Liveに劣る場合
- Seedance/Seedream：新版言及もローカル優先で未試用、検閲酷い評価
- その他：deepseek v4 pro、Animagine、addift

### モデル: 全体傾向
- クラウドはエロ緩さ(Grok) vs 性能/自然さ(GPT/Claude/Gemini)、逮捕リスク警戒強
- ツールはComfyUI/kohya_ss/Forge Neo/EasyForgeNeo中心、int8 convrotがトレンド
- Z-Image系・LTX系は言及薄いorなし
- コミュニティはおかず適性・低スペ実用性を重視

### モデル: Web検索による参考情報
- 2026年7月時点の公開情報を確認
- Anima：CircleStone LabsとComfy Org協業の2B text-to-image、アニメ特化、DiTベース、HF公開・ComfyUI対応、低VRAM動作
- Krea2：Krea AIの約9B foundation model、美的多様性・スタイル制御、2026年5-6月OSS化、ComfyUI/Forge Neo対応
- Illustrious-XL：OnomaAIのSDXLベースイラスト/アニメ最適化、高解像度・キャラ生成に強い
- Wan2.2：Wan-AIのOSS大規模動画生成、MoE導入、t2v/i2v対応、消費者GPUで動作
- GPT-5.6ファミリー：Solフラッグシップ、Terra日常バランス半額、Luna高速低コスト、2026年7月頃公開
- Grok 4.5：xAIの2026年7月リリース、コーディング・エージェント強、安価、Opus級
- NovelAI：V4.5現行、V5は2026年夏頃期待
- その他：Lumina-Image 2.0、HunyuanImage大型、Seedance/SeedreamはByteDance系、int8-convrotは量子化手法でComfyUI热点
- モデルは急速進化、ローカル実行・量子化・オープンウェイトがトレンド

---
# 元の本文
**生成AIモデルに関するレポート**

### 冒頭まとめ：流行しているモデルの推測
提供されたログ（主に日本語の画像生成コミュニティ、特にNSFW/アニメ寄りローカル生成スレと思われるもの）から推測すると、**現在最も流行しているのはAnima（およびその派生：base、Aesthetic、turboなど）**です。圧倒的な言及頻度を誇り、アニメ絵・キャラクター生成で「猛威を振るっている」とされ、低スペック環境でも高速・扱いやすく、LoRA適性が高く、特定表現（手マン、尿道描写など）の精度が良い点が評価されています。AnimaとKrea2の登場でNovelAIやSDXLが「過去になった」との認識が広がっています。

次いで**Krea2（Krea / クレア）**が実写・背景・高解像度・edit用途で覇権的に扱われ、低スペでもエロく高速なワークフローが求められています。

その他、**Wan2.2**（動画i2v）、**Qwen-Image（QIE）**（編集・ピクセルシフト対策）、**FLUX系**（角度変更・edit）、**Illustrious（リアス）**（既存LoRA活用）が実用で絡み、量子化技術（int8 convrotなど）がこれらを低VRAMで動かす鍵としてホットです。クラウドLLMでは**Grok**がエロ規制の緩さで、**GPT系（5.6ファミリー含む）**が性能・会話自然さで、**Claude**が技術支援で登場。コミュニティの主戦場はローカル画像生成（特にアニメNSFW）で、速度・VRAM効率・エロ適性・LoRA適性が選択軸です。

以下、ログから抽出した主要モデルについて、選択理由を中心に整理します。

### 1. Anima（Anima / base / Aesthetic / Aesthetic-b / turbo / turbo LoRA / int8化など）
- **最も多く言及され、中心的なモデル**。アニメ絵で猛威を振るい、スマホ民に「とりあえず3060」と言えるほど扱いやすい。
- **選択理由の主なポイント**：
  - 軽くて扱いやすく、合体・調教・マージがされやすい。DiT式で高解像度に強く、SDXLの2段階アップスケより1発で早く品質が良い。
  - Illustrious（リアス）より優位：過学習+LBW不要寄りで、エロ漫画1ページのLoRAで手マンを綺麗に再現可能（リアスでは無理）。プロンプト流用は避けるべき。
  - 生成速度が圧倒的（turbo LoRA 4stepで約4分、krea2の50分級に対し大幅高速。ガチャ楽でおかず適性高い。int8化+turboでさらに速いが構図固定化・細部簡略化に注意）。
  - VRAM消費を抑えやすい（12GB環境でも可）。
  - Aesthetic-bが安定（美的微調整のみ、尿道描写の確率高い、画風LoRA向き）。turboで絵柄安定、エロ文字/汗のクオリティ良い。baseで十分との声も。
  - LoRA適性高いが影響されやすく、覚えが良いのでゴミ画像枚数稼ぎは悪手。krea2のLoRA学習より同ステップで3〜4倍速い。
  - 亜種乱立だが公式base推奨寄り。v2.0やAesthetic新版への期待強い。AnimaとKrea2でNAI/SDXLを過去にした。
- チェックリスト多数（Turbo/INT8使用時の注意、Illustriousプロンプト流用禁止など）。量子化議論も活発。

### 2. Krea2（Krea / クレア / Omusubi_Krea2など）
- 実写・背景特化で「覇権は変わらなそう」。アニメはAnima、実写/背景はKrea2の役割分担が流行。
- **選択理由の主なポイント**：
  - 低スペでも早くてエロい。高解像度が良すぎ、テキストエンコーダーが「お利口」。
  - edit（脱衣・顔変更）で素直に動く。identity_edit更新やカスタムノード活用。turbo LoRA調整で立体感向上。
  - 実写ハーレム/カップルで没入感高い（「脳破壊」体験談）。版権キャラ・アニメ系特化版への期待。
  - 量子化（int4/int8 convrot）で劣化がAnimaより少なく実用的。文字が安定、特定表現（イノシシ二足歩行など）可能。
  - 一方で負荷が高く低スペで重い、顔/プッシーが画一的になりがちとの指摘。二次元特化軽量版（450MB級LoRA）も話題。
- LoRA学習は時間がかかるが、トレーナー機能（問題画像検出など）も。

### 3. Illustrious（イラストリアス / リアス / ill / IL）
- Anima比較で頻出。チェックリストで「Illustrious系プロンプト流用禁止」。
- **選択／位置づけ理由**：マイナーキャラで既存LoRAが転がっている便利さ。パイプライン（リアス生成 → Flux角度変更 → Wan i2v）で使用。一方で「しがみつく人は何？」と疑問視され、制御難・崩れやすい・絵柄再現不足との不満。体型スライダー追加への関心。

### 4. Wan（Wan2.2など）
- 動画生成（i2v）用途。
- **選択理由**：int8 convrotで大幅高速化（RTX 5090で1生成約130秒→半分）。VRAM/RAM効率良く、低スペで実用。チューンモデル（SmoothMix / DaSiWaなど）の組み合わせ（high fp16 + lowなど）で画質/動き調整。MoEっぽい構造で速い可能性への期待。ComfyUIバージョンアップで速度向上するかの議論対象。

### 5. Qwen-Image（QIE / Qwen Image Edit系）
- 編集用途。
- **選択理由**：ピクセルシフト完全防止手法/ノードが優秀（Xで話題、kohyaも驚いた）。int8_convrot版で一貫性・ポーズ変更がbf16より優秀。リライター（自然言語→json）にQwen3.6-27B使用。ただし高解像度krea2処理で画質落ち、脱衣ではkrea2 editの方が素直な場合あり。

### 6. FLUX（FLUX.2 / flux2-klein / flux2devなど）
- edit・角度変更用途。
- **選択理由**：krea2で無理にeditするより適する場合あり。大型モデルが量子化で低スペ寄りでも実用的に動くようになった期待。一方で色合い制御難、量子化で文字苦手・構造いい加減・構図変化の問題指摘。

### 7. NovelAI (NAI)
- 話題少ない（FAQに「少ないんだけど」追加）。最近課金したがスレで話されない残念の声。v5実装予告に期待。Anima/Krea2で過去になったとの認識。制御のしやすさでNAIA検討の声も。

### 8. その他画像関連
- **SDXL / SD1.5**：速度早いが低性能。マージ適性、既存資産として。Anima full FTは約1/3速度。
- **Lumina Image 2.0 / HunyuanImage**：kohya_ss対応でLoRA/FT注目。HunyuanImage-3.0-Instructは画像編集で「巨人」だが巨大すぎ（80B）。
- **Pony**：scoreタグ比較で参考言及。
- **量子化（int8/int4 convrot）**：Anima/Wan/ZIT/Krea2/FLUXなどでホット。VRAM削減・速度向上・fp16相当品質。自前変換やAdaRound議論活発。「量子化の時代」。

### 9. クラウドLLM / 関連
- **Grok（Grok4.5含む）**：エロ規制緩いのが最大利点（「エロ関係やるならGrok使え」）。エロ小説質高い、安価高速（要約最適）。一方で実写エロ/CSAMリスク強く警告（逮捕事例共有、警察協力拒否報道）。創作はGemini/Claudeの方が良い場合あり。繰り返しタスク向きだがコンテキスト小さい。
- **OpenAI / GPT系（GPT-5.5/5.6、Terra、Luna、ChatGPT、GPT-Image、GPT Live）**：新バージョン性能・価格バランス（TerraはGPT-5.5相当で1/2価格、Luna高速安価）。軽量モデル継続リリース。GPT-Imageで教師画像/絵コンテ。GPT Liveは「自然すぎて会話気分」「コミュ障出る」レベルで流暢。エロ規制極めて厳しく、エロ混じりで挙動不安定、解禁断念済み。スレ民にはオーバースペックとの声。ComfyUIワークフロー修正能力劇的向上。
- **Claude**：量子化/ComfyUI支援で「えらい」（設定解析・改善ループ自律）。エロ適性でGrokより優れる場合。
- **Gemini**：会話自然さ（調整後）、文字/デザイン生成、技術相談/検索。Live APIは応答速度優秀だが人間らしさでGPT Liveに劣る場合。
- **Seedance / Seedream**：新版登場言及だがローカル優先で未試用。検閲酷いとの評価も。
- その他：deepseek v4 pro（知識テスト）、Animagine（Anima対比）、addift（学習手法）。

### 全体傾向
- **ローカル画像生成**：速度（ガチャ効率）、VRAM効率（量子化）、LoRA適性、特定エロ表現精度、高解像度耐性が軸。Anima（アニメ）+ Krea2（実写）のハイブリッドが主流。
- **クラウド**：エロ緩さ（Grok）vs 性能/自然さ（GPT/Claude/Gemini）。逮捕リスク警戒強い。
- ツール：ComfyUI、kohya_ss、Forge Neo、EasyForgeNeo中心。int8 convrotが技術トレンド。
- 除外/該当なし：Z-Image系、LTX系は言及薄いorなし。

このコミュニティは実践的で、モデルの「おかず適性」や低スペ実用性を重視しています。

## Web検索による参考情報
モデル名・バージョン・新サービス等について、2026年7月時点の公開情報を確認しました（日付はツール結果に基づく）。

- **Anima**：CircleStone LabsとComfy Orgの協業による2Bパラメータのtext-to-imageモデル。主にアニメ概念・キャラ・スタイルに特化し、数百万のアニメ画像と約80万の非アニメ芸術画像で学習（合成データなし）。DiTベースで速度と品質のスイートスポット。Hugging Faceで公開、ComfyUI対応。Turbo版やAesthetic版がコミュニティで活発。低VRAM（6GB以下）で動作・学習可能と評価。[[1]](https://huggingface.co/circlestone-labs/Anima)[[2]](https://www.reddit.com/r/StableDiffusion/comments/1qthxyi/new_anime_model_anima_is_amazing_cant_wait_for/)

- **Krea2**：Krea AIのin-house foundation model（約9Bパラメータ）。美的多様性・スタイル制御に特化し、2026年5-6月にオープンソース化（RAW/Turbo）。Artificial Analysisで独立ラボとしてトップ級。ComfyUI/Forge Neo対応、fp8/GGUF版あり。創造的探索向け。[[3]](https://www.krea.ai/krea-2)[[4]](https://github.com/krea-ai/krea-2)

- **Illustrious-XL**：OnomaAI ResearchによるSDXLベースのイラスト/アニメ最適化モデル。v0.1〜v3シリーズあり、高解像度・キャラ生成に強い。Civitai/Hugging Faceで人気、公式サイトもあり。[[5]](https://civitai.com/models/795765/illustrious-xl)

- **Wan2.2**：Wan-Video/Wan-AIのオープンソース大規模動画生成モデル。MoEアーキテクチャ導入で効率的。text-to-video / image-to-video対応（720P 24fps）、消費者GPU（4090など）で動作。論文あり。[[6]](https://github.com/Wan-Video/Wan2.2)

- **Qwen-Image / Qwen-Image-Edit**：Alibaba Qwenチームの20Bパラメータ基盤。テキストレンダリングに強く、Edit版はセマンティック/外観制御で高精度画像編集（多言語テキスト編集、被写体一貫性）。Hugging Face/ComfyUI対応。[[7]](https://qwen.ai/blog?id=qwen-image-edit)

- **FLUX系（FLUX.1 / FLUX.2）**：Black Forest Labsのモデル。FLUX.1-devは12B rectified flow transformer。FLUX.2は次世代でpro/flex/max/klein/devなどバリエーション。高品質・制御性・高速（kleinは1秒未満）、open weightsあり。edit/in-context生成強い。[[8]](https://bfl.ai/models/flux-2)

- **OpenAI GPT-5.6ファミリー（Sol / Terra / Luna）**：2026年7月頃一般公開。Solがフラッグシップ、Terraは日常バランス（GPT-5.5相当性能で約半額）、Lunaは高速・低コスト。ChatGPT/API/Codex対応。価格例：Sol $5/$30 per 1M tokensなど。プロンプトキャッシング改善。[[9]](https://openai.com/index/previewing-gpt-5-6-sol/)

- **Grok 4.5**：xAI（SpaceXAI）の2026年7月リリース。コーディング・エージェント・知識作業に強く、Cursorと共同学習。効率的で安価（例：$2/$6 per 1M）、Opus級と位置づけ。無料期間あり。[[10]](https://x.ai/news/grok-4-5)

- **NovelAI**：V4.5が現行主流。V5は2026年夏頃期待とのコミュニティ予測。サービス稼働中。

- **その他**：Lumina-Image 2.0（統一効率的画像生成フレームワーク、2025年頃）。HunyuanImage関連はTencent系で大型。Seedance/SeedreamはByteDance系動画/画像モデル（Seedance 2.0はマルチモーダル）。int8-convrotはコミュニティ量子化手法（Hadamard回転で外れ値抑制、ComfyUIでホット、FP8より速度/品質良い場合）。[[11]](https://github.com/Comfy-Org/ComfyUI/issues/14722)

これらのモデルは急速に進化しており、ローカル実行・量子化・オープンウェイトがトレンドです。詳細はHugging Faceや公式サイトで確認を。
