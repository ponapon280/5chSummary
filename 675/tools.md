# 🆕 新規トピック（前回からの差分）
### ComfyUI
- 選ばれている主な理由
- 保存形式やプロンプト管理の利便性（webp推奨、拡張機能）

### Krea2 / krea2workflow
- プロンプト反映が良く、フォトリアリズム寄りの出力が安定。LoRAの付け外しや編集用途に適する

### Forge / ForgeNeo / EasyReforge 系
- ForgeNeo 2.27頃からKrea 2 Edit（LoRA）対応、Lora付け外しバグ、旧ForgeのPython更新リスク、Anima導入検討

### StabilityMatrix
- irodori対応への期待、手動管理の煩雑さ解消

### SwarmUI
- モジュール性・高性能・拡張性を重視した代替UIとして位置づけられ、ComfyUIとの併用や移行検討の文脈で言及

### その他のツール・環境関連
- VACE Prep / VACE Join: 動画結合時のフレーム改変・境目対策に特化
- Clipchamp / DaVinci Resolve: 簡易動画編集・結合や後処理用途
- ROCm（AMD環境）: Radeonユーザー向け動作確認・環境構築ツール
- OpenRouter API: フィルター・クレジット管理の問題で敬遠

### Web検索による参考情報
- ComfyUI v0.29.2: Frontend fixes、新規api/partner nodes、MiniMax H3モデルサポート追加
- StabilityMatrix: 複数WebUIの一元管理が可能なオープンソースパッケージマネージャー
- SwarmUI: Stability AIから独立したモジュール型Web UIで、Stable Diffusionや動画モデル対応

---
# 元の本文
**生成AI関連ツールのレポート**

抽出されたテキストから、主にローカル環境での画像・動画生成ワークフローを支えるツール群が特定されました。ComfyUIが圧倒的に多く言及されており、ノードベースの柔軟性・カスタマイズ性・RAMオフロード対応が選定の主な理由として繰り返し挙げられています。その他、インストール管理ツール、代替UI、特定用途の拡張ツールが散見されます。以下にツールごとに整理し、選ばれている理由を明記します（モデル名・バージョン関連は後述のWeb検索参考情報で補足）。

### ComfyUI（comfy / comfy-org）
最も頻出のツール。ポータブル版が推奨され、カスタムノード管理や複雑なワークフロー構築に用いられています。
- **言及の主な内容**: 3060での動作確認、v0.29.2アップデート時のバグ（Custom Combo再発）、安定版v0.26検討、動画生成WF（WanImageToVideo、WanFirstLastFrameToVideo、PainterLongVideo、VACE Joinなど）、RAMオフロード前提の長尺動画、Minimax H3 API対応、webp保存（品質90）、Prompt All in One拡張必須、カスタムノード依存のトラブル、ノード名衝突対策。
- **選ばれている理由**:
  - ノードベースの柔軟性により、フレーム結合・前処理（VACE Prep相当）・サブグラフなどのカスタム処理が容易。
  - RAMオフロード技術との相性が良く、VRAM不足環境（例: 3060）でも長尺動画生成が可能。
  - ワークフロー共有・再利用・テンプレート充実により、更新耐性が高く、複雑パイプライン（T2V/I2V/R2Vなど）を扱いやすい。
  - 保存形式やプロンプト管理の利便性（webp推奨、拡張機能）。
  - 公式/コミュニティのWF公開・API連携が進んでおり、拡張性が高い一方で、依存関係の管理が必要（初心者ハードル高め）。

### FramePack
- **言及の主な内容**: RAM64GB前提、VRAM8GB+RAM64GBでの動作確認。
- **選ばれている理由**: 当時のRAMオフロード技術の先駆けとして、VRAMが少なくても実用可能。ComfyUIなどとの組み合わせで低スペック環境を補完。

### Krea2 / krea2workflow
- **言及の主な内容**: 公式WFベース運用、カスタムノード未使用からの移行、画風LoRA学習ベース、シードハンター機能、Edit機能（1枚絵→実写変換など）。
- **選ばれている理由**: プロンプト反映が良く、フォトリアリズム寄りの出力が安定。公式範囲内で扱いやすく、LoRAの付け外しや編集用途に適する（ただし露骨な内容では理解力が低下する傾向あり）。

