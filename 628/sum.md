# 🆕 新規トピック（前回からの差分）
- Irodori-TTSフォークの実用性向上（絵文字/感情自動）
- Smooth Workflow Wan 2.2 v3.0（動画ボヤ未解決）
- リアル系シフト（Qwen/Z-Image）
- コミュニティ強みと課題（ローカルNSFW自由、ソース要求ループ、VRAM16GB前提）

---
# 元の本文
# なんJ AI画像生成スレッド（なんJNVA部）統合ログレポート

## 1. スレッド全体概要
- **対象ログ範囲**: レス9〜1000（約1000レス）。主にStable Diffusion（SD）関連のAI画像/動画生成ツール（ComfyUI、Forge Neo、Anima、Stability Matrixなど）のローカル運用、トラブルシューティング、モデル/LoRA学習、NSFW生成Tipsが中心。
- **後半シフト**: 中盤以降、5ch.netドメイン喪失事件（動物虐待コンテンツ原因の永久BAN）が急展開。代替ドメイン移行、専ブラ対応、ロリ禁止・ゾーニング論争がAI議論を圧倒。
- **参加者傾向**: AI生成愛好家（ローカルNSFW志向強め）、技術者・ホビイスト中心。互助Tips活発だが、初心者質問無視傾向。ユーモア（リボンパンツ陰謀、オバマネタ、bot疑惑）と愚痴（更新不安定、パーツ高騰）が特徴。
- **全体トーン**: 前半は技術共有と不満ミックス（ComfyUI不安定最大）。後半はパニック→落ち着き→メタ議論（存続危機）。オープンソース人材流出（Qwen/SD離脱）で悲観論も。
- **生成日時**: ログベース（2024年頃推定）。最新情報はCivitai/公式確認を。

## 2. 主要トピックと議論ハイライト

### 2.1 AIツール/UI比較・トラブルシューティング（最多話題）
ComfyUIの不安定さが全編不満源。Forge Neo/Stability Matrixの安定推奨多。


| UI/ツール | 推奨ポイント | 問題点・解決策 |
|-----------|-------------|---------------|
| **ComfyUI** | 動画/高度生成向き。SAM3（Hand検出: `v hand,` + Denoising調整）、LoRA Manager、aimdo（VRAM削減）。アップデート（v0.15.1〜0.16.3）でDynamic VRAM有効化。 | 更新バグ多（Qwen遅延、Frontend WebP非対応→PNG推奨、cu128廃止）。解決: `--disable-dynamic-vram`、Frontendロールバック、git pull確認。カスタムノード互換性なし。 |
| **Forge Neo** | Anima/SAM3対応、LoRA管理楽。Stability Matrixで独立インストール。 | 初回真っ黒（Schedule手動/Anima Preset指定）、NegPiP弱、Python3.13必要。Generate Forever停止（Chromeスリープ対策）。 |
| **Anima** | LoRA学習自然言語キャプション可、Qwen3.5-9Bタグ変換。hires.fix相当（出力→SDXL i2i）。 | i2i弱、1536解像度顔崩れ（wai14推奨）、作者遅延クレーム、商用不可。絵師タグ不安定。 |
| **Stability Matrix** | 独立環境管理（Git/Python個別）。 | 初回エラー（Patron誤読）。 |
| **その他** | EasyReforge（移行注意）、Irodori-TTSフォーク（LM Studio連携、感情推定、300-4000ステップ学習）。SageAttention（1.9倍速）、LTX2.3（RAM128GB推奨、日本語弱）。 | TTS失敗: early stopping調整、Whisper middle注意。 |

- **移行Tips**: EasyWan→標準WFでComfy学習。WF JSONをChatGPT解析。
- **ハードウェア**: PCパーツ高騰（SSD2TB+4万、5090 PC76万）。Dynamic VRAM活用推奨。

