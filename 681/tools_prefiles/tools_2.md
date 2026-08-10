**抽出されたツール関連の話題（モデル名は除外）**

### ComfyUI / Comfy 関連
- **ComfyUI Managerの消失問題**  
  ComfyUIを最新版に更新したらManagerが消えたという報告。起動オプションに `--enable-manager` を付けないとManagerがロードされなくなったという指摘あり。

- **ComfyUIのアップデートによる高速化**  
  ComfyUI更新で生成速度が向上した事例が複数（例: Anima使用時に1024解像度30ステップで24s→19s、さらにint8convrotやspectrum適用で8sまで短縮）。長尺動画生成時のVRAM溢れ対策として `low vram attention` + `chunk feedforward` を有効にすると4時間かかっていた処理が1時間弱に短縮された報告。

- **その他のComfyUI設定・最適化**  
  - `--fast-disk` オプションの使用（DRAMを圧迫しないための設定）。
  - `ref_image_size` の設定が参照画像・動画に反映される挙動。
  - 動画参照時のリサイズ（0.6MP程度に縮小）で大幅に速度改善（174s/it → 25s/it）。

### Sage-attn / SageAttention 関連
- **Qwen-Image特有の問題**  
  `sage-attn` 有効時にQwen-Image / Qwen-Image-EditでSamplerが延々回り続けて終了しなくなる不具合が報告。他の生成モデルではこの現象は確認されていない。

- **高速化としての評価**  
  SageAttentionを有効にすると速度が大幅に向上する一方で、他の高速化手法（Spectrum、TurboLoRAなど）と比べて劣化が少ないという声あり。「質を重視する場合はSageAttention以外をオフにする」という使い分けの言及も。

### AntiGravity 関連
- **用途と評価**  
  自作アプリの保守作業に使用。エロ動画の生成・評価まで一貫して行える点が便利とされ、「チャッピーよりエロ評価がストレートで使いやすい」という理由で選ばれている。

### その他のツール・設定関連
- **ROCm対応**（AMD GPU向け）  
  RX 9060XT / 9070XTを購入し、ROCm対応を待っているという報告。

- **GPU関連のツール・環境構築**  
  - 複数GPU接続のためのライザーケーブル + PCIeスプリッターの検討（マザーボードのレーン分割対応が必要）。
  - VRAM16GB環境での挙動確認（プルーン版と通常版の生成時間差がほとんどないという報告）。

**抽出除外の理由**:
- Anima、H3、MiniMax、WAN2.2、FLUX、NovelAIなどの**モデル名**に関する記述はすべて除外。
- Qwen-Imageについては画像生成に関する部分のみ除外し、Sage-attnとの組み合わせ不具合についてはツール側の問題として抽出。