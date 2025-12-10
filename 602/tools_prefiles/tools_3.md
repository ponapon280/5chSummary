### 抽出されたツール関連話題（ComfyUI, WebUI, Forge neo, FaceDetailerなど）

以下はログから生成AI関連の「ツール」（ComfyUI, A1111/WebUI系拡張, FaceDetailerなど）に関する話題のみを抽出。モデル（DaSiWa, smoothmix, Wan, Z-Imageなど）の話題は除外。ツールが選ばれている理由や関連する利点・問題点は明記。

- **445**: DaSiWa公式WFはGetSet多用で使う気にならないからSmoothmix公式のシンプルなやつでモデルとステップ数変えるだけでいけると嬉しい  
  → ComfyUIのワークフロー（WF）言及。シンプルさが好まれる理由。

- **447**: 恐らくモデルを指定じゃない場所に保存してると思う モデルローダーごとにモデルの読込先はコード内に書かれてるし専用のモデルローダーで独自の場所から読み込むようにしてるのもあるよ  
  → ComfyUIのモデルローダーノード言及。

- **451**: comfyuiのWF試すたびに足りないカスタムノード入れてモデルとかlora階層を自分のやつに設定して生成→動かんが多すぎて赤ちゃんワイ疲れてきたで  
  → ComfyUIのWFとカスタムノード。設定の手間が多すぎて疲れる問題。

- **457**: Comfy色々できることが多いからワークフロー多くなって管理が面倒になってきたンゴ…  
  → **ComfyUI**。選ばれている理由：色々できることが多いが、管理が面倒。

- **458**: DaSiWaのWF見たわ「拡散モデルの読み込みノード」ではなく「チェックポイントの読み込みノード」を使ってそこからモデルだけ出してる拡散モデルの読み込みノードに変更するかモデルの格納場所をcheckpointフォルダに変更すれば対応できると思う  
  → ComfyUIのWFとモデル読み込みノード（チェックポイント/拡散モデルローダー）。

- **461**: ComfyuiごちゃごちゃしてきたからSDXL・次世代静止画・動画に環境わけたンゴ  
  → **ComfyUI**。ごちゃごちゃしてきたため環境分けの理由。

- **483**: 別のモデルローダーに置き換えたらモデル読み込めるようになったでしっかしWF変えるたびにネガを条件付けゼロアウトに置き換えるのも手間やなあ  
  → ComfyUIのWF変更時のモデルローダー置き換えとネガプロンプト（条件付けゼロアウト）の手間。

- **503**: 前前スレのZITのCNのWFを利用させてもらったんですがmodel_patchesにZ-Image-Turbo-Fun-Controlnet-Union.safetensorsを入れても...になるんですが原因が分からなくて困ってます  
  → ComfyUIのWF（ZITのCN用）とmodel_patches。

- **509**: ComfyUIはノードのキャッシュというかfingerprint_inputsメソッド関連がバグっとるみたいねV1 SchemeのIS_CHANGEDなら正常に動いてるっぽいがV3 Schemeで書いた自作のLoadImageノードは常に実行されるせいでワークフローが全実行されてまう  
  → **ComfyUI**のノードキャッシュ（fingerprint_inputs）バグ。自作LoadImageノード問題。

- **515**: 自分もなったUpdate ComfyUI + Switch ComfyUI->Nightlyで動いたけどNightlyなんでAt Your Own Riskで  
  → **ComfyUI** UpdateとNightly版推奨。

- **516**: 最新Comfyuiナイトリーじゃないと動かんかったと思ふ  
  → **ComfyUI** Nightly版必須。

- **561**: ダブルキャラloraとかコロサンてぇてぇmaskワークフローでええやろうま随分前から公式ノードだけでできるでそれはそれとして、いつの間にかまたnumpyがワーニング吐くようになってるなそのせいかFaceDetailerがときどき幅0の領域を処理しようとして落ちとる  
  → ComfyUI公式ノード（mask WF）と**FaceDetailer**（幅0領域エラー）。numpy警告。

- **573**: ワイ環かもしれんがWSL2はComfyUIの自動オフロードが機能せずOOMになるわVRAMに乗り切るモデルは問題なしたとえ学習だけで使うか  
  → **ComfyUI**のWSL2環境で自動オフロード機能せずOOM問題。

- **611**: Z-imageのためにcomfyUIの勉強した方がいい感じ？あれ有能なんかな  
  → **ComfyUI**の勉強推奨（Z-image用）。

- **617**: Forge neoならWebUIのインターフェースでZ-Image turboを使うことができるよUI setはluminaにして、cfgを1にする とりあえずこれでしのぐことも可能  
  → **Forge neo**（WebUIインターフェース）と**WebUI**でZ-Image turbo使用可能。

- **644**: qwenimgedit2509を今更触ってるんですが、生成結果が全部砂嵐模様になるのは設定ミスってる？zuntanさんのeasyimgeditに公式WF流しこんで20stepでも4stepでも(loraあり)CFGを指示通りにしてるけどガビガビなる…。  
  → qwenimgedit2509とzuntanさんのeasyimgedit（公式WF使用）。

- **645**: グラボの世代だったかPytrochのVerだかわからんけど、QIE2509のFP8は環境依存で駄目要素があるFP8じゃなくてBF16かGGUF持ってくるヨロシ  
  → QIE2509（qwenimgedit？）の環境依存問題（FP8→BF16/GGUF推奨）。

- **646**: そういうときはワークフローアップすると妖精さんが修正してくれるかもしれへんで  
  → ComfyUI系WFのアップロード修正（妖精さん=コミュニティ？）。