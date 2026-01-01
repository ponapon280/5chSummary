# なんJ(5ch) AI生成スレッド（ComfyUI/Wan系中心）総合ログレポート (レス4-1000)

## 概要
このレポートは、なんJ板のAI画像・動画生成スレッド（なんJNVA部含む）を5パート（4-227, 228-432, 433-636, 637-842, 843-1000）に分割したログを統合・重複除去したもの。主にComfyUIを活用したエロティックコンテンツ（性奴隷描写、体位構図、射精/潮吹き、百合など）の生成Tips、動画生成進化（PLV→SVI）、環境構築、モデル量子化、トラブルシュートが中心。参加者は中級者〜上級者中心で、WF（ワークフロー）共有活発。ログ期間は2025年末〜2026年初頭想定で、動画長時間化（5秒→30秒+）、ローカル最適化、年末年始あけおめ祭りが特徴。総レス1000超、画像/動画共有控えめだがTips豊富。※FLF=First-Last Frame（FLUX無関係）、wai=Illustrious派生（wanvideo無関係）。

**全体トレンド**:
- **動画生成ブーム**: PLV/SVI/Z-Imageで一貫性向上（背景/顔/色調）。課題: チカチカ/色ズレ/劣化。
- **環境移行**: pixai/NAI→ローカル（ComfyUI Portable/Stability Matrix推奨）。
- **エロ特化**: プロンプト/LoRA/Detailerで高品質体位/背景制御。
- **懸念**: GPU高騰（RTX5090 75万超予測）、クラウド検閲、ローカルvsクラウド論争。
- **進化**: 2025年末動画焦点→2026新モデル（Qwen2512/Z-Image Base）期待。

## 主なトピック別まとめ

### 1. ComfyUIインストール・バージョン管理（地雷回避）
- **推奨環境**:


  | ツール | 利点 | 注意 |
  |--------|------|------|
  | **Portable版** | 管理/再インストール耐性高、初心者向け | KJnodes互換確認 |
  | **Stability Matrix** | バージョン通知、拡張検索楽、Forge Neo/Wan2GP対応 | venv pip手間、フォルダ独特 |
  | **venv/git clone** | カスタムノード強い | 手間大 |
  | A1111/Forge/Reforge | 入門用→Comfy移行 | 開発停滞、動画弱 |


- **Tips**: Update All習慣、英語環境/キャッシュクリアでエラー減。UI変更（Job history追加/停止ボタン隠れ）不満多。EasyWan卒業推奨、SimpleComfyUIでsageattn/triton自動化。

### 2. プロンプト・生成Tips（エロ特化）
- **性奴隷/衣装**: `sex slave outfit, harem outfit, dancer, mouth veil, pelvic curtain, reverse bunnysuit`。ドラビアンナイト参考（猛毒注意）。
- **体位・構図**:


  | 体位 | プロンプト例 | Tips |
  |------|--------------|------|
  | 後背位 | `standing sex, bent over, arms behind back/head` | CN anytest/postest weight 0.3-0.75、デッサン人形（クリスタ/VaM/DAZ） |
  | 騎乗位 | `upright straddle, arms around neck, leg lock, cowgirl` | デッサン人形/棒人間OK |
  | 対面座位 | `upright straddle, leg lock, kiss` | - |


- **背景制御**: `white sheet, bed sheet, simple background:1.5, dakimakura`。単調LoRA推奨。
- **その他**: Hires.fix 2倍、FaceDetailer（YOLO/手・ちんこ対応）、Wildcardネスト、ネガプロ廃止、自然言語/Google翻訳ノード。逆バニー/自作LoRA細部潰れ未解決。Detailerで乳首片方問題対策。

### 3. 動画生成（主力: PLV→SVI）
- **主力ノード/手法**:


  | ツール | 特徴 | 課題/対策 |
  |--------|------|-----------|
  | **Painter Long Video (PLV)** | Start/End画像指定、30-120秒連結（2-3段）、モーション制御（手コキ/事後） | 劣化/背景崩れ/終端4Fチカチカ→End複数指定、Color Match、単調背景LoRA、Refiner後処理 |
  | **Stable Video Infinity (SVI)** | Native WFシンプル、LoRA追加で顔/色一貫高、Pro版台頭（KJNodes nightly必須） | Pro顔変化→無印推奨、オーバーラップ5F、SAM3目Detailer |
  | **FLF2V/WanMove** | 自力複数作成、矢印動き付け（限定Wan2.1） | 一貫性ビミョー |
  | **その他** | i2vハメ撮り、Inpaintポーズ変更、TripleKSampler高速化 | 瞬き（eyes open無効）、目閉じLoRA期待 |


