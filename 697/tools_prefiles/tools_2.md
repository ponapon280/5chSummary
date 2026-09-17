**抽出されたツール関連の話題（モデル除外）**

### ComfyUI（comfy）関連
- **IP-Adapter関連のトラブルと解決**:
  - `ip_adapter-Character_Reference-10.safetensors` を `ComfyUI/models/ipadapter/` に置いているのに **Anima IP-Adapter Loader** でモデル選択できない問題。
  - **IPAdapter Model Loader** なら選択できる。
  - 原因として「ComfyUI本体のバージョン」やフォルダ配置の確認が挙げられ、githubの説明通りに配置を確認するようアドバイスあり。
  - 最終的に正しいLoaderを使うことで解決した報告。

- **ワークフロー・ノード関連**:
  - **Spectrum**（動画生成ワークフロー？）でstepが飛ばない問題 → **block sparse attentionノード** を使うと解決したが、Windowsの改行コード（CRLF）が原因だった。
  - **Extender**（New Project機能）でプロンプトが空になって不正なクリップが生成されるバグ。**Prompt package Bridge** をバイパスすることで回避できた。
  - **ComfyKittichnAttention / SolAttention** を使うと1MP-15step生成が大幅に高速化（5090で20分超 → 半分近く）。

- **その他の言及**:
  - saveノードからEagleへ自動保存するノードをチャッピーに作ってもらった。
  - 全体として「ノードを細かく調整して最適化していく」楽しさが語られている。

### 画像ビューア関連
- **Eagle**:
  - 去年おすすめされて買ったまま放置していたが、今使ってみて「慣れると結構ええ」。
  - saveノードからの自動保存もComfyUIと組み合わせやすい。

- **HoneyView**:
  - 「なんも困っとらん」との声多数。AVIF/JXL対応を望まない層が支持。

- **MangaMeeya（マンガミーア）**:
  - 長年使っている人が複数。zip開け・webp対応・星レート引継ぎなどが評価。

- **その他ビューア**:
  - irfanview、qView、NeeView、ACDSee、Bandiview などが言及され、「自分用にカスタムしたビューアを作った」という報告も。

### LLM / プロンプト作成ツール関連（画像生成以外も含む）
- **ローカルLLM（Gemma4系規制解除版、MiniMax H3）**:
  - エロプロンプト作成に使用。
  - MiniMax H3は公式SkillsをLM Studioで使っているが、最近のランタイムとの相性が悪いためランタイムバージョンを下げて運用。
  - 「GPTだと弾かれるのでローカルLLMでプロンプトを作っている」という声。

- **Codex**:
  - 画像ビューアのコード作成や、複数のCodex出力を突き合わせて統合する使い方が語られている。
  - 「Codexに任せると味わえない最適化の楽しさ」との対比で言及。

### その他
- **Krea2**（ツール寄りの機能として）:
  - 微妙なニュアンスの調整がしやすい点が評価され、「AnimaよりKrea2の方がやり込める」との声。ただしAnima自体はモデル扱いなので除外。

**特にツールが選ばれている理由として抽出されたポイント**:
- ComfyUI：ノード単位で細かく調整でき、IP-Adapterや動画ワークフローの柔軟性が高い。
- Eagle：saveノード連携が容易で整理が楽。
- HoneyView / MangaMeeya：軽快で必要十分、特殊フォーマット対応が不要な人向け。
- ローカルLLM：検閲回避とプロンプト作成の自由度。