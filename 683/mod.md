# 🆕 新規トピック（前回からの差分）
### 選ばれている主な理由
- Danbooruタグ理解度が高くLoRA作成が圧倒的に容易
- ベースモデルとしての安定性が高くNSFW描写のクオリティが向上
- Turboはマスピ寄りになりやすいためベース＋LoRA推奨、専用custom nodeが必要で生成速度が遅め
- 参照画像保持能力が非常に高くref2v/i2vでの追従性・複数画像参照に優れる
- 動きの自然さと実写寄りモーションが強く、音声付き動画生成が可能
- プロンプト理解力・追従性が高く日本語対応も良好、ComfyUIワークフローがシンプルで高速化しやすい
- Context Loopなど拡張手法との相性が良くエロ動画特化の工夫が進んでいる
- 注意点として背景過剰保持によるカメラワーク悪化やネガティブプロンプトの特殊性が指摘される

### MiniMax H3（minimax_h3 / H3、Turbo版含む）
- ログの大部分を占める最主要トピックで、特に動画生成で熱狂的な支持を集めている

### その他のモデル
- Z-Image（Turbo/Base）：Turboの方が直接出力品質が高く公式も優位とされるが、Baseは自由度・追従性で優位との意見も
- LTX（LTX-2.3/LTX2.5）：日本語プロンプト追従性が弱くH3に劣るとされ存在感が薄れている

### Web検索による参考情報
- MiniMax H3：MiniMax製のオープンウェイトマルチモーダル動画生成モデル（2026年夏頃）。T2V/I2V/ref2V/編集に対応し最大2K・15秒程度の音声付きクリップを生成
- Krea-2-Turbo：Krea AI製のテキスト-to-画像モデル（2026年6月頃）。RAWとTurboの2種がありTurboは高速イテレーション向きでLoRA対応
- 情報は2026年8月時点の検索結果に基づく（モデルは急速に進化中）

