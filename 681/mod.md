# 🆕 新規トピック（前回からの差分）
### レポート冒頭まとめ：流行しているモデル
- 生成AIコミュニティでMiniMax H3が圧倒的主流となり、他のモデルは比較対象として言及される
- H3の台頭によりSeedanceからの移行が進んでいる

### MiniMax H3（H3 / Minimax H3 / Hailuo 3.0相当）
- 言及数が最多でほぼ全てのスレッドで中心的に議論されている
- 複数参照画像による局部・構図制御精度が高くR2Vとの相性も良好
- 日本語プロンプト・テキスト表示で他モデルを上回る
- 激しい動作の一貫性・再現性が高くリドロー不要
- グロ・エロ両対応で軽量、Motion Contextによる画風継続性が高い
- クラウド・ローカル両対応で多用途

### Wan（Wan2.2）
- Motion LoRAの出自や比較対象として複数ログで言及
- 単純反復動作（特にセックス運動）に強く生成速度が速い
- 画質・自然さ・多様な動きでH3に劣り旧世代扱い
- 二次エロ用途で画風制御・Danbooruタグ対応が強くLoRA相性良好
- 参照画像・体位LoRA作成で実用
- テキストエンコーダーが弱く自然言語が通じにくい

### その他のモデル（言及少なめまたは比較対象）
- LTXはH3より重く液体表現の癖で言及
- NovelAI / illustrious / Z-Imageはほぼ言及なし
- LLM系（Gemini、Gemma4、Grok、Claude、Deepseek）はH3用エロプロンプト生成で補助的に使用

### Web検索による参考情報
- MiniMax H3は2026年7-8月リリースのオープンウェイト多モーダル動画生成モデルで、omni-referenceやモーション制御に強い
- Wan2.2はAlibabaのMoE採用オープンソースモデルで720P/24fps対応、消費者向けGPUで動作
- LTXは高解像度・長尺・音声同期に強くプロダクション向けモデル群

