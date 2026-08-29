# 🆕 新規トピック（前回からの差分）
### ツール: 選ばれている主な理由
- 有志調整済みノードの手軽さが利点で、高速化ノード乱立の中でも実用的
- バージョンアップ時のノード互換性リスクを避けるため最新環境追従が推奨
- 360度視点の動画生成が容易で、アート寄り・実写/二次元両対応のニッチ用途に強い
- Krea3のオープンソース化期待によりローカル運用しやすくなる可能性
- 起動・生成管理が容易で複数ツールの統合運用に適する

### ツール: Krea（Krea2 / Krea3）
- Krea2の360ERP機能（パノラマ動画生成・MiniMax H3対応）とLoRA共有が言及され、Krea3のオープンソース化動向も話題

### ツール: Stability Matrix
- ComfyUI起動・管理向けランチャー/パッケージマネージャーとして言及

### ツール: LM Studio（LMStudio）
- ComfyUIと併用されるローカルLLMツールで、エロプロンプト生成やコーディングに活用

### ツール: その他の言及
- electron自作ツールとして背景透過生成物のデスクトップ常時表示アプリを提案
- falをモデル改造・公開プラットフォームとして言及

### ツール: Web検索による参考情報
- ComfyUI v0.34.0（2026年8月25-26日頃）：MiniMax H3ガイド追加、HDRビデオ保存（AV1）、3Dモデルサポート、Gemma4高速化など
- Krea 2 / Krea2 Turbo（2026年5月頃）：美学・スタイル転送特化のスクラッチ基盤モデルで、Turbo版は高速生成・スタイル参照対応、オープンウェイト版も提供
- Stability Matrix：Stable Diffusion系パッケージのワンクリックインストール・管理ツールで、起動引数管理やカスタムノード対応が容易
- 情報は2026年8月時点の公開ソースに基づき、コミュニティ有志による最適化ノードが公式コアと統合されていることを確認

---
# 元の本文
**生成AI関連ツールのレポート**

このテキスト（ログ抽出結果）から、生成AI（主に画像・動画生成）関連ツールとして最も頻繁に言及され、具体的な評価・理由が記載されているのは**ComfyUI**とその周辺（カスタムノード・最適化・起動オプション）です。次点でKrea、Stability Matrix、LM Studioが挙げられます。モデル名自体（MiniMax H3、Qwenなど）の性能議論は除外し、ツール・ワークフロー・運用面に焦点を当てています。

### ComfyUI（およびカスタムノード・最適化）
ComfyUIはノードベースのモジュラーな拡散モデルGUI/バックエンドとして位置づけられ、ワークフロー構築・API制御・動画生成（T2V/I2V）で特に強みを発揮すると評価されています。ログでは複数同時起動、ワークフロー共有、カスタムノードの活用が話題です。

**選ばれている主な理由**:
- **VRAM節約と高速化**: Limiter + Memory Optimization + SageAttention/Sparse Attentionの組み合わせで、生成時間を約半分にしつつVRAMを5GB程度空けられる（SageAttentionオンリー比）。Sparse Attentionの劣化を許容できるVRAMカツカツ環境向けにLimiterとMemory Optimizationを推奨。
- **メモリ対策の柔軟性**: `--disable-pinned-memory`で使用メモリを減らし（生成時間はほぼ変わらないか1-2割増）、`--fast-disk`と組み合わせることで64GB RAM環境でも安定運用可能。グラボの発火防止（特に高性能GPU）にも有効。
- **最新機能・更新追従のしやすさ**: デスクトップ版更新でH3ワークフローのTurbo標準搭載やノイズシード外部出力などの改善。カスタムノードの充実（LoRA Loader互換性対応、Acc-Lora対応PR適用など）により、公式テンプレより柔軟なカスタムワークフローが構築しやすい。
- **ワークフロー向きの特性**: 動画生成で参照画像対応が強く、高速化後の挙動確認がしやすい。API制御しやすく、外部ツールとの併用（LM Studioでの並行プロンプト推敲など）が容易。公式テンプレよりカスタムワークフロー（dasiwa WFなど）の再現性・拡張性が高いとされる。
- その他: 高速化ノードの乱立はあるが、有志調整済みノード（kijai製など）の手軽さが利点。

バージョンアップ時は一部ノードが使えなくなるリスクがあるため、最新環境追従が推奨される点も指摘されています。

