# なんJ(5ch) AI生成スレッド ログレポート (レス226-426)

## 概要
- **期間/範囲**: レス226〜426の会話ログ。主にComfyUIを中心としたAI画像/動画生成ツールの議論。
- **主なトピック**: ComfyUIの更新・インストール方法、動画生成モデル（Wan2.2、LTX2、SVI）のワークフロー/エラー解決、LoRA適用、グラボ（RTX5090/4090など）トラブル/構成、NSFW生成Tips、実写/アニメモデル比較、ライセンス問題。
- **参加者の傾向**: ベテラン勢のTips共有、新規/低スペ環境ユーザーのトラブル相談。NSFW（エロ）生成が頻出で、技術的深掘りとジョークが混在。
- **全体のムード**: 活発な情報交換。エラー解決共有が多く、サンガツ（感謝）レス多め。次世代モデル（Zimageなど）への期待高まる。

## 主要議論点

### 1. ComfyUIの更新・インストール
- **バージョンアップデート**: v0.8.1 → v0.8.2（毎日更新ペース）。デスクトップ版はCore版より遅れ（v0.7.0止まり）、エラー多発で非推奨。ポータブル版/Git版推奨。
  - Git/clone + venvが汎用性高く、branch管理で戻し可能。Portableは初心者向け。
  - 更新方法: `update.bat`（デスクトップ）、pip install -r requirements.txt（venv）。
  - Dockerで攻守最強（上級者向け）。
- **問題点**: カスタムノード/バージョン衝突（CUDA/PyTorch）。新規勢難易度高め。--reserve-vram 4、preview method=NoneでVRAM安定。
- **新機能Tips**: サブグラフ多用（スッキリ化、モジュール化）。set/getはローカル名推奨（コピペ時重複回避）。階層in階層は避けろ。

| インストール方法比較 | メリット | デメリット |
|---------------------|----------|------------|
| Desktop版          | お手軽   | 更新遅れ、エラー多 |
| Portable版         | 即使用   | カスタムノード管理煩雑 |
| Git + venv         | 柔軟、戻し可能 | 初回セットアップ必要 |
| Docker             | 環境隔離 | 上級者向け |

### 2. 動画生成モデル・ワークフロー
- **LTX2 (LTX 2.0 Distilled)**:
  - 低スペ（3060/12GB, RAM32GB）で動くが13分/生成。テンプレWFから開始推奨。
  - エラー: smZNodes削除で解決。SEED Randomizeで同一動画再現（バグ？）。VRAM12GBでエラー多、16GB以上推奨。
  - 魚顔バタ臭、顔維持に画角固定。refine+upscale解像度低で顔崩れ。
- **SVI (Smoothmix SVI LoRA)**:
  - LoRA key not loadedエラー（fp8モデルNG？）。lora.py 9093行コメントアウトでログ抑制（WAN以外実害注意）。
  - 3種類（Wan2.2公式、派生、Kijai用）。前スレ確認推奨。バイク動画継ぎ目ミス修正で高速化。
  - NSFW版新登場（テスト依頼あり）。
- **Wan2.2**:
  - WF入れ替えで低スペ高速綺麗。エンドイメージ色ズレ（後端暗転、全フレーム薄亮）。カラーマッチ+デフリッカー（DaVinci Resolve）で抑制。
  - 巨乳物理表現弱（endimage差分推奨）。服脱がせ後高さ固定問題。
- **その他**: Subgraph多用WF増加。マルチGPUでLoRA/LLM有用（VRAM合算なし）。auto_unload=trueでLLM VRAM解放。

### 3. モデル・LoRA関連
- **アニメ/NSFW**: Illustrious（wai派生、v3.6まで）。noobベース注意（自然言語弱）。Danbooruタグ必須（自然言語NG）。2girls学習で複数キャラ容易。
  - LoRA作成: 原作コピー+CN誘導で128枚。単体+2girlsで10キャラ対応可（detailer併用）。
- **実写/次世代**: Qwen Image 2512（QI2512）主流。NSFW LoRA（SNOFS 1.3, 4/8step Lightning）豊富。ZIT/Zimage Edit LoRA期待（表情変化）。
  - 肌質難、構図偏り（リアス本家優位？）。背景ZIT（SAM3？）。
- **ライセンス**: SDキャラ商用NG多。YouTube非収益OK実状だが、クラウド/アバター（Vroid）推奨。モデル確認必須。

### 4. ハードウェア・環境
- **グラボ問題**: Amazonアウトレット5090→5080詐欺報告。5090+Pro6000理想。マルチGPU（余剰活用、LLM/LoRA向け）。MicroATXで2枚挿し難。
  - LTX2: 3080/12GBエラー、5090推奨。VRAM60%ダウン報告（v0.8.2+LTXVideo更新）。
- **低スペTips**: 量子化でLTX2可。ハイロウ載せ換え回避で高速。

### 5. NSFW/生成Tips
- Danbooruタグ化必須（自然言語無視）。fat manプロンプトOKだが問題あり。
- エロシチュ提案: Grok/SillyTavern活用。肌/物理法則弱（学習不足）。
- 実写エロ: QI + SNOFSで多ポーズ。Flux1 LoRA自作優位感。

## 新着/注目情報
- ComfyUI v0.8.2: VRAM減、sage attention警告消。
- Zimage Base: トレーニングコスト低、SDXL超え期待（FT待ち）。
- LTXVideo更新: VRAM最適化。
- 新エロWAN/SVI: テスト中。
- ワークフロー共有: >>395（整理版、smZNodes除去）。

## トレンド・示唆
- **移行期**: SDXL覇権継続もZimage/QI2512へシフト。動画NSFW強化（喘ぎ声/T2S進化待ち）。
- **課題**: VRAM/スペック壁、新規参入障壁高。サブグラフ/WF共有で効率化。
- **未来像**: LLM統合（RAG/Antigravity）、マルチGPU/クラウドハイブリッド。エロ生成効率化で「エネルギー→エロ変換」ジョーク流行。

このレポートはログのエッセンスを抽出。詳細確認は元ログ推奨。追加質問あればどうぞ！