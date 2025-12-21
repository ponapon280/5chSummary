### 抽出された「ツール」に関する話題

ログから生成AIに関連する「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana など）に該当する話題をすべて抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen など）に関する話題は除外。ツールが選ばれている理由（例: 軽量、高速、使いやすさ、LoRA対応など）が明記されている場合のみ、その点を併記。抽出順はログの登場順。

- **440**: nano banana を例に挙げ、プロンプトを箇条書き（例: 「〇〇の画像以下の条件で生成してください。 - 画像のタッチは劇画調 - キャラクターは…」）やyaml/markdown形式で入力すると「と思った通りにはなる…かも」と好印象。**理由: AIの解釈が良くなる（備忘録・やることリスト風が有効）**。

- **445**: ZIT で「Yellow thin cotton hairband with large ribbon on top middle of hairband.」→リボンが真ん中に出ない問題に対し、「Yellow large ribbon on top of forehead, and cotton yellow hairband beneath the ribbon.」に変更したらリボンが真ん中に出るようになった。**理由: 伝え方の習熟で精度向上**。

- **454**: Janku 使ってみたけど「発色と目がむっちゃいいな」。**理由: 発色と目のクオリティが高い**。

- **462**: Zimage（Danbooruチューンが来れば日本語+Danbooruタグが実用的になるはず）とNetaYumeLumina（Danbooruタグと日本語自然言語両対応でプロンプトテスト。服混じるが髪色・目色・リボン描き分け可。複雑形状でグチャる限界あり）。**理由 (Zimage): Danbooruチューン待ちで実用性期待。背景は日本語、メインはタグ運用想定**。

- **466**: Z-image（性能が低い、出てくる画像はSDXL以下、プロンプト追従するが細部グチャる、LoRAは動作するがノリ悪く実用圏外、オマ環のせいかも）。**理由: 性能・画質・LoRAの面倒さで流行らない**。

- **469**: Z-image が軽いと期待される。**理由: 要求スペックが低い**。

- **470**: Z-image（上記466の詳細補足: 画質の問題、細部溶け、LoRA作成がSDXLより面倒・うまくいかない、DiTパラメータ2.6Bで高性能ではない）。**理由: 同上（性能・LoRA問題で実用圏外）**。

- **472**: zimageの自作LoRAは表情変えても別人にならない（QIE2509の画像参照は表情変えると別人化）。**理由: LoRA作りやすい**。

- **474**: A1111は無事動いた、ComfyUIに手を出してみるか。

- **484**: ComfyUIのFor Loopノードを使ったPainterLongVideoのフローで30秒動画作成（酷い出来）。次はSAM3使ったDetailer研究。**理由: 目的（動画作成）のために使用**。

- **485**: Qwen-Image-Layered で ComfyUIは使えるか？（ワークフロー待ち）。

- **490**: Comfy Org にワークフローない（diffusers直叩き提案されたが無理）。

- **493**: OpenRouterのAPIに画像投げれるノードで「qwen/qwen-2.5-vl-7b-instruct:free」に投げて元絵詳細書かせる。**理由: free使用可能（デボジット必要）**。

- **499**: Comfy-Org にきてた（Qwen-Image-LayeredのWF）。

- **505**: Comfy-Org に Qwen-Image-Layered がきてた。

- **555**: Z-imageBase まだ？ Turbo出て1ヶ月経った。

- **557**: z-image の生成と編集モデルの統合はqwenのようにはならない（LoRA作成で分散）。

- **558-560,564,571,588,591**: Qwen-Image-Layered の ComfyUI CustomNode/WF（量子化GGUFでVRAM16GB余裕、CLIP/Qwen用VAE必要、Layered用VAEあり、DisTorch2MultiGPUで3080/12GB VRAM可、20ステップ/3レイヤーで5分）。**理由: VRAM低くても動く（量子化）、MultiGPU対応で高スペ不要**。

- **562**: zimage は統合版（base）でLoRA作成、そのLoRAはturbo/edit両方で使える？ baseも16G VRAMでいけると文句なし。**理由: LoRA汎用性・低VRAM期待**。

- **599**: ComfyUI をアプデしたら Load Video (Upload) の動画プレビュー表示されず（Settings > VHS > Previews > Advanced PreviewsをNeverにしたら直った）。

- **600**: Low VRAM mode (`python src/app.py --low_vram`) で10Gくらいで行ける。

- **611**: wikiで EasyImageEdit で ZIT をインストール（画像用）。**理由: 最近の流れで初心者向けインストール**。

- **612**: forge-neo を入れるのが一番簡単（python/venv と git がわかるなら）。**理由: 簡単インストール**。

- **617**: a1111 の i2i で adetailer person/face 二つ実行はVRAM32GBでも無理（1回目person、2回目faceに分ける）。

- **618**: 初心者なら reForge で（情報多く安定）、Forge-Classic は軽量高速だが情報少なく拡張機能動作しないので非推奨。EasyImageEdit/Forge-Neo/ComfyUI も知識次第。**理由 (reForge): 情報多く安定。Forge-Classic: 軽量高速だが情報・拡張不足で初心者非推奨。ComfyUI: 知識あるなら良い**。

- **622**: 今からAI再履修なら ComfyUI 一択（リアスしか使わないなら別）。**理由: 一択推奨（汎用性高？）**。

### 補足
- **ZIT/Z-image/z-image**: ログ全体で頻出（軽量・LoRA容易・日本語対応期待など理由多め）。ツールとして一貫して扱い抽出。
- **ComfyUI/Comfy-Org**: 最多登場。ワークフロー・ノード（PainterLongVideo, SAM3 Detailer, DisTorch2MultiGPUなど）中心。
- **その他ツール（Janku, OpenRouter API, forge-neo/reForge/Forge-Classic/EasyImageEdit）**: 明確に生成AIツール文脈で登場。
- モデル混在話題（例: Qwen-Image-LayeredのComfyUI使用）はツール部分のみ抽出。
- 理由なしの単発言及（例: 474のA1111）は理由省略。合計20件以上の話題を整理。