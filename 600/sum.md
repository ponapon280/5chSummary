# なんJ AI生成スレッド（なんJNVA部）総合レポート（投稿239-998 + 600スレ記念）

## 概要
なんJ板のAI生成スレッド（Stable Diffusion系ツール中心、ComfyUI/Wan2.2/Z-Image Turbo (ZIT)/Illustrious/wai※など）のログを5パート（239-998 + 600スレ記念）から統合要約。総レス数約1,000超。主なトピックはZITブーム（Base公開待ち）、ComfyUIトラブル/UI不満、NSFW生成Tips（エロ構図/LoRA）、GPU/RAM高騰、動画生成最適化。参加者はRTX3090/4080/50シリーズユーザー中心で、初心者質問から上級者Tips共有まで活発。実践互助文化強く、トラブル即解決・WF/画像共有多め。エロ特化（手マン/膜/プッシーなど）前提の口語体議論で、なんJらしい自虐/煽り混在。次スレ（★601）でZIT Base/LoRAエロチューン期待。

※wai: Illustrious派生モデル（wanvideo無関係）。

## 主要ニュース・アップデート
- **Z-Image Turbo (ZIT)**:
  - トレーニングアダプターv2公開（v1の2倍サイズ、LoRA互換向上）。実写/人物/アニメ/文字/コントロールネット優秀（有名人/逆立ち/漫画優位）。100万DL突破、Base/EditモデルScope公式Xで近日オープンソース（中国HF版）。
  - EasyImageEdit対応（アップスケール/プロンプト強化）。LoRA作成安定（zuntanニキ活躍、エロチューン待ち）。VRAM低負荷（12-16GB可、3060対応）。
  - 評価: 高速（3-9step/8秒）、プロンプト忠実もイラスト幅狭/貧乳/城固定弱点（ノイズ除去0.95/SeedVarianceで改善）。QIE2511互換/Qwen連携で自然言語→タグ変換強化。

- **その他モデル/ツール**:


  | モデル/ツール | ポイント |
  |---------------|----------|
  | Wan2.2/Illustrious/wai/Noob | エロ安定/プニプニ質感。獣姦LoRA/エミリア動画試行（プッシー開き/膜不安定）。EasyWan22/EasyReforge高速化。 |
  | HunyuanVideo-1.5 | VRAM14GB動作、Training code近日。 |
  | Qwen3-VL-8B-NSFW-Caption-V4.5 | エロ画像解析神（日本語推奨、LM Studio/GGUF連携高速）。Q6_K量子化バランス良（VRAM12GB）。 |
  | MiaoMiao RealSkin v1.1 | 髪グラデ良も異方性反射不足、Wan移行テスト。 |
  | painterLongVideo/kijai WF | 動画一貫性高（顔溶けにくい、パーティクル優秀）。 |
  | Genspark/raylight | FLUX2 Pro/ZIT対応、GPU2枚分散未検証。 |

- **ComfyUIアップデート**: 0.3.75/Frontend1.30.6/1.33.1で高速化もUI改悪（中断ボタン削除/進行オーバーレイ/ジョブキュー浮遊）。回避: frontendダウングレード/ショートカット（Ctrl+Alt+Enter）/新メニュー無効化。Rキー再読み込み/×ボタン復活。

## ハードウェア事情
- **GPU**: RTX3090/4080定番→5090/5060Ti16GB/5070Ti買い替えラッシュ（1.6倍速、電源1200W/BTO推奨、40-45万）。AMD（RX6800）遅れ不満。ドライバ566.36/581.x（CUDA13）。
- **RAM/VRAM高騰**: DDR5 64-128GB必須（AI特需/円安/Crucial撤退）。2-3倍騰騰、在庫確保連呼。TiledVAE/OOM対策（バッチ1/--fp32-vae）。
- **消費電力**: アイドル100W/生成250W。MultiGPU fix共有。

## トラブルシューティング


| 問題 | 解決策 | 頻度 |
|------|--------|------|
| ComfyUI UI改悪（中断ボタン削除/ノードエラー） | frontend1.30.6ダウングレード/新メニュー無効/再インストール/custom_nodes削除→git clone。 | 高 |
| カスタムノード（Impact-Subpack/ZIT/rgthree）赤エラー | requirements.txt手動/Manager Install missing/Nightly→ベータ。 | 高 |
| EasyImageEdit/WF壊れ（ファイル見つからず/コピペ不能） | Windowsファイル名制限解除/Tritonキャッシュ削除/パイパス+AnySwitch。 | 中 |
| VRAM OOM/生成カクガク | TiledVAE有効/バッチ1/Clean VRAM/gguf量子化（Q6/Q8）。 | 高 |
| LoRA身体崩れ（乳3個/腕欠/竿カラカラ） | 1キャラ厳選/全身満足画像/buckets OFF/Regional Prompter。 | 中 |
| プロンプト末尾カンマ削除/Seed変動 | AutoComplete設定変更/Wildcard seed固定。 | 低 |
| 高解像度ジャギー | Rife非対応→PainterI2V/LongVideo。 | 低 |

- GPT不信: エラー時はログ/チャッピー共有推奨。

## 生成Tips・モデル評価
- **エロ構図プロンプト**:


  | 構図 | 推奨タグ（ネガ例） |
  |------|---------------------|
  | 壁手ついて後ろからpussy広げ | `1girl,1boy,from behind,(spread pussy:1.2),ass focus,bent over,against wall` ネガ: licking。 |
  | 手マン（下向き） | `fingering`（上向き注意）+尻出し。 |
  | 引き/遠景 | `wide shot, distance view`。 |
  | 強制フェラ/オーガズム後ガン突き | POVPENIS/男配置/POVPENIS。onee-shota: `mounting, size difference`。 |
  | 子宮口/アナル断面/膜 | FaceDetailer/LoRA蒸留/Qwenキャプション。 |

- **手法**: デッサン人形→プロンプトガチャ vs MMD/Unity→v2v（Quickmagic70点）。LLM（Gemini/Grok）でプロンプト生成/ロールプレイ。サンプラー: **Euler a鉄板**（早安定、母なるサンプラー）。Step18/CFGpp/bf16。
- **評価**:


  | モデル | 強み | 弱み |
  |--------|------|------|
  | ZIT | 高速/精度/低VRAM/LoRA実用 | イラスト狭/貧乳/固定構図 |
  | Wan2.2/Illustrious | エロ安定/質感 | WF壊れ/膜不安定 |
  | Noob/wai | 愛用多 | - |

## コミュニティトレンド・その他
- **ローカル vs クラウド**: ローカル（NSFW自由、低スペZIT歓迎）vs クラウド（NAI/Grok高速も規制厳、月3-7k）。ハイブリッド推奨。
- **市場/未来**: GPU枯渇/AI戦争（中国無料公開）。ZIT Base/QIE2511/Sora2待ち。Civitai不具合（DLバグ/成人非表示）。
- **雑談**: オカズ画像貼り/ヤベーニキ/入院生成禁断症状。他板（エッジ/ふたば）移行論。
- **経済懸念**: メモリ/SSD高騰で低スペ最適化加速。

## 総括
ZITブームでSDXL後継候補化、ComfyUI依存高まるもUI/ハード課題多し。NSFW実践Tips豊富で初心者歓迎文化。トラブル共有即解決が強み。詳細ログ/WFは元スレ参照。次スレでBase公開/RTX50実機/動画深化期待。質問時はエラーログ共有を。