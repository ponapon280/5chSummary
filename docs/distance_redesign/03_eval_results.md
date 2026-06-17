# distance.py 新設計 オフライン検証結果

> 自動生成: docs/distance_redesign/prototype_eval.py
> 対象スレ: 654, 655, 656, 657, 658, 659（各スレはそれ以前のスレのみを窓に使用＝リークなし）

> 既定パラメータ: N=6, r={'sum.md': 0.15, 'mod.md': 0.15, 'tools.md': 0.06}, SAT=0.5
> legacy閾値: sum/mod=0.07, tools=0.02（現行コード準拠）


---
## sum.md  （collection: 5ch_summaries）

### 既定パラメータ（N=6, r=0.15, SAT=0.5）でのスレ別比較

| thread | legacy新規 | rec:new | rec:emerging | rec:除外(飽和) | rec採用計 | Anima採用(legacy→rec) |
|---|---|---|---|---|---|---|
| 654 | 16 | 3 | 2 | 11 | 5 | 2 → 0 |
| 655 | 11 | 1 | 4 | 8 | 5 | 2 → 1 |
| 656 | 11 | 1 | 1 | 11 | 2 | 4 → 0 |
| 657 | 17 | 1 | 7 | 9 | 8 | 5 → 1 |
| 658 | 18 | 2 | 2 | 15 | 4 | 4 → 0 |
| 659 | 17 | 1 | 6 | 11 | 7 | 3 → 0 |

### 659 パラメータ感度（採用計 / Anima採用 / 既知新規ヒット）

