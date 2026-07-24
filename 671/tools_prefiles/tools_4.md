**抽出されたツール関連話題（モデル関連は除外）**

- **ComfyUI（comfy）関連**
  - kijaiのmega-flowプルリクエストの言及（ワークフロー/ノード関連の更新）。
  - ComfyUIのモデル対応状況（Mage-flowなどのツールがComfyUIに未対応または対応した直後の話題）。
  - workflowの使用（プロンプトノードの置き換え忘れ、Safetensors量子化ツールとの組み合わせ）。
  - comfy-kitchenの使用（silveroxides/convert_to_quantと併用した量子化）。

- **Fizgig関連**
  - Krea2でのLoRA学習ツールとして使用。VRAM 8GB環境でも学習可能にする機能（エラー検出、学習率自動調整、キャプション自動修正）。
  - 選択理由：低VRAM時のOOM回避と学習の安定性。教材画像1枚ごとの処理が特徴。

- **aitoolkit関連**
  - Krea2 LoRA学習での使用（VRAM 16GB環境でオフロード設定により1024解像度学習を可能に）。
  - 選択理由：text encoderとtransformerのオフロード比率調整でOOMを回避しやすい。

- **Musubi-tuner関連**
  - Krea2 LoRA学習ツールとして言及（VRAM 16GBでもOOMしやすい点が指摘）。

- **Mage-flow関連**
  - 新規ツールとして試用報告（T2I turboやedit turboでの動作確認）。
  - 選択理由・評価：全モデルを正しく動かせるかは微妙（特にturbo系で異常動作）。

- **Forge Neo関連**
  - negpip機能の言及（デフォルト版がanimaで効かない問題）。

**Qwenシリーズ（画像生成以外）**
- AlibabaのAI研究部門である点、中国語プロンプト対応の背景としての企業情報。
- 公式ページソースに「hentai」などのキーワードが含まれていた発見（非画像生成トピックとして）。

これら以外に、ツール名が明示的に挙がる話題は見当たりませんでした。