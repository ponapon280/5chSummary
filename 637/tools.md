# 🆕 新規トピック（前回からの差分）
- ComfyUIのunloadオプションによるLLM後自動VRAM解放と数百枚バッチ処理放置可
- Forge系のanima XY Plot対応と画像ドラッグWF解析（ComfyUI表示）
- Stability Matrixのmodels全削除履歴とQwen3-ASR/TTSテスト用複数環境管理
- nanoの20パターン立ち絵角度出し、学マス生成失敗例、ざっくり指示+修正活用
- webUIのRealESRGAN_x4Plus Anime 6B使用hires.fix/upscale 4倍負荷比較とsupermergerエラー
- LM Studioのqwen3.5-35b Thinking長問題とメモリ取り出し手間
- kohyaのfp8無効化LoRA学習プリセットとgemma改良ドスケベプロンプト
- ADetailerの乳首LoRA、yolo.pt/safeTensor/sam3読み込み、境界ボヤ設定難
- Qwen3-VL-8B-NSFW-Caption + llama-cpp-python（CPU推奨トラブルシュまとめ）とトークン暴走対策スクリプト
- その他ツールのlitVideo（seedance2.0待ち時間短縮）
- その他ツールの自作ツール（AIタグフィルター/leeyes代替、動画分割、Qwen暴走スクリプト、eagle読み込み不満解消で効率50倍）
- 全体傾向の総話題数約200件超（ComfyUI単独半数超、ログ後半安定議論深化）

---
# 元の本文
# 生成AI関連ツール抽出レポート

## 概要
提供されたログ（複数抽出結果統合）から、生成AI関連の「ツール」（インターフェース、拡張ノード、管理ツール、スクリプトなど）を抽出・整理。モデル（anima, illustrious/リアス, Wan, NAI, FLUX, LTX, Qwen-Imageなど）関連話題は除外。主なツールは**ComfyUI**が圧倒的に最多で、上級者向けの柔軟性・新機能対応が議論の中心。選好理由として**VRAM効率化**、**カスタムノード/WF容易さ**、**新機能対応速さ**、**安定管理**、**バグ耐性**などが頻出。初心者向け代替として**Forge Neo**や**Stability Matrix**が推奨される一方、バグ・アップデートトラブルも共通課題。自作ツール（Claude/ChatGPT活用）も増加傾向。

抽出ツール数は20種以上。以下、話題頻度順に分類・まとめ。各ツールの選好理由/利点は**太字**で強調。

## 主要ツール詳細

### 1. ComfyUI (comfy/comfyui) - 最多話題（全ログの70%以上）
   - **主な話題**: WF管理（XY Plot, グループ化, サブグラフ, 切り替えスイッチ）、ノード検索（latent拡大, Hキー掴むモードバグ）、アップデートトラブル（missing nodes, protobuf競合, git pullエラー, v0.19.0オシャカ）、カスタムノード（ComfyUI_Mira, prompt-control, QwenVL, llama-cpp_vlm, Klein, Dynamic Prompts, SAM3, WD14Tagger）、タグ付け（Qwen3-VL-NSFW-Caption + llama-cpp-python）、VRAM削減（App Mode + GeForce RTXで60%減）、API連携（LM Studio, 翻訳API）。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **新機能/モデル対応速い** | A1111より早い。新人でもCoreノードテンプレから始めやすい。 |
     | **カスタムノード/WF便利** | WF経由で大量ノードアクセス容易。Claudeに依頼で専用ノード作成（テキストボックス+トグルでワンクリック切り替え）。 |
     | **VRAM効率** | unloadオプションでLLM後自動解放。バッチ処理放置可（数百枚タグ付け）。 |
     | **柔軟性** | 領域指定（Create Tilling PNG Mask）、プロンプト制御（comfyui-prompt-control）。extra_model_paths.yamlでパス管理。 |


   - **欠点**: 上級者向け（敷居高）、アプデでノード死/エラー頻発（Coreノード推奨で回避）。

### 2. Forge Neo / reforge / Forge系
   - **主な話題**: anima XY Plot対応、ADetailer/FaceDetailerフォルダ管理、protobuf/tensorflow競合（WD14 Taggerインストールで発生）、WF解析（画像ドラッグでComfyUI表示）、単独インストール推奨。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **初心者/赤ちゃん向け簡単** | マウス領域指定、テンプレ使用でComfyUI不要。趣味程度なら最適。 |
     | **安定代替** | Stability Matrixバグ時単独インストールで使用可。アプデ死にくい。 |


   - **欠点**: カスタムノード/WF共有弱い、最新技術追従遅れ。