| N | r | SAT | 採用計 | Anima採用 | 既知新規ヒット |
|---|---|---|---|---|---|
| 4 | 0.1 | 0.4 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.1 | 0.5 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.1 | 0.6 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.1 | 0.8 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.1 | 1.0 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.15 | 0.4 | 5 | 0 | 2 (plamo,llm-jp) |
| 4 | 0.15 | 0.5 | 5 | 0 | 2 (plamo,llm-jp) |
| 4 | 0.15 | 0.6 | 7 | 0 | 5 (ideogram,fable,mythos,plamo,llm-jp) |
| 4 | 0.15 | 0.8 | 10 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.15 | 1.0 | 10 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 4 | 0.2 | 0.4 | 0 | 0 | 0 |
| 4 | 0.2 | 0.5 | 0 | 0 | 0 |
| 4 | 0.2 | 0.6 | 0 | 0 | 0 |
| 4 | 0.2 | 0.8 | 0 | 0 | 0 |
| 4 | 0.2 | 1.0 | 0 | 0 | 0 |
| 6 | 0.1 | 0.4 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.1 | 0.5 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.1 | 0.6 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.1 | 0.8 | 18 | 4 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.1 | 1.0 | 18 | 4 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.15 | 0.4 | 7 | 0 | 5 (ideogram,fable,mythos,plamo,llm-jp) |
| 6 | 0.15 | 0.5 | 7 | 0 | 5 (ideogram,fable,mythos,plamo,llm-jp) |
| 6 | 0.15 | 0.6 | 10 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.15 | 0.8 | 12 | 0 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.15 | 1.0 | 12 | 0 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 6 | 0.2 | 0.4 | 0 | 0 | 0 |
| 6 | 0.2 | 0.5 | 0 | 0 | 0 |
| 6 | 0.2 | 0.6 | 0 | 0 | 0 |
| 6 | 0.2 | 0.8 | 0 | 0 | 0 |
| 6 | 0.2 | 1.0 | 0 | 0 | 0 |
| 8 | 0.1 | 0.4 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.1 | 0.5 | 17 | 3 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.1 | 0.6 | 18 | 4 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.1 | 0.8 | 18 | 4 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.1 | 1.0 | 18 | 4 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.15 | 0.4 | 10 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.15 | 0.5 | 10 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.15 | 0.6 | 11 | 0 | 6 (ideogram,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.15 | 0.8 | 12 | 0 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.15 | 1.0 | 13 | 1 | 7 (ideogram,seedance,gemma4,fable,mythos,plamo,llm-jp) |
| 8 | 0.2 | 0.4 | 0 | 0 | 0 |
| 8 | 0.2 | 0.5 | 0 | 0 | 0 |
| 8 | 0.2 | 0.6 | 0 | 0 | 0 |
| 8 | 0.2 | 0.8 | 0 | 0 | 0 |
| 8 | 0.2 | 1.0 | 1 | 0 | 0 |

#### 659 チャンク別 再出現スレ数（N=6, 窓=['658', '657', '656', '655', '654', '653']）

| rec@0.1 | rec@0.15 | Anima | 既知新規 | チャンク |
|---|---|---|---|---|
| 4 | 6 | ● |  | 【見出し: スレッド概要】 本スレッドは、Anima系モデルを中心としたアニメ調画像生成を軸に、ComfyU |
| 0 | 3 |  | ideogram | 【見出し: Ideogram 4関連の新情報】 専用VAE（Liquid9745VAEに近いビビット寄りピン |
| 0 | 2 |  | ideogram | 【見出し: Ideogram 4関連の新情報】 編集機能（edit）の正式実装を強く待望する声が多数で、「e |
| 0 | 3 |  | ideogram | 【見出し: Ideogram 4関連の新情報】 VRAM 12GB環境での動作報告があり、DynamicVR |
| 0 | 1 |  |  | 【見出し: 動画・音声生成の新ワークフロー】 LTX2.3 + MMAUDIO + Irodori-TTSの |
| 0 | 4 |  | ideogram,seedance | 【見出し: 動画・音声生成の新ワークフロー】 Seedance2.0（特にNSFWファインチューン版）が動画 |
| 0 | 0 |  |  | 【見出し: 動画・音声生成の新ワークフロー】 sousaku.ai（ByteDance系とされるサービス）が |
| 0 | 6 |  |  | 【見出し: LoRA学習・プロンプトの新Tips】 512px vs 1024pxの解像度論争が継続する中、 |
| 0 | 6 | ● |  | 【見出し: LoRA学習・プロンプトの新Tips】 Animaの自然言語対応力の高さが再確認され、「中学英語 |
| 0 | 2 |  |  | 【見出し: コミュニティ・運用ルールに関する新議論】 FANZA・pixivでのAI未申告投稿に対する「通報 |
| 0 | 1 |  |  | 【見出し: コミュニティ・運用ルールに関する新議論】 画像管理ツールとしてInfinite Image Br |
| 0 | 2 |  | fable,mythos | 【見出し: 規制・国内AIに関する新話題】 Anthropic系新モデル（Fable 5 / Mythos  |
| 0 | 1 |  | plamo,llm-jp | 【見出し: 規制・国内AIに関する新話題】 PLaMo（Preferred Networks）やLLM-jp |
| 1 | 6 | ● |  | 【見出し: 技術的知見（統合・整理）】 Anima / hakushiMixAnima / Wai-Anim |
| 0 | 4 |  |  | 【見出し: 技術的知見（統合・整理）】 ComfyUI：Save Image Extendedのwebp互換 |
| 0 | 3 |  | gemma4 | 【見出し: 技術的知見（統合・整理）】 LLM活用：Gemma4-31Bが日本語エロ・プロンプト生成で強い一 |
| 0 | 6 |  |  | 【見出し: 全体の空気感】 情報共有は活発だが、単なる生成自慢ではなく「AIはツールで人間次第」「漫画制作の |
| 1 | 6 | ● |  | 【見出し: 全体の空気感】 （前回・前々回スレッドで繰り返し登場したAnimaの基本評価やComfyUIの基 |

### 659 既定パラメータの定性内訳（窓=['658', '657', '656', '655', '654', '653'], r=0.15, 飽和閾値=3スレ）

**除外（飽和）と判定されたチャンク:**
- 【見出し: スレッド概要】 本スレッドは、Anima系モデルを中心としたアニメ調画像生成を軸に、ComfyUIワークフロー、LoRA学習、動画生成、LLM活用を
- 【見出し: Ideogram 4関連の新情報】 専用VAE（Liquid9745VAEに近いビビット寄りピンク強調型）が共有され、「Ideogram4用に追加学
- 【見出し: Ideogram 4関連の新情報】 VRAM 12GB環境での動作報告があり、DynamicVRAMやGGUF形式の活用が背景として語られた。
- 【見出し: 動画・音声生成の新ワークフロー】 Seedance2.0（特にNSFWファインチューン版）が動画生成で高評価。Ideogram4生成キャラとの組み合
- 【見出し: LoRA学習・プロンプトの新Tips】 512px vs 1024pxの解像度論争が継続する中、MLP層を抜く設定（ParamGui）で画風LoRA
- 【見出し: LoRA学習・プロンプトの新Tips】 Animaの自然言語対応力の高さが再確認され、「中学英語レベルでも直接記述可能」という声が増加。一方で複数人
- 【見出し: 技術的知見（統合・整理）】 Anima / hakushiMixAnima / Wai-Anima：現時点の主力。dynamic poseや自然言語
- 【見出し: 技術的知見（統合・整理）】 ComfyUI：Save Image Extendedのwebp互換性問題や、Gemma系翻訳ノードを活用したNSFWプ
- 【見出し: 技術的知見（統合・整理）】 LLM活用：Gemma4-31Bが日本語エロ・プロンプト生成で強い一方、Qwen系はコーディング寄り。用途別棲み分け（C
- 【見出し: 全体の空気感】 情報共有は活発だが、単なる生成自慢ではなく「AIはツールで人間次第」「漫画制作のネーム・コマ割りはまだ人力が強い」といった現実的な指
- 【見出し: 全体の空気感】 （前回・前々回スレッドで繰り返し登場したAnimaの基本評価やComfyUIの基礎的な使い方、GPU買い替え議論の基本部分は省略）

**採用（new/emerging）チャンク:**
- [emerging] 【見出し: Ideogram 4関連の新情報】 編集機能（edit）の正式実装を強く待望する声が多数で、「edit来たらゲームエンド」との意見が目立った。
- [emerging] 【見出し: 動画・音声生成の新ワークフロー】 LTX2.3 + MMAUDIO + Irodori-TTSの組み合わせによるリップシンク＋効果音抽出の実例が投稿
- [new] 【見出し: 動画・音声生成の新ワークフロー】 sousaku.ai（ByteDance系とされるサービス）が無検閲寄りとして注目された。
- [emerging] 【見出し: コミュニティ・運用ルールに関する新議論】 FANZA・pixivでのAI未申告投稿に対する「通報運動」の必要性が強く主張され、規制強化前の自主的な棲
- [emerging] 【見出し: コミュニティ・運用ルールに関する新議論】 画像管理ツールとしてInfinite Image Browser、Smart Gallery、Diffus
- [emerging] 【見出し: 規制・国内AIに関する新話題】 Anthropic系新モデル（Fable 5 / Mythos 5）の外国人アクセス禁止（輸出規制）に関する情報がス
- [emerging] 【見出し: 規制・国内AIに関する新話題】 PLaMo（Preferred Networks）やLLM-jpへの言及もあったが、「予算の中抜き」や「驚き屋の少な

---
## mod.md  （collection: 5ch_ai_models）

### 既定パラメータ（N=6, r=0.15, SAT=0.5）でのスレ別比較

| thread | legacy新規 | rec:new | rec:emerging | rec:除外(飽和) | rec採用計 | Anima採用(legacy→rec) |
|---|---|---|---|---|---|---|
| 654 | 12 | 4 | 0 | 9 | 4 | 3 → 0 |
| 655 | 7 | 0 | 0 | 13 | 0 | 6 → 0 |
| 656 | 10 | 0 | 0 | 15 | 0 | 3 → 0 |
| 657 | 13 | 0 | 0 | 19 | 0 | 4 → 0 |
| 658 | 13 | 0 | 1 | 16 | 1 | 2 → 0 |
| 659 | 10 | 2 | 0 | 9 | 2 | 3 → 0 |

### 659 パラメータ感度（採用計 / Anima採用 / 既知新規ヒット）

| N | r | SAT | 採用計 | Anima採用 | 既知新規ヒット |
|---|---|---|---|---|---|
| 4 | 0.1 | 0.4 | 10 | 3 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 4 | 0.1 | 0.5 | 10 | 3 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 4 | 0.1 | 0.6 | 10 | 3 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 4 | 0.1 | 0.8 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 4 | 0.1 | 1.0 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 4 | 0.15 | 0.4 | 2 | 0 | 2 (hidream,hotgen) |
| 4 | 0.15 | 0.5 | 2 | 0 | 2 (hidream,hotgen) |
| 4 | 0.15 | 0.6 | 2 | 0 | 2 (hidream,hotgen) |
| 4 | 0.15 | 0.8 | 2 | 0 | 2 (hidream,hotgen) |
| 4 | 0.15 | 1.0 | 2 | 0 | 2 (hidream,hotgen) |
| 4 | 0.2 | 0.4 | 0 | 0 | 0 |
| 4 | 0.2 | 0.5 | 0 | 0 | 0 |
| 4 | 0.2 | 0.6 | 0 | 0 | 0 |
| 4 | 0.2 | 0.8 | 0 | 0 | 0 |
| 4 | 0.2 | 1.0 | 0 | 0 | 0 |
| 6 | 0.1 | 0.4 | 10 | 3 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 6 | 0.1 | 0.5 | 10 | 3 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 6 | 0.1 | 0.6 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 6 | 0.1 | 0.8 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 6 | 0.1 | 1.0 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 6 | 0.15 | 0.4 | 2 | 0 | 2 (hidream,hotgen) |
| 6 | 0.15 | 0.5 | 2 | 0 | 2 (hidream,hotgen) |
| 6 | 0.15 | 0.6 | 2 | 0 | 2 (hidream,hotgen) |
| 6 | 0.15 | 0.8 | 3 | 0 | 4 (fable,mythos,hidream,hotgen) |
| 6 | 0.15 | 1.0 | 7 | 2 | 9 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,plamo,llm-jp) |
| 6 | 0.2 | 0.4 | 0 | 0 | 0 |
| 6 | 0.2 | 0.5 | 0 | 0 | 0 |
| 6 | 0.2 | 0.6 | 0 | 0 | 0 |
| 6 | 0.2 | 0.8 | 0 | 0 | 0 |
| 6 | 0.2 | 1.0 | 0 | 0 | 0 |
| 8 | 0.1 | 0.4 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.1 | 0.5 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.1 | 0.6 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.1 | 0.8 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.1 | 1.0 | 11 | 4 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.15 | 0.4 | 2 | 0 | 2 (hidream,hotgen) |
| 8 | 0.15 | 0.5 | 2 | 0 | 2 (hidream,hotgen) |
| 8 | 0.15 | 0.6 | 2 | 0 | 2 (hidream,hotgen) |
| 8 | 0.15 | 0.8 | 5 | 1 | 6 (ideogram,gemma4,fable,mythos,hidream,hotgen) |
| 8 | 0.15 | 1.0 | 8 | 2 | 10 (ideogram,seedance,gemma4,fable,mythos,hidream,hotgen,rouwei,plamo,llm-jp) |
| 8 | 0.2 | 0.4 | 0 | 0 | 0 |
| 8 | 0.2 | 0.5 | 0 | 0 | 0 |
| 8 | 0.2 | 0.6 | 0 | 0 | 0 |
| 8 | 0.2 | 0.8 | 0 | 0 | 0 |
| 8 | 0.2 | 1.0 | 0 | 0 | 0 |

