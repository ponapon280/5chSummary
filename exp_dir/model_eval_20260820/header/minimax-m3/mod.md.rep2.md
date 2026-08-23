### モデル: Minimax H3（H3 / MiniMax H3）
- 言及数最多。事実上の中心話題。
- 日本語プロンプトの理解・貫通力が突出している。
- 動画生成性能がWan2.2やLTX2.3を大きく上回る（画質・制御性・エロ表現・参照機能）。
- 参照機能、Motion Context、clip chainingが優秀で、複雑な動きやエロ表現に強い。
- 静止画も構図などで高性能。性能向上により生成者の才能が活きると評価。
- 低〜中スペックでもある程度動作可能（高スペック推奨派もあり）。
- ComfyUIでのワークフロー成熟度が高く、LoRA作成やContext Loopなどの実験が活発。

### モデル: その他のモデル
- Wan / Wan2.2：H3に明確に劣ると認識。アニメキャラの動き再現などで使用。
- LTX / LTX2.3：H3に及ばないが、生成速度の速さが利点。
- NovelAI（NAI / nai5）：次世代候補として言及あり。背景生成で高評価。
- その他（Krea2、MiniMax静止画モデル、10Eros、Gemma4、Grokなど）：次世代候補や補助として散見。Krea2は画質で期待大。

### モデル: 全体傾向と補足
- ComfyUIワークフローの成熟度やLoRA相性がモデル選択の主要因となっている。

### モデル: Web検索による参考情報
- MiniMax H3：2026年7月31日リリースのオープンウェイト汎用マルチモーダル動画生成モデル。テキスト・画像・動画・音声を統合処理し、最大15秒・2K・ネイティブステレオ音声対応。米欧など地域制限付きライセンス。[[1]](https://www.minimax.io/blog/minimax-h3)[[2]](https://www.reuters.com/world/china/chinas-minimax-releases-h3-video-model-2026-07-31/)[[3]](https://github.com/MiniMax-AI/MiniMax-H3)
- Wan2.2：MoEアーキテクチャ採用のオープン動画生成モデル。720p/24fps対応で消費者向けGPU（例: 4090）でも動作可能。[[6]](https://github.com/Wan-Video/Wan2.2)[[7]](https://docs.comfy.org/tutorials/video/wan/wan2_2)