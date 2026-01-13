# なんJ NVA部 AI生成スレッド 総合レポート（4〜1000レス）

## 1. スレッド全体概要
- **ログ範囲**: 投稿4〜1000（約1000レス、複数パート分割）。なんJ板のなんJNVA部スレッドで、次スレ★613へ継続。
- **主なテーマ**: ComfyUIを中心としたAI画像/動画生成の高度な技術共有。特にNSFW（エロ画像/動画）生成に特化。モデル更新（SmoothMix V2, Wan2.2, LTX-2, DaSiWa V9, Z-imageなど）、LoRA作成/共有、ワークフロー（WF）最適化、ハードウェア（RTX 5090/プロ6000, RAM128GB）/VRAMトラブルシュート、環境構築（Linux/Docker/WSL2）が中心。
- **参加者傾向**: 中級〜上級者中心（自作ノード/パッチ/LoRA作成者多数）。低スペ（3060/12GB VRAM）ユーザーも工夫共有。ユーモア混じり（「サンガツ」「抜き用」「シコれない論」）でエロネタ9割だが、実践Tipsが濃密。
- **注目キーワード**: SmoothMix V2, Z-image (turbo/base), DaSiWa V9, LTX-2 (音声/V2V), EnhancedNSFW V2, lightx2v LoRA, NVFP4/FP4量子化, SVI/PLV/FLF2V（First-Last Frame）, Radeon ROCmパッチ, ComfyUI 0.8.2〜0.9.x。
- **全体トーン**: 共有志向・実験熱心。エラー解決/高速化Tips多め。SDXL移行→動画生成フェーズへシフト。waiはIllustrious派生（wanvideo無関係）。
- **トレンド**: High/Lowモデルハイブリッド（High=動き/NSFW強調, Low=顔/安定維持）、LoRA共有文化、低スペ最適化（FP4/NVFP4）、ローカル信仰（検閲回避）。

## 2. 主要議論カテゴリ（重複統合・最新情報優先）

### (1) モデル/ツール更新と評価
新モデル評価が高頻度。動画NSFW最適化が進む。


| モデル/ツール | 評価・強み/弱み | 推奨Tips・関連 |
|---------------|-----------------|---------------|
| **SmoothMix V2** | プロンプト追従/表現力向上。高解像度/フレーム改善だがHigh硬め・腰振り病。高速LoRA（lightx2v）併用。GGUF版でエラー回避。 | High+DaSiWa Lowハイブリッド。公式WF（653）。 |
| **Z-image (turbo/base/edit)** | SDXL超え期待（表現力/LoRA乗せ）。FTモデル（ZWAI/エロ版）半年待ち。Comfy/ForgeNeo前提。 | Baseリリース間近。先行LoRA検証。 |
| **DaSiWa V9/V8** | Low覇権（安定/綺麗）。High応答性悪→EnhancedNSFW V2/FastMove併用。体揺れ抑制。 | High=EnhancedNSFW(Q6)+Low=DaSiWa。narrow eyesで維持↑。 |
| **Wan2.2/lightx2v** | 動画NSFW最適（ピストン/顔射）。I2V/T2V両対応、画質/動き安定。瞳変化/モヤ焼き注意。 | LoRA（ahegao_high_wan, lightx2v_14B）。Easy版でドット絵。 |
| **LTX-2** | 音声生成ブーム（t2v/i2v/v2v、パンパン/喘ぎ声LoRA）。リップシンク良。アニメ絶望/リアル少女ババァ化注意。V2V上位互換？ | Wan→LTX-2音後付けWF（911）。FP4/FP16混在、低スペ可（23分）。 |
| **SVI (WanImageToVideoSVIPro)/PLV** | SVI:長尺/繋ぎ目消し。PLV:エンドフレーム/プロンプト追従高。VRAM食い。 | LoRA必須。バッチ画像参照PR。FLF2V（Rife TensorRT）併用。 |
| **QIE/QIL-2511/2512/SAM3** | マルチアングル内蔵/背景合成。実写リアル。一貫性難（パース/影）。SAM3:小物/pussy検出（crotch推奨）。 | LoRA（Multiple-Angles）。緑背景クロマキー。 |
| **その他** | EnhancedNSFW V2（揺れ抑制）、EXITIUM VICTRIX（モーション抑制）、Flux.2 NVFP4（20秒/1024x1024）、Illustrious（danbooru準拠）。 | FP4/NVFP4低スペ高速（Blackwell5060Ti朗報）。 |

