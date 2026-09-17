# 🆕 新規トピック（前回からの差分）
### その他の関連
- ComfyUI-Anima-DAVE custom node：Anima関連の多様性保持に有効
- ComfyUI内マルチテキストエディタ・自作プロンプトエディタ（ツリー構造対応）：プロンプト管理の利便性向上
- saveノードからEagleへ自動保存するcustom node：整理効率の向上

### 画像ビューアー・管理ツール
- Eagle：ComfyUI custom node連携による生成画像の振り返り・自動保存に活用
- HoneyView：軽快で必要十分、AVIF/JXL非対応層に支持
- MangaMeeya：zip開け・webp対応・星レート引継ぎが評価され長年使用例多数
- その他ビューアー：irfanview、qView、NeeView、ACDSee、Bandiviewおよび自作ツール（webp対応改善）が報告され、カスタム運用が現実的
- 画像管理とプロンプト管理の分業：Eagleなどの専用ソフトと別ツールの併用が推奨

### トレーニング・最適化・その他ツール
- musubi-tuner（kohya-ss製）：MiniMax系LoRA学習の最新実装マージ予定で採用、メモリ効率が高くWindows/Linux対応
- DaVinci Resolve：ComfyUI生成長尺動画の編集・繋ぎに使用
- uv：Python環境管理で重複削減・未使用キャッシュ削除によりSSD寿命に優位
- WizTree：ディスク容量内訳調査に便利
- RefMods / Ref2v系ノード（ComfyUI-MiniMaxH3Modなど）：参照精度向上・生成時間短縮、ゼロトレーニング参照アダプタとして機能
- Fable5.1：ComfyUIエラー修正・不要ノード削除で起動時間短縮に寄与

### LLM / プロンプト作成・コード支援ツール（画像生成以外も含む）
- Qwenシリーズ（edit 2511、Qwen3.8など）：編集用途で「簡単で素直で丁寧」と評価、エージェント・カスタムノード作成・キャプション作成・Codex代替としても活用
- Krea2：吹き出し・文字作成、手書き文字学習、anima絵合成ワークフローで使用、微妙なニュアンス調整・やり込みやすさが評価

### 全体の傾向と補足
- ComfyUIエコシステム基盤：custom nodeによる柔軟拡張とビューアー/管理ツールの分業が実用的、ノード単位調整・更新による速度・メモリ改善・連携容易さが理由
- Qwen：非画像生成用途に限定して抽出

### Web検索による参考情報
- Stability Matrix：ComfyUIを含むStable Diffusionパッケージの一括インストール・更新・管理ツール、custom node管理容易
- musubi-tuner（kohya-ss）：HunyuanVideo・Wan・MiniMax-H3対応LoRA学習ツール、メモリ効率が高くWindows対応
- RefMods：MiniMax H3向けゼロトレーニング参照アダプタ（ComfyUI-MiniMaxH3Modなど）、参照精度向上・生成時間短縮
- Fable5.1：ComfyUI専用ツールとしての公開情報が限定的、Qwenはモデルシリーズとして扱われツール用途に限定

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出テキストに基づく）**

ログから抽出された内容は、主に**ComfyUI**を中心としたローカル生成環境の運用・拡張ツール群に焦点が当てられています。モデル性能比較は除外し、ツールの利便性・運用方法・選定理由を優先してまとめています。全体の傾向として、「ComfyUI + custom node + ビューアー/管理ツールの組み合わせ」が主流で、理由として**環境の標準化・拡張性・ワークフロー管理の容易さ・メモリ効率・速度改善**が繰り返し挙げられています。

### 1. ComfyUI（本体・ワークフロー・custom node）
ComfyUIは静止画・動画生成のローカルベース環境として最も頻出。選ばれる主な理由：
- 標準環境が整っており、静止画・動画問わず簡単にDLして利用可能。
- ワークフローやプロンプトをPNGメタデータで保存・共有・再利用できる（Codex連携も含む）。
- 複数GPU構成で動画・参照画像・LLMを並行実行しやすい。
- custom nodeが豊富で、IP-Adapter、block sparse attention、Prompt package Bridge、ComfyKittichnAttention/SolAttention、RefMods（参照精度向上・生成時間短縮）、Media Loader/Prompt Builderなどの拡張が容易。
- 更新（v0.35→v0.36.0など）でVAE高速化、RAM使用量低減、`--fast-disk`自動判定、起動時間短縮などの恩恵を受けられる。
- 動画生成では「VRAM容量ゲー」から「RAM活用による速度ゲー」へシフトし、Fable5.1（エラー修正・不要ノード削除ツール）との組み合わせで起動時間を30秒以上短縮した事例あり。
- トラブル例：IP-Adapter Loaderの選択不可（正しいLoader使用やフォルダ配置で解決）、Spectrumワークフローの改行コード問題（block sparse attentionで回避）など。ノード細かく調整する「最適化の楽しさ」も評価。

**その他の関連**：
- ComfyUI-Anima-DAVE（custom node）：Anima関連の多様性保持に有効。
- ComfyUI内マルチテキストエディタや自作プロンプトエディタ（ツリー構造対応）：プロンプト管理の利便性。
- saveノードからEagle自動保存するcustom node：整理効率向上。

