# 生成AI関連「ツール」話題抽出レポート

## 抽出対象ツール一覧

### ComfyUI / Comfy Agent
- **ComfyUIのメモリ管理改善**: メモリ不足時に捨てSSDに大容量の仮想メモリを当ててOOM防ぐ方法があったが「今じゃComfyui自体が賢くなってやる必要性すらなくなった」という報告（>>355）
- **Comfy Agent**: ローカルでも使えるようになるとLLMの話題でスレが占拠されると予想する声（>>375）
- **Strata + ComfyUI連携**: 「strataにcomfy触らせてNSFW画像・動画生成支援エージェント環境構築」という構想。並列が厳しい場合はComfy動くときStrataを落とす運用を提案（>>387）
- **ComfyUIとLLMの同時起動問題**: 「Comfyと同時起動できないと少し辛い」という指摘（>>399）
- **過去のComfyUIメモリ消費**: 2年前のComfyUIでFlux1-devをロードする時にメインメモリを70G以上使う現象があったとの回想（>>283）

### Strata
- **Strata + Hermes Desktop**: 「実質Codex無料で使い放題プラン」と評価（>>232）
- **StrataでAIエージェント体験**: codexを使ったことがない層がStrataで初めてAIエージェント的なことができたという報告（>>233）
- **Strataの推奨ハーネス**: Strata作者の考える4大ハーネスはHermes, pi, open code, Deepseek harness（>>239）
- **Strataの更新速度**: 「更新速いから頻繁に驚ける」「利用者も増えてきたから情報も充実してきた」（>>318）
- **Strataの量子化**: 「strataのq3は量子化きついからRAMがあるならnvfp4とかq4がええよ」という助言（>>390）
- **StrataのCodex対応**: 「strataがcodex対応したんね」という報告（>>424）
- **Strata選定理由**: ローカルLLMのロマンとして言及。ただし価格・性能面ではDeepseek v4.1 flashの方がマシという比較（>>235）
- **Strata鯖構築例**: ハードオフで安いケース買ってUbuntuでStrata鯖にする構想。AM4ならCPUとマザボで2万でいける（>>388）

### Hermes / Hermes Desktop
- **Hermesの思想**: openclaw等と同じく常時起動で日常的なルーティン作業を自動化するパーソナルアシスタントを作る思想（>>238）
- **Hermes DesktopのAutoCompaction**: API経由でもコンテキスト圧縮してくれる機能を確認。UnslothDesktopはAPI経由だとAutoCompactionしてくれない（>>243, >>244, >>245）
- **Hermes Desktopのバグ**: 「たまにバグるから使うならcliかtuiで使ったほうがええ」という助言（>>240）
- **Hermes Desktop設定時の発見**: BionicにOpenAI互換APIの設定がないことを確認。LM StudioでDLしたモデルを優先的に使う思想かと推測（>>247）

### OpenWebUI
- **OpenWebUI推奨**: スマホでチャットする用途に対し「OpenwebUIいいぞ」という推奨（>>338）
- **環境構築の面倒さ**: OpenWebUI + OpenTerminalの面倒な環境構築が終わった後にHermes Desktopという導入簡単なオールインワンがあることを知ったという報告（>>250）

### LM Studio / LM Studio Bionic
- **LM Studio BionicのAutoCompaction**: AutoCompactionしてくれることを確認（>>244）
- **Bionicの制限**: API経由でローカルLLM動かせないはずという指摘（>>245）
- **LM Studioのスマホ利用**: 久々に使ったらスマホでチャットするのが面倒になっているという報告。以前はアプリでいけた（>>330）
- **LM Studio BionicのAPI設定**: OpenAI互換APIの設定がないことを確認（>>247）
- **BionicのSandbox機能**: Sandboxフォルダにhtmlファイルをポン出ししてくれる機能。LM Studio bionicでも同じことができたがStrataとの連携ができなかった（>>237）

### OpenCode
- **OpenCodeのデスクトップアプリ連携**: デスクトップアプリとの連携ができるかという質問。ハーネスに該当するかという問い（>>234）
- **4大ハーネスの一つ**: Strata作者の考える4大ハーネスに含まれる（>>239）
- **オープンソース志向**: オープンソースで揃えたい場合の候補としてPi, JAN等と共に挙げられる（>>238）

### Pi
- **コーディング用途の最適**: 「コーディング重視ならPiをハーネスにするのが一番ミニマムで使いやすい」。Pi2が出たばかり。Strataの推奨もPi（>>263）
- **4大ハーネスの一つ**: Strata作者の考える4大ハーネスに含まれる（>>239）

### DeepSeek Harness
- **4大ハーネスの一つ**: Strata作者の考える4大ハーネスに含まれる（>>239）
- **思想**: all of pluginみたいな思想らしい。難易度高め（>>238）

### Unsloth Desktop
- **制限事項**: API経由だとAutoCompactionしてくれない仕様。コンテキスト足りなくなったら引き継ぎ書作成させて新しいセッションで続きやる使い方をしているが「くっそめんどい」（>>243）

### Claude Code
- **バックエンド変更の容易さ**: codexみたいにしたいならClaude Codeのバックエンド変えるのが一番簡単という助言（>>238）
- **自作ツールの提案**: コーディング用途以外なら自分に合わせた機能とUIをClaudeCodeに伝えて半日で作ったほうが満足度高いという意見（>>262）

### Ollama
- **スマホ接続**: OllamaアプリでPC接続してチャットできたという報告。5.6Solに質問した時は変なこと言われたが（>>334）

### DeepL
- **翻訳ツールとしての言及**: 自然言語が必要な場合にDeepLを使うことが多いが、ローカルLLMと併用がいいかという問い（>>409）

### Caveduck
- **エロチャットツール**: AIモデルをClaude 5.5にしたらめっちゃエッチな文を書くようになったという報告（>>403）

---

## ツール選定理由のまと要

| ツール | 選定理由 | 根拠 |
|---|---|---|
| Strata | codex無料で使い放題相当。更新速い。初めてAIエージェント体験できる | >>232, >>233, >>318 |
| Pi | コーディング用途でミニマムで使いやすい。Strataの推奨 | >>263 |
| Hermes | 常時起動のルーティン自動化思想。API経由でもAutoCompaction対応 | >>238, >>244 |
| OpenWebUI | スマホチャット用途で推奨 | >>338 |
| Claude Code | バックエンド変更が簡単。カスタムツール自作が半日で可能 | >>238, >>262 |
| DeepSeek Harness | all of plugin思想だが難易度高め | >>238 |