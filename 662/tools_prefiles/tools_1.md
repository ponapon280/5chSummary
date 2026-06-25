**抽出されたツール関連話題（モデル関連は除外）**

- **ComfyUI（comfy）**  
  - comfyの初期ワークフロー（wf）が変更されたという言及  
  - ComfyUI-Manageのv3系とv4系の移行・互換性について（v4移行後にUIが変わったがすぐに慣れた、legacy UIフラグでv3風に戻せる）  
  - civitai comfy nodes / 新civitaiノードの挙動（青消費が発生するが用途が不明）  
  - ComfyUIのMask Editor使用時に発生するinputエラー（見た目上の問題で再実行すれば正常）  
  - ComfyUIへの移行が進んでいる（WebUI/Forge neoからの乗り換え）  
  - comfyuiをDドライブへ移す際の挙動（Hugging Face関連ファイルがCドライブに作成される）

- **Stable Diffusion WebUI / Forge**  
  - ComfyUIへの移行が進んでいるという言及（Forge neoも一部残っている）  
  - ローカル生成の主流ツールとしてWebUIからComfyUIへのシフトが話題

- **nano-banana**  
  - nano bananaとgpt imageの調子が悪いという報告

- **Animerge（マージツール/GUI）**  
  - Animergeの複数回更新（GUI見た目調整、翻訳UI、マージタブのプルダウン→エントリー方式変更、実行ログ追加、ADDifTプリセット追加、DPOモード追加）  
  - ADDifTのDPOモード（良い画像・悪い画像のペアでモデルを好みに寄せる簡易版。LECOとの違いとして「関連ワードへの経路遮断」が挙げられている）  
  - DPOモード使用時の挙動（画像A/Bの順序で効果が逆転する可能性、学習率・preference_betaは低めに設定推奨）  
  - カスタムノードとして「金取れるレベル」と評価され、便利さが強調されている

**特に選ばれている理由が明記されている点**  
- ComfyUI：WebUIからの移行が進んでおり、カスタムノードの柔軟性（ADDifT、DPOなど高度な学習・調整機能）が理由として挙げられている。  
- Animerge：ADDifT/DPOのような「カユいところに手が届く」特殊効果調整が手軽にできる点が評価され、学習時間も短い（1分程度）。

**Qwenシリーズ関連**  
該当する話題なし。

（モデル名・バージョン・新サービス等のweb検索対象はログ内に該当なしのため省略）