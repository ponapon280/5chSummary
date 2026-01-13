### NovelAI (NAI)
- ログ内で言及なし。

### Pony
- ログ内で言及なし。

### illustrious (イラストリアス, リアス, ill, IL)
- >>710: 「ずっとWAIとoneの**リアス系モデル**ばっか使ってたけど、そろそろ乗り換えてもいい感じにはなったのだろうか」
  - 理由: 長く使用していたが、他のモデル（文脈からWan2.2やSmoothMixなど動画生成系へ？）への乗り換えを検討中。リアス系（illustriousの愛称）の使用実績あり。

### Noobai
- ログ内で言及なし。

### FLUX
- >>663: 「**FLF2V**にRife Tensorrtとアップスケーラーを組み込んだワークフローでおすすめあったら教えてクレメンス dasiwa純正WF使っとるんやがRife Tensorrtがないから組み込もうにも隠れまくってて分からん」
  - FLF2V（First Last Frame to Video?）のワークフロー関連で言及。Wan2.2との組み合わせ推測。
- >>774: 「Turbo LoRA出たから久しぶりに**Flux2**触ったんやけどオフロード処理がバグってるね ComfyUIはv0.8.0やけど4回目の生成でRAMのキャッシュがクリアされてモデルが再読み込みになる その際に192GBよりオーバーフローして読み込みが終わらない」
  - 理由: Turbo LoRAのリリースで久しぶりに試したが、バグ（RAMオーバーフロー、再読み込み）で使用意欲喪失。ハイエンド環境（192GB RAM）でも不安定。

### Wan
- 多数の言及あり。主に**Wan2.2**（動画生成モデル、特にI2V/T2V/V2V/FLF2V関連）が中心。SmoothMix、SVI、LTX-2などと組み合わせ多用。
  - >>631: Linux+7800XTでSmoothMix 2+2step生成（Windows 3060と同等速度）。TensorRTで高解像度/フレーム補完高速。
  - >>652: 「SmoothMix **WAN 2.2** Img2Vid v2.0」
  - >>653-654: SVIワークフローで**Wan**（kijai WanVideoWrapperフロー用LoRA）。nativeフロー用と分岐。
  - >>661: 「ltx2ちゃん**wan2.2**以上にちんぽねじ切り率高いんやが」→生成エロクオリティの文脈。
  - >>663-665,670-671: **FLF2V**（Wan2.2 First Last Frame to Video）のWF、条件付けゼロアウト、Rife Tensorrt組み込み。
  - >>704: 「**wan2.2 I2V**でお辞儀させられんのやろか？」（プロンプト試すが失敗）。
  - >>707,713: **WanImageToVideoSVIPro**ノード（ComfyUI-KJNodes）。PRでバッチ画像参照強化。
  - >>721: 「**Wan2.2 FLF2V**のWFならワイの神経質エディションでよければどうぞ」
  - >>728: SmoothMixで「The girl bows.」でお辞儀可能（純正**wan2.2**は不明）。
  - >>729: **Wan**のWFエラー。
  - >>740: SVI実験（**Wan**ベース？ anchor/prev/end画像参照）。
  - >>771: 「ZITで素材作ってQIEで調整して**Wan**で動画にしてLTX2で音声載せる」
  - >>776-779: LTX2のt2v/i2v/v2vで**Wan生成動画**に音声付与。リップシンク良し、音声はプロンプトベース（入力動画非依存）。
  - >>780: LTX2 v2vで**Wan**互換（video loader差し替え）。
  - >>808-809,812: **PainterLongVideo**（Wan上位互換、長尺/一貫性/顔キープ）と**SVI**（繋ぎ目違和感消し特化、アンカー癖あり）の使い分け。
    - 理由: PainterLongVideo（速度1で最終フレーム繋ぎ、エンド対応、顔キープ可だが継ぎ目違和感）。SVI（繋ぎ目完璧だがプロンプト追従低下）。長尺動画でSVI推奨。
  - >>810-811: LTX2トレーニングで**Wan動画**入力（パンパン音/喘ぎLoRA成功、BGM抑制）。
  - **選ばれている理由まとめ**:
    - 動画生成の定番（I2V/T2V/FLF2V長尺対応）。SmoothMix V2/SVI/LoRA（高速化、絵柄維持、動き補強）で強化。
    - 一貫性/繋ぎ目処理優秀（SVI/PainterLongVideo）。LTX-2音声合成との相性抜群（Wan動画→LTX2 v2vで音付与）。
    - 高品質エロ動画（NSFW LoRA多用、揺れ制御）。プロンプト効き/フレーム補完（Rife TensorRT）で高速・安定。
    - 欠点: お辞儀など特定動作弱い、VRAM食い（16GBカツカツ、DistorchMultiGPU推奨）。

