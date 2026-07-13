# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI / comfy / 関連ノード・ワークフロー（最多言及）
- comfy-kitchen: INT8 ConvRot時、古いPyTorchでCUDAバックエンド無効化により不安定化する注意

### ツール: WebUI系 / Forge Neo / EasyForgeNeo / forgeneo
- A1111 Forge派生/フォークで、Anima/リアス等の手軽運用・起動時ブラウザ制御・用途別バッチ分けに使用
- ブラウザウィンドウサイズ（全画面/最小化等）による生成速度差の検証多数（ほぼ誤差か環境依存寄り）

### ツール: 学習・LoRA関連ツール
- musubi (Musubi Tuner): 3090で高速化全オプション試行、Krea2 LoRAはAnima比3〜4倍時間、Wan2.2等動画系対応
- 選択理由: 高速化オプションが充実
- addift (ADDifT): 画像ペア1組（multi可）で学習可能、TrainTrain拡張等に実装
- 選択理由: 手軽に学習できる点と手法発案者を評価
- kohya_ss v26.0.0: Lumina Image 2.0・Native LoHa/LoKr・HunyuanImage-2.1・LECO・Inpainting・ControlNet-LLLite・torch.compile等対応、X生成法にkohyaニキが驚いた速報
- Omusubi_Krea2_gui: 他GUI過多で方向性変更、学習過程量子化に挑戦中（int8ConvRotは学習不適）
- Fizgig (verアップ): Krea 2 trainer固有機能（live dataset curator、problem images検出、Per-image adaptive LR等）
- その他: 学習過程の量子化が重要との指摘

### ツール: 量子化・高速化・変換ツール（INT8/INT4 ConvRot / 昆布化）
- INT8 ConvRot（昆布化）が活発、turbo+turbo LoRA 6stepで約1/3時間・動画系で約半分、ctqや--exclude-layers・--simple推奨等の詳細議論
- 注意点: 構図固定化・細部簡略化は不可避、英語圏の無劣化誤解、kijai変換済み信頼派、Radeon INT8動作・50シリーズはint8使用
- Claude活用: 変換ツール作成・設定/メタデータ分析・量子化改善ループに使用
- comfy-model-tools / ctq: 変換の中心ツール

### ツール: プロンプト変換・リライター・補助ツール
- Danbooru tags → natural-language prompt converter: 前スレ続きで導入、タグを自然言語化
- Qwen3.6-27Bリライター: 自然言語をjson強化、動画カット/長尺制御向上期待、Wan2.2のMoE的速度可能性
- 選択理由: プロンプト構造化による制御性向上と速度期待
- LMStudio: サブセットでエロ絵生成可否の質問
- GPT/Claude/Grok/Codex: WF作成・変換ツール生成等の相談用、エロ混じりで不安定、Grok推奨あり

### ツール: 後処理・2D→3D / VR / 編集ツール
- Owl3D / iw3: 生成動画の立体・VR化、Owl3Dは簡単高品質、iw3は無料高速だが設定癖あり、ダヴィンチ編集→Owl→クエスト運用
- 選択理由: 立体臨場感、無料/簡単/高品質
- Anydepth: 奥行き付き作成事例（UI不便でエロ貢献せず終了）
- Blender MCP: LLM進化で実用化、単純タスクは完全任せ可能

### ツール: その他関連ツール・サービス
- PixAI: エロ動画生成可能との話、無規制Grok級なら課金意向も話題化しにくいとの見方
- Civitai: int8モデル用項目の要望（既存だが設定未変更の場合あり）
- NAIA / hermes agent: 温かみ制御や有用性への言及（詳細不明瞭）
- ブラウザ/OS関連: WSL Ubuntuアップグレード・Python/cu130等で速度改善事例

### ツール: 全体の特徴・トレンド
- 手軽さ vs 柔軟性: Forge Neoは入門向け、ComfyUIはカスタム/上級者向け
- 学習の民主化: 1ペア学習のaddiftや高速musubi、特化GUI
- エコシステム連携: ComfyUI＋量子化＋学習ツール＋LLM補助が主流、後処理でVR臨場感向上
- 課題: 設定複雑さ・品質トレードオフ・環境依存（PyTorch/CUDA）・メタデータ/ブラウザ影響
- コミュニティはローカル高性能生成を追求しつつ最適化と手軽さの両立を図っている

