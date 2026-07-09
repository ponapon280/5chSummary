**抽出された「ツール」関連の話題（モデル話題は除外）**

ログから生成AI関連の**ツール**（ComfyUI/comfy、WebUI系、関連ユーティリティなど）に関する話題をすべて抽出しました。モデル（NovelAI/NAI、illustrious系、FLUX、Wan、Qwen-Image、anima、Z-Image系、LTX系）の話題は除外しています。  
**例外としてQwenシリーズは画像生成以外（VL/キャプション/LLM連携など）を抽出**しています。  
ツール選択理由がある場合は特に明記します。

### ComfyUI（comfy）関連
- **477**: ComfyUIでのエロ利用について細かく解説したブログを共有。
- **505**: Krea2でLoRA使用時の遅延対策としてCUDAをcu124→cu130に変更。ComfyUIは最新版を使用して改善（15分→3分程度）。
- **506**: StabilityMatrixはComfyのアプデの度に自動的にrequirementsを叩く。
- **527**: LM Studioを入れてComfyUIとの連携を確認。
- **535**: Comfy-Orgはチーム（企業）開発。Forge NeoはComfyUIの機能・ソースを流用して実装することが多い。
- **575**: WebUI Forge Neoを試したがError連発・UIがゴチャゴチャして見にくいためアンインストールし、ComfyUIに戻った。**理由：直感で操作しやすい**。
- **577**: ComfyUIのtaggerノードでしきい値調整（デフォ0.35/0.85推奨）を説明。
- **584**: comfyanonymous（ComfyUI開発者）がテンプレWFのデフォルトモデルをint8 convrotに変更すると発言。kijaiとともに二大ツール開発者として言及。
- **608**: convert_to_quantをhermesに使わせて自身で変換。z_image turboなどで生成速度向上。
- **651**: ComfyUIのマルチGPUで生成高速化を提案（4070ti追加など）。

### WebUI / Forge Neo関連
- **454**: Forge Neoを入れた。クソ早い。周回遅れだが捗る。
- **487**: ForgeNeoがINT8 ConvRotに正式対応。拡張を入れればWebUIから簡単に変換できて楽。Anima・ZITなどは自分で変換確認済み。fp8済みのものは元モデル確保が必要。ZITは5GBくらい縮む革命。
- **530**: ForgeNeoの更新が早い理由を質問。
- **535**: Forge NeoはHaoming02一人の個人開発（たまに野良PRあり）。ComfyUIの機能・ソースを流用。ゼロからではないが凄い。
- **559**: forge neoにもint8が下りてきてようやく話題についていける。
- **563/574**: int8 convrotはRTX40以降でもfp8より速度・精度上。Forge Neo開発者のヤオミン（Haoming）はfp8をお墓に入れた。
- **575**: Anima用にWebUI Forge NeoをわざわざインストールしたがError（アセーショナル/ランタイム）連発・UIゴチャゴチャで最悪。アンインストールしてComfyUIに戻った。**理由：ComfyUIの方が直感操作しやすい**。
- **584**: Haomingニキ（Forge Neo）がfp8 scaledを墓に埋め、comfyanonymousがint8をデフォルトにすると発言。kijaiがint8をアップしまくり。二大ツール開発者が推している。

### StabilityMatrix関連
- **506**: StabilityMatrixはcomfyアプデの度に自動的にrequirementを叩く。

### LM Studio / LLM連携ツール関連
- **527**: LM Studioを入れてComfyUIでの連携確認。Gemma4（通常版/規制回避版）の違いも確認。画像を読ませても直接的表現が少ない出力になる問題（体位が出ないなど）。
- **572**: taggerとLM Studioの間にタグ連結ノードを挟み、ユーザープロンプトに放り込むワークフローを構築。Oppai Oracle v1.1を使用したがタグ過多でLLMがエラー。
- **579**: LM StudioのLocalServerでコンテキスト長をVRAM余裕があれば上げる提案。

### Tagger / キャプション関連ツール
- **537/548**: エロ画像分析はDanbooru学習のTaggerモデルの方がLLMより賢い。WD Taggerなどで出したタグ（スペース/アンスコ抜き）を規制解除版LLMのプロンプトにフィードして「これらのキーワード使って画像をdescribeして」が良い。
- **572**: Oppai Oracle v1.1（最新tagger）を使用。タグ過多でLLMエラー。
- **577**: taggerノードのしきい値調整で出力タグを抑える。

### 変換・量子化・ダウンロード関連ツール
- **487/595**: INT8 ConvRot変換。ForgeNeo拡張でWebUIから簡単。変換ツールにはqwen3などのプリセットもあり、TE側もint8化可能で普通に生成できる。
- **555/560/561/563/567/570/571/573/574/581/584/585/589**: int8 convrotの議論（速度・精度がfp8より上、RTX30以前で恩恵大、40/50でも有効、NVFP4比較など）。Haoming/kijai/comfyanonymousが推している点が信頼源。
- **591/594/598/600/607**: int8_convrot版QwenImageEdit2511のダウンロード失敗対策。Hugging Faceアカウント＋アクセストークン＋huggingface_hub（hf download）で解決可能。チャピーにツール作らせる方法も。別ソースから落としてRTX4070Tiで0.6s/it高速化確認。
- **608**: convert_to_quantをhermesに使わせて自身で変換。

### その他ツール・プラットフォーム
- **472**: LMArenaを試した（zen-bear-v3などQwen系が出てきたが、ツールとしてLMArena使用）。
- **557**: Qwen3VL 8B NSFWを画像からプロンプト取得・生成時に使用（キャプション用途）。拒否対策でシステムプロンプト必要。フェラ系で長文吐く時あり。
- **580**: VLとして規模大きめのgemma/qwenキャプション特化やjoycaptionを使用。再現度が高かったのはjoycaption。
- **634**: 中華モデルなら公式契約よりopenrouterなどの方が良い提案。

### 選択理由のまとめ（特に強調されていたもの）
- **Forge Neo**: 生成がクソ早い・捗る。INT8 ConvRot対応でWebUIから簡単変換可能。更新が早い（個人開発ながらComfyUI流用）。
- **ComfyUI**: 直感で操作しやすい（Forge NeoのError多発・UIゴチャゴチャを嫌って戻る）。最新版でCUDA更新と組み合わせて高速化。StabilityMatrixでアプデ時の依存関係自動処理。マルチGPU対応。taggerノードなど柔軟。
- **INT8 ConvRot関連変換ツール/拡張**: 速度・精度がfp8より優れ、ファイルサイズ削減（特にZITで5GB縮む）。ForgeNeo拡張やconvert_to_quantで手軽。主要開発者（Haoming, comfyanonymous, kijai）が推進。
- **LM Studio + ComfyUI連携 / Tagger**: 画像分析→自然言語キャプション生成のワークフロー構築に有用。タグ過多対策やしきい値調整が必要。
- **Hugging Face関連（hf downloadなど）**: ダウンロード失敗時の確実な取得手段。

これらがログ内のツール関連話題のほぼすべてです。モデル固有の性能・LoRA・生成結果の話は除外しています。