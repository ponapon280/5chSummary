# 生成AI関連ツール話題 抽出レポート

## ComfyUI / カスタムノード

### MiniMax H3関連のノード構成・操作
- **Context Loopの長さ設定**: Context Loopの長さはRef2V Tagged Planのdefault duration secondsで決まると思っていたが、実際は各シーンのExact frames（もしくはSeconds）を足した数値。Plan defaultにするとdefault値が有効になる。Review Gateの数値はReroll時のシードと長さ（レス233, 238）
- **Scene LoRAのロード方法**: Plan内のScene Lora routeでシーンごとにLoraを選ぶ項目があるが、どこでロードするか不明。→ MiniMax H3 Scene LoRA SchedulerノードをPatchAttention系ノードの前に差し込み、入力のstateにMinimax H3 Contex Loop Startの出力のstateを繋ぎ、入力のlora_Aやlora_Bに使うLoRAを繋げばよい（レス251, 263）
- **LoRA読み込みに必要なカスタムノード**: 本体minimax_h3_ref2va_pruned_int8_convrot.safetensorsに、叡智LoRA MysticXXX_MMH3-V3.safetensorsと8step LoRA MiniMax-H3-Ref2VA-Acc-8Step.safetensorsを組み合わせる場合、LoRA読み込み用のカスタムノードを当てる必要がある。LoRAはComfyUI/models/pdd_acc/に配置（レス249）
- **Loop Studioのプロンプト作成**: Loop StudioのプロンプトはLLM(MMH3用Skills)を使用して作成したシーンごとのプロンプトをコピペして貼り付けて生成している（レス268）

### サンプラー
- **cfgpp_ud10_abサンプラー**: 新しく追加されたサンプラー。815stepぐらいで使うのが良さそう（レス236）

### ComfyUIへの移行・習熟
- A1111に固執してComfyUIに半年以上乗り遅れていたが、観念してComfyUIを始めたら1日で移行が完了し、数日後にはComfy Registryに登録してカスタムノードを配布していた。利用者側は根本的にそこまで難しいことをやっていない（レス266）
- A1111系で覚えたからcomfyuiにはテコでも動かん、エージェントに環境作らせるのは嫌がるという光景がスレで見られる（レス345）
- comfyui手動操作の知識はcomfyui以外では役立たない知識であり、手動操作にこだわるユーザーがちらほらいる（レス278）
- **ツール設計の工夫**: comfyuiに完全に依存するのはリスクが大きい。自分が作るツールは別にライブラリ化しておいて、カスタムノードはただのラッパにしておくのがよい（レス364）

### QwenEdit (QIE2511) 関連のComfyUI最適化
- ピクセルシフトの問題を解消するカスタムノードをとりにくニキが作成（レス433）
- ComfyUIの最適化の恩恵でQIE2511もturboを使わなくても1分以内に生成終わするようになった（レス433）

### Forge
- **neo更新のトラブル**: 何も考えずにforge neoを更新したらまともに動作しなくなった。慎重に更新する必要がある（レス426）

### kijaiのツール制作
- kijaiはOSS界隈のパイプが強く、いち早くツールを作っている。コードを見るとcodexで作っていることが分かる（レス340, 341, 360）
- 無償であらゆるテストして実装を繰り返していた。ComfyUI開発チームにコネで呼ばれている（レス356, 360）

## Codex（AIコーディングツール）

### ダウンロード問題の解決
- huggingfaceのデカいファイルダウンロードが失敗する問題についてCodex先生に聞いたら、キャッシュ用意して失敗しても途中から再開するようにする仕組みを作ってくれた（レス237）
- codexに投げてもできないことは結構ある。蓄積がないとcodexに「何を指示するか」で躓く（レス275）

### プラグイン作成・エラーチェック
- ツクールのプラグインやコイカツのプラグインはcodexが簡単に作ってくれる。ログ読み込んでのエラーチェックも速攻で終わる（レス329）

### Codex触るべきか
- まだcodexに触れていないが、動画作成で作業量が多いのでそろそろ触るべきか検討中。映像の創作とは感覚が異なる世界なので一度は触れてみることを推奨。分からなければChatGPTで相談するのも良し（レス280, 281）

### Codexの限界
- ゲーム作らせようとすると、人間が手綱を握って方向性を指し示さないと「安全安全安全」と言いながら無限にいらんことばっかやり、極小リスクを延々潰しているのをトークンと金と時間を溶かしながら見守る時間になる（レス283）

### エージェントAIでのクリエイターアプリ操作
- エージェントAIでblenderを操作させて3DCGモデルを作らせたり、UE5やUnityでゲームを作らせている海外ユーザーがいる（レス300）
- ただし現状ではある程度blenderや3DCGの知識がないと無理。AIに3Dモデルを作らせると造形がぐにゃぐにゃで頂点が物凄く多い激重の全く使えないモデルになる（レス307, 313）

## ダウンロードツール

### ブラウザ・ダウンローダーの使い分け
- **Firefox推奨**: 10GB以上あるようなクソデカファイルをChromeで落とすと、ほぼダウンロードが終わるころにやり直しになるため、Firefoxで落としている（レス235）
- **aria2c推奨**: デカいファイルDL時はダウンローダー(aria2c)を使用。中断再開や分割DLができる利点と、軽量なことが利点。鯖のふ化が少ない（レス240, 241）
- **公式CLI推奨**: huggingfaceはデカいファイルが失敗するようになったため、コマンドプロンプトでhuggingface-cli downloadを指定して直ダウンロード。これで失敗しない（レス239, 243）
  - 例: `huggingface-cli download Comfy-Org/MiniMax-H3 diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors --local-dir "D:\ComfyUI\ComfyUI_windows_portable\ComfyUI\models\diffusion_models"`

### Civitai・huggingfaceの比較
- Civitaiはダウンロードで苦労した記憶ない。huggingfaceはダウンロード完了したと思ったらエラーで一からやり直しになる（レス237, 239）

## その他ツール関連

### inochi2d + AI
- inochi2dを使って1枚絵からLive2d的なものを作ろうとした。GPTでレイヤー分けしてからinochi2dでレイヤーを再結合させようとしたができなかった。sonnetでは荷が重く、Fableやcodexを使えばできるか気になっている。最悪そこは手作業（レス328）

### Live2D（ツール選択の理由）
- クラウドAIで1枚絵からlive2dを作ることは不可能。live2dはlive2d社のプロプライエタリなソフトを使う必要があるため、クラウドAIのサポートには限界がある（レス292）

### beellama
- 前スレで教えてもらったbeellama。26BのQ4を使う→googleに聞いたらQATがいいらしい→UDmergeがいいらしいでモデルを試行（レス376）

### ファイル管理
- 思い出チェックポイントとLoRAを削除して20GB空いた。貯め込んだPNGをwebpにするかJPGにするか迷っている（レス422）