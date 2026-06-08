**なんJ AI生成スレッド要約レポート（Anima/Ideogram中心）**

### スレッドの主な内容
- **WAI-ANIMA / Anima base 1.0** の評価が中心。Turbo LoRA併用時の絵柄変化、looking at viewerなどのプロンプト効き、指崩れの少なさ、LoRA学習解像度（512 vs 1024）の差などが話題。
- **Ideogram 4.0** のローカル版が急浮上。JSONプロンプト（bounding box）による配置精度、検閲の緩さ・厳しさ、API版との画質差が議論された。手書きラフからの生成や、Civitai系ワークフローとの比較も。
- ComfyUIの更新影響（dynamic VRAMによる動画生成遅延）、AnyTest ControlNetの相性、背景パース崩れ対策などが技術トピック。
- その他：Gemma 4 12Bのローカルエロチャット性能、LTX系動画生成、旧モデル（Rias、シルバニアニキ系）からの移行話。

全体として「Anima系でどこまで自然言語・構図制御できるか」「Ideogram 4.0のローカル実用性」がメインの盛り上がりポイントだった。

### 注目モデル・機能の傾向
- Animaは「自然言語がそこそこ通る」「Turbo LoRAで低ステップ安定」という評価が定着しつつ、背景整合性や特定ポーズの弱さを指摘する声も。
- Ideogram 4.0は「JSONで配置指定できるのが革命的」と好評だが、エロ表現の学習不足やAPI版との差が課題視された。

## Web検索による参考情報
- **WAI-ANIMA**: Civitaiで公開されているAnima系ファインチューニングの人気モデル群。base 1.0に加え、WAI、Hakushi、Cottonなどの派生が同時に話題になることが多い。
- **Ideogram 4.0**: Ideogram.aiが提供する最新モデル。特徴的なJSON/bounding box形式のプロンプト対応とテキスト生成精度が強み。ローカル版は有志による実装が進んでおり、API版（Turbo/Qualityモード）と画質・検閲挙動が異なる点が指摘されている。
- **Google Gemma**: ログ内の「Gemma 4 12B」はGemma 3 12B（またはGemma-3-12B-IT）の誤記・先読みと思われる。Googleは端末側推論を強く意識した軽量モデルを推進しており、12Bクラスでもローカルエロチャット用途で実用的な速度が出る。
- **NVIDIA Cosmos**: 2025年時点でCosmos-1が公開されており、ログで言及された「Cosmos 3」は将来の大型アップデートを指している可能性が高い。物理世界シミュレーション向けのmixture-of-transformersアーキテクチャを採用。
- **LTX / Qwen-Image**: LTX Video系はControlNet（Depth）との組み合わせが主流。Qwen-Imageは高解像度静止画生成でControlNetのベースとして使われるケースが増えている。

（情報は2025年時点の公開情報に基づく。モデルはCivitai・公式サイト・NVIDIA発表資料で確認）