# 🆕 新規トピック（前回からの差分）
### 主な活用点
- ワークフロー: ref2v / I2I / Video reference（vhs loadvideo → images抽出） / ModelPreviewOverride / conditioning/sampling組み合わせ
- 環境: Portable版推奨、StabilityMatrixとの組み合わせ
- 更新頻度が高く、最新モデル対応や新機能が早く反映される

### StabilityMatrix
- ComfyUIのインストール・管理を自動化し、Sage AttentionやTriton導入を容易化
- 導入・更新の容易さ、特に初心者や複数環境管理に便利

### その他のツール
- Davinci Resolve: 動画マージ・編集で多機能（無料版でも十分）
- MiniMax H3 Rustランタイム版: CUDA不要（Vulkan/DirectX12/Metal対応）、低スペック向け
- 自作ツール: WebP/MP4大量同時再生・ファイル名表示による確認効率向上
- Easy ComfyUI: 「絶対入れるな」との警告あり

### 選ばれる全体的な傾向
- 運用性: 更新対応、インストール容易さ、低スペック最適化（SSD強化、キャッシュ活用など）
- コミュニティの活発さとKijaiなどの最適化ノードがComfyUI選択の要因

### Web検索による参考情報
- ComfyUI: 2026年8月時点でv0.31.0が最新安定版
- MiniMax H3: 2026年7月末リリースのマルチモーダル動画生成モデル（最大2K・15秒＋音声）
- Sage Attention (KJ Nodes): ComfyUI-KJNodesのPatch Sage Attentionノードが速度向上目的で導入
- Codex関連: AIエージェントからのComfyUI駆動（MCP統合）の議論あり

---
# 元の本文
**生成AI関連ツールレポート（ComfyUI中心）**

提供されたテキストから抽出された主な生成AI関連ツールは、**ComfyUI**（およびそのカスタムノード・ワークフロー）を中心に、インストール支援ツール、UI拡張、補助ツール、代替ランタイムなどが挙げられます。これらは主に動画生成（特にMiniMax H3向けref2v/I2Iワークフローや高速化）を目的としたローカル運用で議論されており、モデル性能自体は除外してツールの機能・運用面に焦点を当てています。

### 1. ComfyUI（本体・カスタムノード・ワークフロー）
ComfyUIはスレッドの中心ツールで、ノードベースの柔軟なワークフロー構築が特徴です。バージョン更新（例: 2.13.0+cu130、3.10.2+22コミット、最新コミット対応）が頻繁に言及され、SamplerCustomAdvancedエラー解消や新サンプラー（MiniMax-H3 Turbo Samplerなど）対応が確認されています。

**主な活用点**:
- カスタムノード: ComfyUI-MiniMax-H3-Cache / BlockCache (T8) / EasyCache / Spectrum / KJノード（Sage Attentionパッチ） / ComfyUI-MiniMax-H3-Turbo同梱サンプラーなど。
- ワークフロー: ref2v / I2I / Video reference（vhs loadvideo → get video component → images抽出） / ModelPreviewOverride / 参照画像・動画制御のためのconditioning/sampling組み合わせ。
- 起動オプション: `--use-sage-attention` / `--disable-pinned-memory` / `--lowvram`。
- 環境: Portable版推奨、StabilityMatrixとの組み合わせ。

**選ばれている主な理由**（テキストから抽出）:
- ノード単位の柔軟性が高く、参照画像/動画制御やキャッシュ/高速化ノードの自由な組み合わせが可能。
- 更新頻度が高く、最新モデル（MiniMax H3など）対応や新機能が早く反映される。
- 低〜中スペック環境（VRAM8-16GB/RAM32GBなど）向け設定（pinned memory無効化、キャッシュ系ノード）が細かく調整可能で、実用速度が出せる。
- コミュニティでのワークフロー共有・トラブルシューティングが活発（zuntanニキの「全部入りワークフロー」など）。

### 2. StabilityMatrix
ComfyUIのインストール・管理を自動化するツールで、Sage AttentionやTritonの導入も容易にします。Portable版との併用でバージョン更新時のトラブルを軽減。