---
# 元の本文
**流行しているモデルのまとめ（レポート冒頭）**  
ログ全体から、**MiniMax H3（minimax_h3 / H3）** が動画生成（特にi2v/ref2v/R2V、動きの自然さ・参照画像保持・音声付き出力）で圧倒的に話題の中心となっており、**Anima（Anima-2.9B / Anima Base + Turbo LoRA）** が画像生成・LoRA作成・二次イラスト/NSFW用途で最も支持されている。H3はリリース直後から「お祭り状態」と評され、AnimaはLoRAの作りやすさやタグ理解度で「現状唯一無二」と評価される。Krea2-turboは画像生成の有力候補として名前が上がり、Qwen-Image系は編集用途でオンリーワン級の評価。Z-ImageやLTXは品質差や日本語性能の弱さで比較対象として言及される程度で、NovelAI / FLUX / Wan / illustriousは言及が極めて少ないかゼロ。全体として、**ローカル環境での実用性（ComfyUI相性・速度・自由度）** と **特定用途（動画の動き/参照保持、アニメLoRAの制御）** が選定の鍵となっている。[[1]](https://www.minimax.io/)[[2]](https://www.youtube.com/watch?v=d_wEd-fZcdg)

### Anima（Anima-2.9B / Anima Base + Turbo LoRA）  
最も言及が多く、LoRA作成・二次イラスト/NSFW生成で強く支持される。  
**選ばれている主な理由**  
- Danbooruタグ（絵師タグ含む）の理解度が高く、左右理解も強いためLoRA作成が「圧倒的」にしやすい（「現状唯一無二」）。  
- ベースモデルとしての安定性が高く、ユーザー改変なしでも十分高品質。NSFW（特に詳細描写）のクオリティが向上したとの声多数。  
- Anima-2.9B（2B→2.9Bパラメータ、層拡張・170万枚追加学習のFTモデル）は素の出力で高クオリティが出やすく、ワークフローをシンプルにできる。H3との相性も良い（ref2vやキャラシート量産）。  
注意点として、Turboはマスピ寄りになりやすいためベース＋LoRA組み合わせを推す声が多い。専用custom nodeが必要で生成速度がやや遅くなる点も指摘されている。

### MiniMax H3（minimax_h3 / H3、Turbo版含む）  
ログの大部分を占める最主要トピック。特に動画生成で熱狂的な支持。  
**選ばれている主な理由**  
- 参照画像の保持能力が異常に高く（「gptimageより上」）、ref2v/i2vでの追従性・複数画像参照が優れている。  
- 動きの自然さ・実写寄りのモーション（胸の揺れなど）が強く、音声（セリフ・効果音）付き動画生成が可能でクオリティが高い。  
- プロンプト理解力・追従性が優れ、日本語対応も良い。ComfyUIワークフローが比較的シンプルで、高速化（Turbo 4step/8step + lightx2v LoRA、Spectrum併用）で実用速度が出る。ローカル無規制クラスでSora2並み〜Seedance2.0相当との評価。  
- Context Loopなどの拡張手法との相性も良く、エロ動画特化の工夫が進んでいる。  
注意点として、背景過剰保持によるカメラワーク悪化や、ネガティブプロンプトの扱い（肯定的誘導が有効）の特殊性が指摘される。

### その他のモデル  
- **Krea2 / Krea-2-turbo**: 画像生成の主力候補としてAnimaと並んで言及。Turboは高速（数秒）で高品質だが、Danbooruタグ理解度はAnimaに劣る。RAWはLoRA学習向き。  
- **Qwen-Image（Qwen-Image-Edit / QIE）**: 編集性能が「オンリーワンクラス」。ピクセルずれが起きにくく、時間・天候変更などの指示追従性が高く、TEの性能が評価される。  
- **Z-Image（Turbo / Base）**: Turboの方が直接出力品質が高いとされ、公式も「Turbo優位」との発言あり。ただしBaseの方が自由度・追従性で優位との意見も。  
- **LTX（LTX-2.3 / LTX2.5）**: 日本語プロンプト追従性の弱さやH3との比較でネガティブに言及されることが多い（H3が一世代上）。動画生成の過去実績はあるが存在感が薄れている。  
- **Wan / illustrious / FLUX / NovelAI**: 言及が少なく、Wanは過去のt2v用途、illustriousはForgeユーザーでの定番、FLUXはref2v/fl2vの比較で名前が出る程度。選定理由の詳細はほぼなし。

**全体の傾向**  
Animaは「LoRAの作りやすさ・タグ制御」で、H3は「動画の動き・参照保持・マルチモーダル実用性」で選ばれている。ログはComfyUI移行やローカル活用の文脈が強く、速度・ワークフローの簡素化・特定用途特化が人気の要因。H3とAnimaの組み合わせ（H3動画＋Anima画像/LoRA）も話題。

## Web検索による参考情報  
- **MiniMax H3**: MiniMax（Hailuo AI）製のオープンウェイト汎用マルチモーダル動画生成モデル（2026年夏頃リリース）。テキスト・画像・動画・音声を単一コンテキストで扱い、最大2K解像度・15秒程度のクリップをネイティブステレオ音声付きで生成。T2V / I2V / ref2V / 編集に対応し、ComfyUIなどでローカル実行可能。Hailuo 3.0とも呼ばれる。[[1]](https://www.minimax.io/)[[3]](https://fal.ai/minimax-h3)[[4]](https://huggingface.co/MiniMaxAI/MiniMax-H3)  
- **Anima-2.9B**: CircleStone LabsのAnima 2Bを基にしたアニメ/イラスト特化のテキスト-to-画像モデル（約2.9Bパラメータ）。Transformer層拡張＋追加学習（約170万枚）のプレビュー版。Hugging Faceで公開されており、SDXLのillustrious的な位置づけ。[[5]](https://note.com/toshia_fuji/n/n4e6dea2891b3?hl=en)[[6]](https://huggingface.co/models?pipeline_tag=text-to-image)  
- **Krea-2-Turbo**: Krea AI製のテキスト-to-画像拡散モデル（2026年6月頃）。RAW（ベース）とTurbo（蒸留・高速版、8ステップ程度で数秒生成）の2種があり、Turboは高速イテレーション向き。LoRA対応。[[7]](https://huggingface.co/krea/Krea-2-Turbo)[[8]](https://www.krea.ai/models/krea-2-turbo)  
- **Qwen-Image-Edit**: AlibabaのQwenチーム製画像編集モデル（Qwen-Image基盤、20B規模）。セマンティック/アピアランス編集に強く、テキストレンダリングや精密編集に優れる。複数画像対応版（2511など）も存在。[[9]](https://qwen.ai/blog?id=qwen-image-edit)[[10]](https://github.com/QwenLM/Qwen-Image)

（情報は2026年8月時点の検索結果に基づく。モデルは急速に進化中。）
