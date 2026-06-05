**なんJ AIアニメスレッド レポート（要約）**
### スレッド全体の傾向
- **中心トピック**: SDXL系アニメ特化モデル「Anima」（特にAnima base / Hakushi Mix Anima）の評価と活用法。
- v2v（動画生成）やimage-to-image、LoRA学習の話題が活発。
- 「公式に寄せたファンアニメ」の是非や、クラウドAI（ChatGPT/Gemini/Grok）のBANリスク、ローカル完結環境の重要性が繰り返し議論されている。
- 技術的な話題（ComfyUIワークフロー、TensorBoard、LBW調整）と、ハードウェア（RTX 3060〜5090）の価格・性能談義が混在。
### 主なモデル・ツールの言及
- **Animaシリーズ**（特にAnima base v1.0、Hakushi Mix Anima v1.0）
 - 線が綺麗でfull bodyでも顔が崩れにくいと高評価。
 - 画風LoRAとの相性や、NSFW寄りの挙動（特定の構図で制限がかかる）についての実験報告多数。
- **その他モデル**: GhostXL、Linen Illustrious、Pony v7、WAI-Anima。
- **ツール**:
 - ComfyUI（v0.23→v0.24.0への更新報告、MMAudioノード、Spectrum Adaptive Forecaster使用例）。
 - kohya、TensorBoard（学習ログ確認）。
 - クラウド系: ChatGPT（ちゃっぴー）、Grok、Gemini、Deepseek v4 flash + Hermes agent。
### コミュニティの主な関心事
- **クラウドBANリスク**: NSFW寄りのプロンプトでアカウントBANが多発。ローカル環境（特にAnima）の重要性が再確認されている。
- **規制・二次創作**: 「公式に寄せすぎたAI作品」の通報問題や、将来的なプラットフォーム規制への懸念。
- **ハードウェア**: RTX 3060 12GBの再販価格（中国で約4.8万円）や、5070ti/5080への移行検討。VRAMの重要性が強調される。
- **新技術の模索**: Qwen Image系チェックポイントやGemma4 12Bなどの新モデルへの言及。
---
## Web検索による参考情報
- **Anima / Hakushi Mix Anima**: Civitai上で公開されているSDXLベースのアニメ特化モデル。Hakushi Mixはコミュニティ製のマージモデルとして人気で、線画の綺麗さとアニメ調の安定性が評価されている（2025年時点でbase v1.0が主に議論）。
- **ComfyUI v0.24.0**: 2025年頃にリリースされた最新版。MMAudioや各種カスタムノードとの互換性改善が報告されており、v0.23からの短期間アップデートとして話題に。
- **Deepseek / Hermes**: Deepseek v3/v4シリーズは中国製LLMで、HermesはOpenHermes系エージェント。ローカルでの動画グリッド生成やプロンプト補助に使われている事例あり。
- **Gemma 4 12B**: GoogleのGemmaシリーズ後継モデル。量子化なしで24GB未満VRAMでも動作可能とされる軽量モデルとして注目。
- **PiD SDXL/Qwen Image**: Qwen-VL/Qwen2系を基にした画像生成チェックポイント。ComfyUI対応が進められており、NSFWフィルタの挙動が議論の的。
- **RTX 50シリーズ**: 5060/5070/5080/5090は2025年以降のNVIDIAミドル〜ハイエンド。3060 12GBの再販は中国市場で確認されており、VRAM重視のユーザー層で根強い支持。
レポートはスレッドの空気感（技術共有＋BAN警戒＋モデル愛）を中心にまとめました。