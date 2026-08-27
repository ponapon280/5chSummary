# 🆕 新規トピック（前回からの差分）
### ツール: 全体
- PixAIはクラウド型AI画像生成プラットフォームで、無修正高品質生成・LoRA対応が評価される一方、Googleログイン強要が敬遠される。
- FreeTokenはMoE特化ローカル推論エンジンで、GGUF対応の弱さとDenseモデル比の移行メリットの少なさが指摘される。
- Irodori-TTS（v4 Small / v4.1 Small）は日本語TTSツールで、Emoji制御・音声クローニングの品質が高くASMR用途で評価される。
- Draw ThingsはiOS/macOS向けローカルオフライン画像生成アプリで、単体デバイス完結の手軽さとプライバシー保護が利点。
- Krea（Krea 2 / Krea3相当）はスタイル転送・美学重視の画像生成スイートで、LoRA相性とリアルタイム編集の柔軟性が評価される。
- Davinci Resolveは動画編集ソフトでモーショントラッキング性能が優秀とされ、手動作業の多用途性が選ばれる理由。

### ツール: その他の言及
- LM Studio / llama.cppはFreeTokenとの比較でエラー報告や差別化の少なさが言及される。
- SillyTavernは公式フロントエンドとしての位置づけが言及される。
- Eagleは画像管理・自動転送スクリプトとの組み合わせが言及される。
- minimax関連ツールはComfyUI統合での動画生成速度・柔軟性が言及される。

### ツール: Web検索による参考情報
- PixAIはMetanomaly株式会社（東京都渋谷区）運営の日本AI二次元創作プラットフォームで、グローバル登録ユーザー1,500万人突破。
- Irodori-TTS v4 Smallは2026年8月頃にHugging Face公開の766MパラメータFlow Matchingベース日本語TTSで、Emoji制御・MITライセンス対応。
- Draw ThingsはiOS/macOS向け無料オフラインAI画像生成アプリ（2022年開始）で、Stable Diffusion系や大型モデルをローカル実行可能。
- Krea 2は2026年5月頃に発表された自社基盤画像モデルで、スタイル転送・美学重視のMedium/Large/Turboバリアントを持つ。
- FreeTokenは2026年8月頃にUC Berkeley/UT Austinチームが提案したMoE特化ローカル推論エンジンで、Apache-2.0ライセンス・単GPU動作対応。
- これらの情報は2026年8月時点の公開情報に基づく。

