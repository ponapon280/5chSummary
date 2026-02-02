# なんJ AI生成スレッド ログレポート (抜粋: 324-527)

## 概要
このログは、AI画像/動画生成コミュニティ（主にStable Diffusion系ツール）の議論を記録したもの。主な焦点は**ComfyUI、Forge Neo、Zuntan Image (ZI/ZIT/ZIB)、Wan2.x系動画生成**。新モデル（Anima、susamixEX）、最適化ツール（NVFP4、Tiled Diffusion）、ストレージ問題（SSD価格高騰、WebP圧縮）、エロ生成のTipsが活発に共有。技術トラブルシューティングが多く、迅速なissue報告/修正（Haoming02氏の対応）が目立つ。全体として、**高速生成・高品質化・エロ対応**を求める実践派の会話。

- **期間推定**: 2026/01頃（天王星wiki言及から）。
- **参加者特徴**: 実機検証（5090/5070ti/40xxユーザー）、Linux推奨派、Stability Matrixユーザー多め。エロAA（gigantic breasts/pensis/pussy）で盛り上がり。

## 主要トピックと議論ポイント

### 1. **新モデル・ツールの評価とTips**
   - **ZI/ZIT/ZIB (Zuntan Image系)**:
     - Tiled Diffusion対応確認（t2i:1024x1024/40step=30秒、i2i高速）。
     - Simple+Eulerサンプラ最強（次世代モデル内蔵工夫）。DPM++2M Karras不向き。
     - エロ生成: LoRA併用で可能だが、リアス/ill系派生に劣る。作者にエロ対応要望出た。
     - ZIB: 構図固定向き（エロ最適解: Moody ZIB + ZIT WF, Civitai参照）。
     - Qwen-Image-2512-Turbo-LoRA: 2-4step高速化（bf16でメモリ重め、実写20step推奨）。
   - **NVFP4コンバーター**:
     - ZIT容量11.4GB→4.19GB。品質維持（右端家以外優位）。Blackwellアーキ対応（FP16比3.5倍効率）。
     - 50xx限定（40xxユーザー涙）。Wan2.2 High対応希望。
   - **Anima (新アニメモデル, 4.18GB)**:
     - 自然言語/絵師タグ/NSFW対応。borutag効くが、@toriyama akira崩壊（dragon ballで代用）。
     - ライセンス厳格（Flux並み）、step30-50推奨。キャラ書き分け可。
   - **susamixEX**:
     - プロンプト忠実（「1boy, サトシ, トレセン制服」テスト）。子供感薄め。
   - **Refiner活用**:
     - Comfyで別モデル再サンプル（タイミングで特性変更）。ill構図→XL質感リファイン推奨。
     - 絵柄LoRA時は恩恵薄。Detailer系LoRAで15/30step refine。

### 2. **動画生成 (Wan2.x, LTX-2など)**
   - **リップシンク比較 (InfiniteTalk vs PainterAI2V vs LTX-2)**:
     | ツール          | 強み                          | 弱み                          |
     |-----------------|-------------------------------|-------------------------------|
     | InfiniteTalk   | 日本語自然、無音Embeds便利   | 体動き指示必要                |
     | PainterAI2V    | 体自動動き                    | 口動き/色味悪い                |
     | LTX-2          | -                             | 口大げさ、歯崩れ、近接崩壊   |
     - ペン子ちゃん演歌動画で好評。Multimodal GuiderでLTXクオリティUP。
     - Wan2.2: WF次第でq4でも高動き。目の修正: 前スレRefiner WF参照。
   - **FLFV2/LTX-2**: 5秒動画コスパ高。InfiniteTalk+ダンスLoRA実験（リアル/アニメ系動画共有）。

### 3. **トラブルシューティングと環境Tips**
   - **Forge Neo 2.9バグ修正**:
     - ネガ空で画像変化: 新設定「For SDXL, zero out conditioning when negative prompt is empty」有効化。
     - Latentアップスケールエラー: 2.9以降バグ（issue報告推奨）。
     - SageAttention: NaN回避でネガ変更。--disable-sageで無効。Stability Matrixでtorch2.8→2.9不整合注意（Python Dependencies Overrideで固定）。
     - Clip_skip: Forge内部-2処理（メタデータ不一致でComfy黒画像）。
   - **画像保存/メタデータ**:
     | 形式 | 利点                  | 欠点                  |
     |------|-----------------------|-----------------------|
     | PNG | メタ/WF残りやすい    | 容量食う              |
     | WebP| 可逆圧縮（JPG以下容量）| Comfy読み込み不安定  |
     - JXL希望（WF保存）。Pixiv投稿時PNG流出注意→WebPデフォ推奨。
   - **VRAM/モデル管理**:
     - ComfyUI-Image-Filters: numpy破壊注意。
     - モデルオフロード: 「VRAM」検索ノード（Easy use推奨）。
   - **Trellis2 (ComfyUI-Trellis2)**: Windows拒否多（Linux/WSL推奨）。HY3D2.1+UltraShape代替。
   - **LoRAの||**: 区切り記号（複数ワード表記、e.g. コス/タグ）。ファイル名不可（Windowsパイプ）。

### 4. **ハード/ストレージ事情**
   - **SSD価格高騰警報**:
     - m.2 4TB: 5万→7-15万。SN7100/SN850X在庫枯渇→即買い推奨。
     - GEO 2TB/2万（Micron TLC）、WD gen4 8TB/15万好例。
   - **FlashAttention**: 入手報告（Trellis2諦め）。

### 5. **エロ/ネタ話題**
   - ZIエロ弱（gigantic AA祭り）。害虫LoRA（モスキート/ベッドバグ少女）。
   - メタデータネタ（NVA文字、ビッグエンディアン化け）。
   - AIエージェントSNSリスク（ウォレット晒し、Copilot人事評価閲覧）。

### 6. **その他共有WF/モデル**
   - Civitai: Moody ZIB + ZIT Simple WF, Qwen2511AnimeNSFW3。
   - ill系3D slider LoRA重宝。

## 注目Tipsまとめ
- **即効対応**: Forge issue→1分返信/10分修正（Haoming02神）。
- **エロ初心者**: ZIB構図固定+LoRAでスタート。
- **高速化**: NVFP4/ZIT Tiled/2step LoRA。
- **注意**: Stability Matrix更新でtorch不整合。猫箱.moeアップ失敗多（0byte確認）。

## 結論
スレは**ZI/ZITの高速実用性**と**動画リップシンク進化**が熱く、Forge/Comfyの微調整文化が強い。エロ需要高く、次世代モデル（ダブルフェラ級）期待。価格高騰でハード投資煽り。継続監視推奨（新モデルAnima/ZI更新待ち）。総レス200超の濃密ログ、技術共有コミュニティの好例。