**抽出されたツール関連話題（モデル関連は除外）**

### ComfyUI（comfy）関連
- **インストール・環境構築**:
  - 公式版インストール時にmodelsフォルダが存在しない点が話題に。ポータブル版ではComfyUIフォルダ内にmodelsフォルダがある。
  - custom_nodesフォルダへのgit cloneによるCustom Node追加（例: ConditioningKrea2Rebalanceノード）。
  - templateにkrea-2、boogu image edit、boogu turboが公式追加されている。
- **使い勝手・学習コスト**:
  - ノード繋ぎが複雑で初心者にはハードルが高い（Forgeからの移行者も戸惑う）。
  - 一度workflowを作れば変更が少なく、自動化（i2i、アップスケール、領域分けマスク生成など）に強い。
  - 最新モデル対応が早く、公式workflowが充実しているため「勢いのあるところに乗っかる」メリット。
- **選択理由**:
  - 最新モデル（Krea2など）の公式対応が早い。
  - 動画生成や高度な自動化が必要な場合に避けられない。
  - webUIより軽快に動作するケースあり。
- **その他**:
  - Easy系（Easy Comfyなど）の需要は低く、ComfyUI単体で十分という意見多数。
  - APIをエージェントに渡す用途も言及。

### webUI / Forge系（A1111、Forge、Reforge、Neo、Easy Reforgeなど）関連
- **移行・比較**:
  - Forge NeoやEasy ReforgeからのComfyUI移行話が頻出。
  - webUIは「らくらくフォン」的で脳死運用可能だったが、最新モデル対応でComfyUIに劣る。
- **選択理由**:
  - ComfyUIより操作が直感的で、初心者・静画メインの人に適する。
  - ただし「webUIの知識はノイズになりつつある」「ComfyUI推奨」という意見が優勢。
- **その他**:
  - webUIは同人表紙作成程度なら十分で、無理にComfyUIを覚える必要はないという声。

### Custom Node / Workflow関連
- **Krea2向けノード**:
  - ConditioningKrea2Rebalanceノード（検閲フィルター除去用）。強度0.5〜0.8で効果あり、副作用として日本語文字が崩れる。
  - Turbo版との相性問題（一部で動作せず、別のworkflowで対応可能）。
- **選択理由**:
  - 検閲解除やプロンプト制御のために必要だが、設定詰めが難しく「有能な人が出てくるのを待つ」状態。
  - LoRA併用やノード単体で効果が変わる説が混在。

### その他ツール
- **nano-banana（nanobanana2）**:
  - 半年以上使っていたユーザーが言及。R15程度までなら十分で、ローカル生成をやめていた。
- **Qwen（画像生成以外）**:
  - Qwenを使ったworkflow（WF）で背景生成などの用途が言及（非画像生成用途のため抽出対象）。

**ツール選択の主な理由まとめ**:
- **ComfyUI**：最新モデル公式対応・自動化・軽快さ・workflow共有のしやすさ。
- **webUI系**：操作の簡単さ・初心者向け。
- **Custom Node**：特定機能（検閲解除など）の補完。

## Web検索による参考情報
- **ComfyUI公式テンプレート**: 2025年時点でKrea系やBoogu系モデルのworkflowが公式に追加されており、最新モデル対応の早さが確認できる。
- **ConditioningKrea2Rebalanceノード**: Reddit（r/DegenDiffusion）でKrea2の内蔵フィルター除去用Custom Nodeとして共有されており、強度調整による検閲突破と副作用（文字化け）が報告されている。
- **Forge Neo / Easy Reforge**: ComfyUIへの移行を促す動きの中で、A1111系webUIの後継として位置づけられているが、最新モデル対応ではComfyUIに劣る傾向。