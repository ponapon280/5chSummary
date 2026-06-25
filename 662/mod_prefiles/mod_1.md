**抽出結果**

### anima / Anima-turbo
- **話題の出現**: 32, 62, 63, 67, 80, 85, 126, 134, 187
- **主な内容**:
  - Anima-turboの近日公開情報（32, 63）
  - LoRAマージしたモデル vs 外付けLoRAのメリットについての議論（62）
  - おっぱいサイズが大きくなりやすい傾向（smallでも大きめに出る）（67）
  - minigirl・size difference・stomach bulgeなどの表現のしやすさ（126, 134）
  - αをRankの数百倍にする設定でも破綻しにくいという評価（187）
- **選ばれている理由として抽出された点**:
  - minigirlやsize differenceのスケール感がillustriousやponyより扱いやすい
  - 自然な表現や強度指定の緩さ

### illustrious（イラストリアス / リアス / ill / IL）
- **話題の出現**: 126, 134
- **主な内容**:
  - minigirl・size difference表現におけるモデル比較（illustrious＞anima＞pony）
- **選ばれている理由として抽出された点**:
  - minigirl表現の強さ・扱いやすさで現在最も評価が高い

### Wan / easywan
- **話題の出現**: 22, 62, 228
- **主な内容**:
  - easywanでの舌を絡めるキス・POVキス表現の難しさ（22）
  - wan light2v向けLoRAの多さ（228）
- **選ばれている理由として抽出された点**: 特になし（むしろ苦手分野として言及）

### NovelAI（NAI）
- **話題の出現**: 68
- **主な内容**:
  - 23日のメンテナンスが生成高速化かどうかの推測

### その他関連（リスト外だが言及あり）
- **Animerge**: 75, 84, 97, 128, 148, 151, 159（マージツールとしての言及多数、ADDifT/DPOモードの新機能）
- **pixeldit**: 78（特定のcheckpointとして言及）

---

## Web検索による参考情報

- **Anima-turbo**: 2025年現在、Animaシリーズの新バージョンとして「Anima-turbo」が開発中・近日公開予定と複数ソースで言及されているアニメ特化モデル。base1.0公開時点から「Coming Soon」表記があった。
- **illustrious（IL）**: アニメ・美少女イラスト特化のDiT系モデル。minigirlや変形表現の扱いやすさで評価が高い。
- **Wan / easywan**: 「Wan」は動画生成関連のモデル（特にlight2v系）の呼称として使われており、LoRAも多数公開されている。
- **pixeldit**: DiTベースの画像生成モデル（1024px対応のbf16版など）が存在し、一部ユーザーがcheckpointとして利用。

---

**抽出された「モデル」関連話題（除外対象除く）**

- **Animerge**  
  複数回にわたり更新報告と機能追加の話題あり。主な内容はGUI改善、翻訳UI調整、マージタブの読み込み方式変更、ADDifTへのDPOモード追加（良い画像・悪い画像のペアで好みに寄せる簡易版）。  
  **選ばれている理由として抽出された点**：  
  - LECOと比べて関連タグへの影響が少なく、バイアス連想を遮断しやすい（プロのガードレール調整に近い）。  
  - DPOモードにより、特定効果（例: bukkake）の強度をスライダー的に調整可能で、既存モデルに影響を与えにくい。  
  - LoRAマージ系モデル全般のメリットとして「1モデルで済む」「LoRA処理を都度行わないため若干高速」点が言及されたが、デメリット（自由度低下）も指摘。

- **pixeldit_1300m_1024px_bf16.safetensors / gemma_2_2b_it_elm_bf16.safetensors**  
  NEO（推定ComfyUI系ワークフロー）でCheckpoint + VAE/Text Encoderとして使用する組み合わせとして言及。ModuleNotFoundError発生時のトラブルシュート話題。

- **DiT系モデル全般（SDXL以降の次世代モデル）**  
  LoRA学習時のα/Rank設定について「SDXL時代はαをRankの半分以下が良いとされたが、DiTではαをRankより大きくした方が良い」という意見がKohya氏のX投稿を基に議論された。

- **Stable Diffusion（総称・ソフトウェア含む）**  
  ローカル生成の主流かどうかの質問に対し、「モデルとしてのStable Diffusionは3.5で死亡した」「ソフトウェアとしてはComfyUIへの移行が進んでいる（Forge neoも健闘）」という指摘あり。自然言語プロンプトやdanbooruタグ変換の話題も関連。

- **ChatGPT / Claude（LLM）**  
  課金検討時の選択肢として「ChatGPT Plus（3000円）が利用制限で優位」との結論。開発以外での用途を想定した実用性比較。

**## Web検索による参考情報**  
- Animerge：5ch/なんJスレッド内で独自に開発・公開されているマージツール＋ADDifT実装のGUIアプリ。DPOモードは2025年時点で最新機能として言及されており、論文ベースの嗜好最適化（DPO）を簡易化したもの。  
- pixeldit：DiTアーキテクチャをベースにしたPixelArt特化モデル群。1024px bf16版は特定のワークフローでVAE/Text Encoder（gemma系）と組み合わせる例が見られる。  
- DiT（Diffusion Transformer）：SDXL以降の主流アーキテクチャ。α/Rankの最適値が従来のSD系と異なる可能性が指摘されており、Kohya氏らの実験的知見が参考にされている。

（除外モデル：NovelAI、illustrious、FLUX、Wan、Qwen-Image、anima、Z-Image、LTXは一切抽出対象外とした）