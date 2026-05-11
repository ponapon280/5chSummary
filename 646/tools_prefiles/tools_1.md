## 生成AI関連ツール抽出結果

### 画像生成・編集ツール
#### ComfyUI (comfy)
- **話題**: 
    - 特定のノード（spectrumとLLLite）の併用時にLLLiteが機能しない問題についての相談。
    - 特定のカスタムノード（impact wildcard processor）が動作しなくなった不具合の報告と代替ノードの模索。
    - inputフォルダに出来の良い画像を保存して動画ネタに活用している。
    - AnimaとSDXLを切り替えて使用するワークフローの構築。

#### Forge Neo
- **話題**: 
    - spectrumとAnima ControlNet LLLiteを併用しても高速に動作する点。
    - AdetailerおよびDynamicPrompt(wildcard)が動作しなくなった不具合の報告。

#### Civitai
- **話題**: 
    - コミック機能でのアップロード時のリサイズ仕様（長辺1200px基準）について。
    - リサイズによる画質劣化を防ぐため、事前に手動でリサイズすることや、生成モデル（NanoBanana2からOpenAI GPT-image 2へ変更）を選択することが重要であるという知見。

#### Anima-Standalone-Trainer
- **話題**: 
    - 低VRAM環境（RTX 2070 super）でもLoRA作成が可能である点。

#### Anima-LoRA-Factory
- **話題**: 
    - 環境によってはVRAM不足で失敗する場合がある。

#### BooruDatasetTagManager
- **話題**: 
    - LoRA学習用のデータセットへのタグ付けに使用。

#### sd-scripts
- **話題**: 
    - LoRA学習時の設定（最適化手法や学習率など）に使用。

### その他ツール・LLM
#### Claude
- **話題**: 
    - 動作しないノードのログを読み込ませて、自作のカスタムノードを作成させる手法。

#### Grok
- **話題**: 
    - エロティックな文章の生成において優秀かどうかの検討。

#### Gemma 4
- **話題**: 
    - 特定のシチュエーションにおける長編テキストの生成に使用。