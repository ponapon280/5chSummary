**なんJスレッド要約レポート（AI画像生成・ComfyUI中心）**

### スレッドの概要
- スレッドは主に**ComfyUI**でのワークフロー構築、**Anima**モデル（および関連LoRA）の運用・学習、Turbo LoRAを活用した多段階生成、アップスケーラー選び、LoRA作成Tipsを中心に進行。
- 2〜3段階生成（低解像度→Turbo適用→ディテール調整）の手法が複数回提案され、構図維持と破綻修正のバランスが話題の中心。
- Animaの階層LoRA適用・LECO/iLECO実装、negpipの活用、shift値1による多様性向上など、技術的な試行錯誤が活発。
- 新規情報としてNVIDIA Cosmosシリーズ（Cosmos3-Super-Text2Image / Image2Video、64B規模）の言及あり。将来的なAnima v2への期待も散見された。

### 主な議論ポイント
- **多段階生成ワークフロー**: 1段目で通常モデル＋低解像度生成 → 2段目以降でTurbo LoRA適用（低denoise＋高shift値）。hires fixよりi2i寄りの運用が推奨され、構図の安定性と速度の両立が評価された。
- **Anima関連**: Turbo LoRAの挿入順、CFG/Stepの切り替え方法（スイッチノードやGroups Muter活用）、公式baseモデル以外でのLoRA学習失敗事例。LECO実装の試みも報告。
- **アップスケーラー**: ScuNET（Forge時代に愛用）がForge Neo移行後に挙動変化。RealESRGAN_x4plus_anime_6BやStarSampleの評価も。
- **その他**: Civitaiのフィルタ不具合、音声生成（Irodori-TTS）、furry/デフォルメ系LoRAの破綻対策、shift1生成の多様性検証。

### ## Web検索による参考情報
- **NVIDIA Cosmosシリーズ**: 2025年頃にNVIDIAが発表した物理AI向けWorld Foundation Model群。Cosmos-2B/4B/64B規模のText2Image・Image2Videoモデルが存在し、DiTベースでトークン間関係を強く捉える構造が特徴。SDXL系とは異なる挙動のため、Animaのようなfine-tuneモデル開発に影響を与える可能性あり（公式発表・Hugging Face/NVIDIAブログに基づく）。
- **Animaモデル**: コミュニティ製のアニメ特化fine-tuneモデル（Illustrious系やCosmos系を基盤とする噂）。公式baseモデル（anima_baseV10など）でのLoRA学習が安定しやすい点や、階層制御・LECO対応が特徴として挙げられる。開発者は将来的に企業支援を視野に入れている発言あり。
- **Forge Neo / ScuNET**: Forge Neoは初期状態で利用可能なアップスケーラが限定されており、ScuNETなどの外部モデルは手動配置が必要。ComfyUI環境との互換性に差が出る事例が報告されている。
- **その他ツール**: rgthreeノード（Context Big、Fast Groups Muter）、Animarge、AnimaEditなどはComfyUIカスタムノードとして実際に存在・利用されている。

スレッド全体として、**実践的なワークフロー共有**と**新モデル（Cosmos/Anima）への期待・検証**が主眼。