### 抽出された「ツール」関連話題一覧

以下は、提供されたログから生成AI関連の「ツール」（ComfyUI, webUI, nano-banana, kohyaスクリプト, llama-cpp-python, Forge Neo, StabilityMatrix, ADetailer/FaceDetailer, LM Studio など）に関する話題を**すべて**抽出・整理したものです。モデル（anima, illustrious/リアス, Wan, NAI など）の話題は除外。Qwenシリーズは画像生成（Qwen-Imageなど）以外の話題（例: Captioner/tagger用途）は抽出。ツールが選ばれている理由や利点が明記されているものは強調して記載。各ログ番号順にまとめ、重複は統合。

#### 33: ComfyUI
- ComfyUI起動直後の初回生成が数ピクセル微妙に異なる問題（以降は同一WFで安定）。nvidiaのcuDNNが原因の仕様っぽい。

#### 44: kohya氏のキャプション付けスクリプト
- kohya氏のキャプション付けスクリプト使用。gemmaモデルでエロ画像をsafeタグ付けしてしまう問題をgemmaに相談したらドスケベ対応プロンプトに改良してくれた（理由: エロ対応強化）。

#### 47, 51: Qwen3-VL-8B-NSFW-Caption / qwen3のtagger + ComfyUI + llama-cpp-python
- Qwen3-VL-8B-NSFW-CaptionをComfyUIで一括タグ付け。環境構築（llama-cpp-python）がCPU/GPUで鬼門で時間かかるが、動かすのは楽（CPU運用推奨）。AIのトラブルシューティングまとめ機能が便利（職場の先輩並み）。
- >>51: 普通の無検閲qwen3のtaggerより良いか？（比較話題）。

#### 58-60, 135: comfy couple / couple系ノード / Forge系 + ComfyUI_Mira / Create Tilling PNG Mask / krita / character_select_stand_alone_app / comfyui-prompt-control
- comfy couple（シンプル）使用中。Forge系のようにマウスで適用範囲決めたい。ComfyUIだと少ない。
- >>59: comfy couple以外のノードおすすめ求む。
- >>60: Create Tilling PNG Mask（カスタムノード: ComfyUI_Mira）使用。プロンプトごとに領域指定（画像にWF残ってる）。
- >>135: 領域指定ツールとして①kritaの領域指定描画、②character_select_stand_alone_appのRegional Condition（WAI専用）、③comfyui-prompt-control（3つしか知らない）。

#### 75: banana (nano-banana推定)
- bananaで学マス10人生成試すが、初星学園の文字しか出ず駄目。

#### 78: easyanimaワークフロー (ComfyUI)
- 高速化/VRAM削減/キャッシュフローを兼ね備えた赤ちゃん用easyanima WFはまだか。

#### 84-95: Forge Neo + ComfyUI / NEO
- >>84: 赤ちゃんはforge neo使え。
- >>85: forge neoでは面倒見切れない（最新技術触れたがる赤ちゃん向けでない）。
- >>88: Forge Neoでanimaのxy plot使えるか？ ComfyUIだとWF組めない赤ちゃん。
- >>89: ComfyUIで「animaでこういう事したい」と授乳せがめばWF作ってくれる。forge neoだと開発者に亀頭するしかない。
- >>90: Comfyがオシャカなら下ちいWF作ってもらう。
- >>91: ローダーnode/LoRA(ry)で読み出し対象変え/nodeスキップで対応可。
- >>95: comfyカスタムせずテンプレ使用ならneoでいいが、ここ住民はcomfyバリバリ（趣味程度ならneo）。

#### 96: 仮想環境設定 (cuda/python/torch)
- cuda12.8 + python3.11 + torch2.7.1 or 2.8 が互換性高くオススメ（RTX5000対応、python3.11で処理早い）。コマンド叩ける人向け。

#### 97, 103: claude (一発インストールツール)
- claudeに「exeクリック一発インストール」頼んだら作って動いた。
- >>103: comfyインストールフォルダでclaude --dangerously-skip-permissions でエラー直し。

#### 99, 105: XY Plot WF (ComfyUI/civitai)
- >>99: Anima XY Plot WFをcivitaiにアップ。
- >>105: サンガツ、試す。

#### 117: KohyaのGUIプリセット
- Kohya GUIプリセットでLoRA学習したが効果なし（fp8読み込み無効化で解決？）。自前時は効果あり。

#### 119, 124, 129, 132: ADetailer / FaceDetailer + ForgeNeo / StabilityMatrix / yolo.pt / SafeTensor / sam3
- >>119: Adetailer用の乳首LoRA（Anima-preview3版）。
- >>124: detailerモデルはyolo.pt（SafeTensorは保存場所違う？）。
- >>129: ForgeNeoならModels/adetailerフォルダ、StabilityMatrixならdata\models\AfterDetailer、ComfyUIはFaceDetailer（Manager経由）。noteに導入法多数。
- >>132: sam3で読み込みエラー、諦め。

#### 203, 208, 217-218: ComfyUI WF (Klein導入/切り替え/グループ/サブグラフ)
- >>203: 前スレWFにKlein導入方法わからん（sdxl/anima/klein切り替え？）。
- >>208: 切り替えスイッチ2つだけなので無理。WF分ける方がいい。
- >>217: SDXL/animaでサンプラー違う/CN tile必要で一緒にすると品質上げにくい。
- >>218: WFテンプレ縦並べ/グループ化/選択ミュート（サブグラフで情報量減）。WF分けた方がいい。

#### 235-236, 239, 241, 244: LM Studio (シスプロ/Thinking設定)
- >>235: LM Studio 0.4.11でシスプロ設定場所わからん（チャット初め手書き？）。
- >>236: シスプロ工夫（品質タグ省略でタグ+自然英語のみ出力）。
- >>239: モデル一覧の歯車から設定。
- >>241: チャット右側タブ/モデル一覧で詳細設定可（パラメーター悪いと繰り返し）。
- >>244: qwen3.5-35bのThinking長すぎ（Q5？）。

#### 237: 翻訳APIノード
- 簡単英文プロンプトはLLM通さず翻訳APIノードでOK。