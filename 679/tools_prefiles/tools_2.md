**抽出されたツール関連話題（ComfyUI中心）**

- **ComfyUI（comfy）の更新・ノード/キャッシュ関連**  
  - comfy更新後に `comfyui-minimax-h3-blockcache-T8` がインポートエラーになる件。  
  - Cache系（easycache、MiniMax H3 Cache、MiniMax H3 Block Cache (T8)）を比較検証した結果、**MiniMax H3 Cacheがバランスと速度で一番良い**と評価。  
  - MiniMax H3 Cache使用時に `patch_model.py` を実行する必要がある点。  
  - 時短ノード（Turbo系含む）を直列接続せず、Kijaiの比較（Vs Sage）を参考に単品使用を検討。パラメータ調整の重要性も指摘。

- **ComfyUI + stabilitymatrixの組み合わせ**  
  - stabilitymatrix上でminimax-h3のref2vを動かした事例。参照画像枚数制限（デフォルト3枚→9枚まで増やす方法）の質問と解決（空きスロットに突っ込む）。

- **ComfyUIワークフロー・カスタムUI関連**  
  - zuntanニキの「全部入りワークフロー」を使いたいという要望。  
  - Codex（カスタムスマホWebUI）をComfyUIベースで構築し、**スマホからモデル/Loraダウンロード・生成・保存まで完結**できる利便性を高く評価。「Codexに丸投げ」「外出先からガンガン生成可能」との声。  
  - チャッピー（Codex）に指示を出してComfyUIで自動生成させるアイデア。

- **ツール選択の理由として抽出された点**  
  - **MiniMax H3 Cacheを選んだ理由**: 速度と画質のバランスが最も良い（他のCache系との比較結果）。  
  - **Codex（カスタムWebUI）を選んだ理由**: スマホUIが完璧で、場所を問わず生成・管理ができる。ローカルマシンをほとんど触らなくて済む快適さ。  
  - **ComfyUI全体の利点**: ノード/ワークフローの柔軟性が高く、高速化ノードやCacheを自由に組み合わせられる。Kijaiなどの貢献で最適化が進みやすい。  
  - Power Limit（PL）設定（70-80%推奨など）はComfyUIでの長時間生成時の発熱・電力・安定性を考慮した運用テクニックとして複数言及。

モデル（Wan、LTX、H3本体、Qwenなど）の性能比較・エロ向き議論は一切除外。Qwenシリーズの非画像生成話題も該当なし。