### ツール: Web検索による参考情報
- モデル名・バージョン・新サービス等の事実確認結果（2026年7月頃情報、主要ソース引用）
- ComfyUI: 最新v0.27.0前後、INT8 ConvRotネイティブ対応、comfy-kitchenは高速カーネル、comfy-model-toolsはパッケージング用
- Forge Neo / EasyForgeNeo: Haoming02のsd-webui-forge-classic neoブランチ、Flux/Qwen/Wan等対応の軽量高性能後継
- kohya_ss v26.0.0: Lumina/Anima/Hunyuan等多数対応、musubi-tunerは別リポジトリで動画/FLUX等LoRA対応
- INT8 ConvRot（昆布化）/ctq: ComfyUIネイティブ進行中、ConvRotで品質維持INT8、ctq主流、Krea2等で大幅高速化、--simple/group-size重要
- ADDifT (addift): TrainTrain拡張実装、2枚差分から高速LoRA学習、1ペア手軽さが特徴
- Krea 2: Krea AIの美学重視OSS画像基盤（2026頃）、Turbo版・Identity Edit LoRAあり、ComfyUI対応活発
- Qwen3.6-27B: 2026年4月頃の27B dense、エージェント/コーディング高性能、リライター/ローカルLLM向け
- Owl3D / iw3: Owl3Dは商用簡単高品質2D→3D、iw3は無料OSS代替（高速・設定癖あり）、VR/クエスト向け
- PixAI: アニメ特化オンライン生成、I2V強化でエロ動画可能性に合致
- Blender MCP: BlenderとLLMをMCP連携、自然言語3D操作が実用化中
- その他: Danbooruタグ⇔自然言語変換は複数存在、LM Studioは一般的ローカルLLMランナー、NAIA/hermesは明確一致少なく文脈依存
- 上記は議論の信頼性を裏付け最新進化（特に量子化とComfyUI統合）を反映、使用時は公式最新を確認

---
# 元の本文
**生成AI関連ツール レポート**

本レポートは、提供されたコミュニティログ（主に日本のAI画像/動画生成関連スレッド）から抽出された生成AI関連「ツール」の話題を整理・まとめたものです。純粋なモデル比較・画質議論は除外し、ツール（UI、ワークフロー/ノード、学習ツール、量子化/変換ツール、プロンプト変換、後処理ツールなど）に焦点を当てています。選択理由が明示されている場合は併記しています。

議論の中心は**ComfyUIエコシステム**で、操作性や量子化対応の優位性が繰り返し強調されています。次いでForge Neo（WebUI系）、LoRA学習ツール、量子化手法（INT8 ConvRot/昆布化）、2D→3D後処理ツールが活発に言及されています。全体として、速度向上・VRAM削減・手軽さ・制御性向上を目的としたツール選択が特徴的です。

### 1. ComfyUI / comfy / 関連ノード・ワークフロー（最多言及）
- **概要と用途**: ノードベースのモジュール型UI/エンジン。画像・動画生成、インペイント、合成、量子化モデル対応などで広く使用。バージョン0.27.0の言及あり（WSL環境アップグレード後の動作確認）。ワークフロー（WF）共有・作成が前提の話題多数（Krea2用WF、動画自動モザイク用WF、画像参照インペイントWF、krea2-identity-editなど）。
- **具体的なノード/機能**:
  - MosaicCreatorノード（動画チンポ自動モザイクWF作成の試み。ChatGPT相談時に挙動不安定の指摘。エロ用途ではGrok推奨の声）。
  - ReferenceLatentノード（QIEのピクセルシフト防止。去年からあったが効果に疑問）。
  - Image Compositeノード（透過レイヤー合成。SAM3+Krea2との組み合わせで手書き文字合成など）。
  - とりにくネキ公開の「Qwen Image Edit2511用ピクセルシフトが一切起きないノード」（非常に優秀と評価）。
  - INT4/INT8対応（ComfyUI-INT4-Fastなど。ネイティブマージも進行中）。
