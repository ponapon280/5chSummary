**抽出結果（ツール関連のみ）**

### ComfyUI（comfy）関連
- **バージョン・環境関連**
  - comfyui 2.13.0+cu130にしたらcomple model +がエラー出て動かない（988）
  - LMstudioとconfyuiは同時に使ったことはない（972）

- **ワークフロー・ノード関連**
  - トリ肉ネキのI2Iワークフロー（890, 903）
  - 公式のr2vワークフローのconditioningとsamplingを噛ませる（903）
  - ref2V / ref2vaワークフロー（872, 931, 945）
  - kijai版lightx2v + spectrum + block cache (T8) の組み合わせ（967, 971, 977）
  - Model Preview OverrideのStep time確認（971）

- **選ばれている理由・評価**
  - 参照画像・動画を扱う際の柔軟性が高い（conditioning/samplingの組み合わせでref2vを実現）
  - I2Iワークフローが強力で、Loraを多用しなくても高品質な結果が出せる
  - ノードを組み合わせることでプロンプト追従性や参照画像の制御が細かく調整可能
  - Turbo系（lightx2vなど）とblock cacheの併用で高速化しやすい

### LM Studio関連
- **使用例**
  - lmstudioでqwen3.6 35b a3bをGPUオフロード0にしてminimax int8を動かしている（904）
  - Gemma-4 26B MoEやGemma4 31b q4kmをプロンプト生成用に使用（972, 980）

- **選ばれている理由**
  - MiniMaxなどの動画生成ツール用のプロンプト作成に適している
  - ローカルLLMとして手軽に使える（特にプロンプト生成用途）
  - VRAMに乗り切らない場合でもオフロードで動作させられる

### その他
- **EasyWan22**：MiniMax H3のワークフローとして言及（962付近の次スレ修正案で言及）
- 全体的に「ComfyUIのワークフロー（特にref2v / I2I）」が圧倒的に多く、**参照画像・動画の制御性とカスタマイズのしやすさ**が選ばれる主な理由として繰り返し語られている。