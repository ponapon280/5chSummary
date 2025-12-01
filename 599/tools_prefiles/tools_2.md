### 抽出された「ツール」に関する話題一覧

ログから生成AI関連の**ツール**（ComfyUI/comfy, A1111, webUI, SUPIR, nano-bananaなどUI/ノード/拡張ツール類）の言及をすべて抽出。**モデル関連（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）は完全に除外**。ツール選択理由が明記されているものは太字で強調。

#### ComfyUI (comfy)
- **246**: 「完璧なワークフローが配布されればcomfyuiでもそんな苦労せんのやないか？ でもアプデのたびにシンボリックリンクを配置し直して他人のモデル階層とかを自分のやつに変更せなあかんからやっぱしんどいは」  
  → **ComfyUIの理由**: アプデ時のシンボリックリンク再配置が面倒でしんどい。
- **273**: 「z-image使うだけならComfyUIを最新にアプデしてここに書かれている通りにやるだけの超絶簡単実装やで モデルをダウンロードしてフォルダに置いてWFドロップするだけ」  
  → **ComfyUIの理由**: Z-Image使用が超絶簡単（最新アプデ→WFドロップだけ）。
- **276**: 「とっくにcomfy公式がWFもモデルもTEもVAEも用意しててダウンロードして動かすだけやのに何言うてんねん」  
  → **ComfyUIの理由**: 公式がWF/モデル/TE/VAEを用意済みでダウンロード&動かすだけ（簡単）。
- **277**: 「comfyuiにアプデが予めあって LoRA訓練方法も迅速に出てきて 開発陣がもう手慣れたもんやな」  
  → **ComfyUIの理由**: アプデが早く、LoRA訓練方法が迅速に出て開発陣の手慣れ感。
- **371**: 「ComfyUI内包のサンプルワークフローから自分の使い勝手がいいように改造」  
  → ComfyUIのサンプルWFを改造して使用。
- **380**: 「z-imageのためにcomfyuiアプデしてからz-imageでの生成時にたまにoomするなーって思ってたら 既存のフローでも生成繰り返してるとoomするようになっちまってた」  
  → ComfyUIアプデ後、VRAMリーク（OOM）発生。
- **382**: 「ComfyUI-DFloat11のフォーク版の開発者が活発だったんでそっちのノードで推論してみた」  
  → ComfyUI-DFloat11ノード使用（フォーク版推奨、オフロード対応）。
- **383**: 「z-imageが原因なのかComfyUIの最新バージョンが原因なのか分からんけど どんどんVRAM使用量が増えていってOOM起こすな」  
  → ComfyUI最新版でVRAM使用量増加&OOM。
- **385**: 「DFloat11のおさらいした 行列演算の直前に解凍され使用直後に破棄されるみたいや」  
  → DFloat11（ComfyUI関連ノード）の動作説明。
- **390**: 「z-imageで早速試した 少し計算コスト上がるとのことだけど速度差はほぼ無い感じやった フルロード動作時のVRAMは3GB減量出来て」  
  → ComfyUI-DFloat11でVRAM3GB減量（デメリットなし）。
- **434**: 「ComfyUIにvscodeみたいなマークダウン入力用のヘルパー欲しいな」  
  → ComfyUIへの機能要望（マークダウンヘルパー）。

#### Forge / reForge / Forge Neo / Forge Classic
- **242**: 「forge neoも対応してくるやろ」  
  → Forge Neoの対応期待。
- **248**: 「reforgeの改修もされてるからその時まで待つわ」  
  → reForgeの改修待ち。
- **274**: 「z-imageはforge neoで出来るって言うてるのに何をみとるんや？」  
  → **Forge Neoの理由**: Z-Image対応可能。
- **356**: 「>support Z-Image in Forge NEO」  
  → Forge NEOがZ-Imageサポート。
- **400**: 「別に問題ない pytorchとcudaのバージョンが古いと動かんけどComfyUIとかForgeNeoとかkohyaSSとかの有名どころは最新版をクリーンインストールすれば動く」  
  → ForgeNeoは最新クリーンインストールで50xx対応。
- **414**: 「WebUI A1111系だとreForge, Forge Classic / Neoは対応済み」  
  → reForge/Forge Classic/Neoが50xx対応済み（A1111系WebUI）。
- **436**: 「StabilityMatrixのreforgeは未だに更新すると環境ぶっ壊れる」「昨日入れたforge neo(classic)は普通に動いた」  
  → **reForgeの理由**: 更新で環境破壊（非推奨）。**Forge Neoの理由**: 普通に動作。

