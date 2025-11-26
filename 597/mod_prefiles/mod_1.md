### 抽出結果: 指定モデルに関する話題

ログ（4〜241）から、指定されたモデル（NovelAI (NAI), Pony, illustrious(イラストリアス, リアス,ill,IL), Noobai, FLUX, Wan, Qwen）に関する言及をすべて抽出。該当なしのモデル（NovelAI (NAI), Pony, illustrious, Noobai, FLUX）は一切言及なし。主に**Wan**と**Qwen**のみ。

#### Wan（主にWan 2.2, EasyWan, SmoothmixWan2.2など）
- **26**: nanobananaやべえな（※nanobananaは別モデル扱いだが、文脈でWan関連のLora学習・ComfyUIプロンプト不要化と関連づけ。理由: 知識不要で生成が容易になるため選ばれやすい）。
- **44**: WANを動かした時にLow側でComfyUIが強制終了（PyTorch 2.8.0以降で問題発生。一生2.7.1を使い続ける？）。
- **57**: Forge Neoはxformersとsageattentionに対応（Wanの基本速度問題なし。理由: カスタムノード多用時ComfyUIより速度・使い勝手が良い可能性で乗り換え検討）。
- **76**: gguf＋SmoothXXXAnimation(lora)で問題なく動く（ロースペ環境でgguf化・fp8化推奨。理由: VRAM/CPU RAM使い尽くしを防ぎ安定動作）。
- **78**: gguf＋SmoothXXXAnimation(lora)で動く（5090+RAM128GB環境でもロースペ扱いされ、FP16→FP8で解決）。
- **83**: wan2.2で6秒とか普通に作れる（5秒の壁突破。理由: 長尺動画生成が容易）。
- **105**: Smooth、FP16の3段サンプラー。最後にFP8で問題なく動く（モデル入れ替えでメモリ管理おかしくなる？）。
- **110**: 実質3つ分モデル入れ替えてメモリ管理おかしく（PyTorch 2.8.0以降/SageAttentionが原因？）。
- **128**: Wan2.2やQwen2509で生成時間に影響なし（iGPU併用無意味）。
- **131**: Wan2.2の話（自然言語翻訳ツール欲しい。理由: Google翻訳が効かず扱い難しい）。
- **194**: SmoothmixWan2.2でLoRA不使用、セックス20秒生成（目安定化にEnd画像不使用+プロンプト「動画の最後で目を開く」。理由: 中出し運ゲー回避にLoRA追加検討。入力画像正規化でワンクリック動画可能）。
- **197**: Wan animateのモデル（EasyWan22から移行。理由: 長尺楽、Video2VideoにFunControl+Animateが最新環境）。
- **212**: easywan22環境ならanimateが一番楽、長尺出来る（Wan animateモデルなしのためEasyWan22経由）。
- **213**: SmoothMixばっかり→Animateへ（Zuntan依存）。
- **225**: Wan 2.2(EasyWan+エロLoRA)（エロくするのに必須。理由: 本格エロにはローカルPCでこれ+ Qwen-Image-Edit 2509。作り込みにNano Banana Pro必要だが最終エロ出力はローカル最強）。

**Wan選定理由まとめ**: 長尺動画（6秒/20秒/30秒）生成が容易（5秒壁突破）、EasyWan/Smoothmixで安定・エロLoRA対応、ComfyUI/Forge Neoで速度優位。メモリ管理（gguf/FP8）でロースペ対応。エロ動画最強。

