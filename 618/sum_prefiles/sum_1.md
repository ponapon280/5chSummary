# なんJ AI生成スレッド（レス4-323）レポート

## 概要
このログは、AI画像・動画生成に特化したなんJスレッドの抜粋（主にレス4〜323）。参加者たちはComfyUI、A1111、reforgeなどのツールを使い、Z-image/ZIB、QwenVL、PainterAI2V、HeartMulaなどのモデルで生成実験を共有。LoRA学習、VRAM最適化、プロンプト生成などのテクニック議論が中心。後半でスレ荒らし（デブ画像連投など）が発生し、NG設定共有へシフト。全体としてローカル環境の試行錯誤と次世代モデル（ZIB）の期待が高く、クラウドAPI（Grok）の話題も散見。ゲーム放置や選挙の雑談も混在。

## 主要トピック別まとめ

### 1. 画像生成関連
- **モデル/ツールの活用**:
  - Z-image/ZIB: 強化学習なしでクリエイティブ向き。LoRA学習（musubi-tuner使用、学習率5e-4、dim16推奨）が活発。noob LoRAの高クオリティを評価し、CN（ControlNet）や二段samplerで構図制御提案。SDXL後継候補として将来性高く評価（エロチューン待ち）。
  - QwenVL/Qwen3-VL: 画像→プロンプト生成に優秀（Thinking版は小モデルでポンコツ）。NSFWキャプション対応GGUF版使用もVRAM右肩上がり問題報告。
  - Janus-Pro、trinart2: 古モデル再利用（プロンプト生成→ZI hires fix）。
  - その他: HeartMula（歌詞英訳でMV風）、grok imagine video API（480p1秒0.05ドル、安いが課金消耗早い）。

- **テクニック**:
  - LoRA領域描き分け: detaler segsでpersonマスク+個別適用提案。
  - Hires fix: ModelSamplingAuraFlow shift値（6/9/24）実験。
  - プロンプト: 画風指定必須（女体化回避）。自然言語で構図自由度高く。

- **生成例共有**: メカ娘再現、元素法典風プロンプト、flat/boldline LoRA（sdxl2-flat2-512b現役）。

### 2. 動画生成関連
- **ツール/モデル**:
  - PainterAI2V: 最終フレーム荒れ問題（エンドイメージ指定時）。FLF（First-Last Frame）2Vの色変わり/モザイク報告。InfiniteTalkでリップシンク改善提案（Wan2.2使用）。
  - Wan2.2/Wan2.1: マーライオン減少も「満面の笑み病」発生。after anal i2vで余韻動画（3秒繋ぎ/SVIモデル切り替え提案）。
  - LTX2: アジア人顔崩れ（LoRA苦戦）。MMUAUDIO（アニメNSFW声モデル待ち）。
  - Grok API: モデゆるくエロOK、日本語音声向上もmotion amplitude高めで大袈裟。

- **課題**: ピストン遅延、動きガチャ、API料金高（15秒4本で$5尽き）。

### 3. 環境構築・最適化
- **推奨環境**:
  - ComfyUI > A1111（化石、重い、v-pred非対応）。reforgeでVRAM削減（12GB medram有効）。
  - WSL2: 5090移行で一から構築報告。Stability Matrixで復元。
  - カスタムノード: ComfyUI-QwenVL（自動DL）、musubi-tuner（convert_lora.py注意）。
  - VRAM対策: --full_bf16（b2限界）、sageattention/fastでqwen/Z-image死。gguf vs fp8（lowvram時gguf速い場合あり）。

- **移行アドバイス**: A1111 devブランチ/Forge/Neo推奨。チャッピー相談でスペック診断。

### 4. トラブルシューティング
| 問題 | 原因/解決策 |
|------|-------------|
| VRAM右肩上がり（QwenVL GGUF） | llama.cpp問題？ Load Image Dataset from Folder/バッチ処理代替。 |
| 出力荒れ（PainterAI2V） | 最終4フレーム破棄/繋ぎ。 |
| プロンプト切れ | max_tokens=2048でも限界。 |
| susamix v3/vpred1黒画像 | A1111非対応→reforge/Advanced Model Sampling。 |
| LoRA効き弱 | Z-image特有、強度2.0必要。 |
| enbフォルダ肥大 | カスタムノード61個残骸。 |

- 全体: 土日限定ユーザー多し。チャッピー/Gemini相談有効。

### 5. 雑談・コミュニティ問題
- **懐古**: 元素法典、waifuDiffusion、フラット革命（flat LoRA-適用でディテール追加）、abyss orange mix。
- **選挙/オフ**: 期日前投票呼びかけ（民主主義嫌い反論）。
- **荒らし**: デブ画像連投→新芽/画像NG（chmate json共有）。負のフィードバック/自演疑惑。自画自賛批判も。
- **クラウド vs ローカル**: pollo.ai夜逃げ疑い（クレカ停止推奨）。Illustrious/wai FT待ち。

## トレンド・展望
- **ホットモデル**: ZIB（SDXL超え期待、エロ/LoRA現実的）。musubi-tunerでFT加速。
- **シフト**: A1111卒業→ComfyUI/reforge。動画はPainter/Wan2.2中心。
- **課題**: ベースブレ大、VRAM/互換性。エロ強化モデル/アジア人対応待ち。
- **コミュニティ**: 共有精神強いが荒らし耐性強化（NGファイル流通）。

総レス約200超、生成共有活発。次スレ期待: ZIBエロチューン、wai FT進捗。