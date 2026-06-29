**なんJスレッド要約レポート（AI画像生成モデル関連）**
このスレッドは、主にローカル環境向けアニメ/NSFW画像生成モデル「Anima」と新モデル「Krea2」の比較・移行議論が中心。ComfyUIワークフロー、LoRA学習、VRAM最適化、検閲回避などの技術的話題が活発に交わされている。
### 主要な議論ポイント
- **AnimaからKrea2への移行動向**  
  Krea2の登場により「Animaはもう古い？」という声が出る一方、Animaの安定性・柔軟性・エロ耐性を評価する意見も根強い。Krea2は画風LoRAの相性が良く、背景描写やプロンプト追従性で優位だが、検閲が強くエロ表現で苦戦するケースが多い。
- **Krea2の技術的特徴と運用**  
  - RAW版とTurbo版が存在し、LoRA作成はRAW、通常生成はTurboが推奨されている。
  - ComfyUIノード（ConditioningKrea2Rebalance、Krea2 Image Edit Rebalanceなど）のアップデートが活発。
  - Musubi TunerでのLoRA学習が主流。blocks_to_swap（最大26）＋H2D onlyオプションでVRAM16GB環境でも動作可能。
- **LoRA・ControlNet関連**  
  Anima版LoRAのリリースが相次ぐ中、Krea2向けの画風LoRAやNSFW LoRAの報告も増加。2キャラ同時生成やマージ手法の検証も行われている。
- **VRAM・環境問題**  
  LoRA適用時のOOM対策として`--novram`やblock swapの活用が共有され、16GB勢でも実用可能になったという報告多数。
- **検閲・NSFW性能**  
  Krea2はエロLoRA併用で暴力表現なども通りやすくなる傾向が指摘される一方、Animaほど「極端なエロ」が出しにくいという声が目立つ。
- **その他**  
  CivitaiでのLoRAアップロード、動画生成、プロンプト共有 vs LoRA文化の違いなどが話題に。
全体として「Krea2は進化が速く将来性があるが、Animaの完成度・エロ耐性はまだ健在」というバランスの取れた評価が主流。
## Web検索による参考情報
- **Anima**：Civitaiなどで公開されているアニメ特化型Stable Diffusionモデル（AnimaBaseなど）。特にNSFW耐性と小物・ポーズの学習精度で人気。ControlNetやLoRAとの親和性が高い。
- **Krea2**：スレッド内で言及されている新型モデル。公式情報ではRAW/Turboの2種展開があり、Musubi Tunerでの学習が推奨されている。ComfyUIとの連携が進んでおり、Krea.ai関連の新機能（Image Edit系ノード）も確認できる。
- **Musubi Tuner**：Krea2などの新型モデル向けLoRA学習ツール。block swap機能により低VRAM環境での学習を可能にしている。
- **ComfyUI関連ノード**：ConditioningKrea2RebalanceなどのKrea2専用ノードがアップデートされており、ワークフローの進化が続いている。
（情報はスレッド内容とCivitai・GitHub上の公開情報に基づく）