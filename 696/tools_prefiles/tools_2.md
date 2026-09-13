**抽出されたツール関連話題（モデル除外）**

- **ComfyUI**  
  - 複数回登場。特にバージョン0.35.0でのSpectrum/er-sde動作問題や、0.34→0.35更新時の挙動について言及。  
  - ComfyKittichnAttentionを将来性・楽さの観点でSageAttention2系より推奨（Wan2.2時代からの実績とComfy本体サポートの見込み）。  
  - MiniMax-H3公式WFのTEがnvfp4のため、デフォルトがnvfp4になりやすい点に言及。  
  - Stability Matrix経由での0.34→0.35更新で問題なく動作した報告あり。  
  - カスタムノード更新（Spectrum MiniMax-H3ノード 0.2.23→0.2.26）でOOMが発生した事例あり（ロールバックで解消）。  
  - TorchCompile関連のトラブルで再起動が必要になるケースの対処として、カスタムノードを一つずつ切る or クリーンインストールを提案。

- **webUI**  
  - YuE2-3B（音楽生成）で「webUIはcodexで簡単に作れる」との言及。ポン出しの弱点（インストゥルメンタル生成）も指摘。

- **codex**  
  - ChatGPT系ツールとして複数言及。$200プラン加入・リセットの話題や、コンテキストループワークフローの改造依頼に使われている。  
  - 「仕事関係除けばツール作成やゲーム製作がメイン」との使用例あり。高度な作業を任せているという声も。

- **DaVinci Resolve**  
  - MCP対応というビッグニュースとして言及。ローカル環境が必要になる点で注目。

- **irodori TTS**  
  - ボイスクローン性能について「感情指定できない」「全然似ないし感情豊かにならない」との不満。speakercfgなどの数値調整を試したが改善せず、GPTに相談して絵文字多用を試す提案あり。

- **floyo**  
  - MiniMaxをfloyo経由で使っている人の有無を尋ねる投稿あり（実用性についての言及なし）。

- **その他ツール関連の言及**  
  - ControlNet（openpose / scribble）: 構図参照の文脈で過去から使えていた点を指摘。  
  - SageAttention2系 / ComfyKittichnAttention: 将来性・速度・品質のトレードオフで比較され、ComfyKittichnAttentionが推奨される理由として「Comfy本体サポートの見込み」と「楽さ」が挙げられている。

**特に「選ばれている理由」が明記されているもの**
- ComfyKittichnAttention：将来性（Comfy本体サポート）と操作の楽さでSageAttention2系より優位。
- codex：コンテキストループなどの複雑ワークフローの改造が容易にできる点。
- DaVinci Resolve：MCP対応によりローカル環境の必要性が高まった点。