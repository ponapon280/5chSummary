# 🆕 新規トピック（前回からの差分）
### MiniMax H3（H3 / MMH3）の評価と活用
- H3は主力動画モデルで、参照画像保持・日本語理解・実写寄りの自然な動きを評価。一方、アニメ・エロ生成では追従性・細部描写に課題。
- 主なワークフローはref2v/i2v/fl2v/Context Loop/RIFE。ステップ20-32が主流でTurbo LoRA併用。4stepが音質画質バランス良く、8stepは画質向上も音質劣化。
- NSFW生成では性器・動作・効果音が課題。ワイルドカード・短尺ループ・局部LoRAを試行し、実写や後付けSEが現実的。

### 高速化・最適化・ワークフロー
- 速度向上事例多数（1MP5秒動画が240秒→25秒）。ComfyUI Kitchen + Sage Attention + Turbo LoRAなどが有効。精度重視はbf16推奨。
- ワークフロー管理（pngメタ・日付）、Easyノード是非、VRAM節約を共有。ComfyUI v0.30以降更新活発。Context Loopは低ステップLoRAと相性良く、Music3とSuno/AceStep併用も検討。

### コミュニティの雰囲気
- 高速化技術の進展に興奮と疲労が混在。初心者向け厳しめアドバイスが多く、NSFW関心高く自嘲も。完全自動化を目指す層も。

### Web検索による参考情報
- ComfyUI Kitchen、SageAttention、Turbo LoRAがH3高速化に有効でユーザー報告あり。
- モデル情報は2026年8月時点の公開情報に基づく。

---
# 元の本文
**なんJ（5ch）AI画像・動画生成スレッド 統合レポート**

### スレッド概要
本スレッドは、主に**ComfyUI**を用いたローカルAI動画生成（特に**MiniMax H3** / H3）を中心に、静止画モデル（Anima系）との併用、ワークフロー最適化、ハードウェア議論、NSFW生成の工夫が活発に展開される技術系スレッドです。H3登場直後の過渡期で、従来のAnima/Krea2/LTX2.5からH3への移行が進み、ComfyUIへの完全移行を推奨する声が多数を占めています。投稿は実践検証重視で、速度向上報告や具体的な設定共有が目立ちます。

### 主要トピック

**1. MiniMax H3（H3 / MMH3）の評価と活用**  
H3は現時点の主力動画モデルとして最も言及が多く、参照画像保持能力（i2v/ref2v/edit用途）の高さ、日本語理解度の向上、実写寄りの自然な動きが評価されています。一方、アニメ・二次元やエロ生成では追従性・細部描写に課題があるとの声も。  
主なワークフロー：ref2v / i2v / fl2v / Context Loop / RIFEフレーム補完。ステップ数は公式30-50に対し、20-32前後で妥協する例が多く、高速化LoRA（Kijai版 lightx2v系 Turbo LoRA）の併用が一般的。4step（強度0.7前後）が音質・画質バランスで優勢、8stepは画質向上するが音質劣化（おばちゃん声化など）の報告あり。Adaptive OFFで改善例も。  
NSFW（エロ）生成の課題として性器描写・ピストン動作・効果音がボトルネックで、システムプロンプトのワイルドカード活用、短尺ループ動画推奨、局部参照LoRA併用などが試行されています。実写系や後付けSEが現実的との意見も。

**2. Anima系モデル（Anima base / Turbo / Anima-2.9B）**  
Anima base v1.0はアニメ・イラスト特化の基盤モデルとして残存し、LoRA学習のしやすさ（Danbooruタグ対応）で高評価。Turbo版は画風変化で好みが分かれる。  
Anima-2.9Bはサードパーティ製のレイヤー拡張（2B→2.9B）＋追加学習モデルで、構図安定性向上・NSFW描写強化が肯定的に評価される一方、生成速度の低下（約1.4倍）やタグ効きの変化が指摘されています。ComfyUI-Anima-2.9Bカスタムノード必須（プラグ＆プレイだが他ノード衝突注意）。SDXLのIllustrious/Noob相当の派生モデルとして位置づけられ、LoRA作成環境整備が進んでいます。

