### NovelAI (NAI)
- **491**: SDXLからオンラインサービスへ乗り換え検討中。NovelAIを候補に挙げる。理由: イラスト生成（エロ含む）で連続生成可能、何時間も回すのに適する。
- **495**: 絵ならWebサービスでNAIが性能上。ただし月額4k。
- **501**: NAIは性能上（ただし月額4k）。
- **514**: NovelAI無料分で感触よかったため課金予定。
- **517**: NovelAI課金は開始日基準で1ヶ月更新。

### Pony
- ログ内で言及なし。

### Illustrious (イラストリアス, リアス, ill, IL)
- **524**: 版権絵（NSFW含む）生成でillustriousのparuparuv4で止まっている。オススメを尋ねる。
- **544**: 安定して人気のIllustrious系: WAI-illustrious, Hassaku, Prefect, NTR MIX, Nova Anime。paruparu v4は1年くらい前で今でも通用するが、進化少ない。NoobAI系はObsession。
- **545**: paru4より新しいモデルは大概上。進化してないようでちゃんとしている。
- **547**: WAIは基準モデルで優秀。他のモデル触ってもすぐ戻る。
- **549**: Civitaiで「リアス系」とマークのモデルは実際全部noob系。純粋リアス系はほぼなし。WAIもv9頃からnoob eps1.1ベース。検索性考慮でリアス分類にしているモデルも。
- **551**: ILL系とNoob系はマージ多すぎて製作者の匙加減。区分けほぼ意味なし。
- **552**: v-predなのはnoob系。epsのnoobマージはリアス系。
- **553**: リアスとnoobの関係性ふんわり。境目薄い。
- **556**: マージ詳細不明なら高解像度対応→Illustrious2.0寄り、多キャラ対応→noob寄りで判断。
- **558**: WAIの優秀さはちびたい産LoRAのシェア率（waiナンバー違い考慮しても他と大差なし、ブランド強い）。
- **560**: WAIのNoobベースはWAI-SHUFFLE-NOOB（別物）。
- **571**: 全部Noob系は言い過ぎ。ライセンスで明確に分ける人も。WAIも分けてる。原神「ムアラニ」出やすさでNoob入り判定（今世代不明）。
- **575**: Nova Orange/Nova AnimeはNoobAI EPS v1.1 + Illustrious v2.0だがNoob寄り（横長画像で胴長問題、Il2.0ベースでも解消少ない）。
- **587**: paruV4から移行気起きない（脳勃起嫌、LoRA作り直し面倒）。
- **588**: paru4は人肌の影がノイズバグあり。乗り換えで解消大。
- **604**: WAI-illustrious-SDXL v15でmtu_virusの構図・服装一貫性安定。

### Noobai (NoobAI)
- **544**: NoobAI系はObsessionくらいしか知らない。
- **549**: Civitaiリアス系は全部noob系（WAIもnoobベース）。
- **551-556,571,575**: 上記Illustrious関連で頻出。Noob系としてマージベースが多く、リアスとの境目曖昧。多キャラ対応・高解像度判定基準に挙がる。EPS v1.1/Noob eps1.1がベース例多し。

### FLUX
- **620**: flux2.devでdfloat11圧縮できない（64GBメモリでも高騰）。
- **625**: flux2を救えるのはnuchakuだけ。
- **634**: flux2でDFloat11 Model Compressorエラー（pattern_dictに未登録？）。
- **640**: flux2圧縮にpattern_dict.py修正提案（ComfyUI-DFloat11-Extended）。

### Wan
- **493**: forge neoでwan2.2試すが解説少なくわからん。
- **536**: easy wanからsmoothmix移行したが開始画像無視で実写生成（T2Vモデル使用オチ）。
- **542**: ベースがWan Video 2.2 T2V-A14B（I2Vなし？）。
- **546**: GGUFにI2Vなし確認。
- **554**: smoothMixWan22I2VT2V_i2vHigh-Q4系GGUFファイル選択迷い（High3種）。
- **557**: 容量大=品質高（スペック対応で選ぶ、Q4K_M推奨）。
- **559**: M（要求高）で試す。
- **591**: SmoothmixWan2.2公式WF比較推奨。
- **594/597**: smoothmix step4→6推奨（low1ステップでノイズ）。
- **608**: smoothmix暴れ対策: Low/wan2.2、step8、wan2.2+LoRA、Q4限界割り切り。

### Qwen
- **499**: qwen2511早く来てくれーっ！
- **577**: Qwen-VL > Qwen3_VL_8B_NSFW_Caption_v45配置・json追記試すがエラー。
- **579/583/584**: マージせずディレクトリ配置、repo_id修正（thesby/Qwen3-VL-8B-NSFW-Caption-V4.5）。
- **593**: ディレクトリごと配置（hf CLI/git clone/手動DL推奨）。
- **614**: Qwen3-VL-8B-NSFW-Caption-V4.5無事動作。

---

### 生成AI「モデル」に関する話題抽出（除外モデル除く）

