# 生成AI関連「ツール」話題抽出レポート

## ComfyUI / ComfyUI関連

- **ComfyUIのプロンプト权重変更仕様**: `from_side`のような2語の単語でctrl+↑/↓で重みを変更すると、単語全体を選択しない限り`(from:1.05)_side,`のように部分的にしか変わらない。カスタムノードを作って解決した（>>106）。仕様との回答あり（>>110）。
- **ComfyUI経由でのAIエージェント構成**: `Bionic ⇔ Comfy MCP ⇔ ComfyUI ⇔ Strata`の経路で結果的に連携可能になった（>>88）。Bionic(Gemma4 E2B)とComfy MCP経由での画像作成でAIエージェントごっこが実現。avif形式はBionic側が未対応、comfy-cliからの実行はextra_pnginfoが取得できずPowerPuterノードがエラーを出す（>>178）。
- **ComfyUI連携による対話型画像生成**: Open WebUIのComfyUI連携機能で対話型画像生成が可能。VRAMのアンロードをワークフローや連携処理に噛ませればメモリの天元突破を防げる（>>201）。
- **Open WebUI + Strata + ComfyUIのローカル環境構築**: Open WebUI＋Strata＋ComfyUIで画像生成（Krea2-turbo）させ、更に画像編集（Qwen-Image-2.1）も出来るようにした（>>170）。PC1台でグラボ2枚挿し（RTX3080でStrata、RTX5080で画像生成、RAM128GB）で稼働（>>199）。
- **Qwen3.8とComfyUIの比較**: 「qwen3.8使えたらなと思うんやがcomfyuiよりインストール難しそう」という理由で導入を躊躇（>>49）。
- **Krea2をComfyUIで使用**: AVのコマをKrea2でほぼ再現出来るようになった（>>44）。Krea2でパンツを穿かせると股間がモッコリする問題が発生（>>135）。
- **Krea2 + Codexのエージェント連携**: CodexにKrea2のプロンプト作成をさせ、生成画像を放り込んで修正箇所を比較・改善させる運用。髪色・髪型・目の色はワイルドカードでランダム性を出させている（>>101）。CodexにKrea2のプロンプト作成引き継ぎメモを作らせ、Grokにドロップして教えればGrokでも良いプロンプトが作れる（>>105）。
- **Krea2の機能に関する疑問**: Prompt Guideを見た印象では、Ideogram 4.0みたいに頭・身体・上腕等を個別指定できないのかという疑問（>>53）。
- **kijaiのhuggingface**: ターボ系が多数追加され、flashgenが一番使えそう。PDMD 2stepは動かないがクッキリ出る（>>165）。
- **Context Loop（動画生成ツール）**: R2Vでシーン毎に使う参照を切り替える方法について議論。Review CandidatesでApprove & stopして参照入れ替え後、Loop StartのStart Clipで番号指定して続きを作る方法がある（>>143）。HR-Endless-SamplerやH3-Longvideo等の代替もあるが、Context Loopが一番使いやすいという意見（>>147）。Extenderを使えば柔軟に対応可能（>>148）。MiniMax H3 Latent Relayの方がContext Loopよりきれいという情報（>>173）。

## Strata

- **Strataの概要**: Qwenを動かすエンジン。OpenAI/Claude Code API互換サーバーであり、OpenAI API互換ベースURL、Anthropic互換ベースURL、Claude Code互換ベースURLを提供。ComfyUIカスタムノードやBionicやUnslothで動く（>>81, >>90, >>214）。
- **選ばれている理由**: LM Studioよりもだいぶ早い（>>193）。Strataが動くようになり、Irodori-TTSのエロセリフ自作が難しかったのが解決した（>>108）。成年向けSkillsを作りたい用途にも関心（>>42）。
- **Strataの動作実績**: RTX3080でStrataを動かしRTX5080で画像生成する2GPU構成（>>199）。RTX4070ti 12GB + RAM96GBでもMMH3もStrataも使える（>>206）。RAM192GB環境にUD-Q4_K_XLを入れた結果、GPU使用量15.4GB、共有GPU使用量68GB、RAM使用量121GB、平均3338tok/s（64Kコンテキスト）。IQ3_Sが6377tok/sだから速度は遅い。規制解除できず画像も読めないため削除検討（>>150）。
- **Strataの調整**: 無修正版と画像読み込み機能を調整してエチエチな使い方ができるようになった（>>167）。
- **StrataのUI**: 標準WebUIで新しいチャットを開始するには入力欄左下のボタンをクリック。過去のチャットは保存されず破棄。会話を残したければアプリやハーネスにAPI経由で接続（>>195）。標準WebUIは体験版みたいなものなのでハーネスを使った方が良い（>>202）。System Prompt入力欄はないがAPI経由なら送れる（>>226）。
- **Strataへの評価**: 優秀だが気を抜くと「お前」呼びになり一人称が「俺」になる（>>123）。技術発展させて高速SSDさえあればOKみたいなところまでいくことを期待（>>205）。
- **Strataでツール作成**: 複数の画像からグリッド画像作るツールをQwen3.8 IQ2-XS Strata Unslothで作らせたらサクッと良いものができた。chatGPTに頼んだ場合は完成前に無料枠終了した（>>225）。
- **Strataの導入**: OpenAI/Claude Code API互換サーバーのため、対応しているComfyUIカスタムノードやBionicやUnslothで動く（>>81）。

