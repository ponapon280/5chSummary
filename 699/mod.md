# 🆕 新規トピック（前回からの差分）
### 流行の見立て
- 選定軸は、軽さ・速さ、編集時の元画像保持、参照追従、成人向け二次創作の実用、ライセンス、クラウド規制、既存LoRA、Seedで詰められるか、日本語と描き文字にほぼ集約される。
- 見立ての枠は「位置づけ / モデル / ログ上の温度」。
- 動画の実用本命はMiniMax H3（Ref2VA / FL2VA / Image Studio）で、運用は最も具体的だが全面採用ではなく用途分担。
- 人物・実写の物差しはKrea 2 / Krea 2 Turboで、比較基準として居座り、乗り換えより継続利用。
- クラウドの基準点はNovelAI V5で、日本語・文字・バランスに加え、規約とAnlasも同量の話題。
- 外部の上限・規制はSeedance、GPT Image、Nano Banana、Grok Imagineで、ローカル採用ではなく品質か規制の対照。

### MiniMax H3（Image Studio / FastH3 / Ref2VA / FL2VA）
- 除外対象以外で運用が最も厚い動画・画像モデルだが、全面採用ではなく用途で使い分けている。
- 冷める理由は使いにくい商用条件、ComfyUI更新による参照ノード破損、重いLoRA（4090でもギリギリで変化量は小さい）、特定アングルの学習不足と破綻、極端に遅い初速、同一設定での生成時間の暴れ。Singularityは外部では持ち上げられるがこの場ではほぼ不評で、Seedance生成物で学習したように見え、成人向け訴求がなく、3D・シネマ寄りで2D専門には無用、初期は革命的だったが今は話題がない。

### Krea 2 / Krea 2 Turbo
- 人物・実写・複数人・手指の本命として、他モデルの比較相手であり続けている。

### NovelAI Diffusion V5
- ローカル採用ではなく、クラウドの基準点。
- 選定理由は全体のバランス（この水準がローカルに来ればゲームセット）、日本語の直接指定、お手軽な位置指定と高精度インペイント、描き文字の文字と色の指示、Danbooru概念の一発出し、衣装の色と柄が混ざりにくいこと、ネガティブで画風を抑えると画力が上がる調整。漫画投稿やシチュ遊びの実用例はあるが、選定理由が明示されないものもある。
- 厚いのは不採用ではなく運用不安で、ログイン不能、V5規約による残Anlas失効、デフォルトCuratedで成人向けが出ず枠を無駄にした報告がある。ローカル勢がまだNAIに求めるのはほぼ描き文字だけ。
- 公式確認では2026年8月21日公開の非オープンウェイトで、V4.5の2倍超、32チャネルVAE、英日対応、1シーン最大22人、漫画ページ一括、文字最大750字、CuratedとFullがある。OpusはV5のAnlas量に連動する利用上限があり、コストがV4.5の2倍超になったことが公式理由で、ログの不安と一致する。

### Z-Image
- 選定理由はなく、QI2.1の複雑ポーズがKrea 2どころかZ-Image以下という比較の下限、緊縛が弱くKrea 2同様に不採用、公式アニメ側は学習ツール配布で終わりオープンソース継続で揉め、絵師タグの履修不足で実用圏外、という言及だけ。

### その他、選ばれているもの
- Ideogram 4.0はKrea 2から乗り換える積極理由が見えず使い慣れたものに戻った報告で、ライセンスが厳しいモデルはIdeogram 4程度の限定エコシステムにしかならない物差しにも使われる。
- Seedanceはローカル採用ではなくX上の動画品質の上限で、ローカルMiniMaxより上、Singularityの学習元ではないかという推測もある。
- Tsubaki.3は試用中で、漫画は人数が少なければ比較的自由という一言が中心で選定理由は薄い。PixAI側のtsubakiは成人向けで拒否された報告もある。
- Ming-Imageはデザイン特化でこの場の需要とはずれるが、アニメ化のベースなら画面のAI臭さが出にくいという見方で、積極採用の理由はない。
- GPT Image 2.0とNano Bananaは品質の天井で、Krea 2＋QI2.1はNano Bananaは超えたがGPT Image 2.0までは届かない、という序列がログ上の合意に近い。
- Grok / Grok Imagineは画像では規制が強く意図どおり作りにくいためMiniMaxへ流れる反動側。プロンプト作成用には、ローカル27B級がVRAMを食うのでコスパで選ばれている。
- GPT-6 Sol / Luna / AstraとClaude Opus 5.5は画像モデルではなく、実装・レビュー・Blender補助の使い分け。Astraは重い仕事、Solは通常作業、Lunaは成果物を求めない会話。Opus 5.5はAstraを一応超えた評で、課金を両方に寄せるかが話題。

