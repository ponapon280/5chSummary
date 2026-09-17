# 🆕 新規トピック（前回からの差分）
### モデル: MiniMax H3（H3 / FastH3 / MMH3 / Hailuo H3）
- 動画生成の主力として速度・参照機能・編集性能・LoRA対応で高評価され、Krea2との組み合わせ例が多い

### モデル: Wan（Wan2.2 / Wan2.1など）
- i2vやループ動画で動きの自然さが評価され、オープンソース勢として注目

### モデル: その他のモデル
- NovelAI V5：リリース後の勢いが低下し「お通夜」状態
- Z-Image Turbo：ComfyUI移行や速度・LoRA相性で言及

### モデル: 全体の傾向と選ばれる主な理由（ログから抽出）
- ComfyUIとの親和性が高く運用が容易
- Turbo/Fast系モデルの速度と品質バランス
- LoRA反応の良さや参照機能の強さ
- 新しめモデルで触りやすく復帰しやすい実用性

### モデル: Web検索による参考情報
- Krea2：2026年6月頃12B DiTモデルをオープンウェイト公開、Raw/Turbo版あり
- MiniMax H3：2026年7月リリース、ネイティブ2K・音声同期・omuni-reference対応
- Wan（Wan2.2）：AlibabaのMoE動画モデル、720p TI2V対応でオープンソース
- NovelAI Diffusion V5：2026年8月リリース、大規模化と日本語・位置指定強化
- 検索結果は2026年9月時点の公開情報に基づく

---
# 元の本文
**レポート冒頭まとめ：テキストから推測される流行モデル**

