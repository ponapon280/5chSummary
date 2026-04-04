# 🆕 新規トピック（前回からの差分）
- スレッド全体トーン: 技術共有・称賛中心、NTR論争/Pixiv荒らし/X承認欲求批判
- Anima/Illustrious強み: 低VRAM効率、自然言語プロンプト優位、多人数/群衆、長尺動画一貫性、wai派生
- Anima/Illustrious課題Tips: 髪ジャギー(v0.25改善/LoRA)、挿入描写(`just the tip`/deep/stomach bulge/neg)、多人数構図(girl連打/circle_formation)、手指/視線(Detailer/bad hands neg)、アップスケ/動画(SEGS/Wan2.2/FLF)
- Anima/Illustriousマージ/共有: SuperSanicAnima+dmd2+i2i、Texture Enhancer+Raejin、Wai-Illustrious初心者推奨
- ComfyUI推奨版/バグ: v0.17.x安定、v0.18.xノード消失/OOM対処(git pull/0c63b4f6)、Manager避け
- ComfyUI高速化: SageAttention/TorchCompile(7→9it/s)、Spectrum/Wavespeed(10秒生成)、Dynamic VRAM/TurboQuant(1/6圧縮)
- ComfyUI新機能: Live2Dパーツ分け(SDXL+SAM2)、See-through軽減、Irodori-TTS-v2、PixAI Tagger安定
- ComfyUI WF例: Hires/FaceDetailer移植、Anima下絵+i2i、公式WF初心者
- LLMローカルNSFW推奨: Qwen3.5 9B/35B(Q4/Q5_K_M)、NovelAI GLM4.6(355B MoE API)、Gemma4 26B(A4B/Heretic)
- LLM Tips: LM Studio/Ollama、Grok/Claude jailbreak、プロンプト矛盾指摘
- LoRA学習パラメータ: キャラ(4-64/1)、画風(16-64/8-64)
- LoRA生成: CG集(>>61級)、NTR(夫眼鏡/間男チャラ)、漫画(1枚絵>多コマ、視線/コマ割り弱)
- LoRA投稿戦略: Pixiv(オリジナル/DLsite/背景タグ)、X(相互/リポスト/シャドバン/微エロ版権)
- ハードウェア足切り/注目: NVIDIA 12GB+(3060OK/Laptop6GB NG)、RAM32GB+、Intel Arc B-series(B70/B580 32GB/15万)
- ハードTips: RAMディスク/ZRAM、電源/3090焼損、クラウド(Runpod/Colab)
- 注目共有リソース生成例: >>61(CG集)、>>102(多人数制服)、>>183(古多人数手破綻)
- 注目共有リソースモデル/WF: Animaマージ(326)、dasiwa v10(320)、easywan22代替、GitHub Live2D/See-through
- 注目共有リソースツール: NegPip、PNG D&D→Catbox、SD Prompt Saver
- トレンドシフト: Anima/Illustrious > SDXL/リアス、Wan2.7微妙→LTX/Seedance、ComfyUI安定待ち
- トレンド進化: エロLoRAマージ/NSFW LLM脱獄でプロ級CG/小説、Live2D/TTSエロゲ実用
- トレンド課題: VRAM壁、Comfy互換性、手/挿入ガチャ、SNS営業、アップ画像責任
- トレンド未来: Anima正式版、Gemma4後Embedding統合、Arc実機/Wan OSS、初心者Wai-Illustrious+v0.17.x

---
# 元の本文
# なんJ AI生成スレッド 総合ログレポート (レス4〜1000)

## スレッド概要
- **対象ログ**: なんJ板AI生成スレッド（主にAnima/Illustrious/Wan/LTXモデル中心の画像/動画生成議論）。総レス約1000。時期は2024年4月頃推定。
- **主なテーマ**: AnimaYume（v0.3/v0.25/preview2）のNSFW性能（多人数/一貫性/挿入描写）、ComfyUIワークフロー/バグ修正、LLM（Qwen3.5/NovelAI/Gemma4）併用、Pixiv/X投稿戦略、LoRA学習、ハードウェア最適化、動画生成（Wan2.2/2.7/LTX2.3）。Live2D自動化やTTSも後半活発。
- **参加者傾向**: ローカル環境ユーザー（RTX 30/40/50xx系、VRAM12-40GB+）中心。エロNSFW特化でTips共有活発。初心者相談多め、上級者はトラブルシュート/新モデル共有。
- **全体トーン**: 技術共有・称賛中心（「ゲームエンド級」「おめ！」）。NTR論争/Pixiv荒らし疑惑/X承認欲求批判あり。生成例絶賛多し。

## 主要トピック別まとめ

### 1. Anima/Illustriousモデル性能・生成Tips
- **強み**: 低VRAM効率（Detailer/CN不要）、自然言語プロンプト優位（冠詞で重複減、多人数/群衆優秀。「後列20人立たせ、前列10人座らせる」で高多様性）。長尺動画一貫性高。waiはIllustrious派生（wanvideo無関係）。
- **課題/Tips**:


  | 問題 | 解決策 |
  |------|--------|
  | 髪ジャギー | v0.25/preview2で改善。LoRA併用。 |
  | 挿入描写 | `just the tip`（浅）、`deep penetration`/`stomach bulge`（深）。根元難→`penis:-1.5` neg。バック時玉/竿強制。 |
  | 多人数/構図 | girlタグ連打/`circle_formation from_below`。glass table wariza例。 |
  | 手指/視線 | LoRAなし+Detailer。bad hands neg。 |


