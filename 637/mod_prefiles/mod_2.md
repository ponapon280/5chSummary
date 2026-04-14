### anima
- **247**: fp8版のanimaを使ってVRAM節約（理由: VRAM効率が良い）。
- **248-249**: AnimaでCN（ControlNet）を使えたら最高、anytest多用で完全移行できない（要望: CN対応で移行促進）。
- **250**: CNは正式版で対応予定。
- **253**: Canny/Anytestを使いたい、Animaでも出にくいポーズ/オブジェクト対応を望む。
- **254**: 比較: リアス（CNなし） < Anima（CNなし）、リアス（CNあり） > Anima（CNなし）、リアス（CNあり） ≒ Anima（CNあり）。CN使うならリアスでいい？という議論。
- **257**: リアスは右手、Animaはオナホ（上位互換、究極の選択）。
- **259**: Anima有利（あり比較でも表情個別指定、LoRA再現度高、背景/小物/群衆制御など多点優位、CN強度弱め可能で素の性能大事）。
- **260-261,265,285-286,290**: AnimaでHiresFix時に画面暗転/アウトオブメモリー（原因: VRAM不足、補助電源抜け、スペック不足）。
- **264**: AnimaとIL（illustrious）を反復横跳び使用。
- **266**: CNありリアスよりCNなしAnimaが複数描き分け強い、弱点は目的語弱い（3人以上試行錯誤必要）。
- **271**: Anima下げ意見に疑問、リアス比較はwai部族語1girl限定が多い。
- **277**: リアスwaiが今強いが、Anima派生（ファインモデル充実）で並び越すのは時間の問題。
- **278**: anima3で自然言語プロンプト（バイブ/まん汁滴り）成功、少しガチャ必要だが楽しい（理由: 自然言語理解高）。
- **279**: anima3でhires.fix使用可能、リアスの弱点解消、LoRA学習元絵柄乗る、満足（高速化非原因）。
- **280,282-283**: Animaでデブショタ/体格差出し方、size_difference難しいが自然言語で可能。
- **287**: AnimaでHires.fix（1536okだが2048ノイズ、リアス/ZIT推奨）。
- **289**: botan anima（civitai、Anima派生で本家に近い性能+画質向上）。
- **291**: Anima hires.fix可能だった。
- **294**: 分割でAnima大きく可能。
- **296**: Anima基本WFで女の子生成、アップスケール繋ぎ方不明。
- **314-315**: CNなしで構図制御（QWEN3.5で英文化+追記）、Anima自然言語能力高に驚き（CN相当可能）。
- **316**: Animaで漫画作ってる人感想求む（背景/表現加味）。
- **324**: tentacle in mouthで本体繋がらない問題、Animaなら大丈夫？
- **328**: Anima用LoRA「Scribble Reference」でCN Scribble相当。
- **332**: Anima軽い、量子化/読み込み設定でLLM併用可能（16GBで）。
- **336**: Animaモデル保存場所（Stability Matrix Packages下、クリーンインストールで消える懸念）。
- **357**: Anima暫定HiresFix（タイル、デノイズ0.12で継ぎ目なし、EasyCacheで生成時間許容）。
- **362**: Zimage二次元待ちのところにAnima登場で助かる（理由: 二次元対応）。
- **368**: AnimaYume 0.4リリース、派生モデル中心。
- **370**: Animaで即落ち2コマ、何でも可能（漫画ワンチャン）。
- **372-373**: anima3で3-4コマ（起承転結）可能、工夫次第（LLM翻訳プロンプト使用）。
- **374**: 漫画用途はSDXL（同一性保持優先）、Animaは多様性強いが品質バラつき。
- **392,399,401,406,414-415,420**: Animaサンプラー挙動変わりやすい（euler a扱いやすい、er_sde推奨/線パリッ、背景/線重視er_sde、キャラ重視euler a、res multistep、er_sde、Euler帰結）。
- **398**: Anima LoRA作成で512解像度の方が再現良い場合あり。
- **411**: Animaは1536以上不要、アプスケ書き込み増えず。
- **428**: Animaイマイチ理由は絵師タグ微妙（再現度高すぎて下手部分再現）、理想絵師探し必要。
- **432**: animayume順当うまくいってる。

**illustrious (リアス, ill, IL)**
- **254,259,266,270-271**: Animaとの比較多（CNあり強いがAnimaに表情/LoRA/背景制御で劣る、CNなしAnima > CNありリアス複数描き分け）。
- **257**: Anima上位（右手相当）。
- **264**: AnimaとIL反復。
- **277**: リアスwai今強い（ファインモデル充実チンコ絵出やすい）。
- **279**: リアス本体hires.fix（Animaでfires.fix解消）。
- **287**: hires.fixはリアス推奨。
- **406**: 最初リアスでeuler a（Animaはer_sdeで線パリッ）。

**Z-Image (ZIT, ZIE, Zimage)**
- **287**: hires.fixでリアス/ZIT良い（Anima2048ノイズ）。
- **362**: Zimage実写強いが二次元ファインチューン来ない（Anima助かる）。
- **384**: ZI(T)からLTXで遊べる。
- **411**: z-image hiresバキバキ（Animaで十分）。

**LTX (LTX-2.3, ltx2.3)**
- **355**: ローカル動画はLTX2.3多少触る。
- **380,384-386,388,390,393-395**: LTX2.3 FLF2V Templateで任意フレーム指定（v2v、キーフレーム、複数ガイド、ガチャ要素強、音声不気味注意、試行錯誤楽しい、distill lora調整）。

