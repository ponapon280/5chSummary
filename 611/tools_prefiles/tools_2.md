### 抽出された「ツール」関連話題一覧

ログから生成AI関連の「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR, nano-banana などの画像生成/動画生成UI・ワークフロー・インストール関連ツール）に限定して抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen）関連話題は一切除外。ツールが選ばれている理由（例: 使いやすさ、安定性、機能性）が明記されている場合のみ追記。

#### ComfyUI (comfy) 関連
- **226-270以降なし（間接）**: ComfyUIの文脈でworkflow言及（236: wan2.2のworkflow入れ替えたら低スペでも早くて綺麗、Subgraphだらけ）。
- **228-229,241**: huggingface-cliでモデルファイルを全部落として同じ階層に配置（json, tokenizer.*など）。初めてのケースでクリックダウンロードで動いた。**理由: 基本的な使い方として推奨（huggingface-cliが標準）。**
- **234-235**: lora.pyの9093行目をコメントアウトしてlora key not loadedのログを抑制。**理由: 実害ないログをうざいので非表示（WAN以外では実害あるため注意）。**
- **246**: テンプレWF集からltx2のテンプレ持ってきてダウンロードリンクからファイル配置で実行。**理由: 一番簡単（3060/12GB RAM32Gで動く）。**
- **283**: ComfyUIがgemma_3_12B_it.safetensors読み込みで落ちる（text to video(LTX 2.0 Distilled)のテンプレートでも同様）。
- **287**: 起動オプションに --reserve-vram 4 付け、preview methodをNoneに。**理由: 3060用に必要（試したが変わらず）。**
- **288**: fp8 e4m3fn使用（OSError: ページングファイル小さすぎるで落ちる）。
- **292**: ComfyUI 0.8.1来た（毎日のようにアプデ）。
- **293**: --reserve-vram 0-4試したが変わらず、fp8 e4m3fnでOSError後ComfyUI落ち。仮想メモリ増やす必要？
- **294**: テンプレLTX-2 WFでtensor sizeエラー、smZNodes消したら動いた（issue報告済）。
- **300**: ComfyUIの入れ方？ GITが汎用性高い？ **理由: GITが1番楽（branch作って戻すコマンド一発、302）。**
- **302**: GIT慣れたら1番楽（branchで戻す簡単）。
- **305**: portableが個人的に楽。**理由: お手軽。**
- **307**: v0.8.2来た。
- **311**: デスクトップ版手動アプデ方法なし？ v0.7.0でLTX-2エラー。
- **312**: デスクトップ版はやめといた方がいい。
- **314**: git/venvは開発者向け、docker導入で攻守最強。**理由: バージョン衝突回避（349: CUDA/PyTorchバージョン難易度高い）。**
- **315**: update.batで手動アプデ可能。
- **316**: EXEワンクリ希望。
- **317**: SourceTreeでgit pull、venv activate後pip install -r requirements.txt。
- **319**: easywanとPortable分けてる、デスクトップ版はバグバグで環境壊れた。
- **320**: venvならフォルダ削除で便利。
- **321**: デスクトップ版v0.7.0（CoreとDesktopバージョン独立、タイムラグあり）。
- **324**: デスクトップ版アプデ毎エラー、venv作り直しやGPTで直す。
- **332**: デスクトップ版ハズレ、エラー多い。
- **333**: お手軽はデスクトップ版（タイムラグ/Magerノード対応しにくい/OS汚染のデメリットあり）。
- **336**: ポータブル版UNZIPだけで使える。**理由: それ以上手軽なものなし。**
- **343**: ポータブル関係なくwhlインストールで赤ちゃん撃沈、カスタムノード入れすぎで助からない（flash/sageattentionで血涙）。
- **349**: 新規がComfyUI始める難易度高い（CUDA/PyTorchバージョン衝突）。
- **356**: venv環境ComfyUI v0.8.2でオールグリーン（一部ノード未対応警告除く）。
- **360**: ComfyUIで動画生成3倍早くVRAM60%ダウン。
- **395**: >>142氏のWF整理（setget/サブグラフ使用、サンプラーcoreに変更、カスタムノード減）。
- **397-417**: サブグラフ話題多数（階層またぎ不可/ローカル名メリット、コピペ簡単、シュリンク化便利、公式WFで入力ミス、inサブグラフきつい、String(Multiline)スペース対策）。**理由: ノードまとめスッキリ/モジュール化/コピペ便利/関数的に使えるが多用注意。**
- **401**: 公式プロンプト入力→サブグラフ→生成が使い辛い。
- **404**: ローカル名で階層またぎなしが良い（コピペ重複気にせず）。
- **406**: 公式WFサブグラフ内で高さ/幅入力して正方形化（外確認必要）。
- **409**: デフォでプロンプト外に出てない。
- **410**: auto_unload=trueにしないとLLM VRAM常駐。
- **415**: v0.8.2+ComfyUI-LTXVideo更新でVRAM消費下がった気が。
- **418**: sage attention使えずpytorch cross attentionメッセージ出なくなった（バグ？）。

#### Stable Diffusion Web UI (A1111/webUI) 関連
- **325**: Stable Diffusion Web UIで画像生成後、ゆっくり実況立ち絵利用。

#### nano-banana 関連
- **279**: Gemini 3 Proで画像生成しようとしたらJson吐き出し、課金してNano Banana Pro使えってこと？

#### その他のツール言及（SVI, LTX2などComfyUIワークフロー関連）
- **230-239,256,326,335**: SVI lora適用でlora key not loaded（fp8モデル？3種類: Wan2.2公式/Smooth Mix派生/Kijaiフロー用、ガチャ）。kijai版で適応。SVIpro WFでホワイトノイズ。AttributeError出続ける。
- **246,275,283,291,294,304**: LTX2テンプレWF（VRAM12GBで13分、SEED Randomizeでも同じ動画、VRAM16GB無理？量子化でいける、ComfyUI-LTXVideo更新）。
- **391,403**: Civitai検索API壊れ、URL貼り検索/ checkpointマネージャーでメタデータ入手。**理由: 一番楽。**

**抽出まとめ**: ログの大部分がComfyUI中心（インストール/アプデ/サブグラフ/起動オプション/WFトラブルシュート）。選ばれる理由は「楽/簡単/汎用性/スッキリ/バージョン管理」多め。Stable Diffusion Web UI/nano-bananaは少数。SVI/LTX2はComfyUI WFツールとして扱い抽出。モデル混入なし確認済。