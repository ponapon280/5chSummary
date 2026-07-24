# 🆕 新規トピック（前回からの差分）
### 環境構築・トラブルシューティング
- ComfyUIワークフロー共有、PyTorchバージョン問題、negpip小技が話題

### ハードウェア事情
- VRAMの重要性が強調され「8GB→16GBで世界が変わる」「12GBは敗落者」「5060 Ti以上推奨」との声多数
- 4070 Ti（16GB）や5070 Ti搭載PCのコスパ、BTO各社比較、RAM 32GB→64GB移行検討が話題
- 夏場のGPU発熱（3060/4090）、VRAM溢れ確認方法、OCCT/3DMark負荷テスト、温度監視、電源・BIOS対応策が共有

### モデル・LoRA関連の比較・運用
- Krea2は自然言語プロンプト・スタイル再現性・液体表現に優位、RAW/Turbo版あり、LoRA反映の弱さとVRAM消費多さが指摘
- NAI v5は日本語対応・NSFW扱いやすさ・キャラ配置でゲームチェンジャー期待も未リリースのため判断保留
- T-LoRA/概念LoRA、small breastsタグ制御、ブロックウェイト調整、Fizgig/aitoolkitによるLoRA学習（dim/alpha設定、過学習対策）が話題

### NSFW生成・運用
- Krea2でのエロ生成でPrompt WeightやDenoising Strength=1の活用報告
- 日本国内のモザイク規制・法人リスクを懸念しローカル環境の強みを再確認
- 画像アップロード注意点としてWebP非対応、メタデータ削除、児童ポルノ禁止が共有
- Geminiのエロロールプレイ実用性（検閲比較的緩い）、Grokとの比較、失敗例（髪の毛残り、アナル描写破綻）が話題

### その他の話題
- プロンプト効き方（位置指定・細部指定）、モデルマージ体感、WAI/Z-image動向が話題
- マネタイズ話は暗黙の了解で避ける傾向
- 暑さネタ（エアコン・室温）と生成活動への影響が共有

### 傾向・特徴
- 技術志向のライト〜ミドル層が多く、最新コミット追従や量子化を積極的に試す一方「環境をクリーンに保つ」「最新版を追いすぎない」現実的アドバイスも目立つ。検閲の緩さ・実用性・ローカル制御を重視し、ハイプへの辛口評価や実践主義が特徴

### Web検索による参考情報
- Krea-2はKrea AIのtext-to-imageモデルで高審美性・スタイル多様性向け、RAW/Turbo版あり、ComfyUI最適化モデルがHugging Faceで利用可能
- NovelAI v5は2026年時点で未リリース（V4.5が最新）、テスター募集や開発中との言及あり
- 情報は2026年7月時点の公開ソースに基づく

---
# 元の本文
**なんJ AI画像生成スレッド 要約レポート**

### スレッド概要
主に**ローカルAI画像生成（Stable Diffusion系）**をテーマにした技術・運用スレッド群。ComfyUI / Forge Neo / Stability Matrixを中心とした環境構築、NSFW生成Tips、GPU/VRAM事情、モデル比較（Anima・Krea2・WAN/Wan2.2・NAIなど）が活発に議論されている。エロ規制やアップロード時の注意点も散見され、ローカル環境の優位性が再確認される傾向が強い。

### 主要トピック