---
# 元の本文
**レポート冒頭まとめ：流行しているモデル**  
提供された複数のログ抽出結果から、生成AI（主に画像・動画生成、特にエロティックなモーション制御用途）のコミュニティで圧倒的に話題の中心であり、**流行・主流となっているモデルはMiniMax H3（H3 / Minimax H3 / MMH3）**である。ほぼすべてのスレッドでH3がメインに議論され、他のモデルはH3との比較材料として言及される形が一般的。H3の優位性により、Seedanceなどの以前の人気モデルからの移行も報告されている。[[1]](https://fal.ai/minimax-h3)[[2]](https://www.minimax.io/blog/minimax-h3)

Wan2.2やAnimaは一部で速度や特定用途（反復モーションや2Dスタイル）で評価されるが、全体的な品質・実用性ではH3に劣るとの見方が多い。NovelAI、illustrious、FLUX、Qwen-Image、Z-Image、LTXなどは言及が少なく、陳腐化またはニッチ用途に留まっている。

---

### 1. MiniMax H3（H3 / Minimax H3 / Hailuo 3.0相当）
**言及の多さ**: ログ全体で最も多く、ほぼ一色。  
**選ばれている主な理由**（ログから抽出）:
- **参照画像制御性能の高さ**: 複数枚の参照画像（特に局部・構図指定）で精度が向上。「下手にLoRAを使うより参照画像を増やす方が良い」という評価多数。R2V（Reference to Video）との相性も良好。
- **日本語対応の強さ**: 日本語プロンプト・テキスト表示でIdeogram4.0やKrea2を上回る。静止画モデルとの差別化ポイント。
- **動きの一貫性・再現性**: 激しい動作（腰振り・挿入・ケンカシーンなど）で安定。「リドローほぼなし」「モデルられない」。Wan2.2由来のMotion LoRA移植も可能。
- **その他の実用性**: グロ・エロ両対応、軽量寄り（LTX2より軽い）、プロンプトの質で結果が変わるが本番エロ以外も多用途。Motion Context機能で画風継続性が高い。クラウド/ローカル両対応。

H3の台頭により、Seedance離れが進んでいるという空気感が強い。

### 2. Wan（Wan2.2）
**言及**: 複数ログでMotion LoRAの出自や比較対象として登場。  
**選ばれている/評価される理由**:
- 単純な反復動作（特にセックスなどのピストン運動）に強い。「wan+loraの方がエロは強そう」。
- 生成速度が速い点が強み（短時間でそれなりのエロ動画）。

**否定的評価**: 画質・自然さ・多様な動きでH3に劣る。「もう全部消した」「Wanには絶対作れないものもある」「2.5D以外だと違和感」。旧世代扱いされ、積極利用は少ない。

### 3. anima（Anima / botanAnima_base10V31など）
**言及**: 速度・実用性・参照画像作成文脈で複数回。  
**選ばれている理由**:
- 軽量・高速（SDXL比でサイズ約30%減、ComfyUI更新で大幅高速化例あり）。
- 二次エロ用途で画風制御が強く、Danbooruタグ対応が良い（small breastsなどの指示通りやすい）。LoRA相性も良好。
- 参照画像作成や体位LoRA作成で実用。

**弱点**: テキストエンコーダーが弱く、自然言語が通じにくい（専用構文「部族語」必要）。H3登場前は外人品質で優位だったが、日本語対応でH3に巻き返された。

### その他のモデル（言及少なめまたは比較対象）
- **LTX（LTX2 / LTX-2.3）**: 軽さ比較や液体表現の癖で言及。H3より重いという声。
- **FLUX（fl2v / fl2va）**: 参照動画使用時に極端に重くなるため敬遠されやすい。
- **Qwen-Image**: sage-attnとの相性悪（無限ループ現象）やedit系で強い点のみ。
- **NovelAI / illustrious / Z-Image**: ほとんど言及なし（NovelAIは歴史的文脈で稀に登場）。
- **LLM系（Gemini、Gemma4、Grok、Claude、Deepseek）**: H3用プロンプト生成（特にエロ寄り）で補助的に使用。Gemma4は「欲望に素直」なプロンプト生成で評価。

---

## Web検索による参考情報
- **MiniMax H3**: 2026年7-8月頃にリリースされたMiniMaxのオープンウェイト多モーダル動画生成モデル。テキスト・画像・動画・音声を統一コンテキストで扱い、ネイティブ2K解像度・最大15秒・ステレオ音声同期生成を特徴とする。Hailuo 3.0 / Hailuo H3とも呼ばれ、参照条件付け（omni-reference）やモーション制御に強い。Hugging Faceなどで利用可能。[[1]](https://fal.ai/minimax-h3)[[2]](https://www.minimax.io/blog/minimax-h3)[[3]](https://openart.ai/ai-model/minimax-h3/)
- **Wan2.2**: Alibaba Tongyi Lab（Wan-Video）によるオープンソース動画生成モデル（MoEアーキテクチャ採用）。720P/24fpsのtext-to-video / image-to-video対応で、消費者向けGPU（例: 4090）でも動作。 cinematic controlや複雑モーションに強み。[[4]](https://github.com/Wan-Video/Wan2.2)[[5]](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- **Anima**: Circlestone Labs製のアニメ特化テキスト-to-画像モデル（2Bパラメータ版DiTベース）。高速生成とキャラクター一貫性・プロンプト追従に優れ、ComfyUIワークフローで人気。アニメ/手描きスタイル向け。[[6]](https://www.reddit.com/r/StableDiffusion/comments/1qthxyi/new_anime_model_anima_is_amazing_cant_wait_for/)[[7]](https://www.youtube.com/watch?v=xv7OWNQHjkw)
- **LTX（LTX-2 / LTX-2.3）**: Lightricksのオープンソース動画生成モデル群。LTX-2は高解像度・長尺・音声同期に強く、プロダクション用途向け。[[8]](https://ltx.io/model/ltx-2)[[9]](https://en.wikipedia.org/wiki/LTX_(text-to-video_model))

（その他FLUX、Qwen-Imageなどは広く知られたモデルだが、本ログ内での言及は限定的のため詳細検索は省略。）
