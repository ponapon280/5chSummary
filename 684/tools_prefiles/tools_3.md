**抽出された「ツール」関連話題（モデルは除外）**

### ComfyUI（comfy）関連
- **Sage Attention + Sol-Attn + AdaptiveCacheの併用**  
  公式wf比で3.4倍高速化（0.5MP 15s → 164s）。理由：生成速度を最優先。クオリティは若干低下する可能性あり。
- **Sage AttentionとSol-Attnの併用順序**  
  「Sage Attention → Sol-Attn」の順で繋がないとSol-Attnが無効化される。逆順だと逆に遅くなる報告あり。効果は出ている（893s→776s）。
- **Mem Eff Sage Attentionへの切り替え**  
  通常のPatch SageからMem Eff Sageに変えたら速くなった。
- **Spectrumへの切り替え**  
  Sage Attentionでエラーが出る環境でSpectrumに変更（動画品質改善に力を入れているため）。
- **kitchen（kijaiワークフロー）**  
  ComfyUIの高速化ノードとして言及。cuda最適化が入ったらSageと入れ替えたいという声。
- **ComfyUIをWebUI化**  
  「ComfyUIに側被せてWEBUIにしたほうが早い」という提案。
- **Context Loop（ContexLoop）**  
  動画生成の繋ぎ目が自然になるツール/手法として高評価。シーン毎に秒数調整可能で低予算アニメを超える品質が出せるため学習意欲が湧くという声。
- **Blockswap**  
  VRAM節約のために使用（20GB台で学習可能になった）。
- **musubi_tuner（dev版）**  
  Minimax H3のLoRA学習に使用。理由：ローカルで学習したい場合に必要。

### その他のツール
- **runpod**  
  5090環境で使用。ローカルより高速に出したい場合に選択。
- **Switchbot（スマートプラグ）**  
  リモートでPCの電源ON/OFF制御用。ComfyUI生成環境の運用ツールとして言及。

### Qwenシリーズ（画像生成以外）
- Qwen/Qwen3.8-27B、Qwen3.8 27B  
  Gemini3.5 Flashより高性能という評価で、LLMとしての性能について議論されている（画像生成用途は除外）。

**特に「選ばれている理由」が明記されているもの**
- ComfyUIの各種Attention高速化（Sage+Solなど）：**生成速度を最優先**するため。
- Spectrum：**動画品質改善**に力を入れているため。
- Context Loop：**繋ぎ目の自然さ**と**シーン調整の柔軟性**で高品質動画が作りやすいため。
- Mem Eff Sage：**単純に速くなった**ため。