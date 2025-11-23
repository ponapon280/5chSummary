### 抽出された「ツール」に関する話題

ログ全体から、指定されたツール（ComfyUI, A1111, webUI, SUPIR, nano-bananaなど）に該当する話題を抽出。モデル（NovelAI, Pony, illustrious/リアス, Noobai, FLUX, Wan, Qwenなど）関連の言及は除外。ツールが選ばれている理由や文脈も併記。各レス番号順に整理。

#### ComfyUI関連（最多言及）
- **644**: バナナプロの公式アドレスを尋ねる文脈で、偽物サイトが多い。
- **658**: Comfy cloudに課金が必要か？（Web版使用時）。ローカルなら不要。APIノード使用時はクレジット課金（ComfyUI設定画面から）。OpenrouterにもAPIあり。サードパーティAPIラッパー多数。
  - **理由**: ローカル使用で課金不要、柔軟性が高い。
- **660**: ComfyUIで5ドルから課金可能（外部APIとして）。生成サイト（Fal ai, AIstudio, higgsfield, Freepik）のAPIキーをどう使うか不明。
- **661**: Comfy cloud（Web版）は課金必要。ローカルComfyUIはAPIノードでクレジット課金。
- **662**: Forge NeoでFluxなど使用可能。ComfyUIに馴染めない人向けにWebUI（Forge系）が軽快。最近のモデル対応で動きが良い。reForgeから移行予定。Gradioバージョン変更で一部拡張（Taggerなど）使えず、Issues検索必要。
  - **理由**: ComfyUIが馴染みにくい人向けにWebUI/Forge系が画像生成に適し、軽快。
- **666**: ComfyUI 0.3.71更新でUI不安定（ワークフロー名がUnsaved Workflowになりタブクリックで複製）。
- **669**: 自作Kijai版ワークフローをNative版に作り直し。OOM解消、生成速度向上。ワンボタン切り替え（サンプラー/Baseモデル/Seedガチャ/MoE/EASYWAN風LoRA）多数実装、数時間かかる。
- **670**: リリース当初はNative版無理でKijai版のみだったが、今のComfyUIアップデートでNative版推奨。
- **671**: 自分のワークフローがKijai版か判別不能。
- **692**: WAN 2.2 SmoothMixAnimationStyle Triple Sampler v1.7.1(β)のComfyUIワークフロー更新内容詳細（キュー不具合解消/FaceDetailer修正/スイッチ追加/無線化）。ComfyUIバグでNaN発生時はタブ切り替えで解決。
- **694**: ComfyUI frontend 131.0/132.0でタブ選択死。
- **696**: カスタムノード（comfyui-keep-multiple-tabs）が干渉疑い。python3.14でscikit-image不具合。
- **698/702/713**: ComfyUI-PromptSwitch 0.4.1がタブ選択死の原因。--disable-all-custom-nodesで起動したら正常。
  - **理由**: カスタムノード特定でトラブルシュート可能。
- **709**: Distorch2派だったが最近v0.3.68はComfyUI任せ（Qwen不安定で消去法）。
- **710**: ノード使わず--reserve-vram追加で安定。
- **712**: Geminiノード作成（APIキー環境変数入力推奨）。
- **727**: Blockswapノード複数あり区別不能。comfy最新版ネイティブWF希望。
- **728**: SmoothmixWan2.2公式WFシンプルで良い。easywan22環境ならアップデートせず。
- **729**: 最新版ComfyUIは賢くBlockswap不要。
- **758**: A1111からComfyUI移行。オートコンプリートが最新辞書使用？でサジェスト出ず。
- **759**: WFで5090使用時、出力フェーズ高速化限界。高画質工程で時間かかる。
- **760/766**: Cutoff（Extension）で色移り防ぐ。easyrefoge（EasyReforge）で可能（専用ではない）。
- **768**: Wavespeed使用でRTX3060で8.72秒生成（DMD系不使用）。
- **783**: WeiLin-ComfyUI-prompt-all-in-one使用。意外と使われてない？
- **828**: comfyui新環境作成でモデル消去ミス。
- **830**: 別環境構築/モデル退避推奨。
- **833**: EasyWan2.2→SmoothMix使用でI2V満足。Video2VideoのWF/モデル人気は？

#### nano-banana / Banana Pro関連
- **640**: banana側が自発的にエロ寄せ（規制懸念）。
- **644**: バナナプロ公式アドレス依頼（Google検索で偽物多し）。
- **646**: Grokimage.ai偽物ビジネス（動画出るがGrok無関係）。
- **648**: 公式フィルター厳しく外部API必須。
- **650**: Geminiアプリ（思考モード/3Proモード）でNano Banana Pro生成。
  - **理由**: サクッと使いたい場合に便利。
- **653**: フォトショbananaproでパンツ出す一苦労。
- **656**: PROをAPI使用（AIstudio課金APIキー？）。
- **668**: Googleアプリから外部APIでモデレない？

#### A1111 / webUI関連
- **662**: WebUI（Forge系）大好きっ子向けにForge Neo良い。
- **758**: A1111からComfyUI移行（オートコンプリート問題）。

#### その他ツール言及
- **735**: Forgeで1024x1496生成予定（スペック相談）。
- **738**: DMD2 4stepで高速化（4060Ti/3070で10秒2-3枚可能？）。

**抽出まとめ**: ComfyUIが圧倒的に多く、UI不安定/カスタムノードトラブル/ワークフロー最適化/ローカルvsWeb/API課金が主話題。Banana ProはAPI経由のエロ生成/フィルター回避で言及（偽物注意）。Forge/WebUIはComfyUI代替として軽快さが理由。理由抽出時は「時間短縮」「安定性」「課金不要」「馴染みやすさ」など効率面中心。SUPIRは未言及。