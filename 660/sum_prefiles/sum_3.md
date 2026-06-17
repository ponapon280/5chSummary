**なんJNVA部スレッド要約レポート**

このスレッドは、主にStable Diffusion系ローカル画像生成（特にアニメ調・2.5D）を扱う「なんJNVA部」参加者による技術・絵柄議論が中心。Animaモデルを中心としたワークフロー、Regional ControlNetの活用、2.5Dの定義、アップスケール手法、動画生成（Wan系）などが活発に語られた。

### 1. 2.5D絵柄の定義と変遷
スレッド参加者間で「2.5D」の解釈が大きく分かれていることが確認された。
- 旧来（3年前頃）：立体感のある2D寄り（顔がアニメ調で体に厚みがある）
- 現在主流：実写寄り3D（一目でCGとわかるが、リアルに寄せた質感重視）
- 共通の認識として「人中が強調される」「鼻・唇がリアル寄り」「人形感が強い」などが挙げられ、背景のみリアルなものは2.5Dとは呼ばない傾向が強い。

### 2. 主なモデル・ツール議論
- **Anima**（base / preview3）：アニメ調の肌表現・質感で高評価。Regional ControlNet（LLLite版）との相性が良く、領域指定による構図制御で注目を集めている。
- **SCAIL-2**：Berniniとの使い分けが話題に。SAM3によるポーズ検出精度が高く、動きの再現性で優位という声あり。
- **Wan（Wan2.2 / Lightx2v LoRA）**：動画生成で使用。Lightning LoRAの設定やステップ数でピンボケ対策が議論された。
- その他：Realism Engine（Ideogram 4）、WAI Illustriousなども言及。

### 3. 技術的Tips
- アップスケール：潜在拡大 → モデル拡大 → i2i低ノイズの組み合わせが主流。
- Regional ControlNet：マスクによる領域別プロンプト適用で、複雑な構図制御が可能。
- 2dVAE化：効果は限定的（1%程度の変化）という報告多数。

### 4. その他の話題
- Civitai / Civitai REDの使い分け（REDは全年齢モデル検索に制限あり）
- プロンプト圧縮やRegional ControlNet依存の弊害

---

## Web検索による参考情報

- **Anima**：Civitaiで公開されている人気のアニメ特化Stable Diffusionモデル。base版とpreview版が存在し、特に肌の質感やアニメ寄り表現で評価が高い。Regional ControlNetとの組み合わせ事例もコミュニティで増加中。
- **SCAIL**：おそらく「Scail」または「Scale」系動画・アニメーション向けモデルの通称。Berniniは同系統の別系統モデルとされ、ポーズ検出にSAMを活用したバージョンがSCAIL-2として言及されている可能性が高い。
- **Regional ControlNet (LLLite)**：ComfyUI向けのカスタムノード。RGBマスクによる領域別制御が可能で、Animaユーザー間で急速に普及している。
- **Wan / Lightx2v**：動画生成向けLoRA。Lightning LoRA併用時のステップ数調整で画質安定化が図れることが知られている。
- **Civitai RED**：Civitaiの全年齢向けサブセクション。NSFWモデルの閲覧制限や新着順検索の挙動が通常版と異なる。