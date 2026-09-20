# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI（および関連カスタムノード・拡張）
- ドラッグ&ドロップ時のタブフリーズ対策（Chrome設定変更、Firefox推奨）
- 標準VFI Frame Interpolationによる高速フレーム補間（RIFE TensorRT不要）
- 更新・CUDA差による生成再現性の問題
- NegPiP代替として「Krea2 Prompt Weight」推奨
- 大規模Workflow対策としてのJSON出力ノード活用
- comfy_kitchen_attention等による速度向上
- ROCm（AMD GPU）対応のインストール・運用
- Comfy Desktop安定版のテンプレート同梱・更新管理
- ノードベースの柔軟制御・手動作業削減・LLM連携効率化・速度オプション豊富さ

### ツール: RefMOD（RefMods / context loop ref2v 関連）
- MiniMax H3向け参照画像/動画をsafetensors化するツール（ComfyUI連携）
- 参照画像による動画LoRA相当の一貫性実現とRef2VA安定生成
- 誰でも簡易にキャラクター一貫性を実現（Token管理注意）

### ツール: AI-Toolkit（ostris/ai-toolkit）
- 拡散モデル向けLoRA学習ツールキット（YAML/Web UI対応）
- 16GB VRAM環境でのLoRA学習（3000step、数時間）
- GUIの使いやすさ・簡易設定（musubi-tunerベースの信頼性）

### ツール: その他のツール
- VFI Frame Interpolation（TensorRT不要の高速フレーム補完）
- Codexによるカスタムノード自動生成（手作業削減）
- Comfy-KitchenのROCm最適化による速度向上
- コンテナ/Dockerによる環境分離・セキュリティ対策
- Unsloth Desktopによるサンドボックス対策
- jevの自社/個人システム組み込み検討

### ツール: Web検索による参考情報
- ComfyUI Desktop公式AMD ROCm対応（2026年1月以降、v0.7.0〜）
- AI-Toolkitの概要（LoRA特化、Web UI/YAML対応、多モデルサポート）
- RefMODの概要（safetensors変換、ComfyUI連携、トレーニング不要の一貫性実現）

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出に基づく）**

ログから抽出された主なツールは、**ComfyUI**を中心としたワークフロー/ノードベースの環境と、LoRA作成・参照管理・フレーム補間などの補助ツール群です。モデル（Krea2、MiniMax H3、Qwen-Image系など）に関する言及はすべて除外しています。ツール選択の主な理由として、**処理速度・VRAM負荷低減・GUIの使いやすさ・操作の簡便さ・既存機能の置き換え可能性・安定性**が繰り返し挙げられています。

### 1. ComfyUI（および関連カスタムノード・拡張）
ComfyUIはノードベースのビジュアルワークフロー構築ツールで、画像・動画生成の柔軟な制御が可能。ブラウザ上でドラッグ&ドロップ操作を行い、外部プロンプト連携やLLMとの統合がしやすい点が評価されています。

- **主な話題・機能**:
  - ドラッグ&ドロップ時のタブフリーズ対策（Chromeグラフィックアクセラレーションのオンオフ、Firefox推奨）。
  - フレーム補間機能（標準搭載のVFI Frame Interpolationが高速で、RIFE TensorRT不要化）。
  - 生成再現性の問題（更新やCUDAカーネル差によるシード結果の変動）。
  - NegPiPの代替としてkijaiのkjnodes「Krea2 Prompt Weight」を推奨（安定性向上）。
  - 大規模Workflow対策（JSON出力ノードの活用）。
  - 拡張「Image-Studio」：参照画像からキャラクターシート（3面図・顔アップなど）作成に活用。動画生成時の素材作成を効率化。
  - comfy_kitchen_attentionなどの最適化ノードで速度向上（例: 1.15it/s → 1.40it/s）。
  - ROCm（AMD GPU）対応のインストール・運用。
  - Comfy Desktop安定版（v0.37.0など）のテンプレート同梱や更新チャンネル管理。

- **選ばれている理由**: ノードベースによる細かい制御（ガイド、ループ、編集）の柔軟性、手動作業の削減、LLM連携の効率化、速度・軽量化オプションの豊富さ。既存ツールの置き換えやAMDユーザー向け互換性もポイント。

### 2. RefMOD（RefMods / context loop ref2v 関連）
MiniMax H3向けの参照画像/動画を小さなsafetensorsファイル（数MB程度）に変換するツール/手法。ComfyUIのカスタムノード（ComfyUI-MiniMaxH3Modなど）と組み合わせて使用。

