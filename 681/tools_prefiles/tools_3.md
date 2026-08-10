**抽出結果（ツール関連のみ）**

### ComfyUI（comfy）関連
- **複数回登場**し、動画生成・ワークフロー構築のメイン環境として使われている。
  - 具体的な言及：
    - ComfyUI上でGemma4を使って画像9個・動画3個・オーディオ3個まで参照できる「MiniMax H3 Prompt Writer」というワークフローが話題。
    - `load image batch`をランダム設定で繋いで性別関係なく登場人物をガチャする手法。
    - `Model Preview Override`を使って短時間で構図・流れを確認する使い方。
    - `contact_sheet`（examplesディレクトリ内）を使ったキャラシート作成ワークフロー。
    - `Patch Sage Attention KJ`ノードの使用（グローバル設定との併用・切り替え）。
    - `qwen edit`ノードの使用（アップデート後の雰囲気変化を指摘）。
    - `Single frame edit basic`（CivitaiのSimple Image Editとの比較）。
    - `I2Vワークフロー`（公式デフォルトに近いシンプルなものを推奨）。
  - **選ばれている理由**：
    - ワークフローの柔軟性が高く、参照画像・動画を組み合わせた複雑な制御がしやすい。
    - ノード単位でSage Attentionのオンオフを切り替えられる。
    - シンプルなワークフローの方が高品質が出やすい傾向がある。
    - ローカル環境でH3などのモデルと組み合わせやすい。

### Stability Matrix
- ComfyUI環境の構築・拡張機能（sage attentionなど）のインストールに使われている。
  - **選ばれている理由**：sage attentionの導入が比較的簡単。

### その他
- **webUI**：1回のみ言及（「webuiの『画像を生成』ボタン」）。内部処理の例として触れられた程度で、積極的な使用話はなし。
- nano-bananaなどの言及はなし。

**除外したもの**
- モデル名（H3, Wan, anima, Qwen-Image系など）の性能・比較話
- LLM単体の話（Gemini, Claude, Grokなど）はツールとしてのComfyUIとの連携時のみ言及を残した

主なツールは**ComfyUI**で、ワークフローの柔軟性・ノード制御のしやすさ・参照機能の強みが選ばれる理由として繰り返し語られています。