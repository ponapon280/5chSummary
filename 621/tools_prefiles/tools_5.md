### 抽出された「ツール」に関する話題

ログから生成AI関連の**ツール**（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなどに相当するもの）のみを抽出。モデル（Anima, Qwen, Flux, Z-image, Pony, NAIなど）に関する話題は一切除外。ツールの選ばれている理由や具体的な使い方・問題点などが記載されているものは併記。

#### Stability Matrix
- **888**: Stability Matrixポータブル版の場合、モデル本体/テキストエンコーダー/VAEをDataModels以下のフォルダに配置する方法を説明。
- **889**: Stability Matrixの起動からNew Projectタブでのモデル選択、歯車アイコンでVAE(qwen_image_vae)とText Encoders(sd3, qwen3_06b_base)を選択し、Generate Imageで生成する方法を詳細手順で説明。
- **898**: Stability MatrixのTEの2・3を空欄にするのが正解。WFよりプロジェクト保存が捗る。
- **905**: Stability Matrixでモデル選択の欄を押しても何も出てこない問題。
- **912**: Stability MatrixのModel Loaderにチェック、precision→default、vae→qwen_image_vae、Model Loader→UNet、Encoder Type→sd3、Encoder1→qwen_3_06b_baseでモデル検索にdiffusion_modelsフォルダを使う方法。
- **916**: Stability Matrixを使ってる場合はPython 3.13必須（>>719参照）。
- **960**: DiffusionModelsフォルダのモデルをStableDiffusionフォルダにコピー/シンボリックリンクして889のやり方で使う。
- **989**: matrixからcomfyui入れたら再生くらいは余裕。

#### ComfyUI (comfy)
- **914**: Prompt Controlをanimaで使おうとしてもエラー。単純なcomfyui更新じゃダメ？ StabilityMatrixがまだ最新じゃない？
- **958**: animaでloraのxyプロット作れるカスタムノードを探す。モデルのローダーがSDXL前提でうまくいかない。中身をいじるしかない？
- **980**: ComfyLab-Packとテキストでloraを読み込めるprompt-controlを組み合わせてxyプロット。
- **981**: xyプロットの実例（画像リンク？）。
- **982**: comfyui easy installでsageattention導入できた。
- **983**: comfyui easy installのおかげでsageattention導入成功。
- **987**: sage attention入れられないけどcomfyUIで生成できる環境は作れる人が意外と多い。
- **991**: anima用にcomfyをもう一個構築。sageattentionが一発で入った（python3.13 torch2.9.1+cu130 5070ti）。
- **992**: sageとtriton-windowsはPytorch最新版の方が導入しやすい。アップデート怖がる環境ほどバージョン指定が必要で難しい。
- **993**: 981のxyプロットでやりたいことできそう。
- **994**: Python/PyTorch/CudaのVerを合わせればOK。チャットAIのトラブルシューティング力が上がってるおかげで導入が楽。

#### Forge Neo (A1111/WebUI系フォーク)
- **916**: Forge NeoのanimaブランチでAnimaが動いた。Python 3.13必須。
- **962**: Forge Neoでanima成功。

#### WebUI Forge (WF)
- **898**: WFよりStability Matrixのプロジェクト保存が捗る。
- **920**: WFの方でも作れるから困らない。

#### loragui
- **972**: loraguiでanimaのプリセットで生成。sam3で適当に切り抜いた顔画像だけでも反映されて速い。

#### その他のツール関連（カスタムノード/最適化）
- **982-983,987-988,991-994**: sageattention（ComfyUI最適化プラグイン）の導入方法と効果。animaでstep数があるから多少早くなる。ComfyUI easy installが便利。
- **992**: triton-windows（ComfyUI関連最適化）もPytorch最新で楽。

**抽出まとめ**: 主にStability Matrix（モデル管理・プロジェクト保存の利便性が高い）とComfyUI（カスタムノード、sageattentionなどの拡張性・最適化で高速化、xyプロット対応）が多用。Forge Neo/WF/loraguiは代替ツールとして軽く触れられる。選ばれる理由は「プロジェクト保存が捗る」「sageattentionで高速」「easy installで導入楽」「Python/PyTorch最新でトラブル少ない」など実用性・速度・互換性重視。モデル話題は完全に除外済み。