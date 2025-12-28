### なんJNVA部★607 スレッドレポート

#### スレッド概要
- **期間**: 841-988 (約150レス、動画生成・LoRA作成・ComfyUI移行がメイン)
- **主なトピック**:
  - **スケベ椅子（hentai bath stool）問題**: Danbooruタグ提案議論（bath_stool_with_cutout, cutout_bath_stoolなどChatGPT相談）。素材50-100枚程度でタグ有効性疑問視。**姫騎士ニキがIllustrious用LoRA「sukebe_bath_stool_v1_Illustrious」公開（>>915）**。女性/男性座り両対応で好評。
  - **動画生成WF最適化**: High=Smoothmix + Low=DaSiWa(Ver8) Q8 GGUFの5ステップ構成が定番（顔保持力向上、PainterLongVideoで3-6段繋ぎ安定）。StoryMem(MI2V版)顔一貫性劣るが動き自然。新モデル（>>855、libidinous系？）試用で好感触も説明文攻撃的で不安視。射精LoRA競合注意。
  - **LoRAトラブルシュート**: 4キャラ目白飛び問題→白背景多用/表情差分が原因。対策: 背景正規化、white backgroundキャプ削除、ノイズオフセット0.1↑、IL1.0混在回避。
  - **ComfyUI移行ブーム**: EasyWan22卒業派増加。PainterLongVideoスタンダード、StabilityMatrix→venv推奨。新規EasyReforgeインストールエラー（HFサインイン失敗）→としあきwiki参照（5000番台GPU無関係）。領域指定: Comfycouple/Cond Pair Set Props/Rprompt-control/SSSノード。
  - **プロンプト共有**: ポールダンス（theater background, night, on stage, fantasy victorian:1.2）。射精（He ejaculates... wet splat）。
  - **その他**: ポールダンス背景（stripper platform）、GGUFローダー必須、浦島太郎ネタ多。

#### 注目投稿・成果
| レス | 内容 | 反応 |
|------|------|------|
| >>841-861,915 | スケベ椅子タグ/LoRA公開 | 職人認定、ニッチ需要火力高評価 |
| >>847-848,935 | Smoothmix+DaSiWa WF | 基本固定、WFスクショ共有で感謝 |
| >>855-880 | 新モデル（ガチギレ作者） | 動き良/プロンプト効き↑、謎ノード(SKYNET)無視OK |
| >>860-863,898 | 白飛びLoRA修正 | 背景/キャプ対策で解決 |
| >>920 | ポールダンスprompt | 参考/ガチャ要素指摘 |
| >>967-986 | 領域指定ノード（Comfycouple等） | WF梱包共有助かる |

#### 問題点・相談まとめ
- **素材不足**: スケベ椅子bath_stool 1.2k中有効100未満→タグ荒れリスク。
- **モデル相性**: LoRA強度/射精競合でプルプル、CFG調整必須。
- **環境構築**: Easy系卒業でComfyUI知識壁高（git/venv/GGUFノード）。新規インストールエラー多発。
- **ニッチ要望**: ポールダンス薄暗ピンクstage、zip内サムネ閲覧（leeyes推奨も限界）。

#### 次スレ
- **>>975**: なんJNVA部★608 立ておつ多発。ComfyUI深化フェーズ突入か。

全体: 動画長時間化（6段30秒）進展、Illustrious/wai系LoRA活発。エロ実用論中心でボランティア精神健在。負け組報告（>>914 35万）も草。