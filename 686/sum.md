# 🆕 新規トピック（前回からの差分）
### スレッド概要
- MiniMax H3を中心としたアニメ調・エロ寄り動画生成の技術共有と実験報告が活発
- お盆明け直後からH3公開直後の過渡期に位置する
- 技術的試行錯誤と自虐ネタが混在する典型的ななんJ AIスレで、エロ生成が主流

### MiniMax H3の活用状況
- Context Loopによる長尺動画生成・シーン追加・Approve & Continueが中心
- エディターノードやリファレンス画像サイズ設定のTipsが共有され、Turbo LoRAとの画質比較も実施
- ref2va / fl2vaノードの精度向上やInpaint活用が話題

### ワークフロー・技術的最適化
- ComfyUI + Kitchen Attention + Sol-Attnの組み合わせが最強候補として共有
- Latent Upscale高速化やRAM節約オプションが低スペック環境で好評
- Krea2との併用が進み、公式テンプレートやGGUF化の是非も議論

### ハードウェア事情
- RTX 5090 BTOが即完売し、75万円クラスを中心に争奪戦が発生
- 低スぺ勢のVRAM/RAM節約術が頻出し、4090からの乗り換え評価も見られる
- 価格高騰と転売問題への不満が強い

### LLM活用・その他
- Qwen3.8-27BやGemma4-31Bがプロンプト作成やエロ・ロールプレイで好評
- Geminiはオタク創作でClaude/Qwen/Gemmaに劣るとの評価
- Xノイズ回避やエロ声生成の権利・法律話も散見

### 傾向・特徴
- 5090持ちガチ勢、中間層、ROM/低スぺ羨望層の温度差が顕著
- 「H3祭り」継続中ながら「作りたいものがなくなってきた」声も出始める
- 金銭感覚の麻痺、NSFW特化最適化、自己皮肉がコミュニティの特徴
- H3 + ComfyUI最適解探しと低スぺ追従可能性が主戦場
- Krea3への期待・憶測も見られる

### 総評
- H3登場によりローカル実用動画生成フェーズに入った実感が強い
- 性能向上の速さとハードウェアコスト・ワークフロー複雑さの間で揺れる過渡期

### Web検索による参考情報
- MiniMax H3は2026年7月31日頃公開のオープンウェイト動画生成モデルで、ComfyUI対応が進む
- Krea 2は2026年5月頃の画像基盤モデルで、H3との併用が主流
- RTX 5090は米国MSRP $1,999、日本では70万円台〜で発売直後の争奪戦が話題
- スレッド内容はユーザー投稿に基づくため、実際の動作は自己責任で検証が必要

---
# 元の本文
**なんJ（5ch）AI動画生成スレッド 統合レポート**

### スレッド概要
- **主なテーマ**: MiniMax H3（特にアニメ調・エロ寄り動画生成）を中心としたローカルAI画像・動画生成の技術共有・実験報告。ComfyUIワークフロー最適化、ハードウェア事情、LoRA/モデル活用が活発。
- **時期**: お盆明け直後〜H3公開直後（RTX 5090 BTO出荷・在庫話から推測）。Krea3発表前後の過渡期。
- **全体の雰囲気**: 技術的な試行錯誤と「ワイはもうこれで死ぬわ」系の自虐・ネタ投稿が混在する典型的ななんJ AIスレ。エロ生成話が主流で、ガチ勢・中間層・ROM専/低スぺ勢の温度差が顕著。「このスレはアニメ絵の変態ばっかり」などの自己皮肉も定番。

### 主要トピック

