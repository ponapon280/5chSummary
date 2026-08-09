# 🆕 新規トピック（前回からの差分）
### ハードウェア投資の活発化とローカル vs クラウド
- RTX 5090搭載PCを100〜120万円で購入する報告が複数あり、32GB VRAMモデルが主流。
- メモリ価格高騰により96GB〜128GB以上（2枚挿し推奨）への投資が増加し、低スペックからの大幅アップグレード報告が多い。
- 100万円投資 vs クラウド（1時間160円）のコスト比較で、1日8時間使用なら約2.6年で元が取れる計算が共有され、所有欲や即時性を評価する声とクラウド派の主張が対立。
- DGX Spark（128GB）検討や5070/5070 Ti買い替え、4090 48GB化などの話題も挙がる。

### MiniMax H3の最適化・ワークフロー
- 主流組み合わせはPatch Sage Attention KJ + Patch Sol-Attn + H3 Block Cache（T8）/Easy Cache + Turbo LoRAで、Mem Eff Sage Attention併用はCUDA相性で不安定。
- I2V/FL2V/T2V対応でTurbo LoRAにより4〜12ステップ生成が可能になり、20秒程度の長尺も現実的に。高速化時の音質劣化・ノイズに注意が必要。
- ComfyUI 0.31.0などで挙動が変わり、`--disable-dynamic-vram`解除で大幅短縮、`--fast-disk`でディスク使用量削減などの小技が共有される。

### LoRA・プロンプト戦略・LLM活用
- プロンプト作成はLLM（Grok、Claude、Gemma4など）に委ね、「雑な指示 → H3向け変換」のパイプラインが主流で、公式ガイドのretention_analysisなどを活用。
- 長尺生成では細切れ＋接続時の声トーン統一やカメラワーク安定が課題で、音声参照（リップシンク）やステレオASMRの試みも。

### NSFW・その他の傾向
- エロ生成ではおっぱいの動き・乳首露出・セックスシーンの安定性が焦点で、vibrates the breastsなどの記述やsexgod LoRA、衣装詳細が有効。
- 故人・家族写真を使ったAI生成の倫理的懸念や逮捕事例が指摘される一方、「普通のネット動画なら問題ない」という意見も。
- キャベツ動画実験、note有料販売者への懐疑、GeminiよりH3の動き自然さ・指示忠実度が高いという比較も。

### スレの特徴・トーン
- 海外（特にKijai氏）の最新情報を素早く取り入れ、技術共有が活発。「オナニー用」という前提が公然と語られ、金銭的余裕自慢や直接表現が普通で、金持ち優位の空気が強い。情報更新が非常に速い。

### 総評
- MiniMax H3によりローカル動画生成のハードルが下がり、Ref2V中心の高品質・一貫性ワークフローが実用段階に。Sage Attention系パッチ＋Turbo LoRA＋LLM補助が主流で、5090クラス移行検討者が増加。ComfyUI進化で初心者も入りやすいが、プロンプト精度と参照画像の質が最終クオリティを左右する。

### Web検索による参考情報
- MiniMax H3は2026年8月上旬にオープンウェイトでリリースされたomni-modal動画生成モデルで、ネイティブステレオ音声・T2V/I2V/Ref2V/FL2V対応、最大2K・5〜15秒クリップ生成。ComfyUIにDay-0サポートあり。
- RTX 5090は2025年1月30日発売、Blackwellアーキテクチャ、32GB GDDR7、MSRP $1,999で、ComfyUI動画生成用途で高評価。
- 最適化ではKijai氏のComfyUI-KJNodesにPatch Sage Attention KJが含まれ、Turbo LoRA（4ステップ対応）もコミュニティで共有が進む。
- 情報は2026年8月上旬時点のもので、モデル/ノードは急速に更新されているため最新状況はComfyUI公式やHugging Faceを確認のこと。

---
# 元の本文
**なんJ（5ch）AI生成スレ 統合レポート（MiniMax H3 / ComfyUI中心）**

### 概要
本スレッド群は、主に**ComfyUI + MiniMax H3**（通称H3 / mmh3）によるローカル動画生成環境の構築・最適化・実用化をテーマとした議論が中心。NSFW（特に実写寄り・Ref2V/I2V活用）用途を前提としたワークフロー共有が多く、「金で時間を買う」姿勢で高額ハードウェア投資を厭わない層が活発に情報交換している。Wan2.2時代のカスタムノード依存から脱却し、ComfyUIのテンプレート機能やコアノードだけで実用可能になった点が好評で、生成速度より品質・安定性を重視する慎重派と「とにかく速く」を求める勢力が混在する典型的ななんJ AIスレッド。

### 主要トピック

