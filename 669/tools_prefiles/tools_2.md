**抽出されたツール関連話題（モデル関連は除外）:**

- **ComfyUI（および関連パッケージ）**:
  - ComfyUI 0.27.0 + Python 3.12.12 + PyTorch 2.12.1+cu130環境でkrea2のint4convrotモデル使用時にshapeエラーが発生。int8convrotまでは動作するがint4は未対応。
  - **選ばれる理由**: int4/ConvRot（convrot_w4a4）サポートのため。リリース版では未対応のためgit pullが必要で、**comfy-kitchen 0.2.18**（最新版）と組み合わせることでNative ops（float8_e4m3fn, int8_tensorwise, mxfp8, nvfp4など）が有効化され、正常にロード・動作する。
  - RTX 50シリーズはint4非対応のためComfyUIではint8にフォールバック。RTX 20/30/40シリーズのみint4対応。
  - Comfy-Kitchenの更新（requirements.txt経由のpipインストール）がINT8_ConvRotの動作に必須。Portable版/Desktop版/Stability Matrixなどのパッケージでは自動更新の挙動が異なる。
  - 生成速度向上（int8化、sage attention、compile model、easy cacheノード併用）で素の半分程度まで短縮可能という報告あり。

- **Stable Diffusion WebUI系（Forge neo、Civitai Helper拡張）**:
  - Forge neoにanima edit拡張が来ている。
  - Civitai Helper拡張（Stable-Diffusion-Webui-Civitai-Helper-RED-UPDATEなどfork版）でRED参照先を切り替える方法。APIコード発行やfork版の選択でred/blueの参照先を制御。
  - **選ばれる理由**: モデル/LORA管理やCivitai連携を効率化するため。RED更新版はred参照に確実に対応。

**Qwenシリーズ関連**: 該当ログ内に画像生成以外のQwen話題はなし。

**その他**: nano-bananaなどの指定ツールの言及なし。ツール選択の主な動機は「特定精度（int4/int8/ConvRot）の動作安定性」と「バージョン互換性の確保」。