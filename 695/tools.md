# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUIの最適化・ノード関連ツール
- Block Sparse Attentionノード（Model Sparse Attentionに名称変更）とcomfy kitchen attention
- Comfy Compiler
- メモリ周りの最適化（CUDA allocation overhead削減）
- メモリ効率向上によるOOM対策と安定動作、--disable-comfy-compilerでの回避運用
- TRT VAE / Fast VAE
- VAE関連の高速化ノード（TRT VAEはFP16精度重視、Fast VAEは速度重視）
- 精度と速度の使い分け、int8convよりTRT VAEが総合的に有利
- その他のComfyUI運用ツール
- power lora loaderの代替やsubgraph回避の工夫
- カスタマイズ性・再現性・手軽さ（コピペ可能テンプレ）
- Sage attention起動オプションの機能破損リスク回避

### ツール: 3D生成ツール（ComfyUI native対応）
- Trellis.2 / Pixal3D
- ComfyUI native対応（公式ノード群）による形状・テクスチャ生成とMesh後処理統合
- カスタムノード不要の手軽さと公式テンプレ充実による導入ハードル低下

### ツール: 音声生成ツール
- Irodori-TTS（ComfyUIラッパー/ノード）
- 口パク合わせノード自作と出力ファイル名自動追加スクリプト
- ファイル管理利便性と口パク精度向上、v4.1系の読み込みエラー注意

### ツール: その他のツール・運用関連
- BlenderによるAI連携3Dモデル作成・プリビズ・カメラワーク制御とComfyUI組み合わせ
- TrainTrain / GUIによるLoRA学習の更新・管理
- Astraの5時間リミット厳格さとProプラン検討
- Codex（ChatGPT機能）のログ整理・コード生成とセキュリティ懸念
- 運用Tips（WSL活用、CrystalDiskInfoによるGPU監視、CapCut後処理）

### ツール: Web検索による参考情報
- Block Sparse Attention / Model Sparse AttentionノードのComfyUIコアマージ（2026年9月頃、PR #16072）と3モード選択
- comfy kitchen attentionのネイティブINT8注意力バックエンド実装と--use-ck-attention有効化
- Comfy Compilerのコアマージ（2026年9月頃）とCUDA graphsによるメモリ最適化
- Trellis.2 / Pixal3DのComfyUIコアnative統合（2026年8月22日頃、PR #14718）
- Irodori-TTSのComfyUI用ラッパー存在とv4.1系読み込みエラー報告
- 検索結果は2026年9月時点の公開情報に基づく

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出に基づく）**

ログから抽出された生成AI関連ツールは、主に**ComfyUI**エコシステムの最適化・拡張機能に集中しています。ComfyUIはカスタムノードの柔軟性が高く、LoRAの扱いやすさ、ワークフローの細かい制御、再現性の高さ（ワークフロー共有文化）、速度・VRAM効率のバランスが選ばれる主な理由として挙げられています。モデル名・バージョン関連の記述は除外し、ツール・ノード・運用面に焦点を当てています。

### 1. ComfyUIの最適化・ノード関連ツール
ComfyUIは複雑なワークフロー構築に強く、公式テンプレートの充実により最新技術のハードルが下がった点が評価されています。更新方法（マネージャー vs `update_comfyui.bat`）の違いも話題で、最新実験機能を使いたい場合に後者が推奨される傾向があります。

