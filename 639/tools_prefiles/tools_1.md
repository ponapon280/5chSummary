### 抽出された「ツール」関連話題

ログから生成AI関連の「ツール」（ComfyUI(comfy)、webUI、nano-bananaなど）に限定し、モデル（NAI、illustrious/リアス/ill/IL、FLUX、Wan、Qwen-Image、anima、Z-Image/ZIT/ZIE、LTXなど）に関する話題を除外して抽出。Qwenシリーズの画像生成以外は含むが、本ログでは該当なし。ツールの選定理由が明記されている場合を特に注記。

#### ComfyUI (comfy)
- **35**: Comufy（ComfyUIのタイポ）でモデルのフォルダパスが画像に保存される問題。配置場所によってはメタデータ漏れが発生し、アップ前に確認必須。
- **90**: スレに投げられた画像をComfyUIにぶち込んで確認。Anima Layer Replay Patcher（ComfyUIのカスタムノード？）で高速化でき、GitHub通りの設定を推奨（スレ民WFでエラー発生）。
- **103**: ComfyUI version: 0.19.3, comfy-aimdo version: 0.2.12, comfy-kitchen version: 0.2.8, ComfyUI frontend version: 1.42.11。生還報告（インストール成功）。
- **114**: ComfyUIのmodels/lorasパスがメタデータにフルパスで漏れる例（恥ずかしいパス名）。
- **136**: WF（Workflow）からのフルパス流出を防ぐためoutput/inputフォルダ固定だが、カスタムノードでフルパス仕様にされやすい。ロードノードに注意。
- **150**: CドライブにComfy入れるか？別ドライブ推奨。
- **154**: スタンドアロンアプリ限定で別ドライブ管理するも、ドライブ跨ぎで絶望。Cに余裕あれば全部Cが良い。
- **211**: ComfyUI 0.19.3, LLM導入見越してVRAM節約のためfp8版使用。質は落ちない。
- **理由関連**: 90で高速化（Anima Layer Replay Patcher）。211でVRAM節約（fp8版選定）。

#### WebUI / Forge系ツール
- **102**: forgeNEOでDynamicPromptのcombinatorial generationにチェックすると、ワイルドカードtxtファイルの内容が上から順ではなくランダム実行（例: 1red→5blackの順が21435になる）。前はeasyreforgeで順次実行。
- **104**: reforge（Reforge）の頃のDynamicPromptで順番生成は@などの特殊構文使用。batchが効くPrompts from file or textbox使用。今はComfyUI勢。
- **119**: SD.Nextのサンプリングステップ数などの初期設定保存場所不明。default項目なし、forgeと違うため設定保存不可。
- **理由関連**: 102でforgeNEOのDynamicPrompt挙動に困り（ランダム実行）、easyreforge時代と比較して不満。

#### その他の生成AIツール
- **27**: いつぞやのスクリプトがimgur使用（メタデータ関連の文脈）。
- **78**: civitai.redで使えるcivitai downloader（Firefoxアドオン）。右下ボタン、設定なし、Claude作成。rarファイル共有。**理由**: civitai.red専用。
- **92**: easy wan（Easy WAN?）同梱のWF活用継続（センシティブ部位検出モザイクWF、動画繋ぎWF）。現環境移植難。他人WF理解難しい。**理由**: 当時活用、現在もモザイク/動画繋ぎWFが有用。
- **181,184,212,213,219**: civitai/civitaired/redでソート「newest」出ない問題、PG以外フィルターでエラー、サイト全体問題発生。
- **Catbox (アップロードツール)**:
  - **9,63,64,65,66,67,70,84,94**: Catboxからお知らせ（AIエージェントによる大量アップロード問題、500GB超、35IP犯人、総ストレージ272TB、無制限プラン議論）。無料ユーザー容量制限/アカウント削除提案。**理由**: 善意WEBサービスがAIに潰されかねない（23）、大盤振る舞い（65）。

#### 補足
- WF（Workflow）は主にComfyUI文脈で登場（72,76,90,92,136）だが、ツール単体としてではなくComfyUIの機能の一部として扱い。
- 抽出外: クリスタ/MSペイント（一般画像編集）、Gemini/Grok/Claude（LLMチャット）、pixiv/civitai投稿規約議論（ツール非関連）。
- 全ログスキャン済み、重複/文脈的にツール非該当は除外。ツール選定理由は明示的な箇所のみ注記。