**抽出結果（ツール関連のみ）**

### ComfyUI関連の話題

- **公式Sparse Attentionノード**
  - 「公式のSparse Attentionノードがでとる 比べてみた感じ他のノードと同じくらい速度が出とるからもうこれでええな」
  - 理由：既存の非公式ノードと同等の速度が出るため、公式実装で十分と判断。

- **Comfy Compiler**
  - 「2日前にComfy CompilerとやらもマージされててMMH3とかでもメモリ周りの最適化されてるみたいだな」
  - 「--disable-comfy-compilerで一旦落ちるのを防止」

- **Block Sparse Attentionノード（comfy公式）**
  - Sol-Attn(adaptive tau)、top-k(SLA)、VSA(FastVideo)を選択できるセレクタが付いている。
  - 「comfyuiに実装されたBlock Sparse Attentionノードは...」
  - 理由：Sage/Solから乗り換え検討。VRAM12/16GB民向けに「Loader - ModelAttentionBackend(comfy kitchen attention)- Block Sparse Attention(top-k(SLA))- MiniMax H3 Chunk FeedForward - ModelSamplingMiniMaxH3」が鉄板とされる。

- **comfy kitchen**
  - 「sageもsolも消したな... Comfy kitchen attention」
  - 「comfy-kitchen更新しとる? version:0.2.32以上やないとたぶんあかんよ」
  - Sage/Solからcomfy kitchenへ移行する動きあり。

- **Spectrum / VDN**
  - 「結局VDN+ spectrumに落ち着いた」
  - SpectrumはTurboに近い位置づけで、ステップを端折るが劣化も伴う。

- **Trellis.2 / Pixal3D**
  - 「いつの間にかcomfyuiがTrellis.2とPixal3Dにnative対応してたぞ」

- **Irodori-TTS**
  - 「Irodori-TTS-v4.1-Anime これもだけどsmallもcomfyuiになぜ対応してくれないんだ」
  - ComfyUIでの読み込みエラーに関する言及あり。

### その他のツール

- **Astra**（使用制限・プラン関連）
  - 5時間リミットが厳しくなった、Proプラン検討、友達料で制限緩和などの話題多数。
  - トークン消費が激しいタスク（Blender操作、監督役など）で制限に引っかかりやすい。

- **Blender**
  - AIと連携して3Dモデル作成、プリビズ制作、カメラワーク制御に使用。
  - 「Blender触らせるの流行ってる」「Blenderでプリビズを作って動画AIに流し込む」

- **TrainTrain**
  - 「TrainTrainの更新や新しいLora学習手法の提案」

- **GUI（学習用）**
  - Anima Lora学習時の設定（dim/alpha、LR、CAMEなど）をGUIで管理。

### Qwenシリーズ関連（画像生成以外）
- Qwen 3 0.6B → Qwen 3.5 2Bへの置き換え検討（Anima開発者のコメント内）。
- 翻訳用途でQwen3 14Bを使用した事例あり。

**モデル名（Anima, MiniMax H3, NAIなど）の言及は除外**して上記のみ抽出しています。