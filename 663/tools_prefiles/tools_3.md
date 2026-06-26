**抽出結果**

- **ComfyUI**（複数言及）
  - 更新後にCLIPNegPipノードが使えなくなり、エラーになる問題が発生。Negpipの更新が必要。
  - 本体側のVRAM管理が改善されており、生成時のボトルネックが減った点が評価されている。
  - マルチGPU環境でのCUDA_VISIBLE_DEVICES指定などのコマンドライン設定が必要になるケースあり。

- **musubi-tuner**（LoRA学習ツール）
  - Krea2のLoRA作成に使用。VRAM16GB環境向けに`--blocks_to_swap 25`などの省メモリ設定を組み合わせ、1024解像度で2000ステップを9時間程度で回す事例あり。
  - 省メモリオプション（gradient_checkpointing、block_swap関連フラグ）の調整が活発に議論されている。

- **ai-toolkit**
  - Krea2のLoRA学習に利用。raw版ベースで学習を開始し、VRAM24GB前後で3000stepsを3時間弱で処理する報告あり。

**理由の抽出ポイント**
- ComfyUIは「VRAM管理の改善」と「ノード互換性の問題」が主な話題。
- musubi-tuner / ai-toolkitは「VRAM16〜24GBの低〜中スペック環境でもLoRA学習が可能」という実用性が評価されている。

該当するツール話題は上記のみ。モデル（Krea2、Anima、ZITなど）に関する言及は除外した。

## Web検索による参考情報
該当なし（ログ内に新規サービス・バージョン・モデル名に関する確認対象なし）