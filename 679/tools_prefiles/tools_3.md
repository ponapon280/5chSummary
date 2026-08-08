**抽出結果（ツール関連のみ）**

### ComfyUI（Comfy / ComfyUI関連）
- **言及多数**（ほぼスレの中心ツール）
  - デスクトップ版（3.10.2+22コミット）を使っている事例
  - 最新コミットへの更新でSamplerCustomAdvancedのエラー解消や新機能（KSamplerSelectのeuler、MiniMax-H3 Turbo Sampler）対応
  - カスタムノードの活用（ComfyUI-MiniMax-H3-Turbo同梱サンプラー、MiniMaxH3DualClockSampler、KJノード、BlockCache、Spectrum、EasyCache、sage attentionパッチ）
  - 高速化ノードの組み合わせ検証（Patch Sage Attention、BlockCache T8、Spectrum、H3Cacheなど）
  - 起動オプション（--use-sage-attention、--disable-pinned-memory、--lowvram）
  - ポートable版 vs 通常版の難易度比較
  - Easy ComfyUIの導入事例

**選ばれている理由（明記されているもの）**
- ノードの柔軟性が高く、MiniMax H3などの最新モデル対応が早い
- 各種高速化ノード（sage attention、BlockCache、Spectrumなど）を組み合わせやすい
- 更新頻度が高く、最新のサンプラーや最適化がすぐ反映される
- 低スペック向け設定（pinned memory無効化など）が細かく調整可能

### Davinci Resolve
- マージ作業で「多機能で便利」と評価
- 無料版でも十分使えるが、操作習得の難しさが指摘されている
- 有料版だと60p出力などの追加機能あり

**選ばれている理由**
- 動画のマージ・編集機能が強力

### MiniMax H3 専用ツール / ランタイム
- **Rustランタイム版**（CUDA不要、Vulkan/DirectX12/Metal対応）
  - no Python / no PyTorch / no CUDA toolkit / no ffmpeg
  - CPUメインで動作しつつ、GPUオフロード可能（VRAM14GB要求）
  - 低スペック民でも満足に使える可能性が指摘されている

**選ばれている理由**
- CUDA環境不要で動作する点（Radeonでも動作確認事例あり）
- 低スペック向けの軽量実装

### その他ツール
- **LM Studio**：システムプロンプト（シスプロ）の確認・編集に使用
- **Easy ComfyUI**：導入のしやすさから新規参入者に推奨されるケースあり

**モデル関連（anima, Wan, LTX, FLUXなど）は一切抽出していません。**  
Qwenシリーズの言及も該当なしでした。