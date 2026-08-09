# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUI（本体・カスタムノード・ワークフロー）
- ComfyUI v0.30.2→0.31.0アップデートでkijai 4step LoRAの動作・音質・生成速度が改善された一方、T8 Cache停止やモデル破損事例が発生。
- StabilityMatrix経由更新はReleaseタグ限定のため最新版到達が難しく、GitHubコミットハッシュ直接指定が必要になるケースがある。
- ComfyUI-LoRA-Block-Filter / rgthree Power LoRA Loader / LoRA ManagerはCivitai連携によるトリガーワード取得が容易で、特にPower LoRA Loaderの使い勝手が評価されている。

### ツール: バージョン管理・インストール支援ツール
- StabilityMatrixは複数UIの一元管理・更新が可能で初心者向けインストール手段として機能するが、Releaseタグ限定のため最新版到達を阻害する点が指摘される。
- EasyWan22はWan 2.2向け簡単Windowsインストーラーとして言及されるが、メンテナンス停止によるインストール失敗のため非推奨とされる。

### ツール: LLM関連ツール（ComfyUI連携含む）
- ollama / llama.cppは自動unload挙動やComfyUI直接呼び出しで活用される。
- OpenRouter APIはサブスクより安価でプロンプト生成用途に十分と評価される。
- Codex（LM Studio + ComfyUI API一括操作）、Msty Studio（Deepseek API接続）、Claude/Grok（ワークフロー作成・プロンプト変換）が補助ツールとして挙げられる。

### ツール: Web検索による参考情報
- ComfyUI v0.31.0は2026年8月7日リリースでWan-Animate2ネイティブサポート、MiniMax H3 VAE修正、Flux 3 videoサポートを含む。
- Power LoRA Loader (rgthree) / LoRA Managerは複数LoRA扱いやCivitai連携・トリガーワード取得を容易にする人気カスタムノード。
- 検索結果は2026年8月時点の情報に基づく。

---
# 元の本文
**生成AI関連ツールのレポート**

ログから抽出された主なツールは、**ComfyUI**（およびそのカスタムノード・ワークフロー関連）とその周辺ツール（バージョン管理・クラウド・LLM連携）です。A1111（Automatic1111 webUI）やEasyWan22などの言及もあります。モデル名・LoRA・最適化手法（Sage Attentionなど）自体は除外し、ツール・運用・選定理由に焦点を当てています。

### 1. ComfyUI（本体・カスタムノード・ワークフロー）
ComfyUIはログで最も頻繁に言及されるツールで、ワークフローの柔軟性・ノード組み合わせによる高速化・VRAM管理のしやすさが評価されています。

