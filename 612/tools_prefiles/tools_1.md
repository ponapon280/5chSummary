### 生成AI関連「ツール」に関する話題抽出

ログから「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-bananaなど）のみを抽出。モデル名（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）は一切含めずスキップ。ツールの言及箇所をレス番号順にまとめ、各話題の要点と選ばれている理由（明記されている場合）を記述。

#### ComfyUI関連
- **11**: ComfyUI 0.8.2でFP4の恩恵により5070Tiで生成時間が140秒→110秒に短縮。ただし連続生成（SVI）で生成停止エラーが頻発（VRAM16GB vs モデル20GBが原因か）。0.7.0の安定環境推奨、または連続一発出しを避けた方式を検討。**理由**: 時間短縮効果が高いがVRAM負荷で不安定。
- **12**: ComfyUIのジョブキューで「Asset not found in media assets panel」エラーが発生、どう対処するか。
- **19**: 自作ノード（Size_Tools.py）の共有。custom_nodesフォルダに_init_.pyとSize_Tools.pyを配置し再起動で使用可能。スタート画像ごとに動画サイズ設定の手間を省くためのもの。**理由**: 手間削減のためのカスタマイズしやすさ。
- **27-28,31-32,34**: Radeonユーザー向けComfyUI最適化テクニック（省VRAM・高速化）。model_management.py, sd.pyのコード修正パッチ共有（cudnn/MIOpen有効化、VAEのpytorch attention有効化、VAE_KL_MEM_RATIO=1.0固定）。環境変数AMD_ENABLE_MIOPEN_ENV=1でRDNA3/4対応。**理由**: Radeon（Geforce比で挙動違い）でVRAM消費・速度改善（7800XTでVAEエンコード/デコード大幅改善）。
- **39**: >>19の自作ノードを感謝。色んなサイズの画像を720p出力に統一する機能。
- **76**: Z-imageがComfyUI前提のため、WF（ワークフロー）を整える必要。
- **77**: ZI対応でSDXL用WF作り直しが必要で面倒。**理由**: ComfyUIのWF柔軟性が高いが更新対応が手間。
- **78**: 覇権モデルならA1111系でZ-image対応される可能性。
- **80**: ComfyUIのアプデで別物級の変化可能性。
- **85,96**: ForgeNeoがZ-Image turbo対応済み。
- **101**: >>27の最適化（2,3番目）でRX9070でzimage-turbo/SDXL生成が1.5秒速化。
- **103,106**: 「Comfy赤ちゃん」（ComfyUI初心者）でサブグラフが見やすく便利だが、setノードなどが使えなくなる問題。
- **111**: ComfyUI公式WFがサブグラフで一階層潜り展開/配置が面倒。
- **113**: 自作カスタムノードエラー→ComfyUI git pullアプデでワークフローJSONがnull上書きされる問題。
- **115**: 自作カスタムノードでエラー発生時の対処（ComfyUI落としてコード修正→アプデ）。
- **116**: ComfyUIのためにpip install（requirements/whl）する行為を実質「ゲーム」と例え。
- **117**: ComfyUIを「ノード配線ゲーム」と表現。
- **145**: ComfyUIアプデ後、sageAttentionインストール不可（Python3.12が原因で3.11推奨）。
- **150**: ROCm用ワークアラウンド（最適化パッチ）が仕様解消後も残すと性能低下の懸念。
- **163**: 画像メタにComfyUIのWFが埋め込まれる問題（CNローダーで無臭入る恐れ）。
- **206-207**: ComfyUIの画像メタ参照はinputフォルダ依存。他人PCではblank表示のため安全。

#### その他のツール関連
- **186-189**: Rife TensorRTノードがインストール/アップデートでmissing。StabilityMatrix使用時、requirements.txt/onnx→tensorRT変換スクリプト修正、CUDA/PyTorchバージョン対応、たけのこニキのフォーク版手順が必要。**理由**: 動画関連高速化のためだがインストールが環境依存で煩雑。
- **A1111**: 78で言及のみ（Z-image対応可能性）。

**抽出まとめ**: 主にComfyUIが圧倒的に多く、省VRAM/高速化、カスタムノード/WF柔軟性、Radeon最適化が選好理由。初心者向け見やすさやアプデ頻度が課題として挙がる。他ツール（ForgeNeo, StabilityMatrix, Rife TensorRT）は補助的に言及。理由が明記されていない話題は省略。