### なんJ NovelAI部（生成AIスレ）ログ要約レポート

#### スレッド概要
- **期間/レス数**: 提供ログは>>4から>>225までの約200レス（抜粋）。主にComfyUI中心の生成AI議論。NovelAI (NAI)、Illustrious (リアス)、LTX-2、SVI、SAM3などの動画/画像生成ツールがホットトピック。
- **全体傾向**: ComfyUIのアップデート（v0.8.0）と新モデル（LTX-2）のトラブルシューティングが最多。ハードウェア在庫/価格高騰、NAI vs リアス比較、複数キャラLoRA作成難易度、AMD ROCm高速化ニュースが目立つ。動画生成ブームで「追いつけん」「環境構築しんどい」声多数。なんJらしい下ネタ（エロ生成、シコり報告）混在。

#### 主なトピック別まとめ

##### 1. **ハードウェア/在庫/価格事情** (>>19-20,36,104,193-198,209など)
   - ドスパラPalit RTX 5070Ti (16GB) 在庫切れ→値上げ復活→即切れ。VRAM16GB以上品薄。
   - AmazonUSでRTX 5070Tiポチ多発も、空箱詐欺/キャンセル報告（開封動画推奨）。
   - RTX 5090新モデル（GIGABYTEなど）発表ラッシュ。「ラジカセ感かわいい」「rev商法で価格ゴリ上げ」「企業努力（）」と皮肉。
   - AMD ROCm 7.1.1ニュース: ComfyUIでSDXL 2.6倍、FLUX.1[schnell] 5.2倍、WAN 14b 5.4倍高速化（>>42）。RTX5090民「意味ないわ」。
   - 低VRAM民の悲鳴: RTX3060 12GB/8GB再生産リークで「悲劇」。Tesla M40 24GB活用希望も微妙。
   - 自慢マシン: i7-10700K + RTX5080 (PCIe3.0ボトルネック)で「あと3年戦う」宣言。

##### 2. **ComfyUIアップデート/環境構築/トラブル** (>>17,30,32,59,62,67-69,71,79,86,90,95,120-122,135,204-208,213-216など)
   - **v0.8.0アップデート激アツ**: Sage Attention3対応、comfy_kitchenエラー多発（RTX50用FP4モジュール、無視OK）。CU130推奨でCU128環境キープ派多数。
   - **Stability Matrix移行**: モデル共有に`extra_model_paths.yaml` or シンボリックリンク推奨。アプデ後リンク切れ注意。
   - **エラー祭り**:
     | エラー内容 | 解決策/推測 |
     |------------|-------------|
     | hires.fixで奇形 | denoise調整/WF晒せ |
     | LTXVAudioVAEDecode tuple index out of range | SMZ Nodes無効化、モデル分割ファイルDL（fp8_e4m3fn/q4/gemma3一式） |
     | SAM3 nipples/areolaeエラー | 卑猥ワードNG、カンマ→and、confidence_threshold 0.01-0.05下げる |
     | comfy_kitchenモジュールエラー | requirements.txt実行、無視可 |
     | cu128/130ミスマッチ | TensorRT/SageAttention再構築、EasyWan2.2でcu118安定 |
   - Manager不調/ノード混乱: ComfyUI-SAM3 vs comfyui_sam3（ハイフン版が複数プロンプト可）。Custom Node Manager半分しか入らず。
   - 動画環境: EasyWan2.2/tensorRTで速く、reforge併用派も。マルチGPU/raylight話題皆無。

##### 3. **新モデル/ツール実力評価** (>>23,25,27,33,40,42-44,49-50,77-80,91,100-102,114,120,142,169,176,188,219など)
   - **LTX-2**: 音声付き動画神（リップシンク/BGM込）。RTX3060 12GBで余裕（--reserve-vram 10/2）。アニメ溶けまくりだが実写◎、生成早い。fp8/ggufで低VRAM可もVAEエラー多。I2Vは3次元向き、NSFW Lora即出現。WF公開（>>142: 6連サンプラーでガチャ継続）。
   - **SVI/StoryMem/SAM3**: SVIはanchor sampleでキャラ崩れなし。SAM3は3060可（fp16版軽量）。複数検出むずい。
   - **WAN2.2/EasyWan**: 30秒動画安定、LoRA学習待ち。
   - **NAI vs リアス (Illustrious/wai派生)**: NAI「ポーションで絵柄調整可だがキャラ参照弱い、高い、肌質感AI臭」「ストーリー手軽」。リアス「人体カチカチ/構図弱いが柔軟、ZIT+i2i◎」。NAI v3/v4.5強調耐性高。NAI「均一化逆、多様」。
   - **複数キャラLoRA**: 超難関。顔混ざり/融合祭り。解決策: 画像数/リピート1:1、DoRA、マスク分割（Latent Couple/Regional Prompter）、2girls画像混ぜ、マルゼン式キャプション、wildcards有効。Zimage/Turbo期待。
   - **その他**: Google AI Proでスレ要約動画生成（>>63）。kohya GUI Lionオプティ、RAdamScheduleFree推奨。

##### 4. **生成派閥/哲学/雑感** (>>21,24,28,40,58,85,88,105,147-158,169-172,181,184-185など)
   - **ComfyUI移行組急増**: 「動画避けられん」「柔軟◎」「裏配線魂燃える」。Forge/A1111離脱中だが「使い方わからん」「赤ちゃん」多。
   - **クラウド/ローカル論争**: 「ローカルクソ！クラウドサイコー」vs「買えん状況でローカル必須」。
   - **エロ至上**: 「1girlポン出し最強」「spread pussyで脳汁」「bare shoulderセーターシコ」。
   - **進化速すぎ問題**: 「1週間でLTX新登場」「WF陳腐化」「追いつけん」。サブグラフ/グループで汎用化提案。
   - **要約ツール**: NotebookLMでスレ音声/動画化枯れ技。チャッピー（Grok?）に「お上品モード」でエロスレまとめ。

#### 注目ニュース/未来予想
- AMD ComfyUI高速化で「安価AMD夢ある」。
- RTX3060 8GB再生産で低VRAM民絶望。
- LTX-2/SVI/SAM3で動画ブーム。Z-Image Base（ZI）/複数キャラ進化待ち。
- ComfyUI「2年で別物」「アップデート必須化」。

#### 総括
スレ民の9割が動画生成に傾倒、ComfyUIがデファクト。環境構築地獄だが「脳汁出る神イベント」とポジ。NAIは優秀だが高/硬直的でリアス補完。ハード品薄で「企業努力（）」煽り。次スレはLTX-2 WF共有/複数LoRA聖戦予想。生成楽しめンゴ！