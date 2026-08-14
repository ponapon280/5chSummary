# 🆕 新規トピック（前回からの差分）
### ツール: ComfyUIのインストール・管理ツール
- venv/portable版：最新対応の速さとカスタムノード追従で主流
- Stability Matrix版：インストールが最も簡単で初心者向け
- Desktop版：ComfyUI本体の安定化により選択肢に挙がる
- 全体傾向：最新追従を重視してvenv/portableを選ぶケースが主流
- Stability Matrix：複数UIを一元管理できるパッケージマネージャー

### ツール: 高速化・最適化ツール
- Patch Sage Attention / Memory Efficient Sage Attention Patch：速度向上を確認
- spectrum（context loop系）：context loop非対応のため離脱
- Sage Attention：Kitchen Attention（CK）と比較され、用途・モデルにより使い分け

### ツール: ワークフロー構築・管理・動画関連ツール
- RunPod：高性能GPU借用用途でnetwork volume転送速度が課題
- VideoHelperSuite + RIFEノード：動画フレーム補完専用ワークフロー
- load video ffmpeg：mp4使用時の色味変化回避に推奨
- 高速化LoRA運用：Kijai版turbo LoRAを組み込みstep数・強度を調整

### ツール: カスタムノード・拡張
- adetailer：特定用途（口を閉じるプロンプトなど）向け

### ツール: 他のUI・環境との比較・移行理由
- Forge / A1111系 vs ComfyUI：動画生成ではComfyUIの拡張性・ネイティブサポートが優位
- 非Comfy勢の課題：最新ツール・モデル対応をほぼ諦めざるを得ない

### ツール: 学習・LoRA作成関連
- sd-scripts：anima_utils.pyのnum_blocks変更で学習可能
- 全体傾向：新モデル向けLoRA構築環境が増加し、既存LoRA作り直しの可能性
- Anima LoRA Factory：GPT連携の学習ツールとして言及

### ツール: その他
- GGUF関連（Unet Loader (GGUF)）：重くて遅くなるため非推奨
- Qwenシリーズ（LLM/TE用途）：プロンプト生成やText Encoder強化に使用

### ツール: 全体の傾向
- ComfyUI：拡張性・最新対応・動画生成の扱いやすさから選ばれる
- 最適化：Sage/Kitchen Attentionやキャッシュ系を環境に応じて検証
- 非ComfyUI環境：最新ツール追従が困難

### ツール: Web検索による参考情報
- Stability Matrix：複数UIを一括管理できるオープンソースのパッケージマネージャー
- Sage Attention / Kitchen Attention：量子化・スパース手法による高速化バックエンド
- 検索結果：2026年8月時点の公開情報に基づき、動作は環境により異なる

---
# 元の本文
**生成AI関連ツールレポート（ComfyUI中心の抽出内容に基づく）**

抽出されたテキストは、主にローカル生成AI環境（特に動画・画像生成）における**ComfyUI**の導入・運用・最適化・ワークフロー構築に関する議論を基にしています。モデル性能比較は除外し、ツール選定理由が明記されている点を優先してまとめました。全体の傾向として、最新モデル（H3/Animaなど）へのネイティブ対応の速さや拡張性からComfyUIへの移行が進んでおり、動画生成での優位性が強調されています。

### 1. ComfyUIのインストール・管理ツール
- **venv版 / portable版**：最新対応が早く、カスタムノードや新機能への追従が速い点が評価され、「最新対応の速さ」で選ぶ人が多い。
- **Stability Matrix版**：インストールが最も簡単で、ComfyUI本体の管理が比較的まとも。昔のトラブルはほぼ解消されており、「楽に始めたい人向け」との評価。
- **Desktop版**：ComfyUI本体が安定してきている点で選択肢に挙がる。
- **全体傾向**：どれでも良いが、最新追従を重視してvenv/portableを選ぶケースが主流。Stability Matrixは初心者・手軽さを求める層に推奨。

Stability MatrixはComfyUIをはじめ複数のUI（Automatic1111、Forgeなど）を一元管理できるパッケージマネージャーとして位置づけられています。

### 2. 高速化・最適化ツール
- **Sage Attention / Kitchen Attention（comfy-kitchen）**：実行時間比較（例: 17.80s vs 17.58s）が行われ、微差でSage Attentionが速いケースも報告。`--use-ck-attention`オプションとの併用検証も。comfy-kitchenは「これだけで十分」との声が多く、他の高速化ノードを探さなくなるほど評価が高い。
- **Patch Sage Attention / Memory Efficient Sage Attention Patch**：有効/無効での速度比較が実施され、速度向上を確認。
- **Adaptive Cache系ノード**：知名度は低いが効果ありと指摘。
- **spectrum（context loop系）**：一時使用されたが、context loopで使えないため離脱。
- **その他組み合わせ**：Sage + turbo（4/6/8step） + メモリ効率化ノードの検証例あり。環境（PCスペック + ComfyUI設定）次第で効果が変わるため、個別検証が必要。

Sage Attentionは高速化で注目される一方、Kitchen Attention（CK）と比較され、用途やモデルにより使い分けられる。

### 3. ワークフロー構築・管理・動画関連ツール
- **Stability Matrix**：インストールだけでなく全体管理のしやすさで評価。
- **RunPod**：高性能GPU（例: 5090）を借りて生成を試す用途。network volumeの転送速度が遅い点が欠点として指摘。
- **VideoHelperSuite + RIFEノード**：動画フレーム補完専用ワークフロー（load video → get video components → RIFE → create/save video）。VideoHelperSuite導入済みなら簡略版も可能。フレーム補完だけを行いたい場合に余計な処理を省ける。
- **load video ffmpeg**：mp4使用時の色味変化を避けるために推奨。通常のload videoではフレーム補完時に変色が発生するため。
- **Context Loop / contex loop**：長い動画を安定生成するより、短いループ素材を繋げる方が実用的と判断され使用。
- **FaceDetailer（H3用）**：MiniMax H3向けの専用ノード/ワークフローが共有。
- **高速化LoRA運用**：Kijai版turbo LoRAなどをサンプラーに組み込み、step数（4/6/8）や強度（0.7など）を調整。速度優先しつつ音質劣化を抑える目的。
- **その他Tips**：Clean VRAMノード（VAE Decode直前）、Patch Sol-Attn + Block Cache(T8)の比較検証、LLMエージェント経由の自動プロンプト送出ノード。

