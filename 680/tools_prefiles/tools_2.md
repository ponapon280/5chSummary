**抽出結果（ツール関連のみ）**

### ComfyUI（comfy）関連
- **ComfyUI本体の更新・管理**
  - Stability Matrix経由での更新が「Release」タグにしか対応していないため、最新版（v0.31.1など）に上げにくいという話題。Tagのコミットハッシュを直接指定する必要がある。
  - 理由：GitHubのRelease管理の都合で、最新機能をすぐに使えない。

- **ComfyUIのノード・拡張機能**
  - `comfyui-lmstudio-image-to-text-node`、`QwenVL`、`ComfyUI-llama-cpp_vlm` などのLLM呼び出しノード。
  - **選ばれている理由**：生成後にLLMモデルを自動でunload（VRAMから降ろす）できるため、VRAM16GB環境でも「プロンプト生成→画像/動画生成」を1回のワークフローで完結させやすい。
  - `ComfyUI-llama-cpp_vlm`を最終的に使っている人が複数。LM Studioを常駐させる必要がなく、ComfyUI単体で完結する点を評価。

- **メモリ/VRAM管理関連のツール・設定**
  - `--fast-disk`起動オプション（メモリ使用量を30GB削減）。
  - メモリ解放用batファイル + Stream Deck割り当て。
  - `--reserve-vram`オプション（0.6GB程度余裕を持たせる）。
  - **選ばれている理由**：VRAMギリギリ構成で安定して生成時間を短縮するため（特に`--disable-dynamic-vram`を外しただけで40%高速化した報告あり）。

- **その他のComfyUI関連**
  - `t8 blockcache`の動作確認（最新ComfyUIで動くようになった）。
  - w4a8（int4→int8変換）対応の話題。

### LLM関連ツール（画像生成以外）
- **ollama**
  - 放置するとVRAMから自動でモデルが降りる挙動を確認している。
- **llama.cpp**
  - ComfyUIから直接呼び出す用途で使用。
- **OpenRouter API**
  - ComfyUIに直繋ぎで使う選択肢として言及。
  - **理由**：サブスクより安く、プロンプト生成用途では十分という意見。

### その他
- Stability Matrix（ComfyUIのバージョン管理ツールとして登場）。

**除外したもの**
- H3 / MiniMax H3、lightx2v、sage attention、sol-attn、Spectrumなどのモデル・LoRA・最適化手法。
- Wan、LTX、Z-Image、FLUX、animaなどのモデル名。
- 純粋なモデル精度比較（int8 vs pruned bf16など）。

以上がログから抽出できた「ツール」に関する話題です。