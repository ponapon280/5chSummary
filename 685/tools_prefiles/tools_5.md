**抽出されたツール関連話題（モデル話題は除外）**

- **ComfyUI (comfy)**  
  - comfyuiをAPIで使えばええだけ（875）  
    → 理由: vLLM-OmniやOpenWebUIとの組み合わせでUIを一本化できるため。  
  - comfyuiのworkflow（Ref2v-Basic）をcontext loopで使う（902, 904）  
    → REVIEW GATEノードで止まる仕様をauto_continue_timeoutで回避して自動化。  
  - ComfyUI更新でNumPy2.5エラーが発生 → 2.3.5にダウングレードして復旧（894）  
  - webuiからComfyUIへ移行（892）

- **OpenWebUI + vLLM-Omni**  
  - OpenWebUIでエロ小説生成 → エロシーン画像生成 → 動画化の一連の流れをUI一本化（874）  
    → LAN内別PCのMiniMax H3をAPI経由で呼び出せる点が利点。

- **SeeDance2**  
  - 戦闘シーンは過剰に忖度してくれるSeeDance2で作ったほうがええ（862）  
    → コンテの質が低い個人制作アニメの戦闘シーン向けに推奨。

- **その他ツール関連の言及**  
  - huggingface_hubの暴走でスクリプトが止まる（871）  
  - 10eros（特に10eros-LTX）で1pass30秒生成（887）  
    → スピード感を重視する場合の選択肢として言及。

**除外したもの**  
- anima / リアス / ZIT / LTXなどのモデル自体の性能・使い勝手比較  
- Qwen3.8-27Bのトークン消費・コンテキストウィンドウの話（画像生成以外ではあるが、ツールではなくモデル性能の話題のため除外）