### Web検索による参考情報
- ログの略称と公式事実のずれを優先確認。日付は公開情報ベースで、2026年時点のリリース。

### MiniMax H3 と周辺
- コミュニティライセンスは年商2,000万ドル未満なら帰属表示などの条件付きで商用可、超過は事前許諾、出力の他モデル改善への利用禁止、地域制限がある。ログの「商用不可で使いにくい」は無条件の商用可ではない点では当たるが、全面禁止とは公式条項が一致しない。Singularityは公式モデルではなくAIGC-SingularityによるH3のコミュニティ融合ファインチューンで、Image StudioもコミュニティのComfyUI実装。

### FLUX.2 Klein、Z-Image、Wan、LTX-2.3
- Z-Imageは通義系で、Turboは2025年11月26日・6B・Apache 2.0・8ステップ、未蒸留の本体は2026年1月27日。ログで選ばれていないことと、Turboがファインチューン向きでないことは一致する。
- Wanの公開ウェイト現行はWan 2.2（2025年7月28日、Apache 2.0）で、5Bと27B MoE（ステップあたり14B活性）があり、2.5以降のフロンティアは非公開。「周回遅れのWan」という自己評価は公開世代と合う。

### クラウドと比較対象
- Seedance 2.0はByteDanceのクローズド動画モデルで2026年2月12日公開、Dreamina／即梦の裏側。画像・動画・音声の同時参照とネイティブ音声が特徴で、公開時に動画アリーナ上位という報告があり、ローカル非採用・X上の品質上限というログと一致する。
- GPT Image 2は2026年4月21日、ChatGPT Images 2.5は2026年9月8日で、ログの「GPT-Image 2.0」は前者に対応する。Nano Banana 2はGemini 3.1 Flash Imageの通称で2026年2月26日。
- Grok ImagineはxAIの画像・動画機能で、2025年末から2026年のディープフェイク問題のあと画像生成は有料枠中心になり成人向け制限も強まった。動画1.5は2026年6月、解像度上限は720pという報道で、規制によりMiniMaxへ流れるというログと整合する。
- Ming-Image-0.1-Designは2026年9月22日、蚂蚁／inclusionAIの6B・MIT・UIとポスター向け・RGBA対応。KijaiのComfyUI対応は作業中という報道と一致する。
- Tsubaki.3はPixAIのホステッド旗艦で2026年9月に技術報告。前段のTsubaki.2は2026年3月のDiTで、ローカルのオープンウェイトとしては確認できない。

### プロンプト用・エージェント用
- Gemma 4は2026年4月2日公開。31B密モデルと、総量約26B・活性約3.8Bの26B-A4Bがあり、ログの「31Bは意図汲み、26B-A4Bは速度」はサイズ構成と一致する。
- GPT-6はAstraが2026年9月上旬、SolとLunaが9月22日。APIは前世代比50%減で、Solは入力100万トークン2ドル・出力10ドル、Lunaは0.10ドル・0.50ドル。Claude Opus 5.5も同日公開で前世代より安く、コーディング上位という同社発表。ログのラインナップ入れ替えと課金話はこの週の実リリースと重なる。Terraが「死んだ」はコミュニティ解釈で、公式の廃番告知は未確認。
- YuE2-3Bは2026年9月10日、m-a-pの音楽生成で約3.6B、CC BY-NC 4.0。SheetSage2による採譜が同じエコシステムにある。ログの「24GB前提でH3より難しい」は、非商用ライセンスとは別の運用上の話。

---
# 元の本文
テキスト内のモデル名・バージョン・サービスの事実関係を確認します。まず中心になっているモデルから調べます。このログ群は、コンシューマGPUとComfyUIを主戦場にする日本語コミュニティの抜粋です。話題の厚さと「実際に手を動かしているか」から見ると、新規の中心は画像の **Qwen-Image-2.1**、動画の **MiniMax H3** です。品質の物差しは **Krea 2**、二次イラストの現役は **Anima** と **Illustrious** のままです。LTX-2.3、Z-Image、Wan、FLUXは名前が出ても、この場の流行の中心ではありません。

## 流行の見立て

