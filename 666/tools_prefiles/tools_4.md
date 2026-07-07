**抽出されたツール関連話題（モデル名・性能比較は除外）**

- **ComfyUI（および関連ノード/バックエンド）**  
  Krea2使用時の主要ツールとして複数言及。  
  - ComfyUI-Krea2T-Enhancerノードの使用（バイパス/エンハンス系ノード併用で速度が変わる可能性）。  
  - comfy_kitchen backend + Tritonの有効化（`available: True`確認必須）。  
  - INT8 Convrotモデル使用時のTriton/Trition不要条件（NVIDIAドライバ580.88以上、torch cu130系推奨）。  
  - SageAttention/TorchCompileの効き具合検証。  
  - ワークフロー（WF）作成・複製・ControlNet併用例（シルエット下絵一括生成など）。  
  **選ばれている理由**: 3060環境でもAnima（bf16）より高速（int8_convrotで約半分以下の生成時間）になるため。Turboモデルとの組み合わせで実用速度を確保。

- **ローカルLLM関連ツール**  
  - Qwen（非画像生成用途）: 部族語プロンプト作成や自然言語量産で推奨されるケースあり。  
  - Gemma4/Gemma: 日本語理解力重視でQwenと使い分け言及。  
  **選ばれている理由**: Anima向け長文プロンプトやタグ翻訳・補強を自動化するため（手動部族語より効率的）。

- **その他自作/補助GUIツール**  
  - >>399提供のGUIツール（LoRA学習用）: 学習の速さ・文字再現性・ユーザビリティで高評価。オプティマイザ選択や詳細設定の制限は指摘あり。  
  **選ばれている理由**: 通常のComfyUIユーザー向けに設計されており、学習の敷居が低い。

**Web検索による参考情報**  
- ComfyUI-Krea2T-Enhancer: Krea2専用拡張ノード群（Enhancer系）。Triton併用でINT8量子化モデルの推論高速化が公式・コミュニティで確認されている。  
- Triton（PyTorchバックエンド）: NVIDIA GPU向けカーネル最適化ライブラリ。cu130系torchでは不要になるケースが増えている。  
- Qwen/Gemma（ローカルLLM）: ともにOllama/LM Studioなどで容易に利用可能。Qwenは多言語・長文、Gemmaは日本語寄りで評価が分かれる。