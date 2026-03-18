### 抽出された生成AI関連「ツール」話題一覧

ログから、指定ツール（ComfyUI(comfy), webUI, nano-bananaなど）に該当する話題を抽出。モデル（NAI, illustrious/リアス/ill/IL, FLUX, Wan, Qwen-Image, anima, Z-Imageなど）関連は除外。Qwenシリーズは画像生成以外の話題のみ抽出（本ログでは該当なし）。ツールが選ばれている理由や言及の詳細を可能な限り記載。各レス番号付きで時系列順。

#### ComfyUI (comfy) 関連
- **652**: LLMプロンプトをanimaワークフローに載せてComfyUIに投げるだけ。VRAM12GBで動くなら問題ない（理由: シンプルな投げ込みで動作確認）。
- **659**: 自前のWFを使うとエラーでComfyUIに生成したLLMtext送れない。anima-pipeline-1.4.1にWF置いてポジティブ81ネガティブ12Kサンプラー19入力したがエラー（理由: 自前WF使用時の互換性問題）。
- **662**: >>595のノード比較（ノード無し vs ノード有り）。spectrum_w/m調整で発色調整、高速化もそこそこ（block 3,5,9, denoise_start0.6/end0.8, spectrum:true, w0.3 m24 lam1 warmup8）。理由: 高速化とパラメータ調整で有効。
- **663**: v1.4.2でLoRAありなし試したがエラー。Positiveノード81が存在しない。anima純正WF以外自前WF使いたい（理由: アプスケ/高速化ノード追加のため）。
- **667**: 高速化はeasycache/comple+併用で効くか？ Kサンプラー直前に置いたが生成速度変化なし（理由: 高速化検証）。
- **693**: 動画のためにComfyUIに手を出し始めた（理由: 動画生成開始）。
- **697**: ComfyUIの簡易UIモード実装されたか？ Forge NeoにAnima-Enhancer実装なら別（理由: 簡易UI期待）。
- **701**: RTX VSR2ノードで顔微細化機能欲しい（理由: 顔処理強化）。
- **706**: spectrumノードのパラメータ説明（block_indices, denoise_start_pct/end_pct, enable_spectrum, w/m/lam, warmup_steps）。二度漬けとSpectrum高速化の関係疑問（理由: 高速化/再生成最適化）。
- **709**: spectrumのワイ的設定（block:3,5,9 start:0.6 end:0.8 spectrum:true w:0.25 m:16 lam:0.95 warmup:9）。発色そのままシャープ高速化（理由: 発色維持しつつ高速化）。
- **717**: WF開いた後ComfyUI画面黒くなってノード見れなくなる問題（理由: 長期間のバグ）。
- **745**: >>709パラ参考にSpectrum使用。30stepが25s→18s短縮、絵柄変わらず彩度丁度良（理由: 高速化・品質維持）。
- **747**: easy cacheとSpectrumどっちが良いか（理由: 高速化比較）。
- **754**: Spectrum使うと絵師タグ効き悪くなる（理由: タグ影響検証）。
- **755**: Forge Neoの「Spectrum Integrated」オンで18.8s→9.8s（初期設定）。構図維持できず（理由: Forge Neo内高速化）。
- **762**: Forge Neo実装はcomfyui-spectrum-sdxlと微妙に違う（デフォルト値違い）。論文同じ（CVPR 2026）（理由: 動作比較）。
- **831**: ComfyUI難しそう（naiから移行検討）（理由: 学習曲線の高さ）。
- **835**: リアス/NAIなら素のreForge、安imaならForge Neo、いろいろならComfyUI（理由: 用途別最適ツール）。
- **842**: ComfyUIにapp modeできた。将来的一強？（理由: UX向上期待）。
- **844**: バックエンド一強だがUX壁厚い（理由: ユーザー体験の課題）。
- **845**: app modeはWF組める人前提（理由: 高度ユーザー向け）。

