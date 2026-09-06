# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI および関連カスタムノード・機能
- ComfyUI Desktop v0.34.3と公式テンプレート・カスタムノードマネージャー
- 高速化ノード群と`--fast-disk --disable-pinned-memory`オプションの併用例
- 初心者向け公式テンプレートからの段階的スケールアップとminimax公式プロンプト変換ノード追加
- ComfyUI-VDN-H3（Video Delta Net関連カスタムノード）
- VDN-H3による画質・プロンプト追従性向上と速度特性
- ComfyUI NVIDIA PAIRノード / 関連システム
- 複数マシン分散処理ツール（生成時自動選択・キュー投入）
- 複数PC空きリソース自動活用のための分散処理
- Zironic/H3-Optimizations（Minimax H3向け）
- その他のComfyUI関連
- ImpactWildcardProcessorの複数抽出挙動対策とサブフォルダ指定
- Regional Prompt系ノードの自作事例
- ComfyUI native版 SeedVR2（更新停止版代替）
- Comfy CompilerのH3生成時異常終了バグ
- Mac（M5 Ultra）環境での動作とCUDA依存ノードによる移行難
- カスタムノード全般のOSS性とClaude/Codex移植可能性

### ツール: その他のツール・環境
- sd-scripts + GUIツール
- GUI非対応機能のためのsd-scripts直接編集とdataset.toml手法
- GUI経由の設定しやすさ（初心者〜中級者向け）
- Animerge（更新版）
- LoRA学習対応プリセット読み込みツールとBase1.0 3.8B版疑似コンバート
- liquidmix
- Anima3.8B向け設定（Qwen3対応調整済み）
- Animaモデル相性とQwenシリーズ動作カスタマイズ
- Minimax H3公式skillsによるプロンプト作成自動化
- 公式マニュアル準拠プロンプト作成の簡易化
- Qwenシリーズ（非画像生成用途）
- サーバー障害時の信頼性とローカル/代替LLMとしての安定性
- クラウド障害時の安定性

### ツール: 共通の傾向と注意点
- 選ばれにくい理由（ノード知識必要、低スペック不安定、編集時間長）
- ComfyUIのOSSカスタムノード豊富さとWanGP回避策

### ツール: Web検索による参考情報
- ComfyUI v0.34.3リリース情報とDesktop版機能
- NVIDIA PAIRのベータ公開と分散処理機能
- AnimergeのGUIツール概要と対応機能
- liquidmixのAnima 3.8B向け実験的派生
- QwenシリーズのLLM群とローカル利用安定性
- 検索結果の2026年9月時点情報

---
# 元の本文
**生成AI関連ツールレポート（抽出テキストに基づく）**

抽出されたテキストから、生成AI（主に画像・動画生成および関連ワークフロー）で言及されたツールは、**ComfyUIエコシステム**を中心にカスタムノードや最適化ツールが多くを占めています。モデル名（Anima、Minimax H3、Wan、NAIなど）は除外し、ツール・環境・ワークフロー関連のみに焦点を当てています。ツールが選ばれる理由が明記されている場合は明記し、ComfyUIの柔軟性・カスタマイズ性・リソース最適化が共通のテーマとなっています。

### 1. ComfyUI および関連カスタムノード・機能
ComfyUIは最も頻出するツールで、ノードベースのワークフロー編集、複数モデル対応、カスタムノードの拡張性が強みとして挙げられています。

- **ComfyUI Desktop v0.34.3**（および公式テンプレート・カスタムノードマネージャー）  
  高速化ノード（Turbo mode、ModelAttentionBackend、Spectrum Apply MiniMax H3、Patch Sol-Attnなど）と組み合わせた運用例あり。`--fast-disk --disable-pinned-memory`オプションとの併用も言及。  
  **選ばれる理由**: 初心者向け公式テンプレートから始めやすく、解像度・モデルサイズを段階的に上げられる。更新でminimax公式プロンプト変換ノード（有料、有料版はエロプロンプト弾き）が追加され、公式サポートが強化された点。

- **ComfyUI-VDN-H3**（Video Delta Net関連カスタムノード）  
  画質とプロンプト追従性が大幅向上するが、8step Turbo LoRAより遅く、高速化を盛った20step程度の速度。最適化の余地あり。  
  **選ばれる理由**: 画質・追従性を優先する場合に有効。低VRAM環境ではOpenVDNの最適化不足でOOMが発生しやすく、回避策が必要（生成時間がturboの10倍近くかかるケースも）。

- **ComfyUI NVIDIA PAIRノード / 関連システム**  
  家中の複数マシンにComfyUIを配置し、生成ボタン押下時に空きマシンが自動選択・キュー投入される分散処理ツール。  
  **選ばれる理由**: 複数PCの空きリソースを自動活用したい場合に有効（高速化ではなく分散処理目的）。

- **Zironic/H3-Optimizations（Minimax H3向け）**  
  モデルのロード制限・メモリ最適化・SparseAttentionによりVRAMを約5GB節約可能。  
  **選ばれる理由**: VRAM節約を最優先する場合に推奨（多少の劣化を許容すればワンランク上の生成が可能）。

