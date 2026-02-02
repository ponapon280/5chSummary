# なんJNVA部スレッド総合レポート（レス4-1000）

## 全体概要
このレポートは、5ちゃんねるなんJ板のAI画像・動画生成スレッド（なんJNVA部/ぷにぷにNVA部★26など）のログ（総レス約1000）を5パートに分割した要約を統合・重複除去したもの。主な焦点は**Stable Diffusion系ツール（ComfyUI中心、A1111/Forge Neo卒業傾向）**と**アニメ/NSFW特化モデル（Z-image/ZIB/ZIT/Anima/Illustrious/wai/Pony）**の実践共有。LoRA学習、プロンプト最適化、VRAM効率化、動画生成（Wan2.x/PainterAI2V）が活発。エロ生成Tips（gigantic breasts/pussy/触手など）が半数以上を占め、新モデル評価とトラブルシューティングがスレを推進。荒らし（デブ画像連投/bf-ID）対応やハード価格高騰（SSD）も散見。参加者はRTX40/50シリーズ（5090/4070ti）ユーザー中心で、生成画像/WF共有文化強い。期間推定：2025-2026年頃。総レス1000超の技術コミュニティ好例。

## 主要トピック別まとめ

### 1. 画像生成モデル・ツール評価
新モデルサイクルが加速（Z-image系→Anima）。エロ/構図/速度重視。


| モデル | 強み | 弱み/課題 | Tips/活用例 |
|--------|------|-----------|-------------|
| **Z-image/ZIB/ZIT** | 高速（Tiled Diffusion対応、1024x1024/30秒）、構図固定◎、LoRA容易（musubi-tuner、dim16/学習率5e-4）。SDXL後継候補。 | ベースブレ大、エロ初期弱（LoRA併用で改善）。FT時loss収束難（fp16/VRAM富豪向け）。 | Simple+Euler sampler最強。Moody ZIB + ZIT WF（Civitai）。NVFP4変換で容量4GB/効率3.5倍（50xx限定）。Qwen-Image-2512-Turbo-LoRAで2-4step高速。 |
| **Anima** (DiT/2B、新規2025/9リリース) | 軽量高速（24step/12秒@5070ti）、プロンプト追従◎（自然言語/Danbooru/絵師タグ/NSFW：クンニ/乳首/ちんこ）。構図/描き分け自由度高。 | 指/手破綻多（4本指）、絵柄不安定、日本語弱。LoRA未成熟（diffusion-pipe/Windows面倒）。hires fix後背景ノイズ。 | ネガ（ugly/rough sketch）、euler_ancestral。SDXLリファイナー併用。Qwen0.6B TEで性能向上。高解像（1280x1280）安定。Deep Shrink（ダウンスケール→生成→アップ）で細部抑制。 |
| **Illustrious/wai** (waiは派生) | ベース安定、NSFW◎。 | 速度中庸。 | LoRA重宝（3D slider/陰毛調整）。FT待ち。 |
| **その他** (Pony/susamixEX/Anima/リアス/Chroma/Klein) | Pony: プロンプト互換。susamixEX: 忠実。Anima補完。 | 身体崩れ（pussy/骨盤）、リアル弱。 | score_9~6タグバランス（高スコア固定避け）。絵師タグ注意（@toriyama akira崩壊）。 |

- **生成例**: メカ娘/元素法典風/触手産卵/母乳/おしっこ/ダブルフェラ級。flat/boldline LoRA現役。

### 2. 動画生成関連
Wan2.x中心。リップシンク/動き改善実験活発。


| ツール | 強み | 弱み | Tips |
|--------|------|------|------|
| **Wan2.2/Wan2.1/EasyWan22** | 高動き、NSFW一択（enhanced派生）。 | 満面の笑み病、マーライオン減少もピストン遅延/動きガチャ。 | WF次第q4高品質。InfiniteTalkでリップシンク（日本語自然、無音Embeds）。RIFE VFI/Zero-out/TensorRT高速化（5秒/3分初回）。after anal i2vで余韻（3秒繋ぎ/SVI切り替え）。 |
| **PainterAI2V** | 体自動動き、FLF（First-Last Frame）2V。 | 最終フレーム荒れ/色変わり/モザイク、口動き悪い。 | 最終4フレーム破棄/繋ぎ。Multimodal GuiderでLTX UP。 |
| **LTX-2** | 5秒コスパ高、アジア人対応。 | 口大げさ/歯崩れ/近接崩壊。 | ダンスLoRA実験。 |
| **Grok API** | 480p/1秒0.05ドル、エロOK、日本語音声向上。 | 料金高（15秒4本/$5）、motion大袈裟。 | - |

- **音声**: Qwen3-TTS/T5Gemma-TTS/MMUAUDIO（アニメNSFW待ち）。

### 3. 環境構築・最適化
ComfyUI/reforge/Forge Neo推奨（A1111化石）。Stability Matrixで管理。

- **推奨**: Linux/WSL2（Trellis2対応）。--full_bf16/medram（12GB可）。SageAttention/fast注意（NaN/qwen死）。
- **ハード**: RTX5090/5070ti/40xx。SSD価格高騰（m.2 4TB:7-15万、在庫枯渇→SN850X即買い）。Cドライブ分離/外付けHDDバックアップ。
- **保存**: PNG（メタ/WF残り）vs WebP（圧縮軽量、Comfy不安定）。JXL希望。
- **LoRA学習**: musubi-tuner/CAME/RAdam（10-40分）。||区切り（複数ワード）。

### 4. トラブルシューティング


| 問題 | 解決策 |
|------|--------|
| VRAM右肩上がり（QwenVL GGUF） | バッチ処理代替/Load Image Dataset。 |
| 出力荒れ（PainterAI2V） | 最終フレーム破棄。 |
| susamix/vpred黒画像 | reforge/Advanced Model Sampling。 |
| LoRA効き弱 | 強度2.0。 |
| Forgeバグ（ネガ空/ Latentアップスケール） | 新設定有効化/--disable-sage/Stability Matrix torch固定。 |
| enb肥大/Clip_skip不一致 | カスタムノード残骸削除。 |
| 猫箱.moe | マルウェア注意（代替推奨）。 |

- **相談**: チャッピー/Gemini/LLM（ハルシネーション注意）。

### 5. コミュニティ・雑談
- **共有精神**: WF/生成画像/litter/Civitai活発。選挙/ゲーム放置/懐古（waifuDiffusion/フラット革命）。
- **問題**: 荒らし（デブ連投/bf-ID）→NG/chmate json共有。自演/自画自賛批判。
- **クラウド**: Grok安いが課金消耗。pollo.ai夜逃げ疑い。
- **二次元需要**: ローカル天国（実写規制/pixiv BAN）。実写派AV推奨ネタ。

## トレンド・展望
- **ホット**: Anima（ダークホース、プロンプト革命/ZIB超え期待）→LoRA/高解像待ち。Z-image高速実用化（NVFP4/Tiled）。動画リップ進化（InfiniteTalk/Wan2.2）。
- **シフト**: A1111→ComfyUI。DiT/TE（Qwen/Gemma）時代。エロ強化/アジア人対応待ち。
- **課題**: VRAM/互換性/指破綻/モデルサイクル激化。Haoming02神対応文化。
- **次スレ期待**: Anima LoRA本格/ZIBエロチューン/wai FT。継続監視推奨。

このレポートは重複を排除し、時系列進化を反映。詳細はCivitai/HuggingFace参照。追加質問歓迎。