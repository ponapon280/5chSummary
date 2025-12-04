# 600スレ記念 AI生成スレッド（なんJ/5ch）レポート

## 概要
本スレはStable Diffusion系ツール（ComfyUI、Wan2.2、Illustrious、Z-image Turboなど）を中心とした生成画像・動画議論。主なトピックは新モデル（Z-image）の期待、ワークフロー（WF）トラブル、環境構築、エロ特化生成Tips。参加者は主にComfyUIユーザーで、RTX3090/4080環境が多く、初心者質問も活発。Z-image Turboが話題の中心で、Baseモデル公開待ちの熱気高まる。全体で実践共有が多く、解決策が即座に共有される雰囲気。

## 主要ニュース・アップデート
- **Z-image Turbo (ZIT)**:
  - トレーニングアダプターv2公開（v1の2倍サイズ、長時間学習。LoRA互換性向上）。実用レベルでSEXなし1girlエロ構図OKだが、イラスト幅狭くファインチューン待ち。
  - 実写/人物描写優秀（有名人、アニメキャラ、文字、自然、前後/逆立ち/漫画でZIT優位）。コントロールネットも登場。
  - 100万DL自慢で注目。Base/EditはModelScope公式Xで近日オープンソース予定（中国HF版）。
  - LoRA作成中（zuntanニキ活躍）。エロチューン待ち。

- **その他モデル/ツール**:
  - MiaoMiao RealSkin v1.1学習完了→Wan移行テスト中（髪グラデ良好だが異方性反射不足）。
  - HunyuanVideo-1.5: VRAM14GBで動作、Training code近日（Muon optimizer使用）。
  - Wan2.2: 獣姦LoRA（馬以外不足）、高速化LoRA前提。エミリア動画風生成試行中（プッシー開き難、膜吹き飛び）。
  - Genspark: FLUX2 Pro/ZIT対応。
  - Qwen3-VL-8B-NSFW-Caption-V4.5: エロ画像解析（日本語推奨、英語拒否多め）。LM Studio連携高速（GGUF推奨、auto_unloadでVRAM解放）。
  - Illustrious/Noob: 依然人気（waiは派生）。Z-imageはSDXL後継候補でDLC相当（リアス/NoobはZ-image上位版待ち）。
  - EasyWan22/EasyReforge: 現役。ComfyUI 0.3.75でSmoothMixより5-10%高速化。
  - raylight: GPU2枚分散（FSDP）気になり中、未検証。

- **環境アップデート**:
  - ComfyUI: 0.3.75で生成高速化。中止ボタン/フォーカスモード消失（設定「新しいメニューを使用」無効化で復元）。Frontend 1.30.6でUI変化。
  - ドライバ: RTX3090 560.94→566.36（定番）or 581.80/581.94（CUDA13対応）。
  - LM Studio: 推奨（高速・暴走なし）。ComfyUI連携スムーズ、GGUFでVRAM最適。

## トラブルシューティング
| 問題 | 解決策 | 報告者数 |
|------|--------|----------|
| EasyImageEditエラー（ファイル見つからず） | Windowsファイル名長さ制限解除（検索推奨）。Tritonキャッシュ削除も有効？ | 複数 |
| Wan WF壊れ（ノードコピペ不能、エラー） | パイパス+ノード切断/AnySwitch。Condition Selectorで遅延評価回避。サブグラフアンパック。 | 1-2 |
| ComfyUI-Impact-Subpackインストール失敗（UltralyticsDetectorProvider欠如） | custom_nodes手動削除→再インストール（Manager「Install missing」or git clone+requirements）。Nightly→ベータ版スイッチ。 | 複数 |
| プロンプト末尾カンマ自動削除 | AutoComplete Plusのauto formatter設定変更。 | 複数 |
| グラボ換装後ポータブルComfyUI動かず | git clone新環境構築（PyTorch/CUDAバージョン対応）。 | 1 |
| Wildcardプロンプトでseed固定せず変動 | Wildcardノードseedも固定。一括seedノード接続推奨。 | 解決 |
| Rife TensorRT高解像度ジャギー | 高解像度非対応確認。PainterI2V/LongVideo/WaveSpeed代替。 | 1 |

- **GPT信用度**: 嘘つき指摘多め。エラー時はレポート→チャッピー貼り付け推奨。

## 生成Tips・モデル評価
- **エロ構図プロンプト**:
  | 構図 | 推奨タグ（ネガティブ例） |
  |------|-------------------------|
  | 壁手ついて後ろからpussy広げ | `1girl,1boy,from behind,(spread pussy:1.2),ass focus,bent over,against wall,hands on wall,(cunnilingus:0.3)` ネガ: licking,tongue |
  | 手マン（下向き） | fingering（上向き注意）。尻出しポーズ+調整。 |
  | 引き/遠景 | `wide shot, very wide shot, distance view`（full body別）。モデル依存。 |
  | 強制フェラ | 女が女の頭押さえ（難）。POVPENISで簡易。 |

- **手法議論**:
  - デッサン人形→プロンプトガチャ vs Blender/MMD/Unityアニメ→v2v: AI依存大、MMD手間（足IK沼）。QuickmagicでMMD変換70点。
  - FaceDetailer: おまんまん/膜対応（ZITでサクサク）。
  - SDXL: エンパイア/ビッグベン多発（Building/Towerネガ）。

- **評価**:
  | モデル | 強み | 弱み |
  |--------|------|------|
  | ZIT | 描写精度高、LoRA実用 | イラスト幅狭、Turbo悪影響 |
  | Wan2.2/Illustrious | エロ出力安定、プニプニ質感 | WF壊れやすい、膜不安定 |
  | Noob | 愛用多 | - |

## その他議論
- **3D vs AI**: プロンプトガチャ速い（初心者ロボットダンス化）。
- **市場動向**: AI戦争（Mag7+OpenAI）。GPU枯渇継続。中国無料公開（国家戦略、寡占抵抗）。
- **未来予想**: Z-image Base待ち（QIE2511/LTX2延期）。チャッピーエロ解禁未達。Sora2無料30回復活。
- **雑談**: モブ顔健康食、マイクロビキニ歓喜、ばあさん/Z-image Base待ち。

**総括**: Z-imageブーム加速中。トラブル即解決文化強く、初心者歓迎。次スレでBase公開/LoRAエロチューン報告期待。質問時は詳細ログ共有を。