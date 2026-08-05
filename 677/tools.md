# 🆕 新規トピック（前回からの差分）
### 生成AI関連ツールレポート（ComfyUIエコシステム中心）
- ComfyUIおよび関連ツールの話題をまとめ、ツール選定理由を明記したレポート

### ツール: ComfyUI本体・環境構築・運用ツール
- ポータブル版ComfyUI
- 複数ユーザー推奨のDドライブ配置容易性と再セットアップ容易さ
- Stability Matrix
- WSL + git clone
- ポータブル版より安定管理可能な点で支持
- ComfyUI Manager
- Agent AI（Codex、Claude、Grokなど）の活用
- CUDAバージョン管理（cu130 / CUDA 13.0推奨）
- RTX環境でのOOM回避・生成安定化のためのCUDA 12.8から13.0へのアップグレード
- その他の運用Tips
- `--disable-pinned-memory`によるメモリ使用量大幅減
- シンボリックリンク使用時のLoRA-Managerキャッシュ問題解決策

### ツール: 高速化・最適化ツール
- SageAttention（+ Triton）
- EasyCache / Spectrum
- KJNodes（v1.4.8前後）
- pinned-memory

### ツール: その他のツール
- aria2c / hf download / irvine
- Runpod（クラウドGPU）
- Irodori-TTS
- AI-toolkit
- LoRA-Manager
- forgeNEO / easyWan / easyAnima
- Chrome拡張（自作）

### ツール: 選定理由の主な傾向
- 安定性優先：smzNode除外、SageAttention単体使用、CUDAバージョン指定
- 速度・効率：SageAttention/EasyCacheによる生成時間短縮、RAM活用、ポータブル版の管理容易さ
- 容易さ：Stability Matrix、Agent AI活用、aria2cのレジューム性

### ツール: ## Web検索による参考情報
- ComfyUI v0.30.0 / v0.30.1は2026年8月時点で最新リリース
- KJNodes（kijai/ComfyUI-KJNodes）はv1.4.9前後が最新
- SageAttention 2.2.0は公式提供されておりComfyUIとの組み合わせ例多数
- モデル名・新サービス関連の記述は検索対象外

---
# 元の本文
**生成AI関連ツールレポート（ComfyUIエコシステム中心）**

本レポートは、提供されたテキストから抽出されたComfyUIおよび関連ツールの話題をまとめ、ツール選定の理由（明記されている場合）を明記したものです。モデル名・性能比較・画像生成品質に関する記述はすべて除外しています。

