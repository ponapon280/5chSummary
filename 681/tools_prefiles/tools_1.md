**抽出されたツール関連話題（ComfyUI中心）**

### 1. ComfyUIのワークフロー・ノード関連
- **H3 Motion Contextノード**  
  「ComfyUI-H3-Motion-Context」のexample_workflowsを使用したが、`H3 Motion Context Load Latent`ノードでエラーが続く。WF画像を求めている投稿あり。  
  → **選ばれている理由**: Motion Contextを活用した動画生成のため。

- **FramepackOichi風の使い方**  
  MiniMaxをFramepackOichiのように参照画像を多用する形で使う方法が話題に。静止画生成への転用可能性も指摘。  
  → **選ばれている理由**: 参照画像処理能力が高いため。

- **レガシーNode vs Nodes2.0**  
  ComfyUIのレガシーNodeがCanvas描画でGPU使用率を押し上げている点が指摘され、Nodes2.0への期待が述べられている。

- **各種最適化ノード・拡張**  
  - sage attentionノード
  - Spectrum（音質・速度関連）
  - Turbo（ステップ数削減）
  - Sol, effi などの組み合わせ

### 2. ComfyUI起動オプション・高速化設定
- `--fast-disk`, `--disable-pinned-memory`, `--cache-none`, `--reserve-vram` などのオプションが複数言及。
- 最小化実行で生成速度が向上（画面表示によるVRAM消費を避けるため）。
- EasyMiniMax（高速化てんこ盛りのカスタム環境）の要望と、それに対する「公式に高速化を入れるだけで十分」という意見。

### 3. 音声・TTS関連ツール
- **IrodoriTTS**  
  動画生成に組み込んで自動化したいという要望。

### 4. その他のツール・環境関連
- **Codex / Claude Code**  
  ノード接続やUI作成、プロンプト生成を任せる用途で言及。ComfyUIの複雑なノード接続をAIに任せる使い方が推奨されている。
- **スマホ用UI（Codex作成）**  
  帰省先などPC以外からの生成を可能にするためにCodexにUIを作らせている事例。

### 5. 選ばれている主な理由（傾向）
- **速度・安定性**: 最小化実行、起動オプション、Spectrum/Turboなどの組み合わせで生成時間を短縮。
- **VRAM管理**: 16GB環境でも動く設定（--reserve-vramなど）を重視。
- **参照画像の扱いやすさ**: MiniMaxの強みを活かすためのComfyUIノード・ワークフローの選択。
- **日本語対応・細かい制御**: テキストエンコーダーやプロンプトの扱いやすさ。

モデル（H3、Wan2.2、Animaなど）に関する言及はすべて除外しています。