# なんJ NovelAI部（生成AIスレ）統合ログ要約レポート（>>4-1000レス）

## スレッド全体概要
- **範囲/規模**: >>4〜1000（約1000レス）。ComfyUI中心の画像/動画生成AI議論が主軸。初期（>>4-225）は環境構築/新モデル導入期、中盤（226-626）はWF共有/トラブル解決期、後半（627-1000）はLTX-2ブーム・荒らし混在・Zimage期待期。
- **全体傾向**: 動画生成ブーム（LTX-2/SVI/Wan2.2）が加速。ComfyUI v0.8.0〜0.8.2アップデート対応、ハード/VRAM品薄愚痴、エロ/NSFW生成Tipsが恒常。なんJらしい下ネタ/ジョーク/喧嘩（アナルニキ論争）が混在。新規「赤ちゃん」相談多め、上級者WF共有活発。進化速く「追いつけん」「脳汁出る」声多数。
- **参加者層**: 低スペ（RTX3060/12GB）〜ハイエンド（RTX5090/Pro6000）。ローカル派優位、クラウド/NAI補完派少数。エロ志向強（乳揺れ/断面図/femdom）。
- **補足**: waiはIllustrious（リアス）の派生モデル（wanvideo無関係）。FLFはFirst-Last Frameの略（FLUX無関係）。

## 主なトピック別まとめ

### 1. ハードウェア/在庫/価格/VRAM事情（全パート通底、約20%）
- **RTX50xx品薄**: 5070Ti/5090在庫切れ→値上げ即完売。Amazon空箱詐欺報告。GIGABYTE新モデル「ラジカセかわいい」「rev商法」皮肉。
- **推奨スペック**:


  | GPUモデル | 特徴/ユーザー傾向 |
  |-----------|-------------------|
  | RTX5090/Pro6000 | 動画26h生成可能、VRAM70GB超え対応（電気代1万超）。シェア最多。 |
  | RTX4060/60Ti 16GB | Wan効果で高VRAM主流、低スペ主力。 |
  | RTX3060 12GB/4070Ti | LTX-2可もエラー多。再生産リークで絶望。 |
  | AMD Radeon Pro R9700 | 32GB@25万、ROCm7.1.1でComfyUI高速化（SDXL2.6倍）。 |


- **課題/Tips**: PCIe3.0ボトルネック、200V電源必須（60A限界）。量子化/GGUF/block swapで12GB動画可。RAM128GB推奨。

### 2. ComfyUI環境構築/アップデート/トラブル（最多、約30%）
- **バージョン進化**: v0.8.0（Sage Attention3対応）→v0.8.1→v0.8.2（VRAM最適化、sage警告消）。Desktop版非推奨、Portable/Git+venv/Docker推奨。
- **インストール比較**:


  | 方法 | メリット | デメリット |
  |------|----------|------------|
  | Portable | 初心者即使用 | ノード管理煩雑 |
  | Git+venv | 柔軟/戻し可 | 初回セットアップ |
  | Docker | 隔離最強 | 上級者向け |


- **エラー祭り/解決**:


  | エラー | 解決策 |
  |--------|---------|
  | hires.fix奇形 | denoise調整 |
  | LTXVAudio tupleエラー | smZ Nodes無効、fp8/gemma分割DL |
  | SAM3 nipplesエラー | 卑猥ワードNG、confidence 0.01-0.05 |
  | CU128/130ミスマッチ | TensorRT再構築、EasyWan2.2 cu118 |
  | VHS_SelectFilename NoneType | kjnodes latest、保存フォルダ指定 |
  | comfy_kitchen | requirements.txt、無視可 |


- **Tips**: Stability Matrix+extra_model_paths.yaml。サブグラフ/グループでスパゲティ回避。set/getローカル名、--reserve-vram 4/10、preview=None。

