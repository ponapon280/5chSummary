# 🆕 新規トピック（前回からの差分）
- **Anima**: CircleStone Labs開発のアニメ・イラスト特化型画像生成モデル（2026年リリース）
- **Forge Neo**: ComfyUIよりシンプルで柔軟な画像・ビデオ生成アプリ
- **A1111 (Stable Diffusion webUI)**: 漫画制作等に利用される旧来の環境
- **EasyAnima**: 初心者向け導入ツール
- **kohya_ss / kohya_lora_param_gui**: LoRA作成ツール（Anima対応版あり）
- **sd-scripts**: RAdamScheduleFree設定推奨のLoRA学習スクリプト
- **AI-Toolkit**: LoRA学習用トレーナー
- **TIPO / anima-tagger / Tagger**: 自動タグ生成および自然言語プロンプト生成ツール
- **TensorBoard**: 学習ログの可視化・分析ツール
- **LM Studio**: Qwen等のモデルを用いた英文画像説明文生成環境
- **ollama / llama.cpp**: メモリ管理およびRadeon GPU対応のLLM実行環境
- **Grok**: 規制の緩い成人向けプロンプト作成用LLM
- **ChatGPT**: プロンプト作成、スクリプト作成、エラー解析用LLM
- **Gemini**: 説明イラスト作成およびタグ付け用LLM
- **Photoshop / PhotoRoom**: 高精度背景透過・時短処理ツール
- **Krita**: 縦書き文字対応（v5.3〜）による漫画制作ツール
- **CLIP STUDIO PAINT**: テキスト追加・仕上げ用漫画制作ツール
- **Wai-Anima**: SAM3を利用可能なComfyUI用ワークフロー集


---
# 元の本文
## 生成AI関連ツールレポート

### 画像生成・編集ツール
#### ComfyUI (comfy)
- ワークフロー（wf）の共有・再現性が高く、カスタムノードによる高度な制御（構図やポーズ指定、LLM連携など）が可能なため、現在の主流環境として利用されている。
- 最新機能への対応が早いため、拡張性の観点から習得が推奨されている。
- 一方で、ワークフローの肥大化によるエラー箇所の特定困難さや、スマホ操作（listen機能）の不可といった課題も挙げられている。

#### Forge / Forge Neo
- Animaモデルを利用する際に「お手軽で機能が豊富」であるため推奨されている。
- 特にStability Matrix経由での導入が容易であり、A1111系に慣れているユーザーにとって導入ハードルが低い点が評価されている。

#### webUI (A1111) / Neoforge
- 漫画制作などの実用的な用途や、Attention Coupleなどの機能利用のために使用されている。
- Neoforgeは、ComfyUIよりも導入が容易であるとされている。

#### Ultimate SD Upscaler
- タイリングによるアップスケールに使用されるが、一部の環境（Anima等）では結果が「硬い」と感じられ、Latentアップスケールの方が好まれる傾向にある。

#### Photoshop / PhotoRoom / Krita / CLIP STUDIO PAINT
- 背景透過（切り抜き）において、PhotoshopやPhotoRoomの高い処理性能が評価されている。
- 漫画制作においては、縦書き文字への対応が進んだKritaや、テキスト追加が容易なCLIP STUDIO PAINTが利用されている。

### 学習・補助ツール
#### kohya_ss / kohya_lora_param_gui / sd-scripts
- LoRA学習の標準的なツールとして利用されており、特にフォーク版のsd-scriptsはiLECOやADDifTなどの特殊な学習への対応に使用されている。
- 自然言語キャプション作成スクリプトや、RAdamScheduleFreeなどのオプティマイザ設定に関する議論が行われている。

#### Stability Matrix
- ComfyUIやForgeなどの環境構築・管理を圧倒的に楽にするツールとして導入されている。

#### TIPO / anima-tagger
- タグの自動生成および、自然言語プロンプトへの変換作業を効率化するために利用されている。

#### TensorBoard
- 学習ログを図式化し、学習が正しく進行しているか（失敗していないか）を視覚的に把握するために活用されている。

### LLM・プロンプト生成ツール
#### LM Studio
- Qwenなどの大規模言語モデル（LLM）をローカルで動作させ、画像から詳細な英文説明（LoRA用キャプション）を生成させるために利用されている。
- VRAM管理のためのunload機能や、コンテキスト長の設定調整が行われている。

#### ChatGPT / Gemini / Grok
- プロンプトの作成や指示出しに使用されている。
- 特にGrokは規制が緩いため、成人向け（NSFW）プロンプトの作成に利用されており、Xプレミアム経由での利用がコストパフォーマンス面で推奨されている。
- Geminiについては、制限を解除（脱獄）して利用する方法が言及されている。

### 動画生成ツール
#### tensorhub / runpod (EROS)
- 利用はされているが、「質の低い動画しか作れない」といった否定的な評価が多く、コストに見合わないとの指摘がある。
