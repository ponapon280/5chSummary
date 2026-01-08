### 抽出された「ツール」関連話題

ログ全体から、生成AI関連の「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-bananaなどに相当するもの）のみを抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）関連は除外。ツールの言及箇所、内容、選ばれている理由（明示的な場合）をレス番号付きで列挙。重複言及はまとめて記述。

#### ComfyUI (comfy)
- **35**: DaSiWa v8.1で黒画像問題発生時、「Comfyのポータブルを新規で用意」し、高速化依存パッケージ（torch-2.9.1+cu130, sageattention2.2.0, triton_windows-3.5.1.post23）を追加インストール。DaSiWa作者のWFで正常動作確認。**理由**: EasyWAN22環境のv7は動作するがv8.1で黒画像のため、新規ポータブル環境構築で高速化対応。
- **60**: ComfyUI-Rife-Tensorrt (GitHubリンク)。**理由**: 言及のみ（前スレ関連）。
- **61**: EasyWan22で構築しDaSiWa8.1生成可能（バージョンロック解除し>>35環境化）。
- **63**: Ver手動変更時はEasyWan22より「新環境立ち上げてWFだけ持ってきて」ComfyUI使用がスッキリ。
- **82**: 「comfyのマスクのブラシサイズがアプデ後バカでかサイズ」。
- **89**: StabilityMatrixからComfyUI起動せず（新規インストール後Launchで即終了）。**対処試行**: ログ確認、venv activate/pip installなど。
- **94**: StabilityMatrix+ComfyUIアップデート同時で起動不可→NVIDIAドライバー最新版更新で解決。**理由**: 原因不明だがドライバー更新でComfyUI起動可能。
- **99**: StabilityMatrixアップデートでComfyUI 6→7移行時同様症状→venv activate + pip install -r requirements.txt / PyYAMLで解決。
- **100**: ComfyUIのログファイル（Data\Packages\ComfyUI\user）確認推奨。
- **105**: StabilityMatrixはComfyUIの補助ツール。GUI外でvenv activate/pip操作やpython main.py起動可能。**理由**: 自動更新が余計なお世話（Pytorch巻き戻しなど）になるが、生ComfyUIとトラブル対処同等。
- **164/194**: StabilityMatrix+ComfyUI 0.7.0で起動不可→>>94（ドライバー更新）で解決。自作WF動かず、特定ノード修正（comfyui-prompt-reader-node, z-tipo-extension, was-node-suite-comfyuiのRandom Number, ComfyUI_Comfyroll_CustomNodesのCR Text List）。
- **182**: 「comfyとqwen2512初めて触ってる」。IPAdapter使用検討（ノード多すぎて不明）。
- **192**: ComfyUI公式テンプレのQwen2511（3つ画像参照）で画像内人物読み込み可能だが、二次元イラスト画風死ぬ。**理由**: 簡単だが実用圏外（顔/手がQwen風に）。
- **196**: StabilityMatrixアップデートでPytorch cu128→cu130になり古いNVIDIAドライバーでComfyUI動かず。**対処**: ドライバー更新 or Pytorch cu128ダウン。
- **198**: StabilityMatrixのPytorch自動更新でSageAttention/Rife Tensorrt死ぬ。
- **211**: ComfyUIへのSVI実装は実験的で本領未発揮。

#### EasyWan22 / Easy (EasyWAN関連ツール)
- **35**: EasyWAN22環境でDaSiWa v7動作するがv8.1で黒画像。
- **53**: Sage+tensor両立構築で心折れ「easyで生成再開」。
- **61**: 「ワイ環はEasyWan22で構築しとるけどDaSiWa8.1で生成できてる」（>>35環境化）。
- **62**: 「EasyWanで対応できないモデル」。
- **63**: Ver手動変更時はEasyWan22より新環境+WF移行推奨。
- **118**: 「ローカルはクオリティが低い(EasyWan22環境でQ4Mを使用)」と低スペクオリティ犠牲指摘。

#### DaSiWa
- **35**: v8.1で黒画像（EasyWAN22 v7はOK）。作者のWFでComfyポータブル環境確認。**理由**: 高速化（5060Ti 16GB+96GB RAMで560x720 16fps 81フレーム4ステップ初回160秒/以降140秒）。
- **61**: EasyWan22でDaSiWa8.1生成OK（バージョンロック解除+>>35環境）。

#### StabilityMatrix
- **89**: ComfyUI起動せず（Launch即終了、無エラー）。
- **94**: アップデート+ComfyUI同時で起動不可→NVIDIAドライバー更新解決。
- **95**: 問題時「package全部消してただのモデル倉庫」使用。
- **96**: 問題切り分け詰み（無言終了）。
- **99**: ComfyUI 6→7移行時コマンド（venv activate, pip install requirements.txt/PyYAML）で解決。
- **105**: ComfyUI補助ツール。自動更新がPytorch巻き戻しなど余計。自分でpip/python main.py可。
- **164/194**: ComfyUI 0.7.0で起動不可→ドライバー更新解決。特定ノード不具合。
- **196**: アップデートでPytorch cu130化→古ドライバー不動。**理由**: cu128互換必要。
- **198**: Pytorch自動更新でSageAttention/Rife Tensorrt死。

#### SAM3 (Segment Anything Model 3)
- **83**: meta個人情報入力でSAM3使用開始。「detailerが楽に」。
- **84**: 個人情報入力必須（嘘可）。
- **85**: NSFW検知されず使えず。
- **86-88,93,98,101**: 顔/手/小物/服/アクセサリー/男顔検出に使用。性器/乳首未使用。エロで1boy,1girl,sex生成OK（faceless可）。**理由**: adetailerより詳細検出楽（男顔隠れ時有効）。
- **236-237**: ダウンロード申請即許可（0.5秒後DL可）。

#### SageAttention (sage attention / sega attention)
- **35**: sageattention2.2.0 (tritonと併用)。
- **37**: sageattention 2.2.0post4。
- **53**: Sage+tensor両立構築失敗。
- **65**: 「セガアテンション2やsvi試してみたい」（zuntan兄貴待機）。
- **69**: 「sage attentionをsega attentionと書く人」。
- **74**: sega attention過去10スレ未確認。
- **198**: Pytorch更新でSageAttention死。

#### その他のツール
- **IPAdapter**: **182**: 画像内人物を読み込みでキャラ適用検討。「ノード多すぎて不明」。
- **Qwen Image Edit 2511 (QIE)**: **189**: 画像内人物読み込みに使用。**192**: ComfyUIテンプレで3画像参照可だが画風死。LoRA作成提案（ZimageEdit待望、16G VRAM可）。
- **Rife-Tensorrt**: **60**: ComfyUI-Rife-Tensorrt (GitHub)。**198**: Pytorch更新で死。
- **SVI / StoryMem**: **65**: svi試したい。**211**: SVI>StoryMem（延長崩れ少ない）。ComfyUI実装実験的。
- **ZimageEdit**: **192**: 16G VRAMでLoRA作成可、QwenImageEdit代替待望。

**抽出総括**: 主にComfyUI/StabilityMatrix/EasyWan22/DaSiWa周りのトラブルシュート・環境構築話題が中心。高速化/互換性/起動安定性が選定理由の多くを占める。SAM3はdetailer代替として検出精度で選ばれ。モデル関連（Wan/Qwenなど）は一切除外。