# 🆕 新規トピック（前回からの差分）
- HappyHorse-1.0（Alibaba開発、15B param、T2V/I2V+音声、ローカル軽量エロLoRA期待）
- Wan2.2（エロ限界表現、FP4量子化高速）
- StabilityMatrix崩壊報告
- 10girls80ガチャ成功（複数キャラ生成）
- PornMaster anima（乳首綺麗生成）
- Emoji-TTS/VoiceDesign旧版推奨（Irodori-TTS連携）
- Open-LLM-VTuber話題
- AIクローン（将来展望）
- 環境下限（RTX3060ti実用、CPU e2b可）

---
# 元の本文
# なんJ AI画像生成スレッド 総合レポート（ログ4-1000）

## 1. スレッド概要
- **期間/範囲**: ログ4〜1000（総約1000レス、抽出約700レス）。Anima preview3リリース直後から本リリース待ちまでの全貌。
- **主なテーマ**: Anima（preview3/CottonAnima中心）の画像生成最適化、LoRA学習、ComfyUIワークフロー、NSFWエロ生成、動画モデル（HappyHorse/Wan2.2）、LLM（Gemma4/SillyTavern）活用。SDXL/Illustrious（waiはIllustrious派生モデル）/Pony/Noobとの比較多め。
- **参加者傾向**: ローカル環境（ComfyUI/Forge Neo）構築派中心。高スペックPC自慢、トラブル共有、エロ特化（騎乗位/ふたなり/乳首/残像フェラ/アナル）。クラウド（Kling/Seedance）は規制・有料で敬遠。
- **全体ムード**: 興奮と試行錯誤の共有（「サンガツ！」多め）。AI進化速度に「追いつけない」「ゲームエンド連発」と嘆きつつ、Tips交換活発。反AI議論は即スルー。NSFW実用化が鍵で、Anima3が活性化要因。

## 2. 主要モデル更新と評価


| モデル/ツール | 更新内容・強み | 弱み・課題 | ユーザー反応 |
|---------------|----------------|-------------|-------------|
| **Anima preview3/CottonAnima** | クオリティ向上、キャラ/マイナー絵師再現強化、内蔵キャラ増加、hires fix対応（1024→1536可）、自然言語制御優秀、多様なNSFW構図（仰け反りブリッジ/複数人）。LoRA互換良、プロンプト空でも可愛い出力。 | 手/指/腕崩れ、ガチャ不安定（Pony遺伝疑い）、品質タグ（score_9）でテカテカ肌、絵師タグ相性悪、自然言語崩壊。夕焼けバイアス、Facedetailerエラー。 | 「暴れ馬だが他では出せない」「レーシングカー級有望」（高評価50%超）。小出し公開賛否、正式版/ControlNet待ち。 |
| **Illustrious（wai派生）/Noob/ReaJiN** | 安定/美麗、低クOL強化、絵師ミックス得意。 | 特殊構図/多様性弱。 | Animaの「多様性上」だが安定ベンチマーク。「リアスでええんちゃう？」派残る。 |
| **HappyHorse-1.0** | Alibaba開発、Seedance2超え主張（15B param、T2V/I2V+音声）。ローカル軽量期待、エロLoRA可能。 | GitHub未公開、ステマ疑い、テキストエンコーダー貧弱。VRAM48GB+必要。 | 「今年ゲームエンド5回」興奮も偽サイト注意。 |
| **Wan2.2** | エロ限界（触手/アナル/騎乗位/髪揺れ自然）、FP4量子化高速。 | 構図ワンパターン（POV中心）、股間ぼんやり、瞬き崩れ。 | 実用性高評価も後継待ち。 |
| **Gemma4（26B/31B A4B/e4b）** | エロチャット/小説/ロールプレイ実用（Gemini/GPT4o並み、日本語強）。MoE高速化（LM Studio/Kobold.cpp）。 | 否定文/漢字弱、重い版VRAM食い。 | 「安価キャバクラ級」絶賛。SillyTavern連携でフルスタック。 |
| **その他** | NAI v4再現難、Pony/e621臭い、ACE-Step歌唱向上、Meta新LLM規制強。Civitaiゾーニング（red/greenスワップ、ブックマーク更新必須）。 | - | SDXL離脱組増加。 |

