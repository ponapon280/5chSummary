### 生成AIモデルに関するレポート

#### 流行モデル推測まとめ（テキスト全体から）
テキストの複数ログ抽出から、**Z-image系（Z-image / ZIT / Z-Image Turbo / Z-image Base）** が圧倒的に流行・最頻出（9割以上の言及で熱狂的）。SDXL後継候補として「覇権」「次世代本体」と位置づけられ、リアス/Noob/Wan/FLUX/Qwenとの比較で優位（プロンプト忠実性、高速低VRAM、LoRA耐性、多様な描写優秀）。リリース待ち（Base/Edit版）が話題の中心で、100万DLや無料公開戦略が普及を後押し。  
**次点流行**: Wan2.2（動画生成効率・エロ質感・高出力で愛用多数）、Qwen系（NSFWキャプション/プロンプト生成で実用・量子化版多用）、illustrious（リアス: リアル系容易さ・愛着）。Noobai（長期安定愛用）、FLUX（オンライン利便性だが劣勢）。NovelAI/Ponyは言及少なく、マイナー。全体として、低スペ対応・NSFW/エロ特化・高速生成が選好トレンド。

#### 1. Z-image系（Z-image / ZIT / Z-Image Turbo / Z-image-turbo / Z-image Base / Z-imageEdit）
- **全体傾向**: 最頻出・覇権期待株。Turbo版は低VRAM（12-16GB）で高速（2-3step下絵、8秒/1024x1024）、Base版公開待ち。ControlNet/LoRA対応活発（トレーニングアダプターv2公開）。実写/エロ構図/有名人/アニメキャラ/文字/自然/前後/逆立ち/漫画/足ピン/複数人物/膜サクサクで優秀。i2i下絵としてリアス/Wan補完に最適。
- **選ばれている理由**:
  - 高速・低スペ対応（VRAM効率、3060/12GB可、くそざこ消費者向け）。
  - プロンプト忠実・予測不能ワクワク復活（SDXL初期並み）。
  - LoRA作成耐性高（崩壊しにくく、1万stepで画風機能、civitai急増）。
  - 比較優位（リアス/Noob/FLUX/Qwen凌駕、身長差/人体交差/SDXLよりマシ）。
  - LLM連携（Qwen/ChatGPTでバリエ増）、自然言語/構造キャプション対応。
- **欠点**: ランダム性低（同じ出力多、ノイズ調整必要）、貧乳/イラスト未熟、LoRA精度一部不足（Base待ち）。
- **関連**: Genspark/EasyImageEdit/ComfyUI統合、100万DL自慢。

#### 2. Wan（Wan2.2 / EasyWan22中心）
- **全体傾向**: 動画生成特化で愛用多数（長期ユーザー）。髪グラデ/異方性反射/プニプニエロ質感/高出力/パーティクル（液体・しぶき）優秀。smoothmix比較でNSFW安定、RTX5090購入動機に。
- **選ばれている理由**:
  - 動画効率（MMDより短く楽、v2v/i2v対応、フレーム不自然少）。
  - エロ生成強（獣姦LoRA、挿入/オーガズム制御、膜サクサク補正）。
  - LoRA適用/互換性高（NSFWマージ済み、速度向上）。
  - 画質補正力（ZIT/リアス下絵の後処理に最適）。
- **欠点**: WFトラブル（プッシー開き優先）、過剰プニプニ、クラウド最新版依存、RAM128GB必須、ノイズ感。
- **関連**: smoothmix/easwwan WF、LoRA多数作成。

#### 3. Qwen系（Qwen2.D / Qwen3-VL-8B-NSFW-Caption-V4.5 / QIE / QwenVL-NSFW / Qwen2509 / Qwen2511）
- **全体傾向**: NSFWキャプション/プロンプト生成/画像編集で最多活用。量子化版（q4_k_m/q6_k/q8/GGUF/BF16）多用、LM Studio API連携爆速。
- **選ばれている理由**:
  - NSFW特化（エロ画像解析/長文自然言語プロンプト/年齢忠実、手マン制御）。
  - メモリ効率（GGUF/auto_unloadでVRAM8-16GB対応、量子化で安定）。
  - ワークフロー統合（ZIT/i2i/3P構図イラスト化、健全絵も可）。
  - 高性能（スレ一択、簡潔指示/q8安心、AbliterationでUGI高）。