- **操作性・環境関連**:
  - レイアウト調整のしやすさ＋マウスホイールズームでどの解像度/画面サイズでも快適。A1111系より優位。
  - 多ボタンマウスでショートカット登録すると非常に便利。
  - VRAM管理が改善され、12GB環境でも溢れにくくなった。
  - ブラウザウィンドウサイズ（最小化/最大化）が速度に影響する可能性の議論（環境依存、誤差レベルの結果も）。
  - comfy-kitchen: INT8 ConvRot化時にPyTorch古いとCUDAバックエンド無効化で不安定になる注意。
  - comfy-model-tools: デフォルト設定だとシンプル高速モードで変換され微妙な出来になりやすい。comfy-org公式は最適化が入っている可能性。
  - メタデータ圧縮要望（WF埋め込み時）。
  - GPT/CodexによるWF作成・修正が実用的になってきた（以前は無理が常識だった）。
- **選択理由**: 配置の柔軟性・ズーム操作性の高さ（A1111系比較）、VRAM管理改善による低スペPC対応、量子化ネイティブ対応による高速化、ノードの豊富さでカスタムWFが組みやすい。低スペPCでも早くてエロいKrea2 WFを求める声など。
- **その他**: int8/int4 ConvRotとの組み合わせが活況。バージョンアップで速度向上の可能性（見た目変化程度のリスク）。

### 2. WebUI系 / Forge Neo / EasyForgeNeo / forgeneo
- **概要と用途**: A1111 Forgeの派生/フォーク。手軽なUIとしてAnima/リアスなどのモデル運用に使用。起動時ブラウザ制御や用途別バッチ分けの話題。
- **特徴的な議論**:
  - ブラウザウィンドウサイズ（全画面/最小化/小さく）による生成速度差の検証多数（ほぼ誤差レベルか環境依存の結論寄り。Win10+2080Ti、WQHD+firefox+rx9070など）。
  - 「forge neoを使ってる層は浅瀬チャプチャプ勢」との位置づけ（入門・手軽さ向け）。
  - 起動時自動ブラウザ変更方法（System設定でDisableにし、手動orバッチで制御。ChatGPTにバッチ作成依頼で解決）。
- **選択理由**: 手軽に動かす程度の入門向け。ウィンドウサイズ操作で速度向上が期待できる場合があるが、毎回操作が面倒との改善要望。

### 3. 学習・LoRA関連ツール
- **musubi (Musubi Tuner / kohya-ss/musubi-tuner)**: 3090で高速化オプション全部つけてLoRA学習を試行。Krea2 LoRAがAnima比で3〜4倍時間がかかる文脈。Wan2.2など動画系対応。
  - **選択理由**: 高速化が期待できるオプション充実。
- **addift (ADDifT / Alternating Direct Difference Training)**: 画像ペア1組だけで学習可能（multi組み合わせも）。TrainTrain拡張などに実装。
  - **選択理由**: 気軽に（手軽に）学習できる点。手法発案者を評価。
- **kohya_ss (v26.0.0)**: アップデート詳細言及。Lumina Image 2.0 LoRA/full fine-tune、Native LoHa/LoKr、HunyuanImage-2.1 LoRA、LECO、Inpainting、ControlNet-LLLite、torch.compile、timestep visualizationなど。Xでの生成方法にkohyaニキが驚いたとの速報。
- **Omusubi_Krea2_gui**: 他GUIが多いため方向性変更。LLM実用済みの学習過程量子化に挑戦中（int8ConvRotは推論向けで学習には不適）。
- **Fizgig (verアップ)**: Krea 2 trainerの特徴（live dataset curator、problem images検出、Per-image adaptive LR、Auto-recaption stuck images、Warm up look outliersなど。他trainerにない機能）。
- **その他**: 学習過程の量子化が重要との指摘。