- **本体更新・管理の話題**  
  バージョンアップ（0.30.2 → 0.31.0など）でkijai 4step LoRAの動作改善、音質向上、生成速度向上（例: animaで27秒→16秒）などの報告がある一方、T8 Cacheの動作停止や「comple model +」の破損事例も確認されています。StabilityMatrix経由の更新は「Release」タグのみ対応するため、最新版（v0.31.1系統など）に上げにくい点が指摘され、GitHubのコミットハッシュ直接指定が必要になるケースがあります。[[1]](https://docs.comfy.org/changelog)

- **選ばれている主な理由**  
  - ワークフローの柔軟性が高く、自作カスタムノードやノード組み合わせ（Patch Sage Attention KJ + Patch Sol-Attn + MiniMax H3 Block Cache (T8) など）で大幅な速度向上を実現可能。
  - セットアップの容易さ：「テンプレートを開いてエラーの箇所をクリックし、モデルをダウンロードするだけ」で始められ、ほぼコアノード中心で動作するためカスタムノード地獄を回避しやすい。
  - VRAM管理オプション（`--fast-disk`でメモリ使用量30GB削減、`--reserve-vram`など）が低VRAM環境（16GB）でも安定運用を可能にし、ブラウザ最小化でデコード速度が劇的に向上する運用Tipsも共有されています。
  - ローカルサーバー化により複数PCからAPI操作可能で、画像生成PCとLLM PCを分離した運用も容易。

- **主要カスタムノード・拡張**  
  - **ComfyUI-LoRA-Block-Filter / rgthreeのPower LoRA Loader / LoRA Manager**：Civitai連携でトリガーワード取得が容易な点が好評。Power LoRA Loaderは使い勝手が特に優れていると評価。
  - **LLM呼び出しノード**（`comfyui-lmstudio-image-to-text-node`、`QwenVL`、`ComfyUI-llama-cpp_vlm`）：生成後にモデルを自動でVRAMから降ろせるため、VRAM16GB環境でもプロンプト生成→画像/動画生成を1ワークフローで完結しやすい。LM Studio常駐不要でComfyUI単体完結を評価する声多数。
  - **MiniMax H3関連ノード**（Kijai版 / larryvrh版 / drbaph版のTurbo LoRAノード、ref2va/fl2va、Directorノード）：参照画像扱いや長尺生成に適したワークフロー構築が活発。
  - その他：`Apply Anima LLLite`（コアノード版がカスタムノードより安定と評価）、`google translate text node`（アカウント不要でエロいプロンプト翻訳可能）。

### 2. A1111 (Automatic1111 webUI)
生成速度低下の報告に対し、「旧Lycoris拡張機能を削除せよ」との解決策が提示されています。ComfyUIほど詳細なノード議論はなく、シンプルな用途での利用が想定されます。

### 3. バージョン管理・インストール支援ツール
- **StabilityMatrix**：ComfyUIなどの複数UIを一元管理・更新できるツールとして複数登場。Releaseタグのみ拾う挙動が最新版到達を阻害する点が指摘される一方、初心者向けの簡単インストール手段として機能しています。
- **EasyWan22**：Wan 2.2向けの簡単Windowsインストーラーとして言及されますが、「メンテナンス停止によりインストールに失敗する」ため**明確に非推奨**とされています。選定理由の逆として、メンテナンス状況が重要である点が示されています。

### 4. クラウドGPUレンタルツール（runpod / vast.ai / Comfy Cloud）
- **runpod / vast.ai**：未使用時はほぼ料金が発生せず（数十GBで1日10円程度）、自前GPUに負担をかけない点が利点。自作カスタムノード・ワークフローがそのまま使える自由度も高評価。一方、データ送受信の煩雑さ、週末のGPU枯渇、操作性の面倒さが欠点として挙げられます。
- **Comfy Cloud**：自作カスタムノードが使えないため、ほぼ選択肢外とされています。
- **選ばれている理由（ローカル vs クラウド）**：所有欲・所有権、手元にPCが残る安心感、自作ノードの完全自由度を重視する人はローカルComfyUIを優先。クラウドは「使いたい時に使えない」リスクを懸念する声があります。

### 5. LLM関連ツール（ComfyUI連携含む）
- **LM Studio / LM Link**：複数PC間でモデル共有し、画像生成PCからLLM推論を別PCにオフロード可能。RAM圧迫環境でも利用しやすく、VRAM管理に寄与。
- **ollama / llama.cpp**：自動unload挙動やComfyUI直接呼び出しで活用。
- **OpenRouter API**：サブスクより安価でプロンプト生成用途に十分と評価。
- **その他補助ツール**：Codex（LM Studio + ComfyUI APIの一括操作・Unload/Load自動化）、Msty Studio（Deepseek API接続）、Claude/Grok（ワークフロー作成支援やプロンプト変換）。

**全体の傾向と選定理由のまとめ**  
ComfyUIは「柔軟性・高速化・VRAM効率・セットアップ容易さ」が最大の強みで、ノード組み合わせやカスタムノード作成（GPT/Sol兄貴に依頼可能）の容易さが支持されています。一方、クラウドツールはコスト・負担軽減を重視する場面で選ばれ、メンテナンス停止ツール（EasyWan22）は即非推奨となります。ローカル環境の所有感とクラウドの柔軟性のトレードオフが繰り返し議論されています。

## Web検索による参考情報
- **ComfyUI v0.31.0**：2026年8月7日リリース。Wan-Animate2ネイティブサポート、MiniMax H3関連のVAE修正、Flux 3 videoサポートなどが含まれる最新版。[[1]](https://docs.comfy.org/changelog)
- **StabilityMatrix**：ComfyUIをはじめとする複数AI WebUIを一括インストール・管理・更新できるオープンソースのデスクトップアプリとして広く利用されており、ComfyUI Managerの統合もサポート。[[2]](https://lykos.ai/)
- **EasyWan22**：Wan 2.2向けのWindows向け簡単環境構築ツール（ComfyUIベース）として存在し、32GB RAM / 8GB VRAM以上を推奨。ただしメンテナンス状況により利用しにくくなる可能性が指摘される。
- **Power LoRA Loader (rgthree) / LoRA Manager**：ComfyUIの人気カスタムノード/拡張で、複数LoRAの扱いやCivitai連携・トリガーワード取得を容易にする機能が特徴。[[3]](https://github.com/willmiao/ComfyUI-Lora-Manager)

（検索結果は2026年8月時点の情報に基づく）