選ばれている軸は、ほぼ次のどれかに落ちます。軽さ・速さ、編集時の元画像保持、参照画像への追従、成人向け二次創作での実用、ライセンス、クラウド側の規制、既存LoRA資産、Seedで詰められるか、日本語と描き文字です。


| 位置づけ | モデル | ログ上の温度 |
| --- | --- | --- |
| 今いちばん厚い新規 | Qwen-Image-2.1 | 速さ・透過・編集で試されている。ライセンスと二次・ポーズで様子見も厚い |
| 動画の実用本命 | MiniMax H3（Ref2VA / FL2VA / Image Studio） | 運用が最も具体的。全面採用ではなく用途分担 |
| 人物・実写の物差し | Krea 2 / Krea 2 Turbo | 比較基準として居座り、乗り換えるより使い続ける側 |
| 二次の現役 | Anima、Illustrious | 新モデルに話題は移っても、実用の移行はまだ |
| クラウドの基準点 | NovelAI V5 | 日本語・文字・バランス。規約とAnlasの話も同量 |
| 外部の上限・規制 | Seedance、GPT Image、Nano Banana、Grok Imagine | ローカル採用ではなく、品質か規制の対照 |
| ほぼ不在 | LTX-2.3、Z-Image、Wan、FLUX | 比較の床、低VRAMの逃げ先、前例としての名前 |

## レポート

### Qwen-Image-2.1（QI2.1 / QIE2.1）

話題量が最大です。選ぶ理由と外す理由がセットで繰り返されています。

選ばれる理由は、まず軽さと速さです。12GB級でも編集に乗る、同ステップでKrea 2の約半分、旧来の重いbf16より明らかに短い、という実測が採用理由になっています。編集も実用域で、丸を描いて直す、outpainting、背景透過、衣装や髪型の差し替えが挙がっています。透過は「別モデルでキャラと背景を分ける自動化がしやすい」ことが採用理由です。日本語入力が楽で、文字の出も比較的よい、という評価もあります。参照でのキャラ固定、顔の同一性保持、ゲーム向けの細かい連打編集、という使い方でKrea 2やAnimaのEditより選ばれています。素の状態でフィルタが強くない点、AI ToolkitでのLoRA、ComfyUIの公開前対応も加点です。

選ばれない理由の最大はライセンスです。生成物・チューン・LoRAの金のやり取りに個別許諾が要る、という読みで、Anima後継のような大型二次FTは資金が集まらず来ない、商用で小銭を稼ぐ人には使いにくい、とされています。ログ内では「生成物の権利はユーザー」という公式発言をレギュラー投入の根拠にする側と、「商用不可」とする側が並立しています。性能面では、T2Iの人物・実写はKrea 2優位、ポーズと指は弱くZ-Image以下という酷評まである、Danbooru概念（`wariza` など）が通らない、二次の成人向けは素では期待薄、参照を足すと急に重くなる、という不満が繰り返し出ます。二次エロの実用基準としてはAnimaから移る段階ではない、という結論が複数回あります。

### MiniMax H3（Image Studio / FastH3 / Ref2VA / FL2VA）

除外対象以外では最も運用が厚い動画・画像モデルです。全面採用ではなく、用途で使い分けられています。

選ばれる理由は、参照画像を厳密に当てる編集が比較対象より強いこと、RefModに顔・三面・追加参照を梱包して再利用できること、動画モデル由来なので中間コマが取りやすいこと、ローカルでこの水準まで来る点です。r2vよりi2vの方が絵柄崩れがマシ、FastH3はスマホやFHDなら合格、Grok Imagineが規制で意図どおり出ないときmmH3の方が狙える、Seed固定で詰められる、音声参照とリップシンクはテキストエンコーダが賢い、という評価もあります。Krea 2が理解できなかった概念を、Qwenで出してからH3に渡すと通った、というパイプラインも報告されています。多くの人はRef2VA用ワークフローにFL2VAを載せ、品質と動きはFL2VA、眉毛などの意図はRef2VA、という使い分けです。

選ばれない、または冷める理由は、商用条件が使いにくい、ComfyUI更新で参照ノードが壊れる、LoRAが重く4090でもギリギリで変化量も小さい、特定アングルは学習が薄く破綻しやすい、初速が極端に遅く見える、同じ設定で生成時間が暴れる、です。Singularityは外部では持ち上げられるが、この場ではほぼ不評です。サンプルがSeedance生成物で学習したように見える、成人向けの訴求がない、3D・シネマ寄りで2D専門には無用、初期は革命的だったが今は話題がない、という総括です。