### 2. 画像ビューアー・管理ツール
- **Eagle**：ComfyUI custom nodeと連携し、生成画像の振り返り・自動保存に使用。「慣れると結構ええ」との声。saveノード連携の容易さが理由。
- **HoneyView**：軽快で必要十分。AVIF/JXL対応を望まない層に支持。
- **MangaMeeya（マンガミーア）**：長年使用例多数。zip開け・webp対応・星レート引継ぎが評価。
- その他：irfanview、qView、NeeView、ACDSee、Bandiview。自作ビューアー（Zippla代替、webp対応改善、Leeyesコピー品）も報告され、「自分用にカスタム」する運用が現実的。
- 画像管理はEagleなどの専用ソフト、プロンプト管理は別ツールで分けるのが推奨される声あり。

### 3. プロンプト・ワークフロー管理ツール
- PNGベース管理：ComfyUIのワークフロー/プロンプトをPNGメタデータで保存（サムネ用途でファイルサイズ工夫）。
- 自作/カスタムアプリ：CodexにPNGinfo相当機能やプロンプト管理アプリを作成依頼。ダイナミックプロンプトの長い管理用に専用アプリ検討。
- ComfyUI内プロンプトエディタ（自作・共有例）：ツリー構造など利便性向上。

### 4. トレーニング・最適化・その他ツール
- **Stability Matrix**：ComfyUIやAnima環境の管理・更新に使用。一括インストール・更新、custom node管理、`--use-ck-attention`設定のGUI化が評価。
- **musubi-tuner**（kohya-ss製）：MiniMax系LoRA学習の最新実装マージ予定で採用。メモリ効率が高く、Windows/Linux対応。
- **DaVinci Resolve**：ComfyUI生成長尺動画の編集・繋ぎに使用（ComfyUI単体だと劣化しやすいため）。
- **WebUI（自作）**：自宅サーバー（Mac mini）上のモザイク処理用。iPhoneリモート対応、JPEG XL出力実装。
- **uv**：Python環境管理。重複削減・未使用キャッシュ削除でSSD寿命に優しい。
- **WizTree**：ディスク容量内訳調査に便利。
- **RefMods / Ref2v系ノード**（ComfyUI-MiniMaxH3Modなど）：参照精度向上・生成時間短縮が明確な選定理由。ゼロトレーニング参照アダプタとして機能。
- **Fable5.1**：ComfyUIエラー修正・不要ノード削除で起動時間短縮に寄与。

### 5. LLM / プロンプト作成・コード支援ツール（画像生成以外も含む）
- **ローカルLLM（Gemma4系規制解除版、MiniMax H3）**：エロプロンプト作成に使用。検閲回避と自由度の高さが理由。LM StudioでSkills運用（ランタイムバージョン調整）。
- **Codex**：カスタムノード作成依頼（実際に作ってくれる）、キャプション/ワークフロー改善、PNGinfo相当機能作成。複数の出力統合にも使用。
- **Qwenシリーズ（edit 2511、Qwen3.8など）**：編集用途で「簡単で素直で丁寧」と評価。他編集モデルとの比較で選定。エージェント用途・カスタムノード作成・キャプション作成・Codex代替としても活用。「何でも聞いてくれる」点が利点。
- **Krea2**（ツール寄り機能）：吹き出し・文字作成、手書き文字学習、anima絵との合成ワークフローで使用。微妙なニュアンス調整・やり込みやすさが評価。Civitaiテンプレより自前ワークフロー推奨の声あり。

**全体の傾向と補足**  
ComfyUIエコシステムが基盤で、custom nodeによる柔軟な拡張とビューアー/管理ツールの分業が実用的。理由として「ノード単位の細かい調整」「更新による具体的な速度・メモリ改善」「連携の容易さ」が強調されています。Qwenは非画像生成用途に限定して抽出。

## Web検索による参考情報
- **ComfyUI v0.36.0**（2026年9月15日リリース）：Generic Loops実装、Yue2音楽モデル・Marigold v2サポート、VAE高速化・RAM使用量低減・AMD環境改善などの最適化が含まれる。ログの速度向上・RAM低減・起動時間短縮の記述と一致。[[1]](https://github.com/Comfy-Org/ComfyUI/tags)[[2]](https://localmodelwatch.tsuchitsuchi.com/en/2026/09/16/comfyui-v0360-released/)
- **Stability Matrix**：ComfyUIを含む各種Stable Diffusionパッケージの一括インストール・更新・管理ツール。ComfyUIをバックエンドとしてInference UIを提供し、custom node管理も容易。ログの環境管理用途に合致。[[3]](https://github.com/LykosAI/StabilityMatrix/blob/main/README.md)[[4]](https://docs.lykos.ai/stability-matrix/advanced/comfyui-integration)
- **musubi-tuner**（kohya-ss）：HunyuanVideo、Wan、MiniMax-H3など対応のLoRA学習ツール。メモリ効率が高く、Windows対応。MiniMax系学習の最新実装取り込みで選定理由と一致。[[5]](https://github.com/kohya-ss/musubi-tuner/blob/main/README.md)
- **RefMods**：MiniMax H3向けゼロトレーニング参照アダプタ（ComfyUI-MiniMaxH3Modなどcustom node）。参照精度向上・生成時間短縮が利点で、ログの選定理由と一致。[[6]](https://comfyui-wiki.com/en/news/2026-09-07-minimax-h3-refmods)
- **Krea2**：Krea AIの基礎画像モデル（2026年頃）。美学・スタイル転送重視で、open weights版あり。ログの文字/吹き出し作成や合成ワークフロー用途に適する。[[7]](https://www.krea.ai/blog/krea-2-image-model)
- Fable5.1についてはComfyUI専用ツールとして公開情報が限定的（検索では別ツール/モデルがヒット）。Qwenは主にモデルシリーズとして扱われるため、ツール用途に限定して参照。
