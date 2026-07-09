# 🆕 新規トピック（前回からの差分）
### 冒頭：テキストから推測される流行モデルのまとめ
- 言及頻度・議論深度・比較熱量から流行を推測。ローカル勢（ComfyUI中心）の実践が中心で、エロ/NSFW適性・LoRA学習・VRAM/速度・プロンプト親和性が選択基準
- 動画生成：Wan (WAN2.2) が元絵雰囲気保持で優位、LTX (LTX-2.3) が動画+音声同時生成やDirector機能で言及、組み合わせ推奨も
- 有料：NovelAI (NAI) V5 テスター募集・品質期待が複数
- LLM/補助：DeepSeek（安価・規制緩・エロ/コーディング）、GPT/Codex系（壁打ち・開発支援）、ローカルQwen3.x/Gemma4が実務活用。SCAIL-2・Ideogram・Fableも補助的

### Krea2（およびRedCraft / Engineer / RAW / NSFW版など）
- 言及頻度最高。三次/実写寄りNSFWの主戦場
- 選択理由：AI臭軽減、リアル系プロンプト利き、変態寄り衣装がLoRAなしで出やすい、パンツ描写力、盗撮・分割画面等シチュ再現、実写背景臨場感、文字入力柔軟性、Editで絵柄変化少、Civitai学習対応速さ。INT8化・TE差し替えで制御
- 欠点：LoRAで重くなる場合、特定タグ効きにくさ、NSFW制限一部強、キャラ過大現象、低スペLoRA学習難、ジャパングLoRA効き不明瞭
- VRAM消費大（併用で70GB級）、公式WFとNSFW版の相性問題

### Illustrious（リアス / ill / IL / waiIllustriousSDXLなど）
- 選択理由：danbooruタグだけでシチュ出せる自由度、LoRA学習短く制御しやすい、過去資産活用、エロで初期リアス系が強い評価、画風LoRAベース多用

### その他画像系
- Z-Image Turbo (ZIT)：INT8 ConvRotで約5GB縮小＋速度向上が「しゅごい革命」。パンツ/特定NSFWは他に劣る比較も
- NovelAI (NAI)：V5テスター募集。品質一定・背景/構図/下着向上期待。キャラ1枚デザイン再現は他で真似しにくい。略称「NVA部」は検索避け
- SCAIL-2：ダンス動画のキャラ置き換え・ポーズ転写の手軽さ/品質で選ばれる。絡みAV系は検出で躓きやすい
- Ideogram：ComfyUIでのテキスト生成ノード/WF選択肢

### 動画生成モデル
- Wan (WAN2.2)：Start/End制御や文字生成実験。元絵雰囲気保持でLTXより優れ品質優先（時間かかる）。LTX Directorとの声入れ組み合わせ推奨
- LTX (LTX-2.3)：動画+音声同時生成で臨場感に必要。雰囲気保持はWAN劣位だがDirectorで音声用途。特定挙動回避で過去版遡及、dmdサンプラー速度が関心

### LLM・補助モデル
- GPT系（ChatGPT/Codex/5.5 Pro等）：ゲーム開発・壁打ち・WF作成・エラー診断で急増。Codexは一発実行・GitHub連携便利。弱点は文章力・規制強・エロ弱
- DeepSeek（V4/API）：安価・脱獄容易でエロ生成手軽、コーディングも評価。コスト安全（事前課金）
- Claude：Maxプラン多く壁打ち比較対象
- Fable：高度最適化・アプリ/ノード作業で愛着、高級モデル扱い。コストはDeepSeek優位の声
- Grok：アニメ＋実写合成の綺麗さ

