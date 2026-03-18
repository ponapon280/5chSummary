# なんJ(5ch) AI生成スレッド レポート (ログ: 650-850)

## 1. スレッド概要
- **期間/範囲**: 投稿650〜850（約200レス）。主にAI画像・動画生成ツール（ComfyUI, Anima, SDXL, LTX2.3, Wanなど）の活用・トラブルシュート、ハードウェア最適化、生成品質向上策が中心。
- **参加者傾向**: ローカル環境ユーザー（RTX40x0/50x0シリーズ中心）。サンガツ氏（Anima開発者？）の積極的な更新報告とユーザー支援が目立つ。なんJらしい雑談（エロネタ、ハードウェア愚痴、宮崎駿ネタ）混在。
- **全体雰囲気**: 技術共有活発。高速化ノード（Spectrum）の発見・調整ブーム。Anima/ComfyUI移行推進、動画モデル（LTX/Wan）への関心高まる。初心者向けアドバイス（Stability Matrix推奨）も多い。

## 2. 主要トピック別まとめ

### 2.1 画像生成ツール・ワークフロー（Anima, ComfyUI, SDXL）
- **Animaパイプラインの活用**:
  - LLM（Qwen3.5など）でプロンプト生成→ComfyUI投下のフローが主流。VRAM12GBで動作確認済み。
  - 更新履歴: v1.4.1→1.4.3（LoRAバグ修正、ノードID自動検出）→1.4.5（進捗%追加、バグ修正）。自前WF使用時のエラー解決。
  - 問題点: ポジ/ネガノード重複、特徴タグ重複挿入（仕様？修正予定）。APIエクスポートjson必須。
  - 新モデル: preview2 1536解像度試作品公開（手指/背景安定）。Airy/noobe+momizi3.1比較で好評。
- **ComfyUI/Spectrumノード高速化**:
  - 大ブーム。ノード無し vs 有り比較画像多数。30step→25秒→18秒短縮例（comple+併用で16秒）。
  - 推奨設定例（>>709, >>745）:
    | パラメータ | 値例 | 効果 |
    |------------|------|------|
    | block_indices | 3,5,9 | 特定ブロック再処理 |
    | denoise_start/end | 0.6/0.8 | 二度漬け範囲 |
    | spectrum | true | 高速化有効化 |
    | spectrum_w/m/lam/warmup | 0.25/16/0.95/9 | 発色維持・シャープ化 |
  - 注意: warmup6でグチャリ（8-10推奨）。easycache競合、絵師タグ効き弱化報告。Forge Neo版も9.8秒化確認。
  - 高速化メカニズム: UNet特定ブロック再処理 + Spectrum予測（CVPR 2026論文基盤）。
- **生成品質問題とTips**:
  - SDXL wildcard弱点: 泣き顔/goblin shota、押さえつけシーン失敗→Anima移行検討。
  - Animaの「子供落書き」現象: safe/explicit/nsfw同時指定、品質タグ不足、BREAK構文、3d/realisticタグ地雷。対策: danbooruタグ限定、anime screenshot/@絵師、ネガティブ強化。
  - プロンプト: 短め自然言語+LLM、LoRA高速化外し。例: "masterpiece, best quality, score_7, anime screenshot, safe, 2girls, @絵師"。

### 2.2 動画生成モデル（LTX2.3, Wan2.2/2.3）
- LTX2.3: kijai分割モデル+ RuneXX WF推奨（速い/VRAM優位）。extend機能あり（inpaint lipsync話題）。エロ/NSFW待ち、表情大げさ/外人向け批判。DaSiWa作者様子見。
- Wan: 使いやすさ/LoRA豊富/エロ強No.1。動画ループ/リップシンク優秀。息抜き推奨。
- リアルタイムi2i/SD1.5進化言及。RTX VSR2顔微細化/DLSS5期待（別物注意）。

### 2.3 ハードウェア・パフォーマンス議論
- **GPU/生成速度**:
  | GPU | 生成時間例 | コメント |
  |-----|------------|----------|
  | RTX5090 | 3秒/枚 | 1秒未満未来？電力/価格/サイズ増懸念 |
  | 40x0→50x0 | 性能微増/電力爆増 | Nvidia独占批判。AMD不人気 |
  | 12GB | 静止画OK/動画微妙 | 16GB+16GB熱い（qwen3.5 9B+animaで16GB弱） |
- VRAM拡張: キオクシア25.6TB SSD（NVIDIA CMX用、LLM/KVキャッシュ向け）。Radeon Pro SSG古参ネタ。
- SSD: モデル載せ替え遅延愚痴（1.8GB/s）。Stability Matrixで環境構築推奨。

### 2.4 ツールインストール・トラブルシュート
- **推奨入門**: Stability Matrix → Reforge/ComfyUI/Neo/SwarmUI（Reforgeガワ）。EasyReforge古/エラー多（公式リポ消滅）。
- **Gescharアプリ**: 再配信もどんぐりログイン不能（AppStore揉め）。Cookie消去/専ブラ/どんぐりハンターで解決。
- **その他**: 5chドメイン変更でﾜｯﾁｮｲ自衛。reforgeアプデで絵変化。Proサービス（Gemini/Nanobanana/Antigravity）ナーフ批判。

### 2.5 雑談・オフ-topic
- エロoutfit: ドルフィンショーツ+タンクトップ（イルカしっぽバグ）。panties/skirt lift。
- 宮崎駿85歳絵柄ネタ（漫画版ナウシカ似）。
- X投稿Tips: ハッシュタグ/キャラ名/衣装記述で閲覧数↑。
- フリーレンキャラ（フェルン）話題。Gemini/Qwen活用例。

## 3. 注目トレンド・ホットトピック
- **Spectrumノード祭り**: 高速化+発色調整で絶賛。ComfyUI/Forge Neo両対応。将来的一強？
- **Anima進化**: サンガツ氏の頻繁更新でユーザー定着。preview2高解像度が次期主流か。
- **動画シフト**: LTX/Wan競争。エロ/日本語LoRA待ち。
- **ローカル推奨**: クラウドナーフ（Google/Gemini）でローカル基盤重要。UX改善（Comfy App mode/SwarmUI）期待。
- **コミュニティ貢献**: 比較画像/設定共有多。初心者歓迎ムード。

## 4. 結論・今後展望
スレは実践派の技術共有場として活況。Spectrum/Animaが短期ホット、LTX2.3/Wan動画が長期トレンドか。RTX50x0価格下落でハード投資活発化予想。初心者はStability Matrixから。エロ/高速化追求がなんJ魂（笑）。次スレでLTX NSFW/RTX5090実機報告待ち。