### 2.2 モデル/LoRA/生成Tips（NSFW中心）
- **推奨モデル**: Wan2.2（マージでNSFW制御）、リアスv3.6（1536解像度）、WAI-REALISM-Illustrious（NSFW中国美人、waiはIllustrious派生・wanvideo無関係）、Z-ImageTurbo（高速）、Qwen-Image-2512、SDXL三次、Animayume実写エロ。
- **LoRA/TTS**: 横ハミ毛、卵産み付け有効。TTS: 204件データ不安定、LR低め/Num Candidates追加。JoyTag/Florence-2キャプション楽。
- **プロンプト最適化**:


  | 問題タグ | 解決策 |
  |----------|--------|
  | リボンパンツ汚染 | bow pantiesネガ。 |
  | futon（布団） | 畳誤変換→LLM学習不足。 |
  | squat_toilet | 出にくい日本タグ。 |
  | pubic hair | ふわ/硬め使い分け。 |
  | hair tie色指定 | brown hair with hair tie that is yellow color:1.2。 |
  | 表情 | expressionless/embarrassed/shy/humiliation（エロ向上）。 |

- **NSFW妨害回避**: マージモデル、検閲解除モデル。hires.fix: Pixel upscale（ESRGAN bilinear安定）。

### 2.3 ニュース・メタ議論
- **Qwen/SD離脱**: Qwen3.5直後チーム離脱（Alibaba内部事情）。オープンソース冬の懸念→クラウドシフト警戒。
- **AIツール活用批判**: Gemini/ChatGPT誤読多（Python=Patron）。Grok4.2推奨。
- **著作権/投稿**: AI作者不認可。Pixiv（版権エロ30枚推奨）vs X（PV水増し注意）。

### 2.4 5chドメイン喪失事件（後半最大トピック）
- **原因**: 動物虐待コンテンツ（生き物苦手板）でEpik永久BAN（クレカ圧力）。5ch.net全板不能（サーバー/IP無事）。
- **代替対応**:


  | ドメイン | 状況 |
  |----------|------|
  | 5ch.io | 主力移行（siki/Chmate対応）。 |
  | 5ch.one | 一部エラー。 |
  | bbspink.com | 死亡（LLM/オナテク板難民）。 |

- **専ブラ進捗**: Siki 0.40.0、Chmate 0.8.10、Gescharベータ対応。hosts/DNS編集推奨。
- **懸念**: エロ/R18/ロリ火種。ぷにぷに/Telegram避難提案。

### 2.5 ロリ禁止・ゾーニング論争（終盤激化）
- **賛成（25%）**: 存続のためテンプレ改正（18歳以上/ソフトエロ限定）。bbspink再発防止。
- **反対（40%）**: なんでもあり文化崩壊。別スレ移住で無意味。
- **中立**: モザイク/NG活用。pixiv/reddit避難。
- **結果**: 次スレ（★629）立てで一旦リセット。分裂リスク。

## 3. 問題解決・Tipsまとめ
- **Comfy真っ黒**: Anima Preset + モデル/VAE指定。
- **SAM3 Hand無効**: `v hand,` + Denoising up。
- **TTS失敗**: ステップ調整/Loss分析。
- **初心者**: 環境/出力明記。LLMでプロンプト設計。
- **パフォーマンス**: SageAttention 1.9倍、RTX4090 SDXL 34秒基準。

## 4. 注目新情報・トレンド
- **Irodori-TTSフォーク**: 実用高（絵文字/感情自動）。
- **Smooth Workflow Wan 2.2 v3.0**: 動画ボヤ未解決。
- **リアル系シフト**: Qwen/Z-Image。
- **コミュニティ強み**: ローカルNSFW自由。課題: ソース要求ループ、VRAM16GB前提。

## 5. 結論と示唆
スレはComfyUI不安定を嘆きつつ、Forge Neo/Animaで解決余地大の「戦場報告書」。後半5ch危機でAI議論一時後退も、技術共有の粘り強さ目立つ。オープンソース人材流出・規制強化で有料/クラウド懸念増すが、NSFWコミュニティの創造性高い。次スレ期待: Anima正式版、Qwen後継、ゾーニング安定化。ログから「無料ローカル>制約」を重視。5ch存続のため自主規制推奨。追加ログで更新を。