- **Block Sparse Attentionノード（Model Sparse Attentionに名称変更） / comfy kitchen attention**  
  公式実装のSparse Attentionノード（Block Sparse Attention）。Sol-Attn（adaptive tau）、top-k（SLA）、VSA（FastVideo）などの選択肢があり、Model Attention Backendと組み合わせる構成が一般的。comfy kitchen attentionはSageAttentionに匹敵する速度をネイティブで提供し、画質・速度で優位との報告多数。RTX 40/50シリーズユーザー向けに低VRAM安定性や背景一貫性向上の効果が期待される。  
  **選ばれている理由**: Sage/Solなどの非公式ノードから移行しやすく、速度・品質のトレードオフ調整が可能。低VRAM環境での安定性向上や背景変化抑制。comfy kitchen更新（v0.2.32以上推奨）で静止画モデルでもSageより僅かに速く、構図問題も改善された事例あり。[[1]](https://comfyui-wiki.com/en/news/2026-09-08-h3-sparse-attention-compiler)[[2]](https://comfyui-wiki.com/en/news/2026-08-11-comfyui-v0-32-0)

- **Comfy Compiler**  
  メモリ周りの最適化（CUDA allocation overhead削減）。  
  **選ばれている理由**: メモリ効率向上によりOOM（Out of Memory）対策や安定動作に寄与。--disable-comfy-compilerで一時的に問題回避する運用も見られる。[[1]](https://comfyui-wiki.com/en/news/2026-09-08-h3-sparse-attention-compiler)

- **TRT VAE / Fast VAE**  
  VAE関連の高速化ノード。TRT VAEは精度（FP16）が優位、Fast VAEは速度重視で生成サイズが大きいほど恩恵大。  
  **選ばれている理由**: 精度 vs 速度の使い分け。int8convよりTRT VAEの方が総合的に有利という意見。

- **その他のComfyUI運用ツール**  
  - impact pack（LoRAのtext入力扱いなどwebUI風機能）。  
  - ワークフロー共有文化（失敗例画像に埋め込み）。  
  - power lora loaderの代替やsubgraph回避の工夫。  
  **選ばれている理由**: カスタマイズ性・再現性・手軽さ（コピペ可能テンプレ）。

Sage attention起動オプションは一部機能破損（真っ黒画像など）のリスクで避けられるケースあり。

### 2. 3D生成ツール（ComfyUI native対応）
- **Trellis.2 / Pixal3D**  
  ComfyUIにnative対応（公式ノード群）。形状・テクスチャ生成、Mesh後処理などが統合。  
  **選ばれている理由**: カスタムノード不要で手軽に最新3D生成を試せる。公式テンプレ充実により導入ハードル低下。

### 3. 音声生成ツール
- **Irodori-TTS（ComfyUIラッパー/ノード）**  
  口パク合わせノード自作や、出力ファイル名にseed・リファレンス・セリフを自動追加するスクリプト活用。  
  **選ばれている理由**: ファイル管理の利便性向上、口パク精度向上。v4.1系は読み込みエラーの報告もあり、対応状況に注意。

### 4. その他のツール・運用関連
- **Blender**: AI連携による3Dモデル作成・プリビズ制作・カメラワーク制御。ComfyUIワークフローとの組み合わせで使用。
- **Forge Neo / webUI系**: ComfyUI移行検討の文脈で登場。LoRA remap機能などで一時的に利用。
- **TrainTrain / GUI（学習用）**: LoRA学習の更新・管理。
- **Astra**: 使用制限（5時間リミット）が厳しくProプラン検討の声あり（トークン消費の激しいタスクで注意）。
- **Codex（ChatGPT機能）**: ログ整理・コード生成に使うも、セキュリティ懸念で避ける声も。
- **運用Tips**: WSL活用、CrystalDiskInfoによるGPU監視、CapCutでの後処理など。

全体として、**ComfyUI**は速度・品質・VRAM効率・ワークフロー柔軟性のバランスで選ばれており、特にsparse attention系ノードの公式実装移行が目立つ動きです。ワークフロー共有や更新管理の文化が定着しています。

## Web検索による参考情報
- **Block Sparse Attention / Model Sparse Attentionノード**: ComfyUIコアに2026年9月頃マージ（PR #16072）。comfy-kitchenカーネルベースで、Sol-Attn（adaptive tau）、top-k（SLA）、VSAの3モードを選択可能。長シーケンス（例: MiniMax H3動画）で速度向上。comfy-kitchen v0.2.33以上推奨。[[1]](https://comfyui-wiki.com/en/news/2026-09-08-h3-sparse-attention-compiler)[[3]](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_sparse_attention.py)
- **comfy kitchen attention**: ComfyUI v0.32.0前後でネイティブ実装されたINT8注意力バックエンド。SageAttentionに匹敵する速度（一部ベンチマークで僅差または逆転）。起動引数 `--use-ck-attention` や ModelAttentionBackendノードで有効化。追加インストール不要の場合が多い。[[2]](https://comfyui-wiki.com/en/news/2026-08-11-comfyui-v0-32-0)[[4]](https://www.luomor.com/blog/2026/08/14/comfy-kitchen-attention%ef%bd%9ccomfyui-%e5%ae%98%e6%96%b9%e5%8e%9f%e7%94%9f-int8-%e6%b3%a8%e6%84%8f%e5%8a%9b%e5%8a%a0%e9%80%9f%e6%96%b9%e6%a1%88%e8%af%a6%e8%a7%a3/)
- **Comfy Compiler**: 2026年9月頃コアにマージ。メモリコンパイラ（aimdo）+ CUDA graphsでCUDA allocation overhead削減。MiniMax H3など長シーケンス向け。[[1]](https://comfyui-wiki.com/en/news/2026-09-08-h3-sparse-attention-compiler)
- **Trellis.2 / Pixal3D**: 2026年8月22日頃ComfyUIコアにnative統合（PR #14718）。カスタムノード不要で形状・テクスチャ・Mesh後処理が可能。Comfy-Org提供のbf16/INT8 ConvRot重み対応。[[5]](https://comfyui-wiki.com/en/news/2026-08-22-trellis2-pixal3d-native-comfyui)
- **Irodori-TTS**: ComfyUI用ラッパー（ComfyUI_IrodoriTTS_Wrapperなど）が存在。v4.1系は一部読み込みエラーの報告あり（v3まで安定対応の記述も）。音声クローニング・スタイル制御対応。[[6]](https://raw.githubusercontent.com/gazai-io/ComfyUI_IrodoriTTS_Wrapper/main/README.md)[[7]](https://aimtm.net/irodori-tts-anime-comfyui/)

（検索結果は2026年9月時点の公開情報に基づく。実際の動作は最新ビルド・環境により異なる可能性あり。）