- **欠点**: 貧乳弱、FP8ノイズ/砂嵐、低速（VRAM16GB量子化必須）、繰り返し/手を抜く、Base公開待ち（Z-image相互牽制）。
- **関連**: ComfyUI-QwenVLノード、prithivMLmods派生。

#### 4. illustrious（イラストリアス / リアス / ill / IL / Illustrious2.0）
- **全体傾向**: SDXL DLC派生、リアル系エロ生成主力。Z-image下絵+i2iで高速化。
- **選ばれている理由**:
  - リアル系容易さ（難しい構図/タスク簡単、少ないstep/seedガチャで充分）。
  - 愛着・継続使用（ちんぽ向ける魅力、1年愛用）。
  - LoRA適性（SDXLベース、SEX身体崩れ対応）。
- **欠点**: 顔二次元化、特定キャラ学習不足（レイシア）、Z-image/Noobに凌駕、クラウド最新版、ローカル非対応。
- **関連**: Turbo比較、Z-image版待ち。

#### 5. Noobai（Noob / noob系統）
- **全体傾向**: illustrious同様SDXL DLC、長期安定愛用。
- **選ばれている理由**: 安定実績（1年愛用多数、wai愛用層）。
- **欠点**: Z-imageに劣勢、次世代版待ち。
- **関連**: LoRA共有（illustrious/Pony）。

#### 6. FLUX（FLUX2 Pro / FLUX2.D）
- **全体傾向**: オンライン即利用可能だが比較劣勢。
- **選ばれている理由**: Genspark対応早い（利便性）。
- **欠点**: 多描写（有名人/アニメ/文字等）でZIT負け、LoRA崩壊。
- **関連**: ZIT/QIE/SDXL長所比較。

#### 7. NovelAI (NAI)
- **全体傾向**: 季節UI好評、クラウド静止画/動画期待。エロOK希少性。
- **選ばれている理由**: ローカル上位互換（静止画主力、画像参照有効、男の娘生成珍）。
- **欠点**: 二次創作制限、高額サブスク、動画未対応。
- **関連**: banana併用、クリスマス仕様。

#### 8. Pony
- **全体傾向**: 言及少なく、AuraFlowベース期待薄。過去削除談。
- **選ばれている理由**: なし（比較劣勢）。
- **関連**: illustrious/Noob LoRA共有。

#### 9. その他マイナーモデル
- **SDXL / SD1.5**: 基盤安定（DPM++サンプラー常用、棚描写まとも）。inpaint弱。
- **MiaoMiao RealSkin v1.1**: 髪細部良好、プリップリエロ。
- **HunyuanVideo-1.5**: VRAM14GB動画、LoRA fine-tune。
- **banana / bananapro**: イレイナ/シルバニア容易、レイシア学習。
- **Animagine**: SDXL DLC例。
- **LTX2 / QIE2511**: Base待ち期待株。
- **Grok**: NSFWリーダーボード上位、エロ文書/フォトリアル。
- **その他（wai14/15, motsuaki, Lumina等）**: 構図安定/量子化回避推奨もマイナー、欠点多（再現限界）。

#### 全体洞察
- **トレンド**: Z-imageの革新性（低スペ高速）が移行を促進。除外モデル（Wan/Qwen/illustrious）は補完役に。NSFW/エロ/動画/LoRAが主用途、低VRAM/RAM効率が選定キー。クラウド依存/量子化/Base待ちが共通課題。ログはComfyUI/WF中心で、実用・比較議論活発。将来的にZ-image Base公開でさらなる流行加速か。