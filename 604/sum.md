# なんJ AI画像生成スレッド（抜粋: レス4〜1000）統合レポート

## 1. スレッド全体概要
- **対象範囲**: レス4〜1000（約1000レス、複数スレ跨ぎ）。主にStable Diffusion系（ComfyUI/Zuntan/SimpleComfyUi中心）のローカルAI画像/動画生成議論。エロ/NSFW（ロリ/ショタ/アナル/壁尻/squirt/男の娘など）が中心だが、技術共有（モデル/LoRA/WF最適化、トラブルシューティング）が本筋。
- **参加者特性**: 上級者（カスタムノード/LoRA作成者）と初心者（「赤ちゃん」自称）の交流活発。サンガツ文化で画像ポン出し（メタ無し）推奨。法律意識（モザイク/2D/3D判例）あり。
- **雰囲気**: 陽気協力型だが、ComfyUI複雑さ/PCパーツ高騰への不満強め。オフ-topic（ガンダムアイス、ディズニーランド座標トリック）散見。次スレ（605）立てで継続。
- **キーワード**: ComfyUI WF、ZIT/Turbo/Base、WAN2.x、DaSiWa/SmoothMix、Nano Banana、Qwen-Image-Edit、LoRA（アナル/おまんこズーム/squirt）、T5Gemma-TTS、RTX5090、Sage Attention。
- **進化トレンド**: 動画自然度向上（ループ/WanFaceDetailer）、音声cloning実用化、ローカル高速化（量子化/LowVRAM）。商用規制不満 vs ローカル堅持。

## 2. 主なトピック別ハイライト

### (1) AIモデル・LoRA共有・評価
- **ZIT/Z-image系**: Turbo Q8高速（16GB VRAM）、LoRA（ポニー調）Civitai話題。Base/Edit待望で2D/エロ強化。Omni-Baseでコントロールネット不要？
- **banana/Nano banana**: NSFW「ギガピーチ」版、オープンソース速報（VRAM47GB）。温泉浴衣/switchバー生成プロンプト共有。
- **WAN2.x (2.2/2.6)**: 動画一貫性崩れ環境再構築要。LoRA非対応批判もCLIP Vision不要/QIE2511対応期待。fp16/20stepでRTX3080 15分。
- **動画モデル比較**:


  | モデル | 強み | 弱み |
  |--------|------|------|
  | DaSiWa | 二次元チンポ/腰振り自然、Q8期待 | - |
  | SmoothMix | 3次元動き/エロ特化 | 男キャラ乱入、腰振り微妙 |
  | PainterLongVideo | - | 慣性不足/背景変化バレ |
  | SCAIL | extendなし16秒生成 | 手ポーズ検出要望 |