#### Qwen（主にQwen-Image-Edit-2509/2511, Qwen-Rapid-AIO-NSFW, Qwen Anime Beta2など）
- **39**: Forge NeoでQwenの処理遅い？（ComfyUIノード管理ダルいため乗り換え検討）。
- **40**: qwen-image-edit-2509で2次絵実写化、表情キープ方法なし（無表情化・表情変えるな無効）。
- **65**: Qwen-Image-Edit-Rapid-AIO実行でエラー（ドライバ更新推奨、8時間治らず）。
- **71**: 前スレからQwen動かんと書き込み（助け求め？エラーメッセージだけじゃレスなし）。
- **73**: ドライバ最新でもダメ。
- **76**: qwenのall-in-one（gguf化・fp8化でロースペ落ち防止）。
- **81**: アリババのQIE2511（infinit decomposition新機能。物体切り出し・配置換え？webtoon量産期待）。
- **85**: QwenImage全然更新されないのにEditだけ（QIE2511来週？T2I可能で普通Qwen不要？）。
- **87**: Forge NeoでQwen-Rapid-AIO-NSFW-v11.1使用（メタデータあり、プロンプト例。ComfyUI代替）。
- **88-89**: QwenImageEditはT2Iも可能、Qwen-Imageハイブリッド（普通Qwen不要？）。
- **90**: edit2509でT2Iグチャグチャ（誤用）。
- **91**: 無印editでT2I普通生成、高速化LoRA逆順で精度落ち（imageにedit用NG）。
- **94**: Qwen導入前後（角度調整夢→生成遅/画質落ち。RTX4090でもi2i厳しい）。
- **114**: editやるならRTX5070ti+メモリ？（3060tiでSSD削れ）。
- **116**: bf16主流、gguf_Q4で32GBOK（品質落ち）。
- **117**: 5070TI+128GBで80-100GB使用（bf16前提64GB足りず、96GBかも）。
- **128**: Qwen2509で生成時間影響なし。
- **135**: Qwen image edit2509はFP16表記だが中身BF16（FP16配布なし）。
- **143**: Qwen Animeチューン（自然言語+Danbooruタグで次世代。理由: 人物コンタミ回避・書き分け強い）。
- **177**: Qwen image edit2509 BF16確認（Civiti誤表記）。
- **216**: qie2511（gemini/nanobanana並み性能期待。ローカル限界？）。
- **225**: Qwen-Image-Edit 2509（エロくするのに必須。作り込みにNano Banana Pro）。

**Qwen選定理由まとめ**: 2次実写化/T2I/i2i編集強い（表情/角度調整）、2511新機能（レイヤー分割/透過pngで切り抜きゲームエンド）、エロNSFW版（Rapid-AIO-NSFW）、自然言語対応でタグ限界回避（Qwen Anime）。Forge NeoでComfy代替、bf16主流で高品質だがメモリ食い（128GB推奨）。更新頻度高（Edit特化）。エロローカル最強。

---

### 抽出された生成AIモデル話題（除外リスト外のみ）

以下は、ログから生成AIの「モデル」に関する言及を抽出したものです。除外リスト（NovelAI, Pony, illustrious, Noobai, FLUX, Wan, Qwen）に該当しないもののみ対象とし、重複を避けつつ、選ばれている理由や文脈を可能な限り記載。主にRouwei-Gemma、関連Gemmaモデル、NanoBanana系、SDXL、NetaYumeLumina、その他クラウドモデルが該当。

#### Rouwei-Gemma
- **101**: 「Rouwei-Gemmaお試し 細部の描写はともかく自然言語とnsfw両立するとこういうの出しやすくなるのはええな」  
  **理由**: 自然言語とNSFWの両立が優れており、こうした出力が容易になる点が評価。
- **143**: 「Rouwei-Gemmaがいまいち流行らん理由を原理も含めてちょっと調べた ... GemmaはDanbooru語は未履修だろうから ... ここはやっぱ自然言語記述+Danbooruタグ方式がちゃんといけてるNetaYumeLuminaやQwen Animeチューンみたいな次世代組に期待」  
  **理由（否定的側面）**: 翻訳家役（自然言語→意味ベクトル→SDXL）として精度が高いが、GemmaのDanbooru語未履修が弱点でエロ概念がSDXLに届きにくい。流行らない要因として生成時間4倍（163参照）と知名度不足を指摘。一方、CLIP併用でプロンプト追従性が高く、テキストエンコーダ能力向上→生成質向上の利点あり（163）。
