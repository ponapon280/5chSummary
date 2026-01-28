### 抽出された「ツール」関連話題

以下は、ログから生成AI関連の「ツール」（ComfyUI/comfy, A1111, webUI, SUPIR, nano-bananaなど相当するもの）に関する話題をすべて抽出・整理したものです。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwenなど）関連は除外。ツール選定理由や問題点・Tipsが明記されている場合を併記。

#### Forge Neo / Forge Classic（A1111のフォーク/UIツール）
- **848**: UV（おそらく拡張）をシステムにインストール、python/torchもシステムインストールが原因で--sageしたら動かなくなる。
- **849**: Forge Neo/Classicの--sageオプションはtriton 3.5とsage v2.2.0-windows.post4をインストールするだけ。Pytorch古いとエラー（torch 2.7ならtriton 3.3とsage v2.2.0-windows.post3対応）。**理由/Tips**: torch 2.9.0以上に更新推奨（面倒なら対応）。
- **850**: --sage消して--attention-pytorch付ければPytorch Attentionで起動、エラー回避。**理由/Tips**: バージョン不整合回避の代替起動方法。
- **851**: オリジナルのA1111捨ててForge Neo/Classicなど全部最新化検討。
- **852**: Stability Matrix v2.15.5でForge Neo/ClassicインストールするとPytorch 2.8.0になり--sageでバージョン不整合エラー。**理由/Tips**: Stability Matrixの罠だが愛用（詳しくなるため）。
- **854**: Forge Neo更新後モデル切り替え不可、クリーンインストールでもダメ（キャッシュ悪さ？）。
- **857**: Forge Neo 2.9はメモリ管理変更で問題多発（Issue未解決）、2.8（コミット3acf949）に戻す推奨。**理由/Tips**: 安定性優先でダウングレード。
- **858**: Forge Neo 2.8に戻す。
- **961**: easyreforgeneo（Forge Neo簡易版？）対応待ち。

#### Stability Matrix（インストール/マネージャーツール）
- **852**: v2.15.5でForge Neo/Classicインストール時Pytorch 2.8.0固定で--sageエラー。**理由/Tips**: 罠だが愛用（トラブル詳しくなる利点）。

#### A1111（Automatic1111 WebUI）
- **851**: オリジナルのA1111を捨てて最新（Forgeなど）に移行検討。

#### ai-toolkit（LoRA学習/トレーニングツール）
- **896**: ai-toolkitが（新モデル）対応待ち。Turbo時は対応速かった？
- **921**: ai-toolkitが（Z-Image）サポート。
- **924**: ai-toolkit対応遅れはゼロデイ実装が原因？
- **925**: ai-toolkit対応はUIオプション追加だけ？（モデル構造サポート済みで容易）。
- **927**: turboアダプタ付きtrain可能だったため、（新モデル）サポート容易。

#### ComfyUI（comfy）
- **853**: 同じ作業してるから質問OK、チャッピー（ComfyUI？）に聞く方が早いかも。
- **878**: Comfy公式も（新モデル）対応来た。

#### その他ツール関連言及
- **960-964周辺**: fp8scaled/nvfp4（量子化ツール/フォーマット）言及だが3000番台非対応で生成時間きつい（ツール選定理由なし）。

これでログ全体からツール関連を網羅。ツール選定理由は主に「安定性/バージョン互換性/エラー回避/インストール容易さ」で語られ、問題解決Tipsが多い。ComfyUIは「チャッピー」表記で間接的だが文脈上該当。