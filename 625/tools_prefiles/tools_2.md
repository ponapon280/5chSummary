### 抽出された「ツール」関連話題一覧

ログから生成AIの「ツール」（ComfyUI, A1111, Forge neo, StabilityMatrix, Kohya_ss, SageAttention, Detailerノード群など）に関する話題をすべて抽出。モデル（Anima, リアス/illustrious, NAI, Noobaiなど）言及は除外し、ツールの使用・比較・トラブル・導入方法などに限定。ツール選択理由が明示されている場合を★で強調。

#### ComfyUI関連
- **261**: ComfyUIだと自作AnimaLoRAが割と普通に出力されるが、Forge neoだとちゃんと出ない。設定間違え？（ComfyUIがLoRA出力で優位？）
- **289**: ComfyUIアプデでQwen3-TTS/ARSが死ぬ。StabilityMatrixの影響疑うがポータブル作成・モデル/ノード移植・ジャンクションで対応。本家0.14.1 vs StabilityMatrixの0.14.2不整合。frontend書き換わりでグラフ/アプリモードボタン消滅。1.39.12に下げ復活。1.40.7でノード死。Qwen3系専用ComfyUI推奨。
- **300**: Comfy-Orgの更新漏れ？ comfyui_version.pyが"0.14.1"、gitタグv0.14.2。
- **308-316,319,321-325**: ComfyUIのポジティブプロンプトconcatがA1111のBREAKと同じ挙動か？（string concat vs conditioning concatの違い議論。ComfyUI標準ノードではBREAK無意味、カスタムノード(Shinsplat, smZNodes, clip-with-break)で可。Conditioning Concat/Average/Combineの違いはreddit動画参照。A1111 BREAKとComfyUI Concatは同等だが生成画像で差異出る可能性。75トークン処理のSD特有挙動？ AnimaでBREAK可否？）
- **334**: ComfyUIでQwen3-TTS/ASR動かす最適組み合わせ（flybirdxx版TTS + DarioFT版ASR + transformers 4.57.6）。RTX5080環境で安定。
- **338**: TTS/ASR共にDarioFT版使用。死んだらマネージャでQwen3-TTS Try Fix。
- **340**: sam3(girl)->Grow Mask With Blur->InpaintModelConditioning+Differential Diffusionでanimaインペイントテスト。
- **341-342**: sageattention導入試行中、comfyuiフォルダ空っぽに（バックアップ必須）。using sageattention出るが速度変わらず効いてない？
- **344,347,350,352,379,381**: SageAttention導入方法議論。StabilityMatrixでGUI完結/3クリック（Package Commands > Install Triton and SageAttention）。Matrixで上手くいかずComfy Easy Install使用（anima専用でSDXL資産不要、23%速くなる★）。50xxシリーズでも可（ただしInstall Nunchaku失敗）。
- **353**: qwenのload diffusion model/unet loader/load check pointが分かれていて不便。
- **364**: animaでdetailerかける方法？ マスク+InpaintModelConditioning+Differential Diffusion？
- **368**: Detailerノード普通にある。crop&stich使用。
- **369**: civitaiにdetailer用WF（workflow）あり。
- **372**: impact-packのSEGS Detailer使用（Sampler含め多用途）。
- **373**: animaでface detailerかけるとノイズだらけ。SDXLモデル接続必須？
- **376**: ComfyUI version: 0.14.2環境。Python 3.13に変えたら生成速度早くなる？
- **428**: SEGS Detailerは問題なし、FaceDetailerで問題発生はセッティングか。

#### A1111関連
- **308-316,319,321-325**: A1111のBREAK挙動とComfyUI concat比較（上記参照。conditioning再定義？ prompt-control必要？）。

#### その他ツール
- **261**: Forge neoで自作AnimaLoRA出ない（ComfyUI優位）。
- **289,300,344など**: **StabilityMatrix**多用。ComfyUIバージョン管理/パッケージ更新でrequirements.txt実行（Python Dependencies Override推奨）。SageAttention/Triton簡単インストール★（GUIで高速化）。
- **339**: anima用画風LoRA作成にKohya_ssで良いか？
- **418**: kohya_ssのAnimaフォーク発見。

#### ツール選択理由の明示例（★）
- ComfyUI: LoRA出力安定（261）、BREAK/concat柔軟（308〜）、Detailer/Inpaintノード豊富（340,364〜）。
- StabilityMatrix: SageAttention簡単導入（3クリック、GUI完結★）（344,350,352,381）。
- Comfy Easy Install: Matrix失敗時の代替、anima専用で高速化23%★（347,379）。

これでログ内の全ツール話題を網羅。モデル/Anima固有話題（257,262,288など）は除外。