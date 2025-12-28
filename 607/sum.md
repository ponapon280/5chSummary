# なんJ AI生成スレッド（なんJNVA部）総合レポート

## 1. 全体概要
- **スレッド範囲**: なんJ板のなんJNVA部スレッド（1〜988レス程度）。Stable Diffusion（SD1.5/SDXL中心）のローカル環境構築・運用・エロ生成Tipsが主軸。ComfyUI WF共有、LoRA作成、動画生成（wan2.1/2.2、PainterLongVideo）、ハード最適化が活発。
- **雰囲気**: なんJらしい喧嘩腰・自虐・エロネタ満載。低スペ貧乏勢の苦労談 vs 高スペ自慢（RTX5090/RAM128GB）が定番。技術共有（WF/LoRAリンク、作例貼り）が互助精神強く、初心者質問と上級者Tips共存。
- **参加者傾向**: 実践派中心（VRAM12-72GB、RAM32-192GBユーザー）。エロ特化（ロリ/幼女体型、特殊性癖）が20-30%だが技術論重心。時期はクリスマス前後〜年末、RTX5090発売直後で価格議論熱い。
- **トレンド移行**: SDXL → ZIT/wai（Illustrious派生）/セミリアルへ。低スペ高速化（4step/nunchaku）とComfyUI深化が進む。

## 2. 主要トピック別まとめ

### (1) PCハードウェア/最適化（高騰・トラブル多め）
- **メモリ/GPU高騰**: DDR5品薄1-3年予測、BTO128GB+18万。RTX5090（74.8万、400W、電気代月1万、発火報告）。PRO4000/4500/5000（VRAM32-72GB、安価だが遅い）。3060/3080継続勢活発。改造（3080→20GB/3万）も。
- **Tips/トラブル**:


  | 項目 | 対策 |
  |------|------|
  | VRAM漏れ/OOM | 7-max/TCMalloc、Unload SD checkpoint、blockswap、Mem reduce拡張 |
  | SSD寿命 | RAM disk/tmpfs、HDD/NASバックアップ（TrueImage/FastCopy/robocopy）、Cドライブ避け |
  | 低スペ対応 | FP16/BF16/GGUF量子化、sageattention/triton、DistorchMultiGPU |
  | その他 | ネットワーク不良、夏冷却不安、CUDA100%でGPU50℃未満 |

### (2) AIモデル/サンプラー/プロンプト評価


| モデル/ツール | 特徴・評価 | 推奨/欠点 |
|---------------|-------------|-----------|
| **サンガツ（セミリアル）** | 柔らか乳質感高、髪サッパリ。DPM++2Mでノイズ対策 | 顔子供/身体オバちゃん、指目溶け |
| **ChenkinNoob-XL-V0.2** | Euler aノイズ→DPM++2M。不安定（キャラ崩れ）、月イチ更新 | out0/out1保持難 |
| **ZIT/nunchaku/z-image** | 高速4step低スペOK、自然言語+Danbooruタグ | LoRA未対応/エロ外人顔、Base未公開 |
| **wai/Illustrious派生（v10-v16）** | 汎用性最高、LoRAなしでDanbooru/体位出やすい、版権/構図強。V-pred（暗所/発色良）vs E-pred（温かみ/LoRA効き） | LoRA忠実性不足、顔自己主張強、乳首形状不満（huge nipples推奨） |
| **Qwen系（QIE2511/2509、Image Edit）** | プロンプト生成/背景直し/LoRA学習速（20エポック、zero_cond_t=True）。NSFW版複数キャラ服除去↑ | layered重い（3060厳）、変化微妙 |
| **NAI V3/V4.5** | 高性能版権再現、リアス系 | 制御難/絵柄ガチガチ |
| **その他** | tanemomix v7（破綻減）、paperMoon/BSSmix（自作マイナー）、RuindFooocus、libidinous系新モデル | DL数300-600で良作探し推奨 |
| **サンプラー** | DPM++（実写感/i2i）、Euler（アニメ化） | 高速化LoRA併用で不具合→切る |