### Qwen
- >>639: 「**qwen3-vl-8b-nsfw**に脚本書かせてみた」（VLM指示改変、LM Studio使用）。後半妖怪化問題。
- >>641: 「**GLM4.7**」→Qwen関連？（別モデルか）。
- >>655: 「**Qwen Multiangle Camera**のノード、雑にSDXLでのアングルプロンプト作成時の補助にもエエね」
  - >>675: SDXL仕様改造も「**Qwen**とSDXLとの言語理解の差にむせび泣く」（bird eye's view認識せず）。プロンプト作成補助に便利。
    - 理由: アングル/視点プロンプト生成補助（Multiangle Cameraノード）。SDXL互換改造で重み調整可能だが、言語理解差で限界。
- **選ばれている理由**: 脚本/プロンプト生成（VLM/LLM）でローカル使用。NSFW版あり、フォルダ整理可能（Cline経由）。視点指定の補助ツールとして便利だが、SDXLとの相性微妙。

---

### 抽出された生成AIモデル関連話題（除外モデル除く）

ログ全体から、生成AIの**モデル**（主に画像/動画生成モデル、LLMなど）に限定して話題を抽出。除外リスト（NovelAI, Pony, illustrious/イラストリアス/リアス/ill/IL, Noobai, FLUX, Wan, Qwen）に該当する言及は完全に除外。ツール/ノード/ワークフロー（ComfyUI系ノード、Kohya_GUIなど）はモデル本体でない限り除外。LoRAはモデル名と明示的に紐づく場合のみ含む。

#### 1. **LTX2 / LTX-2**（最多話題、動画生成モデル）
   - **主な話題**:
     | レス | 内容概要 |
     |------|----------|
     | 638 | LTX2向けエロLoRAが出現。 |
     | 658 | LTX-2向けRAMオフロード改造（self.memory_usage_factor調整でComfyがメモリ多め見積もり、オフロードしやすく）。 |
     | 664 | LTX-2のLoRA学習（画像のみ24GB未満、動画学習は16GB厳しい？）。 |
     | 752 | LTX-2でMMAudioとバイバイ（音声機能内蔵？）。 |
     | 766 | LTX-2でかわいい声生成可能（音注意）。 |
     | 768 | City96のGGUFローダー更新でKijai氏のLTX-2 GGUFが問題なく動作。 |
     | 776 | LTX2のt2v/i2v/v2v実験（実写面白いがi2vはアニメ絶望、リアル女性がババァ化など品質課題）。 |
     | 778 | LTX2品質はいまいちだがGrok/Sora2並みのローカル動画生成希望を抱かせる。 |
     | 793 | LTX2 i2v/t2v評価（i2v落差大、クリエイティブ向け）。 |
     | 810 | 5090でLTX2トレーニング（二次騎乗位動画ソースで声質/パンパン音強化成功、謎BGM抑制。映像学習微妙）。 |
     | 815 | LTX-2流行ってない？（品質低いがv2vキット）。 |
     | 825 | 動画生成品質低くWan2.1並み、流行当面先だがv2vキットでWan動画に音付け推奨。 |
   - **選ばれている理由**:
     - ローカルで音声付き動画生成（t2v/i2v/v2v、リップシンク良、動画無視でプロンプト音声生成）。
     - LoRA学習で声質/効果音カスタム可能（パンパン音強化成功）。
     - GGUF版で動作安定、RAMオフロードで低VRAM対応。
     - 全体: 動画+音声の統合で便利だが品質/i2v課題指摘多し。

#### 2. **SmoothMix / SmoothMixV2**（動画生成モデル）
   | レス | 内容概要 |
   |------|----------|
   | 646 | SmoothMixV2のEA未完でもGGUF版配布（作者紹介でOK）。 |
   | 653-656 | SVIワークフローでSmoothMix公式比モヤけ（LoRA誤用原因）、高速化LoRA推奨3.0で硬め絵柄維持良（dasiwa硬すぎる人向け）。 |
   | 714 | SmoothMixV2エラー多（真っ黒/ぼやけ）、GGUF版助かる。 |
   | 717 | High側SmoothMixV2+SVI LoRA0.8+高速化LoRA3.0で目の形維持良（enhancedNSFW比）。 |
   | 718 | SmoothMixV2 Highで真っ暗/ぼやけ（GGUF版推奨）。 |
   | 722 | SmoothMixV2真っ黒多発、GGUF版使用。 |
   | 734 | SmoothMix V2.0テスト（V1比頭上げ/口開き改善）。 |
   | 803-805 | SmoothMix V2+SVI LoRA+lightx2v高速化LoRA（推奨3.0、残像注意）。 |
   | 823 | High SmoothMixV2+Low DaSiWa8.1+SVIpro LoRA1+lightx2v（CFG低め推奨で顔変化抑制）。 |
   | 824 | DaSiWa高速化マージ済みならlightx2v不要。 |
   - **選ばれている理由**:
     - V2で挙動改善（頭/口動作自然）、GGUF版でエラー回避/高速。
     - 高速化LoRA（lightx2v 3.0）で絵柄維持/動き補強（硬めOK、dasiwa代替）。
     - SVI/FLF2Vと組み合わせ一貫性高、長尺以外でもLoRA必須。