### Krea 2 / Krea 2 Turbo

人物・実写・複数人・手指の本命として、他モデルの比較相手になり続けています。

選ばれる理由は、肉付き・頭身・肌の生命感、複数人の掛け合いが独壇場であること、キャラごとの体型指定、指が強いこと、テキストエンコーダが強くDanbooruにない柄も自然文で詰められること、特定の実物（筐体など）のベース形状、使い慣れているので二次も三次もこれ、です。素の成人向けは弱いが、LoRA後の実用で残っています。小物まで詰めるキャラLoRAの上限としても、IllustriousやAnimaより上に置かれています。

選ばれない理由は、素ではフィルタが強く、二次エロはAnimaに遠く及ばず絵師タグで画風を調整できないこと、拘束表現で縄が破綻し積極的に乗り換える理由がないこと、キャラクターシートは編集モデルの方が楽なこと、長いプロンプトと構図がほぼ1対1でガチャ回しに向かないこと、状況依存の布の変形が意図どおりにならないこと、編集で元画像が微妙に変わることです。Krea 3は「出たか」という確認だけで、中身の話はありません。

### Anima（waiANIMA含む）

まだ選ばれ続けている二次の実用基準です。QwenやKreaからの移行は「まだ」という結論が繰り返されます。

選ばれる理由は、絵師タグ・版権・Danbooruタグを履修していること、タグと短い自然言語の両方が使えること、ComfyUIで手軽に二次元が出ること、キャラLoRAがIllustriousより作りやすいこと、狙った絵はLLMと相談すれば大体出ること、学習がQwen-Image-2.1より速いこと、構図出しや動画LoRAの素材生成に使えることです。自然言語は、タグだけでは書けない位置関係や、タグが伝染したときの逃げ道として評価されています。

弱点として他へ流れる理由は、テキストエンコーダが弱く長文で人数が崩れること、複数人の動きはKrea 2の独壇場なこと、手指、自作LoRAで頭が大きくなる、表情タグが不安定、役割が反転しやすい、Editでは元画像が微妙に変わる、です。キャプションは争点で、生成時にタグしか使わないなら自然言語は薄い、精度を求めるなら短い自然文を学習時と生成時の両方で使う、LLM全任せは不可、という整理に落ち着いています。

### Illustrious（リアス）

新しいモデルが出ても残る理由がはっきりしています。

選ばれる理由は、ランダム性が妄想の先まで行くので手軽に成人向けイラストが出ること、線と塗り、絵柄が今もトップで絡みや背景も一線級なこと、進化が止まった分FT・マージ・LoRAが厚いこと、タグが生成に直結するU-Netとして「ある意味の到達点」だということです。「リアスは抜きゲー、Animaは普通のエロゲ」という対比、Animaで構図を出してリアスでi2i、という既存ワークフローも残っています。指示遵守より「こういう絵が欲しいんだろ」とパターンを出してほしい人に合う、という選択理由もあります。低スペック（1660 Super級）でもまだ楽しめる、という環境理由もあります。

弱点は、ほくろの左右が分からないなど細かい指定に弱いこと、人数は2人が限界という対比、小物再現を詰める用途ではAnimaやKrea 2に負けることです。出自については「成人向けFTとして生まれた」説と「webtoon等の制作」説が並立し、ログ内では決着していません。

### NovelAI Diffusion V5

ローカル採用ではなく、クラウドの基準点です。

選ばれる理由として明示されているのは、全体のバランスがよく、このくらいがローカルに来たらゲームセットだということ、日本語の直接指定（「目頭の下にシワ」など）が通ること、お手軽な位置指定と高精度インペイント、描き文字のテキストと色を指示できること、`wariza` のようなDanbooru概念が一発で出ること、衣装の色と柄が混ざりにくいことです。ネガティブで画風を抑えると画力が上がる、という調整理由もあります。漫画投稿やシチュ遊びの実用例はありますが、選定理由の明示がないものもあります。

同時に厚いのは不採用ではなく運用不安です。ログイン不能、V5規約で残Anlasが失効する話、デフォルトのCuratedで成人向けが出ず枠を無駄にした、という報告です。ローカル勢がまだNAIに求めるのは、ほぼ描き文字だけ、という位置づけもあります。

### FLUX（主に FLUX.2 Klein）

