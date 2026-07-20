**抽出されたツール関連話題（モデル関連は除外）:**

- **ComfyUI（comfy）関連**:
  - ComfyUIをゲームエンジンやマイコンと接続する用途（言語モデルのコード生成能力を活かした連携）。
  - ComfyUIのカスタムノードを「install via Git URL」ボタンで直接インストールする機能（0.28.0で消滅した件、セキュリティ問題による廃止の可能性）。
  - ComfyUIのバージョン管理（0.27.0 frontend 1.45.20 / manager 3.41、0.28.0、最新Manager v4.2.2 + `--enable-manager-legacy-ui`引数）。
  - ComfyUI上で漫画作成が完結するワークフロー。
  - ComfyUIのROCm対応（公式サポート、comfyui-rocmリポジトリ推奨、sageattention等の諸々をまとめて入れてくれる利便性）。
  - ComfyUIv0.28でのSeedVR2ネイティブサポート。
  - ComfyUIの公式コミットログ確認によるllliteネイティブサポートの進捗。

- **Stability Matrix関連**:
  - Forge Neo / reForgeの表示（NVIDIA表示のみ vs CPU/NVIDIA/ROCm/macOS表示）。
  - modelsフォルダ全消しなどの既知の問題。

- **reForge / Forge Neo関連**:
  - ROCm対応状況や公式READMEとの整合性。
  - メモリリーク・VAE固まり対策としての公式対応の有無。

**特に選ばれている理由として抽出された点**:
- ComfyUI（特にcomfyui-rocm）：ROCm公式対応が厚く、インストールの手間（sageattention等）が省けるためRadeonユーザー向けに便利。
- ComfyUI：SeedVR2やllliteなどの新機能がネイティブサポートされやすい。
- reForge選択：Stability Matrix上ではROCm表示があるため選ばれやすいが、公式対応の薄さが指摘される。
- ComfyUI全体：公式の機能追加意欲が高く、カスタムノードや外部連携がしやすい。

（Anima/Krea/redcraftなどのモデル名や生成例は一切除外。Qwenシリーズの非画像生成話題は該当なし。）