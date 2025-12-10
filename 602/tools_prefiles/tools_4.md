### 抽出された「ツール」に関する話題

ログから、生成AIに関連する「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana など）のみを抽出。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwen など）に関する言及は除外。ツールの選定理由や関連する具体的な言及をレス番号付きでまとめ、各ツールごとに整理。起動オプションやカスタムノードもツールの使用・設定として含む。

#### ComfyUI (comfy) 関連
- **651**: simplecomfyuiでqie2509の砂嵐が発生、stabilitymatrixに切り替えたら発生せず。相性問題と推測。
- **653**: matrix環境（stabilitymatrix）で試す。
- **659**: ComfyUI v0.3.71でWF実行、easyimgeditのComfyUI環境に問題あり？ D2 Send Eagleのカスタムノードを使わず普通のSave Imageに置き換えで生成成功。
  - **理由**: カスタムノードが問題の可能性、標準ノードで問題解決。
- **660**: 最後の画像保存で変なノード使用？ 普通のSaveImageノード推奨。Kサンプラーに入るlatentをStep3 - Image Sizeに交換、ノード選択でバイパスのオンオフ表記あり。
- **664**: easyimage環境で生成結果が砂嵐。
- **668**: 起動オプションの--fastを消したら砂嵐治った。
- **674**: 砂嵐は起動オプションのfastだけ消せばOK。
- **675**: QIE2509はsageattentionと相性悪い。起動オプションに--use-sage-attentionが入ってるなら消す。KJのsageattentionノードは起動オプション不要で動作。
- **676**: --fastだけだとfp16_accumulation, fp8_matrix_mult, cublas_ops, autotuneが自動有効。--fast fp16_accumulationと使う場合のみ指定。
- **678**: simpleComfyUIでQIE25O9のfp8使うと必ず砂嵐、Q8やbf16では発生せず。
- **683**: まったく同じ現象、bf16使ったら正常（ただしbf16は量子化方式でツール直接関連薄いがComfyUI環境）。
- **684**: fast消したら砂嵐改善、上手くいった。
- **689**: -fastオプション切ったらOK。
- **716**: ComfyUIがでかいモデルで60GB確保ガバ、Windowsのコミット値は物理メモリ＋ページファイルの合計。
- **718**: --fast: fp16_accumulation, fp8_matrix_mult, cublas_ops, autotune有効。--use-sage-attentionで演算時量子化高速化。ローダやPatch Sage Attention KJ, Model Patch Torch Settingsで手動設定可能。
- **728**: ComfyUIのメモリ確保ガバ説明。
- **741**: stable video infinity (SVI)のgithubからサンプルワークフローJSON落としてモデル/LoRA入れ即動作。wan video～, video combineノードは動画生成環境なら既に入ってるはず。VRAM16GBでOOM出たのでfp8差し替え。
  - **理由**: 即動作で簡単、追加ノード不要。
- **775**: ComfyUIアップデートでキャンセルボタン常時表示復活（クレーム多かった）。
- **811**: painterlongvideoのwf使用中、シード固定でガチャれず。ComfyUI分からん。
- **812**: PainterLongVideoフォルダにサンプルワークフローあり。シード下のfixedをrandomに変更でランダム化。
  - **理由**: サンプルWFで簡単にシード制御。
- **831**: comfyui v0.4.0出たが様子見。
- **846**: ComfyUIアップデートでFP16処理によるLoRA演算高速化とメモリ使用量削減（@comfyanonymous）。

#### stabilitymatrix 関連
- **651**: simplecomfyuiで砂嵐発生したが、stabilitymatrixで動かしたら発生せず。
  - **理由**: simplecomfyuiとの相性問題回避。
- **653**: matrix環境持ってるから試す。

#### A1111 関連
- **795**: A1111が大幅進化（Comfy避けてる勢に朗報）。
  - **理由**: refoge/classic/neoに追いつく進化で、ComfyUI避け勢向け。
- **806**: refoge/classic/neoはバグだらけ（A1111拡張機能？）。

#### nano-banana 関連
- **686**: nanobananaいいなぁと思ってたけど右下にマーク入ってる。
- **792**: bananaが空いてきたが雑コラに。

#### その他のツール
- **easyimgedit / easyimage / easywan22**:
  - **659**: easyimgeditのComfyUI環境に問題？
  - **664**: easyimage環境で砂嵐。
  - **750**: ガラスキスならeasywan22あり。
- **Zimage**:
  - **691**: Zimageで自然言語or構造式プロンプトでのLoRAノウハウ作成開始、Base早く来てくれ。
- **Pixel Snapper**:
  - **790**: Pixel Snapperでwanアニメ全フレーム適用試したが画像サイズ微妙違って失敗。imagemagickより便利？
  - **796**: pixel snapper便利、imagemagickでフィルター指定面倒。色数指定だけで最適解像度自動。
    - **理由**: imagemagickより簡単・自動最適化。
- **imagemagick**:
  - **796**: imagemagickでフィルター/ティザー指定面倒。
- **LM Studio**:
  - **724**: LM Studioに自然言語プロンプト任せる。
- **SVI (stable video infinity)**:
  - **732**: stable video infinity見たが入れ方わからん。
  - **741**: SVIのgithubからJSON落として即動作（上記ComfyUI参照）。

これでログ内の全ツール関連話題を抽出。モデル名（Qwen, Wanなど）は一切除外し、ツール使用時のトラブルシュートや選定理由を中心に記載。