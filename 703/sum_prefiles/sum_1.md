# なんJ AIスレ レポート

## 1. モデル・環境
- **Strata**浸透中。LM Studioより高速（193）。OpenAI/Claude Code API互換サーバーで、ComfyUIカスタムノードやBionic、Unslothで動作（81, 90）。標準UIは体験版扱いで、本格利用にはハーネス推奨（202）。
- **ハーネス**とはAgent環境の総称。「Hermes Desktop」や「DeepSeek Harness」「Codex」「Claude Code」など複数存在し、単一のソフト名ではない（210, 214, 215）。Hermes Desktopは全部入りでWindowsネイティブ版があり初心者向け、Open WebUIは環境構築が面倒（203）。
- RAM 192GB環境でUD-Q4_K_XLを試すも規制解除不可・画像読み込み不可で削除（150）。Qwen3.8 flash nextはモデルの一部をSSDに置けるためStrataと相性が良い（211）。

## 2. 動画生成
- MiniMax H3 Max R2Vはほぼリアルタイム生成。Eleven V4 TTSと組み合わせリップシンク動画作成例あり（72）。
- 長尺動画向けにHR-Endless-Sampler、H3-Longvideo、MiniMax H3 Latent Relayなど存在。Context LoopよりLatent Relayの方が綺麗（147, 173）。
- MiniMaxで触手LoRAテスト。ref2va 14組28枚で作成したが結合部の描画が壊滅し改善中（189）。
- 5.5opus登場後、動画生成を使わない動画の作成例が増加（20）。

## 3. 画像生成
- **Krea2**でAVコマ再現やCodexと組み合わせたプロンプト作成が可能（44, 99）。パンツを穿かせると股間がモッコリする事象が発生（135）。
- **Anima**はLoRAが作りやすくVRAM4GB環境でも可能だが、絵柄混ぜが難航中（184, 191）。背景実写＋イラスト系キャラの作例あり（20）。
- **NAI5**はクオリティ高く文章まで生成（59）。**Qwen Image2.1**のi2iで実写ヌード変換が可能（180）。

## 4. 制限・コスト
- Antigravity上のOpus 5.5 Highを5回試すと週間枠50%消費・5時間待ち制限発生（42, 67）。
- Claude 5系はトークン消費が激しくサードパーティ利用は不向き（70）。
- Gemini無料枠がFlash Liteのみになる改悪。月725円ではPROモデル使えず（129, 133）。
- Astraは激高＋高速で利用枠が秒で溶けるため常用注意（162）。

## 5. セキュリティ・エージェント挙動
- CodexやClaude Codeがワークスペース外のデータを勝手にチェック・読み書きする報告。児童虐待コンテンツ関与を検出して開発拒否された事例あり（82, 91, 93）。
- Strata君が気を抜くと「お前」呼び・一人称「俺」になる（123）。Claudeが猛虎弁になる事例も（219）。

## 6. ハードウェア
- 動画・アプスケ・エンコにはVRAM 24GB・RAM 64GBでも不足しスワップやエラー多発（169）。
- RTX 3080（Strata用）＋RTX 5080（画像生成用）の2GPU構成・RAM 128GBで運用（199）。
- RAM 32GB環境ではMiniMax等が動かず増設検討中（188）。4070ti 12GB＋RAM 96GBでMMH3・Strata動作確認（206）。60xx待ち・Pro 7000狙いの声あり（34, 35）。