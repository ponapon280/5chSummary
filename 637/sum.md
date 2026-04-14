# 🆕 新規トピック（前回からの差分）
- Chenkin Noob最新版の版権キャラ追加と無印進化
- リアスのCN細ポーズ優位とファインモデル充実
- ComfyUIのAnima XY Plot/Tile分割WF共有とサンプラー(er_sde/euler a)
- Forge/Reforge Neoの赤ちゃん向け高速化とStability Matrix導入
- 環境スペック: CUDA12.8/Python3.11/Torch2.7.1/VRAM12GB+/RAM128GB/Claude exeインストール/ドライバ595.79/596.02
- 新ツール: 自作画像管理(Claude生成/多形式タグ/WD14)、Scribble Reference LoRA(CN代替)、Calibratedノード(色くすみ解消)
- Qwen3.5-35B-A3B-Uncensored(Q5)/Gemma4 26B A4B/Q4_K_MとComfyUI-QwenVL/llama-cpp_vlmノード
- LLM Tips: Thinking停止(`{%- set enable_thinking = false %}`)、画像→英文変換(CN代替)、DeepL後修正、「状況詳述容姿省け」、トークン切れ対策(系プロOFF)
- Anima LoRA自作(1024再学習/TEなし)、高解像度LoRA(Civitai/dim32/0.6)、Adetailer乳首LoRA、世界樹ニキ調整法
- エロTips: ガニ股(standing+(bowlegged pose:1.5))、twitching penis、panties around one leg、futanari不安定、SAM3性器検出(閾値0.06)
- Hires/アップスケ: 1536OK/Tileノード(継ぎ目0.12デノイズ)/RealESRGAN_x4Plus注意
- 動画生成: Wan2.2(実写寄り/目崩れi2i+Anima修正)、LTX2.3 FLF(First-Last Frame/任意フレーム)、Seedance2.0/litVideo待ち
- 漫画生成: LLM+Animaで4コマ/3コマ(起承転結/コマ割り)、ネーム鍵、ジャンプ炎上(内部AI疑い)
- 規制/逮捕: わいせつ物逮捕(生成AI小中学生模写/無修正販売)、モザ無しNG/非実在グレー/ロリ線引き(実写風NG/二次OK)
- マネタイズ: Patreon/Booth締め付け/無修正海外優位、一枚絵売れず/エロゲ動画推奨、専用スレ「AI画像生成マネタイズスレ ★268」
- 手書きvsAI: 手書き擁護(過程/ブランディング)vs AI結果主義、AI粗悪/画一化批判、萌えエロ過程無視
- その他社会: 日本人GitHub弱/炎上商法批判、AI民主化(自作ツール)、奈良AIアニメPR(6本指指摘)
- 次スレ移行: 「なんJNVA部★638」

---
# 元の本文
# なんJ(5ch) なんJNVA部 AI画像生成スレッド 統合レポート（ログ23〜1000）

## 全体概要
- **対象ログ**: なんJ板「なんJNVA部」スレッドのレス23〜1000（総約1000レス）。主にAI画像生成ツール（Anima v3-preview中心、WAI-Illustrious（wai、Illustrious派生モデル、wanvideo無関係）、Chenkin Noob、リアスなどSDXL/Animaモデル）の議論。ComfyUI/Forge Neoユーザー中心の中上級者層が活発で、エロ画像生成（ガニ股、排泄、penis twitching、spread pussyなど具体Tips多め）が前提。
- **主なテーマ**: Animaのポテンシャル高評価 vs 制御難（画風不安定、CN未対応）。WAIの安定性比較、LLM（Qwen3.5、Gemma4）プロンプト補助、LoRA学習、高解像度進化、ComfyUIトラブル、動画/漫画生成、規制/マネタイズ論争、手書きvsAI価値論。
- **傾向**: 技術共有活発（WF/LoRA/シスプロ公開）。Anima覇権加速中だがWAI安定派残存。エロ特化実践志向でポジ率80%。初心者（赤ちゃん）支援文化あり。次スレ「なんJNVA部★638」移行。

## モデル評価・比較
Animaが高性能だが制御難で議論中心。WAIは「オールマイティ完成形」。


| モデル | 強み | 弱み | ユーザー所感 |
|--------|------|------|-------------|
| **Anima v3-preview/3** | 高クオリティ、自然言語、多人数/表情制御、LoRA再現度上。派生（AnimaYume 0.4、Botan Anima）増加。高解像度LoRA（1536安定、Hires不要）で革命（>>913-922,964）。 | 画風/一貫性不安定、CN/Anytest未対応、暴れやすい、Danbooruタグ効き弱。 | ポテンシャル最高/正式版/CN待ちで移行加速。リアス超え（CNあり同等以上）。 |
| **WAI-Illustrious (wai)** | 安定、無難万能、ポン出し強。 | 暗闇弱、キャラ中央寄り。 | 結論モデル/冒険不要。Anima細指定楽だが好み次第で併用推奨。 |
| **Chenkin Noob (最新)** | 版権キャラ追加、無印進化。 | 不安定、高速化LoRAで低下。 | WAIに戻る派多。 |
| **リアス** | CN細ポーズ優位、ファインモデル充実。 | 多人数崩壊。 | Anima素性能に劣後。「右手 vs オナホ」アナロジーでAnima長期推奨。 |
| **NAI** | - | アナルカンスト、多人数崩壊。 | サブスク継続/新モデル待ち。 |

