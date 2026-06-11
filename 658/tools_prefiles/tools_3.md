**抽出結果**

### ComfyUI（comfy）関連の話題
- **ComfyUIでのワークフロー操作の煩雑さ**  
  隙間が埋められないなどの細かい制御でイライラする事例が報告されており、シンプルな設定だけならappモードの方が向いているという指摘あり。

- **ComfyUIの高度なノード操作（ステップスキップ）**  
  safety filter回避を目的とした1ステップ目スキップ手法が議論されており、Basic Scheduler + SplitSigmasノード + SamplerCustomAdvancedの組み合わせが具体的に紹介されている。  
  → 理由：1ステップ目の安全フィルター判定を回避するため。

- **ComfyUI Desktopの名称変更・設定トラブル**  
  「ComfyUI Desktop」が「Comfy Desktop」に名称変更されたことや、`extra_model_paths`の設定が吹き飛ぶ不具合が報告されている。

**上記以外に該当するツール（webUI、nano-bananaなど）の言及はログ内にありませんでした。**

---

## Web検索による参考情報
- **ComfyUI Desktop → Comfy Desktop**  
  2025年頃に公式に「Comfy Desktop」へリブランドされており、Electronベースのデスクトップ版として機能が拡張されている。名称変更に伴い一部ユーザーが設定ファイルの扱いに混乱した事例が散見される。

- **ComfyUIのSplitSigmasノードによるステップスキップ**  
  コミュニティでsafety filter回避テクニックとして共有されており、特にIdeogram系や検閲の厳しいモデルとの組み合わせで使われるケースがある。