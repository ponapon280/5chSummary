### 生成AI関連「ツール」に関する話題抽出

ログから「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなどに相当するUI/ノード/拡張/カスタムツールなど）に関する言及をすべて抽出。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwenなど）関連は除外。ツール選定理由が明記されている場合のみ併記。

#### ComfyUI関連
- **29**: 「コンテニューするか（comfyuiに挑戦するか）って気分にもなるんや」  
  (挫折時のテンプレとして言及。理由: 挑戦対象としてモチベーション源)。
- **130**: 「WF見つけて入れたけどローダーが動かん 何とかDiffってパッチを当てるとかMatrixつこてる万年赤ちゃんには無理や」  
  (ComfyUIのワークフロー/WFでローダー動作不良。理由なし)。
- **133**: 「Z対応のwhlがまだ公式から出てないから自分でビルドしないとあかんね ComfyUI-nunchakuのほうはdevブランチでローダーが追加されてるけどエラーで動かん」  
  (ComfyUI-nunchakuのカスタムノードでローダーエラー。理由なし。Lora未対応が課題)。
- **139**: 「じーまげEditが出たら頑張るます あとSeedVarianceEnhancerってカスタムノードええ感じ」  
  (じーまげEditとSeedVarianceEnhancerのカスタムノードを期待/好評価。理由: 高速/効果的)。
- **166**: 「VRAM16GBのメインメモリ96GBでQWEN25llの 4step設定が動いたんやけど」 (comfyUI側で共有GPUメモリ使用。理由なし)。
- **195**: 「初心者の質問で申し訳ないんやが、共有GPUってメモリの半分やろ？ comfyUI側からは半分しか使えないんか？」  
  (ComfyUIの共有GPUメモリ使用制限について質問。理由なし)。

#### A1111 / WebUI関連
- **76**: 「無料クラウドでやるだけなら簡単だろうね 規制なし、追加学習もできるローカルだと段違いに難易度跳ね上がる pythonインストール時に環境変数にpath通したり コマンドプロンプトを直叩きしたり仮想環境のバージョン競合を解決したり」  
  (A1111 WebUIのLinux版インストール難易度高さを指摘。理由: ローカル環境構築の煩雑さで難易度↑)。
- **123**: 「ページングメモリーのラージページ(やhuge page)を使う最適化は LinuxのA1111 WebUIで2023年にはあった(TCMalloc)」  
  (Linux A1111 WebUIのTCMalloc最適化言及。理由: メモリ効率化)。
- **125**: 「TCMallocは入ってるな Check TCMalloc: libtcmalloc_minimal.so.4 とか起動時に出てくるで」  
  (A1111起動時のTCMalloc確認。理由なし)。
- **171**: 「ChenkinNoob-XL-V0.2 ワイ還ではEuler aだとノイズ画像が生成される dpm++2mなら正常 KSampler (inspire)のA1111モードで生成するとノイズ画像が生成される」  
  (KSampler(inspire)のA1111モードでノイズ発生。理由なし。不安定)。

#### その他のツール
- **74**: 「EasyWan22で楽しいけど四苦八苦しながら動画生成やっとる 画像の方はreForgeを入れ直したけど最近はneo とかも出てるんやな 違いようわからんが」  
  (EasyWan22: 動画生成で使用、四苦八苦。reForge: 画像生成で再インストール、neoと比較中。理由なし)。
- **82**: 「nunchakuのz-imageはRes Multistep/simpleの4stepで低スぺでもめちゃ速いな もうsdxl系の資産はアーカイブ化確定や」  
  (nunchakuのz-image: 低スペックで高速(4step)。理由: 低スペ対応/高速さが選定理由でSDXL資産を置き換え)。
- **86**: 「ZimageBaseまだか…？ ほんまに公開してくれるんかアレ はよLora作りたいんやが」  
  (ZimageBase未公開で待機中。理由: LoRA作成目的)。
- **154**: 「qwen layered重すぎる 3060だと厳しいんご 解像度やレイヤー数にもよるが1時間とか出る QIEのlightning使えるんだよな？ 2511の4step試してみるか…」  
  (QIEのlightning: 重い処理代替として検討(4step)。理由: 高速化)。
- **156**: 「そう言えばRuindFooocusもQwenとZ-Imageに対応してたんだな 使い方さっぱり解らんが」  
  (RuindFooocus: Qwen/Z-Image対応確認。理由なし、使い方不明)。
- **189**: 「今は共有GPUを使う仕様 漏らしてるわけではない 勘違いしてDistorch2使っちゃうと逆に遅くなるで」  
  (Distorch2: 共有GPU仕様で使用すると遅化。理由なし、避けるべき)。