---
# 元の本文
**ComfyUI**は、ノードベースのワークフローで画像・動画生成を行うオープンソースツールとして複数回抽出されており、VRAM管理の向上、カスタムノードによる柔軟な拡張性、純正ノードでのエラー解決力、ワークフローJSON形式によるAPI連携・自動化のしやすさ、量子化ツール（ComfyUI Quantization Toolkit + comfy-model-tools）による軽量化などが評価されている。理由として、低VRAM環境（例: RTX 3060 + 32GB RAM）でのFP8厳しい場合のW4A8量子化によるサイズ削減、プロンプト正規化・結合などのカスタムノード作成による完全自動化の布石、生成速度向上（特に低解像度i2i）、LoRAの柔軟適用などが挙げられる。[[1]](https://comfyui-wiki.com/en/news)[[2]](https://github.com/Comfy-Org/ComfyUI/tags)

**PixAI**は、クラウドベースのAI画像生成プラットフォーム（Metanomaly株式会社運営）で、無修正高品質生成、独自LoRA対応による拡張性が評価され、日本法人である点やGoogleログイン強要のデザインが敬遠される一方、手軽なクラウド利用が利点として言及される。[[3]](https://prtimes.jp/main/html/rd/p/000000055.000173726.html)

**FreeToken**は、MoEモデル特化のローカル推論エンジンで、GGUF対応の弱さやllama.cppとの差が少ない点がネックとして挙げられ、DenseモデルよりMoE限定で移行メリットが薄いと評価される。理由として、公式対応モデルのみで量子化扱いが既存ツールと大差ない点が指摘される。[[4]](https://www.marktechpost.com/2026/08/23/meet-freetoken-an-edge-native-moe-serving-engine-that-runs-753b-glm-5-2-on-a-single-workstation-gpu/)

**Irodori-TTS（v4 Small / v4.1 Small）**は、日本語TTSツールで、Emojiによるスタイル・擬声制御、音声クローニングの品質・使い勝手がASMR用途などで高評価。公式IPキャラでも比較的緩い制限が選ばれる理由。[[5]](https://huggingface.co/Aratako/Irodori-TTS-v4-Small-Quantized)[[6]](https://jiazhuangai.com/articles/irodori-tts-v4-small-766m-tts-emoji-120-)

**Draw Things**は、iPhone/iPad/macOS向けローカルオフライン画像生成アプリで、単体デバイス完結の手軽さとプライバシー保護が利点。Animaサイズ程度の生成が可能で、ComfyUIとは別の用途として言及される。[[7]](https://drawthings.ai/)

**Krea（Krea 2 / Krea3相当）**は、スタイル転送・美学重視の画像生成・編集スイートで、LoRA相性や生成品質が話題。リアルタイム編集や参照画像活用の柔軟性が評価される。[[8]](https://www.krea.ai/blog/krea-2-image-model)

**Davinci Resolve**は、動画編集ソフトでモーショントラッキング性能（モザイク処理・複雑動き対応）が非常に優秀とされ、手動トラッキングや動画繋ぎ作業の多用途性が選ばれる理由。CapCutは課金が必要な代替として言及。[[9]](https://platform.minimax.io/docs/guides/video-generation)

**その他の言及**:
- LM Studio / llama.cpp：FreeTokenとの比較でエラー報告や差別化の少なさ。
- SillyTavern：公式フロントエンドとしての位置づけ。
- Eagle：画像管理・自動転送スクリプトとの組み合わせ。
- minimax関連ツール：ComfyUI統合での動画生成速度・柔軟性（真面目/エロ混在）。
- 自作/カスタムノードやeasywan：ComfyUI内での柔軟な検知・処理。

全体として、選ばれる理由は「手軽さ（クラウド/モバイル/シンプル構成）」「柔軟性（カスタム/LoRA/ワークフロー）」「性能差別化（VRAM管理・トラッキング・品質）」「既存環境との互換・差異」の観点が共通する。モデル関連（Wan、Anima、NAI、Qwen、MiniMax H3本体など）は除外。

## Web検索による参考情報
- **ComfyUI**：2026年8月時点でv0.34.1が最新タグ（8月26日）。MiniMax H3ネイティブサポート、CUDA Graphs、W4A8/INT8量子化対応ノード、Krea2/LTX2統合などが追加されており、VRAM効率化・カスタムノード拡張が活発。[[2]](https://github.com/Comfy-Org/ComfyUI/tags)[[1]](https://comfyui-wiki.com/en/news)
- **PixAI**：Metanomaly株式会社（東京都渋谷区）運営の日本AI二次元創作プラットフォーム。2026年6月時点でグローバル登録ユーザー1,500万人突破。Tsubaki.2などのモデル提供、LoRA対応が強み。[[3]](https://prtimes.jp/main/html/rd/p/000000055.000173726.html)[[10]](https://prtimes.jp/main/html/rd/p/000000036.000173726.html)
- **Irodori-TTS v4 Small**：2026年8月頃にAratakoによりHugging Face公開。766MパラメータのFlow Matchingベース日本語TTSで、Emoji制御・最大120秒参照音声対応。MITライセンス、量子化版もあり。[[5]](https://huggingface.co/Aratako/Irodori-TTS-v4-Small-Quantized)[[11]](https://huggingface.co/Aratako/Irodori-TTS-v4-Small)
- **Draw Things**：iOS/macOS向け無料オフラインAI画像生成アプリ（2022年開始、継続更新）。Stable Diffusion系や大型モデル（Qwen Imageなど）ローカル実行可能。[[7]](https://drawthings.ai/)[[12]](https://gigazine.net/news/20251017-draw-things-image-generation-iphone-macos/)
- **Krea 2**：2026年5月頃にKreaの自社基盤画像モデルとして発表。スタイル転送・美学重視、Medium/Large/Turboバリアントあり。リアルタイム編集・参照画像対応。[[8]](https://www.krea.ai/blog/krea-2-image-model)[[13]](https://www.krea.ai/docs/user-guide/features/krea-2)
- **FreeToken**：2026年8月頃にUC Berkeley/UT Austinチームが提案したMoE特化ローカル推論エンジン。Apache-2.0、expert offloadingで大規模MoE（GLM-5.2など）を単GPUで動作。PyPI/desktopアプリ提供。[[4]](https://www.marktechpost.com/2026/08/23/meet-freetoken-an-edge-native-moe-serving-engine-that-runs-753b-glm-5-2-on-a-single-workstation-gpu/)[[14]](https://www.mindstudio.ai/blog/freetoken-run-large-moe-models-locally)
- **MiniMax関連**：MiniMax H3はオープンウェイトのマルチモーダル動画生成モデル（T2V/I2Vなど）。ComfyUI統合が進んでいる。[[9]](https://platform.minimax.io/docs/guides/video-generation)

これらの情報は2026年8月時点の公開情報に基づく。