ログ全体から、生成AIの**モデル**（ベースモデル、派生モデル、LoRAなど）に関する言及を抽出。除外リスト（NovelAI, Pony, illustrious系, Noobai, FLUX, Wan, Qwen）を厳格にスキップ。主に**Z-Image**（Z-image, Zちゃん）と**SDXL**関連が中心。他は散発的。選ばれている理由や文脈も併記。

#### 1. **Z-Image (Z-image, Zちゃん)**
   - **最多言及モデル**。全体の半数近くを占め、熱狂的な話題。
     - 441: Z-imageのLoRA作成チュートリアル探し。自作LoRAがグチャグチャで、CivitAIの質の良いLoRAを羨む。AIToolkitデフォで失敗。
     - 443-444, 453: LoRA作成時のOptimizer（AdamW推奨）公開なし。ai-toolkit vs diffusersで差。秘伝の設定で試行錯誤。
     - 457: huge breastで服貫通防止策。
     - 464: dfloat試用。VRAM使用量↓だが生成時間↑（16GB環境でメリット薄）。Compressorノードでモデル圧縮可、Diffusers形式オンザフライ圧縮ノードあり。
     - 466: ベースモデル早く出せ。ターボ先行で生殺し状態。
     - 471: Forge NeoでZ-Image使用。操作簡単、メタデータjpg出力可、同じシード再現簡単。ただしVAE/TE指定不便。
     - 502: CivitaiのZimage用テトさん&サムスキャラLoRA同時使用。構造体ベースキャプションで複数キャラ同時生成可、Danbooruタグ利用。
     - 506: 位置関係明確指定可能で可能性大。Base主流化か？
     - 507-508: gigantic breasts LoRAあり。アジア顔になりやすい、手指増殖が難点。
     - 515: Zちゃんすごいが、絵師LoRA関係でSDXLから移行不可。
     - 518: エロチューンモデル待ち（Z-image含む土地確保段階）。
     - 522: Z-imageのエロチューン来るか？
     - 528: ちんこ表現いまいち、LoRA探しでふたなり先行UP。
     - 541: ベース学習不足で男器生やす難。
     - 561: ランダム性低すぎ不満→意味ない文字列入力で多様な画像。
     - 572: 自転車乗車画像で従来モデルより良い（ペダル/足処理向上）。
     - **選定理由の言及**:
       - 自然言語/位置指定/複数キャラ書き分け優秀（535, 506, 502）。
       - VRAM効率/圧縮対応（464）。
       - 構図/服装一貫性向上期待（604で類似言及だが他モデル）。
       - ベース/エロチューン待ちで移住保留（515,518）。
     - **ツール連携**: Forge Neo/ComfyUIで多用（471,617）。Zuntan氏のEasyImageEditでbf16/DFloat11/fp8_scaled/GGUF比較（617）。

#### 2. **SDXL**
   - 移行/比較話題多め。
     - 483: SDXLをComfyUIに移行。reForge機能あまり使ってなかった。
     - 491: SDXL使用中だが古いPCでフリーズ頻発→オンライン移行検討。
     - 515: 絵師LoRAでSDXLからZ-imageへ移行不可。
     - 583: SDXLもComfyUI移行。
     - 634: sdxl-flat。アップスケール時ゴリゴリ描き足し（ヘソ/アバラ/肉盛り影響）。フラット顔維持しつつ身体立体化欲（CunnyFunkyエミリア参考、SS LoRA試すが顔崩れ）。
     - **選定理由**: 絵師LoRA互換性高（515）。古いPC耐性低（491）。

#### 3. **その他のモデル/派生**
   - **ai-toolkit / diffusers**: LoRA学習ツールだがモデル関連（443-445,453,527）。作者解説で蒸留モデル学習NG→アダプター/LoRA推奨（2万ステップ可、539）。パラメータ/キャプション解説（527）。
   - **sdxl-flat**: 上記SDXL派生。アップスケール問題指摘（634）。
   - **AIDC-AI/Ovis-Image-7B (Alibaba)**: 637-642。新規登場で驚き/戦国時代突入？（640-642）。詳細不明だがAlibaba強さ言及。
   - **banana君**: 523。ウマ娘学習だが勝負服/キャラ不一致。
   - **CunnyFunky新作/エミリア**: 538,635。エロ漫画向き？立体感参考。
   - **幻神**: 534。中国由来で出力良好？
   - **StadyDancer**: 601。wan video wrapperでAnimateより参照崩れ少なく長尺可（顔検出なし）。

#### 全体傾向
- **Z-Image**がログの核心。LoRA作成/最適化/エロ特化待ちが熱い。VRAM効率/自然言語プロンプト強みで注目。
- SDXLは移行対象だがLoRA互換で粘る層あり。
- 新規モデル（Alibaba系）は混乱/期待混在。
- 除外モデル（illustrious/NoobAI/Wan/FLUX/Qwen/NAI/Pony）関連は大量スキップ（544以降の系譜議論など無視）。

抽出は文脈保持し、重複最小化。不明瞭/ツール寄りは除外。追加質問あれば уточ。