# 🆕 新規トピック（前回からの差分）
### モデル: 流行モデルの概要
- MiniMax H3が主流モデルとして圧倒的に議論され、高速化パッチ・高解像度動画生成・音声同期・NSFW実用性・ComfyUI最適化・5090環境での安定性が評価される。

### モデル: 主なモデルと選定理由（ログ抽出に基づく）
- MiniMax H3がログの中心で表現力・ref忠実度・自然な動き・音声対応・5090速度で突出し、sexgod LoRAやeasycache/sol_attenとの組み合わせが主流。
- 静止画生成ではH3動画制作の補完としてComfyUI-LoRA-Block-Filter運用やAnyTestノードが共有され、画風・キャラLoRAのブロック制御知見が蓄積。
- Wan（Wan2.2含む）はH3登場前は動きLoRAの調整しやすさが評価されたが、現在は比較対象として自然さや鏡写し表現で劣ると指摘され主流から後退。
- LTX（LTX-2.3）はWanと並びH3との比較で鏡写し表現の弱さが指摘される。
- NovelAI（NAI）は運用簡易化への期待として軽く言及される。
- sexgodモデルはH3とのNSFW組み合わせで動作再現性が高くTurbo LoRA併用例が多い。
- LLM系（Gemma-4、Grok、Deepseek）はH3ユーザーのプロンプト作成補助として無検閲・日本語対応で頻用される。
- ログ全体はH3中心の最適化議論が支配的で、他モデルは補完・比較として語られる。

### モデル: Web検索による参考情報
- MiniMax H3は2026年7月リリースのオープンウェイトマルチモーダルモデルで、2K・最長15秒動画のt2v/i2v/ref2va対応と音声生成に強く、Turbo版やComfyUI対応が進む。
- Wan2.2はAlibabaの2025年リリースMoE動画モデルで720p/24fpsのt2v/i2vとカメラ制御に優れ、4090などで動作。
- NovelAI（NAI）はAnime Diffusion V4.5を主力とするサブスクサービスで画質・忠実度・マルチキャラ対応が強化されている。
- 2026年8月時点の情報はログ内のH3実践議論と公式機能が一致する傾向が強い。

---
# 元の本文
**レポート：生成AIモデルに関する分析（ログ抽出結果に基づく）**

### 流行モデルの概要
複数のログ抽出結果から、**MiniMax H3（minimax h3 / H3 / MiniMaxH3）** が圧倒的に話題の中心であり、現在の主流モデルとして位置づけられている。選定理由として繰り返し挙げられるのは、**生成速度の高速化（Sage Attention系パッチ、Sol-Attn、T8 Cache、Block Cache、Turbo LoRAとの組み合わせ）**、**高解像度・動画生成（t2v/i2v/ref2va）での表現力・指示追従性・参照画像（ref）の忠実度**、**音声同期（リップシンク）の自然さ**、**NSFW（エロ生成）実用性**、**ComfyUIでの最適化しやすさ**である。特にRTX 5090などのハイエンド環境で実用的と評価され、低ステップでも動きの劣化が少なく、長い動画の継ぎ足し生成にも適する点が強みとして強調される。LLM（Gemma-4など）と組み合わせたプロンプト作成との併用も一般的。

その他のモデルは補助的または過去の文脈で言及される程度で、animaは静止画生成やキーフレーム用途、Wanは動き調整の過去事例として比較対象に挙がる。FLUX、Illustrious、NovelAI、LTXなどはヘッダー止まりまたは限定的な言及にとどまる。

### 主なモデルと選定理由（ログ抽出に基づく）
- **MiniMax H3**  
  ログ全体で最も活発に議論され、「一番表現力が高い」「限界が見えなさすぎる」との声多数。ref画像との相性が良く、着エロ〜本番までの自然な繋ぎや物理表現（例: ガラス押し付け）がLoRAなしでもある程度可能。音声生成対応や5090環境での速度が実用性を高めている。sexgod（sexgod0.3 / v3）などのNSFW向けLoRA/Turbo LoRAとの組み合わせが主流で、easycache + sol_attenなどの高速化パッチ検証も盛ん。弱点として、ref画像と初期ポーズの乖離時のキャラ再現度低下や背景POV時の不自然さが指摘されるが、全体として「現時点で突出している」との認識が強い。

