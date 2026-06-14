**抽出結果**

### ComfyUI関連（ワークフロー・カスタムノード中心）
- **ComfyUIワークフロー**（特にIdeogram4用）
  - Ideogram4向けに追加学習させたVAEをComfyUIで使用するワークフローが共有されている。
  - 理由：Liquid9745VAEに近い色合い（ピンク強調・ビビット）を実現するため。
- **カスタムノード関連**
  - **Pixel Art Enhancer**：解像度を落とした際にエッジがボケず、パキッとしたドット絵になるため選ばれている。
  - **comfy_pixelization**：処理速度が非常に速い（1秒未満）点が評価されている。一方、Pixel Art Enhancerは色数・彩度・コントラストの調整が可能で多機能。
  - その他：自作ノードやCombine Primitive(misc)などのノードをワークフローに組み込んでいる事例あり。
- **全体の傾向**：生成画像そのものより「ComfyUIのノードいじり」や「新技術の情報収集」に時間を費やしているユーザーが複数存在。

### Forge / Forge Neo関連
- **Forge Neo**と**reforge**の比較
  - Forge NeoはZ-Image turbo、Qwen、Animaなどの最近のモデルへの対応が優れている。
  - reforgeは従来の拡張機能との互換性が高い傾向があるが、Forge Neoの方が新モデル対応で上位互換的な位置づけ。
  - Forge Neo使用時に生成時間が徐々に伸びる現象が報告されており、注意点として挙げられている。

### 音声・動画生成ツールの組み合わせ
- **使用ツール群**：
  - ComfyUI版Ideogram4
  - Irodori-TTS
  - MMAUDIO（音声・効果音生成）
  - Ultimate Vocal Remover（声の除去）
  - ffmpeg（MIX処理）
  - SUNO AI
- 理由：MMAUDIOで生成した音声をUltimate Vocal Removerでクリーンアップし、ffmpegで最終調整するパイプラインを構築するため。

### その他
- **Ideogram Studio / IdeogramHelper**：Kijai氏とは別のIdeogramHelperノードが登場。アプリっぽいUIで扱いやすい可能性が指摘されている。
- **leco学習UI**：ADDifT（2枚の画像の差分のみを学習する機能）の実装が完了したとの報告あり。差分学習需要についての言及あり。

**モデル名・新サービス等のWeb検索参考情報**  
（該当する新バージョン・新サービスに関する記述はログ内にほとんどなく、事実確認を要するものは以下の通り）

- **Ideogram 4 / Realism Engine Ideogram 4 V2**：Ideogramの新バージョンとして言及されているが、公式に「V2」としてリリースされたかどうかは未確認（ログ時点でのユーザー間の呼称の可能性が高い）。
- **Forge Neo**：Stable Diffusion WebUI Forgeの派生版として、最近のモデル対応を強化したフォーク。作者が異なるreforgeとは別系統。

以上が「ツール」に関する抽出内容です。モデル（Anima、illustrious、WANなど）に関する言及は除外しています。