### ## Web検索による参考情報
- モデル名・バージョン・サービスの事実関係を2025-2026年公開情報で確認・引用したまとめ
- Anima：CircleStone LabsとComfy Org協業の約2Bアニメ特化T2I。Cosmos-Predict2ベース、Qwen3エンコーダ＋VAE。HF公開・非商用寄り
- Krea2：Krea.ai独自基盤（美的表現・制御性・LoRA・高速推論）。画像/動画/3Dスイートの一部。ComfyUI利用活発
- Illustrious XL：OnomaAIのSDXLイラスト/アニメ特化。1536ネイティブ、Danbooru＋自然言語。Civitai/HF人気基盤
- LTX-2.3：LightricksのDiT動画モデル。動画＋同期音声、モーション/忠実度向上。I2V・IC LoRA対応、ComfyUI利用
- Wan 2.2：Alibabaオープンソース大規模動画（Apache 2.0）。MoE、720P/24fps、T2V/I2V。消費者GPU動作、雰囲気保持高評価
- NovelAI Diffusion：有料。V4.5正式済、V5テスター募集中。アニメ特化でキャラ制御強い
- Z-Image Turbo：Alibaba Tongyi-MAIの6B蒸留版。8ステップ・サブ秒高速、フォトリアル・バイリンガルテキスト。OSS
- SCAIL-2：スケルトン不要のキャラアニメ/動き転写。In-Context Conditioningで置き換え・マルチキャラ。ComfyUIチュート多数
- Ideogram 4.0：テキスト精度・編集特化オープンモデル。デザイン用途、ComfyUI Day0サポート
- DeepSeek-V4：MoE LLM。コーディング/エージェントでOSS SOTA級・コスト効率高。1Mコンテキスト、規制緩さ支持
- 主にHF/Civitai/GitHub/公式で利用可。ComfyUIがローカル標準、量子化・LoRAが実用鍵。最新は公式確認推奨
- 本レポートは提供テキスト抽出を基に選択理由を忠実反映しWeb検索で事実補完。深掘りは指示次第

---
# 元の本文
**生成AIモデルに関するレポート**

### 冒頭：テキストから推測される流行モデルのまとめ
提供されたテキスト（主に画像生成コミュニティのログ抽出結果）から、モデルの言及頻度、詳細な議論の深さ、比較・使い分けの熱量を基に流行を推測すると、以下のようにまとめられる。

- **画像生成の二大軸**：**Anima（二次元/アニメ特化エロ）** と **Krea2（三次/実写寄りNSFW・リアル）** が圧倒的に中心。住み分けが明確で、「二次エロはAnima、三次エロはKrea2」との声が複数。AnimaはLoRA学習・エロ性能・継続支持で根強く、Krea2はAI臭軽減・プロンプト利き・特殊衣装/シチュで急速に主戦場化。
- **基盤・前世代**：**Illustrious（リアス）** がLoRA学習のベースやエロ評価で頻繁に比較対象。過去の資産活用や短時間学習の利点が指摘。
- **動画生成**：**Wan (WAN2.2)** が元絵雰囲気保持で優位評価、**LTX (LTX-2.3)** が動画+音声同時生成やDirector機能で言及。組み合わせ利用が推奨されるケースも。
- **高速・軽量・Edit系**：**Z-Image Turbo (ZIT)** や **Qwen-Image関連** がINT8量子化による速度/サイズ改善で試行対象。**FLUX.2-klein** なども効率化で登場。
- **有料サービス**：**NovelAI (NAI) V5** へのテスター募集・品質期待が複数。
- **LLM/補助**：**DeepSeek**（安価・規制緩さ・エロ/コーディング）、**GPT/Codex系**（壁打ち・開発支援）、ローカルの**Qwen3.x / Gemma4** が実務で活用。**SCAIL-2**（動き転写）、**Ideogram**、**Fable**なども補助的に。
- **全体傾向**：単一モデルのオールインワンより、用途別住み分け（2D/3Dエロ、速度/品質、ローカル/クラウド）が主流。INT8 ConvRotなどの量子化・LoRAエコシステム・ComfyUIワークフローが選択の鍵。新モデル流行時もAnima継続層が存在し、「エロ充実モデルが天下を取る」との見方も。

テキストはローカル勢（ComfyUI中心）の実践議論が中心で、エロ/NSFW適性、LoRA学習時間/品質、VRAM/速度、プロンプト親和性が選択基準のコアとなっている。

