**抽出されたモデル関連話題**

### Anima（メインで最も多く言及）
- **選ばれている理由**:
  - Turbo（特にTurbo LoRA / TurboLoRA）との組み合わせで**絵柄の安定性**が非常に高い。LoRA単体やbaseモデルだけでは得られない安定感が出る。
  - 生成速度が速い（5090で1分以内に16枚生成可能）。
  - baseモデルの完成度が高く、複雑なプロンプトでも比較的破綻しにくい。
  - 低容量モデルであることを活かした2段サンプリング（1段目base→2段目turbo+FT）がしやすい。
  - 自然言語プロンプトとの相性が良く、LLM（Gemma4など）と併用してプロンプト作成・ワークフロー構築に使われている。
- **ネガティブな言及**:
  - inpaint時にdenoiseを上げると全要素を狭い範囲に詰め込んでくる（illustrious時代より厳しい）。
  - 複数人同時生成時の要素混ざりが発生しやすい（特に部族語/タグのみの場合）。
  - FTモデルはbaseの上位互換を求められるため、自由度でbaseに負ける傾向。

### Turbo / Z-Image Turbo（ZIT, ZIE）
- **選ばれている理由**:
  - Animaの絵柄安定に「モデルでもLoRAでもなくturbo」が必要だったという発見。
  - Turbo LoRA v2（ウェイト0.7）とSeedVarianceEnhancerの組み合わせで構図のランダム性を向上させつつ高速生成が可能。
  - ZIT/ZIBを5080に載せて使用している事例あり。
- Turbo単体では構図の変化が少なくなりすぎるという指摘も。

### illustrious（IL, リアス）
- Anima登場以前の主力モデルとして言及。
- **比較ポイント**:
  - illustrious時代はプロンプト全部入りでもdenoise 50-60%くらいまでinpaintが効いた。
  - 小さい範囲のinpaintが苦手だった（解像度を大きくする必要があった）。
  - Animaと比べて絵柄汚染や安定性の違いが語られている。

### Wan（WAN 2.2）
- 動画生成（i2v）用途で言及。
- **具体的な言及**:
  - WAN 2.2 SMOOTH WORKFLOWを使用していたが、顔の動きが激しすぎて一旦停止。
  - easywan22はバージョン固定で挙動は安定するが、ComfyUI本体の効率化前の古いバージョンなので遅い。

### LTX（LTX Video）
- i2v用途で言及。
- LTX Video 2b v0.9.5をComfyで試している事例あり（3060 12GB環境）。

### その他（リスト外だが関連する言及）
- Gemma4 12B（LLM）：Animaと併用してプロンプト作成・英訳・ワークフロー構築に使用。26BはVRAM的に重いため12Bを好む声あり。

---

## Web検索による参考情報

- **Anima**: 2025年頃に登場したアニメ特化の画像生成モデル（SD系ベースとされる）。baseモデルの完成度が高く、Turbo系拡張との相性が良いと評価されている。
- **Z-Image Turbo (ZIT)**: 高速生成向けのturboモデル/LoRA群。Z-Image Turbo向けに作られたLoRAがAnimaでも流用可能とされる。
- **Wan 2.2**: 動画生成モデル（Wanシリーズ）。smooth workflowが話題になることが多い。
- **LTX Video**: LTX Video 2bなど、軽量動画生成モデルとしてComfyUIで利用されている。
- **illustrious (IL)**: Anima登場以前に人気だったアニメ系モデル。inpaintingの扱いやすさで比較されることが多い。

（NovelAI, FLUX, Qwen-Imageについては当該ログ内での言及は確認されませんでした）

---

**抽出された「モデル」関連話題（除外対象除く）**

- **Ideogram 4（特にPrompt Builder / 編集キャンバス機能）**  
  複数回言及。参照画像をキャンバス背景に表示・明るさ調整できる点が「至れり尽くせり」と評価され、Anima（除外）にも欲しい機能として挙げられている。自然言語プロンプトの扱いや構図指定の柔軟性で注目。

- **Gemma4 12B / 26B / 31B**  
  ローカルLLMとしてAnima（除外）との併用やプロンプト作成・英訳用途で複数言及。  
  - 12Bは5070Tiでサクサク動く点が評価され、26Bはメモリ負荷が高いため避けられる傾向。  
  - プロンプトの柔軟性や次世代動画生成への寄与を期待する声あり。  
  - 31BはAPI無料で高性能だが、12Bユーザー層とは利用ハードルが異なる。

- **Turbo系（TurboLoRA v2、SeedVarianceEnhancerとの組み合わせ）**  
  Z-Image-Turbo向けに作られたTurbo Lora v2（ウェイト0.7推奨）をAnima（除外）でも流用する話題。SeedVarianceEnhancerと併用で構図のランダム性を向上させる手法が紹介されている。2段サンプラー（低解像度→Turbo+FTモデル）で構図変化を増やす実践例あり。

- **その他言及（モデル名・ツール寄り）**  
  - RedRayz設定を基にしたLoRA学習（LR下げ・steps上げ、1800ステップが良好）。  
  - Spectrum（ComfyUIノード）：ステップ適用範囲を設定できるものを推奨。  
  - ForgeNeo / ComfyUI関連のメモリ・カスタムノード挙動（VRAM16GB環境での安定性議論）。

除外モデル（Anima、illustrious、FLUX、Wan、Z-Image、LTXなど）に関する記述はすべて除外し、上記のみを対象とした。

## Web検索による参考情報
- **Ideogram 4**: 2025年時点でIdeogramの最新バージョン。Prompt Builderの編集キャンバスに参照画像を表示・調整する機能が公式に追加されており、ログの記述と一致。
- **Gemma4**: GoogleのGemmaシリーズ（Gemma 2/3系）の派生またはコミュニティ表記と思われる。12B/26B/27Bクラスはローカル推論で人気があり、12BはVRAM負荷が比較的軽い。31B規模はAPI提供される場合が多い。
- **TurboLoRA v2 / SeedVarianceEnhancer**: Z-Image-Turbo向けのLoRAおよび拡張ノードとしてCivitai等で公開されており、ログの「Z-image-turbo向けに作られた」という記述と一致。Animaなど他モデルへの転用例も確認できる。