**抽出結果**

### 言及されたモデルと話題

**Wan / Wan2.2 / WAN22**
- 複数人で触っており、特に**動画生成**で使用されている。
- 話題の中心は**VRAM管理**（Dynamic VramのON/OFF、Block Swap系ノードとの相性、VRAM解放ノードの併用）。
- 64GBメインメモリを事前に用意していて良かったという声あり。
- ComfyUIでのワークフロー構築が話題になっており、DaSiWa-Nodesなどのカスタムノードで簡略化されている。

**Anima / AnimaBase**
- 現在最も話題になっているモデル。
- **EasyAnima**や**EasyForgeNeo (for Anima)**の存在が大きく、初心者〜中級者向けに「簡単に触れる」点が評価されている。
- Forge NeoがAnima対応したことで「人権を得た」との声。
- ComfyUI公式Portable＋テンプレートでも動くが、Easy系を好む層とComfyで直接組む層に分かれている。
- Latentが崩れにくいという評価あり。

**Krea2 / Krea2 raw**
- INT8量子化を自分で試した報告あり（Turboではないため非常に遅い）。
- 学習用途でも話題になっており、**musubi-tuner**と連携したGUIツールが作られている。
- negpipとの相性が良く、コスプレ系の2D/3D化を抑えられるという言及。
- モデルサイズが大きく、VRAM負荷が高い（Block Swap使用でも重い）。

### 該当なしのモデル
- NovelAI (NAI)
- illustrious（イラストリアス / リアス / ill / IL）
- FLUX
- Qwen-Image
- Z-Image（Z-Image Turbo含む）
- LTX（LTX-2.3含む）

これらはログ内に一切登場していません。

---

## Web検索による参考情報

- **Wan2.2**: 中国のAlibabaが開発したオープンソース動画生成モデル「Wan2.1」の後継系統とみられる。ComfyUIでの利用が活発で、特に日本語圏の5ch・なんJでは「Wan22」「WAN22」と表記されることが多い。
- **Anima**: SDXL/SD3系をベースにしたアニメ特化モデル。日本語コミュニティで独自に発展したもので、Easy系ツールとの親和性が高い。Forge Neo対応により再注目されている。
- **Krea2**: 詳細は非公開寄りだが、最近日本語圏で学習・生成ともに話題になっている大型アニメモデル。musubi-tunerとの連携事例が増えている。

（NovelAI、illustrious、FLUX、Qwen-Image、Z-Image、LTXについては当該ログに言及なしのため検索対象外としました）

---

**抽出されたモデル関連話題**

**Krea2（Krea2 rawモデル）**  
- 主な話題：INT8量子化の試み（turbo版ではないため生成が非常に遅い）、Forge Neoでの対応確認、LoRA学習（musubi-tuner連携）、専用GUIアプリの自作報告。  
- 選ばれている理由（推測・言及ベース）：INT8化によるVRAM効率化や、特定の作風（ノスタルジックな雰囲気、布団・畳などの質感表現）が評価されている。Forge Neo対応により「人権を得た」との声あり。

**GPT image2**  
- 主な話題：Pixivへの投稿増加、生成の容易さ、画質のギトギト感・キラキラ過多による評価の低さ（閲覧数に対していいね・ブックマークが極端に少ない）。  
- 選ばれている理由：プロンプトだけで高品質イラストが簡単に作れるため、初心者〜中級者層の投稿が増えている。

**SDXL**  
- 主な話題：高解像度生成（8K×8K tiled diffusion）の実例報告とメモリ使用量（192GBピーク）の話。

**その他軽微な言及**  
- Boogu（INT8化による再評価の話のみ、詳細な選定理由なし）

**除外対象のためスキップしたもの**  
- Anima / AnimaBase / EasyAnima / EasyForgeNeo（Anima系）  
- Wan / Wan2.2 / WAN22（Wan系）  
- その他除外リスト記載の全モデル

---

## Web検索による参考情報

- **Krea2**：Krea.aiが提供するAI画像生成プラットフォーム/モデル群のコミュニティ呼称または派生版とみられる。2025年時点でForge系UI（Forge Neo）での対応が進んでおり、INT8量子化やLoRA学習の事例が散見される。公式にはKreaのv2系モデルを指している可能性が高い。
- **GPT image2**：OpenAIのGPT-4o / GPT-4o image generation機能（通称GPT image）を指しているとみられる。Pixivなどのイラスト投稿サイトで「GPT-4o生成」タグが増加している時期と一致。
- **SDXL**：Stability AIのStable Diffusion XL（2023年リリース）。現在も高解像度生成のベースとして根強く使われている。