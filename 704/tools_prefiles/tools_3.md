# 生成AI関連「ツール」話題 抽出レポート

## ComfyUI
- ComfyUIのエラー解析やカスタムノード作成にLLMを利用している（442, 489）
- IQ3_SでComfyUI併用する場合でも192GBあればLLMとComfyUIのモデルをアンロードなしで実用範囲で動かせる（587）

## Strata
- 4090環境でstrata + Flash-NEXTをプロンプト係として使用。画像認識が不十分でルールをすぐ忘れる、誤字が多いと判断。UIそのままでシスプロもスキルも入れずに使うと性能が出ない（425, 447）
- gptに課金していないがstrataでUIを作れて感動した（452）
- qwen3.8 flash nextは長すぎて不適切でもstrataと呼びたくなる（453）
- GitHubでGLM-5.3 FlashやDeepSeek4-Flash対応のPRが出ており、来月にはStrataだけではモデル名が分からなくなる見込み。Mac対応も済み（457）
- StrataとUnsloth UD-IQ4_XSをRTX5090 + 128GB環境で仕事使用。機密情報を気にせず使えるのが良い（516）
- IQ2_XSかIQ3_XXSあたりをワンクリックで試せる。ただ64GBで画像生成との併用は双方のモデルのアンロード/ロード必須で生成に時間がかかる（587）
- StrataのIQ3_XXSを導入。LLMをプロンプトエンハンサーとカスタムノード作成程度にしか使わない用途にはゲームエンドかもしれない、plus解約を検討（607）
- StrataのIQ3_XXSが結構速く動くことを確認したが、チケットブッパマン化しているため今はcodexで良いと判断（616）

## nanosaur2
- 軽量画像生成モデルnanosaur2は4stepで1024x1024画像1枚を平均1秒以下で出力可能（3090環境）。qwen3.8 flash nextに水着6枚生成を依頼し10秒程度で出揃う。バッチ処理なら1秒で24枚生成可能。画質はSD1.5程度（522, 524, 529）
- 選定理由：高速生成が可能である点

## irodori-tts
- 脱糞テキストをirodori-ttsに読ませている（562）

## Suno
- sunoの性能自体は高いが、ヒット曲が生まれる土壌・経路が存在しておらず、淫夢文脈がその役割を果たしたというスレ上の見解（556）

## Codex
- codexのリセット権が増加した（599）
- strataのIQ3_XXSが速く動くことを確認したが、今はcodexで良いと判断（616）

## Claude Code
- Claude Code使用時にAPIクレジットが毎月配布されるようになった。申請必要。APIクレジットはサードパーティ製アプリでも使用可能（601, 606）
- 選定理由：APIクレジット配布（100ドル分）により使用ハードルが下がった点

## Krea2
- orca版以外の無検閲QwenでKrea2の画像出力プロンプト生成に使用し、いい感じだった（511）

## copainter
- 漫画エージェント。エッセイまたは4コマ向きというスレ上の評価（423, 424）

## Siki
- 貼られた画像のプレビューが出るため、オリジナルサイズになっているか事前確認できる（602）

## civitai
- 7920x12936解像度・18.7MBの画像サムネイルによりスクロールが激重になる現象が発生。civitai側の改善が望まれる（614, 617）

## llama.cpp
- DeepSeek v4の推論速度向上のため、StrataとFreetokenとllama.cppを参考にAstraに指示し、15tok/sが30tok/s程度に倍速化（555）

## OpenRouter
- DeepSeek v4をローカル導入前にOpenRouterで試した。ほぼタダみたいな金額（567）

## webUI / Anima関連ツール
- WAI-Animaを使用してエロ絵生成したがmating pressが機能しなかった。READMEを読まずにプロンプト順が壊れている可能性（572, 576, 578）
- anima_turboV11.safetensorsを使用する必要あり。Turboの場合VAEとtext encoderは不要（593, 596）
- WAI-Anima以外にBASNSFWBetterAnimeStyleForNSFWHentai_baseV10やanima-base-v1.0.safetensorsを試した（583）
- animaのWAIは微妙。講師のbaseにLoRAを噛ませるのが一番安定する（615）
- animaでは版権キャラを出す場合リアス以上に作品名必須。「tomoe mami from mahou shoujo madoka magica」のような記述を推奨（618）

## コントロールネット
- コントロールネットのi2iやインペイントと素の状態の違いについての質問（623）
- animaのコントロールネットがリアスレベルのものを使えるか不明（582）