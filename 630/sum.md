# 🆕 新規トピック（前回からの差分）
- Nekofantasia（SD3.5ベースアニメモデル、Danbooruタグ再現）
- Z-Image（lyingポーズ/リアル肌質感）
- FLUX.2 klein（fp8推奨）
- Gescharアプリ削除
- Spectrumノード（block_indices=3,5,9, spectrum=true, warmup=8-10で高速化）
- EasyCacheノード（Sampler前挿入で高速化）
- comfy-kitchen（メモリ効率化）
- Resolution Master / Save Image Extended (WebP)
- Stability Matrix（ComfyUI/Reforge入門推奨）
- Kohya_ss/sd-scripts（LoRA作成具体手法、dim64/alpha32設定）
- Animaプロンプト黄金律（自然言語+Danbooru混在、LLM拡張）
- 複数キャラ生成（リージョナル/インペイント、VLM Florence2キャプション）
- GreenBoost/DynamicVRAM（低VRAM拡張）
- AMD/ROCm相談
- DDR4安価調達
- Grok動画生成（爆速だが規制強化）
- Seedance2.0
- fish audio s2 pro（VRAM24GB+音声生成）
- IrodoriTTS合成
- 生成クオリティ問題（指6本/顔変面/NSFW肉塊化）
- ComfyUIバグ（Ctrl+V/Z不具、DynamicPrompt小数無効、真っ白画像）
- 互換問題（Flux OOM、NAI/Civitai検索死、Gescharログイン不能）
- エージェントAI自動プロンプト期待
- 次スレLTX NSFW進捗期待

---
# 元の本文
# なんJ(5ch) Stable Diffusion/ComfyUIスレッド ログレポート (Res 4-1000)

## 1. スレッド概要
- **対象範囲**: Res 4-1000（約1000レス）。なんJ VA部（NVA部）スレッドで、主にローカルAI画像・動画生成（Stable Diffusion/ComfyUI中心）の実践共有。
- **中心テーマ**: Anima（特にAnima2 Preview2）の構図力・自然言語対応を高評価しつつ、Illustrious（リアス/wai派生）との比較、ComfyUI更新（app mode/高速化ノード）、LoRA作成、ハード最適化、動画生成（LTX2.3/Wan）。エロ（二次元NSFW）需要強く、プロンプト/ WF共有活発。
- **参加者傾向**: ComfyUIヘビーユーザー・モデルファインチューナー中心。Anima移行組増加もリアス安定派残存。低スペックユーザー（VRAM6-16GB）の苦労話多め。サンガツ氏（Anima開発者？）の更新報告が活気源。「赤ちゃん」煽り・スパム混在もTips交換熱い。
- **全体トーン**: 試行錯誤活発。Anima革新期の過渡期で、リアス「ぬるま湯」vs Anima「プロンプト必須」の対立。次スレ（なんJNVA部★631）立て済み。

## 2. 主要モデル評価・比較
Anima旋風がスレを席巻。LoRA前提で絵柄克服が定番。


| モデル | 強み | 弱み | Tips/関連Res |
|--------|------|------|-------------|
| **Anima2 (Preview2)** | 構図自由・自然言語追従抜群、VAE優秀（細線潰れにくい）、LoRA親和高。手指/背景安定化進む（1536解像度試作）。複数キャラ可（リージョナルプロンプト）。 | 画風暴れ・固定化、指/頭部消失、エロ弱（頭隠れ）。ガチャ性低。 | 自然言語+Danbooruハイブリッド（主語明確: "an anime girl"）。品質タグ不要。LLM(Qwen3.5)で拡張。LoRA: dim64/alpha32, unet_lr=7e-5。Res27-219,241-278,446-649,851-1000 |
| **Illustrious (リアス/wai)** | 安定平均点高、タグ不要でポン出し簡単。細部修正向き。 | 構図バリエーション少なく背景破綻。自然言語弱。 | Anima i2i仕上げcombo。Z-Image lyingポーズ併用。Res35,79,242,414,853-855 |
| **Nekofantasia** | SD3.5ベースアニメモデル。Danbooruタグ再現狙い、LoRA不要設計。 | 生成遅（B580で16秒）、NSFW検閲疑い（肉塊化）、手書き感強。 | 期待/懸念混在。Res86-146 |
| **Z-Image** | lyingポーズ/リアル肌質感別格。 | 2D非対応。派生多（turbo/bass）。 | Res125,947-976 |
| **その他** | FLUX.2 klein: fp8推奨。Gescharアプリ削除。 | - | Res202,235 |

- **比較トレンド**: Anima→リアス移行派増加も併用主流。「Anima凄い」vs「使いこなせてないだけ」論争（Res244,278,437）。