- **163**: 「ワイRouwei-Gemmaのライトユーザーやけど ... CLIPとの併用で解決できる ... 生成時間が4倍近くになるデメリットには勝らないため大して流行らなかった」  
  **理由**: CLIP併用でDanbooru語弱点を補い、プロンプト追従性・生成質が向上。ただし時間デメリット大。

#### Gemma関連モデル（t5gemma系）
- **159**: 「丁度さっきt5gemma-2b-2b-ul2_encoder_onlyとt5gemma-2b-ul2_adapter_rw08_33k7.safetensors使ったけど なんかエロ含めてダンボール語通ってたよ？」  
  **理由**: Danbooru語（エロ含む）が通る点が確認され、Rouwei-Gemmaの代替/類似として動作良好。

#### SDXL
- **143**: 「自然言語→Rouwei-Gemma→(タグではなく意味ベクトル)→SDXLの流れ」  
  **文脈**: Rouwei-Gemmaの出力先として使用。直接の選定理由なし（基盤モデルとして）。

#### NetaYumeLumina
- **143**: 「自然言語記述+Danbooruタグ方式がちゃんといけてるNetaYumeLuminaやQwen Animeチューンみたいな次世代組に期待」  
  **理由**: 自然言語+Danbooruタグの器用な取り回しが優れており、Rouwei-Gemmaの弱点を補う次世代モデルとして期待。

#### Nano Banana / Nano Banana Pro / nanobanana
- **26**: 「nanobananaやべえな Lora学習してプロンプトがcomfyuiがみたいな知識はどんどん不要になるんやろうな」  
  **理由**: LoRA学習不要レベルの性能で、ComfyUIプロンプト知識が陳腐化するほどの進化。
- **223**: 「Nano Banana Pro 1日100画像 ... Gemini3とNano Banana Proの破壊力は過小評価できない」  
  **理由**: Google AI Pro内で1日100画像生成可能の高破壊力。エロ前作り込みに必須（225）。
- **232**: 「今更だけどbananaヤベーな プロット書いたらマンガ1ページ描いてくれるわ」  
  **理由**: プロット入力でマンガ1ページ生成可能の汎用性・ヤバさ。

#### Veo 3.1 (fast)
- **223**: 「Veo 3.1 fast 一日3動画 加えてVeo 3.1 fast細かい設定で1ヶ月当たり50動画生成可能 ... 月2900円のGoogle AI Proは契約せざるを得ないわ」  
  **理由**: Google AI Pro内で高速動画生成（1日3本+月50本）がコスパ良く、契約必須級。

#### Sora2
- **223**: 「Sora2とgrokは無料でも構わん」  
  **文脈**: 無料で使える代替として言及（選定理由なし）。

#### grok
- **223**: 「Sora2とgrokは無料でも構わん」  
  **文脈**: 同上。
- **160**: 「grok、ロリが厳しいっていうのはあくまでai目線で...」  
  **文脈**: ロリ/エロ判定の厳しさを指摘（否定的）。

#### その他（Smoothmixなど、Wan関連だが明示的に除外外）
- **141,194**: 「SmoothmixWan2.2」「smoothmixデビュー」  
  **文脈**: Wan2.2ベースだが、Smoothmix自体が独立話題として登場。まともに生成通るようになった点で好評（ただしWan除外考慮で境界的）。

**抽出総括**: 主にRouwei-Gemma（自然言語/NSFW両立やテキストエンコーダ強化が強みだが時間・Danbooru弱点で流行らず）とNanoBanana系（高生成量・マンガ生成能力）が目立つ。クラウドモデル（Veo, Sora2, grok）はGoogle AI Proのコスパ文脈で。ツール/ノード（Painter系, Forge Neo）はモデル非該当で除外。