**1. 環境構築・トラブルシューティング**
- **Anima LLLite**の動作不具合報告が多く、`anima-lllite`モデルを`models\controlnet\`から`models\model_patches\`へ移動し、ModelPatchLoaderノードを追加してApply Anima ControlNet-LLLiteに接続する解決策が共有された。strength / start_percent / end_percentの再設定も推奨。
- Forge Neoのバージョン問題（classicブランチ固着）が頻発。Stability Matrixの「Change Version」でneoブランチへ移行する方法が有効。
- Stability Matrixのデメリット（独自バグ・切り分けの煩雑さ） vs メリット（モデル管理の楽さ）が議論された。
- ComfyUIワークフロー共有、PyTorchバージョン問題、negpipなどの小技が話題に。

**2. ハードウェア事情**
- VRAMの重要性が強調され、「8GB→16GBで世界が変わる」「12GBは敗落者」「5060 Ti以上（Blackwell世代）推奨」との声多数。
- 4070 Ti（16GB）や5070 Ti搭載PCのコスパ、BTO（サイコム・ドスパラ・FRONTIERなど）が話題。RAMは32GB→64GBへの移行検討も。
- 夏場のGPU発熱（3060/4090）、VRAM溢れ確認方法、OCCT/3DMark負荷テスト、温度監視、電源・BIOS問題への対応策が共有された。

**3. モデル・LoRA関連の比較・運用**
- **Anima**（DiT系アニメ特化、2Bパラメータ）：線や肌の扱いが安定しやすく、高解像度（1536×1536〜2k程度）ポン出しが強い。Hires.fixとの相性が悪く（ノイズ増えやすい）、代わりに1MP生成＋外部アップスケーラー（ESRGAN、SeedVR2、RTX VSR）やタイルドimg2imgが推奨。性器描写の弱さ（陶器っぽい、ジューシーさ不足）やLoRA相性の指摘あり。
- **Krea2 / Krea-2**：自然言語プロンプトが強く、スタイル再現性・液体/スライム表現に優位。RAW（LoRA学習用）とTurbo（推論用）があり、LoRA反映の弱さやVRAM消費の多さが指摘される。
- **WAN / Wan2.2**：動画生成で注目。INT8量子化版の速度・品質トレードオフが議論され、fp8の方がまだマシとの意見も。
- **NAI（NovelAI、特にv5）**：日本語対応・NSFW扱いやすさ・キャラ配置機能で「ゲームチェンジャー」期待が高いが、未リリースのため判断保留の声も。
- その他：T-LoRA/概念LoRA、small breastsタグ制御、ブロックウェイト調整、Fizgig/aitoolkitによるLoRA学習（dim/alpha設定、過学習対策）。

**4. NSFW生成・運用**
- Krea2でのエロ生成で「Prompt Weight」やDenoising Strength=1の活用報告。
- 日本国内のモザイク規制・法人リスクを懸念し、ローカル環境の強みを再確認。
- 画像アップロード注意点（WebP非対応、メタデータ削除、児童ポルノ禁止）。
- Geminiのエロロールプレイ実用性（検閲比較的緩い）、Grokとの比較、具体的な失敗例（髪の毛残り、アナル描写破綻など）も話題。

**5. 量子化・パフォーマンス**
- krea2_turboシリーズ（int4_convrot、nvfp4、INT8 ConvRot）やWANのINT8/FP8量子化の速度・品質比較。
- VRAM12GB環境での動作試み、Text Encoder量子化（Qwen3VL系）。

**6. その他の話題**
- プロンプト効き方（位置指定・細部指定）、モデルマージ体感、WAI/Z-image動向。
- マネタイズ話は暗黙の了解で避ける傾向。
- 暑さネタ（エアコン・室温）と生成活動への影響。

### 傾向・特徴
技術志向のライト〜ミドル層が多く、最新コミット追従や量子化を積極的に試す一方、「環境をクリーンに保つ」「最新版を追いすぎない」という現実的なアドバイスも目立つ。検閲の緩さ・実用性・ローカル制御を重視する空気感が強く、ハイプへの辛口評価や実践主義（画像を出せ）が特徴的。

### 総評
技術的な情報交換が中心の実用的なスレッド群。Anima/Krea2の具体的な運用Tips、Hires.fix代替手法、量子化による軽量化、VRAM重要性、Forge Neoバージョン管理など即戦力情報が豊富。エロ生成に特化したローカル勢の知見が集積された良スレと言える。NovelAI v5への期待も背景に、ローカル vs クラウドの勢力図変化が匂わされる内容となっている。

## Web検索による参考情報
- **Anima**: CircleStone LabsとComfy Orgによる2Bパラメータのアニメ特化テキスト-to-画像モデル（DiTベース）。Hugging Faceで公開され、ComfyUIワークフロー対応。Anima-LLLiteはkohya-ssによる軽量ControlNet-LLLite実装で、ComfyUIカスタムノードが存在。[[1]](https://huggingface.co/circlestone-labs/Anima)[[2]](https://huggingface.co/kohya-ss/Anima-LLLite)
- **Krea-2 (Krea2)**: Krea AIのテキスト-to-画像モデル。高審美性・スタイル多様性向けで、RAW（LoRA学習用）とTurbo（高速推論用）バリアントあり。ComfyUI最適化モデルがHugging Faceで利用可能。[[3]](https://docs.comfy.org/tutorials/image/krea/krea-2)
- **Wan2.2 (WAN / Wan)**: Alibaba/Wan-Videoによるオープンソース動画生成モデル（MoEアーキテクチャ採用）。テキスト-to-ビデオ・画像-to-ビデオ対応で、ComfyUIで動作。2025年頃リリースのApache 2.0モデル。[[4]](https://github.com/Wan-Video/Wan2.2)[[5]](https://www.thundercompute.com/blog/wan-2-2-comfyui-ai-video-model)
- **NovelAI v5**: 2026年時点で未リリース（V4.5が最新）。V5のテスター募集や開発中との言及あり。[[6]](https://x.com/novelaiofficial?lang=en)
- **Forge Neo / Stability Matrix**: Forge（A1111系フォーク）のneoブランチと、Stable Diffusion環境管理ツール。バージョン切り替え機能が利用される。
- **Anima LLLite**: Anima DiT向けの軽量ControlNet-LLLite。kohya-ssのトレーニング/推論ガイドとComfyUIノードが存在。[[7]](https://github.com/kohya-ss/ComfyUI-Anima-LLLite)

これらの情報は2026年7月時点の公開ソースに基づく。