### 4. 量子化・高速化・変換ツール（INT8/INT4 ConvRot / 昆布化）
- **概要**: INT8 ConvRot（昆布化）が非常に活発。turboモデル＋turbo LoRAで6step運用でノーマルの約1/3時間。動画系（Wan2.2など）でほぼ半分。10erosもint化可能。ctqツール（convert_to_quant、`ctq -hf`でプリセット確認）やきままさん設定、--exclude-layers、--dynamic-convrot注意（現時点非推奨、固定group-size推奨）、AdaRound問題（時間がかかりすぎ、--simple推奨）など詳細議論。
- **注意点**: 構図固定化・細部簡略化は避けられない。英語圏で「bf16無劣化高速化」と誤解する人も。自分で変換すると設定が多くkijai変換済み信頼派も。ComfyUI-INT4-Fastなど。RadeonでもINT8デフォルト動作事例。50シリーズはint4非対応でint8使用。
- **Claude活用**: 変換ツール作成、comfy公式設定/メタデータ分析、量子化改善ループに使用。
- **選択理由/効果**: 大幅な高速化（1/2〜1/3）とVRAM削減。品質・構図の副作用あり。ComfyUIネイティブ対応で調整なしでも高精度の場合あり。ベストは層ごとに4/8/16bit切り替え。
- **comfy-model-tools / ctq**: 変換の中心ツール。

### 5. プロンプト変換・リライター・補助ツール
- **Danbooru tags → natural-language prompt converter**: 前スレ続きで導入表明。タグを自然言語に変換。
- **Qwen3.6-27Bをリライターとして**: 自然言語をjsonに強化。動画生成のカット指定・長尺制御性向上を期待。Wan2.2がMoEっぽく速い可能性。
  - **選択理由**: プロンプト構造化による制御性向上と速度期待。
- **LMStudio**: サブセットでエロい絵が作れるかの質問。
- **GPT/Claude/Grok/Codex**: 相談用（WF作成、変換ツール生成、設定分析、バッチ作成）。エロ混じりで挙動不安定の指摘あり。Grok推奨の声。

### 6. 後処理・2D→3D / VR / 編集ツール
- **Owl3D / iw3**: 生成動画の立体化・VR化。Owl3Dは設定簡単で出来が良い。iw3は無料で早く評判良いが設定癖あり。ダヴィンチで編集してOwlでVR化してクエストで堪能。
  - **選択理由**: 立体的で臨場感が出る。無料/簡単/高品質。
- **Anydepth**: 奥行き付き作成事例（UI不便でエロさに貢献せず終了）。
- **Blender MCP**: LLM進化で実用的に。凝ってないタスクなら完全任せ可能。

### 7. その他関連ツール・サービス
- **PixAI**: エロ動画生成可能らしい。無規制Grokくらいなら課金したいが話題に上がらないのでは。
- **Civitai**: int8モデル用項目の要望（既にあるが設定未変更の場合あり）。
- **NAIA / hermes agent**: 言及あり（温かみのある制御や役立ち疑問）。詳細不明瞭。
- **ブラウザ/OS関連**: WSL Ubuntuアップグレード、Pythonバージョン、cu130などで速度改善事例。

**全体の特徴・トレンド**:
- **速度・効率最優先**: 量子化（INT8 ConvRot中心）とUI操作性で生成時間/VRAMを削減。副作用への注意喚起も多い。
- **手軽さ vs 柔軟性**: Forge Neoは入門向け、ComfyUIはカスタム/上級者向けで選ばれる。
- **学習の民主化**: 少数画像（1ペア）で可能なaddiftや高速musubi、特化GUI。
- **エコシステム連携**: ComfyUI + 量子化 + 学習ツール + LLM補助が主流。後処理でVR臨場感向上。
- **課題**: 設定の複雑さ、品質トレードオフ、環境依存（PyTorch/CUDAバージョン）、メタデータ/ブラウザ影響。

このログから、コミュニティはローカル高性能生成を追求しつつ、ツールの最適化と手軽さを両立させようとしている様子がうかがえます。

## Web検索による参考情報
以下、モデル名・バージョン・新サービス等についてWeb検索で事実関係を確認した結果です（2026年7月頃の情報に基づく）。主要ソースを引用。

