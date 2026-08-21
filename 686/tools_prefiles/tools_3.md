**抽出された「ツール」関連話題（モデル関連は除外）**

### 1. ComfyUI（comfy / comfyui）
- **言及内容**:
  - comfyuiを最新版に更新しただけで、anima生成が1枚36秒→22秒に高速化（>>485）。
  - SageAttentionエラー多発時にワークフローが壊れ、再インストールを検討（>>606, >>614）。
  - comfy-kitchenAttentionへの移行を検討（SageAttention2の進化停滞を理由に）（>>586）。
- **選ばれている理由・評価**:
  - 更新による明確な速度向上（「かがくのちからってすげー!」）。
  - ワークフロー作成・管理の柔軟性が高いが、エラー時の復旧が面倒な点も指摘。

### 2. Attention系カスタムノード / 最適化ツール
- **言及内容**:
  - Sol-Attn（h3専用）、Sage Attention（KJ版 / Saganaki22版 / Patch Sage Attention KJ）。
  - comfy-kitchenAttention（SageAttentionの代替として言及）。
  - MiniMax H3 Low VRAM Attention / Chunk FeedFoward などの組み合わせ（>>543）。
- **選ばれている理由・評価**:
  - ロースペック環境（4060Tiなど）で速度を優先する場合にSaganaki22版Sol-Attnが有効（>>542）。
  - comfy-kitchenAttentionは将来的なComfyUIの進化を期待しての選択（>>586）。

### 3. 動画編集・モザイク処理ツール
- **言及内容**:
  - **DaVinci Resolve**: レンダリング時の暗転問題、GPU（CUDA）設定で解決した事例（>>484, >>487, >>490）。UIの複雑さが不満点として複数言及。
  - **代替ツール**:
    - YMM4：UIが優しく、クリック操作中心でモザイク処理に適する（>>534）。
    - Aviutl：UI整備が面倒だが機能性が高い（>>534）。
    - Kdenlive：使いやすいがモザイクサイズ調整に制限あり（>>536, >>599）。
- **選ばれている理由・評価**:
  - DaVinci Resolveは高機能だがUIが「めんどくさすぎる」ため、モザイク目的ならYMM4や有料ツールを推奨する声あり。
  - 手動モザイク用途では「クリックだけで一通り揃う」簡易性が重視されている。

### 補足
- 上記以外に、Gemini / ChatGPT / Claude（cloude） / CodexはComfyUIのワークフロー作成やエラー解決の補助ツールとして複数登場しているが、生成AI本体というより「補助ツール」としての文脈が強いため、必要に応じて参考程度に留めました。
- モデル名（Wan, anima, H3, MiniMaxなど）やハードウェア（5090など）の話題はすべて除外しています。