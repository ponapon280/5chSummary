**抽出されたツール関連話題（モデル除外）**

### ComfyUI / Comfy（本体・運用）
- **stability matrix経由の更新方法**  
  releasesではなくbranchesで更新する運用が話題に。masterブランチで0.31.1→0.31.0にダウングレードした事例あり。  
  → **理由**: release/v0.31ブランチはパッチ修正のみで進む仕様のため、masterは機能追加用として分離されているのが正常動作。

- **ComfyUI本体の更新・注意点**  
  最新コミット取得でOOMが発生する事例（minimax + sageattention併用時）。  
  → 一度前のコミットに戻す対応が推奨される。

- **--use-ck-attention起動オプション**  
  コマンドラインで直接指定する方法が共有。

### Comfy Kitchen / Kitchen Attention（CK Attn / ModelAttentionBackend）
- **SageAttentionの代替として導入**  
  複数箇所で比較（速度・品質・導入難易度）。

  **選ばれている主な理由**:
  - Sage/tritonのインストールが不要でシンプル
  - 低スペック環境でも安定しやすい
  - 公式デフォルトComfyUI + 公式テンプレだけで完結する可能性
  - 精度向上（細部の崩れが少ないという報告）
  - GPUが古いほどSageビルドが面倒になるため、劣化が同程度ならCKの方が楽

- **速度比較例**:
  - Sage Attention: 3m51s
  - Comfy Kitchen: 3m59s（ほぼ互角〜やや遅めだが導入コストが低い）
  - 低スペック環境ではSageよりCKの方が速くなるケースも報告

### Context Loop / Contex Loop（ワークフロー・ノード）
- **長尺動画生成での採用理由**:
  - motion contextより繋ぎが自然
  - LLMにJSONを大量生成させて放置運用に強い
  - 尺の心配がほぼ不要になる
  - review gateノードと組み合わせればsceneごとにseedガチャ可能

- **motion contextとの使い分け**:
  - 1CLIPずつ確認しながら繋げるならmotion contextの方が使いやすい
  - 完全放置で大量生成するならcontex loopが最強

### その他のツール・ノード
- **kijaiのvideo vae int8 conv**: VRAM節約＋10-20秒程度の高速化で採用。
- **Hybrid Loader**: 特定のワークフローで使用（設定を正しく行えば安定）。
- **crystools**: 競合報告あり（オフ推奨の声）。
- **LoRAローダー(kj4step)**: H3系ワークフローで多用。
- **ModelSamplingMiniMaxH3 / Patch系ノード**: 各種attentionパッチと併用。

### 補足
- Animaはモデル指定のため除外。
- Qwenシリーズに関する言及は今回のログでは画像生成関連のみのため抽出対象外。
- 全体として「導入の簡単さ」「インストール不要」「低スペック耐性」がComfy Kitchenが選ばれる主な理由として繰り返し挙げられている。