#### 659 チャンク別 再出現スレ数（N=6, 窓=['658', '657', '656', '655', '654', '653']）

| rec@0.1 | rec@0.15 | Anima | 既知新規 | チャンク |
|---|---|---|---|---|
| 3 | 6 | ● | ideogram,seedance,gemma4 | 【モデル: 流行モデルの概要】 今回の抽出テキスト群から、Ideogram4（および派生）、Gemma4系（ |
| 1 | 5 |  | ideogram | 【モデル: Ideogram4（Ideogram4.0 / Realism Engine Ideogram  |
| 0 | 5 |  | seedance | 【モデル: seedance2.0】 動画生成モデルとして新たに注目を集めています。「到達しとるね」「エロフ |
| 0 | 5 | ● | gemma4 | 【モデル: Gemma4系（Gemma4-26B-A4B、DiffusionGemma、HauhauCS版な |
| 0 | 4 |  | fable,mythos | 【モデル: Fable5 / Mythos 5（Anthropic系有料モデル）】 従量課金型の高性能モデル |
| 0 | 0 |  | hidream | 【モデル: その他の新・変化モデル】 HiDream-E1/O1: 画像編集用途で言及。Edit機能に特化し |
| 0 | 0 |  | hotgen | 【モデル: その他の新・変化モデル】 Hotgen Video V5: 動画生成の新モデルとしてNSFW許容 |
| 1 | 6 |  | gemma4,rouwei | 【モデル: その他の新・変化モデル】 Rouwei（Rouwei-Gemma4）: 非検閲キャプションモデル |
| 0 | 5 | ● | plamo,llm-jp | 【モデル: その他の新・変化モデル】 PLaMo / LLM-jp: 国産LLMとして日本語性能とAnima |
| 1 | 6 | ● |  | 【モデル: 変化の少ないモデル（省略）】 Anima、illustrious、NovelAI、FLUX、WA |
| 0 | 6 |  |  | 【モデル: 変化の少ないモデル（省略）】 全体として、編集・動画・ローカル効率という軸でモデル選択がシフトし |

