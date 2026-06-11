**抽出されたツール関連話題**

- **ComfyUI（comfy）**  
  複数回登場し、ワークフロー構築・ノード編集・動画生成の文脈で言及。  
  - 理由：RIFEフレーム補間ノードの差し替えやAsset表示の挙動確認、detailer再構築、TensorRTから公式ノードへの移行により処理速度が大幅向上（数十秒→十数秒）。公式テンプレートの更新も確認されており、効率化目的で使用。  
  - 具体例：frame_interporationノードのv4.26差し替え、Assetsメニューのtempフォルダ挙動、detailerノードの使い方、Couple機能の代替。

- **Kohya LoRA GUI / sd-scripts**  
  LoRA学習のメイン環境として言及。  
  - 理由：T-LoRA対応状況や階層マージの扱いやすさ、キャプション処理の安定性でsd-scriptsを優先。新しいAnima専用ツールは未検証のため現状維持。

- **RIFE VFI / frame_interporation（ComfyUIノード）**  
  動画フレーム補間ツールとして複数言及。  
  - 理由：v4.26モデル使用により補間速度が爆速化（例: 400秒→大幅短縮）。ComfyUI公式ノード＋TensorRT併用から公式RIFEノードへ移行し、DRAM消費・処理時間の改善を確認。

- **TensorBoard**  
  LoRA学習の進捗確認ツールとして推奨。  
  - 理由：Loss推移の可視化により収束判断が可能。グラフをLLMに投げて評価してもらう使い方が共有され、自動系LRの確認にも有効。

- **AIToolkit / AI-toolkit**  
  LoRA学習・キャプション生成に使用。  
  - 理由：エポックごとのサンプル画像出力機能が便利。layer offloadingのバグ修正により16GB環境でも動作確認。

- **RedrayzGUI**  
  LoRA学習支援ツールとして言及。  
  - 理由：画像付きの解説があり、TensorBoardのイメージがつかみやすい。

- **wandb**  
  TensorBoardの代替として推奨。  
  - 理由：ブラウザでほぼリアルタイム進捗確認＋過去データ蓄積が可能。

- **その他ツール**  
  - JSON Prompt Builder：プロンプト再利用・ワークフロー再現に使用。  
  - Detailerノード（SAM3含む）：顔・手などの補正用途。Animaでは使用頻度が低下傾向。  
  - LECO（erase）：特定要素の消去用。SDXLより純粋消去用途で効果が高い。  
  - MMAUDIO / Irodori-TTS：音声・環境音追加用途。

**モデル・バージョン・新サービスに関するWeb検索参考情報**  
（ツール抽出対象外のため参考程度に記載）

- **10eros**：RIFE系フレーム補間ワークフロー/モデル（v4.26.safetensors）。ComfyUIのframe_interporationノードで使用され、爆速補間が特徴。
- **Ideogram 4 / Ideogram4.0**：2025年頃に登場した画像生成サービス。構図制御・ロゴ挿入に強く、ComfyUIとの連携事例が増加。FP8/NVFP4での16-24GB動作報告あり。
- **Anima**：画像生成モデル（v1.1相当の更新履歴あり）。ツールとしての学習環境ではなくモデルとして扱う。

上記以外はツールとしての言及が主であり、モデル名は除外して抽出しています。