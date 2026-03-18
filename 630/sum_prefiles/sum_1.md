### なんJ(5ch) Stable Diffusion/ComfyUIスレッド ログレポート (Res 4-239)

#### 1. スレッド概要
- **期間/範囲**: Res 4-239（116終了宣言あり、以降継続）。主にComfyUI更新、anima2/Nekofantasiaなどの新モデル議論、LoRA作成Tips、バグ報告、エロ生成の限界が中心。
- **参加者傾向**: ローカル環境ユーザー中心。ComfyUIヘビーユーザー、モデルファインチューナー多め。エロ（特に二次元）需要強く、リアル系優位を嘆く声多数。
- **ホットトピック**: ComfyUI 0.17.0/0.17.1更新（app mode導入）、anima2 Preview2の進化、Nekofantasia（SD3.5ベース新アニメモデル）の期待/懸念。

#### 2. 主要アップデート情報
| 項目 | 詳細 | 関連Res |
|------|------|---------|
| **ComfyUI 0.17.0** | app mode新機能（簡易UI）。ロゴ変更（くるくるアニメ→静的ロゴで読み込み判別しづらい不満）。入力系カスタムノードバグ（候補クリックで入力消滅）。メモリ効率化でカスタムノード切り捨て多発。comfy-kitchen（高速化カーネル）追加。 | 21,38,42,57,59,69,74,136,210,211 |
| **ComfyUI 0.17.1** | 軽微アップデート（3h前）。 | 135 |
| **anima2** | プロンプト反応向上、構図バリエーション増、LoRA学習改善（指/解像度問題残る）。Preview2リリース（画風安定化）。自然言語強いがガチャ性低め（構図固定傾向）。VAE優秀で細線潰れにくい。 | 27,136,137,138,141,152,155,166,175,196,209,219 |
| **Nekofantasia** | SD3.5Mベースのコミュニティアニメモデル。400万点手動レビュー（gigantic breasts等排除？）。Danbooruタグ再現狙い、LoRA不要設計。生成速度遅め（B580でeuler simple 30steps=16秒）。エロ禁止（NSFW検閲疑い、肉塊化）。サンプル微妙/手書き感強め。 | 86-94,99-112,114,116-120,123,146 |
| **その他** | Illustrious/wai：平均点高く安定（品質タグ不要）。Z-Image：lyingポーズ安定。FLUX.2 klein：nvfp4非対応エラー（fp8推奨）。Gescharアプリ削除（原因不明）。 | 35,79,125,202,235 |

#### 3. LoRA/学習Tips & 設定議論
- **anima2 LoRA作成成功例** (Res141): sd-scripts使用。dim64/alpha32、text_encoder_lr=3.5e-5、unet_lr=7e-5、AdamW、constant scheduler、sigmoid timestep、200枚(反転込)、danbooruキャプション、768リサイズ、バッチ2、face_crop_aug_range=[2.0,3.0]等。50epochsで4h(4080S)。text_encoder_lr有効？（unet_only避け推奨）。
- **比較実験** (Res52): Text Encoder Learning late/LR warmupの有無で絵柄激変。なしが最良。
- **問題点**: animaで頭部消失（髪/目色プロンプトで回避）。画風暴れ→LoRA前提（強度0.2-0.55）。素材40-200枚推奨。
- **Tips**: network_train_unet_onlyオフ推奨（崩れ増）。dim64でデフォルメ絵柄良。--sdpaでVRAM/時間短縮。LLM(Qwen3.5 4B/9B)でプロンプト拡張（自然言語+タグ）。

#### 4. 問題点/バグ報告
| カテゴリ | 内容 | 解決Tips |
|----------|------|----------|
| **ComfyUIバグ** | ワード候補クリックで入力消滅。DynamicPrompt小数ウェイト無効（整数で代用）。Load Image Ctrl+V失敗（ノード貼り付け）。 | JS inputイベント発火（Res70）。kohya_lora_param_guiでエポック保存（Res55）。 |
| **生成クオリティ** | anima：構図固定、画風不安定、エロで頭消失。Neko：背景/タグ反映弱、NSFW肉塊化。指6本、顔変面。 | 品質タグ不要/ブレ増（anima）。自然言語+表情記述。interlocked fingersで恋人繋ぎ。 |
| **ハード/互換** | VRAM12GBオフロード前提。50シリーズnvfp8推奨。更新で生成遅延。 | 安定Ver残存（Res61,74）。Claudeでカスタムノード改修（Res68）。 |

#### 5. エロ/動画生成の議論
- **二次エロ限界**: 動画は体位/顔変面で期待薄（リアル優位）。プレス体位顔隠れ変面。anima/Nekoエロ弱（学習/ライセンス禁止疑い）。画像優位派多。
- **Tips**: High(Smooth)+Low(Dasiwa)最適？ Calvin klein outfits/Danbooruタグ安定。faceless male+povで主観。flat chest, small breasts併記で貧乳。
- **動画**: SVIで10-12秒量産可。gugugaga動画可愛い（仕草表現進化）。

#### 6. ツール/拡張 & 雑談
- **便利ノード**: ImpactWildcard、rgthree Fast Groups Bypasser（キャラ/LoRAトグル）。Clibor+マウスジェスチャー。
- **他スレ移行**: Pink板消滅→CG板【AIエロ画像32】。
- **モデル比較**:
  | モデル | 強み | 弱み |
  |--------|------|------|
  | anima2 | 自然言語/VAE優秀、LoRA親和高 | ガチャ性低、画風暴れ |
  | wai/Illustrious | 安定平均点高、タグ不要 | 構図ガチャ高？ |
  | Nekofantasia | タグ再現、LoRA不要？ | エロ禁止、速度遅 |
- **コミュニティ動向**: 外人承認欲求強（未完成公開）。手動レビュー疑問視（審美眼信用？）。エロ需要がローカル存続の鍵。

#### 7. 全体傾向 & 注目点
- **ポジティブ**: anima2進化でLoRA/SDXL代替加速。app modeで初心者対応。ローカル動画優位（テック企業雲泥）。
- **ネガティブ**: 更新バグ祭り（様子見派増）。エロ/二次元停滞。Nekoエロ禁止で需要限定的。
- **今後期待**: anima正式版、Nekofantasia進捗、ComfyUI安定化。LLM連携でプロンプト自動化。
- **ユーザー感情**: 試行錯誤活発（Tips共有多）。「赤ちゃん」vs「WF組む人」分断（app mode）。

このレポートはログのエッセンスを抽出。詳細検証時は原文参照推奨。