**抽出されたモデル関連話題**

### Anima（AnimaEdit / Animarge / Anima Turbo LoRA）
- **言及回数**: 非常に多い（465, 471, 472, 501, 518, 520, 523, 531, 537, 545, 550, 562, 566, 568, 569, 573, 576, 577, 578, 587, 589, 590, 601, 605, 608, 610, 616, 618, 623, 638など）
- **選ばれている理由**:
  - キャラLoRA学習時の素材生成で顔・画風の変化が少なく、**AnimaEdit**が便利（465）
  - 階層LoRA適用（LoRA-Block filter系）で学習・生成ともに扱いやすい（471, 537）
  - プロンプト追従性が高く、画像を抽象化せずそのまま投入しても融通が利く（520）
  - Turbo LoRAとの組み合わせで高速生成＋画風安定（501, 545, 589, 590）
  - LECO / iLECO実装が進んでおり、絵柄調整・特定タグ弱体化に使える（573, 578, 638）
  - Illustriousよりパラメータが少ないのに性能が高いという声（531）

### Illustrious（リアス / AnyIllustrious / IL）
- **言及回数**: 多い（508, 520, 524, 531, 540, 550, 574, 576, 580, 618, 634）
- **選ばれている理由**:
  - LoRA学習時の**原作画風再現性が高い**（特にAnyIllustrious-XL）（508, 524）
  - Animaと比較して旧世代モデルだが、v-predの方が安定するという評価（540, 576）
  - デフォルメ系やfurryには不向きという指摘あり（524）

### NovelAI（NAI / NAI3）
- **言及回数**: 中程度（624, 626, 627, 629, 630, 631, 634, 637）
- **選ばれている理由**:
  - ローカル勢でも「まだローカルが完全に追い付けていない」との認識（624, 630）
  - **inpaint性能**が特に強い（634）
  - 参入ハードルが低く、品質面で一定の評価を維持している（631）

### その他（該当なし）
- FLUX、Wan、Qwen-Image、Z-Image、LTXについてはログ内に一切言及なし。

---

## Web検索による参考情報

- **Anima**: NvidiaのCosmosシリーズをベースにしたイラスト特化モデル（AnimaはCosmos2.0系）。作者が独自にファインチューニングしたモデルで、2025年現在も活発にアップデート・ツール開発が行われている。
- **Illustrious（AnyIllustrious）**: SDXL系アニメ特化モデル。LoRA学習時の画風再現性で人気があり、特に「AnyIllustrious-XL」はLoRA作成向けに使われることが多い。
- **NovelAI（NAI）**: NAI Diffusion（最新はNAI3系統）。クラウドサービスとして高品質なアニメ画像生成で定評があり、特にinpaintの性能がローカル勢からも評価されている。

---

**抽出された話題（除外モデル以外）**

- **Pony（Pony Diffusion）**  
  デフォルメ系・furry特化の文脈で「ponyはウルトラ強いけど今更感凄い」と言及。AnyIllustrious-XLでLoRA学習した後に、furry寄りの出力が欲しい場合の代替候補として名前が上がっている。画風維持しつつデフォルメ耐性が高いモデルを求めている投稿者が、ponyを候補に挙げている。

- **NVIDIA Cosmosシリーズ（Cosmos3 / Cosmos-Predict2-2B / Cosmos2.0）**  
  ログ後半で複数回話題に。  
  - 「Nvidia releases Cosmos3-Super-Image2Video . 64B」「Cosmos3-Super-Text2Image model . 64 billion parameters」  
  - Anima開発者視点で「Cosmos3が出たってことはAnima v2が更に神になる」との期待値が書かれている。  
  - 「Cosmos系DiTがtoken間の全体関係を強く見る構造」「SDXLより複数トークンに絡み合ってるから部分調整が難しい」という技術的特徴の指摘あり。  
  - 2Bサイズの小型モデルである点と、学習コストの低さがポジティブに評価されている。

- **Gemma系ローカルLLM（gemma-4-e4b-it-2-heretic-i1 など）**  
  ローカルLLM利用者の投稿で具体的なモデル名が挙げられている。「身体の破爛率が高すぎてうまくいかん…」という利用報告あり。Claudeに作ってもらったsysプロンプトと併用している例。

- **アップスケーラ系（ScuNET, RealESRGAN_x4plus_anime_6B, 2x_StarSample_V2.0_HQ）**  
  Forge Neo移行後の挙動変化や、好みのアップスケーラを求めての議論。モデルというよりツール寄りだが、生成パイプラインの一部として話題。

**除外対象のためスキップした主な言及**  
NovelAI/NAI、illustrious/リアス/IL/AnyIllustrious、FLUX、Wan、Qwen-Image、anima、Z-Image、LTX、Animarge、Anytest（anima関連）などはすべて除外。

## Web検索による参考情報
- **Pony Diffusion V6**：SDXLをベースにした人気のファインチューニング済みモデル。furry・デフォルメ表現に強く、Civitaiで非常に多くのLoRAが公開されている。2024年時点で既に成熟したモデル。
- **NVIDIA Cosmos**：2025年頃にNVIDIAが公開した動画・画像生成向けDiT系モデル群。Cosmos-Predict2-2B（2Bパラメータ）や64BクラスのSuper版が存在。完全にオープンなライセンスではなく、FTモデル制作者にある程度の権利を認める形。Animaのようなイラスト特化FTのベースとして注目されている。
- **Gemma-4系（hereticカスタム）**：GoogleのGemmaをベースにした非公式ファインチューニングモデル群。検閲を緩めた「uncensored」系がローカルLLM勢に使われている。