- **その他注目**:
  - Qwen-Image-Edit-2509/2511: Sage Attention黒塗り/解像度Tips（Scale to Total Pixels、--fast外す）。アニメNSFW LoRA公開（Mega/HFリンク）。
  - illustlias/WAI-illustrious-SDXL: 万能/アニメ強い（※wanvideo無関係）。
  - LoRA: アナル/おまんこズーム/squirt/へ口（>:(）、エレン先生、断面図。
  - Pony/Reias/NAI V5: 刺激強い初期エロ、髪再現神。

### (2) 動画/音声生成テクニック
- **動画Tips**: ループ（Start/Endフレーム+1、CFG1/step4、Frame OverlapDetailer）。ColorMatch（ref枚数一致）。WanFaceDetailer（4n+1フレームパディング）。AnimateDiff+リアスで顔一貫。
- **うごイラ進化**: 壁尻ループ、レズ/ふたなり（棒非/摺り合わせ）。
- **TTS**:


  | ツール | 評価 | VRAM/特徴 |
  |--------|------|-----------|
  | T5Gemma-TTS | cloning精度高、長さ制御（速:おっさん/遅:子供）、256並列速 | 12GB/low_vram |
  | llasa/Anime-Llasa | エロ/声優演技強、cloning可 | - |
  | mmaudio NSFW | 効果音/喘ぎ（anime,japanese,young girl） | - |


- **文字挿入**: MediBang/クリスタ（吹き出しマクロ）、Affinity/Canva/Krita/GIMP。

### (3) ComfyUIトラブルシューティング（Q&A集約）


| 問題 | 解決策/Tips |
|------|-------------|
| バージョン固定（0.3.76）/急進化 | テキスト書き換え/公式Git、旧Managerで安定、ver指定スクリプト |
| Tagger/WD14エラー | ComfyUI版/PixaiTaggerOnnxGui/sd-scripts内蔵 |
| Qwen解像度/黒塗り/Sage Attention | Pixel指定/バイパス、gguf vs fp8、Patch KJノード/--use-sage-attentionなし |
| Detailer/Inpaint濁り | デノイズ1.00/CFG統一/Epsilon、VAE完全化、Florence2+Sam2代替 |
| WanFaceDetailerエラー | 4n+1パディング |
| LoRA Loader CLIP接続 | jupo版start>0対応 |
| プレビュー消失/Managerリセット | Preview method変更、ロールバック |
| Subgraphバグ/ノード検索 | Minimalistic-Comply-Wrapper、ダブルクリック/LLM解析 |

- **初心者アドバイス**: 公式ミニマムスタート、Civitai複雑WF避け、CLI/LLM活用。

### (4) ハードウェア・環境問題
- **RTX5090ブーム**: BTO（サイコム）納品ラッシュ、水冷/Define7ケース/ステー（長尾製作所）推奨。PL70/60℃安定、3060比生成時間変わらず？ 減産/60xx延期噂で「今買え」。
- **価格高騰**: GPU/RAM/SSD（5070Ti 1.5万↑、DRAM2028年まで）。対策: BTO/中古DDR4、低電圧3060（SDXL 4765秒/枚）。
- **Asus Ascent Gx10**: 卓上スパコン、コスパ優秀（5090比3倍遅いがLoRA/動画向き）。

### (5) 商用サービス・プロンプトTips・雑談
- **商用不満**: Sora2ディズニー独占、GPT Image1.5/Grok/Firefly規制強化（女の子NG、金食い）。Gemini（冒頭「画像生成」指定、KHプロンプト）。
- **Tips**: ポン出しメタ無し、背景透過（白+クリスタ）、gelbooru低レアキャラ、ディズニーランド座標。
- **オフ-topic**: ガンダムアイス、クリスタ年末配布、ポリコレ叩き、オナニー民主化。
- **イベント**: 12/6ローカルAI展示会、epic無料ゲーム。

## 3. 注目共有・リンク（抜粋）
- **LoRA公開**: Qwen AnimeNSFW（Mega: https://mega.nz/file/49UAWZYL#9hXcBmOWDV7QzbTGSe5kzB8zyFVvXoBGKnnCX3vxCZ4 / HF: https://huggingface.co/chinmankokumin/AnimeNSFW）。
- **WF共有**: 高解像ループ/WanFaceDetailer（>>342,404,752-754）。
- **ベンチ**: Sage Attention 100倍速（4183s→35s、検証待ち）、Wan2.2 15分。
- **画像例**: 壁尻/アナルズーム/squirt/エレン先生/スイカバー/姫騎士ちゃん。

## 4. 全体傾向・洞察・将来展望
- **強み**: リアルタイム共有（新LoRA/WF/Sage Attention速報）、相互支援。ローカルNSFW優位、動画/音声統合進化。
- **課題**: ComfyUI学習障壁、VRAM/パーツ高騰（「オナニー格差」）、商用規制、環境依存エラー。
- **ムード**: 「道具磨き」価値高くローカル堅持もクラウド移行論交錯。12月後半リリースラッシュ（WAN2.6/QIE2511/Z-Image Base）期待だが沈黙続き。
- **示唆**: 初心者脱落リスク大、次スレでRTX5090実践/Sage検証熱望。コミュニティ活力高く、NSFW実践派の「生き残り」意識強い。詳細はスレ民にWFポン出し推奨。