### Forge / ForgeNeo / EasyReforge 系
- **言及の主な内容**: ForgeNeo 2.27頃からKrea 2 Edit（LoRA）対応、Lora付け外しバグ（おま環扱い）、旧ForgeのPython更新リスク、Anima導入検討時の話題。
- **選ばれている理由**: ComfyUIより手軽にLoRAを扱える場面がある。インストール・運用の簡易さで選ばれやすいが、更新追従性や安定性でComfyUIと住み分け。

### StabilityMatrix
- **言及の主な内容**: irodori対応への期待、手動管理の煩雑さ解消。
- **選ばれている理由**: 各種WebUI（ComfyUI、Forgeなど）のインストール・管理・更新を一元化し、環境構築を簡素化。共有モデルリポジトリやCivitai連携が便利。

### SwarmUI
- **言及の主な内容**: 「みんなでSwarmUI使おう」という軽い提案のみ。
- **選ばれている理由**: 詳細な言及は少ないが、モジュール性・高性能・拡張性を重視した代替UIとして位置づけられる（ComfyUIとの併用や移行検討の文脈）。

### その他のツール・環境関連
- **VACE Prep / VACE Join**: 動画結合時のフレーム改変・境目対策や結合処理に特化。切れ目の少なさでSVI（別ツール）と比較される。
- **Prompt All in One**: ComfyUI必須級拡張。複雑WFでのプロンプト管理負担軽減。
- **Clipchamp / DaVinci Resolve**: 簡易動画編集・結合や後処理（モザイク）用途。
- **ROCm（AMD環境）**: 動作確認・環境構築ツールとして、Radeonユーザー向け。
- **OpenRouter API**: ローカルツールとの比較で言及されるが、フィルター・クレジット管理の問題で敬遠。
- **ハードウェア関連（実行環境）**: eGPU（dxg spark）によるVRAM拡張、RTX PRO4000SFF（低消費電力・大VRAM）、NVMe SSD必須（オフロード多発時のボトルネック解消）、3060/5080/4090などの選択理由（リスク低減・安定生成）。

全体として、**ワークフロー/LoRAの扱いやすさ**、**インストール・管理の簡易さ**、**特定機能対応（API連携・保存形式・オフロード）**、**依存関係の安定性**がツール選定の4大ポイントとして抽出されます。ComfyUI派が優勢で、Forge系や管理ツールが補完する形です。

## Web検索による参考情報
- **ComfyUI v0.29.2**: 2026年7月31日リリース。Frontend fixes、新規api/partner nodes追加。MiniMax H3モデルサポート（Ideogram P-Imageと並んで）が追加されており、テキスト中の「Minimax H3のAPI版対応」と一致。[[1]](https://docs.comfy.org/changelog)[[2]](https://github.com/comfy-org/ComfyUI/releases)
- **Minimax H3 API**: ComfyUI v0.29.2で公式サポートされたモデル/API連携機能。パートナーノードとして実装。
- **StabilityMatrix**: AI Art WebUI（ComfyUI、Forge、Automatic1111など）のインストール・管理・更新を一元化するオープンソースパッケージマネージャー。One-clickインストール、共有モデルリポジトリ、Civitai連携が特徴。テキスト中の「インストールの楽さ」期待と合致。[[3]](https://lykos.ai/)
- **SwarmUI（旧StableSwarmUI）**: Stability AIから独立したモジュール型Web UI。Stable Diffusionや動画モデル（Wanなど）対応、powertoolsのアクセシビリティを重視。テキスト中の提案と一致。[[4]](https://github.com/Stability-AI/StableSwarmUI)
- その他（FramePack、Krea2、ForgeNeo、VACE Prep、irodori、SVIなど）は公開情報が限定的またはモデル/ワークフロー固有のため、テキスト内の言及に基づく記述を優先。ハードウェア（eGPU、NVMe SSD、ROCm）は生成環境のベストプラクティスとして一般的に支持される傾向。
