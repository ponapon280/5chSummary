# なんJ生成AIスレッド（なんJNVA部）総合レポート（ログ4-1000）

## スレッド概要
- **対象範囲**: ログ4～1000（約1000レス、複数パート）。NovelAI部スレだが、Stable Diffusion（SDXL中心）派生のローカルAI画像/動画生成が主軸。ComfyUI、Forge/Reforge、モデル更新（Illustrious/Wai派生、Z-image、Qwen系）、GPU危機、LoRA/プロンプトTipsが中心。
- **参加者傾向**: AI生成愛好家（上級者中心、5090保有者多め）。初心者（赤ちゃん）向けTips活発。NSFW（エロ）生成特化で、技術共有熱心だがアナル/脱糞AA荒らしやNTR論争で脱線。ローカル推し強く、クラウド抵抗（エロデータ漏れ懸念）。
- **雰囲気**: 技術談義本流だが、なんJらしいAA祭り（うんこ/アナル連投）、クリスマス/年末雑談混在。荒らし耐性高く、20超え即死回避成功。時期推定: 2025年頃（PyTorch2.11、Reforge大改修2025/3、どんぐり廃止2025/10）。
- **全体トーン**: GPU高騰悲観と新モデル興奮の狭間。次スレ: なんJNVA部★606（>>980～985）。

## 主なトピック分類とまとめ

### 1. **AIモデル更新・評価（最多話題）**
   Illustrious（リアス）系/Wai派生（※wanvideo無関係）が定番。NSFW/アニメ特化でプロンプト追従◎。
   

   | モデル | 特徴・評価 | 注目点 |
   |--------|------------|--------|
   | **Wai-illustrious v16** | 頭部/手指改善、オリキャラ安定。v14推奨（奇数verアダルト寄り微妙）。NSFW表記削除。 | v10好き→v14、IlluXL 0.1/1.0ベース（2.0互換悪）。 |
   | **Z-image (Base/Turbo/Edit/ZIT)** | 高速/表情安定、NSFWアニメ強。LoRA優位、インペイント希望。Base統合待機中。 | omni-base/PR進捗、フォト寄りだが二次弱。 |
   | **Qwen-Image-Layered (QIL/QIE)** | レイヤー分離（背景/キャラ抜き）革命。ComfyUI WF共有、低VRAM量子化（Q4K_M）。NSFW低いが編集向き。 | Apache2.0、Lightning LoRA高速（8step）。表情別人化課題。 |
   | **動画モデル (Wan2.2/SmoothMix/DaSiWa)** | Wan2.2高速エロLoRA必須、SmoothMix内蔵LoRA（腰振り暴走）。FLF（First-Last Frame、※FLUX無関係）活用。 | ハメ撮り風長動画、PainterLongVideo/SVI一貫性向上。 |
   | **その他** | AniKawaXL V4（肌質感◎）、noobAI XL、NetaYumeLumina、ChenkinNoob V0.2、Newbie v0.5.1、Libidinous。NAIキャラ参照高精度。 | Sora2無料化、Hunyuan3D VRAM24GB必須。 |

   **トレンド**: SDXL最強継続、自然言語+Danbooruタグハイブリッド。LoRA互換重視（SD1.5廃止）。

### 2. **GPU/ハードウェア危機（パニック熱）**
   RTX50シリーズ在庫激減/値上げ不可避。即買い推奨も電気代/排熱懸念。
   

   | GPU | 評価・ベンチ | Tips |
   |-----|--------------|------|
   | **RTX5090** | 3060比7倍速（SD1.5 1280x640: 8sec/13GB）。高解像度/動画必須。 | アイドル電力確認、xformers非対応（cap12.0）。PL70%推奨。 |
   | **5070ti/5080** | ミドルお得感薄れ、FHD可。ワッパ最強。 | 電源/ケース/PCI確認。 |
   | **その他** | 3090/3080 MultiGPU可、RTX Pro 6000中古1.5万、AMD Radeon GDDR6、中国64GB期待。 | データセンター爆需減産噂、BTO分割。 |

   **懸念**: PC淘汰/レンタルGPU未来像。ヨドバシ10%還元好評もポイント失効リスク。

