# 🆕 新規トピック（前回からの差分）
### スレッド概要
- 2026年8月頃のなんJ「なんJNVA部」スレッドでMiniMax H3のローカル運用・ComfyUIワークフロー・高速化・NSFW動画生成が活発に共有され高評価

### モデル性能と生成品質
- MiniMax H3はマルチモーダル動画生成モデルでI2V/T2V/ref2vに強く、キャラ一貫性・構図制御・リップシンクに優れる
- ref画像多用で背景・シーン一貫性が向上し、低解像度でも実用レベル、1フレーム推論や衣装変更などの応用例が共有された

### ワークフローと高速化技術
- ComfyUIが主流でサブグラフとKJノードが多用され、主な高速化パッチが複数共有された
- Memory Efficient Sage Attention Patch
- Patch Sol-Attn
- Spectrum Apply MiniMax H3 / H3 Cache
- EasyCache / BlockCache
- SpectrumはEasyCacheより品質劣化がマイルドで、Sol-AttnはSage Attentionと共存可能
- 生成時間は大幅短縮されるが音声劣化とのトレードオフがあり、Preview overrideやRIFE・Mel-Band RoFormerも活用された

### NSFW・検閲関連
- エロ特化需要が高くSexGod / Naughty Times LoRAやPinkFluffyBunnyが話題になり、Civitai削除後のtorrent共有やウイルス詐欺への警戒が共有された
- MiniMax公式のNSFW検閲解除モデル取り締まりに対し「逃さずにチェック」との声が多く、Grok活用プロンプトや隠語LoRAが検閲回避策として報告された
- 胸のサイズ制御（特に貧乳）は通常プロンプトが効きにくく、ref画像複数枚で明示指定する手法が共有され、エロ特化モデルは発展途上との見方が主流

### ハードウェア要件と運用
- 推奨スペックはRAM 64–128GB・VRAM 24GB以上で、RTX 4070Ti/5070Ti/5090での報告が多い一方、3060 12GBでもパッチ適用で動作可能
- 低スペック（VRAM 8–16GB + RAM 32GB）でもpruned int8 convrotやpinned memory/blockswapで動作するが生成時間は大幅増
- メモリ不足時のSSDスワップ負荷、CUDA/PyTorch/Triton/SageAttentionのバージョン相性、5090品切れ懸念が注意点として挙げられ、クラウド利用やBTO情報も共有された

### コミュニティ・配布の動き
- Civitai削除に対抗したtorrent共有が活発で著名作者のLoRA公開自粛傾向も指摘され、静止画派 vs 動画派の温度差はあるが全体として高評価
- 「低スペックでも時間と忍耐で可能」という声があり、技術共有の密度は高い

### 総評
- スレッドはMiniMax H3の実用化フェーズを象徴し、無検閲エロ動画生成の優位性と高速化ノード検証が中心で、音声品質・細かい制御・リソース要件で試行錯誤が続いている
- RTX 50シリーズ＋大容量RAMが当面の最適解として認識され、情報が日々更新される活発な技術検証スレッド

### Web検索による参考情報
- MiniMax H3は2026年7月31日頃にMiniMax社がリリースしたオープンウェイトマルチモーダル動画生成モデルで、最大15秒・2K・ネイティブステレオ音声に対応しComfyUIにday-zeroサポート
- ComfyUIコミュニティではSage Attentionなどの最適化パッチが活用され、RTX 3060などの低スペックGPUでも動作可能との報告が多い
- NSFW関連LoRA（SexGod系など）はCivitai上でコミュニティ作成・共有されており、削除や代替配布の動きは過去事例と一致する
- 検索結果は2026年8月時点の公開情報に基づき、スレッド内の具体的なLoRA名・パッチバージョンはコミュニティ独自の派生である可能性が高い

---
# 元の本文
**なんJ（5ch）スレッド要約レポート：MiniMax H3（ComfyUIローカル動画生成）**

### スレッド概要
2026年8月頃のなんJ板「なんJNVA部」スレッドは、**MiniMax H3**（特にref版やfl2va/int8/convrot版）のローカル運用を中心に、ComfyUIワークフロー構築・高速化・NSFW動画生成の実践報告が活発に共有された。全体のトーンは非常に高評価で、「Sora2がローカルに来た」「2026年のゲームエンド級」との声が多く、生成品質・プロンプト追従性・エロ表現の自由度に興奮が集中。一方で高スペック要件や検閲回避の課題も繰り返し議論された。

### モデル性能と生成品質
MiniMax H3はテキスト・画像・動画・音声入力に対応したマルチモーダル動画生成モデルで、I2V/T2V/ref2v（参照画像/動画）が強く、キャラの一貫性・構図制御・リップシンクに優れる。ref画像を多用することで背景・シーン一貫性が向上し、公式プロンプトガイド準拠で動作・口パク・画質が安定。低解像度（0.4–0.5MP、5–15秒）でも実用レベルに達し、1フレーム推論や衣装/ポーズ変更などの応用例も共有された。