**3. 高速化・最適化・ワークフロー**  
目覚ましい速度向上報告が相次ぎ（例: 1MP 5秒動画が240秒→25秒台）、有効組み合わせとしてComfyUI Kitchen、Sage Attention、Turbo LoRA併用、--fast-disk、int8ConvRot系などが挙げられます。精度重視派はbf16推奨。  
ワークフロー保存・バージョン管理（pngメタデータ、日付付け）、Easy系ノードの是非、最小化時の速度変化、VRAM節約術が共有。H3対応ComfyUIアップデート（v0.30以降）が活発。Context Loopは自由度が高く低ステップLoRAと相性良し。MiniMax Music3も言及され、Suno/AceStep併用検討例あり。

**4. ハードウェア・環境**  
3060 12GBでも動作するが快適には32GB RAM目安。5070Ti/5080/5090勢は高解像度・富豪オプションを試し、BTO機（120-130万円前後）購入報告多数。4070 Tiとの2台体制や64GB→96GBメモリ増設希望も。Radeon（9070 XTなど）勢の台頭もあり、NVIDIAとの安定性・情報量で議論。Stability Matrix経由インストールが人気。RunPod vs ローカルWindowsの挙動差も話題。

**5. その他のモデル・傾向**  
LTX2.5 / WanAnimate2 / Krea2 / PinkCherry 0.6 / Qwen系が言及されるが、H3＋Animaの組み合わせが主流。将来的なAnima2.9B以降のFTモデル期待も。プロンプトは「禁止」ではなく誘導表現が有効で、7000文字対応確認例あり。

### コミュニティの雰囲気
「毎日新しい高速化技術が出てくる」興奮と疲労が混在しつつ、「comfy-kitchenだけでいい」という落ち着きも。初心者には「AIに聞け」「自分で動かせ」という厳しめアドバイスが多く、情報共有は活発（感謝の声も）。NSFW関心が高く、「風俗よりPCの方がコスパ良い」といった自嘲や金銭感覚の話も。完全自動化（LLM＋ComfyUI連携）を目指す層も登場。

### 総評
H3登場により動画生成の主戦場が大きく動き、「H3＋ComfyUIが現在の最適解」というコンセンサスに近づいています。Animaは静止画・LoRA基盤として残りつつ、動画はH3一強ムード。ただし「まだ完成形ではない」認識が共有され、次世代モデル（Anima2系や公式edit強化）への期待が高い状態。静止画時代からの移行期に技術共有が非常に活発なスレッドです。

## Web検索による参考情報
- **MiniMax H3**: Hailuo AI / MiniMaxのオープンソース動画生成モデル（2026年登場）。ComfyUIネイティブサポート（v0.30以降）でT2V/I2V/R2Vワークフロー対応、ネイティブステレオオーディオ生成（最大2K/24fps/約15秒）。モデルはHugging Face Comfy-Org/MiniMax-H3で公開。Turbo LoRA（4/8stepなど）による高速化がコミュニティで活用され、SageAttentionやComfy Kitchen attentionなどのバックエンドと組み合わせ可能。[[1]](https://www.youtube.com/watch?v=d_wEd-fZcdg)[[2]](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- **Anima / Anima-2.9B**: CircleStone Labs / Comfy Orgの2Bパラメータアニメ・イラスト特化テキスト-to-画像モデル（base v1.0など）。Anima-2.9Bはコミュニティ製のレイヤー拡張＋追加学習版（Hugging Face Gazingstars123/Anima-2.9B）で、ComfyUI-Anima-2.9Bカスタムノードが必要（ComfyUI本体にネイティブサポート追加済み例あり）。Danbooruタグ対応が強み。[[3]](https://www.reddit.com/r/StableDiffusion/comments/1vmauuv/release_anima29bpreviewv1_expanded_anima/)[[4]](https://docs.comfy.org/tutorials/image/anima/anima)
- **最適化ツール**: ComfyUI Kitchen attention、SageAttention、Turbo LoRAなどがH3の高速化に有効とされ、実際のユーザー報告で速度向上事例が確認される。[[5]](https://www.reddit.com/r/StableDiffusion/comments/1vl8wqw/comfyui_comfykitchen_attention_speed_up/)

（モデル名・バージョンは2026年8月時点の公開情報に基づく。スレッド内容と一致する実在の開発動向を確認。）
