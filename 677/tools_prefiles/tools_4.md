**抽出結果（ツール関連のみ）**

### ComfyUI関連
- **CUDAバージョン指定**：RTX使用時に「CUDAをComfyUI推奨の13.xにしろ」との指摘多数。CUDA12.8だとOOMになりやすいため、cu130（CUDA 13.0）へのアップグレードが推奨されている。
  - 理由：OOM回避と生成の安定性。実際にcu130に上げた結果、生成が安定したとの報告あり。
- **環境構築・管理**：
  - **ポータブル版ComfyUI**を推奨する声多数。「新しく環境作り直すのが一番簡単」との意見。
  - 画像生成用と動画生成用でComfyUIを分ける運用（smzNodesの影響を避けるため）。
- **カスタムノード関連**：
  - `smzNodes`はuninstall（またはdisable）推奨。入れたままにするとエラーの原因になる。
  - SageAttention + Tritonの導入で大幅に高速化（特にMiniMax系）。
  - その他：KJNodes、Nvidia_RTX_Nodes_ComfyUI、cmdノードの出し入れでエラーが解消した事例あり。
- **WSL2環境**：CUDA12.8から13.0へ手動アップグレードした報告。CopilotではなくGoogle検索で正しい手順を確認した例あり。

### ダウンロード・インストールツール
- **Hugging Faceからの大容量モデルDL**：
  - `aria2c`（スクリプト使用）が最も推奨。レジューム可能で中断しやすい。
  - `hf download`コマンド（huggingface_hub）で高速DLできた報告。
  - `irvine`もまだ使えるとの言及。
  - 理由：数十GBクラスのファイルで直接DLが不安定なため、レジューム性と速度を重視。

### その他のツール
- **Stability Matrix**：ComfyUIの管理に使用している人が複数。
- **irodori-TTS**：GPU動作に関するトラブルシュート（起動引数やcu128指定など）。
- **SageAttention / Triton**：ComfyUIの高速化ツールとして頻出。CUDAバージョンに合わせたインストールが重要と指摘。

### ツール選択の理由として明記されていた点
- **ComfyUI（特にcu130環境）**：生成速度とメモリ効率の向上。古いCUDAだとOOMや不安定になるため。
- **ポータブルComfyUI**：環境の壊れにくさ・移動のしやすさ・再構築の容易さ。
- **aria2c**：大容量ファイルのDLでレジュームできる点が最大の利点。
- **SageAttention**：生成速度が明らかに向上（倍近く速くなった事例あり）。

モデル（MiniMax H3、Anima、Wan、FLUX、LTXなど）に関する記述はすべて除外しています。