### Krea（Krea2 / Krea3）
Krea2の360ERP機能（パノラマ的動画生成、MiniMax H3対応）とLoRA共有が言及され、Krea3のオープンソース化動向も話題です。

**選ばれている主な理由**:
- 360度視点の動画生成が容易で、アート寄り・実写/二次元両対応のニッチ用途に強い。
- Krea3オープンソース化期待により、ローカル運用しやすくなる可能性。

### Stability Matrix
ComfyUIを起動・管理するランチャー/パッケージマネージャーとして言及。SSD読み書き挙動の文脈で使われています。

**選ばれている主な理由**:
- 起動・生成の管理が楽で、複数ツールの統合運用に適する。

### LM Studio（LMStudio）
ComfyUIと併用されるローカルLLMツール（Qwenモデルなど）。エロプロンプト生成やコーディング用途で活用。

**選ばれている主な理由**:
- 生成作業と並行してプロンプト推敲（壁打ち）可能。Deno Local LLM Loaderを使わずLM Studioを選ぶ理由として、並行作業の利便性とVRAM富豪環境での合算活用が挙げられる。

### その他の言及
- **Forge**: A1111系UIの代替としてComfyUIと併用例あり（LM Studioとの同時起動）。
- **electron自作ツール**: 背景透過生成物のデスクトップ常時表示アプリなど、独自用途の提案。
- **fal**: モデル改造・公開のプラットフォームとして言及。
- **civitai**: ワークフロー用データソースとして活用。

全体の傾向として、ツール選択の理由は「VRAM/速度最適化の実効性」「ワークフロー共有・再現性」「最新機能の早期取り込み」「特定ニッチ機能（360ERPなど）の使いやすさ」「並行運用・管理の容易さ」が中心です。特にComfyUIはエコシステムの成熟度とカスタマイズ性が繰り返し評価されています。

## Web検索による参考情報
- **ComfyUI v0.34.0**: 2026年8月25-26日頃リリース。MiniMax H3関連のガイド追加（任意フレームでの画像/音声アンカリング）、HDRビデオ保存（AV1コーデック、mkv/webm対応）、3Dモデル（PixArt 3D、TRELLIS2）サポート、Gemma4テキスト生成高速化などの更新が含まれる。[[1]](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.34.0)[[2]](https://github.com/Comfy-Org/ComfyUI/tags)[[3]](https://docs.comfy.org/ja/changelog)
- **SageAttention / Sparse Attention**: ComfyUI向けのカスタムノード（KJ-Nodesなど）で活用され、量子化・スパース化による高速化（特に長シーケンスの動画生成で有効）とVRAM削減効果が確認されている。SpargeAttnなどの派生も存在。[[4]](https://comfy.icu/node/ApplySpargeAttn)[[5]](https://medium.com/diffusion-doodles/demystifying-attention-in-comfyui-7ad97f6d87bb)
- **Krea 2 / Krea2 Turbo**: 2026年5月頃にKreaの初のスクラッチ基盤画像モデルとしてリリース。美学・スタイル転送・クリエイティブ制御に特化。Turbo版は高速生成（数秒）、スタイル参照対応。Krea2はオープンウェイト版（Raw/Turbo）も提供されており、360ERPなどの特殊機能拡張が議論されている文脈と一致。[[6]](https://www.krea.ai/news/release-notes)[[7]](https://invideo.io/blog/krea-ai-image-generator/)
- **Stability Matrix**: ComfyUIを含むStable Diffusion系パッケージのワンクリックインストール・管理ツール。ComfyUIをパッケージとして扱い、起動引数管理やカスタムノード対応が容易。[[8]](https://docs.lykos.ai/stability-matrix/getting-started/installation)[[9]](https://github.com/LykosAI/StabilityMatrix)
- **LM Studio**: ローカルLLM（GGUF形式、Qwenなど）の発見・ダウンロード・実行ツール。2026年時点でv0.4.x台。Bionicエージェント機能の追加など進化中。ComfyUIとの併用事例と親和性が高い。[[10]](https://www.techspot.com/downloads/7719-lm-studio.html)

これらの情報は2026年8月時点の公開ソースに基づきます。ログ内の具体的な最適化ノード名やPRはコミュニティ有志によるもので、公式ComfyUIコアとの統合が進んでいる点が確認できました。
