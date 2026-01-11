### 抽出された「ツール」に関する話題一覧

ログから生成AI関連の**ツール**（ComfyUI, A1111, webUI, SUPIR, nano-banana などのノード/WF/拡張ツール、カスタムノード、TTSツールなど）を抽出。**モデル**（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen などリスト指定の画像生成AIモデル、LoRA含む）は一切抽出対象外。ツール選定理由が明記されている場合のみ記載。ログ番号順に整理。

#### 427
- **LTX2**（公式T2VのW、gemmaシステムプロンプト加えるノード）：tensorがGPU/CPUに分かれるエラー発生。対応策議論。

#### 429, 433, 435
- **set/get/subGraph**（ComfyUIノード）：自分でWF作れる人は使わなくてよい。スパゲティWF討伐したくなるが、自分のものは可愛い。

#### 436
- **SAM3**（ComfyUI系？）：SDXL画像でpersonマスク、Mask Invert反転、Detailer処理でInpaint Crop使用（denoise 0.5）。res_multistep強めで文字出力成功しやすい。

#### 439
- **ComfyUI**（最新版、公式テンプレ）：LTX2公式WFではなく使用推奨。**理由**：Enhancerなしで動作し、早い。
- **ZimageEnhancer**：Enhancer処理でVRAM消費エグい、デフォルト外部無料API使用。

#### 441
- **ComfyUI公式WF**：LTX2公式WF代替。**理由**：LM Studio的な処理でCPUになるのを避け、5090前提のLTX2公式より良い。

#### 442
- **バイパス**（ノード？）：プロンプト拡張代替として使用。

#### 443, 478
- **メタデータ/tagger**（ComfyUI機能）：性癖解析、danbooru語履修、WF確認に使用。taggerで画像解析推奨。

#### 444
- **PromptToPromptのEnhancer**：次世代標準実装ノリ。Danbooruタグ対応エロチューン版希望。

#### 447
- **LM Studio**：VRAM12GBでQwen-Image bf16プロンプト生成可能。WFがおかしい可能性指摘。

#### 461
- **smZnode**：LTX2現役フローで使用、移行めんどくさい。
- **VAEdecodeノード**：コイル鳴きエラー。

#### 463
- **エンハンサー**（LTX2）：フル性能で32GB最低/A100 80GB推奨。プロンプト修正コスト重い。

#### 465, 477, 490-492
- **VHS_SelectFilename**：NoneTypeエラー原因（動画保存設定不備、フォルダ指定ミス）。
- **WanlmageToVideoSVIPro**（サブグラフ）：カスタムノード未インストールエラー。
- **comfyUI-kjnodes**（カスタムノード）：バージョン問題（switch ver.disable/Uninstall注意）。sageattention/flashattention未導入でコケる。**ComfyUI本体最新推奨**。

#### 484
- **ComfyUI-SAM3 vs ComfyUI-Easy-Sam3**：Easy版優位。**理由**：検出圧倒的に早くVRAM消費少なく、ポイントエディターUndo可。

#### 487-488, 495, 499-501, 504, 519
- **SVI (Stable Video diffusion Infinity)**：WF調整難、anchor_samples差し替えで1st再開（ガチャ時間かかる）。LoRA設定ミスで謎タイル。kijaiのLoRAダウソ注意。海外勢WFはblockswapノード/中国語混在で複雑。**blockswapノード**：海外WFに含まれる。

#### 490, 493
- **gemma3 prompt enhancer**：Googleリポジトリclone/認証必要。

#### 504
- **blockswapノード**（SVI海外WF）：使用でウボァー。

#### 511-515
- **Kling**（オープンソース動画モデル、hunyuan videoベース）：モーショントラック優秀、RTX3060未対応？ ComfyUI未対応（最適化期待）。**量子化でワンチャン**。

#### 517
- **seedVR2**：QI2512画像アプスケで本物と見分けつかず。

#### 525
- **easywan2.2 Workflow**：重すぎ（PC貧弱？）。

#### 526, 565
- **Style-Bert-VITS2**（TTS）：一強？ RTX5060tiでGPU認識せずCPU動作。**理由**：ナレーション/実写向き（学習必要）、CUDA使用で高速（GPU用bat必須）。

#### 528
- **インペイントWF**：更新でサクラダファミリア化。

#### 530, 566, 576, 579
- **T5Gemma-TTS**（フォーク版T5Gemma-TTS-2b-2b, gradio）：イラスト感情表現/そっくり声（5秒参照）。**理由**：品質高、日本語誤読多（ふりがな対応）、VRAM16GBで2B限界。llasa比較あり。

#### 533
- **翻訳ノード**：日本語→英語変換、Facebook翻訳AI（3.6GBオフライン）便利。

#### 564
- **アプスケ**（LTX-2）：既存動画音付け試すも失敗。

#### 571, 575-576
- **InfiniteTalkノード**（Wanベースリップシンク）：s2v系。T5Gemma-TTS+XCodec2 (Anime-XCodec2-44.1kHz-v2)と組み合わせローカルイニD再現。

#### 573
- **comfyui用のノード**：視覚的に分かりやすい。

#### 581
- **nano-banana**（Pro）：Google AI Proで無制限、文字入れ強すぎ。

#### 589
- **Google AI Pro**：banana pro/sora2使用可（課金後）。

#### 594, 602
- **higgsfield**：multipie angles GUI操作、30MBマルチアングル画像生成。

#### 626
- **smoothMIX**（low）：暴れるのでdasiwaに変える推奨。

### 補足
- **ComfyUI全体**：最新版/公式WF/カスタムノード（kjnodes, SAM3系など）頻出。メタデータ/tagger/翻訳ノード/subGraphなどノード群が基盤。
- LTX2/SVIはWF/ツール群として複数エラー/代替議論（ComfyUI公式優位）。
- TTSツール（Style-Bert-VITS2, T5Gemma-TTS）はローカル音声生成で詳細理由記載。
- 理由抽出は明記分のみ（例: VRAM効率、速度、Undo、GPU対応）。
- モデル/LoRA/hard話題（Wan, Qwen, 5090など）はスキップ。無関係ストーリー（479-482）も除外。