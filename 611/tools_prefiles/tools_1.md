### 抽出された「ツール」関連話題一覧

ログから「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana などインターフェース/拡張ツール）に関する話題のみを抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen など）関連は除外。ツールが選ばれている理由（高速化、互換性、使いやすさなど）が明記されている場合を強調。

#### ComfyUI (comfy) 関連
- **17**: 「ポータプル版かと勘違いしてたけどマニュアル版のcomfyUIインスコしてた・・・」  
  → ComfyUIのインストール版（マニュアル版/ポータブル版）の勘違い。
- **30**: 「comfyuiでhires.fixすると２回目のKサンプラー時に寝転んでいる人物が奇形になること多いんですが、解決できるノードや設定ってありますか？」  
  → ComfyUIのhires.fix使用時の問題解決相談。
- **32**: 「denoiseとかどうなってるのかエスパーするよりwf晒したら？」  
  → ComfyUIのワークフロー（WF）公開推奨。
- **42**: 「生成AI実行アプリのComfyUIがROCmへのネイティブ対応を果たし、AMD製グラフィックボードやAMD製SoCを搭載したマシンでの生成速度が大きく向上... Stable Diffusion XL(SDXL)では2.6倍、FLUX.1 [schnell]では5.2倍、WAN 14bでは5.4倍」  
  → **理由: AMD/ROCm対応で生成速度最大5.4倍高速化（RTX非依存で安価AMDグラボ対応が夢あり）**。
- **43-44**: 「結局LTX2のfp8はcomfyでVRAM16GBで動くんか？」「VRAM12GBでも動いたけどVAEデコードで LTXVAudioVAEDecode tuple index out of range」  
  → ComfyUIでのVRAM低減動作確認とエラー。
- **47-48,53-54,56,70,89,103,125,201-203**: 「comfui-sam3とcomfyui_sam3」「ハイフンで区切ってる方はプロンプトをカンマ区切りで複数入れられら」「sam3 nipplesでエラー」「masksを合成しないと最初（face）のほうしか効かない」「TBG-SAM3使っとるがカンマやと効かないけどandやと効く」「ComfyUI-SAM3よりComfyUI-Easy-Sam3ってやつの方が良さそうだ」  
  → ComfyUIのカスタムノード（SAM3系）の使い方/エラー/複数検出問題。**理由: 検出精度/複数プロンプト対応で選択（ただし融通利かず難易度高め）**。
- **57**: 「kohyaニキのguiをアップデートして汎用プリセットを確認したらオプティマイザがLionになってた」  
  → Kohya GUIのアップデート（学習ツール）。
- **59,61,62**: 「ComfyUI早くなったってマジ？ 5090でComfyUIやドライバ最新状態だけど特に変わった様子ないな」「ああAMDグラボの話」「ComfyUI 0.8.0 バージョンアップ激しいな」  
  → ComfyUIの速度向上/バージョンアップ確認（AMD特化）。
- **67**: 「comfyアプデ失敗するんで新しく入れ直した GTXなんでsamやtriton系は削除してnative wan2.2の30秒動画問題なく再生できた」  
  → ComfyUIアップデートとノード削除による動作安定。
- **68-69,81-82,96,115,122**: 「stability matrixのcomfyUIのモデルを、ポータブル版のcomfyUIで使う方法」「新しいcomfyuiで使いモデルのフォルダをmatrixで管理してる場所に指定」「extra_model_paths.yamlにパスを書く」「modelsフォルダごとシンボリックリンク」  
  → Stability MatrixとComfyUI（ポータブル版）のモデル共有方法。**理由: モデル管理の利便性（パス指定/リンクで移行容易）**。
- **71**: 「ComfyUI v0.8.0 でsage attention3に対応してくれるのはええんやけど機能するwhlどこ…」  
  → ComfyUI v0.8.0のsage attention3対応。
- **79,204-207,211**: 「ComfyUI(v0.8.0)起動時にcomfy_kitchenとかいうモジュールエラーが出る」「指定されたモジュールが見つかりません」「FP4用のモジュールだからRTX50以外なら無視してええ」「requireかけていけました」  
  → ComfyUI起動エラー（comfy_kitchen）。**理由: RTX50以外無視可、requirements.txtで解決**。
- **90,95,189-190,202**: 「pytorch version: 2.9.1+cu130 ComfyUI 0.8にうｐしたらcu128から130に」「ComfyUI推奨のPytorchVerがcu130」「comfy-kitchen integration(FP4の高速化？)とやらがPytorchのCU130が必要」「SageAttention3は≧12.8だから普通に動く」  
  → ComfyUIのPyTorch/CUDAバージョン互換（cu128/130）。
- **120-121**: 「ここからltx-2のi2vワークフロー落として... resizeimagemasknodeとかいうのが赤枠」「comfyuiアップデートは？」  
  → ComfyUIのWFエラー解決（アップデート）。
- **135,146**: 「comfyのアップデートしたいんやがcomfyUI managerってどこにあるんや」「githubや やり方はAIに聞くか翻訳すればええ」  
  → ComfyUI Managerの場所/アップデート方法。
- **147-154,168,171,174,184**: 「ワイはニキらの大半がComfyUIに移行してて感動」「AI壁打ちするとcomfy勧められる」「仕方なくcomfy使っとるだけ」「ワイはcomfyUIは動画だけ」「ComfyUIいずれ勉強しよう」「ワイはComfy気に入ったで 柔軟にパイプライン組めて自動制御」「グループでコンポーネント化」「Publish Subgraphでカスタムノード」「ComfyUIに移行して昨日でちょうど2年」  
  → **理由: 動画生成必須（避け通れず）、柔軟性/パイプライン自動制御、移行増加中（Forge/A1111から）**。
- **196**: 「EasyWanにtensorRTを入れた」「後処理のアップスケールとフレーム補間の部分だけ...TensorRTのバージョンを上げないとアカン」  
  → ComfyUIのTensorRT（EasyWan内）で速度向上。
- **213**: 「custom node manager調子悪い」「LTX系入れたら目的の半分ぐらいしか入って無い」  
  → ComfyUI Custom Node Managerの不調。

#### その他のツール関連
- **85-86,92**: 「reforgeとeasyWan2.2をインストールし直してる」「今日easywan2.2入れた」「cu128がインストールされない」  
  → reForge, easyWan2.2のインストール（ComfyUI拡張？）。
- **93,122,144**: 「stability matrixのcomfyUIのモデルを...」「StabilityMatrixのCivitai検索は昔からダメダメだったんだけどv2.15.5になってマトモに」  
  → Stability Matrixの検索/アップデート改善。
- **212**: 「マルチgpu使い結構いるのにraylightの話題がない」  
  → raylight（マルチGPUツール？）の不在。
- **215**: 「SMZ Nodesを削除したら動いた」「A1111系のWebUIから離れて久しいので互換Nodeは要らない」  
  → SMZ Nodes（ComfyUI互換ノード）の干渉、A1111/WebUIからの離脱言及。

#### 全体傾向
- ComfyUIが圧倒的に最多（インストール/アップデート/ノード/WF/バージョン互換中心）。理由として**動画生成の必須性、高速化（AMD/ROCm/TensorRT）、柔軟性、モデル共有容易さ**が挙げられる。
- 他ツール（Kohya GUI, Stability Matrix, reForge, easyWan, A1111）は補助的。A1111は「過去ツール」としてComfyUI移行の対比で言及。