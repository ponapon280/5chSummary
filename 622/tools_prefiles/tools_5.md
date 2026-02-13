### 抽出された「ツール」に関する話題

ログ全体をスキャンし、ツール（ComfyUI/comfy, A1111/webUI関連, SUPIR/nano-banana類似の画像生成/編集ツール、kohya GUI/sd-scriptsなどの学習/生成支援ツール）に限定して抽出。モデル（NAI, Pony, リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）の話題は除外。ツール選定理由が明記されている場合のみ記載。

- **845**: 「yumeシリーズの作者とsd-scriptsのPR提出者が同一人物やんな有能すぐる」  
  → sd-scripts（LoRA学習スクリプトツール）のPR提出者を称賛。

- **854**: 「param guiの最新版触ってみたけどgrokと検証した結果追加の引数周り追記したら動くようになったわ」  
  → param gui（パラメータGUIツール）の最新版使用報告。grok（LLM）と検証して追加引数追記で動作。

- **878**: 「画像生成とかのワークフロー、できればUIベースじゃなくてコードベースで管理してAIに書かせたりモジュール化したりgit管理したいと思ってるんだけどやってる人いる？ 自前でゴリゴリ作るかComfyUIはありきでComfyScript経由するかかなぁって気がしてるけど良い感じの技術ないかな」  
  → ComfyUI / ComfyScript。**理由**: UIベースではなくコードベースでワークフロー管理、AI生成・モジュール化・git管理に適しているため検討。

- **886**: 「ワイめんどくさいからgoogle翻訳ノードに突っ込んでるんやけどやっぱLLMにやらせた方がええんやろか」  
  → google翻訳ノード（ComfyUI系ノード）。翻訳用途で使用中。

- **894**: 「ワイもComfyノード交錯民やで」  
  → ComfyUI（Comfyノード）。ノード交錯（複雑なワークフロー）ユーザー自称。

- **909**: 「>>872 ワイもこういう感じで書きがちだったからAIにコミットメッセージ書いてもらうようにした たまに大嘘書くからチェックは必要だけど」および「一昨日の2月11日にはneoブランチにマージされてたで」「neoでanimaのアプスケはhires fixだと必ず描写が変化してしまう」  
  → neo（A1111系WebUIのブランチ/フォーク）。Anima対応マージとhires fix使用報告。

- **912**: 「kohya GUIで絶対読め！はガチで読まないと詰むンゴねえ やっとanima学習始められたンゴ」  
  → kohya GUI。**理由**: anima学習開始に必須だが「絶対読め！」設定を読まないと詰む（動作不良）。

- **915**: 「ワイは翻訳はplamo2使ってる 国産で出来が良くてCPUで現実的な速度で動いて個人無料や」  
  → plamo2（翻訳ツール）。**理由**: 国産で出来が良く、CPUで現実的な速度、個人無料。

- **942**: 「neoでanimaのアプスケはhires fixだと必ず描写が変化してしまう (元画像) (hires) なので久しぶりにi2iでUltimate SD Upscaleを引っ張り出す (i2i 1.5倍)」  
  → neo（A1111系）, hires fix, i2i（img2img）, Ultimate SD Upscale。**理由**: neoのhires fixで描写変化する問題回避のためUltimate SD Upscale（i2i経由）使用。

- **950-951**: 「ComfyUIでA1111互換のメタデータでjpg保存したくてcomfyui-saveimagewithmetadata入れたら import failedとか出て使えなかったんでMetaHub Save imageいれたんだけど 画像生成時に日付のフォルダ作成してその中にファイル作らせたいときはfilename_prefixとfilename_patternにはどう記述すればええんや？」  
  → ComfyUI, comfyui-saveimagewithmetadata, MetaHub Save image。**理由**: A1111互換メタデータ保存と日付フォルダ自動作成のため導入・検証中（動作問題あり）。

SUPIRやnano-bananaなどの特定ツールはログに登場なし。他のLLMツール（LMstudio, ollama, translategemma, google翻訳など）は画像生成ツールの補助として一部関連するが、主眼の画像生成ツール（UI/ノード/学習ツール）に限定して抽出。