### 抽出された「ツール」関連話題

ログから生成AIツール（ComfyUI, A1111, webUI, Forge/Reforge/Neo, SAM3, FaceDetailerなどのノード/拡張機能、StabilityMatrixなど）に関する話題をすべて抽出。モデル（Anima, Qwen, Wan, illustrious/リアス, banana/nano-bananaなど）の言及は除外。ツールが選ばれている理由や利点が明記されているものは強調して記載。各ツールごとにまとめ、関連レス番号と抜粋を記載。

#### ComfyUI (comfy)
- **443**: カスタムノードを独自改造・置き換え。ガラパゴス化が進むが、WF配布しない個人用なので問題なし。
- **445**: 8割自作ノード使用。形になったら配布予定。ヘビーユーザー向けで一般ユーザーには合わない可能性。
- **446**: ComfyUI-outputlists-combiner（激有能カスタムノード発見、サンプラー並べの努力が無駄に。Animaみたいな拡散モデル対応でええ感じ）。
- **455**: Regional Prompterの描き分けでポーズ入れ替わり問題。comfyuiにした方がいいか？（理由：A1111系？の代替検討）。
- **460**: comfyでもRegional Prompter使用時に入れ替わり発生。プロンプト/分割比率で調整。
- **471**: ComfyUI移行1週間でワークフロー理解中。少しずつ出来る事が増えると嬉しい（初心者移行の喜び）。
- **474**: comfyUI 15.1環境でsage attentionエラー。env-manager抜いても変わらず（トラブル報告）。
- **476**: comfyアプデ恐怖症（sageAttention関連エラーで）。
- **478-479**: sageAttention（cu130用、pytorch 2.10対応のwoct0rdho氏版post4使用。アプデでバージョン入れ替えられ解決）。
- **480**: 古いカスタムノードインストールでnumpy/cv2上書き、Comfy起動不能。StabilityMatrixで修復。年単位更新なしノードは避ける（地獄のnote記事WF）。
- **481**: civi（Civitai）の野良WFは慎重に。更新日/requirements.txt確認推奨。代替ノード多用WFは不審。
- **482-484**: pip install -r requirements.txtでダウングレード禁止策議論（freeze/dry-run推奨）。
- **485**: ComfyUI-SAM3がcomfy-env経由でSageAttention/FlashAttention壊す原因。削除→comfy-envアンインストール→再インストールで直る。代替：easy-sam3（SAM3使いたい場合）。
- **489**: pngでWFアップロードが確実（ComfyUIのWF埋め込み？）。
- **493**: Forge NeoかcomfyでAnima軽く触る？（WebUI慣れならNeoお手軽、Comfy推奨？）。
- **494**: EasyWanみたいな統合機能は海外勢でもA111並再現なし（ComfyのWFでpngドラッグ再現便利。自作凄い）。
- **495-496**: codexでカスタムノード簡単作成可能。大変なのは動作確認（テストコードでログ出力→プロンプト入力でWF保存確認）。
- **513**: >>446のサンプルからWF作成不能（アホやから見せてもらいたい）。
- **514**: ComfyUIなら多人数絵で特徴混ざり/服装入れ替わり解消？（エアプ疑問）。
- **518**: Comfyのノード接続UIで独立キャラ認識しやすい？がモデル依存で変わらず。RegionalConditioning推奨。
- **521**: Comfyのノード線接続で物理的混ざりなし期待したが、モデル依存で変わらず。
- **523**: ComfyUI-SAM3抜いてeasy-sam3入れ、impact-packのmaskDetailer(pipe)接続不明（sageAttention壊れ回避）。
- **530**: sam3代替ノードでcustom_nodes/comfyui-sam3ディレクトリ重複（あるある）。
- **531**: json WF開いてComfyUIで正しく再現。pngメタデータはWebUI用（拡張子変え/ノード変えで対応）。
- **536**: githubにWF付きサンプルあり？
- **541**: Save Image With MetaDataはWebUIフォーマット。Comfy標準画像保存ノード/png、save image extended（tbg-etur）/webp推奨（ドラッグ&ドロップでWF再現）。
- **546**: portable環境でuv/pip併用問題（ComfyUI-SAM3関連）。
- **551**: webpはComfyUIで生成（プロンプト/パラメータ同じでjpg/Forge neo比較。破綻多め）。
- **561**: webpプロンプト取り出しにくい。png推奨（Comfy？）。
- **563**: sam3 detailer無し（荒っぽさ維持のため）。
- **569**: sam3 detailer無し。
- **574**: comfyだとjpg/webp取り出せない。
- **603**: tbg-eturのsave image extendedでwebp安定読み込み。ドラッグ&ドロップで赤枠/WF再現（ComfyUI標準）。
- **639**: easyreforgeからforge neoへAnima対応移行。Lora揃えても細部異なる（完全互換なし）。

#### Forge/Reforge/Neo (Reforge, Forge Neo, easyreforge, reForge)
- **455**: ReforgeでRegional Prompter使用中。受け攻めポーズ入れ替わり（comfy検討）。
- **493**: Forge NeoでAnimaお手軽（UI Preset=anima, VAE/Text Encoder指定。WebUI慣れ向け）。
- **498**: WebUI慣れならneoお手軽。
- **551**: Forge neoでjpg生成。
- **583**: reForgeのCFG矢印で0.1刻み面倒。設定項目なし？
- **610-611**: ForgeNeoでsampling steps=32上書き（Settings＞Presetsで解決）。
- **639**: easyreforge→forge neo移行（Anima対応問題なしだが細部違い）。

#### WebUI / A1111関連
- **494**: A111並の統合機能（海外勢でもComfyで再現なし）。
- **541**: WebUIフォーマットpngメタデータ（Comfyドラッグで標準WFのみ）。

#### SAM3 / FaceDetailer / 認識ツール関連
- **459**: 顔/衣装/H部位修正にSAM3（テキスト/ポイント選択）、FaceDetailer（服モデル+SAM_vit_I）。複数人物/衣装柄変更最適（検証済み）。
- **485**: ComfyUI-SAM3（comfy-env問題）。代替easy-sam3。
- **523**: easy-sam3でimpact-pack maskDetailer接続試行（不明で断念）。
- **563/569**: sam3 detailer無し（荒っぽさ維持）。

#### その他ツール/ノード
- **480/481**: StabilityMatrix（numpy/cv2修復）。Manager（カスタムノードインスト）。
- **541/603**: tbg-eturのsave image extended（webpメタデータ安定、ComfyWF再現）。
- **474/477-479/485**: sageAttention / FlashAttention（エラー多発、whl再インストール推奨）。

**抽出まとめ**: 主にComfyUI中心でカスタムノード/WF/環境トラブルが話題。選ばれる理由は「自作/カスタム拡張の柔軟性」「WF再現便利」「Regional Prompter描き分け」「SAM3/FaceDetailerの精密修正」「Forge NeoのAnimaお手軽UI」。トラブル（アプデ/依存/古ノード）が多く、代替/回避策共有活発。A1111系は過去比較で劣勢。