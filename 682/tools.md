# 🆕 新規トピック（前回からの差分）
### ComfyUI（comfy）本体・エコシステム
- 主な運用・拡張機能
- 選ばれている主な理由
- 初心者でもClaude/CodeX/GrokなどのAIアシスタントに環境構築を丸投げしやすい
- Easy-Install系やManager経由で導入ハードルが下がっている

### 関連サブツール
- Comfy-Kitchen: Sage Attentionの代替として導入の手間が少なく低スペック環境でも安定しやすい
- Context Loop: 長尺動画生成で自然な繋ぎやLLM大量生成＋放置運用に強い

### Stable Diffusion WebUI系（A1111 / Forge / Forge Neo）
- Forge Neo: Hires fix時の不具合報告あり。Krea2対応が言及

### その他のツール・運用Tips
- Irodori-TTS: Smallのv4.1リリース情報あり
- docker + samba + WSL2: NASモデル共有構成例

### 全体の傾向と選定理由のまとめ
- 手軽さ・導入容易さ → SwarmUI、Forge Neo、Comfy-Kitchen（Sage Attentionの壁回避）、Easy-Install/Manager

### Web検索による参考情報
- ComfyUI: 2026年8月時点でv0.31.0が最新リリース
- Comfy-Kitchen: Comfy-Org公式の高速カーネルライブラリで2026年8月もコミット活発
- Irodori-TTS: v4.1-Smallが2026年8月10日頃にデフォルトモデル更新
- 検索は2026年8月12日時点の情報に基づく

---
# 元の本文
**生成AI関連ツールのレポート（テキスト抽出に基づく）**

テキストから抽出された主な生成AI関連ツールは、**ComfyUI**（およびそのエコシステム）と**Stable Diffusion WebUI系（Forge/Forge Neo）** が中心です。これらに加え、**Wan2GP**、**SwarmUI**、**Comfy-Kitchen** などの補助ツール・拡張が複数言及されています。モデル名・性能比較は除外し、ツールの運用・選択理由・カスタム機能に焦点を当ててまとめます。選ばれている理由が明記されている点は優先的に記載しています。

### 1. ComfyUI（comfy）本体・エコシステム
ComfyUIはテキスト全体で最も言及が多いツールです。ノードベースのUI/バックエンドとして位置づけられ、動画生成（特に長尺・ref2v/fl2v系）でのワークフロー構築に強く使われています。「スパゲティ配線」と表現されるほど複雑なワークフローを組むユーザーが多く、柔軟性が最大の特徴です。

- **主な運用・拡張機能**
  - カスタムノードの活用（音声除去、続き生成、軽量化など特定課題解決）。
  - 高速化系ノードの接続順序最適化。
  - 保存ノード（save video）やVAE Decode関連の工夫。
  - `--fast-disk`オプションやRAMディスクの活用（RAM使用量削減目的）。
  - 更新方法：stability matrix経由、masterブランチ指定、Manager経由、cmd直接更新など多岐にわたる。バージョン不一致（例: v0.31.1でのノード互換性問題）への対応が話題。

- **選ばれている主な理由**
  - ワークフローの柔軟性が高く、動画生成やカスタムノードの組み合わせに適する。
  - 初心者でもClaude/CodeX/GrokなどのAIアシスタントに環境構築を丸投げしやすい。
  - Easy-Install系やManager経由で導入ハードルが下がっている。
  - 低スペック環境（例: 3060 12GB + 32GB RAM）でも軽量化ノードで対応可能という声あり。

**関連サブツール**
- **ComfyUI Manager / ComfyUI-Easy-Install**: 更新・ノード管理ツールとして頻出。Manager単体ではUpdateボタンが出ない場合があり、起動ファイル記述や手動`pip install -r requirements.txt`が必要になるケースが指摘されています。
- **Comfy-Kitchen（Kitchen Attention / CK Attn / ModelAttentionBackend）**: Sage Attentionの代替として複数回登場。導入の手間が少なく、Sage/tritonインストール不要で低スペック環境でも安定しやすい点が評価されています。速度はSageとほぼ互角〜やや遅めの場合もあるが、精度向上（細部崩れが少ない）や公式ComfyUI + テンプレだけで完結する可能性が理由として挙げられています。
- **Context Loop（Contex Loop）**: 長尺動画生成でmotion contextより自然な繋ぎや、LLM大量生成＋放置運用に強い点が採用理由。
- その他ノード: video combine + prune outputs（中間ファイル削除）、kijaiのvideo vae int8 conv（VRAM節約・高速化）、Hybrid Loader、LoRAローダー（kj4step）など。

