# 🆕 新規トピック（前回からの差分）
### 人気モデルの傾向と選定理由のまとめ
- NovelAI（NAI5含む）は検閲の緩さ・日本語台詞精度・画質の高さで漫画生成に安定し、有料・多様性低下が指摘される
- Wan（Wan3.0）は動画のエロ表現・液体・動きの一貫性・リファレンス扱いやすさ・30秒生成で評価が高い
- MiniMax H3は自然な動きと日常/エロの柔軟性・Ref2V/LoRA相性・ComfyUI最適化が強みでWanと互角以上とされる
- Krea2は複数キャラの混ざりにくさ・日本語セリフ・背景描写に強く、Danbooruタグ対応とLoRA作成の難しさが課題
- 全体傾向としてローカル運用しやすさ・無修正耐性・エロ実用性（動き・一貫性・日本語対応）が選択基準で、Turbo/クラウドは速度優先、ベースモデルは柔軟性優先

### 詳細：主なモデルの評価と理由（ログ抽出より）
- 言及最多のモデルは自然言語＋Danbooru語の柔軟性・キャラLoRA再現度の高さ・複雑シーン対応・LoRA軽量・VRAM効率が評価され、Turbo1.1はプロンプト追従性の低さが指摘される
- NovelAIは検閲緩さ・日本語台詞・漫画生成の安定性・画質の高さが理由で、有料・生成上限回復の遅さ・多様性低下が指摘されV5で背景透過・多キャラ強化が新機能
- Wanはエロシーン（汁物・動き）の強み・リファレンス活用・30秒生成が選定理由でI2Vはバギー気味のためR2V推奨
- MiniMax H3は自然な混ざり方・LoRA充実・RTX最適化・速度が評価され、Wan比でリファレンスや長尺の実用性が優位視される場合あり
- Kreaは多キャラ安定性・日本語対応・背景力で高評価で、ローカル対応の可否が今後の鍵

### Web検索による参考情報
- NovelAI V5は2026年8月頃リリースで日本語自然言語プロンプト対応・最大22体多キャラ・漫画ページ生成・透明背景・テキストレンダリング向上を特徴とし、サブスクリプション制
- MiniMax H3は2026年7月31日リリースのオムニモーダル動画モデルでテキスト/画像/動画/音声を統一扱い、最大15秒2Kネイティブステレオ音声・Ref2V/V2V/編集対応・商用意識・API提供
- Krea 2は2026年5月頃リリースでスタイル転送・美学制御・参照画像によるスタイル適用・moodboard対応を強みとし、Raw/Turboバリエーション・API/Civitai経由・LoRA対応

---
# 元の本文
**生成AIモデルに関するレポート（2026年8月時点のログ抽出に基づく）**

ログから抽出された話題の中心は、アニメ・イラスト調の画像生成（特にNSFW/エロ寄り用途）と動画生成です。**最も活発に議論され、選択されているモデルはAnima（特にTurbo系）とNovelAI（NAI/NAI5）**で、続いてWan（Wan3.0/Wan2.2）やMiniMax H3（動画）、Illustrious（リアス/IL）、Krea2が比較対象として頻出しています。FLUX、Z-Image、LTX、Qwen-Image系などは言及が少なく、主流とは言えません。

**人気モデルの傾向と選定理由のまとめ**:
- **Anima**：自然言語＋Danbooruタグの柔軟な併用が可能、キャラLoRAの再現性・複雑構図の安定性、LoRA作成のしやすさ、VRAM効率の良さが主な選定理由。Turbo系は速度と特定構図の安定感で評価される一方、プロンプト追従性や表現幅のトレードオフも指摘される。
- **NovelAI（NAI5含む）**：海外サービスゆえの検閲の緩さ（モザイク回避など）、日本語吹き出し・台詞の精度、画質の美しさが繰り返し挙げられる。有料である点や多様性の低下を指摘する声もあるが、漫画生成用途で安定感が高い。
- **Wan（特にWan3.0）**：動画生成でエロ表現（液体・動きの一貫性）の強み、リファレンスの使いやすさ、30秒生成対応が評価。エロ学習済み寄りの扱いやすさ。
- **MiniMax H3**：動画の自然な動き・日常/エロの境界の柔軟さ、Ref2VやLoRAとの相性、ComfyUI最適化が強み。品質はWanと互角かやや上との比較あり。
- **Illustrious（リアス）**：生成速度の速さ、既存LoRA資産の豊富さ、シンプルプロンプトでの安定性。一方、複雑構図や多キャラではAnimaに劣るとの声。
- **Krea2**：複数キャラの混ざりにくさ、日本語セリフ・背景描写の強さ、Raw/Turboの学習方針が評価。Danbooruタグ対応やLoRA作成のしにくさが課題。

全体の傾向として、「ローカル運用しやすさ（GGUF/ComfyUI対応、LoRA容易さ）」「無修正・検閲耐性」「エロ用途での実用性（動き・一貫性・日本語対応）」がモデル選択の大きな基準となっています。Turbo系やクラウドサービス（NAI）は速度・手軽さで、ベースモデルは柔軟性で選ばれています。