- **主な話題**: 参照画像を揃えるだけで動画LoRA相当のキャラクター一貫性を実現。Ref2VAループ時の安定生成や複数参照の組み合わせ検証。
- **選ばれている理由**: 従来ハイエンド勢のみ可能だった作業を誰でも簡易に実現。参照画像のToken数管理に注意が必要だが、処理の簡便さと再利用性が優位。

### 3. AI-Toolkit（ostris/ai-toolkit）
拡散モデル向けのLoRA学習ツールキット。YAML設定またはWeb UI（Gradio/Next.js）で運用可能。

- **主な話題**: Krea2などのLoRA作成で16GB VRAM環境（RTX 4080 Super）で使用。3000stepで数時間規模の学習。
- **選ばれている理由**: **GUIの使いやすさ・設定の簡易さ**（yaml編集も可）。内部がmusubi-tunerベースで信頼性が高く、musubi-tunerよりGUI面で優位という評価。

### 4. musubi-tuner（kohya-ss/musubi-tuner）
HunyuanVideo、Wan、MiniMax H3、FLUXなど多様なモデル向けLoRA学習スクリプト群。ブロックスワップなどのメモリ最適化機能あり。

- **主な話題**: AI-Toolkitからの移行検討や、VRAMオーバー対策としての設定検証。
- **選ばれている理由**: 高度なメモリ効率化オプションで低VRAM環境対応。ただしGUI不在のため設定難易度が高めとされ、AI-Toolkitとの併用・比較で言及。

### 5. その他のツール
- **VFI Frame Interpolation**: ComfyUI内フレーム補完。TensorRT不要で高速。
- **Codex**: AIによるカスタムノード自動生成。ComfyUI内での手作業削減に寄与。
- **LM Studio / OpenWebUI / LlamaWebUI**: ローカルLLM起動・プロンプト作成。ComfyUI連携で環境一貫性を確保。
- **Comfy-Kitchen**: ROCm最適化PR活用による速度向上。
- **コンテナ（Docker） / wise folder**: 環境分離・セキュリティ対策。
- **Unsloth Desktop**: サンドボックス用途でCodexの挙動懸念対策。
- **jev**: 自社/個人システム組み込み検討（オープンソース・小型化前提）。

**全体の傾向**: ツール選択は「速度・VRAM効率」「GUI/操作性」「安定性・互換性」の3点が特に強調されています。ComfyUIを中心としたエコシステム内で、これらのツールを組み合わせることでワークフローの効率化が図られています。

## Web検索による参考情報
- **ComfyUI Desktop v0.37.0**: 2026年9月20日頃にリリースされたComfyUI本体のバージョン。Comfy Desktopアプリは複数インストールの並行運用、ワンクリック更新、スナップショット機能などを提供し、GPU-ready環境を容易に構築可能。[[1]](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.37.0)[[2]](https://github.com/Comfy-Org/ComfyUI/tags)
- **ComfyUI ROCmサポート（Windows）**: 2026年1月頃からComfyUI Desktopで公式AMD ROCm対応が開始（v0.7.0以降）。RX 7000/8000/9000シリーズなどで利用可能となり、公式インストール手順が整備されている。[[3]](https://blog.comfy.org/p/official-amd-rocm-support-arrives)[[4]](https://rncz.net/blog/comfyui-windows-11-rocm-z-image/)
- **AI-Toolkit**: ostris氏によるオープンソースの拡散モデルファインチューニングツールキット。LoRA学習に特化し、Web UIとYAML設定の両対応。FLUX/SDXL/Wan/Z-Imageなど多様なモデルをサポート。[[5]](https://github-com.translate.goog/ostris/ai-toolkit?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)
- **musubi-tuner**: kohya-ss氏によるLoRA学習スクリプト。HunyuanVideo、Wan、MiniMax H3、FLUXなど動画・画像モデル向けにメモリ効率化機能（block swapなど）を備える。[[6]](https://github.com/kohya-ss/musubi-tuner/blob/main/README.md)
- **RefMOD / RefMods**: MiniMax H3向けの参照アダプタ作成手法。画像/動画を小さなsafetensorsファイル（1MB前後）に変換し、ComfyUIノードでLoRA風にロード可能。トレーニング不要でキャラクター一貫性を実現するコミュニティプロジェクト。[[7]](https://comfyui-wiki.com/en/news/2026-09-07-minimax-h3-refmods)

これらの情報は2026年9月時点の検索結果に基づきます。実際の利用時は最新のGitHubリポジトリや公式ドキュメントを確認してください。
