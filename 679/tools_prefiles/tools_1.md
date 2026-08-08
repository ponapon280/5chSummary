**抽出されたツール関連話題（ComfyUI中心）**

- **ComfyUIのバージョン管理・最新化**  
  最新版に更新するとanima生成が速くなった事例あり。ComfyUI・Python・PyTorch・CUDAは最新に保つのが必須と指摘。更新で予期せぬ改善が起きる可能性も言及。

- **ComfyUIワークフロー・ノード活用**  
  - MiniMaxH3向けワークフロー（RAM32GB+VRAM12GB環境向けリクエストあり）  
  - 高精度リファレンス画像作成のためのAnimaLoRA作り直し＋プロンプト作成LLMへの詳細マイルール設定＋キャラ付け記憶  
  - 動画参照（Video reference）ノード活用（vhs loadvideo → get video component → images抽出 → video渡し）  
  - ModelPreviewOverrideによるガチャ効率向上  
  - SageAttention / Sol-Attn / Block Cache / Easy Cache / H3 Block Cacheなどの高速化ノード組み合わせ  
  - KJノード版Sage Attentionへの切り替えでブラックアウト回避  
  - turbo4step + mem eff sage + sol-attn + sigma shift + block cacheの組み合わせで低VRAM環境（5060Ti）でも高速化

- **インストール・環境構築の工夫**  
  - StabilityMatrix使用でComfyUI＋Sage Attention＋Tritonを自動導入  
  - Portable版の推奨（特にバージョン更新時）  
  - runpodなどのクラウドGPUでのComfyUIテンプレート使用とエラー対処（clip loaderエラー時はGPU切り替えで解決）  
  - USB接続SSD→m.2 SSDへの変更で生成時間大幅短縮（転送速度20倍差の実測）

- **低スペック環境での運用**  
  - RAM32GBでも戦えるが厳しい、64GB以上推奨の声多数  
  - VRAM8GB/RAM16GBでも遅いが動作報告あり  
  - SSD強化が第一（nvme推奨）で、GPUより安上がり

- **その他のツール言及**  
  - nano-bananaなどの言及はなし  
  - Qwenシリーズの非画像生成話題はログ内に該当なし

**選ばれている主な理由（抽出されたもの）**
- ノード単位で細かくカスタム可能（参照画像制御、キャッシュ制御、音質改善など）
- 高速化ノードの組み合わせで低〜中スペック環境でも実用速度が出せる
- 最新化や特定ノード（SageAttention系）で体感速度・安定性が向上
- Portable版やStabilityMatrixで導入・更新が比較的容易
- ワークフロー共有・トラブルシューティングがコミュニティで活発

モデル名（anima, MiniMaxH3, Wan, LTXなど）の性能議論はすべて除外しています。