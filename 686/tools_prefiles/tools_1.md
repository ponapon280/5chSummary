**ツール関連の話題抽出（モデル除外）**

以下、ログから**ツール**（ComfyUI系、MiniMax H3の機能・ワークフロー、Krea2、Comfy Kitchen、upscaler/refiner関連など）に関する記述のみを抽出しました。モデル名（anima、NAI、FLUX、Wan、LTXなど）は除外しています。

### ComfyUI / Comfy関連
- **Comfy Kitchen（kitchenattn / Sol-Attn実装）**
  - Comfyでよく使う行列演算をC++/CUDAやROCmで最適化したGPUカーネルライブラリ。
  - 最新版ではconvrot用のint8も入っており、速度向上に寄与。
  - 理由：Spectrumや低ステップLoRA以外で明確に時間短縮を実感できるため。Sage Attention以外を使わなくなったという声も。
- **--fast-disk / pinned memory設定**
  - `--fast-disk`は時間はかかるが、RAM使用量を大幅に抑えられる（RAM40GB近く節約した報告あり）。
  - pinned memoryは生成が1-2割遅くなるが、ピクセル上げや長尺生成が可能になるメリットがある。
  - 理由：RAM32GB環境でもContext Loopを動かせるようになったため。低スペック勢がH3を楽しめるようになった要因。
- **ComfyUIのRAM管理・最適化**
  - 公式テンプレ止まりだと思っていたRAM32GBでもContext Loopが動いた。
  - 起動オプションでRAM使用量が劇的に減った事例あり。
  - 理由：低スペック（RTX4060Ti、5070Ti、5060Ti16GBなど）でも実用可能になった。

### MiniMax H3（MMH3）関連ツール・機能
- **Context Loop**
  - シーン追加時に「Approve&continue → エディタでシーン追加 → 実行」が推奨されるが、シーン1からやり直しになる不具合報告あり。
  - 修正方法として「新しく追加したいシーンの番号に変える」「WFとリポジトリURLをチャッピーに投げる」とのアドバイス。
  - 理由：5秒でも15秒でも動画を繋げてもVRAM/RAM使用量が変わらないため、無限に繋げられる点が評価されている。
- **Extender**
  - Context Loopより扱いやすいという声あり。
- **Upscaler / Refiner / Latent Upscale**
  - H3のアプスケはRefineで回す部分が遅いため手が出しにくい。
  - Latent Upscaleは時間増大がネックだったが、LTXの技術転用で改善されたという言及。
  - 理由：高解像度時の時間短縮目的。
- **LoRAの扱い**
  - 既存の動作系LoRAは細かい動作プロンプトとバッティングして奇形が出やすい。
  - H3の2D Anime Style NSFW LoRA（手コキ&フェラ特化）などの言及。

### Krea2関連
- Krea2をメインに使用し、細部の細かさを重視。
- MiniMax H3との組み合わせが非常に相性が良いと複数で評価。
  - 理由：pony+LTXから数段階引き上げてくれた、リアル・アニメ両方で強い、プロンプトが自然言語（日本語）で通じるためラク。
- Krea2 identity editは衣装・表情の差分作成向きで、自由な動きはMinimax H3の方が向いているという比較。

### その他のツール・ワークフロー関連
- **nano-bananaフォルダ**：ComfyUIの画像出力フォルダに「cc_nanobanana」が毎回強制生成される現象の報告（WFにファイル名指定が入っている可能性）。
- **カメラモーションサンプル動画**：ニキが作ったと思われるサンプルが消えたため、再アップを希望する声。Wiki掲載目的。
- **t2v / i2v / r2vの使い分け**
  - ぐちゃぐちゃになるのを避けるために「i2vを使う」「カメラを動かさない」というTips。
- **Turbo4step / Turbo8step**
  - 音声付きの比較実験（標準20stepとの比較）が行われていた。

### 選ばれている主な理由のまとめ
- **速度・安定性**：Comfy Kitchen、Spectrum、Sol-Attnなどの最適化で生成時間を短縮。
- **低スペック耐性**：RAM32GBや4060Ti/5070TiクラスでもContext Loopや長尺生成が可能になった。
- **相性**：Krea2 + MiniMax H3のタッグが特に強く評価されている。
- **操作性**：自然言語プロンプトが通りやすい、差分作成がしやすいなどの実用性。

モデル（anima、FLUX、Wan、Qwenなど）に関する記述は一切除外しています。