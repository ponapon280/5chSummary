### 抽出された「ツール」関連話題

ログから生成AI関連の「ツール」（ComfyUI, A1111/webUI, SUPIR/nano-bananaなど画像生成/処理ツールに該当するもの、またはそれに準ずる拡張/補助ツール）に関する言及をすべて抽出。モデル（NAI, Pony, illustrious/Wai, Noobai, FLUX, Wan, Qwenなど）関連は除外。TTSツール（T5Gemma-TTS）やレンタルGPU（runpod）、LLMツール（LMStudio）などは生成AI補助ツールとして関連性が高いものを含む。ツール選択理由が明記されている場合のみ記載。

#### ComfyUI (comfy) 関連
- **102**: ComfyUI0.5.1はDistorchMultiGPUは大丈夫そう？
  - MultiGPU対応の確認。
- **158**: ComfyUIのワークフロー作成について... comfyui-easy-useのFor Loopノード... String Selector... 複数のプロンプトをリスト化してインデックスつけて、ループ毎にインデックスをシフト... 入力エリアはプロンプト毎に分けたい。
  - PainterLongVideoで長尺動画生成時のFor Loopノード活用、プロンプト動的変更方法の相談。
- **163**: >>158 For Loopノードもあるんか... Any Index Switch はどうやろ？CONDITIONを入力に繋げれば CLIP Text Encoderを整数インデックス切り替えられそうンゴね。
  - For Loop + Any Index Switchノード提案。
- **174**: ワイもComfyにLMStudio導入 プロンプト作成がクッソ楽になってええな。
  - LMStudioをComfyUIに導入し、プロンプト作成が楽になった理由で使用。
- **176**: ワイも好きな画像達をバッチでVLMに読ませてプロンプト書いてもろて...（ComfyUI文脈）。
  - VLM（Vision Language Modelツール？）でプロンプト自動生成しComfyUIで全自動生産。
- **177**: >>158 Imapct-PackのSwitch(Any)とか。selectにindexを繋げばできそう。
  - Impact-PackのSwitch(Any)ノード提案。
- **180**: LMstudio組み込めばgrokとのモデルの違いこそあるものの、ローカルで完結させられる。
  - ComfyUI + LMStudioでローカル完結を理由に使用。
- **185**: LMStudio自体はComfyUIとは別に起動しとかなあかんけどデフォルトでシステムトレイに常駐するから気にならん。
  - ComfyUI併用時のLMStudio運用Tips。
- **186**: LoRAキャプションは処理に超絶時間がかかるComfyUI-QwenVLノードでバッチ処理で放置 生成時の相談はチャッピーでええか。
  - ComfyUI-QwenVLノードの使用（処理時間長さを指摘）。
- **188**: >>163 >>177 サンガツ! 時間取れたらワイもWF組んでみるかぁ。
  - ComfyUI Workflow（WF）組立。
- **189**: >>163 >>177 サンガツや、両方いけたで... これができると何かの役に立つ気がするんで、色々模索してみるわ。
  - For Loop/Any Index Switch/Impact-Packの実装成功報告。
- **190**: comfyuiに求めてるのはこのワークフローならvramいくらで動かせますよとか言う指標が欲しい lm studioにあるようなの。
  - VRAM使用量指標の要望（LMStudioの指標機能を比較）。
- **191**: ワイも最近LMStudio試してみたけど、PLaMo翻訳に感動したわ ローカルで軽快にエロ文書翻訳してくれるのは色々捗るで。
  - ComfyUI文脈でLMStudioの翻訳機能（PLaMo）が軽快・ローカルで捗る理由。
- **197**: >>158 少し前にSVI2.0を紹介してる動画を見たら、String from Listってのを使って一つのmultiline stringからindexでリスト構造にしてたな。
  - String from Listノード提案（SVI2.0動画参考）。
- **211**: ComifyUIでファイルをドラッグドロップした時に パスの文字列取得出来るノードってありますかね？
  - ファイルドラッグドロップ時のパス取得ノード相談（ComfyUIタイポ）。
- **216**: 自決しました。そもそもブラウザの約束でファイルそのものは取ってもいいけどパスは取っちゃダメ... Comify自体が画面全体で強力なイベントハンドラをもってる。
  - ドラッグドロップのパス取得難易度説明（セキュリティ/実装理由）。
- **226**: Load Image ノードくらいしか使ったこと無い... ComfyUI\inputのパスが取得できれば... 自前のcustom node側で操作できるパスにテンポラリファイルとして複製。
  - Load Imageノード + カスタムパス処理提案。

#### webUI / A1111 関連
- **201**: あかーん！GPUが新しすぎるってエラーが出よる…… requires device with capability <= (9, 0) but your GPU has capability (12, 0)... SD1.5とSDXLで出力できたってことで。
  - xformersエラー（5090 GPU非対応）。
- **218**: >>201 webUIの何かやと思うけどxformersはsageAttentionが出るまでのツールかなと思ってる、今は後者でええかと思うで。
  - webUI + xformersの互換性指摘（一時ツールとして位置づけ、後継sageAttention推奨）。

#### nano-banana 関連
- **30**: >>27 無論 gemのデフォルトツールもバナナや。
  - Geminiのデフォルトツールとしてnano-banana（バナナ）を挙げ使用。

#### その他の生成AI関連ツール
- **49**: >>24 T5Gemma-TTSやで リファレンスなしでテキストは↓... Linux向けだけどWSL2で導入できるで 前スレの並列推論のやつやけど同時に複数出せるからガチャの確認がやりやすい。
  - T5Gemma-TTS：並列推論でガチャ確認がやりやすい理由。WSL2導入容易。
- **57**: T5Gemma-TTSの学習やりたいけど音声系の学習ってどうやればいいんだろう？ readmeに学習方法書いてあるけどサッパリ分からない。
  - T5Gemma-TTS学習方法相談。
- **94**: 生成しながらとかゲームしながら学習したいときrunpodはたまに使ってる データの転送がちょいめんどいけど便利ではある。
  - runpod：生成/学習時の併用で便利（データ転送めんどいが）。
- **113**: 最近話題のなんちゃらTTSがvram12gbで動きますとかならワイも遊べるんやがな。
  - TTSツール（T5Gemma-TTS想定）のVRAM12GB動作情報要望。
- **194**: T5Gemma-TTSのバッチ生成を参考にしてLlasa-Captionsにも実装できたで 無料のGeminiで出来たし気になる人はやってみるとええで。
  - T5Gemma-TTSバッチ生成を参考にLlasa-Captions実装（Gemini無料で可能）。

**抽出まとめ**: 主にComfyUIのワークフロー/ノード活用・拡張（LMStudio併用）が最多。理由として「プロンプト作成が楽」「ローカル完結」「軽快翻訳」「VRAM指標」など効率/利便性重視。webUIはGPU互換性問題、nano-bananaはGeminiデフォルト、TTS/runpodは並列/学習便利さが理由。ツール選択理由は明記箇所のみ記載。