### 3. Stability Matrix
   - **主な話題**: uvバグ/起動失敗（旧版推奨）、models全削除履歴、アプデ死（ComfyUI新規インストール/pipエラー）、パス設定（extra_model_paths.yaml）、複数環境管理（Qwen3-ASR/TTSテスト用）。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **初心者管理ツール** | Packages/Data配下でモデル管理。ComfyUI/reforge/Forge Neo一括インストール。 |


   - **欠点**: バグ多発（データ消失リスク）、カスタム制限（アプデで死ぬ）→単独インストール推奨。

### 4. nano-banana (banana)
   - **主な話題**: 四コマ/立ち絵生成（20パターン角度出し）、学マス生成失敗例、ざっくり指示+修正。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **実用効率** | 四コマ実用範囲内、詳細指示不要で楽。LoRA学習効率化工程に活用。 |

### 5. webUI / A1111系
   - **主な話題**: hires.fix/upscale処理比較（RealESRGAN_x4Plus Anime 6Bで4倍負荷）、ADetailer設定難、supermergerエラー。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **シンプル優秀** | 高機能UIでComfyUI敷居上げる原因。設定記事豊富。 |

### 6. LM Studio
   - **主な話題**: シスプロ/Thinking設定（品質タグ省略、自然英語出力）、API連携（ComfyUIノードでWF完結）、メモリ取り出し手間、qwen3.5-35b Thinking長問題。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **連携容易** | ComfyUI APIでLLM+画像一元化、VRAM解放自動。 |

### 7. kohyaスクリプト / Kohya GUI
   - **主な話題**: キャプション付け（gemma改良でエロ対応強化）、LoRA学習プリセット（fp8無効化で効果）。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **エロ対応強化** | gemma相談でドスケベプロンプト改良。 |

### 8. ADetailer / FaceDetailer / detailer系
   - **主な話題**: 乳首LoRA、yolo.pt/safeTensor/sam3読み込み、フォルダ別管理（ForgeNeo/StabilityMatrix/ComfyUI）、境界ボヤ設定難。
   - **選好理由/利点**: 瞳グチャ/目つき対策（hiresガチャ代替）。

### 9. Qwenシリーズ (非画像生成: タグ付け/プロンプト解析)
   - **主な話題**: Qwen3-VL-8B-NSFW-Caption + ComfyUI/llama-cpp-python（CPU推奨、トラブルシュまとめ便利）、プロンプト英文吐き出し、システムプロンプトON/OFF使い分け、トークン暴走対策スクリプト。
   - **選好理由/利点**:


     | 理由 | 詳細 |
     |------|------|
     | **効率/精度** | 無検閲tagger優位、自然言語構築力強力。並列出力（WD14Tagger併用）。 |

### 10. その他ツール


   | ツール | 主な話題/選好理由 |
   |--------|-------------------|
   | **llama-cpp-python** | Qwenタグ付け環境構築鬼門（CPU楽）。 |
   | **claude (インストールツール)** | exe一発インストール、エラー直し。 |
   | **litVideo** | seedance2.0待ち時間短縮。 |
   | **自作ツール (Claude/ChatGPT/Copilot)** | 画像管理/検索（AIタグフィルター、leeyes代替）、動画分割、Qwen暴走スクリプト。**理由: 既存不満（eagle読み込み手間）で効率50倍**。 |
   | **krita / character_select_stand_alone_app / comfyui-prompt-control** | 領域指定ツール（3種のみ）。 |
   | **ollama / openRouter / nanoGPT** | VRAM不要SFW LLM、API紐付けでプロンプト+生成両立。 |
   | **irodori-tts** | エロ音声出力、ComfyUI代替。 |

## 全体傾向と洞察
- **選好トレンド**: ComfyUI中心（上級者移行推奨）だがトラブル多（アプデ/Coreノード固定）。初心者はForge Neo/Stability Matrixから。**自作増加**: Claude/ChatGPTでカスタムノード/ツール作成が標準化（効率化理由）。
- **共通課題**: アップデート死/競合（protobuf/tensorflow）、VRAM管理。
- **推奨パターン**: Stability MatrixでComfyUI+Forge Neo併用、Claude活用でカスタム。
- **総話題数**: 約200件以上、ComfyUI単独で半数超。ログ後半で安定議論深化。

このレポートは全抽出を統合・重複除去。追加分析が必要なら уточните。