- **WF共有例**: >>331（30秒パワープレイ）、>>577（5秒×3=14秒プロンプト追従）、>>559/623（Native変換）。サブグラフ/set-get活用、スパゲッティ回避。
- **Tips**: 尺7秒プロンプト追従、Ref frame=97、Low noise V2Vでガクガク回避。RTX Video SR/ Lossless Scaling後処理、ffmpeg圧縮。
- **展望**: 2026 Wan2.6ローカル/Z-Image-turbo、ループWF増加。

### 4. モデル・LoRA・量子化最適化
- **量子化比較**:


  | 形式 | 速度 | 品質 | メモリ |
  |------|------|------|--------|
  | fp8 scaled (e4m3fn) | 最速（pinned memory 2倍） | Q8並 | Low VRAM優 |
  | Q8 gguf | やや遅 | fp8超え？ | リーク注意 |
  | FP16 | 基準 | 最高 | 高 |


- **注目モデル/LoRA**:


  | モデル | 評価 | NSFW |
  |--------|------|------|
  | Qwen Image 2511/2512 | 自然言語強、プラスチッキー解消、NSFW LoRA（百合） | 高（resolution steps=ピクセル倍） |
  | Z-Image Turbo/Anime/Omni | 鮮明、自然感、Base待望 | エロFT期待、JPEG風限界 |
  | SVI Pro/Wan2.2/2.6 | 動画神、色ズレ対策 | Kijai版LoRA必須 |
  | その他 | viduQ2アニメ、Banana、Flux2（VRAM重） | 射精/潮吹き（Smooth MIX）、CunnyFunky（乳首溶け） |


- **LoRA Tips**: 白飛び（ノイズオフセット0.1）、セミリアル装飾吹飛け。版権/キャラLoRA可。

### 5. トラブルシュート・周辺話題
- **共通問題**:


  | 問題 | 解決策 |
  |------|--------|
  | 色/背景一貫 | Color Match/Refiner、単調LoRA |
  | チカチカ/色ズレ | 最終4-5F抽出+カラーコレ、モデル依存 |
  | インストールエラー | bat改行CR+LF、git core.autocrlf true |
  | アップローダー | catbox/litter重→ibb/tadaup（メタ消滅注意） |
  | 瞬き/瞳変化 | CFG上げ、LoRA |


- **ハード**: 16GB VRAM運用（SDXL/Qwen）、3080 FP16恩恵、5090高騰/在庫枯渇不安、レンタル検討。
- **コミュニティ**: WF/画像共有積極（Civitai漁り）、エロ規制（Grok/X凍結）、法的グレー（モザイク/LoRA公開、FLMASK事件）。ローカルvsクラウド喧嘩（自由度vs手軽）。年末振り返り（SDXL花火/Kling脱獄）、あけおめ祭り（年賀状/干支馬娘）。
- **脱線**: 勃起薬、モチベ低下、マンネリ、ディープフェイク風当たり。

## 注目Tips集
- **初心者ルート**: Stability Matrix + Portable ComfyUI → WF共有活用。
- **高速動画**: fp8 + pinned memory + SVI Native。
- **構図安定**: デッサン人形 + Detailer + End画像複数。
- **年末整理**: 生成即削除/厳選フォルダ、uv/pyenvでPython管理。

## 結論・トレンド予測
スレはComfyUI動画実践場として機能、PLV/SVI WF共有で長時間エロ動画進化（一貫性向上中）。Qwen2512/Z-Image Baseが2026主流か。ローカル派結束強いが、高騰/検閲でクラウド併用増。コミュニティ活況（新規歓迎）、次スレで5090実践/新LoRA拡散予想。情報鮮度確認を。質問/深掘り歓迎（特定WF例等）。 

**生成日時**: 2025年末-2026初頭ログ基準。