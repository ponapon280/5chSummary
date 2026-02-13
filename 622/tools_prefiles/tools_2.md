### 抽出された「ツール」に関する話題

ログから、生成AI関連の「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなどに相当するもの、例: StabilityMatrix, Forge/Forge Neo, ComfyUI関連ノード/拡張など）のみを抽出。モデル（Anima, Takane, Illustrious/リアス, Noobai, Wanなど）は除外。ツールが選ばれている理由や利点が明記されている場合を併記。

#### StabilityMatrix
- **237**: easywan22からStabilityMatrixに変えてよさげなワークフロー入れて動画生成できるようになった（のはいいけどメモリ抑えたいい感じの設定に苦戦）。
  - *理由*: easywan22からの移行で動画生成が可能になったため選ばれた。
- **240**: Stability Matrixで主にForge系のインストール／更新が115のエラーで中断される問題が発生（公式Discordでアナウンス、修正待ち）。Forge NeoのPython 3.13問題とは無関係。
- **273**: 先週丸々費やして新しいStabilityMatrixに移行して今日ComfyUIを0.12.3から0.13.0にアプデしたらURLが表示されずUIが起動しなくなった（Was node suitsのバージョン問題で解決）。移行環境でtriton&sage attentionがサクッと入った。
- **352**: strabilitymatrix使ってても公式ワークフローだとanimaのモデルをdiffisionmodelのフォルダにいちいちぶち込むのが面倒すぎ。
- **365**: strablitymatrixエラーばっかり。forgeneoアプデしたらインストール失敗しやがって消して入れ直したらインストールできなくなるとか。本体は新しいやつはパトレオンだけだしバグ放置。

#### ComfyUI (comfy) および関連ノード/拡張
- **270**: 今回のworkflowはこちら（ComfyUIのワークフロー共有）。MMaudioは、comfyuiフォルダのhuggingface-hubのバージョンが新しいとエラーを履くので、コマンドでtransformersとhuggingface-hubをダウングレード。
- **272**: comfyui-mmaudio君の依存関係は衝突不可避なんで、公式の修正を当てた方がええよ。bigvgan.pyのインポート文より下の部分をカスタムノードの方にもコピペしたら解決。
- **273**: ComfyUIを0.12.3から0.13.0にアプデしたらUI起動せず（Was node suitsのバージョン問題でComfyUI Managerで最新版入れて解決）。triton&sage attentionを入れようとするとエラーだったが移行環境ではサクッと入った。InfiniteTalkでsage attention選んで生成すると真っ黒の動画になるので外す。ComfyUIの設定でsage attentionのチェック外した。
  - *ComfyUI Manager*: Was node suitsの最新版入れて解決。
  - *triton & sage attention*: 移行環境でサクッと入ったが、InfiniteTalkでsage attention使用時に真っ黒動画になるため外す。
  - *InfiniteTalk*: sage attention使用で真っ黒動画。
- **274**: ワイのComfyUI-MMAudioが古かっただけで、ComfyUI-MMAudioの方が先に修正（コピペ不要）。
- **275**: mmaudio nfswのワークフローが出てきたのでぶつけ本番でつかってみた。ComfyUI-MMAudioは最新のハズだがhuggingface-hub周りでエラー、gemini先生の指示でダウングレード。image用とvideo用comfyui分ける作業でaudio用環境作って解決。
  - *ComfyUI-MMAudio*: 依存関係エラー多発だがダウングレードで解決、動画音付けに使用。
- **337**: ワイ環境forge neo、5070tiで30step 18秒(sageなんとかは無し)、5stepあたり3秒（comfyの方が数秒速いっぽい）。
  - *理由*: comfyの方がforge neoより数秒速い。
- **367**: すまんcomfyで起動中に新しいモデルとかLoRA追加したらブラウザをリロードしないと選択できないんやがなんか方法ないんか？
- **369-371,373-374**: ComfyUIのRキー（Reload）やショートカット「ノード定義を更新 r」でリロード。F5でも復活。アクティブタブ以外消し飛ぶ問題あり。
- **382**: comfyui-keep-multiple-tabsをmanagerから入れると起動時やリロード時に全タブが復元される（最近タブが増殖するバグあり）。
  - *comfyui-keep-multiple-tabs*: タブ復元に便利だがバグあり。
- **412-415, 調整した画風がcomfyとneoでは反映のされ方が全然違う。LoRA込みで画風調整した場合LoRAの反映のされ方が違うせいで差異（対処法あり）。
- **349**: animaでの良さそうなworkflowってなんか無いかな。公式の奴だとシンプルなことしかできなくてlora本格運用する時に困るンゴ。
  - *rgthreeのLora Loader Stack*: 351で、4ついっぺんにLora読める。
- **353**: ワイは普通のLoad Checkpointに差し替えた。そうすれば共有フォルダで行けるし生成結果も違いはない。

#### Forge / Forge Neo
- **240**: Forge系のインストール／更新がエラー（uvのcacheのおかげで問題ない人もいる）。
- **273**: ワイ環境forge neo、5070ti（sage attention無しで生成速度記述）。
- **337**: ワイ環境forge neo、5070tiで生成速度記述（comfyの方が速い）。
- **365**: forgen eoアプデしたらインストール失敗。

#### その他のツール
- **237**: VAE Decode Tiled繋いだら終盤跳ねることはなくなった。
  - *VAE Decode Tiled*: メモリ抑えに有効。
- **270,272-275**: MMaudio / ComfyUI-MMAudio（動画音付けツール、依存関係エラー多発だが修正で使用可能。少ないガチャでそこそこの出来、環境音の音ハメ自然だが顔変わる問題あり）。
  - *理由*: LTX-2よりガチャ要素あるが面白く、aviutlで音ハメの適材適所。
- **280**: 「TeleStyle」使ってみたけど動画の場合は1フレーム目のスタイルを変えた画像を用意しないといけない。どうせスタート画像を作るならそれで普通に動画作ればいいじゃん。正直使い道がわからん。
  - *TeleStyle*: 動画スタイル変更ツールだが、1フレーム目準備が必要で使い道不明、悪用用途しか見えず精度低い。
- **406**: QIEなら何とかなるんじゃない？
  - *QIE*: 画像生成ツール（詳細不明だが文脈で推測）。

これでログ全体からツール関連の全言及を抽出。ツールの利点/理由は明記箇所のみ記載。ワークフロー共有はComfyUI中心でツール扱いとしたが、純粋なモデル話題は除外。