# なんJ NVA部 ログレポート (Res 850-1000)

## 1. スレッド概要
- **対象ログ**: Res 850〜1000（約150レス）。AI画像生成（主にStable Diffusion系）のなんJスレ「なんJNVA部★629」の後半部。
- **主なテーマ**: NSFW（エロ画像）生成の主流モデル議論、ComfyUI/Irodori-TTSのトラブルシュート、LoRA学習Tips、ZIB/Animaなどの新モデル評価。チャッピー（おそらくChatGPT系AI）のポンコツ回答をネタにしつつ、実践的な情報共有が活発。
- **雰囲気**: 技術者層の雑談寄り。エロ特化（巨乳/スカトロ/ロリ禁忌など性癖ネタ多め）、海外（4chan）比較、LLM（Gemini/Claude）批判。次スレ（★630）立て確認あり。
- **キーワード頻出**: Anima（Preview2含む）、ZIB/ZIT（Z-Image）、Illustrious、ComfyUI、Irodori-TTS、LoRA、NSFW、チャッピー、Gemini。

## 2. 主要トピックと議論まとめ

### 2.1 NSFWモデルの主流とトレンド
- **Anima系が圧倒的**:
  - Anima Preview2: 指改善、小物頑健度↑、版権キャラ安定↑、ブラ紐増殖なし。絵師タグ効き向上。chroma形式発表予想。
  - 複数LoRA混ざり対策: マスク分割（ComfyUI推奨）、複数キャラLoRA作成推奨。単独LoRAは1girl経由で混ざりやすい。
  - 浦島太郎勢の質問多め。「SDXL/Anima系でNSFW余裕」「Ponyは時代遅れ（4chan談）」。
- **ZIB/ZIT（Z-Image）評価**:
  - ZIB FT（アニメ/エロ特化）「ゲームエンダー」認定（Res914）。NSFW対応↑だが、胸サイズ（large breasts効き弱）で不満。naked nipples/large breasts明記必須、性器不可。
  - Turbo版: 実写系で検閲疑い（胸増大不可）。ベース未学習のためLoRA必須。
  - 学習推奨: ZIBでLoRA焼くとTurbo出来↑？
- **その他モデル**:
  | モデル | 評価 | 備考 |
  |--------|------|------|
  | Pony系 | 海外一部使用も「時代遅れ」 | 派生model主流？ |
  | Illustrious | 過去主流、現在更新で追いつけ？ NSFW弱め | ComfyUIベース |
  | SD1.5 | HF DL数多（A1111自動DL要因）。Pixiv1-2割現役、リアル有利 | SDXL超え無根拠論争 |
  | SDXL | NSFW強い。風景/オブジェクト微妙 | Anima/SDXL主流 |

- **Civitai/HF問題**: Civitai元画像がHFに継ぎはぎアップ。スカトロ/ゴア/自殺/薬物/ペド/おむつNG規約（Civitai）。

### 2.2 ツール/インストールトラブルと解決策
- **ComfyUI**:
  - 更新後: 変なロゴ（コカ・コーラ風）、タブ崩れ→WF開き直し/タブ閉じで対処。
  - **新機能: Appモード**（v0.17.0?）: WF→Appビルドで簡易UI化。スマホ対応、クラウドVRAM貧民救済。rgthreeノード非対応注意。
  - カスタムノード: ComfyUi_zaknak_nodes（マスク海苔修正）、ComfyUI-Qwen3.5（規制解除版接続難）。
- **Irodori-TTS（Emoji-TTS fork）**:
  | 問題 | 解決策 |
  |------|--------|
  | uv syncエラー（sentencepiece） | uv pip install faster-whisper（Whisper自動DL）。requirements.txt更新必須。 |
  | データセット前処理エラー（CSV） | JSONL出力（audio_path/text列名）。ラベル1行目列名ミス注意（file_name→audio）。 |
  | LoRA学習失敗（空フォルダ） | 出力パス明記。2800stepで変化なし→パラメータ調整/FT推奨。声高くなる→おっさんデータバランス。 |
  | キャプション生成スキップ | uv pip install requirements.txtで不足ライブラリ補完。 |

  - 作者らしきレス（Res913/931）でTips提供。LoRAマージ未知数、バグ疑い。
  - GUI改善要望: テキスト入力位置移動。

- **LLM連携**:
  - Qwen3.5 9B（Q4/Q6）+Anima: VRAM16GB余裕。自然語→Danbooru変換楽。VLでプロンプト修正。
  - Gemini: 劣化（嘘/サボり）多投下。PROは谷間/パンツ可だがエロ弱。AntiGravity待ち時間炎上。
  - Claude: TTSハマり解決推奨。Opus最強、エロ小説◎。

### 2.3 LoRA/生成Tips
- 複数キャラ: 頭部のみ複数LoRA、マスク分割。
- NSFW: Pony派生/Illustrious更新で追いつき？ ZIB FT待ち。
- 巨乳論争: large/gigantic breasts明記。ZIT体型幅狭（貧乳年齢下げ）。

### 2.4 雑談/ネタ
- チャッピーdis: NSFW/Pony回答ポンコツ。「並行世界チャッピー」。
- 性癖ネタ: デブ専、ジャバザハット、スカトロ文化差（欧米嫌悪強）。
- LLMスレ探し: wiki/>>47推奨。
- 次スレ: ★630立て（Res978）。

## 3. 注目ポイントと推奨アクション
- **初心者/復帰者向け**: Anima Preview2 + ComfyUI AppモードでNSFWスタート。ZIB FT監視。
- **トラブル多発**: Irodori-TTSはJSONL+uv pipで9割解決。Claude相談◎。
- **トレンド予測**: Animaエコシステム弱→ZIB FT/ZT進化待ち。ローカルLLM（Qwen）+Comfy連携強化。
- **注意**: Civitai規約厳格化。BOOTH版権通報可。

## 4. ログ終了時状況
- 次スレ移行（★630）。どんぐり復活、v0.17.0更新。Anima0.2癖強？質問ラッシュで締め。

このレポートはログのエッセンスを抽出。詳細ログ参照推奨。質問あれば追加分析可能。