積極採用の話は薄いです。日本語編集はQI2.1よりFlux2 Kleinの方が高い、肌の質感（産毛まで）はFLUXが上、イラストの画風指定ではMiniMaxより強い面がある、セミリアル変換が気に入っていた、という比較だけです。流れとしては「大まかな形はQI、仕上げはFLUXかKrea」で、QIの高解像度ポン出しを見て「QI一本でも」という反論もあります。ライセンスが出るたびに生成物の扱いが問題になる、という前例としても名前が出ます。

### Wan

選ばれている理由は性能ではなく、MiniMaxもQwenも動かせないので周回遅れのWanを使っている、という環境理由です。成人向けが強すぎて困る一方、飛沫表現は出せない、という不満があり、これを理由に選んでいる記述はありません。自由文プロンプトが使える例としてLTXやAnimaと並んだ一文もあります。

### Z-Image

選ばれている理由はありません。QI2.1の複雑なポーズはKrea 2どころかZ-Image以下、という比較の下限、緊縛が弱くKrea 2と同様に不採用、公式アニメ側は学習ツール配布で終わりオープンソース継続で揉めていた、絵師タグの履修が不十分で実用圏外、という言及だけです。

### LTX / LTX-2.3

ほぼ不在です。ある範囲では言及なし、別範囲でもLTX2のnvfp4は「非常に速いが順当に劣化する」という比較基準が1件、自由文が使える例としての並列が1件だけです。版名LTX-2.3を選んで使う理由は書かれていません。

### その他、選ばれているもの

**Ideogram 4.0** は、Krea 2から乗り換える積極理由が見えず使い慣れたものに戻った、という報告です。ライセンスが厳しいモデルはIdeogram 4程度の限定エコシステムにしかならない、という物差しにも使われています。

**Seedance** はローカル採用ではなく、X上の動画品質の上限です。ローカルMiniMaxより上、Singularityの学習元ではないか、という推測もあります。

**Pony** は過去の成人向け・脱衣表現の強さとして引き合いに出され、今のKrea 2がその点で劣る、という位置づけです。現行の第一候補ではありません。

**Tsubaki.3** は試用中、漫画で人数が少なければ比較的自由、という一言が中心で、選定理由は薄いです。PixAI側のtsubakiは成人向けで拒否された、という報告もあります。

**Ming-Image** はデザイン特化でこの場の需要とはずれているが、アニメ化のベースなら画面のAI臭さが出にくい、という見方です。積極採用の理由はありません。

**SDXL** は現行の選択対象ではなく、絵柄とLoRA資産がまだ厚い、複数人は混ざる、キャプションはDanbooru以外がノイズだった、という過去世代の対比です。

**GPT Image 2.0** と **Nano Banana** は品質の天井です。Krea 2＋QI2.1はNano Bananaは超えたがGPT Image 2.0までは届かない、という序列がログ上の合意に近いです。

**Grok / Grok Imagine** は画像モデルとしては規制が強く、意図したものが作りにくいのでMiniMaxへ流れる反動の側です。一方、プロンプト作成用には、ローカルの27B級がVRAMを食うのでコスパで選ばれています。

**Gemma 4** はプロンプト用です。31Bは雑な説明から意図を汲む力がQwen系27Bとは比較にならない、26B-A4Bは速度、が選定理由です。

**GPT-6 Sol / Luna / Astra** と **Claude Opus 5.5** は画像モデルではなく、実装・レビュー・Blender補助の使い分けです。Astraは重い仕事、Solは通常作業、Lunaは成果物を求めない会話、という理由が具体的です。Opus 5.5はAstraを一応超えた、という評で、課金を両方に寄せるかが話題です。

ログの「Qwen3.8 27B」は、画像からプロンプトを作る用途で8Bでは不足だから大きいのを持ってくる、という文脈です。公式のモデル名としては確認できません。

## Web検索による参考情報

ログの略称と公式の事実がずれている箇所を優先して確認しました。日付は公開情報ベースで、2026年時点のリリースです。

### Qwen-Image-2.1

