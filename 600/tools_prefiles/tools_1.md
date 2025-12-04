### 抽出されたツール関連話題

ログから生成AI関連の「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-banana などのUI/拡張/ノード/ワークフロー類）に関する話題をすべて抽出。モデル（NovelAI, Pony, illustrious/イラストリアス/リアス/ill/IL, Noobai, FLUX, Wan, Qwen）に関する言及は除外。ツールの選択理由が明記されている場合を**太字**で強調。

#### raylight (マルチGPUツール)
- **22**: GPU1枚だとOOMするようなのを2枚刺しで動かせるやつ。他のマルチGPU系だと分散処理してもウェイトは全部GPUに乗せる必要があるのをFSDPというので分割してるっぽい？
- **27**: ここでその単語が出て来たのは数回で誰も試した人はいない。

#### EasyImageEdit (zuntanニキのツール)
- **38**: zuntanニキのEasyImageEditを導入して、何もいじらんで生成ボタンを押したらエラーがでる。GPTにきいたら「Triton のキャッシュフォルダを完全削除する」とか「起動時オプションで TorchDynamo を OFF にする」とか言ってきたが信用できん。**解決策としてWindowsのファイル名長さ制限解除（42,43,50,84）、tempフォルダ最上階層移動、triton削除を提案。**
- **41**: レポートを全部コピーしてチャッピーに貼り付ける。

#### Easy Reforge / EasyWan22 (動画生成ツール)
- **67**: Easy Reforge現役？
- **68**: 未だにEasy Reforge使っとるけど今は動画も作れる**EasyWan22というのもある**。
- **71**: easyreforgeとeasywan22 シコることしかしないから他はまだええかな。
- **72**: **ワイはSDXLはreforgeで他は全部comfyuiやな。なんだかんだフォーマットが合うならA1111のデザインは便利やから使う。z-imageが仮に流行ったらそれはそれで色んな人がcomfyuiのWF出してくれるやろうし気にせず好きなもので動かせばええ**。
- **97**: **comfyui 0.3.66だとEasyWan22よりsmoothmixの生成速度がちょっと遅かったけど 0.3.75だとEasywan22より5～10%ぐらい早くなった**。これでEasyWan22から脱却してwan2.2と他をスムーズに使えるようになった。

#### ComfyUI (メインUIツール、WF/ノード/拡張多数)
- **34,37,89**: WanのWFが壊れた（リロード/再起動でノードコピペ不能）。サブグラフアンパック、拡張ノードのせい？ パイバスでoutputエラー回避、Condition Selectorでブランチ回避。**初めたばっかやけど流石に色々参考にしながらこのWFまた組むのはやりたく無い**。
- **36**: サブグラフあったら一旦アンパックしてみて。
- **72**: 上記参照（reforge/A1111との使い分け理由）。
- **90**: **LM Studioオススメ。単体でも遊べるし連携前提の設計でもあるから comfyuiからの利用も想像以上にスムーズに動く エンジン廻り？が揉まれてるから動作速度に安心感がある**。
- **97**: 上記参照（バージョンアップで速度向上）。
- **101**: ComfyUI上でGGUF使える（かつVRAM解放してくれる）ノードを探し中。**VRAM解放がでけんっぽいのが悩みどころ**。
- **109**: LM studioと連携するノードなら、たいていはアンロードも出来るはず。
- **110-111,113,153**: ComfyUI-Impact-SubpackインストールでUltralyticsDetectorProviderエラー。ManagerでInstall missing custom nodes。**手動削除/再インストール、古いバージョンにスイッチで解決。nightly/ベータ版問題？ ComfyUIManagerから入らないのはよくある、手動git clone + venv active + pip requirements.txt**。
- **115-116**: アプデしたらテキストボックス系プロンプトのお尻にある,を勝手に消す。**autoComplete plusのauto formatterの設定**。
- **117**: アプデめんどくせえから0.3.65くらいで放置しようとしたが早くなるのか。
- **144-145,148-149**: ベースプロンプトに{closed,|open,}のようにランダム性をもたせた場合、seed固定しても異なる画像に。**wildcardノード側のseedも固定。seedノードにサンプラーとワイルドカードのseedを同時に繋いどくと一括楽**。
- **146**: グラボ換装でドライバ入れ直したら7zポータブル版comfy動かん（issue/redditに未解決報告）。git cloneから環境構築で動く。
- **190**: **LM Studio導入済みなら新たに入れる必要はない。裏で起動してるLM Studioにポート通じてアクセス。Stability Matrix版でも関係ない**。
- **212-213,219,221,223-227,229**: 最新版にしたら生成ボタン隣の中止ボタンが消えた！UI変えすぎ。**settingsの「新しいメニューを使用」を無効に。frontend 1.30.6で変化、frontend戻す。AutoHotKeyでマウスサイドボタン割り当て。ComfyUI-Managerパッケージ化でマネージャーボタン消え、左上メニューからManageExtensions**。
- **234**: Rife TensorRTで高解像度動画フレーム補完したらジャギー（PainterI2V/PainterLongVideo/WaveSpeedと併用で原因特定）。
- **237**: FaceDetailer（おまんまんにも使える）。

#### その他のツール/ノード/拡張
- **Stability Matrix (124)**: StablitymatrixでCOMFYUIを動かしてる。
- **LM Studio (90,101,120,183,187,190,230-232)**: 上記ComfyUI連携参照。**GGUFコスパ良いがVRAM解放悩み（auto_unload=Trueで毎回解放、ロード時間プラスだが高速）。f16試したがオーバーキル、VRAMに応じてgguf選ぶ。出力暴走せず早い**。
- **ComfyUI-QwenVL (187)**: LM Studio連携より2.6倍高速。
- **smoothmix (97,128)**: 生成速度比較でComfyUI有利。
- **PainterLongVideo (128)**: 長め動画（150フレーム、high側smoothmix/ステップ/shift調整）。
- **PainterI2V, WaveSpeed (234)**: Rife TensorRTと併用。
- **Rife TensorRT (234)**: 高解像度非対応でジャギー。
- **FaceDetailer / ComfyUI-Impact-Subpack (110,237)**: 上記参照。

#### ドライバ/CUDA関連（ツール運用）
- **40,45,53**: RTX3090のドライバ（560.94→566.36定番/cuda12.6、581.80/581.94 for cuda13）。
- **146,200**: グラボ換装でPytorch/CUDAバージョン対応必要。
- **42**: Windowsファイル名長さ制限解除。

これでログの全ツール関連話題を網羅。モデル名（Wan/Z-image/illustrious等）はツールの文脈でも抽出除外。ComfyUIが最多で、速度/UI安定性/拡張連携が選好理由の中心。