- **ComfyUI**: 最新はv0.27.0前後（2026年6月末リリース）。INT8 ConvRotモデルのネイティブサポートが追加。comfy-kitchenは高速カーネルライブラリ（CUDA/Tritonバックエンド）。comfy-model-toolsはモデルパッケージング用ユーティリティ。[[1]](https://github.com/comfy-org/ComfyUI/releases)[[2]](https://github.com/comfy-org/comfyui)[[3]](https://github.com/Comfy-Org/comfy-kitchen)[[4]](https://github.com/Comfy-Org/comfy-model-tools)

- **Forge Neo / EasyForgeNeo**: Haoming02によるsd-webui-forge-classicのneoブランチ。最新ForgeベースでFlux/Qwen/Wanなど現代モデル対応、軽量・高性能。A1111/Forgeの後継的位置。[[5]](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)[[6]](https://www.reddit.com/r/StableDiffusion/comments/1n7fd2v/introducing_sdwebuiforgeneo/)

- **kohya_ss v26.0.0**: 2025-2026頃リリース。Lumina Image 2.0、Anima、HunyuanImage-2.1、Native LoHa/LoKr、LECO、Inpainting、ControlNet-LLLite、torch.compileなど多数対応。musubi-tunerは別リポジトリ（kohya-ss/musubi-tuner）でHunyuanVideo/Wan2.x/FLUX/Qwen-Image/Z-ImageなどのLoRA/full fine-tune対応。[[7]](https://github.com/bmaltais/kohya_ss)[[8]](https://github.com/kohya-ss/musubi-tuner)

- **INT8 ConvRot（昆布化） / ctq (convert_to_quant)**: ComfyUIネイティブ対応進行中。ConvRotは重みの回転による外れ値抑制で品質維持しつつINT8量子化。silveroxides/convert_to_quant（ctqコマンド）が主流。Krea2/Z-Imageなどで速度大幅向上（FP8超えの場合も）、VRAM削減。--simpleやgroup-size指定、exclude-layersなどが重要。INT4も議論中。[[9]](https://www.reddit.com/r/StableDiffusion/comments/1ukjhag/krea2_int8_convrot_vs_fp8_scaled_in_comfyui_270/)[[10]](https://huggingface.co/obsxrver/ComfyUI-Native-INT8_ConvRot)[[10]](https://huggingface.co/obsxrver/ComfyUI-Native-INT8_ConvRot)

- **ADDifT (addift)**: hako-mikan/sd-webui-traintrain拡張に実装。2枚の差分画像から直接LoRAを高速学習（コピー機学習より速い）。Multi-ADDifT対応。1ペアで可能な手軽さが特徴。[[11]](https://github.com/hako-mikan/sd-webui-traintrain)

- **Krea 2 (Krea2)**: Krea AIのオープンソース画像基盤モデル（美学重視、2026年頃）。Turbo版、Identity Edit LoRA（画像編集強化）などあり。ComfyUI対応活発。[[12]](https://www.krea.ai/krea-2)[[13]](https://huggingface.co/krea/Krea-2-Turbo)

- **Qwen3.6-27B**: Alibaba Qwenチームの2026年4月頃リリースの27B denseモデル。エージェントコーディング性能が高く、前世代MoEを上回る部分も。リライター/ローカルLLM用途に適す。HF/Ollama/LM Studio対応。[[14]](https://qwen.ai/blog?id=qwen3.6-27b)[[15]](https://huggingface.co/Qwen/Qwen3.6-27B)

- **Owl3D / iw3**: Owl3DはAIベースの商用2D→3D動画変換ソフト（設定簡単・高品質）。iw3はnagadomi/nunifの無料オープンソース代替（SBS 3D変換、設定に癖ありだが高速・高評価）。VR/クエスト向け。[[16]](https://www.owl3d.com/)[[17]](https://github.com/nagadomi/nunif/blob/master/iw3/README.md)

- **PixAI**: アニメ特化のオンラインAI画像/動画生成プラットフォーム。I2V（Image-to-Video）機能が強化され、エロ動画生成の可能性言及に合致。無料クレジットあり。[[18]](https://pixai.art/theme/i2v)[[19]](https://pixai.art/en)

- **Blender MCP**: BlenderとLLM（Claudeなど）をModel Context Protocolで連携させるツール。自然言語で3D操作可能。実用性が向上中。[[20]](https://github.com/ahujasid/blender-mcp)

- **その他**: Danbooruタグ⇔自然言語変換は複数のLLMベースツール/拡張が存在（text2tagsなど）。LM StudioはローカルLLMランナーとして一般的。NAIA/hermes agentは特定ツールとして明確な一致が少なく、文脈依存の可能性。

これらの情報はコミュニティ議論の信頼性を裏付け、最新のツール進化（特に量子化とComfyUI統合）を反映しています。実際の使用時は公式リポジトリや最新リリースを確認してください。
