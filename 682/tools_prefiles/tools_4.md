**抽出されたツール関連の話題（モデル名・性能議論は除外）**

### 1. **ComfyUI（comfy）本体・環境構築**
- **言及の多さ**: ログ全体で最も多い。
- **選ばれている理由**:
  - 動画生成（特に長尺・参照画像/動画使用時）のワークフロー柔軟性が高い。
  - カスタムノードや高速化ノードを組み合わせやすい。
  - 初心者でもClaude/CodeX/Grokに環境構築を丸投げしやすい（「claudeに環境構築やらせて寝る」「codeXに全部やってもらった」）。
  - 最近はEasy-Install系やManager経由で導入ハードルが下がった。

### 2. **Comfy-Kitchen（kitchen attention / comfy kitchen）**
- **主な話題**:
  - ComfyUIの高速化ノード/attentionバックエンドとして複数回言及。
  - sage attentionよりわずかに遅いが精度が少し良いという声。
  - 導入の手間が少なく、sage attentionの壁を回避できる点が評価されている。
- **選ばれている理由**:
  - 「sage attention導入という壁がなくなって楽」
  - coreでサポートされているため追加設定が不要。
  - 低スペック環境でも安定して使えるという報告あり。

### 3. **ComfyUI Manager**
- 更新・ノード管理ツールとして頻出。
- 問題点として「Managerで更新してもkitchenの新機能（ModelAttentionBackendなど）が出てこない」ケースが報告されている。
- 手動で`pip install -r requirements.txt`を追加で実行する必要があるという指摘あり。

### 4. **ComfyUI-Easy-Install**
- インストール方式として複数人が使用。
- Manager更新後にkitchen関連ノードが出ない原因として挙げられている。

### 5. **その他のComfyUI関連ツール・ノード**
- **video combineノード + prune outputsノード**: 不要な中間ファイル（jpgや音声なしファイル）の削除に使用。
- **SamplerCustomAdvanced**: 各種attentionの処理時間計測に使われている。
- **--fast-diskオプション**: 高速SSD使用時のメモリ節約策として言及。

### 6. **Stable Diffusion WebUI系**
- **Forge Neo**: Krea2を使える点が言及。
- 「Stable Diffusion WebUI」をSDUIと略して呼ぶ文化あり。
- ComfyUIを敬遠していた層が「まずはStable Diffusion WebUIから」という流れで触れられている。

### 7. **環境構築・運用関連ツール**
- **docker + samba + WSL2**: NAS上のモデルをシンボリックリンクで使うための構成例。
- **pip install -r requirements.txt**: ComfyUI更新時の必須手順として複数回強調。
- **codeX / Claude / Grok**: 環境構築やノードの使い方、ワークフロー作成の相談相手として多用。

### まとめ（特に選ばれている理由が明記されているもの）
- **ComfyUI**：柔軟なワークフローと動画対応力。
- **Comfy-Kitchen**：sage attentionより手軽に高速化できる。
- **Easy-Install / Manager**：初心者向け導入のしやすさ（ただし更新時の追加手順が必要）。
- 全体として「Claude/CodeXに聞けば環境が作れる」という、AIアシスタントとの組み合わせがツール選択の大きな要因になっている。