### 659 既定パラメータの定性内訳（窓=['658', '657', '656', '655', '654', '653'], r=0.15, 飽和閾値=3スレ）

**除外（飽和）と判定されたチャンク:**
- 【モデル: 流行モデルの概要】 今回の抽出テキスト群から、Ideogram4（および派生）、Gemma4系（特にMoE版）、seedance2.0（動画）、Cl
- 【モデル: Ideogram4（Ideogram4.0 / Realism Engine Ideogram 4 V2）】 複数ログで積極的に検証されており、特に
- 【モデル: seedance2.0】 動画生成モデルとして新たに注目を集めています。「到達しとるね」「エロファインチューン」との評価があり、NSFW対応の強みと
- 【モデル: Gemma4系（Gemma4-26B-A4B、DiffusionGemma、HauhauCS版など）】 ローカル運用での言及が急増しています。MoE
- 【モデル: Fable5 / Mythos 5（Anthropic系有料モデル）】 従量課金型の高性能モデルとして情報格差の文脈で登場。「一発で成功しやすい」「
- 【モデル: その他の新・変化モデル】 Rouwei（Rouwei-Gemma4）: 非検閲キャプションモデルとして4月公開の新モデルがタグ付け用途で評価。
- 【モデル: その他の新・変化モデル】 PLaMo / LLM-jp: 国産LLMとして日本語性能とAnima構文との相性が指摘され、自立的な選択肢として新たに注
- 【モデル: 変化の少ないモデル（省略）】 Anima、illustrious、NovelAI、FLUX、WAN、Qwen-Image、Z-Image、LTX系は
- 【モデル: 変化の少ないモデル（省略）】 全体として、編集・動画・ローカル効率という軸でモデル選択がシフトしているのが今回の特徴です。