### 3. **ツール・最適化・Tips共有**
   ComfyUI移行加速、拡張相性問題多発。
   

   | ツール | 利点・問題 | 解決Tips |
   |--------|------------|----------|
   | **ComfyUI** | MultiGPU/WF作成鉄板（For Loopプロンプト動変）。Zuntan simple初心者向け。 | venv Python3.10-3.13、Torch2.7-2.9 cu128/130、distorch_2.py差し替え。 |
   | **Reforge/Neo/EasyReforge** | 2025/3大改修、SageAttention高速。拡張破損（WD14/myprompt）。 | シンボリック解除、手動インストール、--use-sage-attention。 |
   | **Forge/A1111** | 安定/Seed再現性高。 | low_vram/tiled VAE、RAM Disk（ImDisk）。 |
   | **Stability Matrix** | Easy併用可もモデル消し前科。 | 別フォルダ、バックアップ（pip freeze）。 |

   **その他Tips**:
   - **Attention**: SageAttention2/xformers（差1割）、蒸留LoRA+CFG1最速。
   - **TTS/キャプション**: T5Gemma-TTS（エロ演技）、Llasa-Captions（Gemini）。
   - **VLM/LM**: LMStudioプロンプト自動化、PLaMo翻訳。
   - **アップスケーラー**: 4xUltraSharp（シャープ）、4xfoolhardy_Remacri（高負荷）、AnimeSharp。Denoise0.55-0.6、Euler a。

### 4. **LoRA学習・プロンプト・ControlNet**
   - **LoRA**: ベースanyillustriousXL（配布用）/Wai（個人）。タグ: 1girl/solo必須、「nanj dress」+既存併用。高解像教師オーバー学習注意。
   - **プロンプト**: 英語>日本語、yaml/markdown構造化。「projectile_cum」「clothes between breasts」「Yellow large ribbon...」。横乳/脚伸ばし苦手。
   - **ControlNet**: Anytest_v4/Posetest_v2.1構図忠実。複数キャラ（1girl+1boy）併用。

### 5. **NSFW/動画生成・エロTips**
   - **エロ特化**: 射精/結合描写（螺旋精液）、竿役（ugly man/black penis）。乳揺れLoRA欲、全裸パルクール妄想。NTR論争（快楽vs精神堕ち）。
   - **動画**: i2vカメラワーク長尺、画面外崩壊対策（end_image）。Motion amplitude/T5Gemma+RVC。
   - **荒らし/論争**: アナル/脱糞AA連投、解剖学書籍推奨。バター犬タブー。

### 6. **オフ題・コミュニティネタ**
   - AA祭り（メリークソシマス）、どんぐり廃止でLv0氾濫。自治厨喧嘩、ハードNG主張も黙認。
   - 雑談: クリスマス/年末おもちゃ、モノタロウ死亡、GTA6独占恐怖、ぽんガチャ性癖。

## 注目ニュース・トレンド
- **即死回避/勢い**: 20超え成功、新モデル（Qwen Layered/Z-image Base）で加速期待。
- **進化軸**: レイヤー分離革命、自然言語ハイブリッド、動画一貫性向上。ハイエンドコスパ向上もVRAM/電気代壁。
- **課題解決**: WF/LoRA即共有、初心者Wiki推奨。英語スキル/履歴削除注意（ChatGPT/Gemini厳格化）。
- **ベンチハイライト**: 5090最速、超高解像度11分。

## 結論・洞察
スレは技術共有の牙城。GPU冬の時代でもローカルNSFW強化で活況、ComfyUI/SDXL全盛継続。新規離脱リスクあるが、Tips豊富で耐性高。Z-image Base/Qwen2511リリースで次スレ爆発予想。エロ板違い恒例も独自深掘り（NTR/解剖学）魅力。詳細レス指定で深掘り可。#なんJNVA部