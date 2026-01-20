### 抽出された「ツール」に関する話題一覧

ログから生成AI関連の「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-bananaなどに類似する画像/動画/学習/拡張ツール、ControlNet, SAM3, ADetailer, i2i, LoRA学習ツールなど）を抽出。モデル（NovelAI, Pony, illustrious系, Noobai, FLUX, Wan, Qwenなど）の話題は除外。ツール名ごとにレス番号と内容をまとめ、選ばれている理由（利点）が明記されている場合は併記。

#### ComfyUI (comfy)
- **73**: ComfyUIのサポートが手厚い。公式テンプレ開くだけで動く（導入簡単さが理由）。
- **75**: ComfyUIデフォルトのFP8はミドルスペック向き、無印(BF16)をLTX-2公式からDLしてPRO6000使い切る。
- **146**: ComfyUI本体のアプデが必要（EasyWan22のSmoothMixV2で真っ黒になる問題解決のため）。
- **148**: Easyの00-I2v_ImageToVideo.json（ComfyUI WF）が真っ黒になる問題。
- **181**: ComfyUIに一度手を出して挫けた（漫画作成の習得コストが高い）。
- **183**: ComfyUIをこねこね（ノード操作）する必要性（オリジナルキャラLoRA作成で）。
- **191**: comfyuiはプロンプト覚えるより楽（変態じみたこと以外は複雑でない）。
- **204**: ComfyUI妄撮ノード作成（nano-bananaの妄撮プロンプト開発関連）。

#### sd-webui-traintrain (webUI系LoRA学習ツール)
- **58**: sd-webui-traintrainのBranch ver4で動く（赤ちゃんユーザー向け呪文で起動）。
- **63**: 拡張版じゃないとaddift目的でまともな結果にならんバグあり（拡張版推奨）。
- **64**: sd-webui-traintrainのinstall.pyでtorchao読み込み、ブランチでtorchao前を探す（バージョン問題解決）。
- **74**: webui-traintrainのBranch verをstandaloneに適用（ADDifT学習で効果確認、torchao/pytorchバージョン合わせの発想外）。
- **102**: webuiにtraintrain入れてADDifT作ったら変化した（効果確認）。

#### SAM3 / sam3
- **28**: SAM3が一番楽、マスク余裕調整で柔軟（背景維持+人間検出+detailerで書き換え）。
- **76**: sam3ほんま便利。
- **93**: sam3でリアル系face指定時唇マスクしてくれん時あり。
- **221**: 人間検出はSAM3使うべき（bbox型がないseg型代替）。

#### ADetailer / adetailer
- **34**: adetailerでhuman検出、本命だけマスク反転+書き直し（SDXL位置ランダム化アイデア）。
- **61**: ghostxlで出してadetailerをillustrious系で（位置調整後）。
- **220**: ADetailerに人間検出モデルbbox型探し（seg型はある）。

#### ControlNet / controlnet
- **20**: controlnet使って下絵で人物寄せる（SDXLローカル位置寄せ）。

#### i2i (img2img)
- **20**: i2iで領域指定/下絵/SAM修正（SDXL位置寄せ/維持）。

#### nano-banana
- **204**: nano-bananaの妄撮プロンプト開発（AntigravityとComfyUI妄撮ノード作成）。
- **205**: nano banana proが強すぎ（SFWでやる気削がれるほど優秀）。

#### Style-Bert-VITS2 (音声合成ツール)
- **21**: Style-Bert-VITS2ディレクトリ内でDockerfile置いてdocker build（TextToSpeech起動）。
- **65**: Style-Bert-VITS2音声をInfiniteTalkでしゃべらせる（動画+音声合成）。

#### InfiniteTalk
- **65**: WanベースでInfiniteTalk使用（Style-Bert-VITS2音声で動画しゃべらせる）。

#### Kohya_LoRA_param_GUI (LoRA学習GUI)
- **144**: 最新1.15.1.2でLoRA学習開始、xformers未インストールエラー（インストール時に入れてほしい）。

#### BooruDatasetTagManager (タグ付けツール)
- **106**: BooruDatasetTagManagerでタグ付けに切り替え、sd-script未導入（ミス大幅減）。
- **108**: BooruDatasetTagManager楽（表計算ソフト的に編集）。

#### antigravity
- **130**: antigravityが細かいcss修正苦手（スクショ何度見せても直せない、次の進化期待）。
- **204**: AntigravityとComfyUI妄撮ノード作成（nano-banana妄撮プロンプト関連）。

#### EasyWan22 / Easyrefoge (ComfyUI WFツール)
- **129**: Easyrefogeでpanties around one leg問題解決（パンティ2枚問題）。
- **143**: EasyWan22のワークフローでSmoothMixの新しいやつが真っ黒（いじる箇所不明）。
- **148**: Easyの00-I2v_ImageToVideo.jsonが真っ黒（配布元WFは動く）。

#### その他のツール言及 (単発/マイナー)
- **69**: WanVideoWrapperノードを中心にWF組む（場面切り替えプロンプト指定、背景シームレス）。
- **70**: WanVideo ImageToVideo Encodeノード重要（Start/End指定）。
- **171/173**: ggufモデル使用でSmoothMixV2解決（EasyWan22で質低下不明）。

これでログ全体からツール関連話題を網羅。理由（便利さ、簡単さ、バグ回避、代替性など）が明記されたものは括弧内に記載。モデル名（Wan, LTX-2, ghostxlなど）はツールの文脈でも抽出除外。