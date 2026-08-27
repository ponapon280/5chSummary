ログから生成AIに関関連する「ツール」に関する話題を抽出しました。モデルに関する話題（NovelAI、illustrious、FLUX、Wan、Qwen-Image、anima、Z-Image、LTXなど）は除外しています。

**抽出したツール関連の話題:**

1. **ComfyUI関連（comfy）**
   - 80: IrodoriTTS v4へのアップデート、ComfyUIカスタムノード未対応、Gradio UIで絵文字が効きにくい
   - 163: civitaiで配布されているWF、画期的なカスタムノードの有無
   - 166: dasiwa配布WFの専用カスタムノード、ComfyUI公式テンププレートの方が良い
   - 183: Context Loopの検索、ComfyのNative対応待ち
   - - 189: comfy-kitchenのpr117更新、sol_attn_minimax_v3.pyノード追加
   - 189: comfy-kitchenのpr117更新、kijai氏の高速化、sol_attn_minimax_v3.pyノード
   - 190-194: 検索しても出てこない、自分でコンパイル必要、ビルド済みwheelの存在
   - 195: ComfyUIで動画生成・画像生成時のメモリ増設の影響
   - 197: 4枚刺し4000MHzでの生成速度、誤差数秒程度
   - 210: Sol-Atten(MinMax)VideoProcessサブグラフの設定、Sage Attentionより遅い
   - 213: モデルとサンプラーの間に挟む、Patch Sol-Attn (MiniMax)ノードのselection設定
   - 215: ノード設定の確認
   - 219: LoRAローダーの位置調整
   - 220: 設定が合っているが速度変わらない
   - 221: top-k(SLA)の使用用途
   - 224: 生成時間の計測（12分28秒 vs 12分25秒）
   - 225: RTX5080でのcomfy kitchenや#117の恩恵、sage attentionとの比較

2. **webUI関連（webUI）**
   - 該当なし（直接的なwebUIの言及なし）

3. **nano-banana関連**
   - 該当なし

4. **その他ツール関連**
   - 22: tadaupのファイルサイズ・形式制限（h264圧縮のmp4が上げられない）
   - 25: ローカルAPIを使えるハーネス（無料GPTで十分）
   - 29: 戦闘シーンの爆発音の書き方（プロンプト作成）
   - 124: deepseek apiで画像を読めるようになった（プロンプト作成効率化）
   - 153: Aviutlでのモザイク処理、出力時の問題
   - 165: aviutlでのモザイク処理手順、x264guiEx出力設定
   - 189-194: comfy-kitchenの詳細（上記）
   - 210-225: ComfyUI関連の詳細（上記）

**ツールが選ばれている理由:**
- ComfyUIはカスタムノードやワークフローの自由度が高く、コミュニティによる拡張が活発（kijai氏の高速化など）
- ローカルAPIハーネスは無料GPTで十分という意見
- aviutlはモザイク処理に広く使われている
- deepseek apiは画像読み込み対応でプロンプト作成が捗る

**特に注目すべき点:**
- ComfyUI関連の話題が最も多く、特に「comfy-kitchen」の高速化（sol_attn_minimax_v3.py）が注目されている
- ユーザー間で設定や使用方法の共有が活発
- 生成速度の計測結果が具体的に共有されている