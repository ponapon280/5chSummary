# なんJ NVA部 AI生成スレッド 統合レポート (>>21-1000)

## 1. スレッド全体概要
- **範囲/規模**: 継続スレッド後半部（>>21〜>>1000、総約1000レス）。ComfyUI/Wan2.x系ツールのワークフロー（WF）共有、LoRA作成/共有、動画生成（I2V/SVI/LTX）、音楽生成（HeartMuLa）、ハードウェア最適化が中心。後半はZ-Image base（ZIB、旧Z-image base）リリース待ち・検証が最大山場。
- **参加者傾向**: 上級者中心（ローカル環境構築勢、RTX50XX/4070ユーザー）。WF/作例即公開文化活発。初心者Tips散見。自虐・煽りネタ（「soon詐欺」「赤ちゃん」「ゲームエンド」）満載。
- **ホットトピック推移**:


  | 時期 | 主眼 |
  |------|------|
  | >>21-239 | Wan2.x動画（InfiniteTalk/PainterAI2V）、HeartMuLa音楽、NSFW LoRA、絵師vsAI論争 |
  | 240-442 | Grok NSFW復活、SmoothMix V2炎上、SVI WF共有、LoRA素材Tips |
  | 443-644 | Z-imageリリース期待ピーク、LoRA学習ツール（AI-Toolkit）、動画高速化 |
  | 645-845 | ZIBカウントダウン、モデル比較（smoothMix/DaSiWa/LTX-2）、ハード故障報告 |
  | 846-1000 | ZIBリリース実況・検証（アニメ強/実写弱）、ツールトラブル（Forge Neo） |


- **次スレ**: なんJNVA部★617（>>978）。

## 2. 主要トピックまとめ
### 2.1 動画生成ツール・WF
- **Wan2.x / InfiniteTalk / PainterAI2V / SVI**: 1分MV作例（HeartMuLa楽曲+リップシンク）。PainterAI2V（WAN2.2版、GitHub: [princepainter/ComfyUI-PainterAI2V]）でFPS同期可能。SVI（ちびたい版WF共有、LTX音付けcomboで10秒生成、56GB VRAM）。トラブル: mp4メタデータ欠損、エラー多発（LightX2V併用推奨）。
- **SmoothMix V2**: 高速化進化（顔崩れ減）もマーライオン（口から精液）問題で炎上（CFG/LoRA依存指摘）。High/Low調整（3.0/1.5）、3段サンプラー有効。V1回帰派多。
- **LTX-2 / DaSiWa**: i2v LoRAで初期フレーム保持↑。Wan2.2動画に声/効果音付与トレンド。リアス/Noob/Illustrious（wai派生）耐性高。
- **Tips**: FLF（First-Last Frame）指定で制御↑。CRF22エンコード、JPEG XLロスレス保存（PNG比70%軽量）。

### 2.2 音楽生成
- **HeartMuLa (RL-oss-3B-20260123)**: ささやき声再現。プロンプト（カンマ区切り、TopK/Temperature調整）。Suno歌詞→音声文字起こし精度高。7Bモデル待ち。

### 2.3 LoRA/モデル作成・共有
- **NSFW特化**: Klein 4B（ひよこ/チェリーパスタ/鼻射）、Enhanced SVI用。素材: 45枚余裕（Banana/QIE水増し、DuckDuckGo英語検索）。設定: dim64/512x512/bfloat16/FP8、RAdamScheduleFree（3060 12GBで6h）。
- **ブレンド/マージ**: 個別学習後マージ（80%再現OK）。Dim/Alpha過剰で破綻注意（強度0.8推奨）。
- **ツール**: AI-Toolkit（ZIT対応速い）、kohya_ss_gui/sd-scripts/OneTrainer。Civitaiアップ苦労。
- **共有例**: SDXLパトラ子、Mega/Catboxリンク（Ew1HCbIS#ie359KRqBD5UrVCeIMqjS0OmPSQjG76lYJc-Ys6YiWo）。

### 2.4 Z-Image / ZIBリリースイベント（後半最大トピック）
- **経緯**: Turbo（ZIT）廃止後、Base（ZIB、12.3GB、bf16）1/28早朝HF/ModelScope公開。ComfyUI 0.11対応（Text to Imageノード）。
- **評価**:


  | 強み | 弱み |
  |------|------|
  | アニメ: 手足正確、多人数書き分け | ノイズ/4本手/実写奇形 |
  | LoRA学習軽量（12GB VRAM） | 生成時間長（1536²/30steps=30秒）、検閲疑い |
  | 自然言語プロンプト有効 | 小サイズ崩れ、Turbo LoRA相性悪 |


- **Tips**: Guidance 3-5、Steps 28-50。ZI+SAM3 i2i背景分離。エロ/リアス/noob LoRA即学習予想。

### 2.5 ハードウェア/最適化
- **RTX5090**: 価格59.8万、電力600W超（ブレーカー/ブラックアウト/煙報告）。Pro6000値下げ推奨（VRAM3倍）。詐欺注意（Amazon17万）。
- **最適化**: SageAttention3、flash_attn、FP8/bf16。RAM80GB+、電源強化。CPU生成（FastSD）代替。

### 2.6 ツールトラブルシュート
- **ComfyUI/Forge Neo**: WD14 Tagger干渉、--sageエラー（torch2.9更新）。Stability Matrix推奨。
- **その他**: CLIP Vision無効、ControlNetバッチ効かず、Qwen-TTS遅い。KritaプラグインWIP（漫画コマ枠生成）。

### 2.7 Grok / その他
- **Grok**: NSFW復活（軟体動き、プルプル指摘も忠実度↑）。スケベプロンプト強。
- **プロンプトTips**: 前傾騎乗位（cowgirl position, leaning forward + hanging breasts）。パンツもっこり回避。
- **絵師vsAI**: AI優位（手描き時代遅れ、商業導入）vsハイブリッド擁護。黙ってAI活用実態。

## 3. 共有リソースまとめ
- **WF/モデル**: InfiniteTalk（前スレ224/>>77）、PainterAI2V GitHub、HeartMuLa RL-oss-3B、ZIB（z_image_bf16.safetensors）。
- **ツール**: AI-Toolkit、OneTrainer fp8、musubi-tuner。
- **リンク/作例**: LoRA Mega/Catbox、>>64 MV、>>549 AI曲、>>463赤ちゃん動画。

## 4. 全体傾向・洞察
- **ポジティブ**: WF/LoRA即共有、サンガツ文化。SVI/LTX comboでNSFW動画主流。ZIBでローカル強化加速。
- **課題**: 環境構築疲労（1日無駄多）、VRAM/電力限界、SmoothMix炎上（無料奉仕あるある）。
- **トレンド**: 動画>静止画、LoRA自作民主化（12GB可）、自然言語プロンプト移行。中国OSS期待。
- **ムード**: 技術追い求め屋化。ZIBリリースで熱狂ピークも「yesterday soon」体質。
- **今後注目**: ZIB LoRA/エロチューン検証、WAN2.5/HeartMuLa7B、ComfyUI自動化、3D/漫画API。

**総括**: 実践志向の活況スレ。高速進化とハード限界の狭間でコミュニティ結束。詳細は元ログ/次スレ確認推奨。追加質問歓迎。  
※wai: Illustrious派生（wanvideo無関係）。FLF: First-Last Frame（FLUX無関係）。