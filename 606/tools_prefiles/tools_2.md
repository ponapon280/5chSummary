### 抽出された「ツール」関連話題一覧

ログから生成AI関連の**ツール**（ComfyUI/comfy, A1111, webUI, nano-banana, SUPIRなど）に限定して抽出。モデル（NAI, Pony, Wan, Qwenなど）の話題は除外。ツールが選ばれている理由や比較・言及の文脈を併記。各ログ番号順に整理。

#### ComfyUI (comfy)
- **246**: 「comfy4ヶ月くらい更新してないんで上げたら動かなそうだなぁ」  
  → 更新停滞を懸念。
- **266**: 「ComfyUI初心者ワイ、FaceDetailerの性能がA1111のADetailerにまるで届かない」  
  → FaceDetailerの性能がA1111のADetailerに劣ると不満。
- **268**: 「Detectorモデルもsamモデルもつながる設定項目も多い デフォ設定値でも綺麗なるで」  
  → FaceDetailerの設定（Detector/SAMモデル接続）を推奨。
- **270**: 「trellis2試してみようと思ったが、相変わらず3D系は環境依存が酷いモジュールが多くて動かんかった」  
  → ComfyUIの3D系モジュール（trellis2）の環境依存性を指摘。
- **271**: 「ComfyUI supports Qwen Image layeredっことでちょっと話題になってたで」  
  → Qwen Image layeredサポートで話題。
- **273-275**: 「A1111 ADetailer前/後 vs ComfyUI FaceDetailer前/後」「このサイズでもちゃんとかかっとるな A1111 ComfyUI」  
  → A1111 ADetailerとFaceDetailerの性能比較（画像添付）。ComfyUIも「ちゃんとかかっとる」と評価。
- **279**: 「ComfyUIでt2i これを使って A1111で2回i2i ComfyUIで2回i2i ComfyUIのi2i、何か間違えている気がする」  
  → t2i/i2iのワークフロー比較でComfyUI使用、挙動に疑問。
- **280**: 「comfyui-impact-packアプデしたらIterative Upscale (Latent/on Pixel Space)の初回クソ遅い現象がなおってる」  
  → comfyui-impact-packのカスタムノード更新でUpscale速度改善。
- **310**: 「ComfyUIでi2iのモデルをhakushiMixにしたらいい感じになったが…」  
  → i2iで使用、互換性に言及。
- **320**: 「comfyuiを使い始めた頃にa1111と同一シードでも同じ絵にならずハマった…a1111互換にしてくれるsmZNodesのカスタムノードを導入して…同じ絵が出るようになった」  
  → A1111とのシード互換性問題をsmZNodes（カスタムノード）で解決推奨。
- **325**: 「ComfyUI-TRELLIS2 comfyのカスタムノードからインストールして、付属のWFで動作確認できたよ」  
  → ComfyUI-TRELLIS2カスタムノードのインストール・動作確認。
- **337**: 「Comfyuiのワークフロー上で特定のノードがどこにあるかって検索できる？ノードが見つかりませんってなったときに…」  
  → ワークフロー検索機能の質問。
- **353**: 「comfyでWebUIの互換は物凄く大変だから特別な理由がない限り両方使うのがいいのでは reforgeとかneoを併せて入れとくのごいい」  
  → WebUI（A1111）との互換大変、reforge/neo併用推奨。
- **391**: 「浦島ワイcomfyuiの最新バージョンが0.5.1になってて困惑してる。先々週は0.3台じゃったような…」  
  → バージョン急更新（0.3→0.5.1）に困惑。

#### A1111 (Automatic1111のWebUI)
- **266**: 同上（ComfyUIとの比較）。
- **273-275**: 同上（FaceDetailer比較）。
- **279**: 同上（i2iワークフロー）。
- **320**: 同上（ComfyUIとのシード互換問題）。
- **351**: 「A1111はアップスケールにtiled diffusion使ってるけどComfyUIは素のi2i…tiled diffusionのカスタムノードがあった記憶があるので、入れて試してみるわ」  
  → tiled diffusion使用をComfyUIに推奨。