## 3. ComfyUIアップデート・高速化Tips
- **更新履歴**: 0.17.0/0.17.1（app mode新UI、メモリ効率化もカスタムノード切り捨て）。Animaパイプラインv1.4.1→1.4.5（LoRAバグ修正、進捗表示）。
- **好評**: app mode（WFコンパクト/タブ自動読み込み）。--gpu-onlyで5090高速化。
- **不満/バグ**: ロゴ変更で読み込み判別しづらい。ワード候補クリック入力消滅。複数WF再開バグ。Preview未対応。
- **高速化ブーム**:


  | ノード/設定 | 効果例 (RTX例) | 注意 |
  |-------------|----------------|------|
  | **Spectrum** | 30step→18秒（block_indices=3,5,9, spectrum=true, warmup=8-10） | easycache競合、絵師タグ弱化。Forge Neo対応。Res709,745,894,973 |
  | **EasyCache** | Sampler前挿入で20step/24s (4060) | Z-Image互換。Res894,955 |
  | **comfy-kitchen** | メモリ効率化。 | Res21,38 |
  | **その他** | Resolution Master, Save Image Extended (WebP)。--sdpa/VRAMオフロード。 | Res487,563 |

- **入門推奨**: Stability Matrix → ComfyUI/Reforge/Forge Neo。EasyWan卒業論争（Comfy難易度高も移行加速）。

## 4. LoRA/学習・プロンプトTips
- **LoRA作成成功例**: Kohya_ss/sd-scripts。素材40-200枚（反転込、Danbooruキャプション、768リサイズ）。dim64/alpha32, text_encoder_lr=3.5e-5/unet_lr=7e-5, AdamW, 50epochs/4h(4080)。network_train_unet_onlyオフ。画風LoRA: 複数キャラ/絵師画像即学習（Civitai参考）。
- **プロンプト黄金律 (Anima特化)**: `an anime girl, [自然言語: She is walking], [Danbooru: 1girl, large breasts], masterpiece, score_7`。主語明確、三人称。LLM(Qwen3.5 4B/9B)で拡張（markdown構造化）。エロ: mating press (folded, legs over head), interlocked fingers, faceless male+pov。ネガ: 尻穴/3d/realistic。
- **複数キャラ**: キャラ名主語+順番記述、リージョナル/インペイント。VLM(Florence2)でキャプション（80 words以内）。

## 5. ハードウェア・環境議論
- **推奨スペック**:


  | 用途 | VRAM | RAM | GPU例 |
  |------|------|-----|-------|
  | 画像 | 12-16GB | 32GB+ | 4060Ti/5090 (3-6秒生成) |
  | 動画 | 24GB+ | 96-128GB | 5090+Linux/WSL |


- **最適化**: GreenBoost/DynamicVRAM（低VRAM拡張）。AMD/ROCm相談多（NVIDIA優位）。DDR4安価調達。
- **懸念**: 50x0電力増/価格高。メモリ暴騰。

## 6. 動画・音声生成
- **LTX2.3**: 1080p/20秒高評価（リップシンク/自然空気感）。kijai分割+RuneXX WF。弱点: エロ/アニメ弱、字幕出やすい、日本語カタコト（LoRA待ち）。Res609-637。
- **Wan2.2/2.3**: エロ/LoRA豊富No.1。ループ優秀。dasiwa v10/SmoothMIXv2。Res378,634-640。
- **その他**: Grok（爆速も規制強化/画質低下）。Seedance2.0格差。fish audio s2 pro（VRAM24GB+）。IrodoriTTS合成。
- **課題**: リップシンク難。High(Smooth)+Low(Dasiwa)廃れ？ ローカル優位（クラウド泥）。

## 7. 問題点・バグ・トラブルシュート


| カテゴリ | 内容 | 解決Tips |
|----------|------|----------|
| **生成クオリティ** | 指6本/顔変面、複数キャラ混ざり、構図固定。NSFW肉塊化。 | 指指定/interlocked fingers。品質タグオフ。ネガ強化。Res449,492,643 |
| **ComfyUI** | Ctrl+V失敗、Ctrl+Z不具（Firefox）。DynamicPrompt小数無効。真っ白画像（LLM思考混入）。 | Chrome推奨。JSイベント発火。システムプロンプト修正/Gemini。Res70,940,992 |
| **互換** | Flux OOM。NAI/Civitai検索死/規制。Gescharログイン不能。 | fp8推奨。Cookie消去/どんぐりハンター。Res313,934 |

## 8. コミュニティ傾向・今後展望
- **トレンド**: Anima/LoRAエコシステム拡大。Spectrum祭りで高速化進化。動画シフト（LTX/WanエロLoRA待ち）。ローカル存続鍵（エロ需要）。
- **対立**: Anima開拓派 vs リアス待機派。EasyWan vs ComfyUI。低スペ vs 高スペ。
- **ポジティブ**: Tips/WF共有多（サンガツ更新活気）。初心者歓迎（Stability Matrixから）。
- **ネガティブ**: 更新バグ祭り。Grok/クラウド規制強化→Geminiシフト？
- **期待**: Anima正式版/high解像度。RTX50x0実機報告。エージェントAI自動プロンプト。次スレでLTX NSFW進捗。

**レポート注記**: 重複削除・最新情報優先抽出。wai=Illustrious派生（wanvideo無関係）、FLF=First-Last Frame（FLUX無関係）。詳細は元ログ参照推奨。質問歓迎！
