# 🆕 新規トピック（前回からの差分）
- Layer Replay Patcher（Spectrumのディテール向上）
- AnimaYume（軽量T2I）
- aimdo（Dynamic VRAM最適化:32s→15s）
- TensorRT（Wan upscale高速化）
- smZNodes（ComfyUI-WebUI互換）
- ImpactWildcardProcessor + Regex（ComfyUIコメントアウト）
- comfyui-adaptiveprompts / LoRA Manager（Wildcard強化）
- `--use-pytorch-cross-attention`（Sage Attention黒画像修正）
- DaSiWa WF（初心者導入）
- LTX-2.3（MV/リップシンク、FP8 vs GGUF Q8、Desktop版ZIT内蔵）
- Smoothmix + Light2xv LoRA（Wan2.2、High3.0/Low1.5）
- FLF2V（ループ白飛び回避、EXITIUM VICTRIX推奨）
- i2v服変更（Wan2.2）
- InfiniteTalk（リップシンク、Grok上限/検閲）
- Anima特化LoRA（顔アップ100枚/5000step、dim下げ）
- ClearAnime VAE（Anima内蔵多）
- プロンプト英語文法論争（"focus on her ass." vs "focus is her ass."）
- Claude最適（ビーデル髪）
- Intel Arc B580（画像コスパ高、動画不可）
- Radeon RX9060XT/9070XT（ROCm高速、5万以内）
- RTX5060/32GB（aimdo効果大）
- Z-Anime蒸留（8step）
- Chenkin Noob V0.5（miomioベース）
- ID-RORA（動作用）
- Unsloth Studio（NVIDIA WebUI）
- Qwen3.5（NSFW善）
- zuntan/Illya休止、kijai氏待ち
- オナネタ論争（生成即抜きvs探求心）
- 中国資金/欧米Flux（国際メタ）
- 脳直結/エロ排除懸念（未来）
- ComfyUI-Anima-Enhancer（ノード検索"anima"）
- wan2.7/LTX長尺（未来）
- Qwen Caption（LLM連携）

---
# 元の本文
# なんJ(5ch) AI画像/動画生成スレッド 総合レポート（Res 4-1000）

## 全体概要
- **対象範囲**: Res 4〜1000（約1000レス）。Stable Diffusion（SDXL/Anima中心）のAI画像・動画生成議論が主軸。
- **主なテーマ**: ComfyUI最適化、高速化ツール（Spectrum/DMD2）、Animaモデル評価・Tips、動画生成（LTX-2.3/Wan2.2）、LoRA学習、プロンプト制御、ハードウェア/GPU議論。新モデル（Illustrious/Z-Anime/Chenkin Noob）情報共有も活発。
- **参加者傾向**: ComfyUI上級者中心。初心者（EasyWan/Forge卒業組）支援多め。RTX3060〜5090ユーザー、低スペック（Intel Arc/Radeon）も。NSFW/エロ生成需要高く、版権再現・オナネタ論争あり。
- **トーン**: 実践的・共有志向。「サンガツ」多用、煽り/釣り混じりつつ親切。技術共有（WF/画像/記事）が豊富。「光のインターネット」自負。
- **トレンド**: Anima席巻（自然言語◎だがピーキー）、高速化ブーム（Spectrum「ゲームエンド級」）、ComfyUI移行加速。課題：互換性/環境差/初心者離脱。

## 主要トピックまとめ

### 1. Animaモデル（最ホットトピック：全レポート貫く）
- **高評価**:
  - 性能/絵師再現/細部（IDカード/瞳）優秀。自然言語解釈抜群（複数キャラ/擬音/状況指示）。LoRA学習しやすく記憶力◎（dim16-64/alpha8-64推奨）。
  - Preview2：画風LoRA強化、日本語崩れ軽減（8step LCM）。ComfyUI最適、Illustrious連携（Animaポーズ→Illustrious塗り→FaceDetailer WF共有）。
- **問題点**:
  - タグ強すぎ（プラグスーツ→エヴァ画風リーク）。目/瞳汚れ、色くすみ（ネガ"grey theme"、サンプラー変更）。複数キャラ混ざり、白光り/メカ雑。
  - Previewゆえ不安定、LoRA作成難航（過学習/指増殖：dim/alpha下げ）。
- **Tips**:
  - 強調(:1.3)効く、カンマ後**半角スペース必須**（英語厳格）。無表情："expressionless" or 「無表情」。NSFW：`explicit/nsfw/sex`+自然言語（"A woman being penetrated from behind."、"focus on her ass."）。Gemini/Claudeでプロンプト生成。
  - 比較：Illustrious（塗り/エロ安定）>Anima（自由度/線/深度）。Pony/SDXL（手軽だがパース弱）。