**採用（new/emerging）チャンク:**
- [new] 【モデル: その他の新・変化モデル】 HiDream-E1/O1: 画像編集用途で言及。Edit機能に特化した点が理由。
- [new] 【モデル: その他の新・変化モデル】 Hotgen Video V5: 動画生成の新モデルとしてNSFW許容を売りに登場。

---
## tools.md  （collection: 5ch_tools）

### 既定パラメータ（N=6, r=0.06, SAT=0.5）でのスレ別比較

| thread | legacy新規 | rec:new | rec:emerging | rec:除外(飽和) | rec採用計 | Anima採用(legacy→rec) |
|---|---|---|---|---|---|---|
| 654 | 15 | 15 | 0 | 0 | 15 | 0 → 0 |
| 655 | 21 | 21 | 0 | 0 | 21 | 2 → 2 |
| 656 | 21 | 21 | 0 | 0 | 21 | 5 → 5 |
| 657 | 16 | 15 | 1 | 0 | 16 | 0 → 0 |
| 658 | 22 | 21 | 1 | 0 | 22 | 0 → 0 |
| 659 | 17 | 15 | 2 | 0 | 17 | 3 → 3 |

### 659 パラメータ感度（採用計 / Anima採用 / 既知新規ヒット）

| N | r | SAT | 採用計 | Anima採用 | 既知新規ヒット |
|---|---|---|---|---|---|
| 4 | 0.04 | 0.4 | 17 | 3 | 0 |
| 4 | 0.04 | 0.5 | 17 | 3 | 0 |
| 4 | 0.04 | 0.6 | 17 | 3 | 0 |
| 4 | 0.04 | 0.8 | 17 | 3 | 0 |
| 4 | 0.04 | 1.0 | 17 | 3 | 0 |
| 4 | 0.06 | 0.4 | 16 | 3 | 0 |
| 4 | 0.06 | 0.5 | 16 | 3 | 0 |
| 4 | 0.06 | 0.6 | 17 | 3 | 0 |
| 4 | 0.06 | 0.8 | 17 | 3 | 0 |
| 4 | 0.06 | 1.0 | 17 | 3 | 0 |
| 4 | 0.08 | 0.4 | 15 | 3 | 0 |
| 4 | 0.08 | 0.5 | 15 | 3 | 0 |
| 4 | 0.08 | 0.6 | 17 | 3 | 0 |
| 4 | 0.08 | 0.8 | 17 | 3 | 0 |
| 4 | 0.08 | 1.0 | 17 | 3 | 0 |
| 6 | 0.04 | 0.4 | 17 | 3 | 0 |
| 6 | 0.04 | 0.5 | 17 | 3 | 0 |
| 6 | 0.04 | 0.6 | 17 | 3 | 0 |
| 6 | 0.04 | 0.8 | 17 | 3 | 0 |
| 6 | 0.04 | 1.0 | 17 | 3 | 0 |
| 6 | 0.06 | 0.4 | 17 | 3 | 0 |
| 6 | 0.06 | 0.5 | 17 | 3 | 0 |
| 6 | 0.06 | 0.6 | 17 | 3 | 0 |
| 6 | 0.06 | 0.8 | 17 | 3 | 0 |
| 6 | 0.06 | 1.0 | 17 | 3 | 0 |
| 6 | 0.08 | 0.4 | 17 | 3 | 0 |
| 6 | 0.08 | 0.5 | 17 | 3 | 0 |
| 6 | 0.08 | 0.6 | 17 | 3 | 0 |
| 6 | 0.08 | 0.8 | 17 | 3 | 0 |
| 6 | 0.08 | 1.0 | 17 | 3 | 0 |
| 8 | 0.04 | 0.4 | 17 | 3 | 0 |
| 8 | 0.04 | 0.5 | 17 | 3 | 0 |
| 8 | 0.04 | 0.6 | 17 | 3 | 0 |
| 8 | 0.04 | 0.8 | 17 | 3 | 0 |
| 8 | 0.04 | 1.0 | 17 | 3 | 0 |
| 8 | 0.06 | 0.4 | 17 | 3 | 0 |
| 8 | 0.06 | 0.5 | 17 | 3 | 0 |
| 8 | 0.06 | 0.6 | 17 | 3 | 0 |
| 8 | 0.06 | 0.8 | 17 | 3 | 0 |
| 8 | 0.06 | 1.0 | 17 | 3 | 0 |
| 8 | 0.08 | 0.4 | 17 | 3 | 0 |
| 8 | 0.08 | 0.5 | 17 | 3 | 0 |
| 8 | 0.08 | 0.6 | 17 | 3 | 0 |
| 8 | 0.08 | 0.8 | 17 | 3 | 0 |
| 8 | 0.08 | 1.0 | 17 | 3 | 0 |

