**抽出結果（ツール関連のみ）**

- **ComfyUI（カスタムノード管理・ワークフロー）**  
  カスタムノードを`ComfyUI\custom_nodes`に1フォルダずつ入れて管理しているが、最近量が増えてきて整理が大変。ComfyUIポータブル版を推奨する声が多く、公式テンプレが充実しているため更新に強いという理由で選ばれている。

- **ComfyUI（動画生成ワークフロー）**  
  Wanの長尺化で以下の手法を使っている：  
  - 画像1枚 → WanImageToVideo  
  - 画像2枚 → WanFirstLastFrameToVideo  
  - 長尺化 → PainterLongVideo  
  - 動画結合 → VACE Join  
  これより良い方法として「SVI」が切れ目の少なさでダントツに評価されている（ただしリファレンス参照が弱く、最新ComfyUIでの動作が不明という懸念あり）。

- **Forge / EasyReforgeNeo / EasyReforge**  
  旧Forgeを使っている人がAnima導入を検討する際に話題に。Python更新で旧Forgeが起動しなくなるリスクを懸念し、venvの扱いやバックアップを推奨する意見が出ている。Forge系は手軽さで選ばれやすいが、更新追従性の低さが欠点として指摘されている。

- **SwarmUI**  
  「みんなでSwarmUI使おう」という軽い提案のみ。詳細な理由はなし。

- **Krea2（Edit機能）**  
  1枚絵から実写ホテルシーンへの変換など編集用途で使われており、「エロは出るけど露骨なエロだと理解力が急落する」という特徴が指摘されている。フィルター解除方法としてSNOFS、MysticXXX、RealismEngineなどのLoRAを組み合わせている例あり。

- **webUI / Forge系全体**  
  「WebUIで動くForgeがええかな」との意見に対し、ComfyUIポータブル版を推奨する回答が多く、更新耐性とテンプレの充実を理由にComfyUIが優勢。

**Qwenシリーズ関連**  
該当する記述なし。

**モデル関連の話題**  
NovelAI、illustrious、FLUX、Wan、Anima、Krea2（モデル部分）、LTXなどはすべて除外済み。