#### A1111 / WebUI
- **401**: 「WebUI A1111系だとreForge, Forge Classic / Neoは対応済み A1111はdevブランチなら対応済み、masterブランチやリリース版では未対応 Forge無印は未対応」  
  → A1111 devブランチ対応、master/リリース未対応。Forge無印未対応。古いcudaの手動アップデート必要。
- **414**: 同上（詳細）。

#### StabilityMatrix
- **414**: 「StabilityMatrixを使って新規インストールすればcu128以降を導入してくれる」  
  → **StabilityMatrixの理由**: 新規インストールでcu128以降自動導入（簡単）。
- **436**: 「ワイのStabilityMatrixのreforgeは未だに更新すると環境ぶっ壊れる」  
  → StabilityMatrix+reForgeで更新時環境破壊。

#### Kohya_ss / kohyaSS / kohya_ssgui
- **394**: 「1.5以来に重い腰を上げてkohya_ssguiたwai nsfw 15でLora作ってみたんだが40秒で生成されていたところがLora読み込むと3分以上かかってしまった」  
  → kohya_ssguiでLoRA作成（生成時間増加問題）。
- **400**: 「ComfyUIとかForgeNeoとかkohyaSSとかの有名どころは最新版をクリーンインストールすれば動く」  
  → kohyaSSは最新クリーンインストールで50xx対応。
- **401**: 同上。

#### nano-banana (banana君 / bananaちゃん)
- **387**: 「みんな飽きてきたのかbanana君軽いわ」  
  → banana君が軽い（動作良好）。
- **393**: 「NAIで作った健全なスク水画像をbananaちゃんでフォトリアルCG化」  
  → bananaちゃんでフォトリアルCG化。

#### Flash Attention2 / flashattn / flash attention2 / SDPA / spda
- **250**: 「導入して試しにspdaで動かしたらアホほど時間かかって草 flash attention2導入はちょっと調べただけやけど結構厄介そうやな」  
  → **SDPA/flash attention2の理由**: 時間かかる&導入厄介。
- **255**: 「今はflash attention2簡単にインスコできるで」  
  → **flash attention2の理由**: 簡単にインストール可能（venv activate + pip install whl）。
- **258**: 「flash attention2対応してないしまた考えなあかんか」  
  → 非対応問題。
- **264-265**: whlリンク集でビルド（bat使用、小一時間）。
- **268**: 「こっちのwhlの指定バージョンとあっちのwhlの指定バージョンが違ったりして、依存関係はほんまに面倒」  
  → whl依存関係面倒。
- **279**: 「Windows版のビルド済みwhlの配布もあるで」  
  → Windows用ビルド済みwhl配布。
- **280**: 「flashattnはバージョン合ったの入れてもなぜか複数ノード巻き込んで壊すからさっさと消した」  
  → **flashattnの理由**: バージョン合ってもノード破壊で削除。
- **293**: 「Flash Attention2使うと出力がおかしくなるからイマイチやな」  
  → Flash Attention2で出力異常。

#### LM Studio
- **281**: 「LLM・VLMはLM Studioに任せるのもええと思う 餅は餅屋らしくインスコするだけで全速力で動くで comfyとの連携も恐ろしく簡単」  
  → **LM Studioの理由**: インスコだけで全速力動作、ComfyUI連携簡単（餅は餅屋）。

#### その他のツール言及（マイナー/ノード類）
- **278**: 「FP8では動作しなくて(ノードの量子化の設定変えても同じエラー) これはチャッピーに聞いた感じ公式で対応したのが出ないと駄目」  
  → FP8ノード非対応、チャッピー（？）相談。
- **292**: 「BooruDatasetTagManagerでQwen3-VL-8B-NSFW-Caption-V4.5ダウンロードして自動キャプショニング始めてみたら、1画像当たり5分以上かかってくさ」  
  → BooruDatasetTagManagerで自動キャプショニング（遅い）。
- **316/336/367**: ComfyUI-QwenVL / ComfyUI_QwenVL（量子化対応、速度比較）。
- **382/384/385/390/439**: DFloat11 / ComfyUI-DFloat11（VRAM削減、bf16可逆圧縮、速度ほぼ同等）。
- **419**: 「AdamWScheduleFreeに変えたら半分の30分で終わる」「LR Schedulerはcosineとconstantのどっちがいいのか」  
  → LoRA訓練パラメータ（kohya系？）変更で高速化。

**抽出総括**: 主にComfyUI/Forge系がZ-Image対応の簡単さで人気。Flash Attention2は導入厄介&不安定で敬遠。Kohya_ssgui/A1111系はLoRA訓練/50xx対応で言及多め。理由は主に「簡単さ」「速度」「VRAM効率」「互換性」。