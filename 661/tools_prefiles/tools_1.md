**抽出されたツール関連話題**

- **ComfyUI (comfy)**: スレ内で最も言及が多いツール。複雑なワークフロー（特にControlNetの多用）で高度な制御が可能とされ、Regional-Controlnet + Attention Couple、Tile & Repair ControlNet、anima-tile-and-repair-controlnet-lllite、SAM3/SAM3.1との組み合わせが話題。初心者にはノードがスパゲッティ状で見づらい・とっつきにくいという声がある一方、「軽い・速い」「大規模ワークフローで威圧可能」「領域分け・修復・アップスケールが強い」と評価する声も。webUIからの移行組も複数存在し、ComfyUIユーザー層はレイヤー構造を意識した整理ができる傾向があると指摘。
  - 選ばれる理由: 最新環境対応・細かい制御（特に修復・タイル・リージョナル）・軽快さ・SAM3との親和性で「Anima+SAM3.1が最強」との結論も。初心者離れしやすい点も特徴。

- **webUI (A1111系)**: ComfyUIの対比として登場。初心者・処女勢が最初に触りやすいツールとして言及され、「ComfyUIより簡単」との声。「ここじゃComfyUIが一番多いが、ワイはwebUI」との使い分け例あり。

- **StabilityMatrix**: ComfyUIなどの起動管理ツールとして言及。Auto Launch設定の挙動（ブラウザ自動起動）に関するトラブルシュート話題。

- **Forge Neo**: Regional-Controlnetの代替・簡易化ツールとして推奨された。

**Qwenシリーズ（画像生成以外）**
- GLM-5.2 / GLM-5.1: エロ小説生成性能が高く、中国課金（サードパーティ含む）で利用されているLLMとして話題。NovelAIにも採用されており「エロ覇権」との声。

**モデル名・バージョン・新サービス等の事実確認（Web検索による参考情報）**
- **anima-tile-and-repair-controlnet-lllite**: ComfyUI向けControlNet。Animaモデルとの組み合わせで低画質修復・ディテール向上に用いられる。2025年時点でCivitai等で配布されており、Tile Repair用途の軽量版として人気。
- **SAM3 / SAM3.1**: MetaのSegment Anything Modelの最新版。ComfyUIワークフローで自動マスク生成に使われ、人物・局部検出などで活用。Animaとの併用で「最強」と評価されるケースあり。
- **StabilityMatrix**: ComfyUI/Forge/A1111などのローカルAI環境を一元管理するツール。Auto Launch機能でブラウザ自動起動が可能。
- **Forge Neo**: ComfyUI派生の高速UI。Regional ControlNet対応を簡略化する目的で言及されることが多い。

（モデルリスト記載のNovelAI/FLUX/Wan/Qwen-Image/anima/Z-Image/LTXなどは一切抽出せず、ツール・ControlNet・UI関連のみに絞っています）