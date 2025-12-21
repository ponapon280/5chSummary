### 抽出された「ツール」に関する話題

ログ全体から、生成AIの「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR/nano-banana系、ControlNet, KohyaSS/musubi-tunerなどのUI/拡張/学習ツール、カスタムノード、ワークフロー関連）に限定して抽出。モデル（NovelAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）の話題は一切除外。ツールの選定理由が明記されている場合のみ記載。

#### ComfyUI (comfy) 関連
- **641**: forgeでSDXLを使ってたけど、今はcomfyでZITを使うのがトレンド？（トレンドとして言及）。
- **663**: ComfyUI内の設定で変更できる（Kサンプラのサムネ表示対策）。
- **666**: webUIとcomfyUIで待ち受ける洗礼（40xx系から50xx系GPU移行時のtorch/cu128対応）。
- **671**: comfyuiだと、今はcuda12.6/12.8/13.0のいずれかを選択（PyTorch2.9デフォで動けば最適、荒波の0.4以降は0.376推奨）。
- **672**: comfyUI portableもforge系も（pythonバージョン管理の話題）。sageAttention3なら128、sa2+130で良さそう。comfyUIは0.5だが下げやすい。
- **673**: comfyのポータブル版なら解凍するだけ（簡単インストール）。
- **683**: comfyuiはwindows版ならpython_embeddedフォルダでpython導入済み（バージョン心配不要）。
- **685**: comfyUI portable python3.10にportable 3.13のembededを上書きしたら壊れた（密結合で旧→新の手順必須）。
- **686**: Comfy最新にしないと新しいモデル試せん（qwen layered試したいため）。
- **690**: SVIはComfyのカスタムノードじゃなくて簡易システムだからeasywan環境だとできない。
- **724**: wslにComfyUIをぶち込んでみた。
- **728**: WSL2のComfyUI環境（Layer試す実験台）。
- **729**: ワイのcomfy 0.3.77のままやのにmultiGPU動かん（torch2.9.1+cu130、5070ti）。
- **735**: ComfyUI、SD1.5のチェックポイントでも普通に出力。
- **736**: ComfyUIはv0.4.0になったのにいきなりv0.5.1（v0.4無かったことに？）。0.4系統から命名規則が変わり週一アップデート。
- **745**: custom_nodes\comfyui-multigpu\distorch_2.pyエラー（multiGPUでraw_block_list unpackエラー、メタデータ付き生成NG）。
- **750**: ComfyUI 0.4.0あたりからアップデート命名規則が変わった。
- **756**: DistorchMultiGPUはVer0.3.6X0.3.7Xぐらいで対策方法あり（最新版でも動く）。
- **777**: smooth mix拾ったワークフローで動いた（ComfyUI WF）。
- **778**: ちびたいに投稿されてる動画はワークフローまるごと保存（プロンプトパクり放題）。
- **783**: ComfyUIに移行したからBREAK使わず、CLIP Text Encodeで女・男・構図・画風を分けてCONDITIONING Concat（BREAK相当効果）。
- **802**: Kandinsky5のオリジナルのWF使うとノード見つからず（いいWF探し）。
- **811**: 今のComfyUIだと普通にNewBie使える（プロンプト細かく記載で描き分け可能）。
- **815**: framepackみたいなのがComfyUI動画生成に光を（Grok級期待）。
- **836**: ComfyUIの導入はStability MatrixかzuntanニキのSimpleComfyUiどっち？（動画生成目的）。
- **837**: Stability Matrixのほうがアプデ体制いい（SageAttention追加楽だがフォルダ構成独特でモデル配置問題多め）。SimpleComfyUiはSageAttention入ってる利点。
- **838**: venvでComfyUI環境整えて初生成成功（5060tiデビュー）。
- **839**: Qwen Image LayeredはこのWFが広まってきてる（ComfyUI WF）。

#### A1111/webUI/Forge系関連
- **641**: 昔はforgeでSDXL（今はcomfyトレンド？）。
- **666**: webUIとcomfyUI（GPU移行時の洗礼）。
- **672**: forge系（pythonバージョン引き継ぎ）。
- **683**: reforgeの環境こさえるのにpython3.10インストールしてvenv（sdwebui周り面倒）。
- **687**: A1111の頃からgit cloneしてvenv切ってる（pip freeze > pip_install_list.txtで復旧一発、pytorch手動）。
- **722**: Forge-Classic入れてみたけどeasyreforgeより遅かった（sageattention導入必須。Classicもオプションで自動導入。Git Readme参照。おま環？）。
- **786**: 未だにforge使ってるワイは取り残されてて（皆comfy前提）。
- **793**: Forge-Classicでもsageattention導入せんと速度変わらず。EasyReforgeは最初からsageattention入ってる赤ちゃん向け。
- **794**: A1111系だとForge Couple使っても複数キャラ書き分け難い。
- **804**: eazyreforgeからforge neoにした（UI preset無効化できない？）。
- **807**: 旧Forge(公式3.10.6)にpython3.12.10でvenv作ってcu128起動（requirements消して依存アップデート、数時間エラー60回で起動成功）。
- **813**: わいの現役バージョン（UI軽くてすっきり）。

#### ControlNet (CN) 関連
- **675**: SD1.5時代のControlNetは最近使う？
- **679**: CNはanytestかposetest使っとけばええ（1.5 LoRA互換なし）。
- **695-696,699,701,705**: anytest/posetest（本絵ポーズ参考にプロンプト微調整。posetestは画風影響少なく構図反映、weight調整でanytestも可。衣装変えたい時posetest忠実すぎ。フォトショ+CNで修正）。
- **799**: cn tile（i2iアプスケ用）。
- **783**: CN(anytest/posetest)併用（男顔出にくいため）。

#### LoRA学習ツール (KohyaSS/musubi-tuner) 関連
- **674**: musubi-tuner導入してZIT学習（B580でコードいじらず動く。kohyaニキ感謝。florence2でキャプション）。
- **692**: Intelボードでmusubi-tuner（VRAM24Gのb60選択肢に）。
- **730**: kohya HR fix（胴長解決の近道）。
- **800**: KohyaSSで学習。
- **808**: KohyaSS。

#### その他のツール
- **660**: RMBGワイ（背景削除？）。
- **691**: Fooocus備え付けのControlNet（SD1.5より劣化？別口あり）。
- **779**: Ultimate SD upscale（16Kx8Kアプスケ用、wsl170GBメモリでTiled VAE Encoder通過）。
- **782**: BREAK構文, RegionalPrompter（複数キャラ生成不安定）。
- **796**: adobe bananaとgemini banana（使い勝手違う、nano-banana系？）。
- **834**: RVC（TTS同一性高める）。
- **809**: Microsoftオープンソース（一枚絵から3Dモデル生成、Hugging Spaceで試せる）。

これでログ内の全ツール関連話題を網羅。理由明記のものは括弧内に記載（例: 簡単さ、速度、互換性、トレンド）。モデル名/Qwen layeredのモデル部分は抽出除外。