- **アップスケ/動画**: SEGSタイル版（VRAM11.5GB）。Wan2.2推奨（LTX2.3速いが動作/手破綻多め）。FLF=First-Last Frame（FLUX無関係）。
- **マージ/共有**: SuperSanicAnima + dmd2 + Illustrious i2i。Texture Enhancer+Raejin Anima（低スペOK）。Wai-Illustrious初心者推奨。

### 2. ComfyUIツール/ワークフロー・バグ
- **推奨版**: v0.17.x（0.17.0/0.17.2安定）。v0.18.xでノード消失/OOM/点滅多発→git pull/タグcheckout（master 0c63b4f6推奨）。Manager凶悪ノード避け。
- **高速化**:


  | ツール | 効果 | 注意 |
  |--------|------|------|
  | SageAttention/TorchCompile | 7→9it/s | 初回遅延（3-5分仕様）。 |
  | Spectrum/Wavespeed | 10秒生成/Anima優位 | 色褪せ抑制。 |
  | Dynamic VRAM/TurboQuant | モデル1/6圧縮 | Wanアンロード要。 |


- **新機能**: Live2Dパーツ分け（SDXL+SAM2、VRAM16GB+）。See-through（軽減更新）。Irodori-TTS-v2（VoiceDesign）。PixAI Tagger安定。
- **WF例**: Hires/FaceDetailer移植。Anima下絵+i2i。公式WFから初心者スタート。

### 3. LLMローカル実行・NSFW活用
- **推奨**:


  | モデル | 量子化 | VRAM/速度 | 特徴 |
  |--------|--------|-----------|------|
  | Qwen3.5 9B/35B | Q4/Q5_K_M | 低/62tok/s | Anima併用、自然言語作成。 |
  | NovelAI GLM4.6 (355B MoE) | API | - | エロ小説/口調保持↑。 |
  | Gemma4 26B | A4B/Heretic | RAM乗せ | NSFW脱獄（催眠/洗脳OK、ロリNG）。 |


- **Tips**: LM Studio/Ollama。Grok/Claude jailbreak（Fastモード）。プロンプト矛盾指摘で精度↑。

### 4. LoRA学習・CG集/漫画/NTR生成
- **パラメータ**:


  | タイプ | Dim/Alpha | ステップ | Tips |
  |--------|-----------|----------|------|
  | キャラ | 4-64/1 | 1500 | 低Dim精密。タグ無編集最強。 |
  | 画風 | 16-64/8-64 | - | U-net半LR。背景多→低Dim。 |


- **生成**: CG集（>>61動画級）。NTR（夫:眼鏡真面目/間男:チャラ）。1枚絵>多コマ。Markdown無効→自然文。視線/コマ割り下手→プロ練り。
- **投稿戦略**:
  - **Pixiv**: オリジナルじわじわ伸び（DLsite強い）。背景/設定こだわり。タグ検索優位。
  - **X(Twitter)**: 相互/リポスト必須。新規シャドバン1ヶ月。微エロ/版権/営業力重視。

### 5. ハードウェア・最適化
- **足切り**: NVIDIA 12GB+（3060 OK、Laptop6GBアウト）。RAM32GB+。
- **注目**:


  | GPU | VRAM/価格 | 注意 |
  |-----|-----------|------|
  | Intel Arc B-series (B70/B580) | 32GB/15万 | PyTorch可、動画NG版注意。 |
  | RTX 50xx/AMD RX90xx | 16GB+ | AMD静画遅め。 |


- **Tips**: RAMディスク/ZRAM。電源/3090焼損注意。クラウド（Runpod/Colab）低スペ救済。

## 注目共有リソース
- **生成例**: >>61（CG集世界級）、>>102（多人数制服）、>>183（古多人数手破綻）。
- **モデル/WF**: Animaマージ（326）、dasiwa v10（320）、easywan22代替（公式WF）。GitHub: Live2DパーツAI、See-through。
- **ツール**: NegPip、PNG D&D→Catbox、SD Prompt Saver。

## トレンド・示唆・課題
- **シフト**: Anima/Illustrious > SDXL/リアス（自然言語/多人数で超え）。Wan2.7微妙→LTX/Seedance。ComfyUI安定待ち。
- **進化**: エロLoRAマージ/NSFW LLM脱獄でプロ級CG/小説量産。Live2D/TTSでエロゲ実用化。
- **課題**: VRAM壁、Comfy互換性、手/挿入ガチャ、SNS営業負担。アップ画像自己責任。
- **未来**: Anima正式版、Gemma4陳腐化後Embedding統合、Arc実機報告/Wan OSS期待。初心者: Wai-Illustrious + v0.17.xから。

このレポートは全ログの重複除去・統合版。詳細/元ログ参照。追加質問歓迎。
