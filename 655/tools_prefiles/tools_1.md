**抽出されたツール関連話題（モデル関連は除外）**

- **ComfyUI（comfy）**  
  - カスタムノードの利用（特にIP-Adapter、ControlNet、Anytestとの組み合わせ）。  
  - ワークフロー構築やインペイント用途で言及。  
  - 理由：柔軟なノード接続が可能で、IP-AdapterやControlNetを組み合わせた高度な制御がしやすいため。初心者殺しにならないようカスタムノードの言及が必要と指摘あり。  
  - 直接llama.cppのChat_handlerノードとの併用例あり（VRAM管理のためUnload Model node使用）。

- **LM Studio**  
  - ローカルLLM/VLMサーバーとして使用（画像キャプショニング用）。  
  - 理由：OpenAI互換APIサーバーを簡単に立ち上げられ、gemmaやQwenシリーズを読み込んでキャプショニングスクリプトと連携しやすい。ollamaより情報が多く、扱いやすいという声。

- **kohya（kohya_ss提供のimage_caption_cli.py + promptファイル）**  
  - Anima向けキャラLoRA作成時の自動キャプショニングツール。  
  - 理由：LM Studioと組み合わせることでローカルAIによるスペルチェック・タグ修正が効率化され、手動タグ付けの負担を大幅に軽減できる。

- **llama.cpp（直接使用 / Kijai版fork）**  
  - LM Studioを介さず直接利用。  
  - 理由：パフォーマンスが最も良いとされ、VRAM管理（Unload Model node）が容易。ollamaやLM Studioより軽量で速度面で優位という指摘。

- **ollama**  
  - ローカルLLM実行環境として言及。  
  - 理由：MoEモデルをCPUに逃がす設定がしにくく、最近の情報が不穏という理由で敬遠する声あり。LM Studioやllama.cppへの移行を検討する人が多い。

- **IP-Adapter**  
  - ComfyUIワークフロー内での使用・研究。  
  - 理由：読み込んだ画像の「雰囲気」を反映させる用途。ただし「使い時が見つからない」という声もあり、ControlNet/Anytestとの比較で検討されている。

- **ControlNet / Anytest**  
  - IP-Adapterとの併用研究。  
  - 理由：Anytest超えを目指した高度な制御用途。

- **Layer Forge**  
  - ComfyUIでのマスク作成代替ツールとして試用。  
  - 理由：右クリックでのマスク作成が面倒なため。ただし「使いづらい」との評価。

- **SD-scripts形式LoRA**  
  - ComfyUI v0.21.1での対応状況。  
  - 理由：Anima TE学習LoRAをComfyUIで扱えるようになった点が注目。

**Qwenシリーズ関連（画像生成以外として抽出）**  
- VLM（画像キャプショニング）用途としてgemmaと並んでLM Studioやllama.cppで使用。  
- 理由：OpenAI互換APIサーバーで読み込め、キャプショニングスクリプトとの連携が容易。

---

## Web検索による参考情報
- **ComfyUI**：Stable Diffusion向けのノードベースUI。カスタムノードの豊富さが特徴で、IP-AdapterやControlNetとの高度な組み合わせが一般的。
- **LM Studio**：ローカルLLMのGUIツール。OpenAI互換サーバー機能を備え、VLM（gemma、Qwenなど）を使った画像キャプショニング用途で人気。
- **llama.cpp**：軽量なLLM推論エンジン。直接使用することでオーバーヘッドが少なく、VRAM管理がしやすい。
- **kohya_ss**：LoRA学習・キャプショニング用スクリプト群を提供するツール。image_caption_cli.pyはVLM連携による自動キャプション生成に使われる。