## Hermes Desktop

- **おすすめ理由**: 全部入りでWindowsネイティブ版があるため楽（>>203）。Open WebUI＝LM Studio、Hermes Desktop＝LM Studio + Bionicのような位置づけ（>>210）。>>170の環境に対しておすすめされた（>>174）。

## Open WebUI

- **概要**: オンライン・ローカル共用のLM Studio的なUIを提供するツール（>>209）。ComfyUI連携機能で対話型画像生成が可能。OpenTerminal入れればOpenWebUIと連携してCodexみたいにファイル操作やコーディングができる（>>201）。
- **導入難易度**: 環境構築がめんどい。初心者ならWSLから始めてDockerコース（>>203）。

## Harness（ハーネス）全般

- **定義**: 「Harness」という名前のソフトが一個あるわけではなく、AIエージェント環境の種類。ブラウザ（Chrome/Firefox/Edge）と同じで、Agent Harnessという種類があり、DeepSeek Harness、Hermes、Codex、Claude Code等がある（>>214, >>215）。Qwenに手足を付けるAgent環境で、ComfyUIはその手足で操作する画像生成環境（>>214）。
- **用途**: ハーネス言うてもチャット用途ではスキルで読むファイルをルーティングして会話の幅広げるしか思いつかない（>>216）。Qwen3.8 flash nextはただのチャットには勿体無いからハーネスを使うべき（>>198）。

## Bionic

- **Bionicを使用したAIエージェントごっこ**: Bionicを使ってAIエージェントごっこしたい（>>80）。Bionic(Gemma4 E2B)とComfy MCP経由で画像作成が実現（>>178）。

## Unsloth

- **Strataとの組み合わせ**: UnslothでStrataを使っている（>>224）。Qwen3.8 IQ2-XS Strata Unslothでツールを作成（>>225）。

## Antigravity

- **Opus 5.5 Highの消費**: AntigravityでOpus 5.5 Highを5回試したら週間枠50%消費。5時間待ち制限とともに週間枠51%消費。添付PDF・動画の分析はできない。プランは月2,900円のGoogle AI Pro。年額一括（1万円ちょい）がコスパ良い（>>42, >>67）。

## VSCode + Continue

- **問題点**: VSCode + CONTINUEでやっていると高確率で追記を丸々上書きにする。調教し直しても忘れる（>>96）。

## Siki

- **用途**: 4chanスレの翻訳をDeepLのAPIでできないかとSikiで開いて相談した例（>>82）。

## その他ツール関連

- **MiniMax H3 Max R2V**: ほぼリアルタイム生成。リップシンク動画生成に使用（>>72）。
- **Eleven V4 TTS / Gemini 3.8 Flash TTS**: 大阪弁TTSを試した結果、Eleven V4の方が良かった（>>72）。
- **GPT-Image2.5**: 参照画像の生成に使用（>>72）。
- **GIMP**: LLMとのやりとりで生成された画像ファイルをGIMP等で普通に読める（>>181）。
- **Strata起動方法**: `START-HERE.bat --setup --host 0.0.0.0 --api-key <secret>`でスマホや他PCから開ける（>>90）。

## ハードウェア・スペック関連（ツール選択理由含む）

- **RAM不足の問題**: RAM32GBではMiniMax等が動かせない。+64GB増設を検討。5060Ti16GB保有（>>188）。動画作成やアプスケやエンコだとVRAM24GBとRAM64GBでも足りなすぎてスワップやエラー吐いて緊急停止多すぎ（>>169）。
- **LLM専用マシン**: LLM専用マシンがあると色々捗る。llm用に3060買い直しを検討（>>182, >>183）。
- **GPU選択**: AI用途ならproとか買った方が良い（>>39）。6090でもせいぜい48GB（>>37）。5090を買ったがqwen3.8がcomfyuiよりインストール難しそうで使えないと困る（>>49）。