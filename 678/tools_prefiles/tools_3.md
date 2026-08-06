**抽出されたツール関連話題（モデル除外）**

### ComfyUI関連
- **ComfyUI portable版**：最新のportable版を入れてMinimax H3を使うとcuda/pythonバージョンが新しすぎて問題が出る可能性あり。古い環境だとsage attention/triton対応で苦労する。
- **pinned memory**：現在主流の高速化手法。blockswap時代よりSSD負荷が少なく、RAMをVRAMのように使える。`--disable-pinned-memory`はメモリが逼迫した環境やマルチGPUでエラーが出る場合に使用。逆に有効にするとDMA転送が高速になるが、PC構成によっては逆に遅くなるケースもある。
- **RAM_DISK活用**：余剰RAMをRAM_DISKにしてWindows tmpファイルやComfyUIのテスト環境、生成キャッシュを置くことでSSD寿命を延ばす使い方。
- **低スペック向け運用**：32GB RAMでもComfyUIが自動でRAM容量を見て動作を調整してくれる。VRAMオンリーよりは遅いが、swapなしで実用的な速度が出る。
- **ワークフロー/ノード関連**
  - 自作ノードや複雑なWFは書類選考で評価されにくい（GitHub Starが少ないと特に）。
  - 「は処理をせき止め」「Latentダウンスケール」などの独自ノードをコーディングエージェント（Codexなど）に作ってもらう事例。
  - NestedTensor形式のLatentでエラーが出るためモンキーパッチが必要になるケース。
- **SageAttention / Sol-Attn / EasyCache / Spectrum**
  - Patch SageAttention KJノードを追加して生成時間を短縮（例: 0.7MP10秒で6分→改善）。
  - Sol-Attnは50xx番台以外では効果がなく、逆に遅くなったりエラーになったりする。
  - EasyCacheは品質への影響が大きいため、Spectrumを推奨する声。
  - 50xx番台ならSageAttention + Sol-Attn + Spectrumの組み合わせで安定して高速化。
- **ダウンロード関連ツール**
  - huggingface_hub + `hf download`コマンドを使うと大容量ファイルの切断が減る。
  - PowerShellのcurl.exeで直接DLする方法も一部で使われている。
- **simpleComfyUI**
  - 古いバージョン固定のため最新の効率化（pinned memoryなど）が反映されておらず、純粋ComfyUIより2.5倍遅くなる事例あり。
  - 最新版に上げても一部機能（パイタッチなど）が使えない制限がある。
- **AI-toolkit**
  - LoRA学習で早期に対応したため、短期間でLoRA作成が可能になった。
- **その他**
  - RAM64GB環境でもComfyUIが自動調整してくれるため、必ずしも大容量が必要ではない。
  - マルチGPU環境ではpinned memoryのON/OFFでエラーが出るため、環境ごとに検証が必要。

### ツール選択理由として明記されていた点
- **pinned memory**：SSD書き込みを最小限に抑えつつ高速転送が可能。低スペックでも安心安全に運用できる。
- **SageAttention系**：生成時間を大幅短縮（4割削減例あり）。ただしGPU世代によって効果が大きく変わる。
- **Spectrum**：品質劣化が少なく、step数削減目的ならEasyCacheより優位。
- **RAM_DISK**：SSD寿命保護と一時ファイルの高速化を両立。
- **hf download**：大容量モデルのダウンロード安定性が高い。

モデル（FLUX、Wan、Minimax H3本体、SexGod、10Erosなど）の性能・出力結果に関する言及はすべて除外しています。