### 3. 新モデル/ツール/WF評価（約25%、動画ブーム核心）
- **主力モデル進化**:


  | モデル | 強み | 弱み/Tips |
  |--------|------|-----------|
  | **LTX-2** | 音声/リップ/BGM神、低スペ（12GB）可、生成早い。I2V3次元◎、NSFW LoRA即。WF:6連サンプラーガチャ、テンプレ使用。 | VAEエラー、顔崩れ。Enhancer Gemmaバイパス、gguf量子化。CEO I2V修正予定。 |
  | **SVI (Smoothmix)** | anchor sampleキャラ維持、LoRA v2 PRO。NSFW版新。 | LoRA keyエラー（lora.pyコメント）、タイル赤枠。kjnodes/WanImageToVideoSVIPro必須。 |
  | **Wan2.2/EasyWan** | 30秒安定、FP8高速（81f61秒）。 | 色ズレ/暗転（カラーマッチ+デフリッカー）。巨乳物理弱、endimage差分。 |
  | **SAM3/StoryMem** | 複数検出/編集速、Easy-SAM3 Undo可。 | 卑猥ワードNG。QIE/ZIT背景編集併用。 |
  | **Zimage Base** | Danbooruチューン/NSFW FT期待、Turbo調整後。 | 配布保留（Stardust寄付99%）。学習16GB可。 |
  | **その他** | Qwen Image 2512/QIE（実写/編集◎）、PLV（最後フレーム結合）、Kling OSS（モーショントラック、量子化待ち）、TTS（T5Gemma-TTS+InfiniteTalk）。Rainbow v7（アニメ健全）。 |


- **NAI vs リアス (Illustrious/wai派生)**: NAI「ポン出し/ストーリー手軽、高い肌AI臭」。リアス「柔軟/ZIT+i2i◎、人体硬直」。v3.6まで、Danbooruタグ必須。
- **WF共有**: >>395（整理/smZ除去）、SVI Pro（LoRA2種分離）、ten連結動画。Seed固定/-1ガチャ。

### 4. LoRA/生成/NSFW Tips（約15%）
- **複数キャラLoRA難関**: 顔融合→画像1:1/DoRA/マスク分割/2girls混ぜ/wildcards。i2L高速作成。
- **エロ特化**: Danbooruタグ必須（spread pussy/nipple tweak/femdom）。断面図deep penetration（SAM3+Mask Invert）。乳揺れ/脚短/口暴れ→denoise0.5/短小LoRA。メタデータ解析、未使用コンドーム咥えプロンプト。
- **実写/アニメ**: QI2512+SNOFS多ポーズ。低: dasiwa、高: EnhancedNSFW。プロンプト自動（Qwen VL/NSFW Caption V4.5）。

### 5. コミュニティ/雑感/企業動向（約10%）
- **派閥**: ComfyUI移行急増（柔軟◎）、Forge/A1111離脱。ローカルvsクラウド論争。
- **カオス要素**: アナルニキ/姫騎士ニキ投稿で大荒れ（擁護vsアンチ）。スレチ（パーツ/政治）不満、NAI回帰声。
- **企業**: Cygames/CA AI求人（修士/論文歓迎）。サイゲAI活用、Llama日語FT。
- **ツール活用**: NotebookLM/Grok/ChatGPTでスレ要約。Google AI Pro（950円/3ヶ月）。

## 注目ニュース/トレンド/未来予想
- **ニュース**: AMD ROCm高速化、LTXVideo VRAM最適化、Kling OSS公開、Zimage Base coming soon。
- **トレンド**: 動画長尺化（15-30秒）、高VRAMシフト（16GB主流）、編集工程増（SDXL→QIE→SAM3）、量子化で低スペ救済。エロNSFW強化（喘ぎ/T2S）。
- **課題**: 新規障壁高（ノード複雑）、API無料枠枯渇、生成時間長。
- **予想**: Zimage配布でイラストシフト、LTX-2二次/エロ強化、RTX Super/マルチGPU普及。次スレ: WF聖戦/Zimage大荒れ。

## 総括
1000レス超の活況スレ。ComfyUIがデファクト、動画生成が「神イベント」化も環境地獄/品薄で苦痛共有。技術Tips/WFが宝庫、エロ脳汁で延命。ローカル防衛強化中。生成楽しめンゴ！詳細/WF質問歓迎。