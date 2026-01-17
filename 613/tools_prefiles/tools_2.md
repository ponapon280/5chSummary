### 抽出された「ツール」に関する話題

ログから、ComfyUI（comfy）、Forge（Classic/Neo/reForge）、EasyReforge、Stability Matrix、A1111/webUIに相当しないが類似のインストールツール/ノード/ライブラリ（sageAttention、flash attention、triton、Google Translate Text Node、VFIノード、Patch Sage Attention KJ、Model Patch Torch Settingsなど）を「ツール」として扱い、生成AI環境構築・運用関連の話題をすべて抽出。モデル（Wan、Qwen、LTX2、GLM-image、QI25I2/ZITなど）の話題は除外。ツール選定理由が明示されているものは太字で強調。

#### ComfyUI関連
- **225**: flash attention導入検討。cu13のwhlなしでビルド試したらメモリ96GB食いPC落ち。**231**: whlあり（日本人公開）。**234**: ComfyUI-QwenImageLoraLoaderの作者。
- **226**: GLM-imageがComfyUI未対応。
- **236**: LTX2モデルロード時python落ち（ノードキャッシュ次第で回避）。sageAttention未導入者はtriton影響なし。
- **239**: GMFSS FortunaのVFIノードがWindows環境変数CUDA_PATH読み込みでToolkit必要。
- **241**: デスクトップ版わからずポータブル版に戻す。
- **247**: ComfyUI 0.9.1でWF動画処理遅い（7秒動画5分）。
- **249**: nvfp4用ComfyUIインストール手順（venv activate後、torch2.9.1+cu130、triton-windows、sageattention-2.2.0+cu130torch2.9.0.whl、flash_attn-2.8.3+cu130torch2.9.1.whl）。
- **254**: CU128環境は**SageAttentionあり推奨、CU130環境はSageAttentionなし+Tritonなし**（LTX2不安定対策）。**255**: ComfyUIポータブル版新規でtorch2.7.1→2.9.1+cu128+sageAttention導入。**WanVideo Torch Compile Settings**ノードエラーだが無効でwan2.2動作（改良点）。
- **256**: RTX30xx+cu?環境でsageattention有効で画像生成可。
- **263-264,266**: プログレスバー表示が重い（非表示可？100msポーリング？）。frontend迷走気味、assets/サムネイル（webp/mp4）重い、無駄機能指摘。
- **286**: ComfyUI公式テンプレでRAMオフロード自動（VRAM不足でもRAMあればOK）。全体不安定（止まる問題、アプデ待ち）。
- **287**: ComfyUI WFで720p5秒動画30秒（RTX5090）。
- **291-293**: **自然言語日本語→英語翻訳ノード**として**ComfyUI_Custom_Nodes_AlekPetのGoogle Translate Text Node**推奨（BuimeLaboは改行で翻訳不可）。
- **302**: ComfyUI WF詰まり箇所特定（got prompt後、LTXVPreprocess、LTXVImgToVideoInplace、カスタムサンプラー）。解像度/サイズ大で遅い。
- **329**: --use-sage-attention/--fastバグ疑い。**Patch Sage Attention KJ + Model Patch Torch Settingsで手動適用推奨（速度速い）**。fp16_accumulationはfp8モデルにも有効（内部fp16高速化）。Model Patch Torch Settingsは常時trueでOK。
- **336**: ComfyUI WFで動画ビットマップ展開/縮小後LTX2投入（解像度大でメモリ溢れ）。
- **337**: >>112のWF（ComfyUI？）猫箱接続可。
- **342-343**: I2V動画生成で**SVI（一貫性強いが融通効かず）** vs KJWF（意味不明）。SVIアップデート期待。
- **346**: **Wan/QIEならComfyUIが分かりやすい**（forge neo比）。
- **349**: easyreforgeでwan/PLV素材作成中だがComfyUIわからん。

#### Forge/Neo/reForge/EasyReforge関連
- **257**: **forge neoでZIT試すがRuntimeError（mat1/mat2 shapes）**。CLIPモデル間違い疑い。
- **284**: forge neo PNGinfoでcheckpoint/VAE/Text Encoder指定（Z-Image turbo画像）。
- **289**: EasyReforgeインストールエラー（torch==2.7.1+cu128ハッシュ不一致）。**requirements.txtの--require-hashes削除**（チャッピー/Geminiアドバイス）。RTX5000限定作業。
- **294,296,303**: EasyReforgeインストールエラー（ハッシュチェック）。Reforge_RTX50x0_PipTorch260Cu128.bat必要だったが今不要。**pip cache purge + --force-reinstallで治る印象**。
- **299**: PCクリーンインストール後EasyReforgeエラー→**StabilityMatrixでReforge/NEO導入**。
- **300**: NEO vs easyreforge（生成早い？）。
- **305**: **EasyReforgeは古いreForge/sageattention（1年近く前）**。**最新reForge/Forge Classic/Neo + sageattention + fp16 accumulationでEasyReforgeより12割速い**。
- **334**: forge neoインストール（Stability Matrix）。
- **344-346,350,352**: **Stability Matrixでforge neo/Classicインストールサクッと可（venv/torch2.8.0→2.9.1推奨）**。**EasyReforgeもReforge_Fast.batでsageattention（古い）使え速度数%差**。Python venv干渉なし。Python3.11.9推奨。
- **345**: easy reforgeインストールエラー対策（note掲載、対応ファイル上書き必要、手間）。

#### その他ツール/ライブラリ
- **233,237,238,244-246**: CUDA Toolkit不要（生成はPytorch CUDAランタイムでOK、LoRA作成/ビルド時に必要）。一部モデル良い。
- **249**: triton-windows, sageattention/flash_attn whlインストール（nvfp4用）。

**選定理由まとめ**:
- **速度/安定性向上**: SageAttention（CU128あり、CU130なし）、flash attention/triton、fp16_accumulation、Patch Sage Attention KJ + Model Patch Torch Settings（手動で速い）、Forge Neo/reForge最新版（EasyReforgeより12割速い、数%早い）。
- **インストール容易さ**: Stability Matrix（サクッと）、ポータブル版ComfyUI（新規移行早い）。
- **機能/互換**: Google Translate Text Node（BuimeLaboより改行対応良）、VFIノード（CUDA_PATH必要）。
- **エラー回避**: whl公開（flash attention）、ハッシュ削除/pip force-reinstall（EasyReforge）。