- **移行意見**: SDXL（WAI）十分派 vs Anima実験派。Anima LoRA/CN充実で完全勝利見込み。

## ComfyUI/ツール関連・トラブルシューティング
ComfyUI上級者向けイメージ強。更新エラー多発。


| 項目 | 推奨/Tips | トラブル/解決 |
|------|-----------|--------------|
| **ComfyUI** | Coreノード中心で安定。WF共有（Anima XY Plot、Tile分割）。サンプラー: er_sde（背景綺麗）、euler a（安定母）。App ModeでVRAM60%減。Managerデフォルト化。 | アプデでmissing nodes/protobuf競合（transformers再インストール、extensions削除+venv tensorflowアンイストール）。v0.19.0確認多、安定版固定推奨。Hires.fixクラッシュ（Tile/電源確認、ページファイル有効化）。 |
| **Forge/Reforge Neo** | 赤ちゃん向け高速化。Stability Matrixから導入。 | Stability Matrixバグ（UV/インストール失敗、旧版再インストール）。 |
| **環境** | CUDA12.8/Python3.11/Torch2.7.1、VRAM12GB以上（fp8でLLM併用）。RAM128GBでMoE。Claudeでexe一発インストール。ドライバ595.79/596.02。 | VRAM開放（unloadノード）、熱暴走（ファン増設）。 |

- **新ツール**: 自作画像管理（Claude生成、多形式/タグフィルタ/WD14内蔵）。Scribble Reference LoRA（CN代替）。Calibratedノード（色くすみ解消）。

## LLM活用・プロンプトTips
Qwen3.5/Gemma4でAnima制御必須。

- **人気モデル**: Qwen3.5-35B-A3B-Uncensored（Q5）、Gemma4 26B A4B/Q4_K_M。ComfyUI-QwenVL/llama-cpp_vlmノード。
- **Tips**: シスプロ（Animaページ貼付+混合形式、masterpiece省略）。Thinking停止（`{%- set enable_thinking = false %}`）。画像→英文変換でCN代替。DeepL後修正。「状況詳述、容姿省け」。トークン切れ対策（系プロOFF）。
- **連携**: VRAM自動unload。コンテキスト長超え注意。

## LoRA/学習・生成Tips
- **Anima特化**: 自作可能（1024再学習、TE学習せず）。高解像度LoRA（Civitai、dim32、0.6強度）。Adetailer乳首LoRA。世界樹ニキ調整法（強度/ステップ総当り）。
- **エロTips**: ガニ股（standing+(bowlegged pose:1.5)）、twitching penis、panties around one leg自然出力。futanari不安定。SAM3性器検出（閾値0.06）。
- **Hires/アップスケ**: 1536OK、Tileノード（継ぎ目0.12デノイズ）。RealESRGAN_x4Plus注意。

## 動画/漫画生成
- **動画**: Wan2.2（実写寄り、目の崩れi2i+Anima修正）。LTX2.3 FLF（First-Last Frame、任意フレーム指定、FLUX無関係）。Seedance2.0/litVideo待ち。一貫性難。
- **漫画**: LLMプロンプト+Animaで4コマ/3コマ再現（起承転結、コマ割り指示）。ネーム鍵。ジャンプ+炎上事例（内部AI使用疑い）。

## 社会/ニュース・議論


| トピック | ハイライト |
|----------|------------|
| **規制/逮捕** | わいせつ物逮捕（生成AI小中学生模写、無修正販売）。モザ無しNG、非実在グレー。ロリ線引き難（実写風NG、二次OK派優勢）。スルー推奨。 |
| **マネタイズ** | Patreon/Booth締め付け厳、無修正海外優位。一枚絵売れず、エロゲ/動画推奨。専用スレ「AI画像生成マネタイズスレ ★268」。 |
| **手書きvsAI** | 手書き擁護（過程/ブランディング）vs AI結果主義。AI粗悪/画一化批判。萌えエロは過程無視されやすい。 |
| **その他** | 日本人GitHub弱/炎上商法批判。AI民主化（自作ツールブーム）。奈良AIアニメPR高評価（6本指指摘）。 |

## ユーザー傾向・推奨
- **中上級者**: Anima+LLM実験/WAI併用。WF/シスプロ共有活発。
- **初心者（赤ちゃん）**: Forge Neo/テンプレから。WF依頼/Claudeカスタム。
- **全体推奨**:
  - **Anima入門**: Qwen3.5シスプロ+高解像度LoRA（Civitai即DL）。
  - **安定**: WAI v16+LoRA。
  - **トラブル**: エラーAI投下/スレ相談。
  - **スペック**: VRAM12-16GB、電源確認。

## 結論・洞察
Animaの自然言語/CN/高解像度進化でSDXL（WAI）超え加速中。コミュニティのTips共有（LoRA/WF/LLM）が強みで、エコシステム拡大。規制圧力/価値論争あるが技術志向優勢。次スレ注目: Anima正式版/CN対応、ComfyUI v0.20、高解像度検証。なんJらしい実践・エロ特化スレで、生成効率向上の好例。詳細は原ログ参照。