#### 3. **dasiwa / DaSiWa**（動画生成モデル、Low側特化）
   | レス | 内容概要 |
   |------|----------|
   | 656 | dasiwa絵柄維持良だが硬すぎ（SmoothMixV2高速化LoRA代替）。 |
   | 717 | Low dasiwaV8（V9目の形変化多）、High SmoothMixV2併用で目維持良。 |
   | 723? | High dasiwaV8.1（SmoothMixV2+LoRA併用）。 |
   | 751 | enhancedNSFW揺れ過剰→SmoothMix animation LoRAマイナスで抑制（顔良化）。 |
   | 827-828 | Low DaSiWa8.1（高速化マージ済、顔変化気になるがfp16少数派、生成時間短縮優先）。 |
   - **選ばれている理由**:
     - Low側安定/高速（高速化マージ済）、絵柄維持力高（硬め指摘）。
     - SmoothMixV2 High併用で目/顔変化抑制、揺れ調整LoRA相性良。

#### 4. **SVI**（動画生成/長尺特化モデル）
   | レス | 内容概要 |
   |------|----------|
   | 653-654 | SVIワークフローLoRA誤用でモヤけ（native/kijai用2種）。 |
   | 677 | SVI+Rife-TensorRT成功、長尺難易度高。 |
   | 712? | WanImageToVideoSVIPro（KJNodes）。 |
   | 717 | SVI LoRA0.8必須、SmoothMixV2併用。 |
   | 738-740 | SVI実験（アルカナ・シャドウちゃん、anchor/prev/end参照癖）。 |
   | 803-805 | SVI LoRA必要（一貫性保つ）、PainterLongVideo代替（繋ぎ目違和感特化）。 |
   | 808? | SVIpro LoRA1。 |
   | 812 | SVI vs PainterLongVideo（繋ぎ目消し特化、anchor癖でプロンプト追従低下）。 |
   | 814 | VRAM長尺依存増（16GBカツカツ、無圧縮画像蓄積）。 |
   | 819 | VRAM不安定（ComfyUI0.7.0推奨、DistorchMultiGPUで空き確保）。 |
   - **選ばれている理由**:
     - 長尺/繋ぎ目自然（PainterLongVideo上位互換、違和感消し特化）。
     - LoRA必須で一貫性高（短尺も有効）、end参照強力だがanchor癖注意。

#### 5. **その他のマイナーモデル/LLM**
   - **GLM4.7** (641): H100レベル必要？
   - **Cerebras** (635,637): 新LLMクッソ早い（分散機能1つにまとめ人間接近）。
   - **enhancedNSFW (V2)** (717,751,789,799): 体/胸揺れ過剰（V2抑制、SmoothMix LoRAマイナスで良化、civitai人気NSFW LoRA源）。
   - **WAI / one** (710): リアス系から乗り換え検討（最近良くなった？）。
   - **miaomiao v1.3** (674): v1.2難あり→v1.3よさげ。
   - **reForge** (741): ComfyUI移行でプロンプト効き違い、要領掴み難。
   - **nano banana pro** (744): 生成+Grokファッション追加+動かす。
   - **City96** (768): GGUFローダー更新でLTX-2対応。
   - **PainterLongVideo (PLV)** (808-812,816): SVI代替（速度上げリアル化癖、繋ぎ目違和感、エンド対応上位互換）。
   - **lightx2v_I2V_14B_480p_cfg_step_distill_rank128_bf16** (805,823): SmoothMix高速化LoRA（3.0推奨、低CFGで顔安定）。
   - **LCM** (717): simpleでHigh2step/Low4step。

**全体傾向**: 動画生成（特LTX2/SmoothMixV2/SVI/dasiwa）が中心。Low/High併用、GGUF/LoRA/高速化でVRAM/速度/一貫性最適化。RTX5090/7800XT環境多。品質課題（顔変化/揺れ/エラー）解決策共有活発。