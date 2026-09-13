# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI（最も頻出・中心的ツール）
- 最も頻出・中心的ツールとして位置づけられる
- 将来的な本体サポート見込みと操作の楽さで推奨

### ツール: Codex（Codex系ツール/インターフェース）
- プロンプト・コード生成の精度と柔軟性が高い
- 仕様を考え作る共同作業者として機能する

### ツール: StabilityMatrix
- ComfyUIの導入・管理に使用
- ComfyUIの簡単な導入・管理ツールとして活用

### ツール: Krea2
- キャラLoRA検証や文字入れ機能、GPT Image 2.5との比較で言及
- キャプション単位での服制御や複数キャラ混在抑制に強み

### ツール: その他のツール
- Animerge: LoRAマージ作業の利便性向上
- MMAudio: ローカル効果音生成ツール（完成度不十分）
- YuE2 3B: ローカル音楽生成のSuno代替（弱点あり）
- DaVinci Resolve: MCP対応でローカル環境が注目
- irodori TTS: ボイスクローン性能の調整
- dasiwa: ref2vaで最も安定・高品質
- audio.cpp: Linux+Radeon/macOS向けCLIツール
- Claude: UI・カスタムノード作成の相談先
- DrawThings: MiniMaxH3対応（モデルサイズで断念例）
- ControlNet: 構図参照用途で活用
- SageAttention2系 / ComfyKittichnAttention: 将来性・速度・品質のトレードオフ比較

### ツール: Web検索による参考情報
- StabilityMatrix: 複数SDパッケージの一括管理ツールの特徴
- LM Studio: 活発更新のGUIツール（llama.cpp制御・画像サポート）
- Krea2: 画像生成基盤モデルのスタイル制御強み
- YuE2-3B: 音楽生成モデルのComfyUIサポートとSuno代替性
- 2026年9月13日時点の検索に基づく最新動向

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出テキストに基づく）**

抽出されたテキストから、生成AIワークフローで活用されている主なツールをまとめました。モデル名・生成エンジン自体は除外し、ツール・インターフェース・マネージャー・ワークフロー支援ツールに焦点を当てています。各ツールについて、ログ内の言及内容と「選ばれている理由」（明記されている場合）を記載します。理由が明記されていないツールについては、活用文脈のみを記載しています。

### 1. ComfyUI（最も頻出・中心的ツール）
- **主な言及内容**: 画像・動画・音楽生成のワークフロー実行環境として複数回登場。バージョン0.35.0でのVRAM消費増加やOOM対策、カスタムノード作成・更新、AVIF/JPEG XLメタデータ保存対応、Context LoopやComfyUI-llama-cpp_vlmなどのノード活用が話題。StabilityMatrix経由の導入や、Forge neoとの比較で「新モデル対応速度の速さ」が評価される。LLM・動画・音声など画像生成以外でもComfyUI一択になりつつあるとの声あり。
- **選ばれている理由**:
  - 新機能・新モデルへのゼロデイ対応が速い（Codexリセット対応やMiniMax H3対応など、Forge neoより根回しが早い）。
  - カスタムノード作成・ワークフローの柔軟性が高い（LLMにノードを作らせやすい、UI非対応モデルでも扱える、再現性が高い）。
  - VRAM管理や自動アンロード制御がワークフロー内で可能。
  - 将来的なComfy本体サポートの見込みや操作の楽さ（ComfyKittichnAttention推奨の文脈）。

### 2. Codex（Codex系ツール/インターフェース）
- **主な言及内容**: プロンプト作成、システムプロンプト作成、ComfyUIカスタムノード作成、仕様検討、コンテキストループワークフローの改造、キャラ×シチュの完全自動生成（60枚ストーリー＋モザイク）などを任せる用途。ChatGPT系ツールとして$200プランやリセット話題も。
- **選ばれている理由**:
  - プロンプト生成・コード生成の精度と柔軟性が高い。
  - 複雑なワークフロー（コンテキストループなど）の改造が容易。
  - 単なる生成ツールではなく「仕様を考えたり作らせたりする過程が楽しい」共同作業者として機能する点。

### 3. LM Studio
- **主な言及内容**: ComfyUIとAPI連携、VLM（画像認識）時のエラー対策（Physical Batch Size変更）、Gemmaモデルクラッシュ回避、VRAM使用量目安運用、MTP対応確認。
- **選ばれている理由**: 設定変更（特にバッチサイズ）が簡単で、画像認識のトラブルシューティングがしやすい。エンジンバージョン切り戻しが容易。

### 4. StabilityMatrix
- **主な言及内容**: ComfyUI（0.35など）の導入・管理に使用。
- **選ばれている理由**: 明記なし（ComfyUIの簡単な導入・管理ツールとして活用）。