#### 659 チャンク別 再出現スレ数（N=6, 窓=['658', '657', '656', '655', '654', '653']）

| rec@0.06 | rec@0.08 | Anima | 既知新規 | チャンク |
|---|---|---|---|---|
| 2 | 2 |  |  | 【ツール: Forge Neo（前回比で位置づけ変化）】 前回までComfyUIが主流だったワークフロー環境 |
| 0 | 0 | ● |  | 【ツール: Forge Neo（前回比で位置づけ変化）】 reforgeとの差別化：Forge NeoはZ- |
| 0 | 0 |  |  | 【ツール: Forge Neo（前回比で位置づけ変化）】 注意点の新出：生成時間が徐々に伸びる現象が報告され |
| 0 | 1 |  |  | 【ツール: Forge Neo（前回比で位置づけ変化）】 初心者向けUIの使いやすさやSageAttenti |
| 1 | 2 |  |  | 【ツール: 新規登場・注目されたツール】 以下のツールは今回の抽出で初めて具体的な言及・評価が見られたもの： |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 Animerge |
| 0 | 0 | ● |  | 【ツール: 新規登場・注目されたツール】 Animaモデルをレイヤー単位でマージ・分析できる総合ツールとして |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 Unsloth Studio / LMStudio + llama |
| 0 | 0 | ● |  | 【ツール: 新規登場・注目されたツール】 12GB VRAM環境（RTX 4070/5070など）でGemm |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 Hotgen Video V5 |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 NSFW対応を売りにした動画生成ツールとして初登場。seedanc |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 画像管理ツール群の再検討 |
| 0 | 0 |  |  | 【ツール: 新規登場・注目されたツール】 ComfyUI-Image-Browserの重さに対する不満から、 |
| 0 | 0 |  |  | 【ツール: 継続的に変化が見られるツール】 IdeogramHelper系：Kijai氏版とは別の「アプリっ |
| 0 | 0 |  |  | 【ツール: 継続的に変化が見られるツール】 leco学習UI：ADDifT（2枚の画像差分のみを学習する機能 |
| 0 | 0 |  |  | 【ツール: 継続的に変化が見られるツール】 Qwen（非画像生成用途）：ローカルLLMとしてのプロンプト生成 |
| 0 | 1 |  |  | 【ツール: まとめ】 前回までのComfyUI中心の流れに対し、Forge Neoの台頭とAnimerge・ |

