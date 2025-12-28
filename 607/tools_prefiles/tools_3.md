### 抽出結果: 生成AI関連「ツール」に関する話題

ログ全体をスキャンし、指定ツール（ComfyUI(comfy), A1111, webUI, SUPIR, nano-bananaなど）に該当する話題のみを抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）関連の言及は除外。Tiled, FaceDetailer, SAM3, sageattention, blocswap, triton, easywan/EasyWan/simple comfyUI, WF(Workflow), extra_model_paths.yamlなどはComfyUI関連の機能/拡張/派生ツールとして扱い抽出。ツール選択理由が明記されている場合を強調。

#### 456
- **ComfyUI**: 「今迄reForgeやったからアプスケ+ディテーラーは一段やったんやけど ComfyUIでこれ二段やったら稚作膜LoRAの性能が劇的に向上したで」
  - 理由: アプスケ+ディテーラーを二段化することでLoRA性能が劇的に向上。
- **Tiled**: 「TiledはLCMサンプラーのせいか境界線出て上手く行ってないンゴね」
  - 理由: 境界線が出るためVRAMの暴力で一枚出しに切り替え（不満点）。

#### 483
- **FaceDetailer**: 「>>8ニキのWF（過去スレ）からお借りして、開始終了フレーム補完/アプスケ/FaceDetailer/フレーム補完機能だけのWFや」

#### 486
- **WF (Workflow, ComfyUI関連)**: 「ワイは自分のWFでシードを-1のランダムにして フレーム補間・アプスケ・ディテーラー を無効にしつつガチャって」

#### 499
- **A1111**: 「>>17 手の形って大分前のA1111＆SD1.5の記憶で悪いんやけど 素材から手の形を選んでCNのインペイントつかって元の絵に被せて修正するみたいなのあったよな」

#### 520
- **ComfyUI**: 「ComfyUIの環境を構築しなおしてSAM3入れて自動マスク関係の処理を置き換えて調整してみたけど検出精度が高いから調整し甲斐があるわ」
- **SAM3**: ComfyUI環境に導入し自動マスク処理を置き換え（検出精度が高いため調整しがいあり）。

#### 553
- **easywan**: 「ずっとeasywanだったけどアプデできないから新しくcomfy入れました」
- **comfy (ComfyUI)**: easywanから移行。

#### 554
- **comfy (ComfyUI)**: 「最新型のcomfyとsageattentionを入れたら爆速になった。 comfyはいろいろと最適化されて、blocswapいらんな」
  - 理由: 最新型+sageattentionで爆速。最適化によりblocswap不要。
- **sageattention**: 上記と併用で爆速。
- **blocswap**: 最適化により不要に。

#### 555
- **easywan**: 「モデルとかLoraとかの関係でeasywanから離れられないぞ 同じフォルダにComfyいれて共有とかできるんかな」
- **Comfy (ComfyUI)**: easywanと共有可能か検討。

#### 559
- **easywan**: 「easywanからなら同じzuntanニキの simple comfyUIの方がええんやないか」
- **simple comfyUI**: easywanからの移行推奨。
- **comfy (ComfyUI)**: 「素のcomfyにはsage attentionやtritonが入ってないから 動画作るの遅くなるで」
  - 理由: sage attention/triton未搭載で動画生成が遅い。
- **sage attention**: 上記で動画生成遅延の原因。
- **triton**: 同上。
- **Update.bat**: simple comfyUIのアップデート用（気づき）。

#### 560
- **comfyui**: 「comfyui間なら、extra_model_paths.yamlや、コマンドラインオプションで各種パスを指定するって方法もあるかな あとは、symbolic link(mklink)を作れば、異なるパスでも同じところを参照させるってこともできるね」
  - **extra_model_paths.yaml**: comfyui間でモデルパス共有方法。
- **symbolic link (mklink)**: 同上、管理者権限必要で面倒。

#### 589
- **comfyui**: 「Geminiにcomfyuiをスマホで動かすためのコード書いてもらってるけどめちゃくちゃ楽しい」

#### 599
- **comfyui**: 「最近のcomfyuiは優秀だからVRAM超えるデカいモデルも動くけど 解像度上げての生成はOOMするわね」
  - 理由: VRAM超過モデルも動く優秀さ（ただし高解像度でOOM）。

#### 601
- **EasyWan22**: 「EasyWan22でSSDに溢れずfp16を使えるのか」

#### 616
- **PainterLongVideo**: 「PainterLongVideoが分かってきたで ... WorkFlowも置いとくで」
  - 機能: ３動画連結、FLF2V/ループ動画、ColorMatch、VFI、各回長さ/シード調整、LoRA２パターン適用。
- **WF (Workflow, ComfyUI関連)**: 上記カスタマイズ版共有。

#### 622
- **KJNodes (Get Images From Batch Indexed)**: 「最終フレームだけ取得するなら KJNodes の Get Images From Batch Indexed」
- **VideoHelperSuite (Split Images)**: 同上、インデックス-1指定で最終フレーム取得。

### まとめ
- **主なツール**: ComfyUI/comfy/comfyui（最多出現、速度/最適化/共有/環境構築で好評）、easywan/EasyWan/simple comfyUI（移行検討中だがモデル共有面倒）、A1111（過去のインペイント記憶）、Tiled/FaceDetailer/SAM3/sageattention/blocswap/triton/extra_model_paths.yaml/WF/PainterLongVideo/KJNodes/VideoHelperSuite（ComfyUI拡張/ノードとして機能向上/速度/共有理由で言及）。
- **全体傾向**: ComfyUI系が中心で、速度向上（sageattention/triton最適化）、VRAM/メモリ効率、ワークフロー共有/カスタムが選好理由。easywanはモデル互換で粘るがアップデート/共有難でComfyUI移行推奨。A1111は過去ツールとして懐疑。SUPIR/nano-banana/webUIは未出現。