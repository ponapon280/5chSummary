# なんJ(5ch) AI生成スレッド ログレポート (243-443)

## 1. スレッド概要
- **期間/範囲**: 243レスから443レスまでの会話ログ。
- **主なテーマ**: ComfyUIを中心としたAI画像/動画生成のTips共有、トラブルシューティング、モデル/LoRA/ワークフロー(WF)の議論。Anima Preview2、DMD2、Spectrumなどの高速生成ツールがホットトピック。初心者のComfyUI学習難易度、GPU選択、A1111系(Forge/Neo)との比較も頻出。動画生成(Wan2.2関連)、LoRA学習、LLM(Qwen3.5)活用も散見。
- **参加者傾向**: ComfyUI上級者による初心者支援多め。RTX3060/4090/5090民中心だが、低スペックユーザーも。移行組( EasyWan/Forge → ComfyUI)の苦労話が目立つ。
- **全体トーン**: 実践的・共有志向。「サンガツ」(ありがとう)が多用。初心者いじりありつつ、親切な回答多数。

## 2. 主要トピックと議論ポイント

### 2.1 ComfyUIノード/WF/トラブルシューティング
- **スペース/コメントアウト/wildcard問題** (243-245,247-249,252,268-269,284):
  - プロンプトのスペース有無で出力変化(クオリティ低下)。ImpactWildcardProcessor + Multiline → CLIPでコメントアウト(// or #)対応。
  - 解決策: Regex Replaceノードで`/\*[\s\S]*?\*/|//.*`置換。hide_commentsオンで後段除去。
  - WebUIではデフォで機能するがComfyUIはノード挿入必須。
- **高速化ツールの相性** (246,251,258-259,264-265,280,309,316):
  - Anima Preview2 + DMD2: 出力好み化、Spectrumより速い。高速化LoRA(発色単調化副作用)。
  - Spectrum + DMD2: 相性最悪(予測ステップ短縮が干渉)。4-8step推奨。
  - クオリティタグのカンマ後スペース削除で低クオリティ検証。
- **モデル分割/SDXL対応** (253,257,270,272,277):
  - SDXLのUNET/CLIP/VAE分割: HuggingFaceのJSON使用(高度な機能→モデルマージ)。
  - sdxl-workflow.json共有(標準ノード化)。
- **初心者学習難易度** (310,314,335,354,393-406,409,414-419):
  - EasyWan卒業難: WF複雑、エラー多発。gguf/safetensors混在でモザイク。
  - アドバイス: 公式テンプレ(Anima検索)から開始。サンプルWFドラッグ&ドロップ。45回環境破壊推奨(慣れ重視)。
  - ComfyUI vs A1111: ビジュアル難解 vs 親しみやすい。StabilityMatrix/Portable運用OK。
- **アップデート/エラー** (262,278,289-290,304):
  - サブグラフ不具合残存。Forge NeoでSpectrum拡張対応。

### 2.2 モデル/LoRA共有とTips
- **Anima関連** (246,251,273-276,299,343,345,347,408-410):
  - Preview2 + cottonanima_prevew2善し。画風LoRA強化。日本語崩れ軽減(8step LCM)。
  - 複数キャラ: 自然言語特徴記述必須(混じりやすい)。
- **LoRA学習** (266-267,271,291,350,358):
  - 繰り返し回数: 基本1でOK(正則化不要)。フォルダ名影響なし。クオリティ低下時は他要素確認。
- **Wan2.2動画** (324,360-361,371-375,384-387):
  - smoothmixV2: step20+Light2xv LoRA(High3.0/Low1.5)。ggufよりsafetensors速い。Low=dasiwa推奨。
  - 遅延原因: バックグラウンドVRAM食い/PC再起動。
- **その他** (336,369-370,380,437):
  - SD1.5 Canny → SDXL配置制御。
  - 実写アプスケ: UltimateSDupscale/Hires.fix(ディテールマシマシ)。SeedVR2は補完寄り。

### 2.3 GPU/ハードウェア議論
- **Intel Arc B580** (279,292,295-296,318,321,348):
  - 画像生成コスパ高(5060ti上)。動画不可。B65/B70(32GB)来週予定。
- **Radeon RX9060XT/9070XT** (300,302,318,322):
  - ROCm高速化で魅力。白/三連ファン/5万以内難。
- **RTX5090/LLM** (293-294,308,311):
  - Qwen3.5: 27B Q6(24Kコンテキスト)/35B Q4_K_M(24GB、NSFW善)。
- **その他** (306,320,339):
  - Mac Mini M5待機推奨(LLM高速)。

### 2.4 動画/モザイク/その他Tips
- **モザイク** (366,386): PointsEditorで検出→自動処理。
- **服変更** (442): Wan2.2 i2vで可能(フリッカー注意)。
- **版権再現** (443): NovelAI v3優位。ローカル(SD/Anima)は進化止まり気味。

## 3. 共有リソース
| カテゴリ | 内容 | 参照 |
|----------|------|------|
| WF/JSON | SDXL分割チェックポイント: https://huggingface.co/asfdrwe/wai16DMD2/blob/main/%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%83%A2%E3%83%87%E3%83%AB%E5%88%86%E5%89%B2.json<br>sdxl-workflow.json: https://huggingface.co/asfdrwe/wai16DMD2/blob/main/sdxl-workflow.json | 253,257 |
| モデル | DMD2, cottonanima_prevew2, Light2xv LoRA | 273,275,384 |
| GPUベンチ | やかもちGPU比較 | 295 |
| その他 | Regex: `/\*[\s\S]*?\*/|//.*` (コメント除去) | 284 |

## 4. トレンドと示唆
- **人気ツール**: Anima Preview2 + DMD2/Spectrum(高速化)。ComfyUI移行加速中だが、初心者離脱多め(A1111/Forge残留派)。
- **課題**: WF視認性/ノード多さ。エージェントAI期待声あり。
- **未来志向**: LLM連携(Qwen3.5-VL/Caption特化)、Radeon/Arc低価格GPU台頭。Animaサイズ拡大でSDXL民足切り懸念。
- **コミュニティ強み**: 即時Tips共有。初心者「サンガツ」多発で活発。

このレポートはログのエッセンスを抽出。詳細相談時は特定レス参照を推奨。