### 1. ComfyUI本体・環境構築・運用ツール
- **ポータブル版ComfyUI**  
  複数ユーザーで推奨。Cドライブ圧迫を避け、Dドライブへの配置が容易な点が理由。新規環境構築時の再セットアップ容易さや移動のしやすさも評価。SageAttention導入時のエラー回避のため、ポータブル版から通常版へ移行するケースも報告。[[1]](https://github.com/comfy-org/ComfyUI/releases)[[2]](https://docs.comfy.org/changelog)

- **Stability Matrix**  
  「ComfyUI導入は結局Stability Matrixでいいのでは」との意見多数。環境分けやカスタムノード導入の簡単さが選定理由。

- **WSL + git clone**  
  ポータブル版より安定管理可能との理由で支持。

- **ComfyUI Manager**  
  カスタムノード管理に使用。ただし更新遅延の不満あり、手動最新版導入が必要になる場合がある。

- **Agent AI（Codex、Claude、Grokなど）の活用**  
  インストール・ワークフロー構築・カスタムノード導入をAIに任せる手法が複数言及。「自分で調べるより速い」「エージェントに環境構築を任せられるようになった」点が理由。

- **CUDAバージョン管理（cu130 / CUDA 13.0推奨）**  
  RTX環境でOOM回避・生成安定化のため、CUDA 12.8から13.0へのアップグレードが推奨。実際に安定化した報告あり。

- **その他の運用Tips**  
  - `--disable-pinned-memory`：メモリ使用量大幅減。ただし「ちょっと怖い」との声。
  - RAM積極活用：VRAMだけでなくRAM128GB積むのが普通になった（モデルがVRAMに収まらなくてもRAMで動く）。
  - シンボリックリンク使用時のトラブル（LoRA-Managerキャッシュ問題）解決策として特定フォルダ削除が挙げられる。

### 2. 高速化・最適化ツール
- **SageAttention（+ Triton）**  
  最も頻出の高速化ツール。生成速度向上（例: 3060環境で30s/it → 23s/it）が主な選定理由。Spectrum/EasyCache併用時に不安定化・音声劣化が発生しやすいため、**単体使用を推奨**する声多数。インストール時は`triton-windows` + 特定whlファイル、startup args（`--enable-triton-backend --use-sage-attention`）追加が必要。マネージャー経由ではなくGitHub直接導入を推奨する指摘あり。[[3]](https://github.com/thu-ml/sageattention)

- **EasyCache / Spectrum**  
  EasyCacheは`reusu_threshold 0.50`、`start_percent 0.30`、`end_percent 0.80`設定で1.43倍速を実現し、1.5倍速以内に抑えることで劣化を最小限に。Spectrumは複数キャラ・カメラワーク時に劣化目立ちやすい。併用時の競合で生成時間不安定になる事例あり。

- **KJNodes（v1.4.8前後）**  
  MiniMax用SageAttentionノード追加などで低スペック環境（VRAM16GB/RAM64GB）での安定性向上に寄与。バージョン管理が重要。[[4]](https://github.com/kijai/ComfyUI-KJNodes)

- **pinned-memory**  
  RAM→SSD漏れ防止のためデフォルトオンで使用。

### 3. カスタムノード・ワークフロー関連
- **smzNode**  
  A1111書式互換のために導入されるが、MiniMax H3などで動作阻害の原因となるため**uninstall/disable推奨**。安定性優先で外すケース多数。

- **KSampler (inspire)** など  
  ワークフローで使用例あり。

- **Load videoノード / ref_video_0接続**  
  get video component経由でimages取得して渡す必要があるなど、接続Tipsが言及。

- **ComfyUI公式ワークフロー**  
  シンプルさが評価され、カスタムノード大量必要だった過去からの改善点として挙げられる。

### 4. その他のツール
- **aria2c / hf download / irvine**  
  Hugging Faceからの大容量モデルDLで**aria2c（レジューム可能）**が最も推奨。直接DLの不安定さを解消する点が理由。

- **Runpod（クラウドGPU）**  
  ローカルGPU不足時の代替。電気代・故障リスクを他人に押し付けられるメリットが選定理由。ストレージ維持費に注意。

- **Irodori-TTS**  
  R2Vの参照音声として使用。GPU起動トラブル時はtorch再インストールで対応（v4対応）。

- **AI-toolkit**  
  LoRA作成ツールとして使用。デフォルト設定で学習可能。

- **LoRA-Manager**  
  checkpointハッシュ計算エラー発生時の対処が言及。

- **forgeNEO / easyWan / easyAnima**  
  ComfyUI移行時のハードルとして言及（ぬるま湯からの脱却）。

- **Chrome拡張（自作）**  
  データセット収集用（非公開）。

**選定理由の主な傾向**  
- **安定性優先**：smzNode除外、SageAttention単体使用、CUDAバージョン指定。
- **速度・効率**：SageAttention/EasyCacheによる生成時間短縮、RAM活用、ポータブル版の管理容易さ。
- **容易さ**：Stability Matrix、Agent AI活用、aria2cのレジューム性。

### ## Web検索による参考情報
- ComfyUI v0.30.0 / v0.30.1は2026年8月時点で最新リリースとして存在し、安定性・バグ修正が焦点。[[1]](https://github.com/comfy-org/ComfyUI/releases)[[2]](https://docs.comfy.org/changelog)
- KJNodes（kijai/ComfyUI-KJNodes）はv1.4.9前後が最新で、v1.4.8は実在のバージョン範囲内。[[4]](https://github.com/kijai/ComfyUI-KJNodes)
- SageAttention 2.2.0は公式に提供されており、ComfyUIとの組み合わせインストール例が多数確認される。[[3]](https://github.com/thu-ml/sageattention)

（モデル名・新サービス関連の記述はテキスト内に該当がなく、検索対象外としました。）
