**抽出結果（ツール関連のみ）**

### ComfyUI（comfy）
- **言及内容**:
  - sd-scriptsの新機能（素材強度指定）を試す際に、GUIツールが未対応だったためTOMLファイルを作成し、GUIから出力したコマンドを改変して直接コンソールで実行した。
  - Anima関連のWorkflow（WF）が3つテンプレートとして追加されている（Image Inpainting、Depth Control to Image、Any Control to Image）。
  - Krea-2 Int8用のImage Style Reference WFもある。
  - サーバー運用向きで、ウェブアプリとして動作するためメインPCからリモートアクセスしやすい。
  - Mage-flow対応が来た。

- **選ばれている理由**:
  - ウェブアプリ仕様なのでサーバー立てて遠隔操作しやすい。
  - Workflow（WF）が豊富で、Animaとの組み合わせがしやすい。
  - Dockerとの相性が良く、環境構築・再現性が高い。

### Forge / EasyForgeNeo（Automatic1111系webUI）
- **言及内容**:
  - EasyForgeNeo（for Anima）を更新した際、Anima Edit Loraの使い方（`<lora:AnimeEditV2:1:1>`のような二重強度指定、Diffusion in Low BitsをAutomatic(fp16 LoRA)に設定）。
  - Denoising Strengthを1.0にすると良いという情報共有。
  - forge coupleが効きにくいという指摘あり。

- **選ばれている理由**:
  - Animaとの相性が良く、LoRAの強度調整（Text Encoder / UNet）が細かくできる。
  - Low Bits設定でプロンプトの効きが良くなる。

### その他のツール
- **OneTrainer**: Krea2のLoRA作成に使用。Hugging Faceキャッシュの重複ダウンロード問題が発生した事例あり。
- **DrawThings**: HTTP APIサーバー機能があり、スマホから画像生成できるWebUIを自作可能。
- **Kohya_lora_param_gui**: LoRA作成ツールとして言及（有料note記事化されている事例あり）。

### 環境・運用関連ツール
- **Linux + Docker / WSL2**:
  - 画像生成ツール（特にComfyUI）をサーバー運用する場合に推奨。
  - 機械学習コードの再現性が高く、Docker指定が増えている。
  - CLIに慣れればリモート操作が容易で、メインPCとは別にAIサーバーを立てる使い方が一般的。
  - Windows GUIよりCLI中心の運用が安定しやすいという意見。

- **WSL2**: Windows環境でComfyUIを動かす際の選択肢として言及。

### 除外したもの
- モデル名（Anima、Krea2、FLUX、Qwenなど）の性能・画質議論はすべて除外。
- Qwenシリーズは画像生成関連の話題のみのため抽出対象外。