### 抽出されたツール関連話題（ComfyUI, Stability Matrix, その他ツール/ノード中心）

ログ全体から、生成AIツール（ComfyUIの各種導入形態、Stability Matrix、関連ノードなど）に関する話題を抽出。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwenなど）関連は除外。ツール選択理由（地雷/利便性/情報量/UI変更/導入しやすさ/エラー対応など）が明記されているものは強調。

#### ComfyUI（全体/更新/UI関連）
- **25**: comfyデスクトップ版は地雷だったのか…赤ちゃんは大人しくすたびりてぃまとりくす版にします  
  *(デスクトップ版が地雷扱い、Stability Matrix + Rickus版へ移行)*
- **46**: スタビリティマトリクスでコンフィやる時は他と違うノウハウがいるからな 意外と情報がない  
  *(Stability Matrix経由ComfyUIの情報不足)*
- **47**: Manager経由で入れられないカスタムノードなんかは結局Stability Matrixフォルダ内のvenvに入ってpip requirementsが必要で…Stability Matrixの恩恵少なくね？…Stability Matrixとはサヨナラしたな Stability Matrixはフォルダ構成独特すぎて使いにくいと感じてたし  
  *(Stability Matrix経由ComfyUIのノード導入煩雑さ、フォルダ構成の使いにくさで離脱)*
- **48**: そっちじゃなくてスタビリティ側のコンフィのメニューから入れるんよ それやるようになってからはエラー無くなって完全移行できたわ  
  *(Stability MatrixのComfyメニュー使用でエラー解消、完全移行)*
- **72**: ひさしぶりにComfy更新したらフロントエンドがいつの間にかちゃんと難読化されていてちょっとしたローカル修正も面倒ね  
  *(更新でフロントエンド難読化、ローカル修正面倒)*
- **76**: ComfyUIはportable版じゃあかんの？ずっとこれ使ってるわ  
  *(portable版継続使用)*
- **89**: 久しぶりにComfyアップデート、なんかUIの変更の事で文句出ての覚えてるけど、これの事か……確かに糞だなこれ……なんでview job historyなんぞ作った……  
  *(アップデートでUI変更、文句多し)*
- **92**: ポータブル版が管理楽でええよ 導入もダウソして解凍するだけやし 独立環境でOS再インスコしてもそのまま使えるし pyenvやuv不要でpythonバージョンの異なる環境も複数構築できる  
  *(portable版の管理楽さ、導入簡単、独立環境の利点)*
- **94**: git cloneで入れてるわ どのタイミングか忘れたけどポータプル版で使ってたのが動かなくなってその頃からcloneして自分でvenv入れて依存関係も自分で解消して…とやってる  
  *(git clone + venvへ移行、portable版動かなくなったため)*
- **98**: comfyUIは導入手段が複数あるから会話が噛み合わない時あるのよね、そう考えるとeasyは分かりやすい  
  *(導入手段多さで会話混乱、easy版の分かりやすさ)*
- **101**: comfyが迷走し始めたのがUI群雄割拠のスタートの合図だと気づいたのは一年後のことだった  
  *(UI迷走指摘)*
- **124**: 赤ちゃんでようわからんからとりあえず何かあったらすぐリセットできそうなcomfyUIポータブル版入れてみたけどmatrixのほうがええんか  
  *(portable版のリセットしやすさ狙い、Matrix比較)*
- **129**: ComfyUI-nunchakuのZ-Imageがワイ環だとずっとエラーだったけど--fastオプション外したら動いたわ 5060tiで公式WFが8秒台といったところ  
  *(ComfyUI-nunchakuのZ-Imageノード、エラー回避法)*
- **130**: portable版でとくに問題は発生してへんな 動いてて保守できとるならそれでええねん  
  *(portable版の安定性)*
- **133**: 自分がComfyUI使い始めた時は今でいうportable版しかなかったからそのままportable版使ってる まあComfyUI使えたら何でも構わないとは思うけど  
  *(portable版の継続使用理由: 初期からの慣れ)*
- **135**: ComfyUIコロコロUI変わるから出版までにタイムラグある書籍向きじゃないでしょ  
  *(UI頻繁変更のデメリット)*
- **138**: comfy勉強しようとして躓くポイントその1な気がする ブログですら情報古いから実際の画面とスクショの画面が違うし、やりたいことの説明が古いバージョンだったりするしで  
  *(情報陳腐化による学習躓き)*
- **144**: 「できる！ComfyUI」の出版が待たれるな  
  *(ComfyUI書籍期待)*
- **163**: ニキらComfyuiのバージョン何使ってる？ KJnodes動くバージョンが知りたいんやが  
  *(バージョン確認、KJnodes互換)*
