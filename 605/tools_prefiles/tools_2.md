### 抽出された「ツール」関連話題

ログから生成AI関連の「ツール」（ComfyUI(comfy), A1111, webUI, SUPIR, nano-banana など）に限定して抽出。モデル（NAI, Pony, illustrious, Noobai, FLUX, Wan, Qwen など）は除外。ツールの選定理由や言及の文脈も併記。各レス番号順にまとめ、重複は統合。

#### A1111 (Automatic1111 WebUI) および派生（Reforge, EasyReforge, Forge）
- **234**: 5090 a1111 1.10.1 (--opt-sdp-no-mem-attention --no-half-vae: 8sec, 13GB)。3060 a1111 1.6.1 (--xformers --no-half-vae: 55sec, 12GB)。**5090で7倍速い**点を強調。
- **310**: 新PCにEasyReforgeインストールできない問題。
- **315**: A1111 Devブランチで対応。Forge-Classic/Forge-Neoは該当処理なし。**素のReforgeは対応済み**で推奨。
- **318**: EasyReforge neo（未作成？）。拡張「my prompt」がEasyシリーズで動く。**ZuntanニキのEasyReforgeを待望**（拡張相性良い）。
- **322**: ZuntanはComfyベースに移行。**GUIしか触れない人はReforge続行**。
- **325**: バージョン下げで拡張動く場合あり。
- **375**: EasyReforge（Reforgeを2025/2/10固定ver）。**拡張相性で使い分け**（my promptなど）。
- **377**: Forge Neoで生成画像が変わる/ガビガビに（EasyReForgeに戻る）。**EasyReForgeは安定補助輪付き**で使いやすいが、Reforgeに移行必要。
- **395**: EasyReforge（古いver固定）。素のReforge（A1111-Forgeバックエンド→2025/3大規模アップデートで旧/新分岐）。新Reforge（ComfyUIバックエンド）。**拡張機能の影響大**。
- **397**: reforgeでgit pullしたらモデルフォルダ上書き/シンボリックリンク解除。
- **399**: 素のReforge大規模アップデート（改修多すぎて拡張原因特定難）。
- **400**: A1111旧forge安定（拡張込みで解説充実）。**現役アプデで問題発生→ComfyUIより辛い**可能性。
- **401**: A1111旧forge使い続け（Seed再現性重視）。Reforge移行検討中。WD14-Tagger動かん/重い。
- **404**: reForgeでWD14-Tagger動く（noteまとめあり）。
- **407**: easyReforgeとneo使い分け（拡張相性視点）。**プログラム知識なしで修正不可**。
- **414**: WD14-Tagger（前スレ情報活用）。
- **422**: a1111 Quick setting項目爆増（clip skip探し難）。
- **428**: clip_stop_at_last_layer（A1111のclip skip設定）。

**選定理由まとめ（A1111/Reforge系）**:
- 安定性/拡張相性（EasyReforgeの固定ver、旧forgeの解説充実）。
- 生成速度（5090+オプションで高速）。
- GUI使いやすさ（Comfy移行せず続行）。
- Seed再現性/馴染み（移行で画像変わるのを嫌う）。

#### ComfyUI (comfy)
- **231-233**: Loadﾎﾆｬﾗﾗノード（D&Dでinputコピー）。LoadImageFromUrlOrPathノード（Image.open使用）。dream-video-batches For Each Filename。**SSD負荷減/ input掃除不要**狙い（VHSパス読み取り）。
- **236**: inputフォルダ（メモリ上filesystem/symbolic link提案）。workflowにソース埋め込み希望。**RAM Diskで再起動消去**検討（Windowsメモリ不足）。
- **242-243,246**: SageAttention（起動コマンド/ノードで有効）。**起動オプションのみでOK**（ノード両方エラー吐くがバイパス可）。
- **244**: ImDisk Virtual Disk Driver（RAM Disk）。input/temp用（Windows Update再起動で消える問題）。
- **248**: RAM Disk（temp/ブラウザキャッシュ用）。生成AIでメモリ不足飛ぶ懸念（swapオフ）。
- **369**: comfy最新版 multiGPUノード（普通に入れても動かず）。
- **380**: comfyワイルドカード周りだるい（A1111派生より使いにくい）。adaptivepromptom機能あり。
- **395**: 新Reforge（ComfyUIバックエンド）。
- **416**: グリッドWF（ZIT髪型）。
- **423**: ComfyUIプロンプト運用（LLM翻訳、日本語補足）。

**選定理由まとめ（ComfyUI）**:
- ノード柔軟性（パス読み取り/負荷減）。
- RAM効率（input/temp管理）。
- Attention最適化（SageAttention高速化）。

#### nano-banana
- **337**: 既存画像のテーマだけ変えるのに面白い。

#### その他のツール言及（リスト準拠/拡張類似）
- **SageAttention**: 239（環境構築で速く）。242-243（コマンド/ノード有効化）。
- **WD14-Tagger**: 401,404,414（Reforge対応版あり、重い問題）。
- **SCAIL**: 405（1分長動画でポーズ検出OOM→2段分け。スマート法希望）。
- **ZimageBase/ZIT/Z-Image Turbo**: 361（来ないのが悪い）。416（グリッドWFで髪型微妙）。430（日本語自然文通る、陥没乳首出ない利点）。

**全体注記**: ツール選定理由は主に「速度/安定/拡張相性/RAM効率/再現性」。ComfyUIはノード工夫多め、A1111系はGUI/固定ver安定重視。SUPIR/webUI明言なし。