# なんJ AI生成スレッド レポート (抜粋: 634-837)

## スレッド概要
- **期間/範囲**: 634レス以降のログ（主にAI画像/動画生成ツールのTips共有、ハードウェア議論、生成マンネリ解消）。
- **主なテーマ**: Stable Diffusion/ComfyUI中心のNSFW画像・動画生成。マンネリ打破、LoRA/モデル活用、ワークフロー最適化、ハードウェア投資（RTX50xx、メモリ/SSD値上がり）。動画生成（Wan2.2、PainterLongVideo）が活発。AGI/規制の未来論も散見。
- **ユーザー傾向**: 実践派が多く、具体的なWF共有・トラブルシュート。初心者質問から上級者Tipsまで。画像/動画貼り（エロ系多め）がモチベ源。

## 主要トピック別まとめ

### 1. 生成マンネリ解消（構図/行為/物語性）
- **悩み**: 構図・行為単調、物語性不足（>>642）。想像力枯渇。
- **Tips**:
  - Danbooru Wiki漁り（構図/体位アイデア宝庫 >>637,650,660）。
  - MultipleView/Comic追加でエロ詰め合わせ出力（>>635）。
  - TIPOで画風/シチュ刺激（>>635,639）。
  - LLM（Grok/zuntan EasyReforge）でエロノベル生成→膨らませ（>>649）。
  - Temperature上げ+ワイルドカードでバリエーション（>>662）。
- **成果共有**: Danbooruで新構図発見、TIPO説明画像参考（Zuntan）。

### 2. モデル/ツール活用
| モデル/ツール | 推奨/Tips | 関連レス |
|---------------|-----------|----------|
| **TIPO (KBlueLeaf/TIPO-200M)** | GPU推奨、NoobAI V-predでプロンプト追従↑。ratingタグ重要。Temperatureで多様化。 | >>634,637,646,662 |
| **Qwen系 (NSFW LoRA, SNOFS v1.3)** | 微妙報告多（表情崩れ、アヘ顔）。PornMaster-Pro待望。 | >>640,675,688 |
| **nunchaku (SVDQuant)** | FP4/Int4低VRAM高速。外れ値LoRA分離で品質維持（FP16の95%）。50x0恩恵大だが、seed固定で揺らぎ。 | >>643,656,687,706,711-714,723 |
| **z-image-turbo** | ブレザー女子高生でリボン多発→"vertical tie"指定/CFG1ネガ無効（DeTurbo版推奨）。 | >>751,759,776,800 |
| **LoRA管理** | ReforgeでサブフォルダTree View選択（非表示可）。JS書き換えで階層制御（>>709,768）。 | >>641,651,709 |
| **メタデータ検索** | Infinite Image Browser (pyinstaller版推奨)、illustra併用。SaveImageWithMetaDataUniversal必須。 | >>653,655,664,666,758 |

- **キャラLoRA作成**: 複数衣装→タグ一致キャプション（chara_swim等）。フォルダ分けで繰り返し調整（>>807-810）。目つき特化→瞳切り抜き回転画像（>>750,756）。
- **プロンプト**: LLM（lmstudio）でエロ小説（>>685）。

### 3. 動画生成進捗
- **Wan2.2/PainterLongVideo**: 長辺1280妥協、33(32)+17frame、FaceDetailer範囲拡大。ループ→PainterI2V 6(3+3)steps+Color Match（>>658,796-797）。
- **Stable Video Infinity**: LoRAでWan2.2ベース3-6連（19-28秒）。背景安定（>>720,803）。
- **トラブル**: 中止時VRAM解放→掃除機ボタン（>>654,667,702）。モザイクプレビュー→Draw Mask On Image代替（>>718）。
- **LoRA例**: miaomiaoRealskin+copycatPVC（質感エロ、顔補正必要 >>742）。DaSiWaで潮吹きオナニー（webp延長 >>823）。
- **進展**: 1ヶ月でTensorCore/Nunchaku影響中（低VRAM動画↑）。SmoothMix/MMAudio nsfw版以降（>>754）。

### 4. ハードウェア/投資議論
- **RTX50xx (5070Ti等)**: デカさ/SATA干渉注意（3ファン推奨、ATX3.1電源）。8pin x2-3必要（>>674-678,680,686）。5090動画妥協多。
- **メモリ/SSD値上り**: DDR4/32G x2→96G移行（>>661）。128-256GB検討（>>683,715）。HDD8TB 4万→6-7万予想（>>695）。銀高騰影響（>>708）。
- **忠告**: 「シコるだけ？」熟慮せよ（電気代/必要性 >>644）。BTO抑え目推奨（>>726）。
- **購入例**: ガラクロ5070Ti+1000W電源（>>730）。

### 5. 未来/規制論
- **AGI/クラウド**: OpenAI儲け怪しい、Google/Amazon黒字派生存（>>770-775,784-785）。ローカルNSFW優位（規制回避 >>746,753,836）。
- **脳チップ/ディストピア**: 友好的AI希望もターミネーター懸念（>>732,789-792,804,811-814）。
- **待望**: ZimageBase/Qwen edit/ChatGPTアダプルト解禁/Grok動画（>>833）。

## 注目投稿（画像/動画共有）
- >>823: 潮吹きオナニー動画（PainterLongVideo成果）。
- >>742: miaomiaoRealskin+copycatPVC動画テスト。
- >>797,803: ループ/長動画WF例。
- 画像: 映画インスパイア（>>704）、NG集ロボ（>>739）。

## 全体洞察
- **活気**: Tips交換活発（danbooru/TIPO/nunchaku）。動画がホット（Wan2.2進化）。
- **課題**: マンネリ/ハード高騰。ローカル信仰強（クラウド規制嫌）。
- **トレンド**: 低VRAM量子化（nunchaku）↑、WFループ化、LoRA微調整。Baseモデル待機中。
- **アドバイス提案**: 初心者→Danbooru+LLMスタート。上級者→nunchaku+動画LoRA。

次スレ期待: Baseリリース/50xx実機レビュー。ログ完走で実践Tips満載スレ！