- **166**: StabilityMatrixにバージョンアップの通知が付いてから、数日このスレで様子見して、大丈夫そうだったら上げる感じ  
  *(Stability Matrix経由更新の様子見運用)*
- **167**: いまv0.6.0ってコト？ リリースされてからだいぶたったよね  
  *(ComfyUI v0.6.0確認)*
- **179**: ComfyUIいつの間にかノードの色テンプレ以外のRGB値に出来なくなってる･･･  
  *(ノード色変更機能変更)*
- **180**: それってComfyUI本体の機能じゃなくてCustomScriptsの機能じゃなかったか？  
  *(CustomScriptsの機能指摘)*
- **188**: zuntanニキのsimple comfyUIに頼るとええで sage attentionとtriton入ったcomfy自動的にインスコしてくれる  
  *(SimpleComfyUIの自動インスコ利点)*
- **194**: サイドバーにキューがあってキーボードQ(ueue)から呼び出しやすかったのにそれを無くしたからなぁ…デザインによるUIの改悪やと思うわ  
  *(UI改悪指摘)*

#### Stability Matrix（ComfyUIマネージャーとして主）
- **26**: Stability MatrixはStability Matrixという地雷がある  
- **27**: >>25 地雷なん？winアプデでぶっ壊されたから折角導入したのに…  
  *(Win更新で壊れ、地雷扱い)*
- **51**: grok級の事をローカルで出来るフレームパックみたいのがふと出てくると信じて Stability Matrixを使い続ける  
  *(将来性期待で継続)*
- **52**: 普通に使う分には使えるからStabilityMatrixはvenvでcomfyui入れるよりは初心者には向いてると思うStabilityMatrixで学んだことはvenvComfyuiにも活かせるしな ただ情報は少ない  
  *(初心者向け、venvより楽だが情報少ない)*
- **53**: 拡張機能から検索して入れられるからvenvより楽だよ 似た名前のカスタムノードと間違えないようリンク先確認すれば確実だし間違えてもインストール済み一覧から選んで削除すればいい  
  *(拡張機能検索の楽さ)*
- **200**: やったねたえちゃんStabilityMatrix2.15.5でForge Neoに対応したよ  
- **209**: 入口が増えただけで、中身は2.15.4でForge ClassicのBranchesをNeoに変えてインストールしてたのと変わらんで  
  *(バージョンアップ、Forge対応)*
- **213**: kohya_lora_param_gui使ってみたいんだけどStabilityMatrixみたいにvenv環境下のportable python(?)やportable gitで pythonやgitインストールせずに使えるようにならんかな  
  *(portable環境の利便性比較)*

#### ComfyUI内ノード/拡張関連
- **139**: PainterLongVideoを使うのとFLF2Vで自力で何個も作って繋げるのでは…  
  *(PainterLongVideoノードの挙動確認)*
- **145**: painterのノードは動きが早くなるだけで一貫性が保たれるかというとビミョー…  
- **147**: PLVでも一貫性はお察し。LF使うよりはつなぎ目はなめらかな気がするけど…画質の劣化が激しく15～20秒当たりでもう厳しい  
  *(PainterLongVideo/PLVの限界)*
- **153**: ComfyにAdetailerと同じようなものある？  
  *(Adetailer相当探し)*
- **156**: FaceDetailerってやつ  
- **157**: face detailerっちゅうのがある 顔以外も手とかちんことかyoloファイルがあれば描き直せる  
  *(FaceDetailerの多機能性)*
- **164**: RTX5070TiでSimpleComfyUi+DaSiWaチェックポイントとWFを試した際に1回目の動画生成は正常に動くけど2回目以降の動画生成は砂嵐になる現象が発生…Comfyui-GGUFにはpinned memoryとの相性？でメモリリークが発生する…Comfyui-GGUFをgithubから最新版をクローンして使ったら問題は解決した  
  *(SimpleComfyUi + Comfyui-GGUFのトラブルシュート)*

#### その他ツール
- **200/209**: Forge Neo/Classic（Stability Matrix対応、WebUI系?）
- **213**: kohya_lora_param_gui（LoRAパラメータGUI、portable化希望）

**まとめ傾向**: ComfyUIは導入形態（portable/git clone/Stability Matrix）で議論多め。portable版は管理楽/安定推し、地雷版（desktop）やUI変更批判あり。Stability Matrixは初心者向け/拡張楽だが情報少なくWin更新脆弱。ノード（FaceDetailer/PainterLongVideo）は動画/詳細修正用途で言及。全体的にツールの安定性/情報量/UIが選択理由の焦点。