**Qwen-Image (Qwen-Image-Edit, Qwen-image-2.0, QWEN3.5など関連)**
- **252**: qwen3.5 4bでLLM併用（Animaと同時）。
- **314**: QWEN3.5で構図画像→英文プロンプト（Anima投入）。
- **318**: エロ画像編集でQwen-Image-Edit-2511脱獄版最強？
- **320-321,323,326,329,341,347,417**: LLM（Qwen含）+Anima連携（ComfyUIノード、VRAMオフロード、ollama cloud/sf w、API）。
- **361**: Qwen-image-2.0漫画出せる？（日本式コマ割り/日本語不明、Weight非公開）。

**その他（FLUX, Wan, NovelAI）**: ログ内に直接的な言及なし。

---

### 抽出された生成AIモデルに関する話題（除外モデル以外）

ログ全体から、指定の除外モデル（NovelAI, illustrious/リアス/ill/IL, FLUX, Wan, Qwen-Image, anima, Z-Image系, LTX系）を除いた「モデル」に関する言及を抽出。主に画像生成・LLM・動画生成・アップスケールモデルに焦点を当て、話題の文脈と選定理由（あれば）を記載。LoRAやサンプラー（euler a, er_sdeなど）はモデル本体でないため除外。ツール（Stability Matrix, ComfyUI拡張など）やControlNetプレフィックス（CN, Canny, Anytest）も除外。

#### 1. **LLMモデル（主にプロンプト生成・画像説明用併用）**
   - **qwen3.5 4b / gemma4 e4b** (252)
     - VRAM 12GB環境で画像生成（anima）と併用可能。LLM側が終わったらVRAM開放して並行使用。「英訳してって投げる程度すぐ終わる」「think無しで高速」。軽量量子化（4b/e4b）でVRAM節約が理由。
   - **QWEN3.5** (314, 323)
     - 構図のお手本画像を渡して画像生成用英文プロンプト吐出 → キャラ名/好み追記して画像生成。自然言語能力の高さでCN相当の構図制御可能。VRAM 12GBで片方ずつ使用（並行不可）。
   - **gemma4 31B** (360)
     - ローカルLLM性能の高さを絶賛（クラウド比圧倒的）。画像/動画生成の基盤として集約される未来を指摘。
   - **ollamaのcloudモデル / gemma4** (341)
     - SFWプロンプト生成ならVRAM不要（cloud）。NSFWはgemma4のDLモデル推奨で無難。
   - **Gemini** (267)
     - Stability Matrixのuvバグ解決試行したが失敗。GitHubで他ユーザーも同様症状。
   - **ComfyUI-QwenVL / comfyUI-image-to-text-node** (326)
     - LLMモデルをunloadオプションでVRAM自動解放。ComfyUI内でLLM→画像生成のワークフロー完結。
   - **lihaoyun6/ComfyUI-llama.cpp_vlm** (417)
     - ComfyUI環境でllama.cpp python pip install。VRAM 12GBで動作確認済み（manager警告あり）。
   - **grok** (366)
     - お手軽プロンプト生成に使用。自然言語プロンプトを構造化して画像/漫画生成補助。

#### 2. **画像/アップスケールモデル**
   - **RealESRGAN_x4Plus Anime 6B** (351)
     - WebUIで常用された4倍固定アップスケールモデル。ComfyUIでは「モデルを使って画像を拡大」ノードで4倍→リサイズ（Lanczos?）で負荷大。hires.fix相当の挙動疑問視。
   - **SDXL** (266, 374)
     - 複数の描き分け/画面分割で混ざりやすい弱点指摘。漫画用途で同一性保持最優先（背景破綻なし）。banana背景と人物別生成推奨。
   - **SD1.5** (394)
     - 過去のEulerサンプラー時代を回顧。「さっぱりしすぎてクオリティ疑問」だったがモデル進化で今はEulerで十分。
   - **nano banana / nanobanana** (374, 379, 389)
     - 背景きれい/破綻なしで漫画（四コマ）実用範囲内。単純性能でpony時代超えも可能。
   - **rouwei / wai** (271, 277)
     - rouwei: 自然言語で3人出力可能（部族語1girl比較でない本格評価）。
     - wai（リアスwai）: ファインモデル充実で「チンコにクル絵」出力優位。anima並び超えは時間の問題。

#### 3. **動画/漫画生成モデル**
   - **seedance2.0** (301, 303)
     - litVideoサービスで動画生成。順番待ち解消（お得サービス探し中）。
   - **Lumaのuni-1** (372)
     - プロンプトだけで数十ページマンガ作成可能。構造化プロンプト（1ページ一コマずつ）で反映良好。
   - **QI2512** (380)
     - LTX2.3 FLF2Vのキーフレーム指定テスト元絵。strength 0.7で10秒動画生成（一貫性/スロー問題あり、ガチャ要素強め）。

#### 抽出ノート
- **全体傾向**: LLMはVRAM節約・プロンプト補助（構図/英訳）で頻出。画像モデルは漫画/同一性でSDXL/nano banana評価高。動画はlitVideoサービス依存。
- **選定理由のハイライト**: VRAM制約（12GB民多め）で軽量LLM（4b/e4b）優先。漫画用途で同一性/背景安定（SDXL/nano banana）。自然言語制御でQWEN3.5絶賛。
- **除外確認**: anima/リアス/ZIT/LTX/Qwen-Image関連は一切抽出せず（例: 277のanima並び超えはwaiのみ抽出）。LoRA（Scribble Reference, botan animaなど）は派生/補助のため非抽出。

不明/マイナーモデル（PixAI Taggert, sa solver）はツール/サンプラー扱いで除外。追加ログで深掘り必要なら уточните。