2026年9月20日公開。視覚生成部は7B、32層の単流DiT。テキストエンコーダはQwen3-VL-8B。VAEはRGBA対応で、透過は後処理の切り抜きではなくネイティブです。参照画像は最大10枚、既定出力は2K、公式例のステップ数は40です。公開当日からComfyUIを含む複数ランタイムが対応しています。[[1]](https://qwenlm.github.io/blog/qwen-image-2.1/)[[2]](https://www.marktechpost.com/2026/09/21/alibaba-qwen-releases-qwen-image-2-1/)[[3]](https://apidog.com/blog/what-is-qwen-image-2-1/)

ライセンスはQwen Research Licenseで、モデル本体の商用利用には別契約が必要です。前世代のQwen-Image 2512やEdit 2511はApache 2.0のまま、という整理が複数の解説で一致します。[[4]](https://locallyuncensored.com/blog/qwen-image-2-1-explained.html)[[5]](https://github.com/QwenLM/Qwen-Image-2.1?tab=License-1-ov-file) ログで割れていた「生成物の権利」は、公開翌日の公式側の説明として「出力はライセンス対象のMaterialsに含まれず、生成した画像の権利はユーザーにある」とする解説があります。同時に、出力を使って学習・配布する派生モデルには「Built with Qwen」等の表示義務があります。[[6]](https://saascity.io/blog/qwen-image-2-1-local-text-to-image-editing-guide)[[7]](https://4sysops.com/archives/qwen-image-2-1-challenges-closed-models-while-alibaba-clarifies-output-rights/)[[8]](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/LICENSE) ログの両論は、モデル利用と生成物所有を混ぜていた、と読むのが事実関係に近いです。

ログの「8B」はテキストエンコーダ側の話で、拡散本体は7Bです。「Qwen3.8 27B」という公式名は確認できません。近い実在名はQwen3.6-27BやQwen3-VL-32Bです。[[9]](https://www.siliconflow.com/models/compare/qwen3-vl-32b-thinking-vs-qwen3-6-27b)

### MiniMax H3 と周辺

2026年7月31日公開のオープンウェイト動画モデルです。ネイティブ2K、24fps、5〜15秒、同一パスでステレオ音声を出します。入力はテキストに加え、最大9画像・3動画・3音声、という公式説明です。一部サービスではHailuo 3.0とも呼ばれます。[[10]](https://www.minimax.io/blog/minimax-h3)[[11]](https://blog.siray.ai/minimax-h3-hailuo-3-0/)[[12]](https://www.minimaxh3.com/) ComfyUIローカルではT2V/I2V用のFL2VAと参照用のRef2VAが別ウェイトで、テキストエンコーダは量子化Qwen3-VL 32B、という導入記事があります。ログのFL2VA / Ref2VAの使い分けと一致します。[[13]](https://news.qiniu.com/archives/1786351769428)

コミュニティライセンスでは、年商2,000万ドル未満は帰属表示などの条件付きで商用可、それを超えると事前許諾、出力を他モデルの改善に使ってはならない、地域制限がある、という条項が確認できます。ログの「商用不可で使いにくい」は、無条件の商用可ではない、という意味では当たっていますが、全面禁止とまでは公式条項と一致しません。[[14]](https://raw.githubusercontent.com/XGEN-Labs/XGEN-JING/main/LICENSE)[[15]](https://support.comfy.org/articles/6065098425-minimax-commercial-licensing-who-needs-a-license-and-how-to-get-one) SingularityはMiniMax公式モデルではなく、AIGC-SingularityによるH3のコミュニティ融合ファインチューンです。[[16]](https://comfyui-wiki.com/en/news/2026-09-07-h3-singularity) Image StudioもコミュニティのComfyUI実装です。[[17]](https://github.com/astropuzzo/ComfyUI-MiniMax-H3-Image-Studio/blob/main/CHANGELOG.md)

### Krea 2

2026年6月22日にオープンウェイト公開。12BのDiffusion Transformerで、未蒸留のRawと、蒸留済みで高速なTurboの二本です。公式の推奨は「LoRAはRawで学び、推論はTurbo」です。テキストエンコーダはQwen3-VL系です。[[18]](https://huggingface.co/vantagewithai/Krea-2)[[19]](https://github.com/krea-ai/krea-2/blob/main/README.md)[[20]](https://dataphoenix.info/news/krea-2-diffusion-transformer-image) ライセンスはKrea 2 Community Licenseで、一定規模以上の組織利用は有償、違法生成への技術的防止も求められます。[[20]](https://dataphoenix.info/news/krea-2-diffusion-transformer-image) Krea 3の公開は、今回の検索では確認できません。ログの「未着」と矛盾しません。

### NovelAI Diffusion V5

2026年8月21日公開のホステッドモデルで、オープンウェイトではありません。V4.5の2倍超の規模、32チャネルVAE、英語と日本語の公式対応、1シーン最大22人、漫画ページ一括、文字は最大750文字、という公式説明です。CuratedとFullの両方があります。[[21]](https://journal.novelai.net/image-generation-novelai-diffusion-v5-is-here-c2df7c6b8d2d/)[[22]](https://novelai.net/v5) OpusにはV5生成のAnlas量に連動する利用上限があり、運用コストがV4.5の2倍超になったことが理由、と公式が説明しています。ログのAnlas・上限の不安と一致します。[[23]](https://journal.novelai.net/opus-usage-limit-explained-jp/)

### Anima と Illustrious

AnimaはCircleStone LabsとComfy Orgの共同モデルで、正式版は2026年5月15日です。拡散部は約2B、テキストエンコーダはQwen3 0.6B、VAEはQwen-Image系です。Danbooruタグと自然言語の両方で学習されています。SDXLのファインチューンではなく、Cosmos系のバックボーンです。[[24]](https://gigazine.net/gsc_news/en/20260515-anima-image-generation-ai/)[[25]](https://comfyui-wiki.com/en/models/anima)[[26]](https://civitai.com/articles/35368/the-ultimate-anima-prompting-guidebook-all-you-need) ログの「2.9Bか3.8Bか」は公式仕様と一致しません。waiANIMAは公式ではなく、Anima Base上のコミュニティチェックポイントです。[[26]](https://civitai.com/articles/35368/the-ultimate-anima-prompting-guidebook-all-you-need)

IllustriousはOnoma AIのSDXL系で、Danbooruタグを軸に大きなLoRA生態系を持っています。Civitai上のLoRA数はAnimaより一桁多い、という集計もあります。v1.0は2024年、その後v3系まで更新されています。[[27]](https://decrypt.co/300744?p=300744)[[28]](https://www.illustrious-xl.ai/blog)[[29]](https://civitai.com/ecosystems/anima) 「タグが効くU-Netで、資産が厚いから残る」というログの理由は、アーキテクチャと生態系の事実と整合します。

### FLUX.2 Klein、Z-Image、Wan、LTX-2.3

FLUX.2 Kleinは2026年1月15日公開。生成と編集を統合した小型モデルで、4BはApache 2.0、9Bは非商用ライセンスです。9Bは8BのQwen3テキスト埋め込みを使います。[[30]](https://t.co/bvrg6fEr5g)[[31]](https://raw.githubusercontent.com/black-forest-labs/flux2/main/README.md) ログの「TEは同じ8B級なのに日本語編集はKleinの方が上」は、エンコーダ規模の比較としては成立します。

Z-Imageは同じ通義系です。Turboは2025年11月26日、6B、Apache 2.0、8ステップ。未蒸留のZ-Image本体は2026年1月27日です。[[32]](https://lovegen.ai/z-image-turbo)[[33]](https://github.com/Tongyi-MAI/Z-Image/blob/main/README.md)[[34]](https://howaiworks.ai/models/z-image) ログで選ばれていないことと、Turboがファインチューン向きではないことは一致します。

Wanのオープンウェイトの現行はWan 2.2（2025年7月28日、Apache 2.0）です。5Bと、27B MoE（ステップあたり14B活性）があります。2.5以降のフロンティアはウェイト非公開です。[[35]](https://howaiworks.ai/models/wan)[[36]](http://wan.video/blog/wan2.2) 「周回遅れのWan」というログの自己評価は、公開ウェイトの世代と合います。

LTX-2.3は2026年3月5日公開の音声付き動画モデルで、約22B、オープンウェイト、ローカル実行、最大4Kです。年商1,000万ドル超は商用ライセンスが必要、とされています。[[37]](https://ltx.io/newsroom/ltx-2-3-offers-creative-intelligence-without-the-cloud-costs)[[38]](https://huggingface.co/Lightricks/LTX-2.3) 性能やエコシステムの有無にかかわらず、このログ群では流行していません。

### クラウドと比較対象

Seedance 2.0はByteDanceのクローズド動画モデルで、2026年2月12日公開。Dreamina / 即梦の裏側です。画像・動画・音声の同時参照とネイティブ音声が特徴で、公開時に動画アリーナ上位という報告があります。[[39]](https://www.eesel.ai/blog/dreamina-seedance-2) ログが「ローカル採用ではなくX上の品質上限」と扱っていることと一致します。

Ideogram 4.0は2026年6月3日のオープンウェイトです。約9.3BのDiTに凍結Qwen3-VL-8B、ネイティブ2K、文字とバウンディングボックス制御が売りで、商用は有償ライセンスです。[[40]](https://ideogram.ai/news/ideogram-4.0/)[[41]](https://the-decoder.com/ideogram-4-0-drops-as-an-open-weight-model-with-native-2k-resolution-and-improved-text-rendering/)[[42]](https://x.com/ideogram_ai/status/2062956406341517608) ログの「限定的なエコシステムになりやすい」という比喩の相手として、ライセンス形態は当たっています。

GPT Image 2は2026年4月21日、ChatGPT Images 2.5は2026年9月8日です。ログの「GPT-Image 2.0」は前者に対応します。[[43]](https://overchat.ai/ai-hub/gpt-image-2-vs-nano-banana-2)[[44]](https://openai.com/index/introducing-chatgpt-images-2-5/) Nano Banana 2はGemini 3.1 Flash Imageの通称で、2026年2月26日です。[[43]](https://overchat.ai/ai-hub/gpt-image-2-vs-nano-banana-2)[[45]](https://the-decoder.com/google-explains-the-differences-between-its-three-nano-banana-image-generation-models/)

Grok ImagineはxAIの画像・動画機能で、2025年末から2026年にかけてのディープフェイク問題のあと、画像生成が有料枠中心になり、成人向けも制限が強まっています。動画1.5は2026年6月、解像度の上限は720pという報道です。[[46]](https://geotoolbox.ai/blog/grok-imagine)[[47]](https://thecourier.com/news/705411/grok-chatbot-restricts-image-generation/)[[48]](https://winbuzzer.com/2026/06/18/xai-speeds-up-grok-imagine-video-15-for-ai-video-creators-xcxwbn/) 「規制で意図どおり出ないのでMiniMaxへ流れる」というログと整合します。

Ming-Image-0.1-Designは2026年9月22日、蚂蚁 / inclusionAIの6B、MIT、UI・ポスター向けでRGBA対応です。KijaiによるComfyUI対応は作業中、という報道と一致します。[[49]](https://datanorth.ai/news/ant-group-releases-ming-image-0-1-design)[[50]](https://comfyui-wiki.com/en/news/2026-09-23-ming-image-design)

Tsubaki.3はPixAIのホステッド旗艦で、2026年9月に技術報告が出ています。前段のTsubaki.2は2026年3月のDiTです。ローカルのオープンウェイトとしては確認できません。[[51]](https://docs.pixai.art/docs/models/tsubaki3)[[52]](https://blog.pixai.art/en/tsubaki-3-technical-report/)[[53]](https://docs.pixai.art/docs/models-and-lora/tsubaki2)

Pony Diffusion V6 XLはPurpleSmartAIのSDXLファインチューンで、成人向けを含む大きなLoRA生態系があります。ログが「昔のPonyなら余裕だった表現」と比較している相手として実在します。[[54]](https://civitai.com/ecosystems/pony)

### プロンプト用・エージェント用

Gemma 4は2026年4月2日公開。31B密モデルと、総量約26B・活性約3.8Bの26B-A4Bがあります。ログの「31Bは意図汲み、26B-A4Bは速度」はサイズ構成と一致します。[[55]](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)[[56]](https://ai.google.dev/gemma/docs/core/model_card_4)

GPT-6は、Astraが2026年9月上旬、SolとLunaが9月22日です。API価格は前世代比50%減で、Solは入力100万トークン2ドル・出力10ドル、Lunaは0.10ドル・0.50ドルです。[[57]](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)[[58]](https://openai.com/index/introducing-gpt-6-sol-and-luna/) Claude Opus 5.5も同日公開で、前世代より安く、コーディングで上位という同社発表です。[[59]](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/) ログのラインナップ入れ替えと課金話は、この週の実リリースと時期が重なります。Terraが「死んだ」はコミュニティ解釈で、公式の廃番告知としては確認していません。

YuE2-3Bは2026年9月10日、m-a-pの音楽生成で約3.6B、ライセンスはCC BY-NC 4.0です。SheetSage2による採譜が同じエコシステムにあります。[[60]](https://localmodelwatch.tsuchitsuchi.com/en/2026/09/10/yue2-3b-music-generation-model/)[[61]](https://huggingface.co/thepatch/YuE2-3B-GGUF) ログの「24GB前提でH3より難しい」は、非商用ライセンスとは別の運用上の話です。