## 3. 技術Tips・ワークフロー最適化
- **ComfyUI**:
  - SDXL↔Animaトグル（Any Switch/BasicPipe/Fast Groups Muter）。i2i活用（SDXL生成→Anima denoise低め）。
  - SAM3/EasySAM3: 股間/nipple認識不良、crop factor厳。ComfyUI更新でFacedetailerエラー解消もCPU負荷増。
  - Hires.fix: Animaで1024→1.5-2倍可（アップスケーラーなし）。全体Hires vs 顔Detailer論争。WF例: Anima→ReaJiN i2i。
  - その他: YAMLエディタ、rgthreeノード並び替え、グループ/サブグラフ整理、3DカメラUI。
- **LoRA/ファインチューニング**:
  - Anima特化: 1024解像度推奨（512劣化）、Pre2→Pre3互換良、Epoch途中使用で過学習回避。絵師タグ`@artist`必須、`[A|B]`構文、Gelbooru優先。ChenkinNoob0.5/色温度LoRA好評。
  - 戦略: 生成画像集めLoRA化、score_7推奨（masterpiece崩れ）。dim4/batch2でVRAM8.6GB。
- **プロンプト/パラメータ**:
  - 品質: score_7（score_9テカテカ→ネガ"shiny skin"）、flat color弱化時はfuzich○c○。
  - NSFW: 詳細記述（"girl lying on her back, missionary"）、ネガ"realistic, 3D"、negpip -1/-2、explicitタグ。
  - CFG1.0速生成、res_multistep+sgm_uniformで崩壊減。
- **環境構築**: Python venv/embedded（3.10画像/3.11音楽）、Forge Neo 3.13.12、RTX5xxx FP4量子化。StabilityMatrix崩壊報告。

## 4. NSFW/エロ生成の実用性
- **強み**: Animaで特殊体位（sybian/ロールスロイス/body bridge/残像フェラ）、Wan2.2触手/アナル、Gemma4ふたなり/緊縛自然。複数キャラ挑戦（10girls80ガチャ成功）。
- **弱み**: 股間ぼんやり、おっぱい多様性不足、位置関係/マンガ表現難、素材枯渇（うんこ/e621）。
- **生成例/Tips**: 乳首綺麗（PornMaster anima）、パンティー値札→i2i除去、夜景i2i（黒レイヤー乗算）、輝度彩度LoRAでピンク抑制。LLMエロ小説（Gemma>Claude）、TRPG（SillyTavern GM分担）。
- **規制回避**: ローカル信仰、無検閲CLIP、Civitaiロリフィルタ調整。fanza AI漫画絶賛もマスピ抜け悪。

## 5. 動画/音声/LLM動向
- **動画**: HappyHorse商用可予定、Wan2.2髪揺れ◎もアナルガバ、LTX/SmoothMix後継待ち。アニメアクション短参照+i2i希望。
- **音声**: Emoji-TTS/VoiceDesign旧版推奨、Irodori-TTS連携。
- **LLM/SillyTavern**: Gemma4+表情差分/キャラカードでチャット+挿絵+音声。コンテキスト8k、変数展開（[age]18）。Open-LLM-VTuber話題。

## 6. コミュニティトレンドと洞察
- **ローカルシフト**: 無料/カスタム自由でクラウド避け。「人類赤ちゃん化」「置いていかれる」嘆きもTips共有文化強い（アンテナ高ニキ感謝）。
- **進化速度**: 小出し公開賛否、開発者擁護（寄付不要）。反AI「口だけ」認定。
- **懸念**: VRAM限界、NSFW除外、Civitai規制強化、プロンプト丸投げ。
- **将来展望**: Anima正式版/ControlNet/wai安定版、HappyHorseローカルエロLoRA、VLモデルRP、AIクローン。ローカル→クラウド移行予測も抵抗。
- **全体傾向**: Anima3普及兆し（SDXL沈み）。エロ哲学化（「究極のえっち」）と実践熱高。生成実験増加、次スレでLoRA/動画/Anima安定化予想。

## 7. 新規ユーザー推奨アクション
- **即DL/試す**: Anima preview3/CottonAnima、Gemma4-26B A4B（12GB VRAM可）+SillyTavern。
- **優先Tips**: 絵師`@artist`+`[A|B]`、score_7、1024 LoRA、ComfyUI BasicPipeトグル。README/AI相談時は詳細入力。
- **注意**: Civitaiブックマーク更新、HappyHorse偽サイト回避、元ログ詳細確認。
- **環境下限**: CPU e2b可、RTX3060tiで実用。

このレポートは重複除去・統合版。進化早いスレのエッセンス抽出。ローカルエロ生成の「実戦マニュアル」として活用を。
