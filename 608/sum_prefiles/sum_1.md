# なんJ(5ch) ComfyUI/Stable Diffusionスレッド ログレポート (抜粋: 投稿4〜227)

## 概要
このログは、主にComfyUIを中心としたAI画像・動画生成ツールの議論。エロティックなコンテンツ（性奴隷描写、体位構図、動画生成など）を中心に、インストール方法、プロンプトTips、動画生成の課題、モデル量子化、トラブルシュートが活発。参加者は中級者〜上級者で、Stability Matrix、Portable版、venvなどの環境構築、Wan系モデル動画生成がホットトピック。全体として、2026年への展望（動画進化期待）と年末整理の話題も散見。総投稿200超で、Tips共有が豊富。

**主なトレンド**:
- **動画生成の進化**: Painter Long Video (PLV)、FLF2V、WanMoveなどのノード活用。一貫性・劣化問題が課題。
- **環境最適化**: fp8/Q8量子化、sageattn/tritonビルド、pinned memoryで高速化。
- **プロンプト/構図**: 体位（upright straddle, arms behind back）、背景制御（bed sheet）、デッサン人形活用。
- **ツール比較**: ComfyUI Portable/Stability Matrix推奨。UI変更で不満多し。

## 主なトピック別まとめ

### 1. ComfyUIインストール・バージョン管理 (地雷回避・推奨)
- **地雷報告**:
  - Comfyデスクトップ版: Win更新で壊れ（25,27）。
  - Stability Matrix: フォルダ構成独特、venv pip手間（26,47）。ただし初心者向けで拡張検索楽（52,53）。
- **推奨**:
  - **Portable版**: 管理楽、再インストール耐性高（76,92,130,133）。赤ちゃん（初心者）向け（124）。
  - Stability Matrix: バージョン通知で様子見更新（166,167: v0.6.0）。Forge Neo対応（200）。
  - venv/git clone: カスタムノード対応強いが手間（47,94）。
  - Easy版: 会話噛み合いやすい（98）。
- **Tips**: Stability MatrixでComfyメニューから入れるとエラー減（48）。KJnodes動くバージョン確認推奨（163,166,222）。

### 2. プロンプト・生成Tips (エロ特化)
- **性奴隷服**:
  - `sex slave outfit` / `harem outfit` / `arabian clothes, dancer, mouth veil, pelvic curtain`（38,40,42,66,68,70,85）。
  - 参考: ドラビアンナイトしずかちゃん（78,猛毒注意79）。
- **体位・構図**:
  - 後ろから: `standing sex, bent over, arm grab, sex from behind, arms behind back/head`（90,169,215）。
  - 騎乗位系: `upright straddle, arms around neck, leg lock, cowgirl, hug`（80,82,93）。
  - 男後ろ視点: デッサン人形/CN anytest/postestでweight 0.3〜0.75（56,61）。棒人間OK（58）。
  - 服脱ぎ顔隠れ: 未解決（170）。
- **背景制御**:
  - ベッドシーツのみ: `(white background, simple background:1.5), white sheet` / `bed sheet` / `dakimakura (medium)`（131,134,137,140）。
- **その他**:
  - Hires.fix 2倍で高画質（49）。
  - 逆バニー: `reverse bunnysuit`（86,87）。
  - 自作LoRA細部潰れ: 未解決（171）。
  - Detailer: FaceDetailer（手/ちんこ対応、yolo使用）（153,156,157）。

| 人気プロンプト例 | 用途 |
|------------------|------|
| `harem outfit, dancer, mouth veil` | ハーレム奴隷 |
| `arms behind back, leaning forward` | 後背位 |
| `upright straddle, leg lock, kiss` | 対面座位 |
| `bed sheet, simple background` | シーツ背景 |

### 3. 動画生成 (Wan系・一貫性課題)
- **ノード/手法**:
  - **Painter Long Video (PLV)**: スタート/エンド画像指定で一貫性向上、繋ぎ目滑らかだが劣化激（15-20秒限界、139,145,147,177,181）。チュートリアル不足（81）。
  - **FLF2V**: 自力複数作成・繋ぎ。PLVより一貫性ビミョー（139,145）。
  - **WanMove**: 矢印で動き付け、実験動画共有（アニメ/リアル系、181,184,220限定Wan2.1）。
  - i2v Start/End: ハメ撮り再現（143,146）。Inpaint/Anytestでポーズ変更（172-175）。
- **課題**:
  - 一貫性: 背景/衣装準備必須（画像スキル重要、148,178）。劣化/外人顔化（145,147）。
  - 目閉じ: 瞬き学習由来、プロンプト無効（`eyes open`効かず、223-227）。LoRA期待。
  - 環境: sageattn/tritonビルド地獄（103,165,188）。SimpleComfyUI自動インスコ推奨（188,210）。
- **2026展望**: Wan2.6ローカル未公開（107,127）。Z-movie-turbo期待（152）。

### 4. モデル・量子化・最適化
- **量子化比較**:
  | 形式 | 速度 | 品質 | メモリ |
  |------|------|------|--------|
  | fp8 scaled (e4m3fn) | 最速 (pinned memoryで2倍) | Q8並 | Low VRAM優位 |
  | Q8 gguf | やや遅 | fp8超え？（モデル次第） | リーク注意（164） |
  | FP16 | 基準 | 最高（顔/貫通抑制） | 高 |
- **Tips**: pinned memoryで高速DMA（187,216）。GGUF最新クローンでRTX5070Ti砂嵐解決（164）。viduQ2アニメ強（198）。

### 5. トラブルシュート・ツール
- **UI変更**: Job history追加/停止ボタン隠れで糞（72,89,96,141,194）。
- **デッサン人形**: クリスタ（FK+IK、104,113,117）。VaM/DAZで体位無限（99,118,120,123）。物理人形+openpose（106,116）。
- **LoRA作成**: 教材着色（GPT、54）。kohya_lora_param_gui venv対応希望（213）。
- **その他**: antigravity会話混乱（69）。クリスタログボ忘れ（108,112,115）。

## 注目Tips集
- **初心者ルート**: Stability Matrix → Portable ComfyUI（124）。
- **高速動画**: fp8 + pinned memory + SimpleComfyUI（187,188）。
- **構図ガチャ**: デッサン人形/CN weight低め（56,61）。
- **年末整理**: 生成中即削除/厳選フォルダ（34,37,39,43,45）。

## 結論・トレンド予測
スレ民はローカル最適化に注力中。動画一貫性向上（PLV/StartEnd）が2025年末の焦点で、2026はWanローカル/Z-Image進化期待。ComfyUIのUI迷走/情報陳腐化が痛点（101,135,138,142）。エロ生成はプロンプト+Detailerで高品質化可能。次スレで動画WF共有増えそう。質問あれば深掘り推奨（例: 特定ノードWF）。 

**生成日時**: ログ基準2025年末想定。情報鮮度確認を。