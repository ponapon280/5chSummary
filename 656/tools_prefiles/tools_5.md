**抽出されたツール関連話題（モデル名・バージョンは除外）**

- **ComfyUI（および関連カスタムノード・ワークフロー）**  
  複数箇所で言及。主な用途はIdeogram 4.0のJSON構造化プロンプト生成・検閲回避、ワークフロー構築、画像保存先変更（Extra Launch Argumentsや--output-directory指定）、サブグラフ管理。  
  選ばれている理由：LLM連携でJSON形式プロンプトを自動生成でき、自然言語入力より検閲回避率が高いため。公式WFのJSON化ノードを生成用と分離して使う事例あり。Stability Matrix経由での利用も確認。

- **Forge（Forge Couple）**  
  Anima使用時にForge Couple機能で複数キャラのプロンプト制御を試した言及。  
  選ばれている理由：プロンプトでの複数キャラ書き分けの代替手段として検討（ComfyUIとの使い勝手比較）。

- **Stability Matrix**  
  ComfyUIのデータフォルダ・出力先管理に使用。  
  選ばれている理由：ComfyUIの各種データ（特に画像保存フォルダ）のDドライブ移行を簡単に行うため。

- **RedRayzニキのGUI**  
  スレ内で言及される独自GUIツール。  
  選ばれている理由：Animaなどのローカル生成環境で高速プリセット（低ステップ・短時間学習）を提供するため。wiki上では長らく言及されていなかった点も話題に。

- **Clip Studio Paint（クリスタ、EX版）**  
  漫画制作・画像編集ツールとして複数言及。AI生成後の修正・加筆用途。  
  選ばれている理由：マンガ素材（吹き出し・擬音など）が豊富で、AI生成物の後処理が効率的。買い切り版の利点も議論。

**モデル・サービス関連の言及は一切除外**（Anima、Ideogram、Flux、Z-Imageなど）。

## Web検索による参考情報
- **ComfyUI-KJNodes**: ComfyUI向けカスタムノード集（KJNodes）。Prompt Builder機能やワークフロー補助ノードを提供。Ideogram連携事例で言及される。
- **Forge**: Stable Diffusion WebUIのフォーク（lllyasviel/Forge）。高速化・VRAM効率に優れ、Couple機能で領域制御が可能。
- **Stability Matrix**: AI画像生成ツール（ComfyUIなど）のバージョン管理・起動ランチャー。データフォルダの柔軟な変更に対応。
- **RedRayz GUI**: 5chスレ内で言及される非公式のAnima向けGUIツール（詳細は非公開・スレ独自）。高速学習プリセットが特徴。