4step（turbo LoRA） vs 8stepの比較では、4stepは高速だがノイズが強く、8stepで画質が回復する傾向。ref版は画質・制御性で通常版を上回り、「ref版しか使わない」ユーザーも多い。既存モデル（Krea2、Wan2.2、LTXなど）と比べて構図力・追従性が優位と評価された。

### ワークフローと高速化技術
ComfyUIが主流で、サブグラフ活用やKJノードが多用。主な高速化パッチの組み合わせは以下の通り：
- Memory Efficient Sage Attention Patch
- Patch Sol-Attn
- Spectrum Apply MiniMax H3 / H3 Cache
- EasyCache / BlockCache

SpectrumはEasyCacheより品質劣化がマイルドとされ、Sol-Attnは最新更新でSage Attentionと共存可能。生成時間は大幅短縮（例: 4割削減報告）されるが、音声劣化とのトレードオフが指摘された。Preview override（taeh3.safetensors）でガチャ効率向上、RIFEやMel-Band RoFormerによる音声分離・フレーム補完も活用例多数。

プロンプト作成ではGemma4 12BやQwen3.5 4Bに公式ガイドをシステムプロンプトとして与える手法が定着。音声付き生成の需要が高く、肉体接触音などの再現性が今後の課題とされた。

### NSFW・検閲関連
エロ特化需要が非常に高く、「エロ生成機に100万円」との表現も登場。SexGod / Naughty Times LoRA（int8で34–40GB規模）やPinkFluffyBunnyが話題になったが、Civitai削除後にtorrent共有が活発化。「NSFW LoRAをウイルス偽装した詐欺」への警戒も複数見られた。MiniMax公式のNSFW・検閲解除モデル取り締まり方針に対し、「逃さずにチェック」との声が多かった。検閲回避策としてGrok活用プロンプトや隠語的LoRAが報告された。

胸のサイズ制御（特に貧乳・flat chest）は熱い議論点で、通常プロンプトが効きにくく、ref画像複数枚（アニメ系含む）で明示的に指定する手法が共有された。全体として「エロ特化モデルはまだ発展途上」との見方が主流。

### ハードウェア要件と運用
推奨スペックは**RAM 64–128GB**（96GB以上推奨）、**VRAM 24GB以上**（できれば48GB+）。RTX 4070Ti/5070Ti/5090での報告が多い一方、3060 12GBでもパッチ適用で動作可能（解像度・動画長に制限）。低スペック（VRAM 8–16GB + RAM 32GB）でもpruned int8 convrotやpinned memory/blockswapで動作するが、生成時間は大幅増（例: 3070で0.4MP 10秒＝14分程度）。

注意点として、メモリ不足時のSSDスワップ負荷、CUDA/PyTorch/Triton/SageAttentionのバージョン相性、5090の品切れ・値上げ懸念が挙げられた。クラウド（Paperspace、runpod A100）利用の声も。BTO（PC工房）で5090搭載機の情報共有もあった。

### コミュニティ・配布の動き
Civitai削除に対抗したtorrent共有が活発で、「消せば増える」の古いインターネット法則が再現。著名作者のLoRA公開自粛傾向も指摘された。静止画派 vs 動画派の温度差はあるが、全体としてMiniMax H3のクオリティに興奮するユーザーが多数。「低スペックでも時間と忍耐で可能」という声もあり、技術共有の密度は高い。

### 総評
スレッドはMiniMax H3の実用化フェーズを象徴する内容で、特に**無検閲エロ動画生成**における優位性と高速化ノードの組み合わせ検証が中心。性能は高く評価される一方、音声品質・細かい制御（NSFW含む）やリソース要件で試行錯誤が続いている。情報が日々更新される活発な技術検証スレッドとなっており、RTX 50シリーズ＋大容量RAMが当面の最適解として認識されている。

---

## Web検索による参考情報
- **MiniMax H3**は中国のMiniMax社が2026年7月31日頃にリリースしたオープンウェイトのマルチモーダル動画生成モデル。テキスト・画像・動画・音声入力を統一的に扱い、最大15秒・2K解像度・ネイティブステレオ音声出力に対応。ComfyUIにday-zero（リリース当日）でネイティブサポートされ、Image-to-Video、Text-to-Video、Reference-to-Videoワークフローが充実している。[[1]](https://www.minimax.io/)[[2]](https://www.minimax.io/blog/minimax-h3)[[3]](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)
- ComfyUIコミュニティではSage Attentionなどの最適化パッチが活用され、RTX 3060などの比較的低スペックGPUでも動作可能との報告が多い。[[4]](https://www.youtube.com/watch?v=dgts0wG3kh0)[[3]](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)
- NSFW関連LoRA（SexGod系など）はCivitai上でコミュニティ作成・共有されており、削除や代替配布の動きは過去の類似事例と一致する。[[5]](https://civitai.com/user/sexgod1979)

（検索結果は2026年8月時点の公開情報に基づく。スレッド内の具体的なLoRA名・パッチバージョンはコミュニティ独自の派生・最適化である可能性が高い。）
