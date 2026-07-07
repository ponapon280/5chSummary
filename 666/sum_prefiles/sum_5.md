**なんJ（5ch）AI画像生成スレッド レポート**

### スレッド概要
本スレッドは主に **Krea2** と **Anima** の比較を中心に、VRAM制約下での運用、LoRA学習の難易度、NSFW性能、日本語プロンプト対応などを議論した内容。古いGPU（Voodoo言及）から現代GPU（RTX 4090/5090、Radeon）までのハードウェア話や、ComfyUIワークフローTipsも散見された。

### 主な論点
- **Krea2 vs Anima**:
  - Krea2はプロンプト追従性・日本語出力・手足破綻の少なさで評価が高い一方、2次元NSFW（特にdanbooru系エロ）はまだ弱い。
  - AnimaはLoRA作成のしやすさ・NSFW表現力で優勢。既存キャラLoRA資産が豊富なため「手放せない」という声多数。
  - 移行派は「Krea2のポテンシャルが高い」とするが、エロ用途では「Animaのまま」という意見が根強い。

- **ハードウェア・運用**:
  - Turbo版の生成時間（Krea2 Turboで47秒 vs Anima Turboで9.6秒など）が話題に。
  - VRAM 8〜16GB層の現実的な運用（fp8/int8、ComfyUIの--gpu-onlyオプション）が頻出。
  - 低スペック環境（Ryzen 5700U内蔵GPU + ZLUDA）で90分/枚という極端例もあり、クラウド（Runpod 4090/5090）推奨の声も。

- **LoRA学習**:
  - Animaはデータセット10〜20枚＋専用設定で比較的楽に成果が出るが、Krea2は学習負荷が高く熱問題がネック。
  - 品質タグの扱いやステップ数調整のコツが共有された。

- **その他**:
  - Flux/ZIMAGEの下火化、Civitaiの粗悪LoRA増加、健全用途 vs エロ用途の使い分けなどが言及。

全体として「Krea2は次世代感があるが、エロ用途ではまだAnimaが実用的」というコンセンサスに近い空気感だった。

---

## Web検索による参考情報
- **Anima**：Civitaiで公開されているSDXL系アニメ特化モデル（Anima Pencil / Anima Turboなど）。LoRA学習のしやすさとNSFW表現力で人気。2024年後半〜2025年にかけて活発に使われている。
- **Krea2**：RedCraft氏関連で話題の新モデル（Krea Turbo / int8_convrot対応）。プロンプト追従性と日本語出力に強みがあるが、danbooru系NSFW学習はまだ不十分という評価がコミュニティで一致。
- **Flux / ZIMAGE**：Black Forest LabsのFluxは高品質だがVRAM要求が高く、ZIMAGEはローカル勢の間で下火傾向。Krea2/Animaとの比較で言及されることが多い。
- **関連ツール**：ComfyUI（fp8/int8対応、--gpu-onlyオプション）、Forge Neo（INT8 ConvRot対応予定）が実運用で主流。

（情報は2025年時点のCivitai・GitHub・各種AIコミュニティの公開情報に基づく）