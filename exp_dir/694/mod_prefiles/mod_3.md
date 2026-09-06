# モデル別話題抽出レポート

## NovelAI (NAI)
- **選ばれている理由**: 現状、二次画像生成において「神枠」であり、日本語で指示すればクロスオーバーや漫画的表現など何でもこなす。bananaやgptimageも不要なレベル。ただしイラストリアス（リアス）のようなポン出しには向かず、指示しないと描いてくれない点が挙げられる（>>533）

## illustrious（イラストリアス / リアス / ill / IL）
- NAIと比較される形で言及。NAIはリアスのようにポン出しには向かないと評されている（>>533）
- animaの文脈で、ILでは難しかった「逆フェラ」がanimaでは可能であることが評価されている（>>544）

## FLUX
- ログ内に該当する言及なし

## Wan
- minimax H3と組み合わせて使用される例が報告されている。エロに強いWan2.2の映像をカットインさせることで、エロいMVが自在に作れるとの感想（>>610）
- WanGPを使ってminimax（H3）を動かしているユーザーがいる。Pruned20Bで5秒の生成に約3分かかったという実測値が報告されている（>>513）

## Qwen-Image
- ログ内に該当する言及なし

## anima
- **選ばれている理由**: IL（イラストリアス）では難しかった「逆フェラ」がanimaでは可能であることが素晴らしいと評価されている（>>544）
- 動画生成環境の制約（SSD寿命への懸念）から「おとなしくアニマに浸る」という発言があり、animaを動画生成の代替・待機先用として位置づける向きがある（>>503）

## Z-Image（Z-Image Turbo / ZIT / ZIE）
- ログ内に該当する言及なし

## LTX（LTX-2.3 / ltx2.3）
- ログ内に該当する言及なし

---

## 補足：minimax H3（抽出対象外だが複数モデルの文脈で頻出）
- Wanと併用され、動画・LLM両面で使われている（>>579, >>610）
- WanGP上でPruned20Bを使用、5秒生成に約3分（>>513）
- Turbo mode（8step / 4step）や各種高速化パッチ（comfy kitchen attention、Spectrum Apply MiniMax H3、Patch Sol-Attn等）と組み合わせて使用（>>433, >>574）
- 「たった20GBのモデルで音声付き動画生成できるのはオーパーツじみている」と評されている（>>589）
- DeepLで翻訳したプロンプトをWanGP付属のEnhanced H3 Prompt機能で書き直して使用する手法が紹介されている（>>513）

---

## 抽出結果

### モデル関連話題

**MiniMax H3 / MiniMax-H3**
- WanGP上でPruned20Bを5070ti/32GB環境で実行した際は動作不安定だったが、64GBに増設してから安定した。グラボ側は58GBしか使っておらず、肝心なのはメモリ。動画参照なしの5秒生成で約3分かかった（>>513）
- 楽曲駆動テストを行い、元の楽曲をそのまま使ったサウンド駆動が可能。自然な人物の動きやカメラワークを取り入れたMV制作に使える。NSFWだと怪しい部分もある（>>610）
- AMD環境・Intel環境でも問題なく動作し、CUDAの壁は実質的にプログラマーが脳死で選んでいるだけになっている（>>502）
- minimaxfastを導入し、kitchenとsol有効で通常版H3turbo4stepと比較したが大して変わらなかった（>>574）

**Gemini（GPT-6 Astra）**
- ChatGPT PlusでGPT-6 Astraが使える環境になったが、Codex限定（>>613、>>536、>>563）
- 同じメイドアリスの画像を与えて一撃で3D造形を出力し、Sol最大で10回リテイクした結果を上回るレベルで作り込んできた（>>617、>>631）
- Astra最大でBlenderによるバストアップ造形を一発生成。5時間リミットも一撃で消費した（>>617）
- フロンティアベンチマークが加算された結果、Geminiが逝く（>>566）
- 応答が淡白になったという報告あり（>>576）
- エロ用途だとかなり劣化している（>>551）

**MiniMax H3 VAE**
- vae_nameをminimax_h3_video_vae_int8_convrot.safetensorsに設定して使用（>>433）

**MiniMax H3 関連ノード・高速化設定**
- Turbo mode（8step）、ModelAttentionBackend（attentionをcomfy kitchen attentionに）、Spectrum Apply MiniMax H3、Patch Sol-Attnを適用（>>433）

**gemma4 26B**
- VRAM16GB環境での最適解として選択。動画プロンプトのエロ会話を作らせているが物足りないとの評価（>>579）
- 選定理由：VRAM16GBでなんとか我慢できる環境においての最適解のため（>>579）

### ハードウェア関連話題（参考）

**AMD DGX Station（Instinct MI350P搭載）**
- HBM3e 576GB、96-core Threadripper PRO 9995WX、16TB/s帯域、2TB DDR5（>>442、>>443）
- 価格は1500-2000万円程度と推測（>>491）

**Mac M5 Ultra 80C / 512GB**
- Stable Diffusion(SDXL 1024×1024)で約1.2数秒/枚。reForgeやComfyUIは動作するとのAI回答（>>466）
- M5世代以降はGPUにfp16アクセラレーターが搭載され、RTX2000世代あたりに追いつく水準。Metal（CUDA相当）の整備も進んでいる（>>478、>>497）
- 画像・動画生成が第一目的ならNVIDIAシリコンが圧倒的。ゲームのついでならMacもアリ（>>603）

### 除外したモデル・ツール
- NovelAI、illustrious、FLUX、Wan、Qwen-Image、anima、Z-Image、LTXは除外対象のため記載せず（ただしWan2.2は>>610でMiniMax H3と組み合わせて言及されている文脈あり）