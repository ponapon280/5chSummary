### 抽出結果：生成AI関連「ツール」に関する話題

ログから「ツール」（ComfyUI/comfy, A1111/Forge/reforge系, webUI系, SUPIR/nano-banana系など）に関する言及をすべて抽出。モデル（NAI, Pony, illustrious, NoobAI, FLUX/Wan/Qwenなど）関連の話題は除外し、ツール部分のみ記載。ツール選定理由が明示されている場合を★で強調。

#### ComfyUI (comfy) 関連
- **63**: 「ComfyUIの標準で使えるReroute見た目綺麗にできて便利やけど、ノード一直線でつないだ時、通常のノードのグリッドスナップと違う挙動やから水平にならないのすごいもどかしいで… ワイは10pxごとにスナップさせたいんや…」  
  → ComfyUIのRerouteノードのUI利便性とスナップ挙動の問題点。
- **85**: 「既にComfyUI公式がロースペ救済に動いてVRAM12GBでも...使える様になってるのにいつまでもeasywan22じゃなきゃやーやーなのとかクソきっしょい」★  
  → ComfyUI公式がロースペ（VRAM12GB）対応で優位。easywanからの卒業を促す理由。
- **87**: 「zuntanニキに頼らずともコマンドプロンプトに手動インストールと他人のワークフローを拝借していけば何とかなるだろ...easywanみたいな完成系は一気に色んな処理をやろうとするから難しいぞ」  
  → ComfyUIの手動インストールとワークフロー共有の柔軟性。
- **91**: 「ここだったか覚えてないけどComfyUIとかWan2.2もzuntanニキが作ったと勘違いしてる奴もいたしな」  
  → ComfyUIの普及とzuntanニキの誤解。
- **93**: 「Wa2.2リリース当初に比べるとComfyUIが神アプデかましてるからな ComfyUIの最新版入れて...公式テンプレにモデルだけGGUFに変えるで動くもの」★  
  → ComfyUIの神アプデで最新版+公式テンプレが使いやすく、GGUF対応でロースペ対応向上。
- **100**: 「comfyui自体よりsageattentionやtritonが死ぬほどめんどくさかった記憶やが今なら楽なん？」  
  → ComfyUIのインストール依存ツール（sageattention, triton）の面倒くささ。
- **102**: 「comfyuiは難しい それだけや」  
  → ComfyUIの難易度の高さ。
- **105**: 「stability matrixなら簡単に導入できるな 他のプラットフォームは知らない」  
  → Stability MatrixでComfyUI導入が簡単（推奨）。
- **115**: 「割とヘビー寄りのユーザー多そうなここ見てもcomfyUIの利用者が一気に増えたのはこの半年ぐらいの話やろな」  
  → ComfyUI利用者の急増（reforge開発状況や新モデル登場がきっかけ）。
- **123**: 「特に深く考えもなくreforgeやったけどforgeにしとけばよかった… refogeって拡張との親和性若干悪くね？ Regional Prompterの親和性悪いしLayerDiffuseもインストしたけど何度更新してもメニューに出てこねぇ」  
  → ComfyUI拡張（Regional Prompter, LayerDiffuse）の親和性問題（reforge比でforge推奨）。
- **124**: 「SimpleComfyUiを投入した時点で 色々と思うところはあったんかもなぁ」  
  → SimpleComfyUi（ComfyUI簡易版）の投入。
- **140**: 「ワイSmoothMixのWF作ったんやけど ZuntanのWFからDetailer持って来ようとしてもIn/Outが彼方此方飛んでて付いて行けずや 仕方ないから適当にSDXLのFaceDetailer持って来たら重いし綺麗じゃないし駄目ンゴね…」  
  → ComfyUIのワークフロー（WF）共有時のIn/Out接続の複雑さ。
- **144**: 「Wan2.2のDetailerはZuntanのWFから持ってくるのは諦めて、元ネタが配布してるWFを自環境に合うように調整して使っとるね」  
  → ComfyUIのWF調整の必要性。
- **163**: 「Flux.2でinput3枚 output なんかワイ環 Flux.2でinput image使うとVram大量に余して共有Vramつかってめっちゃ時間かかるんよね t2iなら大丈夫なんやけど」  
  → ComfyUIでのinput image使用時のVRAM挙動問題。
- **207**: 「flux2 テキストエンコーダbf16で生成（4080s/192GB/ComfyUI v0.3.75）...Distorch2使用時...」  
  → ComfyUI v0.3.75 + Distorch2の使用（RAM/VRAM消費と生成時間詳細）。
- **209**: 「FLUX.1-devのマイワークフロー(2段サンプラー)で...FLUX.1-devで32秒」  
  → ComfyUIのマイWF（2段サンプラー）の高速性。