### 2. Stable Diffusion WebUI系（A1111 / Forge / Forge Neo）
ComfyUIと明確に区別され、「手軽にきれいな画像が出る」「簡単で速い」と評価される一方、ComfyUIは低スペック有利だがUIが分かりにくいという指摘があります。最近は「WebUI」ではなくForgeかForge Neoの二択で語られることが多いです。

- **Forge Neo**: Hires fix時の不具合報告あり（anima組み合わせ時など）。Krea2対応などの点が言及。
- **選ばれている主な理由**: 手軽さ・シンプルなGUI。ComfyUIを敬遠する層の入門ツールとして機能。

### 3. Wan2GP（deepbeepmeep/Wan2GP）
RTX 5070 Ti（16GB）環境などでMiniMax H3などを動作させるためのツールとして使用例あり。SwarmUIでモデル認識できない場合やVRAMオーバー時の代替として選択されています。480p短尺生成の実用例や、メモリ64GB推奨という運用Tipsも見られます。

- **選ばれている主な理由**: SwarmUI非対応モデルへの対応やVRAM制約時の代替。

### 4. SwarmUI
Wan2GPと比較され、「ノードがいらないので楽」との評価。一方でモデル認識の問題が発生した事例あり。

- **選ばれている主な理由**: ノード不要の手軽さ。

### 5. その他のツール・運用Tips
- **Irodori-TTS**: Smallのv4.1リリース情報あり。
- **RAM関連**: 32GB→64GB→96GB増設議論、RAMディスク活用、pip/uv cache削除（30GB程度空くTips）。
- **docker + samba + WSL2**: NASモデル共有構成例。
- **AIアシスタント活用**: codeX/Claude/Grokを環境構築・カスタムノード作成・ワークフロー相談に多用（特にCodex推奨の声）。

**全体の傾向と選定理由のまとめ**  
- **柔軟性・カスタマイズ性** → ComfyUI + カスタムノード各種。
- **手軽さ・導入容易さ** → SwarmUI、Forge Neo、Comfy-Kitchen（Sage Attentionの壁回避）、Easy-Install/Manager。
- **低スペック耐性・代替性** → Wan2GP、Comfy-Kitchen、軽量化ノード。
- **運用効率** → RAMディスク、cache削除、AIアシスタントとの組み合わせ。
多くの場合、「特定の課題解決（音声除去、速度向上、モデル認識、RAM節約）」や「Sage Attentionなどのインストールハードル回避」が明確な選定理由として記載されています。

## Web検索による参考情報
- **ComfyUI**: 2026年8月時点でv0.31.0が最新リリース（8月7-8日頃）。Frontendパッケージ更新や新モデルサポートが継続中。Python 3.13推奨の記述も見られる。[[1]](https://github.com/comfy-org/comfyui)[[2]](https://docs.comfy.org/changelog)
- **Comfy-Kitchen**: Comfy-Org公式の高速カーネルライブラリ（Diffusion推論向け複数バックエンド対応）。2026年8月にもコミットが活発。[[3]](https://github.com/Comfy-Org/comfy-kitchen)
- **Wan2GP**: deepbeepmeep氏による「GPU Poor」向け高速動画生成ツール。Wan 2.1/2.2、LTX、Qwen Image、Hunyuan Video、Fluxなどをサポート。低VRAM環境向けに設計。[[4]](https://github.com/deepbeepmeep/Wan2GP)
- **Forge Neo**: Stable Diffusion WebUI ForgeのNeoブランチ（Haoming02氏）。最適化・使いやすさ向上版で、最新モデル対応を重視。Gradioベース。[[5]](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo)[[6]](https://www.thundercompute.com/blog/forge-ui-ai-image-generation)
- **SwarmUI**: mcmonkeyprojects氏によるモジュラーWebUI（旧StableSwarmUI）。ComfyUIバックエンド活用し、多数の画像/動画/音声モデルをサポート。v0.9.8 Betaなど。[[7]](https://github.com/mcmonkeyprojects/SwarmUI)
- **Irodori-TTS**: Aratako氏のFlow MatchingベースTTS。v4.1-Smallが2026年8月10日頃にデフォルトモデル更新されており、Voice Cloningやスタイル制御対応。[[8]](https://github.com/Aratako/Irodori-TTS)

（検索は2026年8月12日時点の情報に基づく。モデル性能や具体的なベンチマークは除外。）
