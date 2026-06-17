**抽出結果**

**ComfyUI（および関連カスタムノード/拡張）**
- ComfyUI全般の操作性・ワークフローに関する言及多数。
- rgthree-comfyのPowerLoraLoaderノード：Civitai削除済みLoRAのサムネ/リンク復元方法。
- Anima-LLLite-Regional-Controlnet（Regional-Controlnet）：領域指定によるキャラ配置・ポージング制御に優れ、自然言語プロンプトとの併用で複数キャラ時の打率が向上するため選択。Animaとの相性が非常に良いと評価。
- sageAttention（.whl）：ideogram4使用時にflash attentionより高速（33%程度の速度向上報告あり）なため導入。
- その他：ComfyUI使用後のブラウザ操作癖（ドラッグスクロール）の副作用報告。

**Forge / Forge Neo（webUI系）**
- Forge Neo拡張「sd-webui-llmuse」：Gemma-4-12B-it-QAT-GGUFを軽量・高速で動作させ、Animaとのプロンプト相性が良いため使用。
- Regional-ControlnetがForge Neoでも動作確認された点が言及。
- 全体として軽快さ・Animaとの親和性を理由に選択されている。

**LM Studio**
- Qwen3.6（規制解除版含む）などのローカルLLM実行に使用。画像生成以外のテキスト生成・プロンプト作成用途で言及あり。特にAnimaユーザーがLM Studio経由でQwenを扱う事例あり。

**その他ツール関連**
- NegPip：Turbo使用時でもネガティブプロンプトを有効化するための拡張として言及。

モデル名・バージョンに関する言及はすべて除外。Qwenシリーズは画像生成以外の文脈（LLM実行）のみ抽出。

## Web検索による参考情報
- **Forge Neo**: Stable Diffusion WebUIの高速フォーク「Forge」の派生/拡張版。LLM連携拡張が充実している。
- **Anima-LLLite-Regional-Controlnet**: ComfyUI向けRegional ControlNetカスタムノード。Animaモデル向けに最適化された軽量版として話題。
- **sageAttention**: 2025年頃に登場した新しいattention最適化ライブラリ。特定のhead dim（256など）対応でComfyUIの生成速度向上に寄与。
- **LM Studio**: ローカルLLMをGUIで簡単に扱える人気ツール。GGUF形式のモデル（Qwenなど）に強い。