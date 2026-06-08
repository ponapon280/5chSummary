**抽出されたツール関連話題**
- **ComfyUI (comfy)**: 複数言及あり
 - アプデによる動画生成速度変化（5秒動画が1分遅延、dynamic vram実装影響）。旧バージョンと最新バージョンの使い分け推奨。
 - ネイティブノード vs カスタムノードの動作保証問題（カスタムノード使用時は将来的に動作しなくなる可能性）。
 - メタデータからのワークフロー自動作成機能（SDXL系への変換バグ発生例）。
 - dynamic vramのオン/オフによる生成時間への影響確認。
 - 理由：デフォルト設定が最速になるよう設計されているが、カスタムノード多用時は旧環境保持が推奨されるため。
- **Ideogram (Ideogram4.0 / Ideogram Prompt Builder KJ)**: 複数言及あり
 - JSON形式プロンプトによる生成（検閲回避・正確な制御）。
 - bounding box形式での配置機能。
 - API版（Turbo/標準/Qualityの段階あり）とローカル版の画質・機能差。
 - Image参照機能（API版で対応）。
 - Prompt Builder KJノードの挙動（タブ移動時のレイアウト崩れ）。
 - 理由：手書き指示や複雑な構図指示に強く、JSONで位置指定できる点が革命的。ローカル版でも一定水準のテキスト/構図制御が可能。
- **webui**: 1言及
 - Gemini向けパンピー向けwebuiの規制内容。
- **Affinity (Affinity Photo)**: 背景削除ツールとして言及
 - 無料機能での背景削除用途。
**除外した内容**
- Anima / WAI-ANIMA / hakushi / cotton などのモデル比較・LoRA・プロンプト効き。
- LTX / Qwen-Image / Z-Image などのモデル名・生成例。
- Gemini / Gemma などのLLM単体の性能談義（Qwenシリーズ非該当のため非抽出）。
**## Web検索による参考情報**
- Ideogram 4.0：2025年頃にリリースされたオンライン画像生成サービス。JSONプロンプト対応とbounding box機能が特徴で、API版とローカル版が存在。ローカル版はTurboモデルが主に配布されている。
- ComfyUI dynamic vram：メモリ効率化機能として実装されたが、一部環境で動画生成速度が低下する報告あり。GitHub Issueでの報告が推奨されている。