このログ群（主にローカル環境・ComfyUIユーザー中心の議論）から、**Anima**がアニメ調静止画用途で最も言及が多く、現役の主力モデルとして位置づけられている。次に**Krea2**（リアル寄り静止画・LoRA相性・柔軟性で評価）、**MiniMax H3（H3 / FastH3 / MMH3）**（動画生成の速度・参照機能・品質で高評価）、**Wan（Wan2.2など）**（動画、特にi2vやループ生成で言及）が目立つ。NovelAI（NAI）V5はリリース直後に話題になったが、勢いが続かず使用者が減少傾向。Qwen-Image（編集用途）やZ-Image Turboも一部で実用的に語られている。全体の傾向として、「ComfyUIとの親和性」「Turbo/Fast系モデルの速度」「LoRAの扱いやすさ」「静止画→動画のワークフロー構築」が選択基準となっており、ローカル勢の間でAnima＋Krea2＋MiniMax H3の組み合わせが「復帰しやすい実用コース」として語られることが多い。[[1]](https://docs.comfy.org/tutorials/image/anima/anima)[[2]](https://civitai.com/models/2821932/minimax-h3)

### 1. Anima（アニマ / Anima Base / Turbo版など）
最も言及頻度が高く、ローカルアニメ静止画生成の有力候補として推奨されている。タグの影響力が強く、指示に対してストレートに決まった絵が出やすい点が評価され、Krea2との比較でも「タグの力が強い」「IP-Adapterとの相性が良い」「アーティストタグ混ぜ構文に対応」などの声がある。ComfyUI環境での運用Tips（turbo int8時のstrength調整、IP-Adapter Loader、連続生成）も複数出ており、静止画＋吹き出し合成やLoRA学習元としても使われている。Turbo版の方が安定・使いやすいという意見も見られる。base bf16モデルをメインに使うユーザーも一定数おり、FTモデルとの使い分けも話題に。[[1]](https://docs.comfy.org/tutorials/image/anima/anima)[[3]](https://gigazine.net/gsc_news/en/20260515-anima-image-generation-ai/)

### 2. Krea2（Krea-2 / Krea2 Turbo / Rawなど）
リアル寄り静止画やエロLoRAの効きが非常に良い点で高評価。「些細なニュアンスの差を調整して埋めていける」柔軟性が強みで、Animaが決まりすぎるのに対し微妙な表現が詰め込めるとの声がある。H3の参照画像係として優秀で、好みのリアル寄り女性画像を生成しやすい。文字・吹き出し表現力や座標指定の強みも指摘され、静止画ワークフローの主力の一つとして定着。エロチューン版やAnime版への期待も語られている。[[4]](https://huggingface.co/krea/Krea-2-Raw)[[5]](https://blog.bymar.co/posts/krea-2-open-weights-image-model/)

### 3. MiniMax H3（H3 / FastH3 / MMH3 / Hailuo H3）
動画生成で最も言及が多く、「最近の復帰コース」の動画担当として位置づけられる。生成速度の速さ（VAE高速化の恩恵）、参照機能（画像・動画）の強さ、編集性能の高さ、LoRA学習対応が進んでいる点が選ばれる理由。bf16 TE使用時の挙動やcontext loop機能、4〜8stepなどの実用ステップ数、肌質感や一貫性・追捧性で評価される。Krea2と組み合わせて静止画→動画ワークフローを構築する例が目立つ。[[2]](https://civitai.com/models/2821932/minimax-h3)[[6]](https://www.minimax.io/blog/minimax-h3)

### 4. Wan（Wan2.2 / Wan2.1など）
動画生成（特にi2v系やループセックス動画）でCivitaiショーケースなどを参考に選ばれることが多く、MiniMax H3と比較される中で「動きの自然さ」や「まだ現役」という評価がある。オープンソース勢として注目されており、品質面で「クリックしてしまう」ケースが多い。[[7]](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)

### 5. その他のモデル
- **NovelAI（NAI）V5**：リリース直後は騒がれたが、現在は使用者が減少し「お通夜」状態。位置指定機能への期待は残るが、勢いは続いていない。[[8]](https://journal.novelai.net/image-generation-novelai-diffusion-v5-is-here-c2df7c6b8d2d/)
- **Qwen-Image / Qwen edit（2511など）**：編集モデルとして「簡単で素直で丁寧」と扱いやすさが評価され、今でも現役で使われる声がある。
- **Z-Image Turbo**：ComfyUIデフォルトワークフローの移行やTurbo版の速度・LoRA相性で言及。
- その他：luna（Animaの次世代候補として期待）、Spectrum、YuE2（音楽）などは軽微な言及。

**全体の傾向と選ばれる主な理由（ログから抽出）**  
- ComfyUIとの親和性が高く、環境構築・運用が簡単。
- Turbo/Fast系モデルの速度と品質のバランス。
- LoRAの反応の良さや参照機能の強さ。
- 静止画（Anima/Krea2）と動画（MiniMax H3/Wan）の役割分担が明確で、実用的なローカルワークフローを組める点。
- 新しめのモデルの中で「触りやすい」「復帰しやすい」という実用性重視の声が多い。

## Web検索による参考情報
- **Anima**：CircleStone LabsとComfy Orgの共同開発による2Bパラメータのアニメ・イラスト特化テキスト-to-画像モデル（2026年5月頃公式版リリース）。ComfyUIネイティブ対応、Qwen-3 0.6Bテキストエンコーダー使用、base/turbo/aesthetic版あり。HFリポジトリでモデルファイル公開。[[1]](https://docs.comfy.org/tutorials/image/anima/anima)[[3]](https://gigazine.net/gsc_news/en/20260515-anima-image-generation-ai/)
- **Krea2**：Krea社が2026年6月頃オープンウェイト公開（Raw：ファインチューニング向け、Turbo：8ステップ蒸留版）。12Bパラメータ級DiTモデルでComfyUI対応、リアル・イラスト両対応。[[4]](https://huggingface.co/krea/Krea-2-Raw)[[9]](https://gigazine.net/gsc_news/en/20260624-krea-2-raw-turbo/)
- **MiniMax H3**：MiniMaxの2026年7月頃リリースのマルチモーダル動画生成モデル。ネイティブ2K・最大15秒・音声同期生成、omuni-reference対応。オープンウェイト版あり、ComfyUIで利用可能。[[2]](https://civitai.com/models/2821932/minimax-h3)[[6]](https://www.minimax.io/blog/minimax-h3)
- **Wan（Wan2.2）**：Alibaba Tongyi Labの動画生成モデル群。Wan2.2はMoEアーキテクチャ採用、720p TI2V対応、2025〜2026年にかけて複数バージョン公開。オープンソース。[[7]](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
- **NovelAI Diffusion V5**：2026年8月リリース。V4.5比で2倍超の規模、カスタム32ch VAE、日本語対応強化、位置指定・多キャラ対応向上。[[8]](https://journal.novelai.net/image-generation-novelai-diffusion-v5-is-here-c2df7c6b8d2d/)

（検索結果は2026年9月時点の公開情報に基づく。実際の利用状況はログのローカルユーザー議論と一致する傾向が見られる。）