### モデル別詳細レポート（選択理由を含む）

#### 1. 画像生成モデル

**Anima（Anima-base / Turbo / Aesthetic など）**  
- 最も詳細に議論されたモデルの一つ。二次元エロ特化として「充実したエロが生成できる現状トップ」「二次エロはAnima」と明確に位置づけ。  
- **選択・継続理由**：エロ性能の高さ（Krea比較で優位とする声）、絵柄の良い部分が他LoRAに混ざると好みが向上、小物/家具LoRA学習精度の高さ（SDXLで失敗したケースでも成功）、既存ワークフロー流用しやすさ、プロンプトだけでは品質制御が難しいためLoRA有効。INT8変換でサイズ半分・生成時間ほぼ変わらず（または時短）。  
- 派生：BaseはLoRA学習標準・クッキリ感で好み、Turboは速度/安定性/反復しやすさで公式推奨入り口、Aestheticはキャラ再現度・細部/解剖学・下着/性器クオリティ・美観重視（リアスマージ好き向け）だが、色くすみ・ノイズ・指崩れで好み分かれ。  
- 欠点：特定視点/アングル出しにくさ、汁表現弱さ、手の破綻、長プロンプトでの硬直/崩壊リスク。言語モデルは軽量Qwen3 0.6BをCosmos 2Bとバランス良く採用（パラ数上げでスペック上昇・性能向上わずかのため）。  
- 学習時間は設定（解像度512高速プリセットなど）で短縮可能だが高品質だと長時間。新モデル流行時も「Animaを続ける」層あり。  

**Krea2（およびRedCraft / Engineer / RAW / NSFW版など）**  
- 言及頻度最高。三次/実写寄りNSFWの主戦場。  
- **選択理由**：AI臭さ軽減、リアル系としてのプロンプト利きの良さ、ハイレグ競泳水着など従来NSFWで難しかった変態寄り衣装がLoRAなしで出やすい、パンツ描写力、盗撮・分割画面・スカートめくりなどのシチュ再現、実写背景での臨場感、文字入力の柔軟性（「クソコラ製造機」適性）、Editモデル化で絵柄変化が少ない。Civitaiでのトレーニング対応の速さ。INT8化・TE差し替え（Engineerでケモ表現強化など）で制御。  
- 欠点：LoRA噛ませると重くなる場合あり（CUDA更新で改善例）、特定タグ（high-reg/cameltoe）が効きにくい、NSFW制限が一部強い、背景に対してキャラが異様に大きくなる現象、低スペでのLoRA学習しづらさ。アジア人表現は得意だがジャパングLoRA効きが分かりにくい場合も。  
- VRAM消費大（他モデル併用で70GB級の例）、公式ワークフローとNSFW版の相性問題あり。  

**Illustrious（リアス / ill / IL / waiIllustriousSDXLなど）**  
- Animaの前世代・比較対象として頻出。  
- **選択理由**：シチュエーション毎のLoRA不要でdanbooruタグだけで望みのシチュを出せる自由度向上、LoRA学習時間が比較的短く設定でコントロールしやすい、過去の学習データ資産として活用、エロ生成で「結局リアス系（特に初期）が強い」との根強い評価。画風LoRAのベースとして多用。  
- Animaへの移行・互換（LoRAコンバート希望）や、Aestheticのターゲット層として言及。  

**その他画像系**  
- **Z-Image Turbo (ZIT)**：INT8 ConvRotで大幅サイズ縮小（約5GB）＋生成速度向上が評価。「しゅごい革命」。パンツ描画や特定NSFWで他に劣る比較も。  
- **Qwen-Image / QIE2511 / zen-bear-v3など**：文字出力精度が高い、Editモデル実用性、int8化で速度向上。レイアウトセンスは指示なしだと弱い場合あり。キャプション/プロンプト生成にも活用。  
- **FLUX / FLUX.2-klein-9B**：大型モデルとしてint8変換時の注意（元確保必要）、int8で使いやすくなった報告。  
- **NovelAI (NAI)**：V5テスター募集（徹底テスト＋フィードバック要求）。有料だが品質一定、背景正確さ・構図/ポーズ制御・下着/性器品質向上への期待。キャラ1枚デザイン再現機能は他（Anima含む）でまだ真似しにくい。ローカルとの比較で課金継続例あり。略称「NVA部」の由来は検索避け。  
- **SCAIL-2**：ダンス動画のキャラ置き換え・ポーズ転写の手軽さ/品質で選ばれる。絡みAV系は検出で躓きやすい。  
- **Ideogram**：ComfyUIでのテキスト生成ノード/ワークフロー選択肢。  

