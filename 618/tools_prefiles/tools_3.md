### 抽出されたツール関連話題（モデル話題除外）

以下はログから生成AI（主に画像生成関連）の「ツール」（ComfyUI, A1111, webUI, SUPIR, nano-bananaなどインターフェース/拡張/ノード/ワークフロー類）に関する話題をすべて抽出したもの。モデル名（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）の言及を含む投稿でも、ツール部分のみを抽出・記述。ツール選択理由が明記されている場合を強調。

- **528 >>495**: CFGガイダー（左）とmultimordal（右）の比較。multimordalはpromptに忠実/音に忠実の調整可能が売り。生成時間: CFGガイダー60秒、multimordal140秒（10step）。

- **530 >>522**: sam3で検出（複数対応）。

- **540**: civのworkflow（sampler→detailer→×0.5→×4→sampler）。最後にdetailerより全体統一感が良い。途中のアプスケは×2で十分か？と疑問。

- **541 >>540**: アップスケーラーが基本x4のため×0.5で調整。情報量減を避けるためx4→x0.5の順。

- **542**: アップスケールモデルが4倍のため結果2倍にするために0.5。

- **543**: LanczosResizeノードでの２倍拡大（アプスケ意図不明、超解像か？）。

- **544**: Detailer→UltimateSDUpscaleが良いのでは。

- **545**: Upscale Image (using Model)を使わずUpscale Image Byだけでx4→x0.5は謎。

- **546 >>544**: UltimateSDUpscale/tiled diffusionはVRAM不足時。VRAM十分ならUpscale Image (using Model)→KSampler。

- **547**: アプスケ過程で使うモデルにより変わる。

- **549 >>540**: PatchModelAddDownscale (Kohya Deep Shrink)。最初にダウンスケールで細かい線/チリの乱れ消え、アップスケ後全体整う（deep shrink効果）。

- **550 >>465**: comfyuiで既に動く（共同開発）。

- **553**: アプスケもcomfyUIだと自由度高すぎて正解不明。1girl+αなら基本解像度1.5MPXで十分、detailerあり。

- **558**: Managerで検索するとGradientDeepShrinkのみ（オリジナルのDeepShrinkなし）。

- **560**: CoreにPatchModelAddDownscale (Kohya Deep Shrink)入ってるか？

- **579 >>562**: PatchModelAddDownscaleの理解: 大画像生成時、ステップ始めに小サイズ生成で全体決め、途中から元サイズに戻し速度UP/破綻防ぐ。

- **581**: PatchModelAddDownscale（SDXLで効果確認、Z-Imageでは変化なし）。

- **584 >>562**: PatchModelAddDownscaleのパラメータ説明（ブロック番号、ダウンスケール係数、開始/終了パーセント、スキップ後のダウンスケール、ダウンスケール/アップスケール方法）。ワイは雰囲気で使用、Lanczos好きだが選択肢なし。

- **585 >>581**: Z-Imageのblock_numberデフォルト適用可か？（ブロック構成理解必要）。

- **588**: forge系についてるkohya hrfixと同じ機能？

- **597 >>588**: forge系kohya hrfixのComfyUI移植版っぽい。

- **601**: comfyでLECO使えんか？

- **609**: ComfyUIアプデでZ-Imageも神メモリ管理効く、MultiGPU不要に。

- **614**: AnimaのデフォWFでサンプラーer_sdeだが、euler_ancestral崩れにくい（比較画像）。

- **617 >>616**: diffusion-pipeがCosmos対応（Windowsで面倒）。

- **642**: musubi-tunerのプロンプトでmd形式（LoRA作成テスト、プロンプトファイルtxt/md）。

- **646**: easywanのWFとsmoothmixの公式WF比較（easyの方が人物生き生き）。新規環境でeasyWFのmissingノードがManagerで見つからず。

- **657**: VNCCSとQIEでカメラアングル変更（生成48分）。

- **663 >>660**: オプティマイザーCAMEでキャラLoRA30分。

- **664 >>660**: キャラLoRAは2000-3000ステップで30分-1時間。

- **666 >>662**: civitaiのSlider Lora。

- **668**: RAdamSchedulerFreeで500ステップ10分（5090）。

- **683**: ComfyUI_VNCCS（Visual Novel Character Creation Suite、ComfyUI拡張で一貫キャラスプライト作成）。

- **696**: facedetailerでキャラ再描画（WF: sdxl→z-image背景→FLUX.2馴染ませ→facedetailer。FLUX.2のライティング制御有能、NSFW入力でもキャラ触れず可）。

**ツール選択理由の抽出まとめ**:
- **ComfyUI**: 自由度高（アプスケ/WF）、メモリ管理向上でMultiGPU不要（>>609）、共同開発で即対応（>>550）、拡張豊富（VNCCSなど>>683）。
- **PatchModelAddDownscale (Kohya Deep Shrink)**: ダウンスケールで乱れ消え全体統一（>>549）、速度UP/破綻防ぐ（>>579）、SDXL効果大（>>581）。
- **UltimateSDUpscale/tiled diffusion**: VRAM不足時専用（>>546）。
- **Upscale Image (using Model)/KSampler**: VRAM十分時（>>546）。
- **diffusion-pipe**: Cosmos対応でLoRA組める（>>617）。
- **Manager**: missingノード検索（>>646, >>558）。
- **facedetailer**: 精細感UP/再描画（>>696）。

これらはログ全体でComfyUI中心の議論が多く、A1111/webUI/SUPIR/nano-banana等の明言なし。他ツール（CFGガイダー/multimordal/sam3等）はComfyUIノード/WF拡張とみなし抽出。