- **353**: 同上（ComfyUIとの併用推奨）。
- **355**: 「tiled diffusionのnoise inversionがあるのA1111だけ…A1111はi2iでAdetailerのfaceを入れるとくっそVRAM食う」  
  → tiled diffusion/noise inversionの独自機能、VRAM消費指摘。

#### nano-banana
- **259**: 「nano banana proで赤ちゃんへの授乳イラストの加工してたら初めて勝手に乳首描きやがったぜ」  
  → 加工ツールとして使用、自動乳首描画に驚き。
- **265**: 「ワイはnano banana画像で試したら上記のようになったやで」  
  → 画像分解テストで使用。

#### その他のツール
- **FFmpeg** (252,253): 「FFmpegインストールしてコマンドでやってるわ」「ffmpeg -i input_file.mp4 ... ugoira/連番.jpgが出力されるンゴね」  
  → pixivうごイラ用連番JPG出力ツールとして詳細コマンド共有。
- **DaVinciResolve** (247): 「動画をなんかのツールで（ワイはモザ入れついでのDaVinciResolve）jpg連番出力して」  
  → pixivうごイラ用連番出力ツールとして使用。
- **LM Studio** (370-380,382-397): 「LMstudioを起動してバックグラウンドに設定」「LM Studioでのエラー処理」「LMstudioで画像認識されてないモデルぽい」「LMStudioで目玉マークが付いているモデルが画像認識対応」「LM-studio serverとちょくにやり取り」  
  → 画像認識モデル（VL系）使用時のエラー/設定トラブルシュート。速度がComfyUI-QwenVLより優位（397）。mmproj不要（387,392）。
- **ComfyUI-QwenVL / ComfyUI_Simple_Qwen3-VL-gguf** (388,390,400): 「ComfyUI-QwenVLは連携なんて考えずに単体で使える」「ComfyUI-QwenVLもgguf対応した」「処理早いで llama-cpp-python導入に一手間」  
  → VL系ノード単体使用推奨、処理速度比較（LM Studio優位だが最適化不足）。
- **easyreforge** (398,401,406,414): 「easyreforgeインスコしてこの有様」「EasyReforgeは新規インストールでエラーが出る」「easyreforgeは50XXでもうまくやってくれる」「easyreforgeは確か50##みたいなファイルが内部にあってそれ実行したら行けた」  
  → RTX50シリーズ対応、CUDA/PyTorchバージョンエラー解決に推奨。
- **Z-Image-Turbo** (438,264?): 「Z-Image-TurboのcontrolNetのpatch modelに8step版が出てた…LoRAいれるとボロボロになるんでControlNet使うときはLoRA外してた」「ZITより良い意味で汚くていい」  
  → ControlNet patch model更新でLoRA耐性向上（tile推奨）。
- **easywan / easywan22** (422,423,428,432): 「ddr5の32g環境やとwan生成速度遅すぎて無理…easywan22やん」「esaywanよりも、ポータブル版ComfyUIに…Stabilitymatrixから入れた方が良い」  
  → 低スペック（32GB）環境向け軽量ツール、ポータブルComfyUI/Stability Matrixより軽い。
- **Stabilitymatrix** (432): 同上、ポータブル版ComfyUI導入推奨。
- **smZNodes / comfyui-impact-pack / ComfyUI-TRELLIS2** (320,280,325): ComfyUIカスタムノードとしてA1111互換/Upscale/3D系で言及。

**抽出まとめ**: 主にComfyUIとA1111の比較（性能/互換/ノード）が最多。nano-bananaは加工ツールとして。RTX50シリーズ関連でeasyreforge/easywanが目立つ。理由は主に「性能比較」「互換性」「速度/軽量」「エラー解決」。モデル話題（Wan/Qwenなど）は一切除外。