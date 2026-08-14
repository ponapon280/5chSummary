**抽出されたツール関連話題（ComfyUI/ワークフロー/ffmpeg中心）**

- **ComfyUIでの動画フレーム補完専用ワークフロー**  
  - 基本構成: `[load video] → [get video components] → [rifeノード] → [create video] → [save video]`  
  - VideoHelperSuite導入済みの場合の簡略版: `[load video(upload)] → [rifeノード] → [combine video]`  
  - 理由: フレーム補完だけを行いたい場合に余計な処理を省けるため。

- **load video ffmpegの使用推奨**  
  - mp4使用時に色味が変わる問題を避けるために `load video ffmpeg` を推奨。  
  - 理由: 通常のload videoだとフレーム補完時に変色が発生するため。

- **MiniMax H3関連のComfyUIワークフロー**  
  - ComfyUIチュートリアルからDLできるMMH3用WFのstep設定（25）が話題に。  
  - WF組み直し時にSpectrum-MiniMax-H3を追加したが、enabledがデフォルトfalseだったため効果が出なかった事例。  
  - TurboとSpectrumをXORで切り替えて様子見する運用。

- **Context loop / contex loopワークフロー**  
  - 公式改造版のcontex loopワークフローを使用した10秒×3連結テスト。  
  - 理由: 長い動画を安定して作るより、短いループ素材を繋げる方が実用的と判断されたため。

- **FaceDetailer（H3用）**  
  - Minimax H3向けのFaceDetailerノード/ワークフローが共有・言及。

- **高速化LoRAのComfyUI内運用**  
  - Kijai版の `minimax_h3_fl2v_lightx2v_turbo_4step` などの高速化LoRAをComfyUIサンプラーに組み込んで使用。  
  - step数（4step/6step/8step）の調整や強度（0.7など）の設定が話題。  
  - 理由: 生成速度を優先しつつ音質劣化を最小限に抑えるため（8stepの方が音質が安定するケースも報告）。

- **その他のComfyUI関連Tips**  
  - VAE Decode直前にClean VRAMノードを追加してメモリ不足を解消。  
  - Patch Sol-AttnとBlock Cache(T8)の比較検証（生成時間 vs 画質）。  
  - Run押下時にLLMを自動でイジェクトしてH3ノードへプロンプトを送るノード構成。

これらはすべて**ツール・ワークフロー・ノード操作**に関する記述で、モデル自体の性能議論は除外しています。