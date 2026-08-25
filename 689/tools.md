# 🆕 新規トピック（前回からの差分）
### ComfyUI（comfy）および関連カスタムノード・ワークフロー
- comfy-kitchen PR#117でint8 Sol-Attention追加により生成速度が大幅向上
- Deno Local LLM LoaderやQwenプロンプターノード、NAI APIによるダイナミックプロンプト実装

### MiniMax H3（H3 / minimax）
- テキストto動画・ref2v・カメラ制御・BGM生成対応の動画生成ツール

### Forge Neo / forge-anima系
- Anima 3.8B対応のForge Neo専用拡張で自動認識機能を提供
- 大規模モデル対応の柔軟性と自動認識機能による採用

### FreeToken / llama.cpp
- 大規模MoEモデルのローカル推論エンジン

### その他のツール
- Anima系LoRA学習向けsd-scripts/kohyaの3.8B対応設定
- モザイク処理後のmp4出力にAviutl + x264guiExを使用
- 画像読取対応のdeepseek apiによるプロンプト作成効率化
- IrodoriTTS v4をGradio UIでテスト、ComfyUI非対応
- ComfyUI内プロンプト生成向けollama
- トラブルシューティング・プロンプト作成向け各種LLM（Copilotは企業利用可）
- 実写・先進スタイル生成向けKrea2
- 映像・CGアップスケーラーとしてのTopaz
- マクロによる定型編集自動化向けAffinity

### ## Web検索による参考情報
- comfy-kitchen PR#117のint8 Sol-Attention追加と量子化高速化機能
- MiniMax H3の33B規模多モーダル動画生成とref2v対応
- forge-anima-3.8BのAnima 3.8B自動認識機能
- IrodoriTTS v4.1-SmallのGradio UI推奨とComfyUI互換性課題
- Krea2のスタイル転送・クリエイティビティ制御機能

---
# 元の本文
**生成AI関連ツールのレポート（抽出テキストに基づく）**

抽出された議論は、主に**ComfyUI**を中心としたローカル/カスタムワークフロー構築、**MiniMax H3**などの動画生成ツール、**FreeToken**や**llama.cpp**などのLLM推論エンジン、**Forge Neo**系のカスタム拡張、**IrodoriTTS**などの音声ツールに集中しています。モデル本体（Anima、Qwenなど）の言及は除外し、ツール・ワークフロー・周辺機能に焦点を当てています。選定理由として、**速度向上**、**VRAM管理**、**柔軟な制御性**、**実用的な出力品質**が繰り返し挙げられています。

### 1. ComfyUI（comfy）および関連カスタムノード・ワークフロー
ComfyUIは最も頻出のツールで、画像生成・動画ワークフロー・LLM連携・アップスケールなどに活用されています。
- **comfy-kitchen（pr117更新含む）**: 高速化のためのカーネルライブラリ。PR #117（kijai氏貢献）によりint8 Sol-Attentionが追加され、生成速度が大幅向上（例: 43分→13分）。`sol_attn_minimax_v3.py`ノードなどの追加が推奨。
- **Ollama連携**: 自然文→プロンプト生成ワークフローで使用。`keep_alive="0s"`指定によりVRAM即時解放が可能で、低VRAM環境向け。
- **その他カスタムノード**: Deno Local LLM Loader（日本語→英語プロンプト変換）、Qwenベースのプロンプターノード（MiniMax H3用）、Dasiwa配布ワークフローより公式テンプレートで十分という意見多数。NAI APIノードによるダイナミックプロンプト（ワイルドカード）実装例も。
- **選ばれている理由**: 高速化ノードによる速度向上、カスタムノードの柔軟性（公式テンプレで十分）、他ツール（Ollama、MiniMax H3）との連携容易さ。VRAM管理ノード探索も活発。

### 2. MiniMax H3（H3 / minimax）
動画生成ツールとして強く推奨。テキスト-to-動画、参照画像（ref2v/r2v）使用、カメラ移動・人物動作制御、開始/終了画像指定、BGM生成（non-diegetic_music指定で歌声抑制）に対応。510秒動画化や性器表現のプロンプト工夫（「股の間」など言い換え）も言及。
- **選ばれている理由**: プロンプトによる高制御性（動作指定・参照画像活用）、現代〜先端水準のワークフロー構築容易さ、版権物再現性（原神強い）、長尺BGMやキャラ調整の独自強み。専用ワークフロー（Remix含む）での価値議論あり。

