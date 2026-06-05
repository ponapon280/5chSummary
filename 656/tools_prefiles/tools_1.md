**抽出されたツール関連話題（モデル名・画像生成モデルは除外）**

- **ComfyUI（comfy）**  
  - 複数GPU環境での生成速度向上（spectrum有無・Turboの有無で11秒まで短縮した事例）。  
  - Spectrum / Torch compile / dynamic vramとの併用でエラーが発生するため、ComfyUI単体運用を検討。  
  - Anima生成の高速化により「Forge neoを使わずComfyUI一本でもいい」との声。  
  - 古い環境を残したい場合は完全に分離し、通常は最新版に追従する運用が推奨。  
  - rgthreeのContext BigノードでCFG/Stepを効率的に切り替えるワークフロー構築。  
  - バージョン0.23への更新でNegPipノードがエラーになった事例あり（ComfyUI-ppmフォルダ削除→再インストールで復旧）。  
  - Stability Matrix使用時の更新挙動（Releases vs ブランチの違い）に関する話題。

- **Forge neo**  
  - 前日の画像を生成し直すと微妙に変化する現象が発生し、バージョン戻しで再現。  
  - ComfyUIの高速化により「Forge neoを使わなくてもいい」という選択肢として言及。

- **WebUI（IrodoriのWebUI）**  
  - 推論時にCUDAが選択できずCPUしか使えない不具合の報告。

- **LM Studio / lmstudio**  
  - ComfyUIと連携してLLM（テキスト生成用途）を呼び出す方法（API接続ノードの組み合わせ）。  
  - 画像認識可能なVLMモデル（Qwen3-VLなど）の読み込み・利用方法。  
  - ローカルLLMの動作確認・モデル選択用途。

- **Stability Matrix**  
  - ComfyUIのパッケージ管理・更新タイミングの制御（Version TypeのReleases/ブランチ切り替え）。

- **その他カスタムノード・スクリプト関連**  
  - kohyaさんのNode（LoRA学習用）。  
  - sd-scripts内でのLoRA Block Weight適用・階層制御の話題。

**特にツールが選ばれている理由として抽出された点**  
- ComfyUI：マルチGPUでの速度向上、ワークフローの柔軟性（ノード組み合わせ）、Anima生成の高速化。  
- Forge neo：以前は使っていたが、ComfyUIの進化で移行を検討。  
- LM Studio：ComfyUIとの連携が比較的簡単で、テキスト生成用途に適している。

## Web検索による参考情報
- **ComfyUI 0.23**：2025年時点で実際にリリースされており、ノード互換性変更が複数報告されている。
- **Forge neo**：Automatic1111系WebUIの派生（Forge）の新バージョンとして2024-2025年に登場。ComfyUIとの速度比較がよく話題になる。
- **Stability Matrix**：ComfyUIなどのローカル生成環境を管理するGUIツール。GitHubリリースタグとコミットハッシュの更新挙動が明確に異なる。
- **LM Studio**：ローカルLLM実行ツール。ComfyUIとのAPI連携用カスタムノードが複数存在する。