#### 2. 動画生成モデル
- **Wan (WAN2.2)**：Start/Endフレーム制御や文字/記号生成実験。**元絵の雰囲気を崩さず動画生成できる**点がLTXより優れ、品質優先で選ばれる（時間はかかる）。動画生成＋LTX Directorで声入れの組み合わせ推奨例。  
- **LTX (LTX-2.3 / ltx2.3)**：動画と同時に音声生成するタイプとして臨場感（空間音響＋雑音）に必要との指摘。特定挙動回避で過去バージョンに遡る例。雰囲気保持ではWANに劣るが、Director機能で音声用途。dmdサンプラー速度が関心事。  

#### 3. LLM・補助モデル
- **GPT系（ChatGPT / Codex / 5.5 Pro / 5.6など）**：ゲーム開発・デザイン壁打ち・ワークフロー作成・エラー診断で使用量急増。Codexは「言ったことを一発でやる」「GitHub連携」で便利。Proはリミット大。弱点は文章力弱さ・規制強くエロ弱い・センシティブ絵で挙動増加。  
- **DeepSeek（V4 / APIなど）**：安価・脱獄簡単で手軽にエロ生成、コーディング性能も評価（Claude中間くらいの体感）。ローカルGemmaより良いとする移行例。コスト安全（事前課金）。  
- **Claude**：Maxプランユーザーが多く、壁打ち比較対象。  
- **ローカルLLM（Qwen3.6 / Gemma4）**：Qwenはコーディング向き（Gemmaより）、関係ファイル選別・要約・論点整理に適するが最終実装は危険。Gemmaは日本語優秀だがコーディング落ちる。キャプション用途で活用。  
- **Fable**：高度な最適化・アプリ/ノード作業で愛着強く、高級モデルとして。コスト比較でDeepSeek優位の声。  
- **Grok**：アニメ＋実写合成の綺麗さ。  

**横断的傾向**：INT8 ConvRotがAnima/ZIT/Qwen/Krea/FLUXなどで速度/精度/サイズ改善の「革命」として多数報告（古いGPUでも恩恵）。用途別使い分けが賢いリソース配分。モデル単体よりワークフロー・自作LoRA・設定が「秘伝」化。  

### ## Web検索による参考情報
モデル名・バージョン・サービスの事実関係を確認した結果のまとめ（2025-2026年時点の公開情報に基づく）。主要ソースを引用。