- **その他のComfyUI関連**  
  - ImpactWildcardProcessor: `{2$$__hogehoge__}`形式の複数抽出時の挙動対策やサブフォルダ指定が必要。  
  - Regional Prompt系ノード: 既存ノードと挙動が異なるため自作事例あり。  
  - ComfyUI native版 SeedVR2: 更新停止版の代替として推奨。  
  - Comfy Compiler機能: master版でH3生成時に異常終了するバグ報告あり。  
  - Mac（M5 Ultra）環境: 動作するがCUDA依存カスタムノードが多いためWindowsからの移行は難しい。  
  - ワークフロー柔軟性: 1つのWFで複数モデルを扱え（1段目モデル＋i2i）、複数プロンプト対応しやすい点が強み。初心者には3060+32GB環境で公式テンプレート推奨。  
  - カスタムノード全般: すべてOSSで、Claude/Codexによる移植可能。

**全体の選ばれにくい/選ばれる理由の傾向**: ノード編集の時間コストが高く（生成より「フロー弄ってる」時間が長い）、低VRAM（8GB）でOOMが発生しやすいため実用性が低いとの不満。一方、カスタムノードの急速な実装（DLSS5、VDNノード、Regional Promptなど）や柔軟性が支持される。

### 2. その他のツール・環境
- **sd-scripts + GUIツール**  
  GUIにない機能（timestep sampling offsetなど）を使うためにsd-scripts直接編集を推奨。dataset.toml作成＋コマンド生成後の`--dataset_config`書き換え手法が共有。  
  **選ばれる理由**: sd-scriptsを直接触るよりGUI経由の方が設定しやすく、初心者〜中級者向けにハードルが低い。

- **Animerge（更新版）**  
  LoRA学習のみ対応のプリセット読み込みツール。Base1.0プリセットの3.8B版疑似コンバート機能あり。LoRA・LECO・ADDifT・マージ・timestep対応予定。  
  **選ばれる理由**: 既存マージ・学習ワークフローを拡張しやすく、将来的なtimestep/スーパーマージ対応で柔軟性が高い。

- **liquidmix**  
  Anima3.8B向け設定（Qwen3 0.6B / Qwen3.5 4B対応調整済み）。  
  **選ばれる理由**: Animaモデルとの相性が良く、Qwenシリーズでも動作するようカスタマイズされている。

- **LM Studio + skillsプラグイン**  
  Minimax H3公式skillsを読み込ませてプロンプト作成を自動化（「use $h3-prompt-writing skill」と記述するだけ）。  
  **選ばれる理由**: 公式マニュアル通りのプロンプトを楽に作りたい場合に便利。

- **Qwenシリーズ（非画像生成用途）**  
  サーバー障害時（OpenAI/Claude/Grok大規模障害時）の信頼性が高く、ローカル/代替LLMとして安定。コーディング用途（エロアプリ開発など）でも言及。  
  **選ばれる理由**: クラウド大手が落ちても動作する安定性。

### 3. 共通の傾向と注意点
- **選ばれる主な理由**: リソース最適化（VRAM節約・分散処理）、ワークフロー柔軟性、GUIによる操作性向上、公式/コミュニティノードの急速な拡張。
- **選ばれにくい理由**: ノード知識の必要性、低スペック環境での不安定さ、編集時間の長さ。
- ComfyUIはOSSカスタムノードの豊富さが最大の特徴で、WanGP（ノード知識不要）をComfyUI回避策として選ぶ事例も。

---

## Web検索による参考情報
- **ComfyUI v0.34.3**: 2026年9月2日リリース。Minimax-H3関連機能（H3 Maxオプション追加、Partner Nodes更新）を含む。Desktop版は複数インスタンス管理機能があり、Windows対応。[[1]](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.34.3)[[2]](https://docs.comfy.org/installation/desktop/windows)
- **ComfyUI-VDN-H3**: MiniMax-H3向けVideo Delta Netハイブリッドアテンションノード（Saganaki22氏提供）。公式VDNをComfyUIネイティブで再現し、線形コストの再帰状態で長尺動画の効率化を図る。v1.4.0でストリーミング最適化・VRAM考慮バッファ追加（RTX 5090で約15%高速化例）。Apache 2.0ベースの移植。[[3]](https://raw.githubusercontent.com/Saganaki22/ComfyUI-VDN-H3/main/README.md)[[4]](https://github.com/Saganaki22/ComfyUI-VDN-H3/releases/tag/v1.4.0)
- **NVIDIA PAIR（Personal AI Router）**: 2026年9月頃ベータ公開のNVIDIA公式ツール。ローカルネットワーク上の複数PC（RTX 20シリーズ以降、M4+ Mac対応）の推論リクエストを自動ルーティング。Ollama/LM Studio対応で、ComfyUI関連の分散処理記述と一致する機能。[[5]](https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/)[[6]](https://www.cnet.com/tech/services-and-software/nvidia-pair-speeds-ai-agents-by-annexing-pcs-on-your-network/)
- **Animerge**: Animaモデル向けGUIツール（iron-mukakin氏）。マージ、LoRA/LECO学習、分析機能を提供。Anima Base 1.0および3.8B v1.0/v1.1対応。kohya-ss/sd-scripts統合。[[7]](https://raw.githubusercontent.com/iron-mukakin/Animerge/main/README.md)
- **liquidmix**: Anima 3.8B向け実験的派生（Qwen 0.6B/3.5 4B対応のデュアルコンディショニング）。Animaエコシステム内の拡張機能として言及。[[8]](https://civitai.com/models/2488393/anima-38bliquidmix-anima-29b-anima)
- **Qwenシリーズ**: AlibabaのLLM群。2026年時点でQwen3.8が最新世代の一つとして言及され、ローカル利用の安定性が評価される文脈と一致。[[9]](https://ru.wikipedia.org/wiki/Qwen)

（検索結果は2026年9月時点の公開情報に基づく。ニッチなコミュニティツールの一部は公式情報が限定的。）
