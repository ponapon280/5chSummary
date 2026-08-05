**抽出されたツール関連の話題**

ComfyUI（本体・カスタムノード関連）
- ComfyUI 0.30.1本体の`CFGGuider.sample()`におけるNestedTensor/unbind()処理の不具合がMiniMax H3で発生し、公式報告済みの問題（noiseとlatent_imageの要素数不一致）と一致。修正PR #13318が未マージのためUpdate Allでは解決しない。
- smzNode（A1111書式互換のために導入）がMiniMax H3の動作を阻害する原因となり、ノードを外すことで動作するようになった（LTX2.3のときも同様に悪さしたため外している人が多い）。
- カスタムノードの管理：マネージャー経由で入れたノードはcomfyanonymous管理下になる。KJNodes（v1.4.8）やPatch Sage Attention KJのバージョン管理が重要。
- Load videoノードとref_video_0の接続問題：Load videoの後にget video componentでimagesを取得して渡す必要がある。

SageAttention（高速化・最適化ツール）
- SageAttention単体 vs SageAttention + Sigma Shift + Spectrumの組み合わせで生成時間に差が出ないケースあり（12秒動画で6分）。
- 安定性に問題があり「SageAttentionガチで安定せえへん」。マネージャー経由ではなくGitHubからKJの最新版を直接入れるべきという指摘。
- TritonとSageAttentionの両方が正しくインストールされていることが前提。起動オプションとノードの併用でエラーが出る場合がある。
- 最終的に「SageAttentionだけでええわ」と落ち着いた人が複数おり、Spectrum/EasyCacheとの競合で逆に不安定になるケースも報告。

EasyCache / Spectrum（高速化ノード・設定）
- EasyCacheは1.5倍速までなら劣化を抑えられるが、色が滲む・音声劣化が確実にある。
- 推奨設定例：`reusu_threshold 0.50`、`start_percent 0.30`、`end_percent 0.80` で1.43倍速。音声品質はこれで十分という声あり。
- Spectrumは複数キャラ・カメラワーク・カット割りがあると劣化が目立ちやすい（映像矛盾が発生しやすい）。
- 高速化を詰め込みすぎて競合し、生成時間が逆に不安定になる事例あり。

その他のツール・ノード
- pinned-memory（RAM→SSD漏れ防止、デフォルトでオン）。
- Chrome拡張（バイブコーディングで自作、データセット収集用だがメスガキ口調のため非公開）。
- ワークフロー（dasiwaのminimax3wf）：めんどくさいので素直に使えないという声。

**選ばれた理由・評価ポイント**
- **smzNodeを外した理由**：MiniMax H3（およびLTX）で動作不安定の原因になるため。A1111書式の利便性と引き換えに安定性を優先。
- **SageAttention単体を選んだ理由**：Spectrum/EasyCache併用時に音声劣化や不安定化が目立つため。シンプルで安定性が高い。
- **EasyCacheの設定を調整した理由**：1.5倍速以内に抑えることで画質・音声の劣化を最小限にしたい。
- ComfyUI本体やノードの更新を慎重にしている理由：NestedTensor対応などの特殊処理で既知のバグが残っているため。

Qwenシリーズに関する非画像生成話題はログ内に該当なし。