**1. MiniMax H3の活用状況**  
Context Loop（またはContex-Loop）による長尺動画生成・シーン追加・Approve & Continueが中心議論。エディターノードの扱いやリファレンス画像サイズ設定（デフォルト「match」 vs 「max」）のTipsが共有され、「max」設定で原寸読み込み＋リサイズ推奨の声多数。Turbo LoRA（4/8step）と標準20stepの画質・音質比較実験も行われ、音量注意付きで動画投稿あり。ref2va / fl2vaノードの精度向上やInpaint（SAM3.1組み合わせ）も話題。[[1]](https://www.minimax.io/blog/minimax-h3)[[2]](https://github.com/ethanfel/ComfyUI-MiniMaxH3-Contex-Loop)

**2. ワークフロー・技術的最適化**  
ComfyUI + Kitchen Attention + Sol-Attn（Sage Attention）の組み合わせが最強候補。Latent Upscale高速化やRAM節約起動オプション（--fast-diskなど）が共有され、RAM 32GB環境でもContext Loop動作報告あり好評。Krea2との併用が主流で、「Krea2で細部、H3で動き」という使い分けが進んでいる。公式ComfyUIテンプレートの強みやGGUF化の是非も議論。[[3]](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)

**3. ハードウェア事情**  
RTX 5090 BTO（パソコン工房など）が即完売で75万円クラスが特に早く、100万円超えも売れている状況。「駆け込み需要か？」との声も。低スぺ（4060Ti、5070Ti、3080 10GB、RAM 32〜64GB）勢のVRAM/RAM節約術が頻出。4090→5090乗り換えで「余裕・静けさ・透明感」が向上した比較談や、プロ向け中古GPU（Quadro RTX 8000など）検討も。価格高騰・転売問題が強い不満点。[[4]](https://videocardz.com/newz/japanese-system-integrator-pc-kobo-launches-geforce-rtx-5090-founders-edition-pcs)

**4. モデル・LoRA関連**  
Anima、Krea2、MiniMax H3の使い分け。Animaのアップスケール黒つぶれ問題やEpred/Vpred選択、動作系LoRAの干渉（手・顔増加現象）が課題。anal_stomach_bulge系LoRA作成事例もあり。Seedance2.5との比較も散見。

**5. LLM活用・その他**  
プロンプト作成にQwen3.8-27B（thinking lowで爆速、ONで賢く）、Gemma4-31B（エロ・ロールプレイ向き）が好評。Geminiは日常会話は強いがオタク創作ではClaude/Qwen/Gemmaに劣る・ハルシネーション多めとの評価。Xノイズ回避やエロ声生成の権利問題、法律話（二次元合法前提）も。チャッピー（ChatGPT）文化定着。

### 傾向・特徴
- **層の違い**: 5090持ちガチ勢（Context Loop・LoRAガンガン）、中間層（32〜64GBで試行錯誤）、ROM/低スぺ羨望層。「H3祭り」熱量継続中だが「作りたいものがなくなってきた」声も。
- **コミュニティ空気**: 金銭感覚の麻痺（50〜100万円GPUを「一抜き75円」換算）、NSFW特化最適化（解剖学プロンプト・LoRA調整）、自己皮肉（「ゲームエンド」「チンチンが心配」）が特徴。エロ動画投稿活発で品質競争の雰囲気。
- **主戦場**: H3 + ComfyUI最適解探しと、低スぺ追従可能性。Krea3（画像/動画モデル？ Edit特化？）への期待・憶測も。

### 総評
H3登場により「ローカルで実用的な動画生成」フェーズに入った実感が強く、性能向上の速さに驚きつつハードウェアコストとワークフロー複雑さに苦しむ過渡期のスレッド。技術共有と作品晒し（特にエロ）が三位一体となった典型例。

## Web検索による参考情報
- **MiniMax H3**: 2026年7月31日頃公開のMiniMax社製オープンウェイト汎用マルチモーダル動画生成モデル。テキスト・画像・動画・音声を統一コンテキストで理解し、ネイティブステレオ音声付き動画（最大15秒・2K解像度・24fps）を生成。ComfyUIでT2V/I2V/R2VワークフローやContext Loopノードが利用可能で、ローカル実行事例多数。[[1]](https://www.minimax.io/blog/minimax-h3)[[5]](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- **Krea 2**: Krea AIの画像基盤モデル（2026年5月頃）。RAW（微調整向き）とTurbo（高速推論）版があり、LoRA学習・ComfyUI活用に適する。H3との併用がスレッドで言及される。Krea3の公式発表は検索時点で未確認。[[6]](https://www.krea.ai/krea-2)
- **RTX 5090**: NVIDIA GeForce RTX 50シリーズ。米国MSRP $1,999、日本ではBTO/PC工房などで70万円台〜（ Founders Edition搭載PC 72.88万円〜、転売・関税で100万円超も）。発売直後の争奪戦・価格高騰が話題。[[7]](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)[[4]](https://videocardz.com/newz/japanese-system-integrator-pc-kobo-launches-geforce-rtx-5090-founders-edition-pcs)

（上記は公開情報に基づく確認結果。スレッド内容はユーザー投稿に基づく要約のため、実際の動作は自己責任で検証を。）
