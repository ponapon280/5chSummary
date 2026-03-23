### 抽出された「ツール」に関する話題

ログ（4〜242）から、生成AI関連の「ツール」（ComfyUI, WebUI, forge neo, Spectrum, Greenboost, WaveSpeed, smZNodes, pinokio, Unsloth Studio, LM Studio, impact wildcard processor, comfyui-adaptiveprompts などインターフェース、カスタムノード、高速化ツール、拡張機能）に関する話題をすべて抽出。モデル（anima, Wan/wan2.2, Z-Image Turbo など指定リストのもの）関連は除外。ツールが選ばれている理由（速度向上、一貫性向上、互換性、使いやすさなど）が明記されているものは強調して記載。引用形式でレス番号順にまとめ。

#### 18
- **forge neoのSpectrum Integrated**: 生成速度が嘘みたいに早くなる（理由: 高速化）。

#### 37
- **Greenboost**: KVキャッシュ周りで認識にズレが生じる原因がわかった（ドキュメントの嘘指摘、VRAM不足時のRAM/SSD確保は実装済みだがAllocation Flagsがデタラメ）。作者のFerran Duarri氏批判。

#### 53, 54, 77, 78, 80, 82, 85, 106, 121, 159
- **ComfyUI と WebUI (A1111系)**:
  - 53: ComfyUIに手を出したはいいがWebUIで作った画像を複製できなかった。
  - 54: 複製なんてできない。
  - 77: WebUI生成画像をComfyUIにドラッグ&ドロップで基本ワークフロー再現可能。全く同じ画像にはカスタムノード必要。
  - 78: WebUIとComfyUIで全く同じ画像ができない理由（シード値の違い？）。
  - 80: 仕組みが違うから同じ結果にできない。
  - 82: A1111コンパチじゃないと出せない味（ComfyUIでサンプラー/VAE/CFGスケールなどをA1111同等にしてもComfyUIのがくすむ、無数のプラグイン関係？）。
  - 85: A1111系WebUIとComfyUIの生成画像の違い記事リンク。
  - 106: ComfyUIバージョンアップで出力が変わる。
  - 121: WebUI生成画像をComfyUIにドラッグ&ドロップしても精細さに欠ける（txt2img→Hires.fixの脳死再現難）。
  - 159: ComfyUIでA1111と同じ画像を作る方法【smZNodes】（LTX-2と相性悪くエラー注意）。

#### 90, 95
- **ComfyUI**: comfyのanimaで色が薄味/くすむ（SDXLならVAE替えで解決）。メタデータ入り画像をcatbox.moe/imgbb.comに上げて検証推奨。

#### 102
- **ComfyUI**: BREAK/強調の対応はcomfy側かモデルか不明。

#### 117〜119, 123, 129, 130, 134, 138, 139, 140, 150, 153, 155, 164〜166, 169, 171, 193, 205, 211
- **Spectrum (ComfyUIカスタムノード、高速化ツール)**:
  - 117: comfyuiでSpectrum使いたいカスタムノード？
  - 118: 前スレ595ニキのもの。easy cache/Spectrum使わず（速いが画質/色合い犠牲？）、sage attention/torch compileのみ（理由: 最適設定不明）。
  - 119: 高速化はおまけ、メインはLayer Replay Patcherでディテール/一貫性アップ。
  - 123: 色合い薄くなるが場合によってはプラス。
  - 129: 記事まとめ。色褪せあるがSeed一貫性でガチャ後無効再生成可能（ステップ削減系との違い: 理由）。
  - 130: スケジュール/交互構文使えなくなる難点。
  - 134: 色褪せソフト、生成速度3割加速のデメリット軽い。
  - 138: Lightningと違い出力変化少なく良い。
  - 139: 大型モデルで効きそう、動画向き。
  - 140: 原理的に動画効く、wan2.2微妙。
  - 150: 色褪せ気になるなら後で外せ（知見）。効果驚異的、ゲームエンド大賞級。
  - 153: lightx使わずstep多めで同等高速化可能なら良い。
  - 155: dmd2より優位（CFG1でネガ死/絵柄変化避けられず）。
  - 164: SDXL用Spectrum二種類（前スレ/マネージャー導入）。
  - 165: >>129比較でProper方が良い。
  - 166: 高性能グラボ向け（始め5stepキツくミドル以下不向き）。
  - 169: Proper方が良い感じ。
  - 171: SDXLでKsampler爆速（Detailer速度変わらず）。WaveSpeedと組み合わせてえげつない。
  - 193: animaで速さ変わらず（他原因？）。
  - 205: 3060計測: 元49.55s → Spectrum43.31s → wavespeed40.11s → 両方36.80s（顔変わるのでwavespeedだけ？）。ノード繋ぎ方画像。
  - 211: デフォfalseのまま？ trueにせよ。

#### 133
- **ComfyUI公式**: 更新しまくり破壊的変更でやってらんない。

#### 161
- **ComfyUIマネージャー**: 使ってないカスタムノードはDisable。

#### 178, 195, 207
- **ComfyUIワークフロー (WF)**: LTX extendにlast frame追加うまくいかず（v2vのみ？ i2vでサウンド連続性途切れ）。WF開くと不足ノード案内（読み込めない場合あり）。

#### 205
- **WaveSpeed**: Detailerに繋いで速度向上（Spectrumと併用）。

#### 216, 218, 226, 227, 230, 233, 238
- **Unsloth Studio**: WebUIとしてスジ良さげ（NVIDIA公式紹介、画像/LLM/音声生成全部）。導入直感的じゃない（LM Studioがお手軽）。自分で動かして驚き具体的に（理由: Nvidia公式推し）。

#### 224, 232
- **forge neo/chan**: forge neoでanima動く？ Python 3.13以上必須。

#### 240〜242
- **ComfyUIワイルドカード/コメントアウトノード**: __wildcard__対応、//コメント。impact wildcard processorあかん？ → impactwildcardprocessorで#コメント可。comfyui-adaptiveprompts（##挟み、LoRA不可なのでimpact wildcard encoder下接続）。

#### 247 (ログ外だが242まで)
- 該当なし。

その他ツール言及（pinokio: 147ワンクリックインストールだがフォーク放置多し、Visual Studio: 229処理速度のためネイティブ必要？）はマイナー/文脈薄く詳細抽出省略。LTX-2.3/InfiniteTalk/Grokなどは動画ツールだがモデル寄り/リスト外のため一部スキップ（ツール明確時のみ）。Qwen関連なし。