#### anima-pipeline 関連（animaモデル用ツールとして抽出）
- **659/663/725**: v1.4.1/1.4.2エラー修正。1.4.3公開、jsonからノードID自動検出追加。Kサンプラー直結ポジ/ネガ手動入力推奨（理由: LoRA WFバグ修正、自前WF対応）。
- **743**: git cloneしてanimaテンプレAPI jsonエクスポート、bat起動でrequests ModuleNotFoundError（理由: 初回セットアップ失敗）。
- **750**: bat含め修正版提供（理由: 起動エラー解決）。
- **753**: READMEにpip install requests記載？（理由: 依存インストール）。
- **761**: 修正版で起動・LLM生成成功（理由: 動作確認）。
- **769**: LLM使用時プロンプトに品質タグ+特徴重複（仕様か）（理由: プロンプト重複バグ）。
- **787/821**: 1.4.5公開、進捗%追加/バグ修正（理由: 重複修正など）。

#### Forge Neo 関連
- **697**: Anima-Enhancer実装されるなら話別（理由: Enhancer拡張期待）。
- **755**: Spectrum Integrated実装、時間半分（理由: 高速化）。
- **762**: comfyui-spectrum-sdxlと違い（理由: 実装比較）。
- **835**: animaならForge Neo推奨（理由: anima特化）。

#### nano-banana (Nanobanana) 関連
- **792**: Nanobanana Pro使用も元画像水増し劣化、キャラデザ/衣装崩れ（有料プランでも）。Banana無印並みトンチンカン（理由: 性能劣化不満）。
- **797**: 生成速度落ち劣化。Proで別キャラ/衣装（理由: ナーフ疑い）。

#### DaSiWa 関連（ツールとして抽出）
- **728**: 作者がLTX様子見（理由: 現段階価値なし）。
- **731**: DaSiWaニキ二次コン、現LTXはアニメ崩壊で価値なし（理由: 二次元特化のため）。

#### reForge / EasyReforge 関連
- **816**: reforgeアプデで再生成絵変わる（理由: アプデ影響）。
- **824**: easyreforgeインスコ失敗、SD公式リポ消滅で当然。昔移植で助かる（理由: 導入失敗）。
- **825**: フォークリポ有（理由: 代替）。
- **827**: eastreforge必要？ reForgeは1年前固定、古いモデル使用メリットなし。インスト途中でエラー（理由: 陳腐化）。
- **831**: reForgeから画像生成開始（nai移行）（理由: 初心者向け）。
- **835**: 素のreForge推奨（理由: リアス/NAI最適）。
- **843**: ワンクリック導入不可で初心者不向き（理由: wiki追記）。

#### Stability Matrix 関連
- **836**: ローカルスタートならStability Matrixインスト→reforge/comfy導入（理由: 初心者30分ポン出し）。
- **840**: Stability Matrix最高、web赤ちゃん→ローカル赤ちゃん30分（理由: 簡単導入）。
- **846**: SwarmUI入れればガワReforge（Stability Matrixで導入可）（理由: ComfyUI簡易化）。

#### SwarmUI 関連
- **846**: ComfyUIわからん奴はSwarmUI（連続生成/Wildcardタブ便利）（理由: 扱いやすさ）。
- **848**: SwarmUI扱いやすい、連続生成/Wildcard助かる（理由: UX優位）。

#### その他拡張/ノード（ComfyUI関連ツールとして）
- **667/674/675/694/698**: easycache/comple+（高速化競合？ spectrum true必須）。comple model+で22s→16s（理由: 高速化併用）。
- **745/746/754**: Spectrum高速化実感、彩度落ち着くが絵師タグ効き悪（理由: 速度向上・副作用）。
- **easy cache**: 747でSpectrum比較対象（高速化）。

これで全抽出完了。重複/文脈的にツール非該当（Geschar=5chアプリ、Claude/gemini=LLMなど）は除外。理由言及時は明記。