- **プロンプトTips**: 自然言語vs Danbooru議論。手ポーズ難（指閉じ/6本）、ロリ（toddlercon:1.4/aged down、頭身低め）。エロ一貫性（全裸世界観、licking/tongue out、He ejaculates... wet splat）。背景/小物（TE有効+ユニークタグ）。

### (3) LoRA/学習Tips（エロ特化自作主流）
- **エロ/特殊**: ロリ/幼女（WAI12-14安定、行為中破綻注意）、AnimeNudeWank（Qwen共有）、亀頭舐め/penisplay/licking（Wan2.1用）、スケベ椅子（hentai bath stool/cutout_bath_stool、Illustrious用v1公開）、射精/ポールダンス、futanari/百合。
- **作成Tips**: 過学習対策（裸/別衣装/collarbone混ぜ、weight decay）。素材50-100枚、Adafactorオプティ、背景正規化（white background削除）。複数LoRA干渉注意（School Uniform混入）。
- **トラブル**: 白飛び（ノイズオフセット0.1↑）、射精競合（CFG調整）、LoRAエラー（--pin-shared-memory外す）。

### (4) 動画生成/WF共有（ComfyUI中心）
- **主力ツール**: wan2.1/2.2 fp16高速、PainterLongVideo（3-6段連結/30秒）、StoryMem（MI2V顔劣るが動き自然）、StableVideoInfinity。FLF（First-Last Frame）/VFI/ColorMatch/LoRA2種。
- **WF例**: High=Smoothmix + Low=DaSiWa Q8 GGUF（5step顔保持）、llm_encoding/gesture、フレーム補完/アプスケ/FaceDetailer。mp4 D&D→KJnodes、EndImage挿入ループ。
- **課題/Tips**: フリッカー/一貫性（SEGS+AnimateDiff+デフリッカー、低解像度先行）、背景変動（consistence_edit LoRA）。VRAM12GB可、ガチャきつい。

### (5) アップスケ/Detailer/ポーズ制御
- **多段アプスケ**: 5段Tiled（t2i→noise inversion、ESRGANx4+1/2）、肌/目代替（裸皺誤認）。
- **ポーズ**: 指/閉手難（waving/salute+negpip、高denoising博打）。欧米NGポーズ/fellatio化注意。
- **Detailer**: ADetailer [SEP]表情分離、small nipples弱。

### (6) エロ/ユーモア/メタネタ
- **性癖**: ロリ→マイリトルポニー、サーナイト×ノクタス、スケベ椅子/ポールダンス、チキン老害、グラボ売りの少女。
- **ツール**: Photoshop PSDローダー、lama cleaner、モザイク（としあき/MSペイント、メタデータ保持）。
- **マナー**: 画像貼付（モザイク/catbox）、エアプ批判、魔女狩り（AI絵晒しNG）、闇モデル（TOR/Mega）。

## 3. トレンド/示唆・次回注目
- **進化点**: ComfyUI WF文化定着（set/getノード哲学）、低スペ最適化（量子化/RAM管理）、動画長尺化（FLF/VFI）。自作LoRA/ニッチ共有がコミュニティ強み。
- **課題**: LoRA未対応/不安定新モデル、RAM/GPU高騰（「積んどけ」後退）、特殊性癖ガチャ、SSD寿命/発火。
- **示唆**: ローカル冬継続（クラウド/Grok限界）。エロ実験（オナニー動画）が華、低スペTips満載で初心者歓迎。
- **次回注目**: ChenkinNoob V0.3、ZIT Base/エロ版公開、Qwen LoRA普及、RTX5090実運用/LTX-2 OSS、RAM価格安定、fp4動画。

**総括**: AI生成界隈の日常鏡。技術共有活発で、低スペでも楽しめる実践レポート。詳細ログ参照や質問歓迎、サンガツ！