### 659 既定パラメータの定性内訳（窓=['658', '657', '656', '655', '654', '653'], r=0.06, 飽和閾値=3スレ）

**除外（飽和）と判定されたチャンク:**
- （なし）

**採用（new/emerging）チャンク:**
- [emerging] 【ツール: Forge Neo（前回比で位置づけ変化）】 前回までComfyUIが主流だったワークフロー環境において、Forge Neoが新たに有力な選択肢とし
- [new] 【ツール: Forge Neo（前回比で位置づけ変化）】 reforgeとの差別化：Forge NeoはZ-Image turboやQwen、Animaなど最近
- [new] 【ツール: Forge Neo（前回比で位置づけ変化）】 注意点の新出：生成時間が徐々に伸びる現象が報告され、長期運用時の監視が必要とされるようになった。
- [new] 【ツール: Forge Neo（前回比で位置づけ変化）】 初心者向けUIの使いやすさやSageAttention2/FlashAttentionのデフォルト最適
- [emerging] 【ツール: 新規登場・注目されたツール】 以下のツールは今回の抽出で初めて具体的な言及・評価が見られたもの：
- [new] 【ツール: 新規登場・注目されたツール】 Animerge
- [new] 【ツール: 新規登場・注目されたツール】 Animaモデルをレイヤー単位でマージ・分析できる総合ツールとして登場。階層ごとの細かい制御が可能で、多言語化などの拡
- [new] 【ツール: 新規登場・注目されたツール】 Unsloth Studio / LMStudio + llama-serverの組み合わせ
- [new] 【ツール: 新規登場・注目されたツール】 12GB VRAM環境（RTX 4070/5070など）でGemma系モデルを量子化ロードしながらAnima生成を行う
- [new] 【ツール: 新規登場・注目されたツール】 Hotgen Video V5
- [new] 【ツール: 新規登場・注目されたツール】 NSFW対応を売りにした動画生成ツールとして初登場。seedance2.0並みの性能を謳い、クローズドモデル蒸留の可能
- [new] 【ツール: 新規登場・注目されたツール】 画像管理ツール群の再検討
- [new] 【ツール: 新規登場・注目されたツール】 ComfyUI-Image-Browserの重さに対する不満から、Infinite Image Browser（スタン
- [new] 【ツール: 継続的に変化が見られるツール】 IdeogramHelper系：Kijai氏版とは別の「アプリっぽいUI」の新ノードが登場し、扱いやすさが指摘された
- [new] 【ツール: 継続的に変化が見られるツール】 leco学習UI：ADDifT（2枚の画像差分のみを学習する機能）の実装完了が報告され、差分学習需要に対応した動きが
- [new] 【ツール: 継続的に変化が見られるツール】 Qwen（非画像生成用途）：ローカルLLMとしてのプロンプト生成・コーディング・小説執筆用途が新たに複数確認され、G
- [new] 【ツール: まとめ】 前回までのComfyUI中心の流れに対し、Forge Neoの台頭とAnimerge・Unsloth Studioなどの新ツール登場により