### 2. 高速化ツール
- **Spectrum Integrated**: Forge Neo/ComfyUIで爆速（3060:49s→36s）。Layer Replay Patcherでディテール↑。SDXL/動画向き（Proper推奨）。欠点：色褪せ/スケジュール不可/初ステップ重。
- **DMD2/WaveSpeed**: Anima Preview2と相性◎（Spectrumより速）。4-8step推奨。AnimaYume（軽量T2I）も。
- **その他**: Greenboost（バグ指摘）、aimdo（Dynamic VRAM:32s→15s）、TensorRT（Wan upscale高速化）。

### 3. ComfyUI運用・トラブルシューティング
- **vs WebUI(A1111/Forge Neo)**: 再現難（シード/サンプラー/VAE/CFG差）。smZNodesで互換。PNGドラッグでWF生成。
- **Tips**:


  | 問題 | 解決策 |
  |------|--------|
  | スペース/コメントアウト | ImpactWildcardProcessor + Regex(`/\*[\s\S]*?\*/|//.*`) + hide_comments |
  | アップデート/エラー | git pull/v0.18.1（VAE Decode修正）、venv分離、StabilityMatrix |
  | Wildcard | comfyui-adaptiveprompts、LoRA Manager |
  | Sage Attention黒画像 | `--use-pytorch-cross-attention`追加、KJNodes Patch無効 |


- **初心者アドバイス**: 公式テンプレから開始、45回環境破壊で慣れ。DaSiWa WF導入。

### 4. 動画生成
- **LTX-2.3**: MV/リップシンク優秀（FP8 vs GGUF Q8：RTX40↑FP8）。extend+lastframe難、声/動きガチャ。Desktop版：速（720p10s=55s）、ZIT内蔵。
- **Wan2.2/Smoothmix**: Spectrum対応、step20+Light2xv LoRA（High3.0/Low1.5）。FLF2V（First-Last Frame）でループ白飛び回避（EXITIUM VICTRIX推奨）。i2v服変更可。
- **InfiniteTalk**: リップシンク。Grok：無料上限厳/検閲強化。
- **課題**: 色味劣化（Latent/VAE宿命）、VRAM食い。

### 5. LoRA/VAE/プロンプト/ハード
- **LoRA**: Anima特化（顔アップ100枚/5000step？）。指増殖→dim下げ。Forge Neo対応。
- **VAE**: SDXL：sdxl_vae.safetensors/ClearAnime。Anima：内蔵多。
- **プロンプト**: 英語文法論争（"focus on her ass." vs "focus is her ass."：実践優先）。ソフトエロ：questionable+LLM wildcard。ビーデル髪：Claude最適。
- **ハード**:


  | GPU | 評価 |
  |-----|------|
  | RTX5090/4090 | コイル鳴き/128GB運用 |
  | Intel Arc B580 | 画像コスパ高（動画不可） |
  | Radeon RX9060XT/9070XT | ROCm高速、5万以内狙い |
  | RTX5060/32GB | aimdo効果大 |

### 6. 新モデル/ツール・コミュニティメタ
- **新着**: Z-Anime蒸留（8step）、Chenkin Noob V0.5（miomioベース）、ID-RORA（動作用）、Unsloth Studio（NVIDIA推奨WebUI）、Qwen3.5（NSFW善）。
- **人物**: zuntan/Illya休止？ kijai氏待ち。
- **メタ**: オナネタ論争（生成即抜きvs探求心）。進化停滞感（5本指後絵心次第）。国際：中国資金/欧米Flux。未来：脳直結/エロ排除懸念。

## 共有リソース（重複除去）


| カテゴリ | 内容 | 参照 |
|----------|------|------|
| WF/JSON | SDXL分割: [チェックポイント](https://huggingface.co/asfdrwe/wai16DMD2/blob/main/%E3%83%81%E3%82%A7%E3%82%A7%E3%82%AF%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%83%A2%E3%83%87%E3%83%AB%E5%88%86%E5%89%B2.json), [sdxl-workflow](https://huggingface.co/asfdrwe/wai16DMD2/blob/main/sdxl-workflow.json)<br>Anima→Illustrious WF (>>467/555) | 多 |
| モデル | DMD2, cottonanima_preview2, Light2xv LoRA, EXITIUM VICTRIX | 多 |
| ツール | ComfyUI-Anima-Enhancer（ノード検索"anima"） | >>881 |
| GPUベンチ | やかもち比較 | >>295 |

**注**: wai=Illustrious派生（非wanvideo）。FLF=First-Last Frame（非FLUX）。

## トレンド・注目点・結論
- **人気**: Anima（自然言語/LoRA）+Spectrum/DMD2高速化。ComfyUI安定運用進む。
- **課題**: 環境差/WF複雑さ/新モデル不安定。NSFW手軽さ不足。
- **未来**: wan2.7/LTX長尺、Chenkin/Z-Anime実用報告、Radeon/Arc低価格GPU台頭、LLM連携（Qwen Caption）。
- **総括**: 上級者主導の質高共有スレ。初心者歓迎でローカルAI最前線。次スレ：Anima正式版/エロファインチューン注目。詳細相談時は特定Res参照推奨。
