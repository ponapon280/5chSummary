# ツール関連話題抽出レポート

## ComfyUI / comfy

- **impact packのノード不具合**: impact packのノードが壊れまくっており、comfyの実装と噛み合っていないという報告がある（25）
- **MOSS用テンプレート**: ComfyUIを起動し、左メニューの「テンプレート」で「moss」を検索すればテンプレートが出てくる。凝ったWFでなくても動く（101, 144, 162）
- **標準のloraローダーの使い勝手**: 標準のloraローダーが使いにくいという指標。トリガーワードや推奨強度を管理できるカスタムノードの推奨を求める声あり（207）
- **comfy desktopへの移行**: 普通のcomfyからcomfy desktopの方が管理楽になったと聞いて導入したという報告（225）

## Forge / Forge neo

- **MOSS・animaでの動作確認**: 8700G機でforge neoを使ってMOSSとanimaを試したところ、APUでも一応動く。turboで1kでも1分半/枚かかる（56）
- **MOSS対応**: ComfyUIと同様にForge neoもMOSSに対応している（101）
- **easyReforgeユーザー**: 新規参入のeasyReforge民がたくさんいたという言及（166）

## カスタムノード（ComfyUI関連）

- **loraManager**: loraローダーの代替としてloraManagerを使っているという報告（209）
- **Ultimate lora loader**: 複数のLoRAを使う場合に簡単に変更できるためUltimate lora loaderを使っているという報告（211）

## LoRA学習ツール

- **KohakuMossTrainer**: 推奨設定（AIに丸投げ）で学習しており、今までのモデルの中ではラクな部類という評価（215）
- **fizgig**: MOSS用LoRA学習にfizgigを使い始めたという報告が複数あり、プリセットから選ぶだけで済む。キャプションはリアス時代のものをそのまま使用（216, 217, 218）
- **AnimaTrainFlow**: Anima用の学習ツール。こちらを使っていた身からすると、fizgigはLook Consistency Filterやmasked training、自然語キャプションなど知らないことが多くある（216）

## minimax（音声・動画ツール）

- **音声参照の代替手段**: voice designで声が固定できない問題に対し、気に入った声をダウンロードしてminimaxで音声を参照して作る方法が提案された（136, 139）
- **動画制作ツール**: 4時間超のAI動画作品がminimax製のツールで作られているという言及。声はminimaxではないという指摘もある（152, 159）

## muse

- **I2Vの顔変化問題**: museでI2Vすると顔の雰囲気が変わる。違和感なく生成する方法を求める声あり（137）

## strata

- **DeepSeek動作テスト**: strataでDeepSeekを動かしたが、テストでモデル名を聞くとClaudeと答えたという報告（236）

## dmd2（推論高速化ツール）

- **MOSSでの使用**: MOSSで8stepのdmd2をステップ数増やして強度調整して使用しており、高速化を使わずにステップや解像度をケチるより品質が向上しているという評価（114）

## その他ツール関連

- **codex**: codexのリセットが度々発生しており、使い切れないという声がある（72, 84, 89）
- **AI Studio**: AI Studioを使ってGeminiを利用しているという言及（100）
- **アヘ顔LoRA自作の課題**: プロンプトでアヘ顔を指定するのが難しく、自作LoRAを使うとアヘ顔にならないためキャプションを工夫する必要があるという指摘（170）