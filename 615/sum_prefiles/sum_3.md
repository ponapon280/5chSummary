# なんJ(5ch) AI生成スレッド レポート (ログ: 438-638)

## 概要
このログは、主に**ComfyUIを中心としたAI動画/画像/音声生成ツール**の議論が中心。ComfyUIのインストール方法、HeartMula/LTX-2/WAN2.2などの新ツールの導入・トラブルシュート、LoRA学習、音声生成（TTS/音楽）、クラウド（runpod/Antigravity）の活用がホットトピック。参加者は「赤ちゃん」ユーザーから上級者まで多岐にわたり、互いにアドバイス交換。進化の速さを嘆く声が多く、**ローカル環境構築の難易度**と**生成クオリティのガチャ性**が共通の悩み。エロ/二次元派生への期待も強い。

**ログ期間推定**: 最近（2025年頃？ ComfyUI Manager統合2025/12月言及）。総レス約200、活発。

## 主要トピックまとめ

### 1. ComfyUIインストール・環境構築 (>>455->>508, >>470->>504 など最多議論)
- **Desktop版 vs Portable版**:
  | 種類 | メリット | デメリット | 推奨ユーザー |
  |------|----------|------------|-------------|
  | **Desktop版** | 自動venv構築、AMD対応、検証済みアップデート、Manager統合（2025/12～）。 | 最新機能遅れ、カスタムノード制限？（>>483否定意見も）。 | 初心者/安定志向。 |
  | **Portable版** | 即時最新、柔軟（用途別複数環境）。ComfyUI Manager手動git clone。 | 初期セットアップ煩雑、venv手動。 | 上級者/カスタム多用。 |
- **ComfyUI Managerの変化**: 本体統合（>>484）。git clone（Legacy）or pip+起動引数（--enable-manager / --enable-manager-legacy-ui）。新UIはCustom Nodes Managerのみ、文句多し（>>505）。初回: Managerインストール→更新→Install Missing Custom Nodes。
- **トラブル&解決**:
  - SageAttention: wheel逆算インストール推奨（>>512）。Stability Matrix任せ（>>477）。
  - 記事注意: 古いnote/money化記事避け、GitHub/チャッピー/Civitai優先（>>476-480）。
- **アドバイス聖人まとめ**: >>460のWiki風記事絶賛（分類・評価詳細）。Portable推奨多め（古参ユーザー）。

### 2. HeartMula (音楽生成新星、>>454->>542, >>531->>557)
- **導入**: ComfyUI Portable推奨。GitHub例WFドラッグでノード読み込み（>>531初生成成功！）。ffmpeg依存: full-shared版DLLをtorchcodecへコピー。
- **性能**: Python3.10推奨。VRAM12GBで2分30秒曲→3分（10it/s）。バラード多め（melodic speed metalもスロー）。**instrumental**: "instrumental,"プロンプト（>>529）。女声: "female voice, cute sweet girl voice"（歌詞男言葉避け）。
- **Tips**: Suno代替？ TODO（reference audio, hot song）期待。ラップ/電波ソング（Denpa song）可。不協和音/rhythm崩しで民謡風。
- **生成例**: 日本語理解◎（Comfy仲良しソング>>542）。Ace-Step比較でHardstyle成功（>>543）。

### 3. LTX-2 / リップシンク (>>456, >>489, >>512, >>569)
- **性能**: 12GB WFで5分ゴミ（Q4 gguf二次弱）。アニメLoRA新着（Civitai）。distill版（ltx-2-19b-distilled_Q8_0.gguf）はLoRA内蔵少ステップモデル。
- **使い方**: WAN2.2 PainterLongVideo（20秒口パクなし）→LTX-2リップ。InfiniteTalk（中国語母音◎、日本語可）推奨。英語リップ良、ネイル変動→SAM3非実用的（一貫性なし）。
- **課題**: SageAttention未対応エラー。二次溶けやすい（i2v改良期待>>616）。

### 4. 画像/動画生成進化・ツール (>>442, >>447, >>560など)
- **最新ニュース**:
  - Flux.2 Klein出た（9b/4bタグ）。
  - Z-image: Base未公開（omni base support追加で近日？>>627）。ターボ無印期待→SD並エロ派生。
  - WAN2.2: EasyWan22 venv自動。SVI連続生成（lowリファイナー噛ませ？）。
  - Qwen TTS/VL: 日本語◎、Apache2ライセンス。喘ぎ？未確認。キャプションガバ（二次2girls誤認）。
- **LoRA学習**: バッチサイズ「正解なし」（VRAM大→平均化、キャラ小→詳細）。秘伝のタレ（環境/素材依存）。
- **Detailer**: ADetailer古め（チャッピー参考）。オマンコ特化移植例。

### 5. 音声/TTS/ボイチェン (>>446, >>452, >>594, >>612)
- **RVC**: 古臭いボイチェン感。WAN+RVC喘ぎシンプル（>>448）。
- **TsukasaSpeech**: 長文流暢、ローカル可。喘ぎ/短文弱。
- **新**: Qwen3-TTS（1.7B学習可）、Male finishing v2。鳩村（Suno？）instrumental謎歌声。
- **SUNO/島村卯月**: ペルソナ課金で声指定。オフボーカル分離完璧。

### 6. クラウド/その他トラブル
- **runpod**: サーバーレスthrottled高確率（WAN動画24/32GB）。リージョン/GPU無関係。
- **Antigravity**: ウルトラ契約でも応答不能増（quota浪費）。Comfy構築AIに弱（>>511迷走）。
- **Xアルゴ**: Grokスコア単純、リプライ誘発優先でインプレ減。
- **ハード**: VRAM8GB i2v3時間。PC100万コース。SSD値上がり注意。

## 注目生成例・ミーム
- HeartMula: ラップ女声変換（>>574）、電波ソング（>>592）。
- エロ期待: 膣内射精ネタ（>>453）、ゲーミング電柱/ちんぽ盆栽（>>536）。
- 中華サイト: 規制なし裸動画15円/分（WANカスタム？）。

## トレンド&今後期待
- **ローカル最強**: 無料（電気代無視）。クラウド金/規制/速度で劣勢。
- **二次元渇望**: Z-image Base/i2v LTX-2でエロLoRA爆増期待。Danbooru必須。
- **進化速すぎ**: 月単位変化（>>485）。生成フロー: 画像ガチャ→動画→音付け（1h/5秒）。
- **初心者アド**: 手を動かせ（>>473）。チャッピー/Civitai/GitHub聖典。

**総評**: コミュニティの親切度高（サンガツ連発）。「赤ちゃん」歓迎ムードで敷居低。次スレテンプレに>>460採用提案。エロASMR/アイドルハメ動画世界早よ（>>549-551）。