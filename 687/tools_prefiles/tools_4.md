**抽出結果**

以下のログから、**生成AIの「ツール」**（ComfyUI / webUI系インターフェース・ノード・ワークフローなど）に関する記述のみを抽出しました。モデル（NAI / anima / krea2など）に関する言及は除外しています。

### 該当箇所

- **714**  
  MiniMax公式がそのうち出すって言ってたSparse Attentionやけど、もう今のモデルに適応させるノードが出とるわ  
  **kitchen-attentionとblock cache組み合わせ**で、ワイの環境(5090 / 0.5MP / 20step / 10s)で120秒くらいやった。  
  **sage-attentionよりこっちの方が安定して速くてええわ**。

- **752**  
  >>714 をインストールして、**H3 SLA AttentionをLoRAローダーの後ろに配置**するのね  
  1割くらい早くなった。

- **826**  
  **comfyuiのブラウザの処理を内蔵GPUにしたら生成遅くなった**ンゴ

### 抽出されたツール関連のポイント

- **ComfyUI**でのカスタムノード利用（kitchen-attention + block cache）
  - 理由：**sage-attentionより安定性と速度で優位**（5090環境で120秒程度）
- **ComfyUI**ワークフロー内でのAttention系ノード配置（SLA AttentionをLoRAローダーの後に置く）
  - 理由：**生成速度が約10%向上**
- **ComfyUI**ブラウザ処理を内蔵GPUに割り当てた場合の挙動
  - 結果：生成が遅くなった（ネガティブな報告）

他にwebUIやnano-bananaなどの具体的なツール名・ワークフローの言及はありませんでした。