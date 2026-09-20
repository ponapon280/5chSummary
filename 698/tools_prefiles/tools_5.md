**抽出結果（ツール関連のみ）**

### ComfyUI（comfy）関連の話題
- **Viewerを閉じるキーの設定**  
  ユーザーが要望。開発者側が「そのうちショートカットキーに追加する」と返答。
- **Browserのフォルダアイコンを大きくする**  
  ユーザーが「ファイルかと思ってクリックしてしまう」と不満を挙げ、開発者側が「フォルダとそれ以外でサイズ設定可能にする」と回答。
- **comfy_kitchen_attention（Kitchen attention）**  
  ComfyUIに追加すると速度が向上する（特にQwen系編集時）。  
  理由として「int8convrot環境で1.15it/s → 1.40it/sになった」「2枚画像編集時に処理時間が2/3程度に短縮された」との報告あり。
- **ComfyUIの更新チャンネル / update_comfy.bat**  
  「Stable」だとQwen2.1対応ノード（TextEncodeQwenImage21など）が不足するため、「Latest on GitHub」またはbatファイルから更新する必要があると指摘。
- **Comfy Desktop安定版 v0.37.0**  
  QI2.1のテンプレートが同梱されているとの言及。
- **SelfLiftノード**  
  mmh3の8 steps環境で高速化を試したが、品質劣化が激しく実用的ではなかった。
- **resolution設定（Text Encode Qwen Image 2.1）**  
  デフォルト（1024）だと出力が1MP相当にリサイズされるため、1536に上げると速度・品質のバランスが変わるという報告。

### その他のツール・機能
- **Ref2VAモード**  
  first/last frame imageを同時に使えるようになったという報告。
- **musubi-tuner**  
  Minimax H3のLoRA学習で使用。block swapを最大にしても4090でVRAMオーバーになるため、設定の難易度が高いと指摘。

**除外したもの**
- Qwen-Image 2.1 / Krea2 / MiniMax H3 などのモデル・生成性能に関する言及はすべて除外。
- LoRA（TaoMateなど）やモデル自体の話題は除外。

ツールとして明確に言及され、かつ選ばれている理由（速度・操作性・更新対応など）が書かれている部分のみを抽出しました。