- **anima**  
  静止画生成（特に元画像やキーフレーム用）でH3動画制作時に併用される事例あり。ComfyUI-LoRA-Block-Filter（LBW）での運用が詳細に解説され、画風LoRAは中間層を0にして汚染防止、キャラLoRAは中間層を残す推奨など、ブロック制御の知見が共有されている。AnyTestノード使用例もあり、絵柄再現性については評価が分かれるが、高品質な静止画素材として位置づけられる。生成速度面でのComfyUIアップデート言及も見られる。

- **Wan（Wan2.2含む）**  
  過去の文脈で動き（特に胸揺れ）のLoRA調整しやすさや強度制御が評価されていたが、H3登場後は比較対象として「LoRAなしでも自然に出るようになった」「鏡写し表現で劣る」などの指摘あり。手軽さや安定性は一部で認められるが、主流からシフトしている傾向。

- **その他のモデル**  
  - **FLUX（fl2）**: ref系とのワークフロー違いが軽く言及される程度。  
  - **Illustrious（リアス / ill / IL）**: 参照忠実度でanima AnyTestより優位との比較あり。ただし、新モデル（Z-Imageベース）の話題性が低く、コミュニティ対応のまずさが理由で敬遠される声も。  
  - **LTX（LTX-2.3）**: Wanと並んでH3との比較対象（鏡写しなどの表現で劣る指摘）。  
  - **NovelAI（NAI）**: 運用面倒くささ解消への期待値として軽く言及。  
  - **sexgodモデル**: H3とのNSFW組み合わせで動作再現性が高いと評価（Turbo LoRA併用例あり）。  
  - LLM系（Gemma-4、Grok、Deepseek）：プロンプト作成補助としてH3ユーザー間で頻出（無検閲・日本語対応・柔軟性が理由）。

全体として、ログはH3中心の最適化・ワークフロー議論が支配的で、他のモデルはH3の補完や過去比較として語られる。

## Web検索による参考情報
- **MiniMax H3**: 2026年7月31日頃にMiniMax社がリリースしたオープンウェイトの汎用マルチモーダル生成モデル。テキスト・画像・動画・音声を統合コンテキストで扱い、2K解像度・最長15秒の動画をネイティブステレオ音声付きで生成可能。t2v/i2v/ref2va/first-and-last-frameなどのワークフローをサポートし、指示追従性・参照忠実度・V2Vモーション転送に強い。Hugging Face（MiniMaxAI/MiniMax-H3）、fal.ai、Krea、Sogniなどで利用可能。Turbo版（4ステップ高速化）も存在し、ComfyUI対応が進んでいる。[[1]](https://www.minimax.io/blog/minimax-h3)[[2]](https://fal.ai/minimax-h3)[[3]](https://huggingface.co/MiniMaxAI/MiniMax-H3)

- **anima**: CircleStone LabsとComfy Orgの協力による2Bパラメータのテキスト-to-画像モデル（アニメ・イラスト特化）。ComfyUIネイティブサポートで、2026年時点でpreview/base版がHugging Face（circlestone-labs/Anima）で公開されており、1MP程度の解像度で30-50ステップ推奨。[[4]](https://docs.comfy.org/tutorials/image/anima/anima)[[5]](https://huggingface.co/circlestone-labs/Anima)

- **Illustrious XL（イラストリアス）**: OnomaAI Research（Illustrious Team）によるSDXLベースのイラスト特化モデル。v0.1（2024年）からv3.xシリーズへ進化し、アニメ・イラスト生成に強いプロンプト追従性が特徴。[[6]](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0)[[7]](https://www.illustrious-xl.ai/)

- **Wan2.2**: Alibaba（Wan AI / Tongyi Lab）によるオープンソースMoEアーキテクチャ採用の動画生成モデル（2025年7月頃リリース）。t2v/i2v対応、720p/24fpsでシネマティック制御が可能。消費者向けGPU（4090など）で動作し、動きの一貫性やカメラ指示への応答性が向上。[[8]](https://github.com/Wan-Video/Wan2.2)[[9]](https://docs.comfy.org/tutorials/video/wan/wan2_2)

- **NovelAI（NAI）**: サブスクリプション型サービスで、Anime Diffusion V4.5（2026年時点の最新版）が主力。V4シリーズで画質・忠実度が大幅向上し、マルチキャラクター対応なども強化。[[10]](https://novelai.net/updates)[[11]](https://novelai.net/v4)

これらの情報は2026年8月時点の公開情報に基づく。ログ内の実践的議論（特にH3の高速化・NSFW用途）と公式機能が一致する傾向が強い。
