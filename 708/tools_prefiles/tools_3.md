## 抽出結果：ツールに関する話題

### ComfyUI / ComfyUI関連ノード

- **>>433**: ComfyUI最新版に更新したが不具合関連の話題。現時点の最新版を入れれば直るか確認求む。
- **>>435**: ローカルLLMとComfyUIを同時に使いたくなる。モデル入れ替えの自動化をしているか質問。もう一台AI用マシンが欲しいという意見。
- **>>437**: KJnodesのVRAM debug機能を使い、毎回VRAMを解放してからLLMを呼ぶようなworkflowを組んでいる。やはりもう一台マシンが欲しいとのこと。
- **>>450**: forgeは現役。ComfyUIでxyz比較（チェックポイント比較）をやるのは禿げるとの不満。
- **>>454**: xyz比較用にforgeを残している。
- **>>458**: チェックポイント比較でxyzをよく使うため、forge neoと添い遂げると述べる。
- **>>466**: プロンプトのオールインワン化や部族語の自動翻訳変換、LoRAのサムネイル一覧表示機能がComfyUIでできるなら完全移行したい。画像生成試行を繰り返す際にforgeの方が楽だと理由を説明。
- **>>484**: ツールの使い方。Resolution SelectorのW/H出力をEmpty Imageノードに繋ぎ、Create Bounding Boxesのbackground入力に接続すれば、解像度やアスペクト比がResolution Selectorで指定したものに反映されるとのアドバイス。
- **>>495**: Bounding Boxの数字をクリックすれば奥に行った箱も選択できることを発見。>>484の繋ぎ方でCreate Bounding Boxノード実行時に自動で解像度が変わることを確認した。
- **>>502**: 既存のノードを弄って画像参照に成功した。背景もBounding Boxで対応可能とのこと。
- **>>532**: >>484の繋ぎ方で空のBBoxキャンバスも反映されるようになった。空の状態のBBoxキャンバスをクリックするとノード下部のボックス編集用部分が出てくる挙動について、元からこうだったか疑問を呈している。
- **>>574**: チャッピー（ChatGPT）に聞いて、rgthreeのFast Muter/Fast Bypasserの代替となるノードを発見。`ComfyUI_Eclipse`と`ComfyUI_LC123_nodes`でrgthreeの主要機能を代替でき、Nodes 2.0に移行できるとのこと。
- **>>589**: >>502の情報を参考にして似たようなノードが作れたとの報告。

### Forge / Forge neo

- **>>450 / >>454 / >>458**: ComfyUIでのxyz比較の手間に対し、forge（forge neo）をxyz比較用に残しておく、またはforge neoと添い遂げるといった選択の理由としている。
- **>>466**: 画像生成を何度も試行する際、forgeの方がComfyUIより楽だと理由を述べている。

### Create Bounding Box（機能・ノード）

- **>>464**: Create Bounding Boxについて、コマの中にセリフや擬音のbboxを入れると選択できなくなる問題がある。改善を求めている。
- **>>484 / >>495 / >>532**: BBoxの解像度反映に関するノード接続のワークフロー改善。
- **>>502 / >>589**: BBoxを用いた画像参照機能の実装と成功報告。

### Fizgig

- **>>489**: LoRA作成の調査。FizgigではProdigyが使えないことが分かった。
- **>>539**: FizgigでMOSS用LoRAを作成した報告。モデル構成によってはvram 8Gでも作成可能（50stepsで1時間半、細かい設定はAuto）。MOSS公式の`moss-image-prompt-enhancer skill`をLM Studioのプラグインに導入し、gemma4にbooruタグを自然言語に加工させる手法を試した。
- **>>597**: FizgigがMOSSに対応したためアップデートしたところ、主要なローカルモデルをほぼ網羅するようになった。最初はFLUXとkrea2だけの対応だったがやる気を評価。
- **>>602**: `Launch Fizgig in browser.bat`で立ち上がったwebUIが最初の画面で固まりクリック反応しなくなるハング状態になる（エラーは出ない）というトラブル報告。
- **>>603 / >>607**: トラブルに対し、`Launch Fizgig.bat`で起動すれば独立アプリ風に立ち上がるためそちらを使うようアドバイス。

### LM Studio

- **>>539**: LM StudioのプラグインとしてMOSS公式の`moss-image-prompt-enhancer skill`を導入し、gemma4にbooruタグっぽい記述を加工させる用途で使用。

### WebUI（一般・その他ツール）

- **>>497**: 次世代ローカルAIのラインナップとして、編集ツールにQwen Image 2.1を挙げている。
- **>>522**: 文字加工を見据えたギャグ画像作成にはMOSS（モデルではなくツールとしての構図制御・文字機能の文脈）が相性良いとの助言。
- **>>626**: civitaiのWebUI機能について、新しいモデルが無条件でcreateできるようになっているかどうかの話題。

### sd-scripts

- **>>479**: krea2と同じトレーニング設定で上手くいかない件（>>431）に対し、sd-scriptsで環境を整え、研究を開始する準備をしている。

### ショーケース / safetensors メタ情報管理

- **>>626**: 作業中にアップロードしたsafetensorsのメタ情報からNSFW語句を読み取られ、モデレーションに引っかかった体験談。`生ハメOK`や`中出しOK`がスキャンで指摘された。loliだったら致命傷だったとの感想。

### ComfyUI_Eclipse / ComfyUI_LC123_nodes

- **>>574**: rgthreeの代替ノードとして、ComfyUI_EclipseとComfyUI_LC123_nodesがFast Muter/Fast Bypasserの代替になる。これによりNodes 2.0へ移行できる。 チャッピー（ChatGPT）に聞いて発見したツール。