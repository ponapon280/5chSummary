**抽出結果（ツール関連のみ）**

### ComfyUI / カスタムノード系
- **ComfyUI（comfy）**
  - >>919: 「久しぶりにqie(aio)使ったけど、こんなに生成早かったかな?comfyuiのアプデのおかげか?」
    - **理由**: ComfyUI本体のアップデートで生成速度が向上したと感じている。

- **comfy-kitchen**
  - >>936: 「comfy-kitchen/pull/117がmainにマージされとるからそろそろComfyUI本体に降りてきそうやな」
  - >>958: 「comfy-kitchenってsageみたいにノード噛ませてやるやつちゃうんか?」
    - ノードを挟んで処理を追加するツールとして認識されている。

### 動画・一貫性関連ツール
- **Context Loop / Lora Scheduler**
  - >>914: 「Contex LoopってStudio使う意味ある? 試しに使ってみようと思ってLora Schedulerを普通のtaggedと同じ構成で繋げてみたけど砂嵐」
    - Context Loop + Lora Schedulerの組み合わせを試したが、砂嵐（ノイズ）が出て失敗した事例。

- **ref2va**
  - >>932: 「contex loopより普通にref2vaで動画作って繋げていったほうが一貫性とクオリティ取れる」
    - **理由**: Context Loopより**一貫性とクオリティ**で優位と判断して使用。

### 高速化ノード（ComfyUI系）
- **Sol Atten / H3系ノード**
  - >>933: 「高速化ノードのsol attenってどれが本命なんや? sol atten / H3 / H3 Scheduled Sol Atten / H3 Memory Efficient Sol Atten」
    - 複数のSol Atten系ノード（H3含む）を比較検討している。

### その他ツール
- **minimax**
  - >>862: 「今日色々llmでminimaxのprompt生成試してたけどこれが良かったで」
    - **理由**: 複数のLLMでprompt生成を試した結果、**minimaxが一番良かった**。
  - >>925: 「minimax image edit まだなのぉ」

---

**除外したもの**
- モデル名（NAI、FLUX、anima、Qwenなど）の言及はすべて除外。
- 純粋なLLMの使い勝手やBAN話は、ツールとしての具体的な言及がない限り除外。