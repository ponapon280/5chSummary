### 抽出された「ツール」関連話題

ログから生成AI（主に画像/動画生成）に関連する**ツール**のみを抽出。モデル（NAI, illustrious/リアス/ill/IL, FLUX, Wan, Qwen-Image, anima, Z-Image/ZIT/ZIE, LTX/ltx2.3など）の話題は除外。Qwenシリーズの画像生成以外は対象外（ログに該当なし）。ツールとはComfyUI(comfy), webUI(A1111など), nano-bananaなどの環境/インターフェース/拡張を指す。ツール選択理由が明記されているものは強調。

#### EasyWan / easywan / easywan22関連
- **248**: easywanダウンロード過程でここに来る可能性。
- **256**: easywanは更新されてないから自信がある人は**ComfyUIの標準テンプレートから使い始めた方が良い**（理由: 更新停止で信頼性低いためComfyUI推奨、としあきのwiki記述）。
- **257**: 時代遅れのnoteを読んで出戻り。
- **258**: easywan22の説明を読まない嘆き。学習コストで**標準テンプレートで動画生成の流れ理解した方がお釣りくる**（理由: easywan22の説明読むコストが高い）。
- **273**: easywanをリポジトリから削除すべき（更新停止で迷惑）。
- **283**: noteやitmediaでeasy取り上げられお客さん増。
- **290**: Easyシリーズ半年更新なし。一般は半年前なら使えると思うが、**A1111（web UI）は**（対比で継続使用）。
- **292**: EasyReforgeのfork作成（reForge本体とtorch,sage,拡張機能のアップデートとバージョン固定なしが違い。Spectrum追加。**EasyForgeNeoも作れるがStability Matrixを使った方が良い**（理由: ニーズ少ない上級者向けだがStability Matrixの方が優位）。
- **295**: 求められてるのは**EasyWan22のfork**だがWF難易度高くトラブル面倒。**EasyForgeNeoなら仕組み簡単だがモデル/サンプル画像大変でStabilityMatrixと変わらない**（理由: 手間と差別化不足）。
- **297**: easyの環境アプデ（supermergerがneoで動かずreforge捨てられず）。
- **306**: EasyReforge問題はここで解決。

#### ComfyUI (comfy / ConfyUI / comfyui)関連
- **256**: ComfyUIの標準テンプレート推奨（easywan代替、理由: 更新性と自信ある人向け）。
- **258**: 標準テンプレートで動画生成（easywan代替）。
- **298**: **ComfyUIをアプデしたらエラーで生成不能、WAS Node Suite消したら解決**（理由: カスタムノード衝突）。
- **300**: **comfyui環境作ってエロ量産**（恒久的ストレージ+WF+モデルでAPI代替、理由: エロ向けAPI無理）。
- **329**: ワークフロー（ComfyUIのworkflow示唆、サンプラー/ポジ/ネガ設定晒し）。
- **383**: **comfyuiを0.18.1にしたらカスタムノード不具合多数、0.17.0で様子見**（理由: 互換性切りすぎ）。
- **389**: **comfyUIはカスタムノード入れない/使わないのが理想、静画と動画分ける**（理由: 安定性）。
- **401**: comfyuiはControlNet用専用フォーク版必要（neoはファイル差し替え可）。

#### A1111 / webUI関連
- **249**: A1111流行り初めは低スペPCユーザーも。
- **290**: A1111（web UI）（Easyシリーズ対比で継続）。
- **386**: **A1111系で出力プレビュー画像をマウスホイール拡大縮小拡張探し**（チャッピーに聞くもなし）。
- **390**: Imagusで対応？（A1111系）。
- **403**: **A1111?でJSパッチ（zz_lightbox_zoom_patch.js）でプレビュー拡大縮小**（チャッピーに作ってもらい動作）。

#### forgeneo / neo / reforge / EasyReforge / EasyForgeNeo関連
- **261**: NEOのインストール厄介（クリーンインストール必要）。
- **266**: forgeneoインストール簡単（アテンションコンパイルなし）。
- **292**: EasyReforge fork（アップデート対応）。EasyForgeNeoも可だがStability Matrix推奨。
- **295**: EasyForgeNeo簡単だがモデル集め大変。
- **297**: supermergerがneoで動かずreforge使用。easy環境アプデ。

#### Stability Matrix (matrix)関連
- **292**: **Stability Matrixを使った方が良い**（EasyForgeNeo代替、理由: 仕組み簡単でモデル/サンプル不要）。
- **295**: **StabilityMatrixと変わらない**（EasyForgeNeoの欠点として）。
- **312**: matrixこそあらゆる環境のeasy詰め合わせ（使えばいい）。

#### その他のツール/拡張/API/クラウド関連
- **285**: AIエージェントにCivitaiのAPIKey有効化依頼。
- **286**: **クラウドGPU借りてサクサク**（低スペPC代替、理由: メモリ16GB少ない場合）。
- **289**: **easyクラウド環境構築システム**が必要（ガチ赤ちゃん向け、クラウドGPU金直結で出てこない）。
- **291**: **簡単な方法でクラウドGPU画像生成**（詳細省略）。
- **293**: API使用（環境構築不要）。
- **296**: APIじゃエロ無理（動画クラウドサービスなし）。
- **298**: WAS Node Suite（ComfyUIカスタムノード、削除で解決）。
- **384**: （animaだがツール外）
- **423**: idorriのwebuiフォーク（ベースモデル指定可、RTX50対応）。

#### ツール選択理由まとめ（明記分）
- **ComfyUI標準テンプレート**: easywan更新停止で信頼性高く学習コスト安い（256,258）。
- **Stability Matrix**: EasyForgeNeoより手間少なくあらゆる環境対応（292,295,312）。
- **クラウドGPU/API**: 低スペPC代替でサクサク（286,289,293）。
- **forgeneo**: インストール簡単（266）。
- **カスタムノード最小化**: ComfyUI安定性向上（389）。
- **JSパッチ**: A1111プレビュー操作改善（403）。

これでログ全体のツール関連を網羅。ハードウェア（5090/PRO6000/グラボ/VRAM）やログイン/どんぐり/TTS/DRM突破などはツール外として除外。