### (2) LoRA作成/共有・NSFW生成技法
NSFW特化LoRA共有が活性化要因。プロンプト（danbooruタグ優位）議論活発。


| LoRA事例 | 特徴・用途 | 備考 |
|----------|------------|------|
| **陰毛系** | Excessive Pubic Hair, stray pubic hair（ill系）。sparse/peek。リアル+キャラで剛毛。 | pubic hair:-1で乱交回避。hymen併用で膜。 |
| **ahegao_high/low_wan** | Wan2.2向け壊れ顔（対魔忍非対応）。アナル/機械姦。 | フレーム113学習。 |
| **lightx2v_14B (kijai)** | 万能動画（ピストン/顔射）。 | T2V/I2V両対応。 |
| **都市伝説解体センター** | 原作再現（wd14タグ）。 | 4090/4h学習。 |
| **その他** | 姫騎士アヘ、触手pit、抜歯/歯無し、フェラ顔射、ブラ貫通脱ぎ。 | Kohya_ss+Emonaviオプティマイザ。ウェイト0.9。正則化画像多め。 |

- **プロンプトTips**: danbooruタグ精密（torogao）。自然言語ハイブリッド（LLM生成）。問題:枕/makura自動（under coversネガ）、缶ビール（can回避）、湯気マンコ（heavy breathing）、男一体化（pov/male pubic hair）。
- **技法**: 背景合成（SDXLガチャ/Blender/white bed sheet）。抜き用4コマ（1girl+working/town）。ポン出し（尻/ケツ）。お辞儀（The girl bows）。

### (3) ComfyUI/WF Tips・問題解決
- **バージョン**: 0.8.2（FP4恩恵、VRAM短縮）→0.9.x（semver急進化、バグ多）。ジョブキューエラー→setノード外出し/Python3.11。
- **自作共有**: Size_Tools.py（動画サイズ自動）、Radeonパッチ（MIOpen/VAE有効化、1.5s高速）、Rife TensorRT（たけのこフォーク）。
- **WF**: サブグラフ展開注意。input/*消去でメタ臭除去。条件付けゼロアウト（時間短縮）。rgthree Seedノード。スパゲティ回避（Gettersジャンプ）。
- **注意**: カスタムノードmissing/マルウェア（docker推奨）。

### (4) ハードウェア/VRAM/環境最適化
- **GPU**: 5090推奨（動画数割速、LoRA学習OK）。pro6000（VRAM48GB+、学習/高解像向き、騒音85℃）。5070Tiブラックアウト（PCIe Gen4/ドライバ581.57）。AMD 7800XT（Linux SmoothMix可）。値上げ/在庫枯渇中。
- **VRAM/RAM**: 16GB厳（SVIカツカツ）→128GB必須（High+Low）。12GB+64GBで低スペ可（10-18分）。
- **環境**: Linux/Docker/WSL2＞Win（速度/メモリ効率）。AI-Toolkit/Singularity初心者向け。仕事PC分離（セキュリティ）。

## 3. 注目トレンド・課題・未来予測
- **トレンド**: 動画シフト（LTX-2音声/SVI長尺）。ハイロー統合/Danbooru+自然言語。低スペFP4/NVFP4。ローカル検閲回避。
- **課題**: 背景一貫性/エロ顔変化/WF見づらさ/VRAM限界/アプデ互換。「自分で作ったエロがシコれない」哲学。
- **未来**: Z-image FTリリース、ブチギレ量子化、WAN2.5/LTX-2 V2V普及、RAM標準化。Comfyクラウド併用。

## 4. 結論・アドバイス
スレはNSFW動画生成の宝庫。**初心者**: ComfyUI+danbooruタグ+SmoothMix V2/lightx2vから。**中級**: DaSiWa Low+EnhancedNSFW Highハイブリッド、LoRA共有活用。**上級**: 5090+Linux+LTX-2音後付けWF。自作パッチ/ノード即適用（Radeon/Size_Tools）。低スペはFP4/GGUF/FLF2V。次スレ★613監視で新モデル検証を。

（レポート生成: 現在。重複削除・統合済み。省略中心、詳細元ログ参照。質問歓迎。）