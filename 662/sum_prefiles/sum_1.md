**なんJ（5ch）スレッド・レポート**

### スレッド概要
本スレッドはStable Diffusion（主にアニメ系モデル）をローカルで扱うユーザーによる雑談スレッド。話題の中心は以下の通り：

- **Anima系モデル**（Anima-turbo / Animerge）の話題が非常に多い
- Animergeの新機能「ADDifT」（特にDPOモード）の実用報告
- GPUの物理的設置問題（ステイ・ケーブル・発火リスク）
- LoRAマージ vs 外付けのメリット比較
- ComfyUI関連の細かいトラブル・運用話

全体的に「実際に触ってる人」の技術的・実践的な会話が多く、単なる感想だけでなく具体的な設定や失敗談が散見される。

### 主なトピックまとめ

**1. Anima / Animerge関連**
- 「Anima-turbo近日公開」という発言に対し「base1.0出た時からずっとComing Soon」との指摘あり。
- Animerge作者による複数回の更新報告（GUI改善、ADDifTのDPOモード追加）。
- DPOモードは「良い画像・悪い画像の2枚で好みを反映させる」簡易版実装として紹介され、実際にぶっかけ強度調整などで効果が出た報告あり。
- 「animaはおっぱいが大きくなりがち」「minigirlやstomach bulgeの再現性はillustrious＞anima＞pony」という評価も。

**2. ADDifT / DPOの実践**
- 通常のADDifTとDPOモードの違いを作者が説明（パラメータ直接操作 vs 経路遮断）。
- 実際に「ぶっかけ前後画像」でADDifTを作成した報告があり、マイナス方向で効果が出た事例も共有された。

**3. ハードウェア・設置問題**
- Fractal Design Define 7のGPUステイ問題が複数報告。
- 結束バンド・アクスタ・ミンティアケースなど独自の固定方法が共有される。
- 12V-2×6コネクタの発火リスクについても言及あり（甘挿しが主因という意見が多数）。

**4. その他**
- LoRAマージのメリットは「1モデルで済む＋わずかに速い程度」との評価。
- ChatGPT Plus（月額3000円）とClaudeの比較では「利用制限の観点でChatGPT一択」という結論。
- ComfyUIのManager v4系移行に関する話題も散見。

### ## Web検索による参考情報

- **Animerge**：CivitaiやGitHub上で公開されているアニメモデルマージ用GUIツール。ADDifT（Advanced DPO for Image Tuningの略か）と呼ばれる独自の好み反映機能を実装しており、2025年現在も活発に更新されている。
- **Anima（Anima-turbo）**：Civitaiで公開されているアニメ特化のマージモデル群。IllustriousやPonyと並んで2次元イラスト用途で人気。公式に「Coming Soon」と長期間記載されていたAnima-turboは、baseモデル公開後も正式リリースが遅れている状態。
- **ComfyUI**：現在ローカルStable Diffusion環境のデファクトスタンダード。WebUI（Forge含む）からの移行が進んでおり、Managerのv4系への移行も2025年に入って活発化している。
- **ADDifT / DPO**：元々はLLMの強化学習で使われるDPO（Direct Preference Optimization）を画像モデルに応用した手法。Animergeでは簡易版として実装されており、2枚の画像ペアで特定の表現を強化・抑制できる。

---

**総評**  
技術的な深みがあり、実際にツールを触っている層の会話が中心。AnimergeのADDifTは現時点で最も実用的な「好み反映」手法の一つとして注目されている。