- **Anima**：CircleStone LabsとComfy Orgの協業による約2Bパラメータのテキスト-to-イメージモデル。NVIDIA Cosmos-Predict2-2B-Text2Imageをベースに、Qwen3 0.6Bテキストエンコーダ＋Qwen VAEを使用。主にアニメ特化。非商用ライセンス寄与。Hugging Faceで公開、AnimaYumeなどの派生も。[[1]](https://huggingface.co/circlestone-labs/Anima)[[2]](https://www.reddit.com/r/StableDiffusion/comments/1qsbgwm/new_anime_model_anima_released_seems_to_be_a/)

- **Krea2**：Krea.aiの独自基盤画像モデル（Krea 2 / Turbo / Largeなど）。ゼロから構築され、美的表現・制御性・LoRA対応・高速推論に焦点。画像・動画・3D対応のクリエイティブスイートの一部。ComfyUIでの利用・LoRA学習が活発。[[3]](https://www.krea.ai/)[[4]](https://www.youtube.com/watch?v=0jssDQ9b9hI)

- **Illustrious XL**：OnomaAI ResearchによるSDXLベースのイラスト/アニメ特化モデル。高解像度（1536×1536ネイティブ）対応、Danbooruタグ＋自然言語プロンプト。v1/v2/v3シリーズあり。Civitai/Hugging Faceで人気基盤。[[5]](https://civitai.com/models/795765/illustrious-xl)[[6]](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0)

- **LTX-2.3**：LightricksのDiTベース動画生成モデル。動画＋同期音声生成、シャープ詳細・モーション改善・プロンプト忠実度向上。Image-to-VideoやIC LoRA対応。ComfyUIで広く利用。[[7]](https://ltx.io/model/ltx-2-3)[[8]](https://github.com/Lightricks/ltx-video)

- **Wan 2.2**：Alibaba (Wan-AI) のオープンソース大規模動画生成モデル（Apache 2.0）。MoEアーキテクチャ、720P/24fps、T2V/I2V対応。消費者GPU（4090など）で動作。雰囲気保持や人間表現で高評価。[[9]](https://github.com/Wan-Video/Wan2.2)[[10]](https://www.thundercompute.com/blog/wan-2-2-comfyui-ai-video-model)

- **NovelAI Diffusion**：有料サービス。V4.5が正式リリース済み（品質・マルチキャラ・プロンプト改善）。V5はテスター募集中（X/Pixivフォロワー条件など）。アニメ特化でキャラコントロール強い。[[11]](https://novelai.net/v4)[[12]](https://x.com/novelaiofficial?lang=en)

- **Z-Image Turbo**：Alibaba Tongyi-MAIの6Bパラメータ画像モデル。蒸留版で8ステップ・サブ秒級高速生成、フォトリアリスティック・バイリンガルテキスト対応。オープンソースでHugging Face/デモ利用可能。[[13]](https://zimageturbo.com/)[[14]](https://github.com/Tongyi-MAI/Z-Image)

- **FLUX.2 [klein]**：Black Forest Labsの次世代FLUX。klein 9B/4Bは高速・効率的（1秒未満推論、消費者GPU対応）、生成＋編集統一。Apache 2.0版あり。[[15]](https://bfl.ai/models/flux-2)[[16]](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)

- **Qwen-Image**：Alibaba Qwenチームの画像生成モデル（20B級MMDiTなど）。テキストレンダリング精度・編集・プロンプト忠実度に強み。API/Together AIなどで提供。Qwen VLoは理解＋生成統合。[[17]](https://www.mindstudio.ai/blog/what-is-qwen-image-alibaba)[[18]](https://qwen.ai/blog?id=qwen-vlo)

- **SCAIL-2**：エンドツーエンドのキャラクターアニメーション/動き転写モデル。スケルトン不要のIn-Context Conditioningでキャラ置き換え・マルチキャラ対応。ComfyUIチュートリアル多数。[[19]](https://www.youtube.com/watch?v=_5aYMeIMdZc)[[20]](https://teal024.github.io/SCAIL-2/)

- **Ideogram 4.0**：テキスト（タイポグラフィ）精度・プロンプト忠実度・編集に特化したオープンモデル（9.3Bなど）。デザイン用途で評価。ComfyUI Day0サポート。[[21]](https://ideogram.ai/)

- **DeepSeek-V4 (Pro/Flash)**：DeepSeek AIのMoE LLM。コーディング・エージェント能力でオープンソースSOTA級、コスト効率高い。1Mコンテキスト、エロ/規制緩さがコミュニティで支持。Hugging Face/API提供。[[22]](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)[[23]](https://api-docs.deepseek.com/news/news260424)

これらのモデルは主にHugging Face、Civitai、GitHub、公式サイトで利用可能。ローカル実行はComfyUIが標準的。量子化（INT8/fp8）やLoRAが実用の鍵。情報は急速に更新されるため、最新は各公式を確認推奨。

このレポートは提供テキストの抽出内容を基に構成し、選択理由を忠実に反映。Web検索で事実確認を補完した。さらなる深掘り（特定モデルの設定例など）が必要であれば指示を。
