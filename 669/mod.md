# 🆕 新規トピック（前回からの差分）
### 【モデル: Krea2（Krea 2 / Krea2 Large / Turboなど）】
- 実写寄り用途で具体的に言及される
- int4対応によりVRAM効率と速度で有利（RTX 50シリーズではint8フォールバック）
- 大型モデルで生成に1時間かかるケースがあり、画質と時間のトレードオフやNSFW時のプロンプト厳しさ・ワークフロー複雑さが課題

### 【モデル: その他のモデル】
- SD1.5は400it/s程度の速度が魅力で手軽な補助用途や成分摂取用に言及
- DaSiWa / EXITIUM VICTRIX（ブチギレ）は動画用途で動きの一貫性・ダイナミックさで比較される
- NovelAI (NAI)はv5リリースへの期待がある一方、テスター品質への不満も指摘
- モデル選択は即戦力画質・LoRA資産・速度/VRAM効率・用途（静止画/動画、実写/アニメ）のバランスで決まり、ComfyUIや量子化・TurboLoraが併用される

### 【モデル: Web検索による参考情報】
- Wan2.2 / AnimeGenはAlibaba開発のMoE動画生成モデルで、AnimeGenはAIdeaLabによるWan2.2ベースのアニメ特化版（T2V/I2V、Apache-2.0）として2025年頃公開予定

---
# 元の本文
**生成AIモデル人気傾向のまとめ（レポート冒頭）**

2026年時点のコミュニティログ（主にStable Diffusion / ComfyUIユーザー中心の議論）から、**Anima（特にAnima base / Aesthetic / Turbo版）** が圧倒的に主流・人気モデルとして位置づけられている。Illustrious（SDXL系、別名Rias/IL/Illustrious XL）が以前の主力だったが、Animaへの完全移行が進み、「SDXLは2026年でお役御免」「肥やし」との声が優勢。Krea2は実写寄り用途で併用され、Wan2.2ベースのAnimeGenは動画（特にアニメ調I2V/T2V）で言及される。SD1.5は速度重視の補助用途で残存。全体として、**生成速度・画質安定性・LoRA相性・ワークフロー簡易さ** がモデル選択の主な基準となっている。[[1]](https://www.reddit.com/r/StableDiffusion/comments/1jjubsr/what_is_illustriousillustriousxl/)[[2]](https://civitai.com/models/795765/illustrious-xl)

### Anima（最も言及が多く「一強」と評価）
- **言及の多さ**: ログ全体の中心。Anima base / Aesthetic v1.1 / turbo版の比較が頻出。
- **選ばれている主な理由**:
  - Illustrious比で顔の崩れが少なく、Face detailer不要で生成時間短縮。
  - TurboLora併用でさらに高速化（絵柄変化が少ない）。
  - Illustriousで生成したエロポーズのバリエーション作成に強い。
  - LoRAなしでもある程度高品質。アニメらしい動きや人体バランスが良好。
  - VRAM消費が少なく、int8/量子化との相性が良い。キャラLoRA成功率が高く、絵柄LoRA併用時の劣化が少ない。
  - Anima Edit（自然言語によるi2i/Edit LoRA的な機能）で服装・髪色変更などが容易。
- **注意点**: Turbo使用者は低ステップで画質低下しやすいため批判される場合あり。学習時は解像度（512推奨）の選択が重要。

### Illustrious（Illustrious XL / Rias / IL、SDXL系）
- **言及の多さ**: Animaとの比較で多く登場するが、全体傾向として衰退。
- **選ばれている（または残っている）理由**:
  - SDXL特有の大量LoRA（特にマニアック/版権キャラ向け）がまだ使える。
  - 特定のキャラ再現性で今でも必要なユーザーあり。
- **課題**: 特定のポーズ・体型制御が難しく、Animaに移行する声多数。「もう要らん」との意見が優勢。

### Krea2（Krea 2 / Krea2 Large / Turboなど）
- **言及の多さ**: 実写寄り用途で具体的に語られる。
- **選ばれている主な理由**:
  - Animaとは「実写と二次で使い分ける」関係。自然言語プロンプトや画像参照が扱いやすい。
  - int4対応によるVRAM効率・速度面の利点（ただしRTX 50シリーズではint8フォールバック）。
- **課題**: 生成に1時間かかる大型モデルもあり、画質 vs. 時間のトレードオフ。NSFW時のプロンプトシビアさやワークフローの複雑さ（多段サンプラーなど）が指摘される。

### Wan（Wan2.2）およびAnimeGen
- **言及の多さ**: 少数だが、動画生成で登場。
- **選ばれている主な理由**:
  - AnimeGen（Wan2.2ベースの国産アニメ特化動画モデル、AIdeaLab公開、Apache-2.0）がテキスト→動画/画像→動画で利用可能。アニメらしい動き（日本のリミテッドアニメ感）が自然。
  - int8量子化による速度向上の可能性。
- **課題**: 重い（ダウンロード・生成ともに）、一貫性や解像度面で試行錯誤しにくい声あり。

### その他のモデル
- **SD1.5**: 速度（400it/s程度）が魅力で、手軽さ重視の補助用途。「定期的に成分を摂取」する参考モデルとして言及。
- **DaSiWa / EXITIUM VICTRIX（ブチギレ）**: 動画用途で動きの一貫性やダイナミックさで比較される。
- **NovelAI (NAI)**: v5リリース期待の声はあるが、テスター品質への不満も。
- **言及ほぼなし**: FLUX、Qwen-Image、Z-Image（ZIT）、LTXなど。

**全体傾向の補足**: モデル選択は「即戦力の画質」「特定LoRA資産」「生成速度・VRAM効率」「用途（静止画/動画、実写/アニメ）」のバランスで決まる。ComfyUIワークフローや量子化（int4/int8）、TurboLoraなどの最適化が併用される。

## Web検索による参考情報
- **Illustrious XL**: OnomaAI Research開発のSDXLベースイラスト/アニメ特化モデル。v0.1（2025年2月頃公開）からv1.0などで1536pxネイティブ対応など高解像度強化。Kohaku XLを基盤にillustration/animation最適化。[[1]](https://www.reddit.com/r/StableDiffusion/comments/1jjubsr/what_is_illustriousillustriousxl/)[[2]](https://civitai.com/models/795765/illustrious-xl)
- **Wan2.2 / AnimeGen**: Alibaba（Wan AI / Tongyi Lab）開発の動画生成モデル（MoEアーキテクチャ、高ノイズ/低ノイズexpert）。2025年頃にAnimate-14Bなどが公開。AnimeGenはAIdeaLab（日本企業、GENIAC支援）によるWan2.2ベースのアニメ特化ファインチューニング版（T2V/I2V、Apache-2.0ライセンス）。既存Wanエコシステム活用可能。[[3]](https://github.com/Wan-Video/Wan2.2)[[4]](https://huggingface.co/aidealab/AnimeGen-T2V)
- **Krea2**: Krea.aiの独自画像生成モデル（Krea 2 Turbo/Rawなど）。美学重視・リアルタイム生成・4Kネイティブ対応。Fluxなども統合したクリエイティブスイート。オープンソース版やLoRAも存在。[[5]](https://www.krea.ai/)[[6]](https://huggingface.co/krea)

Animaについては公開検索で具体的な公式情報が確認できなかった（コミュニティ固有のファインチューニングモデルである可能性が高い）。情報はログに基づく。