**選ばれている理由**: 導入・更新の容易さ。特に初心者や複数環境管理に便利。

### 3. Codex（カスタムスマホWebUI）
ComfyUIベースで構築されたカスタムWebUIで、スマホからモデル/Loraダウンロード・生成・保存まで完結可能。「チャッピー（Codex）」経由で指示を出し、ComfyUIで自動生成させるアイデアも。

**選ばれている理由**: スマホUIが使いやすく、外出先からローカルマシンをほとんど触らずに生成・管理できる快適さ。

### 4. LM Studio
ローカルLLM実行ツールとして、MiniMax H3などの動画生成用プロンプト作成（システムプロンプト確認・編集、Gemma/Qwen系モデル使用）に活用。GPUオフロード設定でVRAM不足時も対応。

**選ばれている理由**: プロンプト生成用途の手軽さと、オフロードによる柔軟な動作。

### 5. その他のツール
- **Davinci Resolve**: 動画マージ・編集作業で「多機能で便利」と評価（無料版でも十分、有料版で追加機能）。
  - **選ばれている理由**: 強力な動画編集機能。
- **MiniMax H3 Rustランタイム版**: CUDA不要（Vulkan/DirectX12/Metal対応）、Python/PyTorch不要で低スペック向け。CPUメイン＋GPUオフロード。
  - **選ばれている理由**: CUDA環境不要でRadeonなどでも動作し、軽量実装。
- **自作ツール（動画確認・整理用）**: WebP/MP4大量同時再生・ファイル名表示機能。
  - **選ばれている理由**: 生成動画の確認・整理効率向上。
- **注意点のあるツール**: Easy ComfyUI（「絶対入れるな」との警告あり、SimpleComfyUIとの混同も）。

### 選ばれる全体的な傾向
- **柔軟性とカスタマイズ性**: ノード/ワークフローの組み合わせで参照制御や高速化（Sage Attention、BlockCache系、Turbo系）を追求。
- **運用性**: 更新対応、インストール容易さ、低スペック最適化（SSD強化、キャッシュ活用、PL設定70-80%など）。
- **利便性**: リモートUI（Codex）や補助ツール（LM Studio）によるワークフロー全体の効率化。
- コミュニティの活発さとKijaiなどの貢献者による最適化ノードが、ComfyUI選択の大きな要因となっています。

## Web検索による参考情報
- **ComfyUI**: 2026年8月時点でv0.31.0（2026年8月7日リリース）が最新安定版。新モデルサポートやUI/パフォーマンス改善が継続的に行われている。[[1]](https://docs.comfy.org/changelog)[[2]](https://github.com/comfy-org/comfyui)
- **MiniMax H3**: 2026年7月末にオープンウェイトでリリースされた汎用マルチモーダル動画生成モデル（テキスト・画像・動画・音声を統合コンテキストで扱い、最大2K解像度・15秒の動画＋ネイティブステレオ音声生成）。ComfyUIでのワークフロー対応が進んでいる。[[3]](https://www.minimax.io/blog/minimax-h3)[[4]](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- **Sage Attention (KJ Nodes)**: ComfyUI-KJNodesに含まれるPatch Sage Attentionノードが広く使われており、速度向上目的で導入。バージョン更新時の互換性問題が報告されるが、nightly更新で対応可能。[[5]](https://www.reddit.com/r/comfyui/comments/1p8xibn/sage_attention_flash_attention_for_latest_comfyui/)[[6]](https://github.com/kijai/ComfyUI-KJNodes/issues/390)
- **Codex関連**: ComfyUIをAIエージェント（Codex/Claudeなど）から駆動するMCP統合やカスタムUIの議論があり、スマホ/リモート生成の利便性が評価されている。[[7]](https://www.reddit.com/r/codex/comments/1t6wdm5/using_codex_to_drive_comfyui_server_fully/)[[8]](https://comfy.org/mcp/)

（注: モデル性能比較や生成結果の評価はテキストの指示に従い除外。事実確認は2026年8月時点の公開情報に基づく。）
