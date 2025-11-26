# なんJ AI生成スレッド（Res 4-241）レポート

## 概要
- **スレッド期間**: Res 4 から 241 まで（主に2024年後半の議論）。
- **主なテーマ**: ComfyUIを中心としたローカルAI画像/動画生成ツールの活用、トラブルシューティング、ハードウェア最適化。Wan2.2、Qwen-Image-Edit（2509/2511）、PainterLongVideoなどの動画生成モデルがホットトピック。エロ生成（NSFW）Tips、メモリ/VRAM問題、RTX5090 BTO購入報告が活発。
- **参加者傾向**: 実践派が多く、ワークフロー共有、Gemini/ChatGPT活用、カスタムノード作成を議論。初心者質問から上級者Tipsまで幅広い。
- **全体トーン**: 技術共有が中心。サンガツ（感謝）多めで協力的な雰囲気。エロ特化（中出し/アナル/セックス動画）生成が半数以上を占める。

## 主要トピック別まとめ

### 1. ComfyUIのUI/運用Tips
- **ノード管理の不満と解決策**:
  - ノードズレ/リンク見づらさ: `設定 > Lite Graph > 常にグリッドにスナップ`（Res45）、スペースキー+ハンドアイコンで移動（Res46）、Ctrl+Zで戻す（Res70）、ピン止め推奨（Res48）。
  - リンク表示: Quick Connectionノードで回路図風（Res67）、Altキー+ドラッグで曲げ（Res74）。
  - カスタムノード推奨: custom script（オートコンプリート）、rgthree（Seed/Power LoRA）、Impact-Pack（ワイルドカード/ディティラー）（Res59）。InspirePackでA1111モードKsampler（Res97）。
- **Forge Neo移行議論**: Comfyより速いがカスタムノード非対応（Res57/82）。Qwen対応済み（Res87）。
- **問題点**: カスタムノード多すぎで起動不可（Res50）、生成集中妨害（Res54）。

### 2. 動画生成（Wan2.2 / PainterLongVideo / Qwen）
- **長尺動画突破（5秒の壁）**:
  - PainterLongVideoで6段30秒生成成功例多数（Res61/68/152）。Smoothmix LoRA使用（Res30関連WF）。
  - Tips: MotionFrames増/End Image交互指定で繋ぎ目改善（Res152/153）、UnloadAllノード避け（Res96）、Subgraph化でシード再利用（Res64失敗談）。
  - WF例: セックス20秒（ピストン→中出し、LoRA調整推奨 Res194）、ループ改造で口パク/Music（Res209）。
- **モデル比較**:
  | モデル | 特徴 | 推奨用途 |
  |--------|------|----------|
  | PainterLongVideo | 長尺/安定 | メイン（FLF2V/I2V不要？ Res75/78） |
  | Smoothmix Wan2.2 | FP16/FP8で低スペOK | 3段サンプラー（Res105） |
  | FunControl/Animate | Video2Video楽（Res210/212） |
- **Qwen関連**: Rapid-AIOエラー（ドライバ/NVIDIA更新 Res65/71/73）、メモリ不足（Res127/142）。表情キープ難（Res40）、実写化Tipsなし。

### 3. プロンプト/生成Tips（主にNSFW）
- **性別/体型問題**: `fat`で男太りやすい→`curvy/plump`で女寄り（Res41/115/119）。自然言語モデル（Rouwei-Gemma）で改善期待も混ざりやすい（Res126/143）。
- **表情/安定化**: 会話形式プロンプト（Res51）、End Imageで顔固定（Res136）。
- **LoRA/モデル**: BananaでSAMPLE文字除去（Res72）、Qwen Anime Beta2 FP8（Res115）。Rouwei-Gemma: 自然言語強いが生成時間4倍/エロ弱（Res143/163）。
- **他**: 中出しガチャ運ゲー（Res100）、参考画像無視ポンコツAI（Res205）。

### 4. ハードウェア/環境問題
- **RTX5090 BTO熱狂**: Frontier 60万切り売り切れ→クリスマス62万（9950X3D/64GB/1200W Res168）。コスパ神（Res49/52/56）。
- **メモリ/VRAM必須量**:
  | 用途 | 推奨RAM | 備考 |
  |------|---------|------|
  | Qwen Edit (BF16) | 128GB | 64GB足りず（Res114/116/117） |
  | 動画長尺 | 96-128GB | DDR5推奨、値上がり中（Res122/125） |
  | iGPU併用 | 効果薄/クラッシュ注意 | 生成速さ変わらず（Res93/103/106/137） |
- **PyTorch問題**: 2.8.0+でLoRA/WANクラッシュ→2.7.1固定（Res44）。torch2.9.0+rgthreeでOK例（Res111）。
- **グラボ相談**: 1070Ti→4070TiS/5070Ti（PCIe4.0OK、RAM128GB推奨 Res185/197）。改造3080 20GB（Res198）。

### 5. 新情報/ニュース
- **Qwen Image Edit 2511**: 来週リリース？ Infinit Decomposition（レイヤー分割: テキスト/人物/背景）で透過PNG/切り抜きGE（Res81/85/121）。T2I対応（Res88/89）。
- **他モデル**: NanoBanana Pro（Gemini連携漫画生成 Res223/232/235）、wan2.5 80GB想定（Res204）。
- **API/クラウド**: Google AI Pro月2900円（Veo/NanoBanana Res223）、DeepL翻訳推奨（Res177）。

## 注目Tips集
- **初心者即戦力**: rgthree/Impact-Packインストール（Res59）、Geminiでカスタムノード作成（Res218）。
- **トラブル**: エラー時はドライバ/nvidia-smi確認（Res84）、仮想メモリ増（Res155）。
- **将来トレンド**: メモリゲー加速（Unifed Memory256GB？ Res174）、AIブームで価格高騰継続（Res122/144）。

## 結論/トレンド
- **進化点**: ローカル動画生成が30秒超え安定、Qwen2511でEdit特化強化。ComfyUIはTips次第で神UI。
- **課題**: メモリ高騰/低スペ限界、自然言語のエロ精度。RTX5090+128GBがエンドゲーム環境。
- **コミュニティ価値**: WF/画像共有多（Res30/100/101/191）、Gemini活用で自作ノード増加。次スレで2511実機報告期待。

（総レス約200、画像/WF貼り20+。エロ率高く実践志向強め）