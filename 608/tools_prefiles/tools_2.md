### 抽出された「ツール」に関する話題

ログから、生成AIの**ツール**（ComfyUI/comfy関連のワークフロー、カスタムノード、EasyWan22、PainterLongVideo、QIE、nano-banana、背景切り抜きアプリ、translateノードなど）に限定して話題を抽出。**モデル**（NovelAI/NAI、Pony、illustrious/NoobAI/FLUX/Wan/Qwenなど）の言及は一切除外。ツールが選ばれている理由が明記されている場合のみ、その点を括弧内に追記。

#### ComfyUI (comfy) および関連カスタムノード/ワークフロー (WF)
- **238**: ComfyUI-WanVideoWrapper_QQ（実験したが扱いにくい）。
- **248**: ComfyUI Managerで「translate」を検索し★付きカスタムノードをインストール → Google翻訳ノードが使え、日本語指示が可能（日本語プロンプトが通りやすいため選ばれている）。
- **251**: node整理、サブグラフ/setter/getter関連のエラー議論。
- **290-300, 308-309, 311**: 画像切り取りアプリ（背景切り抜き機能、RMBG v1.4/v2.0対応、bat/venv/git clone/install_app.batの改行コード問題、git core.autocrlf設定）。商業利用不可モデル使用注意（導入手間がかかるが、RMBG精度が高いためv2.0推奨）。
- **302-304**: 前スレ935のWF再掲依頼（スクショのためメタデータなし、サブグラフなし）。
- **330-331, 336, 340-346, 349, 352, 355, 359-360, 362-363, 368, 370, 372, 382-383, 384, 386-387**: WF共有/改修（PainterLongVideo組み込み、LoRA/EndImage指定、サブグラフ/set-get、EasyWan22からの移行、json出力+GPT分析）。綺麗なWFが好まれるがスパゲッティ状になりやすい。他人WFは参考用（共有しにくいが、個人用は見せびらかしたくなる）。
- **364**: Adetailer（乳首検出、範囲/検出数調整が片方しか効かない問題）。
- **366**: detailer（動画1コマごと適用でガクガク、一貫性問題）。
- **368**: Color Matchノード（image refの引数順序問題）。
- **370**: 実験WF（PainterLongVideo前後生成、Color Correct）。
- **384**: Stability MatrixでComfyUI画像動作（Geminiでカスタムノード作成）。
- **388-389**: Refiner/Upscaler（後処理用、WF一括/バッチ処理。VRAM/RAM効率重視で直接720p生成推奨）。
- **396, 421**: LoRA Loader（バイパス/トリガーワード手打ち）。
- **404**: I2V WF（color matcher挟み）。
- **407**: cn tile/FaceDetailer（白背景でタイパ良い）。
- **409, 418, 426-428, 430-431**: Stable Video Infinity (SVI/SVI 2.0 Pro、LoRA追加のみ、WanVideoWrapper以外ネイティブWF、ComfyUI-KJNodes更新必要）。
- **411, 429**: save-image-extended-comfyui（webp 100%画質でWF再現不可バグ、issue報告推奨）。

#### EasyWan22
- **321, 342, 354-356, 359, 377-378**: EasyWan22卒業推奨（環境丸ごとオールイン、赤ちゃんでも動画生成可だがWF複雑/バージョン固定、カスタムノード/Manager不要、LoRA自動入）。Upscaleガチャせず直接720p（スペック/動画条件による）。
- **343, 372**: 導入手順（別ComfyUIインストール、Managerでノード自動追加、モデル/VAE/TE/Lora手動配置）。

#### PainterLongVideo (PLV)
- **294, 297-298, 313-320, 322-323, 325-327, 329-339, 342, 365, 369-371, 390-395, 397-400, 404-405, 412-414, 417, 422**: Start/End画像指定で長時間動画/一貫性確保（背景/小物一貫重要、3連結推奨、顔detailer/posetest併用、色ズレ/フリッカー対策にcolor match/correct失敗。LoRA/モデル影響大、背景単調/ベッドLoRA推奨）。エンド画像自動補完なし、手動準備必須（キャラキープ長時間実用的）。SVI併用検討。

#### QIE (Qwen Image Edit?)
- **314, 320, 326**: next scene LoRA/i2iで一貫性/画風維持（重い、エロ不可、自作LoRAでエロ差分→PLV）。

#### nano-banana
- **301**: nanobananaで着衣→背景一貫ポーズ変更→インペ剥き（動画作成提案）。

#### その他ツール
- **247**: Qwen3 VQAノード（参考画像/動画からプロンプト自動生成）→ Qwenモデル関連のため抽出スキップ。
- **290**: 画像切り取りアプリ（上記ComfyUIインストール関連に含む）。
- **368**: split imageノード（80+1フレーム分割、initial reference/start/previous video）。
- **394**: miaomiao（動画試作）。

**抽出まとめ**: 主にComfyUIのWF/カスタムノード共有が中心。理由として「日本語対応しやすさ」「動画一貫性確保」「EasyWan22からの卒業（柔軟性）」「背景切り抜き精度」「タイパ向上」が挙げられる。PainterLongVideoは長時間動画制御で人気だが色ズレ課題多し。nano-bananaはポーズ一貫提案のみ。