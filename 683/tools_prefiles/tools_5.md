**ComfyUIに関する話題の抽出結果**

- **ComfyUIのアップデートによる挙動改善**  
  turbo（4step）使用時に発生していた雑音が、v0.31.0〜v0.32.0以降で大幅に減ったという報告。アップデートでバグが修正された可能性を指摘。

- **ComfyUIのH3対応アップデート**  
  ここ数日の更新でH3関連の対応が強化されていると指摘。H3動画生成時の安定性向上を期待する声あり。

- **runpod（Ubuntu） vs WindowsのComfyUI環境差**  
  Windows版では動画をドラッグ&ドロップするとワークフロー（WF）が出てくるのに、runpodの素のComfyUI（カスタムノードはmanagerのみ）ではWFが出ず動画アップロードノードになる違いについて議論。  
  → 原因として`pip install -r requirements.txt`未実施やフロントエンドパッケージ（comfyui-frontend-package）の違いが挙げられている。

- **ComfyUIのカスタムノード・ワークフロー関連**  
  - 縦UI対応のカスタムノード（AutoCompletePlus対応のもの）を利用している事例。
  - 高速化ノードの組み方や、WFをAIに渡してプロンプト作成を効率化する使い方。
  - コンテナ環境でのrequirements.txt適用や、Clean VRAMノードの挿入など、運用カスタマイズの話題。

- **ComfyUIのマルチGPU対応**  
  ComfyUIが正式にマルチGPU対応したことで、Radeon環境でも活用しやすくなったという指摘。

- **ComfyUIの環境依存性**  
  高速化ノードやLoRAの効果が「PCスペックとComfyUI環境の組み合わせ次第」で大きく変わるため、一律の最適解が出しにくいという意見。

これらはすべて**ツール（ComfyUI）**に関する話題で、モデル自体の性能議論は除外しています。