- **212**: 「Set/Get使ってかんと配線がぐっちゃやなぁ…」  
  → ComfyUIのSet/Getノードで配線整理。

#### Forge / reforge 関連（A1111系フォークツール）
- **31**: 「flux2ってforgeのモデル差し替えるだけで動くんやろか」  
  → Forgeのモデル差し替えの簡単さ。
- **115**: 「利用者多かったであろうreforgeの開発状況が二転三転したり」  
  → reforgeの開発不安定。
- **123**: 「reforgeやったけどforgeにしとけばよかった… refogeって拡張との親和性若干悪くね？」★  
  → reforgeの拡張親和性悪く、forge推奨。
- **125**: 「リージョナルの代わりにforge coupleってのが頻繁にアップデートされてる LayerDiffuseは本家にある機能使ってるからその辺から機能を持ってこないといけない」  
  → forge coupleの頻繁アップデート（Regional Prompter代替）。
- **128**: 「今更環境を変えれないという結論になったからforge coupleっての見てみる LayerDiffuseも代替があるってこと？機能持ってくるってのがちょっとよくわかんない」  
  → forge couple / LayerDiffuse機能移植。
- **164**: 「forgeneoやからワークフローは無いんや」  
  → forgen eo（Forge派生？）のWFなし問題。

#### nano-banana / banana / bananapro 関連
- **22**: 「あんまりBANANA使った事無かったがフィギュア作ってgrokに回転させるだけでも楽しいものね」  
  → BANANA（nano-banana）の使用（フィギュア生成+回転）。
- **45**: 「bananaproのあと数日の遊び方を考え中」  
  → bananaproの使用。
- **190**: 「あと検閲に引っ掛からないものはBananaの方が性能高いと思う」★  
  → Bananaの検閲回避性能の高さ。
- **223**: 「「初音ミクがRTX5090を買う４コマ漫画を描いて」でflux2devとflux2proに作らせてみた nanobananaほどの日本語力じゃないけどproは使えそう」  
  → nano-bananaの日本語力の高さ（比較優位）。

#### その他のツール / 拡張 / WF関連
- **47**: 「家の場合はBTRFSパーティション（といっても4Tまるまるやけど）をComfy用に割り当てて遅いって感じはない」  
  → ComfyUI用のBTRFSパーティション割り当て（I/O高速化）。
- **123/125/135**: 「Regional Prompter」「LayerDiffuse」「forge couple」「ABG Remover」「rembg」  
  → 背景除去/レイヤー分離ツールの雑さや親和性問題。
- **130**: 「pnginfoでforgeで再生成して切り抜くかGIMPあたりでヌいたほうが手っ取り早い」  
  → pnginfo + GIMPの代替使用。
- **135**: 「LayerDiffuse使ってみようかなって思ったんや ABG Removerもrembgも抜き方が雑でさ…」★  
  → LayerDiffuse/ABG Remover/rembgの背景除去精度不足。
- **137**: 「いまだeasywanから卒業できない 備え付けのモザイク、リファイナー、アプスケが便利すぎて」★  
  → easywanのモザイク/リファイナー/アプスケ機能の便利さ。
- **138**: 「ワイはWan2.1時代の機能ごとに分かれてるWFの方が使いやすかった」★  
  → 分割WFの使いやすさ。
- **140/144/166/168**: Zuntan / 元ネタWF / Detailer / FaceDetailer / WanDetailer / SEGS / ELT。  
  → WF共有/調整の難易度、Detailerの拡大v2v貼り付け機能。
- **171**: 「今すぐに5万円出せるなら尼でアドビCC買うのもええかも」  
  → Adobe CC（Photoshop）の代替推奨。
- **183/189**: 「WanDetailer」「ELT」「SEGSで取り出した部分を拡大してv2v」  
  → Detailerの詳細化機能。
- **193**: 「動画関連はTime to Moveのnative用ノードを色々試してるがちっとも上手くいかん 素直にWanVideoWrapper専用のノードを使った方がいいかもしれん」★  
  → Time to Moveノードの失敗 vs WanVideoWrapperノード推奨。
- **207/209/221/231**: 「Distorch2」「WaveSpeed」「TeaCache」  
  → Distorch2の画面操作安定化、WaveSpeed/TeaCacheの高速化期待。

#### 全体傾向
- ComfyUIが最多言及で、アプデ/ロースペ対応/WF柔軟性が選好理由。
- easywan/reforgeは便利だが卒業/親和性問題でForge/ComfyUIへ移行推奨。
- nano-banana系は日本語/検閲回避で優位。
- 抽出外：モデル（FLUX/Wan/Qwenなど）言及はツール文脈のみ残し、純粋モデル話題はスキップ。zuntanニキはWF提供者としてツール関連。