**1. ハードウェア投資の活発化とローカル vs クラウド**
- RTX 5090搭載PC（自作・工房・サイコムなど）を100〜120万円前後で購入した報告が複数。32GB VRAMモデルが主流で、5090推しが非常に強い。
- メモリ価格高騰が深刻で、96GB〜128GB以上（2枚挿し推奨）への投資が目立つ。低スペック（4060ti、4070tiなど）からの大幅アップグレード報告が多く、生成速度の劇的向上を実感している。
- コスト比較：100万円投資 vs クラウド（1時間160円程度）で、1日8時間使用なら約2.6年で元が取れる計算。3年後の中古相場を考慮した「実質タダ」論や所有欲・即時性が評価される一方、クラウド派は初期投資不要・故障リスク回避を主張。ただしクラウドは週末混雑やアップロード遅延の不満も。
- その他：DGX Spark（128GB）検討や、5070/5070 Ti買い替え、4090 48GB化などの話も。

**2. MiniMax H3の最適化・ワークフロー**
- 現時点の主流組み合わせ：Patch Sage Attention KJ + Patch Sol-Attn + H3 Block Cache（T8）/Easy Cache + Turbo LoRA。Mem Eff Sage Attentionとの併用はCUDA相性で不安定という報告あり。
- Ref2V（Reference to Video）が特に熱いトピック。複数参照画像を「subject definition → summary → retained analysis → detailed description」の流れで構造化し、LLM経由で整理して投入。「リファレンスを渡せおじさん」スタイルが定着。
- I2V / FL2V / T2Vも対応。Turbo LoRAにより低ステップ（4〜12 steps）生成が可能になり、20秒程度の長尺も現実的に。高速化すると音質劣化・ノイズが発生しやすいため、用途別に使い分ける。
- ComfyUIバージョンアップ（0.31.0など）で挙動が変わる報告あり。`--disable-dynamic-vram`を外すと大幅短縮、`--fast-disk`でディスク使用量削減などの小技も共有。

**3. LoRA・プロンプト戦略・LLM活用**
- Anima LoRAのブロック制御（LBW）、ComfyUI-LoRA-Block-Filter、Power LoRA Loader、Civitai連携ツールの活用。
- プロンプト作成はLLM（Grok、Claude、Gemma4/Claude/Grok/Deepseekなど）に委ねるのが主流。「雑な指示 → LLMでH3向けプロンプト変換」のパイプライン。公式ガイドの「retention_analysis」「fully_preserved」などを活用した一貫性維持が有効。
- 長尺は細切れ生成＋接続、声のトーン統一やカメラワーク安定が課題。音声参照（リップシンク）やステレオASMRの試みも。

**4. NSFW・その他の傾向**
- エロ生成ではおっぱいの動き・乳首露出・セックスシーンの安定性が頻出。vibrates the breastsなどの具体記述やLoRA組み合わせ（sexgodなど）、衣装詳細記述が有効。
- 倫理的懸念：故人写真・家族写真・遺影AIなどの「需要はあるがヤバい」声や逮捕事例の言及。一方、「普通のネットに上げられる動画なら問題ない」という現実的意見も。
- その他：キャベツ動画などの実験、note有料販売者への懐疑、GeminiよりH3の動き自然さ・指示忠実度が高いという比較。

### スレの特徴・トーン
技術情報共有が活発で、海外（特にKijai氏）の最新情報を素早く取り入れている。「オナニー用」という前提が公然と語られ、金銭的余裕を自慢する書き込みや「シコシコ」などの直接表現が普通。低スペック民への配慮もありつつ「金持ち優位」の空気が強い。情報更新が非常に速く、数日で推奨設定が変わる可能性が高い。

### 総評
MiniMax H3の登場によりローカル動画生成のハードルが一段下がり、Ref2Vを中心とした高品質・一貫性重視のワークフローが実用段階に入った。Sage Attention系パッチ＋Turbo LoRA＋LLMプロンプト補助が現在の主流で、5090クラスへの移行を検討する人が増えている。ComfyUIの進化で初心者でも入りやすくなった一方、プロンプト精度と参照画像の質が最終クオリティを左右する。

---

## Web検索による参考情報
- **MiniMax H3**: 2026年8月上旬にオープンウェイトでリリースされたomni-modal動画生成モデル。ネイティブステレオ音声対応、T2V/I2V/Ref2V/FL2V対応、最大2K解像度・5〜15秒程度のクリップ生成。ComfyUIにDay-0サポートあり（Comfy-Org/MiniMax-H3 on Hugging Face）。[[1]](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)[[2]](https://comfy.org/minimax/)
- **RTX 5090**: 2025年1月30日発売、Blackwellアーキテクチャ、32GB GDDR7、MSRP $1,999。ComfyUI動画生成用途で高評価。[[3]](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)[[4]](https://www.techpowerup.com/gpu-specs/geforce-rtx-5090.c4216)
- **最適化関連**: Kijai氏のComfyUI-KJNodesにPatch Sage Attention KJノードが含まれており、速度向上に広く使われている。MiniMax H3向けTurbo LoRA（4ステップ生成対応）もコミュニティで公開・ワークフロー共有が進んでいる。[[5]](https://comfy.icu/node/PathchSageAttentionKJ)[[6]](https://comfyui-wiki.com/en/news/2026-08-06-minimax-h3-turbo-lora)

（検索時点：2026年8月上旬時点の情報に基づく。モデル/ノードは急速に更新されているため、最新状況はComfyUI公式やHugging Faceを確認のこと。）
