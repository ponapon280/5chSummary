**抽出されたツール関連話題（モデル除外）**

- **ComfyUI（および関連カスタムノード/WF）**  
  - `ComfyUI-ConditioningKrea2Rebalance` のアップデート（Krea2 Image Edit Rebalanceノード追加）。リアル→アニメ寄り編集に使える。  
  - subgraphノードの扱い（unpack必要、modelパラメータいじれない場合の対処）。  
  - ComfyUIラッパー自作（簡単に生成できるようにした、自分用→公開）。高機能化せずComfyUI本体推奨。  
  - ComfyUIアップデート時のトラブル（ClipLoaderがKrea2形式認識しない、0.25.1→0.26.0必要？）。  
  - ComfyUIのカスタムノード導入時のトラブル報告（「ハッキングされた」報告あり）。  
  - 理由：ノード/WFの柔軟性・カスタマイズ性が高いため（Krea2ワークフロー構築、subgraph、Conditioning系）。

- **Musubi Tuner（Musubi-tuner）**  
  - Krea2 LoRA学習用ツールとして複数言及。  
  - VRAM16GB環境での学習Tips：`blocks_to_swap 26` + `--block_swap_h2d_only` + `--novram`（または`--fp8_base`など）でOOM回避・速度向上（20s/it→12s/it）。  
  - Gradio版リポジトリ発見、GUI自作検討中。  
  - 理由：低VRAM（16GB）でもblockswapで学習可能、他のツールよりKrea2との相性が良い。

- **Wan2GP**  
  - 「Comfyやーやーな人」向け代替ツールとして推奨。  
  - 理由：ComfyUIが苦手な人でもKrea2を使える。

- **その他**  
  - ComfyUI公式/redditでの症状共有（subgraph関連）。  
  - 学習GUI不在問題（Musubi公式ドキュメント頼み、Gradio自作検討）。

**Web検索による参考情報**  
- ComfyUI：2025年現在も活発に更新されており、0.26.x系で新機能・互換性向上が続いている。Conditioning系カスタムノードはKrea2などの新モデル向けにコミュニティで開発されている。  
- Musubi Tuner：Krea2（および類似モデル）のLoRA学習に特化したツールとして知られ、block swap / H2D onlyオプションは低VRAM環境での標準的な最適化手法。  
- Wan2GP：ComfyUIを避けたいユーザー向けの簡易ラッパー/代替フロントエンドの一つとして言及されることが多い。