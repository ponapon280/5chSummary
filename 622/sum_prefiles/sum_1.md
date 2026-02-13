# なんJ(5ch) AI生成スレッド ログレポート (レス4〜231)

## 1. スレッド概要
- **期間・規模**: ログはレス4から231まで（一部前スレ引用）。主に2026/02/09頃の投稿と推定。
- **主なテーマ**: Anima（新モデル）のリリースと実装が中心。Forge NEO、ComfyUIのインストール/最適化、LoRA学習、速度向上Tips、StabilityMatrixのトラブル、TTS（Takane）などの周辺ツール議論。エロ画像生成のTipsや雑談（モザイク、CPU消費電力、解像度）が混在。なんJらしい軽いノリで技術共有多め。
- **参加者傾向**: ローカル環境勢（RTX 30/40シリーズユーザー）が多く、初心者〜中級者のトラブル共有と上級者のTipsが目立つ。Anima熱が高く、生成例共有活発。
- **全体トーン**: 興奮（Animaの性能褒め）と苛立ち（インストールエラー）の混在。エロネタ多めだが、ディープフェイクは一部で非難。

## 2. 主要トピック別まとめ

### 2.1 Anima（新モデル）の話題 (最多: 約40%のレス)
- **リリース状況**: Preview版から正式版待ち（1024x1024対応）。Civitaiにタグ追加。Forge NEO/ComfyUIで動作確認多数。
- **使用感**:
  - 自然言語プロンプトの追従性高く、構図/感情表現が優秀（例: 松葉崩し描写、ベッド位置指定、セリフ感情）。
  - 欠点: 画風ブレ、ハイレゾfixで線崩れ、プロンプト長で線崩れ、ロリ体系不安定、服装再現で焼き付き。
  - 最適化: TorchCompileModel + EasyCacheで2倍速（30→20ステップ）。Schedule Promptの`to`開始遅れで効き悪い。
- **生成例共有**: 乱交、悪魔/天使イラスト、アナルビーズLoRA、モザイク画像などエロ多め。DE detailerで描き文字改善。
- **関連アップデート**:
  | ツール | 更新内容 |
  |--------|----------|
  | ComfyUI v0.13.0 | Anima tokenizer fix, fp16 support, Create List node追加。生成速度4割向上報告。 |
  | Forge NEO | Animaマージ完了、StabilityMatrixプルタブ追加→一時消え→復活。 |
  | Anima構造 | [8B Qwen3-VL Encoder] + [7B Diffusion Decoder]（知識蒸留）。Qwen-Image 1.0 LoRA互換不明。 |

### 2.2 インストール/環境構築トラブル (約25%)
- **StabilityMatrix問題**:
  - Forge NEO/Animaインストール失敗（Python 3.13エラー、wheelクラッシュ、プルタブ消失）。
  - 解決策: 「Show Unsupported Python Versions」ONで3.13選択。cache削除（Data\Assets\uv\cache）。今週後半修正予定。
  - 代替: 手動git clone（--branch neo）、venv環境推奨。ComfyUIポータブルは初心者NG。
- **ComfyUI/Forge NEO**:
  - Frontend v1.39.11でApp/Graph mode切り替え追加（simple comfy相当）。
  - 更新: `pip install comfyui-frontend-package==1.39.11` または起動オプション `--front-end-version ...@latest`。
- **注意点**:
  - Python 3.13必須。スケジューラAutomaticで黒画像。拡張挿入で起動失敗。

### 2.3 速度最適化Tips (約15%)
- **主要手法**:
  | 方法 | 効果例 (RTX 40xx系) | 注意 |
  |------|---------------------|------|
  | Sage Attention | 倍速（3060:2倍、4080:1.5倍）。whl手動DL推奨。 | Torch 2.9+/Python 3.9+、CUDA128/130合わせ。動画専用版（SpergeAttention）別。 |
  | FP16 accumulation (--fast-fp16) | 8.7s→6.9s (1024x1024,32step)。 | 劣化リスク。 |
  | Torch Compile/Triton | 半分速（前スレ例）。 | Geminiに聞かずYouTube参考。 |
- **謎現象**: 1024x1280が1024x1024より速い（5070ti,バッチ3で39s→24s）。バッチ1で解消→共有メモリ溢れ疑い。
- **Anima特化**: Step24で27s (4060ti)。Prompt all in one未対応で移行躊躇。

### 2.4 LoRA学習/プロンプトTips (約10%)
- **LoRA**:
  - 画風LoRA弱い: dim32→alpha16、ステップ/バッチ/解像度上げ（複数同時で掛け算爆発）。
  - キャラLoRA: Gemini脳筋キャプションor tagger一発（タグ消しなし）。マイナーソシャゲ成功例。
  - 問題: ロリ体系不安定、服装焼き付き、キャプションめんどい。
- **プロンプト**: 自然言語は線崩れ注意。品質タグ綱引き。gigantic penis:100でデカペニス（笑）。
- **Detailer**: Anima DE detailer優秀（描き文字→綺麗文字）。

### 2.5 その他ツール/雑談 (約10%)
- **TTS**: Takane新作（ステレオ/ASMR追加、話者ID指定）。ビジー即死多発。
- **ACE-STEP**: MIDIチープ→LLM大モデルで改善。Styleプロンプト差大。
- **TeleStyle**: V2V？ 興味あり。
- **雑談**:
  - モザイク: 薄モザ悪質、バーセンサー刑法175条批判。
  - CPU: Intel新上位700W草。
  - 解像度: 商業誌600dpi/6000+px必要。
  - ディープフェイク: 非難（免許証加工OK報告も）。

## 3. 注目Tipsまとめ
- **Anima即戦力**: Forge NEO + Sage + FP16で実用。ComfyUI 0.13.0必須。
- **初心者推奨フロー**: StabilityMatrix（ver固定）→Gemini相談→venv移行。
- **エロ生成鉄板**: LoRA（姫騎士推奨）+自然言語+DE detailer。
- **バックアップ必須**: 環境破壊多発。

## 4. 未解決/今後注目
- Anima正式版（画風制御向上？）。
- StabilityMatrix修正（今週後半）。
- Qwen2.0/3月リリース待ち。
- 解像度謎速現象の原因究明。

このレポートはログのエッセンスを抽出。詳細確認は元ログ推奨。Animaブーム継続中！