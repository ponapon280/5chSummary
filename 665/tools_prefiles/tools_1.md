**抽出されたツール関連話題**

**ComfyUI（および関連ノード・ワークフロー）**
- ComfyUIのキュー一覧表示後の消し方（右側の "0 active" をクリック）。
- ComfyUIアップデート後のノード互換性問題（INT8/ConvRotモデル読み込みに専用ノードが必要）。
- ComfyUI-INT8-Fastを使ったINT8化＋ネイティブ変換方式（Load Diffusion Modelで読み込み、速度向上）。
- ConvRot形式（comfyuiネイティブ対応のconvrotノード）による高速化とLoRA併用時の挙動。
- INT8 Pre-Lora Loaderの使用でLoRA適用時も速度を維持。
- Triton/Sage Attentionの導入（Windowsでのセットアップ難易度と効果）。
- 公式ComfyUIノード vs 野良ノードの移行問題（バージョンアップ後の互換性）。
- EasyWanワークフロー（古いComfyUI環境専用で現在非推奨）。
- DasiwaやSmoothmix作者のワークフロー推奨。
- MCP（Comfy公式β版）の活用例。

**選択理由として挙げられた点**
- 30xxシリーズ（特に3060 12GB）での生成速度向上（GGUF比で3倍以上高速、INT8で2.5s/itなど）。
- LoRA併用時の速度維持（dynamicモード推奨、Pre-Lora Loader使用）。
- 精度と速度のバランス（INT8でほぼ劣化なし、ただし一部LoRAで効きが悪くなる場合あり）。
- 公式対応の早さ（ConvRotのネイティブ対応で専用ノード不要に）。
- ワークフローの再現性・安定性（野良ノードより公式ノード推奨）。

**Forge系**
- Forge NeoのKrea2対応（最新情報として言及）。

**その他**
- 特筆すべきQwenシリーズの非画像生成話題はなし。

**## Web検索による参考情報**
- **ComfyUI-INT8-Fast / ConvRot**: ComfyUI向けのINT8量子化およびモデル変換手法。専用ノードやTritonカーネルを用いることで推論速度を向上させるプロジェクト/手法としてコミュニティで共有されている。
- **Triton / Sage Attention**: NVIDIA Tritonはカスタムカーネル最適化フレームワーク。Sage Attentionはメモリ効率の高いアテンション実装で、ComfyUIユーザー間でWindows環境への導入が議論されている。
- **EasyWan**: Wan系動画生成向けのAll-in-Oneワークフロー。古いComfyUIバージョンに依存するため、現在は非推奨とされることが多い。
- **Forge Neo**: Stable Diffusion WebUI Forgeの派生版。Krea2などの新モデル対応が追加されたとされる。