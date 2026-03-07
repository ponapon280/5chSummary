# なんJ AI画像生成スレッド ログレポート

## 1. スレッド概要
- **ログ範囲**: レス9〜239（抜粋）。主にStable Diffusion（SD）関連ツールの議論。ComfyUI、Forge Neo、Anima、Wan2.2などの画像/動画生成ツールを中心に、UI比較、ハードウェア問題、モデル学習、TTS拡張などが話題。
- **参加者傾向**: AI生成愛好家（主にローカル環境ユーザー）。ComfyUIの不安定さを嘆く声多し。一方、Forge NeoやStability Matrixの利便性を推すレスも目立つ。エロ/NSFW生成のTips共有が活発。
- **全体トーン**: 技術共有と愚痴のミックス。更新頻度の高さによる不具合、PCパーツ高騰への絶望感が強い。AI（Gemini/ChatGPT）依存の是非も議論。

## 2. 主要トピックと議論ハイライト

### 2.1 ComfyUI関連（最多話題）
- **更新問題**: v0.15.1でQwen/Qwen Image Editが激遅、Torch Compile挙動不良、複数WFタブ切り替えで上書きバグ。Frontend v1.39.19でWebPメタデータ読み込み不能（PNG推奨）。解決策: `--disable-dynamic-vram`、Frontendバージョンロールバック（起動引数 `--front-end-version`）、git pull後の動作確認必須。
- **Dynamic VRAM**: VRAM効率化機能だがSDXL 1024x1024で1.5倍遅延報告。メインメモリ活用でRAMピーク減るが、キャッシュ管理が原因で減速/ノード相性悪化の懸念。
- **学習/導入Tips**:
  - LoRA Manager推奨（画像保存/メタデータ抽出便利）。
  - 初心者: Anima/Zimage公式テンプレWFから開始。EasyWanは特殊WFでComfyUI理解の妨げ。
  - SAM3: `yolain/ComfyUI-Easy-Sam3` or `PozzettiAndrea/ComfyUI-SAM3`（環境破壊注意）。Hand検出で`v hand,`記述、Denoising調整、サブグラフ内設定。
- **不満点**: Verアップ怖い、カスタムノード互換性なし（審査なし）。「neoで十分、Comfyは動画限定」との声多数。

### 2.2 UI/ソフト比較
| UI/ソフト | 推奨ポイント | 問題点 | ユーザー声 |
|----------|-------------|--------|------------|
| **Forge Neo** | Anima対応、SAM3使用可、LoRA管理楽。Stability Matrixで独立インストール。 | 初回真っ黒画像（Schedule Type: Automatic→手動、UI Preset/Animaモデル/VAE/TE設定）。 | 「Comfyより簡単」「EasyReforge代替」 |
| **EasyReforge** | 使い慣れ。 | Stability Matrix移行時Git/Python設定変更注意（既存環境壊れず独立可）。 | 複数ソフト併用でMatrix推奨。 |
| **Anima** | i2i弱いがLoRA学習自然言語キャプション可（タグより）。 | SDXL従量課金、解像度1536学習で顔崩れ（旧wai14推奨）。 | 「リアス並エロ待ち」「Forge Neoでテスト」 |
| **Stability Matrix** | 独立環境、Git/Python個別管理。Gemini説明引用多（「箱の中の小部屋」）。 | 初回エラー報告（Git/Patron=Python誤読）。 | 「入れて損なし」「パーツ高騰下の救世主？」 |

- **移行アドバイス**: EasyWan→標準WFでComfy学習。WF JSONをChatGPTに投げ解説。

### 2.3 モデル/生成Tips
- **Wan2.2**: ローカルComfyでNSFW制御難（マージモデル推奨）。乳房指示で隠れ/変顔→学習不足かプロンプト不良。
- **リアスモデル**: v3.6、1536解像度学習（1024+1536併用推奨）。「最新≠最善」（wai12/14継続使用）。
- **Irodori-TTSフォーク** (Aratako/Irodori-TTS): 新機能（LM Studio API連携、絵文字キャプション、感情推定、マージ）。300-4000ステップ学習、Early Stopping、Whisper middle注意。SVB2ツール代替。
- **その他**:
  - NSFW妨害回避: マージモデル。
  - Vポーズ: `v posing`→Vサイン誤認識。
  - Grok動画: ノーパン生成事故（エロ対応）。

### 2.4 ハードウェア/経済話題
- **PCパーツ高騰**: SSD 2TB+4万、5090 PC 76万。メモリ急騰で格安PC絶滅危機（Gartner予測）。Dynamic VRAM惜しむ声。
- **FRONTIER BTO**: セール時正解。ホルムズ海峡封鎖でガソリン/電気代加速懸念。

### 2.5 AIツール活用とメタ議論
- **Gemini/ChatGPT批判**: Python=パトロン誤読、回答貼り付けNG（裏取り必須）。Grok4.2推奨（最新まとめ有能）。
- **Claude戦争ネタ**: イラン攻撃にClaude使用疑惑（未確認）。
- **未来予測**: AI責任押し付け増加懸念。

## 3. 問題解決まとめ
- **Comfy真っ黒**: Anima Preset + モデル/VAE/TE指定、Schedule手動。
- **SAM3 Hand無効**: `v hand,` + Denoising up、text multilineカンマ接続。
- **TTS学習失敗**: ステップ調整（過学習避け）、train_v1.yaml、LossログAI分析。
- **Frontendバグ**: PNG保存、古いVer警告。

## 4. 注目すべき新情報
- **Irodori-TTSフォーク**: 実用度高（絵文字/感情自動）。Kolboldcpp対応、軽量LLM推奨。
- **Smooth Workflow Wan 2.2 v3.0 AIO**: 動画ボヤ/音声エラー報告（未解決）。
- **Qwen3.5軽量版**: 導入検討中。

## 5. 結論と示唆
スレはComfyUIの不安定さが最大の不満源だが、Forge Neo/Stability Matrixで解決余地大。動画/高度生成志向者はComfy必須。パーツ高騰下、Dynamic VRAM活用が鍵。TTSフォークのようなユーザー拡張が活発で、コミュニティの創造性が高い。次スレではAnima正式版/Forge Neo安定化報告期待。

（生成日: ログベース。最新情報はCivitai/公式確認を）