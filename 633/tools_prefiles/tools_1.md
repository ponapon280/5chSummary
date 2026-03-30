### 抽出された生成AI関連「ツール」話題一覧

ログからツール（ComfyUI(comfy), webUI, nano-banana など）に限定して抽出。モデル（anima, illustrious(リアス), NAI, FLUX, Wan, Qwen-Image, Z-Image(ZIT/ZIE), LTX など）関連話題は除外。Qwenシリーズは画像生成以外（例: TTS）の話題のみ抽出。ツール選定理由が明記されている場合を強調。

#### LiteLLM (66, 98, 99)
- 66: LiteLLMのライブラリがマルウェアに感染。comfyuiのimpact packでも過去に類似事件あり。AIエージェントでAPI課金・モデル使い分け時は要注意、クラウドAIユーザーほど感染リスク高。
- 98: litellmの存在チェックコマンド紹介（pip list等）。matrix環境での対応方法質問。
- 99: llvmliteと混同注意。

#### ComfyUI (comfy) (66, 71, 81, 107, 109, 111, 126, 149, 153)
- 66: comfyuiのimpact packで過去マルウェア事件あり。
- 71: ComfyUIのカスタムノード依存関係でマルウェア感染リスク高。
- 81: AntigravityやComfyUI導入で這い上がるユーザー多数。
- 107: comfyは2ヶ月触らないと更新で動かなくなる（音声拡張・画像生成以外も）。初心者におすすめは嫌がらせ級、1年対応時間浪費。
- 109: **動画・音声ならcomfyしか無い**（上級者向け、更新込みで楽しむ選ばれし人間向け）。
- 111: **用途ごと複数バージョン管理がベスト**（初心者はアップデートせずeasy民多数）。
- 126: comfy勉強・ワークフロー管理で絵・美術勉強疎か。**「複雑comfy使いこなし賢い俺」アイデンティティ危険、AI進化で術師不要**。
- 149: ComfyUI vs Python直書き/Claude Code比較。ComfyUIは画面ガチャガチャ・前提モデル使いにくい。Claude Codeは自然言語依頼で構築自動化・重複共通化優秀。**トータルClaude Code寄り**（SD画像生成/LoRA学習/Qwen3TTS音声クローン/QIE画像編集/剥ぎコラはPythonで容易）。
- 153: **コーディング可能ならComfyUI学習コスト無視、ドスケベWF多数でComfyUI必須**。

#### Antigravity (69, 81)
- 69: antigravityは髪ツールかと思ったが、OpenClawまでPC生殺与奪握られ怖い。
- 81: Antigravityでツール作り・ComfyUI導入で這い上がる。

#### OpenClaw (56, 69)
- 56: 定額OpenClaw神、OpenAI潰れても困らない。
- 69: OpenClawでPC生殺与奪握られ怖い。

#### Claude code / codex (80, 149)
- 80: Claude無料枠止まりでcodex試用。ファイル指定なしでローカルファイル触る・powershell使用怖い。**Claude code連携で検証早いが、人間手動検証のためコード出力のみ希望**。
- 149: Claude Code自然言語依頼で構築自動化優秀（ComfyUIより楽、重複共通化）。

#### Botan (76)
- 76: anima生成時botan使用でCFG6まで上げ。

#### QIE (83, 149)
- 83: 素材水増しにSD i2i/QIE/Seedream（エロなしSeedream）。
- 149: QIE画像編集容易（Python直書き）。

#### nano-banana (84, 87, 90)
- 84: gemini（nanobanana2）に素材食わせ描画。
- 87: nano bananaで素材15枚用意・LoRA組んでテスト。
- 90: **nano banana素材は胴体まで・顔学習避け推奨**（遜色ない出来）。

#### Qwen3-TTS (67, 149)
- 67: Qwen3-TTS試用、ゼロショットでレパートリー素材不足（棒読み→感情音声生成希望、動画AI素材→LoRA→LLMオーディオブック）。
- 149: Qwen3TTS音声クローン容易（Python直書き）。

#### Seedream (83)
- 83: 素材水増しにエロなしSeedream。

#### Irodori (95, 178, 205)
- 95: Irodoriフォーク版V2対応感謝。
- 178: Irodori公式LoRA対応。
- 205: 本家LoRA学習yaml追加参考・エラー解消もv2 VRAM爆上がり（5000step16時間、VRAM12GB限界）。公式LoRA学習3時間試用。

#### Stability Matrix (226)
- 226: Stability MatrixのPatreonサイト運営削除（explicit画像生成ツール禁止ポリシー）。

#### その他ツール関連言及
- powershell (80): codexが生成コード検証で使用。
- TurboQuant (76, 138, 200, 202-204, 206, 209, 216, 225, 230-233): GoogleのLLMメモリ1/6圧縮技術。画像生成非対応・LLM/チャット/音楽生成（echo-tts等）に効果大。速度微妙も高性能モデル個人運用革命期待。プルリク検証可能。
- LitMedia (120, 139, 143-145): SeeDance2用買い切りプラン迷い。Kling API偽装サイト問題・新興信用不安・金額バー調整（2万〜6万、月動画本数制限）。
- SeeDance2 (120, 139, 144, 187): LitMedia買い切り・ガチャ1000円/8秒厳しい。

抽出はツール名・文脈・選定理由（強調）を中心に網羅。重複/文脈連続は統合。