### 3. Forge Neo / forge-anima系
Anima 3.8B/2.9Bを動かすための専用拡張（https://github.com/GumGum10/forge-anima-3.8B）。TE（Text Encoder）とアダプターの自動認識が可能。3.8Bは通常Forgeでは動作せず、この拡張が必要。
- **選ばれている理由**: 大規模実験モデル（3.8Bなど）の柔軟な対応と自動認識機能。

### 4. FreeToken / llama.cpp
大規模MoEモデルのローカル推論エンジン。
- **FreeToken**: expertを動的にVRAM/DRAMへオフロード。VRAM不足環境でも実用速度（例: 25 tok/s）が出せ、120B級モデル対応。
- **llama.cpp**: 静的オフロードで安定・高速。FreeTokenとの比較で「VRAM収まるモデルならllama.cppが速い」との評価。
- **選ばれている理由**: VRAM容量が限られる環境での大規模モデル実用性（FreeTokenの動的オフロード強み）、安定性・速度重視。

### 5. その他のツール
- **sd-scripts / kohya**: LoRA学習（Anima系）で使用。層数自動検出やnum_blocks=52（3.8B対応）で柔軟。
- **Aviutl + x264guiEx**: モザイク処理後の実用的なmp4出力（ニコ動設定）。アップロード実績あり。
- **deepseek api**: 画像読取対応でプロンプト作成効率化。
- **IrodoriTTS (v3→v4)**: ComfyUIカスタムノード非対応のためGradio UIでテスト。絵文字効きが悪いとの声。
- **webUI (A1111) / SD webUI**: ダイナミックプロンプト拡張でランダム生成。「脱却できない」という言及あり。
- **ollama**: ComfyUI内プロンプト生成用（ハングアップ事例あり）。
- **LLM系（ChatGPT/Copilot/Gemini/Claude/Grok）**: トラブルシューティング、プロンプト作成、ミーム説明などに用途別使用。Copilotは企業セキュリティで許可。
- **Krea2**: 実写/先進スタイル生成試行で言及。
- **Topaz**: 映像・CG系アップスケーラーとして認知度高。
- **Affinity**: マクロによる定型編集自動化。

**選ばれている主な理由（共通）**: 速度向上（高速化ノード）、VRAM効率（動的オフロード・即時解放）、制御性・柔軟性（参照画像・プロンプト工夫）、実用出力（モザイク後mp4など）。

### ## Web検索による参考情報
- **comfy-kitchen**: ComfyUI向け高速カーネルライブラリ（PyPI v0.2.31、GitHub Comfy-Org/comfy-kitchen）。PR #117（kijai氏）でint8 Sol-Attention追加。CUDA/Triton/HIPバックエンド対応、FP8/NVFP4など量子化高速化機能を提供。[[1]](https://github.com/Comfy-Org/comfy-kitchen/blob/main/pyproject.toml)[[2]](https://github.com/Comfy-Org/comfy-kitchen/pull/117/files)
- **MiniMax H3**: 2026年7月31日リリースのオープン多モーダル動画生成モデル（33B規模）。テキスト/画像/動画/音声入力対応、最大15秒・2K解像度・ネイティブステレオ音声出力。API/オープンウェイト提供（地域制限あり）。ref2vなどの参照機能が強み。[[3]](https://www.minimax.io/blog/minimax-h3)[[4]](https://www.renderforest.com/minimax-h3)
- **forge-anima-3.8B**: GitHub (GumGum10/forge-anima-3.8B) のForge Neo専用拡張。Anima 3.8B + Qwen3.5 4Bアダプター対応、自動認識機能を提供。[[5]](https://github.com/GumGum10/forge-anima-3.8B/blob/main/README.md)
- **FreeToken**: 2026年公開のエッジネイティブMoE推論エンジン（PyPI freetoken v0.1.2）。動的expertオフロードで大規模モデル（120B+）を低VRAM環境で高速実行。llama.cpp比較で大規模MoEに強い。[[6]](https://pypi.org/project/freetoken/)
- **IrodoriTTS**: 日本語特化TTSモデル（Aratako開発、v4.1-Smallなど）。ComfyUIラッパー存在するがv4互換性に課題あり。Gradio UI推奨事例多数。[[7]](https://note.com/comfyui_lab/n/n15fd0a190c6e)
- **Krea2**: 2026年リリースの画像生成モデル（Medium/Large/Turbo/Raw）。スタイル転送・ムードボード・クリエイティビティ制御が特徴。オープンウェイト提供。[[8]](https://www.krea.ai/blog/krea-2-image-model)

以上が抽出テキストと検証情報に基づくまとめです。ComfyUIエコシステムの拡張性と、MiniMax H3/FreeTokenなどの新興ツールの制御・効率性が特に評価されています。
