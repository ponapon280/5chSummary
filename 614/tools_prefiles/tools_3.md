### 抽出された「ツール」関連話題一覧

ログから生成AI関連の「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR/nano-banana類似のUI/ノード/マネージャー/ダウンロードツール/環境管理ツールなど）に関する話題を抽出。モデル（NAI, Pony, illustrious/IL/リアス/ill, Noobai/Noob/Newbie, FLUX/Flux/flux2 klein, Wan/wan2.2, Qwen/qwenなど）言及は除外。ツール選定理由が明記されている場合を太字で強調。

#### 434: WanVideoWrapperとKJNodes
- 「>>415 なんでやWanVideoWrapperとKJNodesに入っとるやろ」

#### 437-438, 451-452: Civitai, Stability Matrix, HF (HuggingFace), aria2
- CivitaiのDL失敗問題。「CivitaiでのDLが途中で失敗しまくる」「Stability Matrix経由だとやたら失敗」「12GB超えるものはHF」「aria2を使ってる」「ZuntanのEasyシリーズのダウンロードバッチ」「civitaiのアプデでDL履歴にサムネが出るようになったな、これ神アプデやわ **サムネ消えで削除確認が容易**」

#### 441: SVIノード, Manager (ComfyUI Manager), KJNodes, Custom nodeフォルダ, Git Clone, Venv, pip requirements.txt
- 「SVIのノードはManeger経由だとKJNodes入らない」「Maneger経由だとアンインストールしても消せてなかったり」「Custom nodeフォルダにGit CloneしてVenv Activeしてからpip requirements.txt」「**VenvActiveしないでグローバルに入れて動かンゴ、環境依存でチャットAIに前提伝えないとグローバルにぶち込まれる**」

#### 459: ComfyUI (comfyui)
- 「comfyuiだとACE-Stepは使用できるぞ」

#### 463-465: ComfyUIのメニュー/サブグラフ
- 「comfyuiで右側にメニューがまとまってるのが好き」「new menuをdisabled」「サブグラフを開いたあとにメインに戻ってくる方法」「**Escキーで戻る**」

#### 467-468, 488-489: SVIノード, KJNodes, Manager
- 「SVIノードはManeger経由でKJNodesをアンストしてから入れ直す」「git cloneしないと動かなかった」「マネージャーからだとダメ」「コマンドプロンプトに直接打ち込む」「マネージャで入る場合も有るが失敗する **赤ちゃんにはgit clone推奨**」

#### 468-470, 478: アップスケーラーカスタムノード, 「画像を拡大（指定サイズ）」
- 「アップスケーラーで4倍とかにした後サイズ縮めるところまでまとめてやってくれるカスタムノード」「**『画像を拡大（指定サイズ）』が使いやすい、倍率で0.5とか0.25で縮小、グループノード化は多用したくない**」

#### 471-486, 489-490, 515, 519, 524: Venv (仮想環境)
- Venv必須議論多数。「各環境にインスコしてたらSSD容量足りないから親環境に直インスコ？」「**ライブラリ間のバージョン不整合で全環境壊れる、トラブルで環境作り直したくなるからvenv必須**」「グローバルにいれてたら別のもの出た時詰む」「SSD 4TBあれば数十個のvenvないに等しい」「mini condaで環境別ドライブ」「venvを消した数だけ強くなれる」「**静止画生成環境・動画生成環境・LoRA学習環境で環境異なるから無理ゲー、隔離必須**」「venvってなんだろ **venvフォルダにPythonとrequirements.txtインストールで依存関係壊れない**」「activate忘れでグローバル汚染」「**run.batにCALL venv\Scripts\activate.bat追加でpandasエラー解決**」「uvならactivateすらいらねえがツール側対応してない」

#### 490: Manager (ComfyUI Manager), SVI
- 「デスクトップ版は安全寄りすぎてManeger経由で入れられないノードはどうしようもない **SVIとか今使えない**」

#### 498-502, 512, 515, 519, 529: LoRA学習タグ付けツール (wd14-tagger, Florence, QwenVL, PixaiTaggerOnnxGui)
- 「lora学習用のためのタグ付け」「wd14-taggerもFlorenceもComfyUI任せ **ノード入れるだけで数百枚バッチ処理楽**」「PixaiTaggerOnnxGui **githubに日本語説明、直感的**」「手動記載推奨 **Tagger参考程度、自分で丁寧に時短**」

#### 503: enhance (おそらくComfyUIノード)
- 「enhanceだとヘイストかかったテルアリンみたいな速さで動くことがたまにない？」

#### 505: easyWan22
- 「easyWan22すら触らずに相談増えてる **LoRA使わずエロ出ないと文句言うレベル**」

#### 534: A1111, reforge, comfy (ComfyUI)
- 「レガシーとして残してるA1111、画像生成用のreforge、動画生成用のcomfyで全部環境バラッバラ **venv一択**」

#### 569: VSCode (Python venv自動activate)
- 「VSCode教に入るのです、自動でactivateされますよ」

#### 612: PLV, SVI, KJNodes
- 「PLV→継ぎ目工夫入ってるがバレバレ、スタート/エンド画像制御 **挙動素直**」「SVI→継ぎ目わからない永久動画、スタート/アンカー画像制御 **挙動工夫必要、LoRA複数で混乱、KJNodes Manager失敗で導入ハードル**」

#### 621-630: ComfyUIのサブグラフ/ワークフロー (WF)
- 「サブグラフはクソ」「配布WFにサブグラフ使うなんて」「ノード裏にノード置いてるWFはクソ」「公式WF入力出力以外サブグラフでクソ」「LTX-2公式テンプレサブグラフ内でランダムシードで動作不良 **展開で解決**」「easywanのテンプレWF一気通貫 **後処理アプスケ別WFに分けるべき**」「何でも詰め込んだ超バカWFをサブグラフ群でコンパクト **公式テンプレ参考**」

#### 669以降なし（ログ終わり）

**まとめ**: 主にComfyUI周りのノード（KJNodes, SVI, Manager）導入難易度/Venv環境管理、ダウンロードツール（Civitai/Stability Matrix/aria2）、タグ付けツール、WF/サブグラフ最適化、A1111/reforgeが話題。選定理由は「依存関係壊れ防止」「楽/直感的」「動作安定」「コンパクト化」中心。モデル関連（Wan/LTX/Fluxなど）は一切抽出除外。