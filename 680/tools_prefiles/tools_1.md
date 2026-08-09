**抽出されたツール関連の話題（ComfyUI / A1111 / その他ツールのみ）**

### ComfyUI関連
- **インストール方法の選択肢が多い問題**  
  「ComfyUIのインストール方法がたくさんあってどれがいいのかわからない」という質問に対し、特定のガイド（>>1のWiki内リンク）を参照するよう案内されている。

- **バージョンアップの影響**  
  - 0.30.2 → 0.31.0に上げたことで「kijai 4step loraが本当に4stepで動くようになった」「音質もかなり改善」。
  - 0.31.0にしたことでT8 Cacheが動かなくなった事例あり。
  - 0.31.0にしたことでanimaの生成速度が向上（2回目以降のキャッシュ効果で27秒→16秒）した報告。
  - 0.3.10.0にしたら「comple model +」が壊れた事例あり。

- **ワークフロー・ノード関連の話題**
  - ComfyUI-LoRA-Block-Filter（animaでLBWするノード）のプリセット情報。
  - LoRAローダーの接続方法（モデルローダー → LoRAローダー → sage attentionノード）。
  - rgthreeのpower LoRA Loaderの使い勝手が良いという言及。
  - Load LoRAノードの追加方法。
  - Civitai連携ツールとして「LoRA Manager」「power lora loader」の言及（トリガーワード取得など）。

- **高速化ノード・パッチの組み合わせ**
  - Patch Sage Attention KJ / Patch Sol-Attn / MiniMax H3 Block Cache (T8) などの組み合わせを試している報告多数。
  - 「H3 Block Cache(T8) + Patch Sol-Attn + Patch Sage Attention KJ」の組み合わせで速度向上を確認した事例。
  - Mem Eff Sage Attention Patchを追加するとエラーになるケースあり（CUDA相性問題の指摘）。

- **その他のComfyUITips**
  - minimaxのVAEをint8に変えると処理時間が短縮（特にミドルスペック環境で推奨）。
  - StabilityMatrixは小数点じゃないバージョンアップだけ拾う挙動。

### A1111 (Automatic1111 webUI) 関連
- **生成速度の低下問題**  
  「久々にA1111使ったら生成がクソ遅い」という報告に対し、「旧Lycorisの拡張機能を消せ」という解決策が提示されている。

### その他ツール関連
- **EasyWan22**  
  「EasyWan22ってどう？」という質問に対し、「推奨しない。メンテされなくなってしばらく経ち、現在はインストールに失敗する」と明確に非推奨とされている（理由：メンテナンス停止によるインストール失敗）。

- **StabilityMatrix**  
  バージョン管理ツールとして言及（0.31系統の挙動について）。

### 抽出されなかったもの
- モデル名（MiniMax H3、anima、NovelAIなど）の単独言及
- グラボ（5090など）やメモリ容量の話
- プロンプトやLoRA自体の性能話

**選ばれている理由として明記されていた点**
- ComfyUI：ワークフローの柔軟性・ノードの組み合わせによる高速化が可能。
- power LoRA Loader / LoRA Manager：Civitaiからの情報取得が容易。
- EasyWan22：メンテ停止により現在は使えないため非推奨。