### 5. Krea2
- **主な言及内容**: キャラLoRA検証（キャプションをユニークタグ化して複数キャラLoRA作成）、文字入れ機能やGPT Image 2.5との比較。
- **選ばれている理由**: キャプション単位で服の着脱制御がしやすい、複数キャラの混在を抑えやすい点。

### 6. その他のツール
- **Animerge**: LoRAマージツール。更新でGPU使用化や不具合修正が行われ、LoRAマージ作業の利便性向上を目的に使用。
- **MMAudio**: 効果音生成ツール。ローカル生成可能という点で言及（Minimax H3との比較で「ローカルで効果音を生成できる」点が評価されるが完成度は不十分）。
- **YuE2 3B（ComfyUIカスタムノード経由）**: 音楽生成ツール。ローカルでメロディー＋インストゥルメンタル出力可能、Suno代替として期待、abc譜出力で事前確認可能という理由で言及。一方、インスト曲作成の弱点も指摘。
- **DaVinci Resolve**: MCP対応というニュースで言及。ローカル環境の必要性が高まった点が注目。
- **webUI / Forge（A1111系）**: ComfyUIとの比較で「画像生成だけはForge neoを使いたい」という声。ComfyUIほどの新モデル対応速度はない。
- **irodori TTS**: ボイスクローン性能の調整に言及（感情指定や類似度向上のための試行）。
- **dasiwa（ref2va / I2Vツール）**: ref2va用途で最も安定・高品質と評価。
- **audio.cpp**: Linux+RadeonやmacOSでのCLIツールとして紹介。
- **Claude**: UI作成やカスタムノード作成の相談先として推奨。
- **DrawThings（Mac）**: MiniMaxH3対応で言及（モデルサイズが大きすぎて断念事例あり）。
- **ControlNet（openpose / scribble）**: 構図参照用途で過去から活用。
- **SageAttention2系 / ComfyKittichnAttention**: 将来性・速度・品質のトレードオフで比較され、後者が「Comfy本体サポートの見込み」と「楽さ」で推奨。

全体の傾向として、**ComfyUIを中心としたカスタムノード・ワークフローの柔軟性**と**Codex/LM StudioなどのAI支援ツールとの連携**が強く、VRAM管理や新機能対応の速さが重視されています。

## Web検索による参考情報
- **ComfyUI**: 2026年9月時点でv0.35.0がリリースされており（9月9日頃）、Pixal3D Multi-ViewやSenseNova U1.5などの新モデルサポート、新ノード追加が行われている。GitHubコミットも活発で、パートナーノードの更新が頻繁。StabilityMatrixとの統合も公式にサポートされている。[[1]](https://sourceforge.net/projects/comfyui.mirror/files/)[[2]](https://docs.comfy.org/ja/changelog)
- **StabilityMatrix**: ComfyUIを含む複数のStable Diffusion系パッケージを一括管理するマルチプラットフォームツール。ワンクリックインストール・更新、共有モデルフォルダ管理、カスタムノード対応が特徴。ComfyUIパッケージを独立して扱いつつInference UIと連携可能。[[3]](https://github.com/LykosAI/StabilityMatrix/blob/main/README.md)[[4]](https://docs.lykos.ai/stability-matrix/advanced/comfyui-integration)
- **LM Studio**: 2026年も活発に更新されており、v0.4.xシリーズで高度なllama.cpp引数制御、画像サポート強化、Bionicエージェント機能（クラウドモデル連携含む）が追加。VLMトラブルシューティングやパラメータ細かく制御しやすいGUIツールとして位置づけられる。[[5]](https://lmstudio.ai/changelog/lmstudio)[[6]](https://overchat.ai/ai-hub/ollama-vs-lm-studio-vs-atomic-chat)
- **Krea2**: 2026年5月頃にKrea.aiからリリースされた自社開発の画像生成基盤モデル。スタイル参照・ムードボード・創造性パラメータによる美的制御に強みがあり、RAW/Turboの2バリアントが存在。LoRA訓練やスタイル制御用途でログの活用文脈と一致。[[7]](https://www.krea.ai/index/krea-2-image-model)[[8]](https://github.com/krea-ai/krea-2/blob/main/README.md)
- **YuE2-3B**: 2026年9月9日頃にm-a-pチームからリリースされた3B規模の音楽生成モデル。歌詞＋スタイルから48kHzステレオ楽曲を生成し、編集可能なスコア（メロディー/コード）を出力可能。ComfyUIネイティブサポート（yue2ブランチ）が追加されており、Suno代替として評価されている。[[9]](https://comfyui-wiki.com/en/news/2026-09-11-yue2-3b)[[10]](https://localmodelwatch.tsuchitsuchi.com/en/2026/09/10/yue2-3b-music-generation-model/)

これらの情報は2026年9月13日時点の検索に基づきます。ログ内のバージョン言及（例: ComfyUI 0.35.0）と一致する最新動向を確認できました。