### 詳細：主なモデルの評価と理由（ログ抽出より）
- **Anima（本家/Turbo1.1/Turbo/Anima 2B/3.8B/oneObsessionAnima/Obsidian Archives）**  
  言及最多。選定理由として「自然言語＋danbooru語の柔軟性」「キャラLoRA再現度の高さ（少量素材でも高精度）」「左右非対称や複雑シーンへの強み」「LoRA作成の軽量さ」「VRAM効率」が具体的に挙げられる。Turbo1.1はリリース直後で「プロンプト追従性が低い」「1.0との差が分かりにくい」との声も。Base/Aesthetic/Turboのバリエーションが使い分けられている。

- **NovelAI（NAI/NAI5/NAIV5）**  
  検閲緩さ（海外サービスという点）が最大の理由。日本語台詞・漫画生成の安定性、画質の高さが評価。一方で有料、生成上限回復の遅さ、多様性の低下指摘あり。V5では背景透過や多キャラ強化が新機能として話題。

- **Wan（Wan2.2/Wan3.0/WAN-Animate-2）**  
  動画生成で「エロシーン（汁物・動き）の強み」「リファレンス活用性」「30秒生成」が選定理由。I2Vはバギー気味でR2V推奨との声。無検閲サイト経由でのエロ対応も。

- **MiniMax H3（MinimaxH3/MM H3）**  
  動画で「自然な混ざり方」「LoRA充実度」「RTX最適化・速度」が評価。Wanとの比較でリファレンスや長尺での実用性が優位視される場合あり。

- **Illustrious（リアス/IL）**  
  速度とLoRA資産の豊富さが強み。シンプル用途では安定するが、Animaとの比較で構図ガチャや多キャラ弱さが指摘される。

- **Krea（Krea2/Krea3）**  
  多キャラ安定性、日本語対応、背景力で高評価。ローカル対応の可否が今後の鍵。

その他（PixAI、SDXL/Noob系、Irodori-TTSなど）は補助的または言及薄め。ローカル運用時のGGUF対応や無修正出力の実用性が継続的な関心事です。

## Web検索による参考情報
- **Anima**：CircleStone LabsとComfy Orgの協業による2Bパラメータ規模のアニメ/イラスト特化T2Iモデル（Qwen3 0.6Bテキストエンコーダー + Qwen-Image VAE使用）。Danbooruタグと自然言語の混合対応が特徴。Base（柔軟性最大）、Aesthetic（画質安定）、Turbo（蒸留・高速、CFG 1・8-12ステップ推奨）のファミリー構成。公式Base v1.0は2026年5月15日リリース、Turbo v1.1は2026年8月24日頃Civitaiで更新。Civitai上でLoRA多数公開・利用可能で、ローカル（ComfyUI）運用に適する。[[1]](https://civitai.com/ecosystems/anima)[[2]](https://civitai.com/models/2458426/anima)[[3]](https://gigazine.net/gsc_news/en/20260515-anima-image-generation-ai/)

- **NovelAI（NAI Diffusion V5）**：2026年8月頃にV5（Full/Curated）がリリース。日本語自然言語プロンプト正式対応、多キャラ（最大22体）強化、漫画ページ生成機能、透明背景出力、テキストレンダリング向上などが特徴。海外サービスとして検閲が比較的緩やかで、NSFW用途でも人気。サブスクリプション制（Anlas消費）。[[4]](https://note.com/itsuki_ailab/n/n3b408b813f7a)[[5]](https://airmore.ai/ai-review/novelai-v5-review)

- **MiniMax H3**：MiniMax Researchが2026年7月31日リリースのオープン寄りオムニモーダル動画生成モデル。テキスト/画像/動画/音声を統一コンテキストで扱い、ネイティブステレオ音声付き動画（最大15秒・2K）を生成。Ref2V、V2V、編集対応が強く、商用ユースも意識。API提供（従量課金）で、ComfyUIなどローカル/ワークフロー統合例も見られる。[[6]](https://www.minimax.io/blog/minimax-h3)[[7]](https://platform.minimax.io/docs/guides/video-generation)

- **Krea 2**：Kreaが2026年5月頃リリースの自社開発ファウンデーションモデル（Medium/Large/Turbo variants）。スタイル転送・美学制御に強く、参照画像によるスタイル適用（強度調整可能）、moodboard対応。Raw（学習用・高柔軟性）とTurbo（高速蒸留）の組み合わせが推奨される。APIやCivitai経由で利用可能で、LoRA対応も。[[8]](https://www.krea.ai/blog/krea-2-image-model)[[9]](https://github.com/krea-ai/krea-2/blob/main/README.md)

- **Wan 3.0**：Alibaba Tongyi Labの動画生成モデル（2026年8月頃パブリックβ）。最大30秒ネイティブ生成、ドキュメント/PDF/ウェブページ入力対応（文書→動画）、Omni-Reference（最大20件）が特徴。Alibaba Cloud Model StudioやQwen Cloud経由で提供。[[10]](https://morphic.com/resources/models/wan-3-0)[[11]](https://the-decoder.com/alibabas-wan3-0-generates-ai-videos-up-to-30-seconds-long-from-text-images-and-documents/)

これらの情報はログの文脈（特にAnimaのTurbo1.1リリースやNAI5の漫画機能、H3/Wanの動画比較）と一致しており、2026年夏〜秋にかけての更新が活発です。詳細はCivitai、公式サイト、Alibaba Cloudなどで最新確認を推奨します。