ワークフロー管理では、PNG自動格納（ドラッグ&ドロップ復元可能）や日付付け・エクスポート・NAS保管が便利とされ、Civitaiの複雑なWFよりシンプルな公式テンプレが好まれる。

### 4. カスタムノード・拡張
- **ComfyUI-Anima-2.9B custom node**：必須カスタムノード。インストール後はプラグ&プレイで使用可能（専用WFノード不要）。一部競合の可能性あり。
- **ComfyUI-sol-attn**：Triton false + Eff外しで動作確認。
- **adaptiveCache**：見つからない場合の対処例あり。
- **rgthreeのseedノード**：-2/-3でのseed制御に使用。
- **adetailer**：口を閉じるプロンプト用など特定用途。
- **その他**：縦UI対応ノード（AutoCompletePlus対応）、Spectrum-MiniMax-H3（enabled設定注意）。

### 5. 他のUI・環境との比較・移行理由
- **Forge / A1111系 vs ComfyUI**：Forge NeoはAnima対応で即時対応の声あり。一部ユーザーは「宗教上の理由」でForge Neoしか使わず、新モデル対応を待つ。静止画メインならA1111ライクUIにこだわる意味はあるが、動画生成ではComfyUIの優位性（拡張性・ネイティブサポート・WF簡素化）が明確。「拡張性を捨てない」「動画でComfyUI嫌ンは意味不明」との意見。
- **移行タイミング・理由**：Anima登場時やMiniMax H3出た頃が好機。「WANやLTXよりWF簡単」「カスタムノード減」「完成度高いテンプレ」「LLM支援で学習コスト低減」。Forge/A1111から完全移行し後戻り不可にした事例あり。
- **非Comfy勢の課題**：最新ツール/モデル対応をほぼ諦めざるを得ない。ComfyUIでないと最新custom node群が使えずモデルを試せない。

### 6. 学習・LoRA作成関連
- **sd-scripts**：anima_utils.pyのnum_blocksを40に変更で学習可能（公式対応待ち推奨）。28層固定の問題対処例。
- **全体傾向**：新モデル向けLoRA構築環境が増える可能性。既存LoRAの作り直し必要性も指摘。
- **Anima LoRA Factory**：GPT連携の学習ツールとして言及。

### 7. その他
- **GGUF関連（Unet Loader (GGUF)）**：非推奨多数（重くて遅くなるため）。
- **Qwenシリーズ（LLM/TE用途）**：プロンプト生成やText Encoder強化に使用（Gemma4/Qwen3.6併記例、qwen3vl_32b_minimax_h3_int8_convrot vs bf16比較）。
- **ComfyUIアップデート**：v0.31.0〜v0.32.0以降でturbo使用時の雑音大幅減、H3関連対応強化の報告。マルチGPU正式対応でRadeon環境も活用しやすくなった。
- **UI不満・肯定的意見**：ノード多すぎ/UIが複雑との声がある一方、ChatGPT/CodexにWF作成・解説を任せられる点が強み。エージェント経由でインストール〜全自動生成まで可能。

**全体の傾向**  
ComfyUIは拡張性・最新対応・動画生成の扱いやすさから選ばれる。最適化はSage/Kitchen Attentionやキャッシュ系を環境に応じて検証。非ComfyUI環境は最新ツール追従が困難。

## Web検索による参考情報
- **ComfyUIバージョン**：v0.31.0（2026年8月頃）はWan-Animate2ネイティブサポートやAMD GPU改善を含む。v0.32.0（2026年8月11日）はLTX 2.5やQwen-Image 3.0対応、バグ修正・安定性向上を含む。[[1]](https://docs.comfy.org/changelog)
- **Stability Matrix**：ComfyUIをはじめ複数UIを一括インストール・管理できるオープンソースのパッケージマネージャー/デスクトップアプリ。初心者向けの簡単セットアップが特徴。[[2]](https://github.com/LykosAI/StabilityMatrix)
- **Forge Neo**：Stable Diffusion WebUI ForgeのNeo版（Haoming02フォーク）。Gradioベースの最適化・使いやすさ向上版で、最新モデル対応を重視したUI。ComfyUIよりシンプルな体験を提供。[[3]](https://www.thundercompute.com/blog/forge-ui-ai-image-generation)
- **Sage Attention / Kitchen Attention**：ComfyUIの高速化バックエンド。Sage Attentionは量子化・スパース手法で高速（特に動画・高解像度）。Kitchen Attention（CK）と比較検証され、モデル/解像度によりSageがやや速いケースが多い。[[4]](https://www.reddit.com/r/StableDiffusion/comments/1vl8wqw/comfyui_comfykitchen_attention_speed_up/)
- **ComfyUI-Anima custom node**：Animaモデル向けのEnhancerノード（Layer Replay Patcherなど）が存在し、ネイティブサポートを補完。ComfyUI公式でもAnimaワークフローが提供されている。[[5]](https://github.com/AdamNizol/ComfyUI-Anima-Enhancer)

（検索結果は2026年8月時点の公開情報に基づく。実際の動作は環境により異なるため、最新GitHub/ドキュメント確認を推奨。）
