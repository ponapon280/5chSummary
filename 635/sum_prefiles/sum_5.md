### なんJ NVA部スレッド（★635→★636）レポート

#### 1. スレッド概要
- **期間/レス数**: 836〜1000（約165レス）。ComfyUI/Anima中心のAI画像生成スレ。Anima Preview3リリースが最大のトリガーとなり、後半で大盛り上がり。次スレ（★636）が974で立てられ、移行。
- **主な雰囲気**: 技術Tips共有、モデル比較、興奮の歓声。Anima3の進化を絶賛しつつ、LoRA再学習の労力に嘆く声多数。エロ画像共有や動画実験も散見。NAI（NovelAI）批判混じりでローカル派優位。
- **キーワード**: Anima3（Preview3）、ComfyUIアップデート、LoRA学習（1024解像度）、リアス（Illustrious派生含む）、NAI v4、VTuber実験。

#### 2. 主要トピックと議論ハイライト
##### (1) ComfyUIの効率化アップデート問題（836〜856, 940〜956）
- **問題点**: 共有メモリ積極使用でSVI生成20秒超で溢れ/OOM。Ver0.13系をWan2.2用にキープ推奨。再現性難（PyTorch/起動オプション/バージョン不一致が原因）。
- **Tips**: 過去スレ検索推奨（taggerは>>506）。ComfyUI Managerでrelease/v0.18.5ブランチ更新安全。Nightly（master）はバージョン表記古め。
- **感想**: 「人間の脳みたい」「アプデ受け入れるべし」。

##### (2) Anima Preview3リリース祭り（870〜993, 後半主力）
- **リリース詳細**: 4/7頃Preview3（月刊Anima: P1=1/29, P2=3/11, P3=4/7）。1024解像度長時間学習、マイナーアーティスト（投稿50-100件）データ拡張。推奨prompt: `masterpiece, best quality, score_7`。
- **評価**: 
  - 解像感/線画向上、プロンプト忠実度爆上げ（鉄パイプ擦り/ダッシュ表現OK）。
  - 多様性増（ガチャ良）、自然言語効き良し。Danbooruタグ流用可。
  - 自転車サンプル絶賛。指/手破綻微増の指摘も少数。
- **DL/確認Tips**: ちびたい/Anima[Official]（HF/civi同一、ハッシュ確認推奨: OpenHashTab）。ComfyOrg資金援助（石油王説w）。
- **懸念/期待**: LoRA再学習必須（FT多様性犠牲）。フルHD（1920x1080）/2048対応期待。正式版/GW次号予想。z-image未定。
- **名言**: 「月刊Animaやんけ！」「Animaちゃん、nai軽々超え」。

##### (3) LoRA/モデル移行とTips（871〜906, 919, 948, 962〜965）
- **LoRA学習**: Cosine with Restarts（lr_scheduler_num_cycles=2以上で過学習抑え）。1500stepならCosineでOK。Anima3で1024試すとOOM/SSD侵食注意。
- **移行論**: SDXL/リアス廃棄派増加。「XL払い箱」「Anima Lora充実まで併用」。NAI超え感。
- **Tips**: IP-Adapter/Anima対応？、chest/ass press on glass（nai系）、against wall併用。Wildcards/LLM変換でリアス→Anima。

##### (4) 動画/VTuber実験（847, 870, 898, 920, 903, 901）
- **実験共有**: 
  - VTuber風: Animaキャラ+Qwen/Grokポーズ+Emoji-TTS+Wan2.2 S2Vリップシンク（files.catbox.moe/jm0x6t.mp4）。3060遅め。
  - MV風: InfiniteTalk I2V（Claude prompt）+Suno v5.5。
- **議論**: TikTokダンス（ControlNet荒れ）。AIVTuber流行？（全自動楽だが下ネタ止まり）。バ美肉/ボイチェン比較。

##### (5) NAI/他モデル比較（837, 851, 858〜864, 985〜990, 996）
- **NAI批判**: v4.0 gdgd（エロ不可、バイブ未実装、SDXL世代進化困惑）。ベータテスター無能。クローズドベータ失敗例。
- **優位**: エロ天国日本ローカル。NAIは単発絵向き、こだわりはComfyUI。Pony初期の苦戦思い出。
- **他**: ACE-Step 1.5 XL公開、sm新作、Forge neo tagger（>>506）、taggui推奨。

##### (6) その他雑談/Tips
- エロTips: ガラス押し付け（glass/against wall）。
- トラブル: datasetバグ仮復旧、SSDごみ箱容量食い。
- 資金/開発: ComfyOrg石油王w。Preview小出し最適（完成品gdgd避け）。

#### 3. 注目投稿
- **870**: VTuber実験動画共有（実践派）。
- **919**: anima3 LoRA自慢（ﾊﾟﾝﾂ!w）。
- **920**: MV没動画（InfiniteTalk/Suno）。
- **889**: Anima3プロンプト進化実感（鉄パイプ/ダッシュ）。

#### 4. トレンド/未来予測
- **Animaシフト加速**: リアス/NAI離れ。1024+マイナー強化で本格移行派急増。正式版でwaiAnima？期待。
- **課題**: LoRA再学習負担、ComfyUIスマホ非対応。
- **スレ勢い**: Anima3で消費爆速、次スレ即立て。音声スレ復活提案も。

#### 5. 総括
Anima Preview3がスレを支配、開発ペース/進化に感謝の声多数。ローカル派のTips共有活発で実践的。NAI過去失敗を反面教師に「Preview文化」支持。次スレでAnima本番/フルHD待ち？ 技術進化のワクワク感満載やで！