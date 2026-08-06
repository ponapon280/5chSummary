**抽出結果（ツール関連のみ）**

### 1. **ComfyUI（comfy）関連**
- ワークフロー（WF）の構築・見直し（turboLora WF、MiniMax H3用Samplerノードの切り替えなど）
- ノード構成の話題（detailer→refiner→upscaleの流れ、ref_videoへの接続方法）
- キャッシュ系ノードの比較・選択
  - EasyCache：音声参照時に声がガビガビになる
  - BlockCache / Spectrum：音質は良いが重い
  - kjattention + Sol-attn + blockcacheの組み合わせで生成時間短縮
- マルチGPU設定
  - `--disable-pinned-memory`オプションの使用
  - 単体GPU vs マルチGPUでの挙動差
- 更新後の変化（モデルアンロードボタンの位置変更、生成速度の変化）
- VAE関連（kijai版 VAEの使用、キャッシュとの組み合わせ）

### 2. **RTX Video Super Resolution / RTX Super Resolution**
- ブラウザ・動画プレイヤーでの使用体験
- 1080p以上の高解像度向けで、480p〜640pの低解像度には不向きという評価
- 導入理由の見直し議論（速さ重視で一旦入れているが、性能的に上位互換を検討する声）

### 3. **Lossless Scaling（Steam）**
- アプスケ＋フレーム補完機能の代替として言及
- 保存方法はOBS推奨という補足あり

### 4. **OBS**
- 動画保存ツールとして言及（Lossless Scalingとの組み合わせで使用）

### 5. **Premiere / Maya / Blender**
- プロレベルの映像制作で必要なツールとして言及
- Premiereだけでは不足で、3Dコンテ作成にはMayaやBlenderが必要という指摘

### 6. **AG（Gemini/Opus系エージェント）**
- エロプロンプト作成補助ツールとして使用
- Opusの方が安定するという評価
- プロンプトの自然な拡張・詳細化に強い理由で選ばれている

### 7. **その他ツール・ノード系**
- video inputノード / ビデオコンポーネント取得ノード（ref2VAでの動画参照用）
- Sol-attn / Mem Eff Sage Attention（VRAM使用量や速度とのトレードオフでON/OFFを検討）
- turbo LoRA使用時のステップ数調整（4step/8step/10stepでのWF変更）

**モデル関連（NovelAI、illustrious、FLUX、Wan、Qwen-Image、anima、Z-Image、LTX、MiniMax H3本体など）は一切抽出していません。**  
Qwenシリーズに関する非画像生成の話題も今回のログには該当するものがありませんでした。