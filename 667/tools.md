# 🆕 新規トピック（前回からの差分）
### ComfyUI（comfy）
- 複雑なワークフロー中心ツール。JSONでAI連携しやすく、最新版でint8_convrot対応により生成時間短縮。Dynamic VRAM等でVRAM管理、各種ノード・マルチGPUも活用
- 直感的操作性が高く、Forge NeoのUI不満から戻る事例あり
- int8_convrot親和性が高く高速化フォーマットの標準化が進む
- StabilityMatrix経由のアプデ時requirements自動処理が便利

### StabilityMatrix
- ComfyUI等のパッケージ管理・アプデ自動化ツールでrequirements自動処理が便利

### Animerge
- Anima向けGUI。ADDifTのDPOモード（SDPO・MaPO）追加でwin/lose画像によるバイアス調整が可能、細かいニュアンス調整に有用
- ZIPは改行コードエラーが起きやすくgit clone推奨。仮想環境後start.batで起動
- 選定理由は導入容易さ（git管理）と学習機能の有用性

### nano-banana（バナナ）
- Google Gemini系画像機能の通称。盗撮シチュのスマホ画面一発再現性が高い
- 選定理由は一発での画面同期・構図再現性の高さ

### ai-toolkit（Ostris製）
- LoRA作成主力。ちびたいWEB経由でも利用、キャプション後学習に使用。alphaを論文ベース制御する事例あり
- 選定理由は消費者向けHWで最新モデル対応のオールインワン、Krea2利用例多数

### kohya_lora_gui / kohya_lora_param_gui（RedRayz改良版） / kohya_ss
- RedRayz氏krea2対応改良版。CAME・3エポック・fp8_scaled等で成功、512×512高速プリセット推奨。解像度とバッチが時間に影響、ダークテーマ対応あり
- kohya_ss v25.2.2リリース、sd-scripts対応ファイル必要。GitHub公開で匿名性・安全性を評価

### ちびたいWEBトレーニング
- Krea2用LoRA焼成。デフォルト2000ステップ約2時間、adamw8bit・dim/alpha32・resolution1024等

### ComfyOrg / kijai の int8 conv 変換ツール
- kijai氏がComfy公式にpushしたスクリプトでINT8_convrot化（約1分）。Animaでサイズ半減・生成時間ほぼ不変
- 選定理由は公式/kijai製の安心感、容量節約による負荷軽減、主要開発者推進で標準化見通し

### ADDDifT（Animerge内など）
- 短時間で確実に効くお手軽スライダー作成可能（例: 夕日効果、5090で約1分）。強すぎる場合あり
- 選定理由は短時間・確実な効果

### その他
- convert_to_quant: hermesに使わせて変換
- KDENLIVE: エロ動画モザイク付けが手軽
- zluda: 格闘中に誤削除の事例
- openrouter: 中華モデルで公式契約より良い提案

### プロンプト作成・キャプションツール
- 自作プロンプト作成ツール: 構図登録・ワイルドカード対応で手短に使える。1語暗記＋オートコンプリート派の反対意見も
- TIPO: 表情系プロンプト投入
- Tagger（WD/Oppai Oracle等）: Danbooru学習がLLMよりエロ分析に優れ、しきい値調整でタグ抑制。LLM連携でdescribe、タグ過多でエラーあり
- joycaption等: VLキャプション特化で再現度高い

### ローカルLLM実行ツール
- LM Studio: Ollamaより楽、model searchで即DL・API有効化。ComfyUI連携可。llama.cppラッパーでキャッチアップ遅延しがち
- llama.cpp/llama-server: Ollamaより推奨。環境をAIに伝えれば導入可能、直接触る派
- Ollama: 不評。gguf createのSSD書き込み仕様が非推奨、性能・炎上指摘あり
- lemonade: 軽くて速いがシステムプロンプト機能なし
- 運用例: LM Studio+VS Code+Qwen3.6-27B。日々はローカル・大規模はクラウド。役割分担（選別・要約OK、最終実装は危険）を明確化

### ChatGPT Plus / Codex / Pro
- ゲーム開発で使用量枯渇、Pro（約16800円）推奨。Codexは一発実行・GitHub連携が強み

### その他LLM
- Gemini: PCIレーン相談や教師画像作成
- Claude/Fable: 高度なコーディング用途（上位プラン）
- deepseek API: 安価でコーディング良好（claude中間）、規制緩い。openrouter経由でお試し推奨
- Qwen3.6系: ローカルコーディング・エージェント適性高く壁打ち相手として運用

### SCAIL-2
- ダンスのキャラ置き換えは容易、絡みAVはポーズ検出で厳しい。TikTok転写・1分動画例あり
- 選定理由はダンス等の置き換えが比較的簡単

### TRIPO
- 画像から3Dモデル化。ローカル手法と月とスッポンの品質差
- 選定理由は圧倒的な品質

### Civitai
- kreaトレーニング対応。モデル/LoRA配布中心だがAPIバグ・BEST MATCH不透明・ファイル名衝突等問題多発。メタデータ認識改善
- Hugging Face（hf download）: DL失敗時の確実な手段

### 選定理由の総合まとめ
- ComfyUI + MCP: 柔軟性・AI支援正確性・int8親和性・直感操作
- Forge Neo: 速度・INT8対応の手軽さ（UI不満あり）
- ai-toolkit / kohya系: プリセット優秀・高速・Krea2対応・GitHub信頼性
- int8_convrot変換: サイズ半減・速度/精度向上・公式/主要開発者推奨
- LM Studio / llama.cpp: 導入しやすさ・Ollamaの不評回避
- Codex / deepseek: コーディング精度・コスト・リミット
- nano-banana / SCAIL-2 / TRIPO / ADDDifT: 一発再現性・手軽さ・品質差・短時間効果
- git clone（Animerge等）: 改行コードエラー回避・バージョン管理・安全性
- 全体傾向: ComfyUI中心の柔軟性＋int8高速化、LoRAはai-toolkit/kohya改良版が活発、ローカルLLMはLM Studio/llama.cppへシフト、クラウドはdeepseekやCodex推。選定鍵は安心感・時短・互換性
- 必要に応じて投稿番号付き引用や時系列再整理が可能

### Web検索による参考情報
- ComfyUIとINT8 ConvRot: 0.27.0等でネイティブINT8/INT8-ConvRotサポート導入。kijai氏・Comfy-Orgが各種int8_convrotモデルをHF提供、品質-性能比が優れる
- ai-toolkit: 拡散モデル向けオールインワンLoRA/FTスイート。Z-Image・Flux・Krea2等で人気、消費者HW対応
- kohya_ss / kohya_gui: v25.2.2リリース。Krea2向けmusubi-tunerやレシピがHF公開
- Animerge: iron-mukakin製。ADDifTにSDPO/MaPO実装追加、Anima向けGUI
- SCAIL-2: Z.ai製キャラアニメ/置き換えFW。骨格中間表現バイパス、ComfyUIワークフロー多数
- nano-banana: Google Gemini系画像生成/編集の通称。高精度テキスト・キャラ一貫性・編集能力で評価
- Qwen3.6: Alibaba最新シリーズ。エージェントコーディング強化、ローカルコーディングで高評価
- ComfyUI MCP: 公式・コミュニティサーバーでAIエージェントがワークフロー制御可能
- TRIPO: テキスト/画像から3D生成。高速高品質で各種形式エクスポート
- CivitaiとKrea2: 関連LoRA多数、公式TrainでKrea2 LoRAベータ対応。API variant問題は議論中
- deepseek API: 安価でコーディング適性高くOpenAI/Anthropic互換
- StabilityMatrix: LykosAI製マルチPFパッケージマネージャ。ComfyUI等をワンクリック管理
- WD Tagger: SmilingWolf製、ComfyUIノードとして広く利用、Danbooruタグ特化
- 量子化（INT8 ConvRot）とMCP連携が2026年トレンド。最新はGitHub/HF/Civitaiで確認推奨

---
# 元の本文
# 生成AI関連ツール レポート

ログから抽出された生成AI関連の「ツール」話題（モデル本体の性能・絵柄比較は除外。Qwen系は画像生成以外のみ採用）を整理・分析したレポートです。特に**選定理由**が明記されているものを強調してまとめます。ツールは主に画像生成ワークフロー、LoRA学習・変換、ローカルLLM運用、コーディング支援、周辺ユーティリティに分類されます。

## 1. 画像生成UI・ワークフローツール

### ComfyUI（comfy）
- **概要と利用状況**: 複雑なワークフロー構築の中心ツール。JSONベースのためAIとの連携（ノード作成・エラー修正）がしやすい。最新版（例: 0.27.0 + PyTorch 2.12.1+cu130）でint8_convrot対応が進み、生成時間短縮（例: animaで約25%、krea2で2割程度）が確認された。Dynamic VRAMや`--enable-dynamic-vram --novram`などの起動オプションでVRAM管理。GenerateTextノードやtaggerノード、潜在アプスケ、マルチGPU対応も活用。
- **選定理由**:
  - 直感的な操作性が高い（Forge NeoのError多発・UIのゴチャゴチャを嫌って戻る事例あり）。
  - ワークフローの柔軟性・カスタムノードとの組み合わせが優れる。AIに全部任せるより「自分で組み立て＋AI製カスタムノード」がベスト。エラー参照・循環参照の特定でAIが強い。
  - int8_convrotとの親和性が高く、高速化フォーマットの標準化が進む。
  - MCP（Model Context Protocol）連携でAIエージェント支援が正確。WebUI単体よりIDE＋MCP環境推奨。
  - StabilityMatrix経由でアプデ時のrequirements自動処理が便利。
- **運用Tips**: 公式ワークフローでLoRA有効時の問題あり（専用ノード必要）。Note多用による情報漏洩懸念で投稿減少の傾向も。推奨環境としてpytorch2.12+cu130以降。

### WebUI / Forge Neo（Haoming02氏開発）
- **概要**: 個人開発ながら更新が早く、ComfyUIの機能・ソースを流用。INT8 ConvRot正式対応（当初ブランチ、後に本体マージ）。生成が「クソ早い」との評価。Anima・ZITなどで変換確認済み。
- **選定理由**:
  - 生成速度が速く捗る。INT8対応でWebUIから簡単変換可能。
  - fp8より速度・精度が上（特にRTX40以降でも有効、Haoming氏が「fp8をお墓に入れた」と評される）。
  - 一方でError連発・UIが見にくいとの不満からComfyUIに戻るケースあり。よく分からなければマージ待ち推奨。
- **その他**: 更新の速さへの言及。int8が下りてきて話題についていけるとの声。

### StabilityMatrix
- ComfyUIなどのパッケージ管理・アプデ自動化ツール。アプデの度にrequirementsを自動で叩く点が便利。

### Animerge
- Animaモデル向けデスクトップGUI。ADDifT学習のDPOモード（SDPO・MaPO実装）を追加。win画像（望む表現）とlose画像（嫌う表現）でバイアス経路を調整。LECOに近く細かいニュアンス調整に有用。
- **インストール注意**: ZIPだとbatの改行コード（LF）でエラーが起きやすい。**git cloneからのセットアップ推奨**（バージョン管理・安全性）。仮想環境作成後はstart.batで起動可能。
- **選定理由**: 導入の容易さ（git管理）と学習機能の有用性。

### nano-banana（バナナ）
- 画像編集・生成ツール（Google Gemini系の画像機能の通称として使われる事例）。盗撮シチュで「スマホに写る画面」を一発で出す再現性が高い。
- **選定理由**: 一発での画面同期・構図再現性の高さ。

## 2. LoRA学習・変換ツール

### ai-toolkit（Ostris製）
- LoRA作成の主力。ちびたいWEBトレーニング経由でも`engine: "ai-toolkit"`として利用。キャプショニング後の学習に使用。alpha設定を論文ベースで制御する事例あり（デフォルトロジックの解除が必要な場合）。
- **選定理由**: 消費者向けハードウェアで最新モデル対応のオールインワン。Krea2などでの利用例多数。

### kohya_lora_gui / kohya_lora_param_gui（RedRayz改良版） / kohya_ss
- RedRayz氏のkrea2対応改良版。CAME・3エポック・fp8_scaledなどで成功例（5060Ti 16GB/128GBで約4時間）。**512×512高速プリセット＋p3版**で1時間未満・出来が良いと推奨。解像度とバッチサイズが時間に最も影響。ダークテーマ要望対応あり。
- kohya_ss v25.2.2リリース。sd-scripts側対応ファイル必要。直接配布を避けGitHub公開で匿名性・安全性を評価。
- **選定理由**: プリセットの優秀さ・高速性。GitHub公開による信頼性。

### ちびたいWEBトレーニング
- Krea2用LoRA焼成。デフォルト設定・2000ステップ・約2時間完了例。パラメータ例: adamw8bit、dim/alpha 32、resolution 1024など。

### ComfyOrg / kijai の int8 conv 変換ツール
- Comfy公式にkijai氏がpushしたスクリプトで通常チェックポイントをINT8_convrot化（約1分）。Animaで数秒・サイズ半減、生成時間ほぼ変わらず。
- **選定理由**: 公式/kijai製で安心。容量節約＝負荷・速度軽減。主要開発者（kijai, comfyanonymous, Haoming）が推進。標準化が進む見通し。

### ADDDifT（Animerge内など）
- 短時間で確実に効くお手軽スライダーが作れる（例: Anima用夕日効果もどき、5090で約1分）。強すぎる場合あり。
- **選定理由**: 短時間・確実な効果。

### その他
- negpip: ノード接続で動作確認。
- convert_to_quant: hermesに使わせて変換。

## 3. プロンプト作成・キャプションツール

- **自作プロンプト作成ツール**: 構図登録・ワイルドカード対応。「今日はこのシリーズと構図で」と手短に使える。一方で「1語ずつ暗記＋オートコンプリートが早い」との反対意見も。
- **TIPO**: 表情系プロンプト投入。
- **Tagger（WD Tagger / Oppai Oracle v1.1など）**: Danbooru学習の方がLLMよりエロ分析に賢い。しきい値調整（デフォ0.35/0.85）でタグ抑制。LLMとの連携（タグをプロンプトにフィード）でdescribe。タグ過多でエラーになる場合あり。
- **Google翻訳ノード / LLMノード / fable製変換ツール**: 日本語→自然文やbooru語→自然言語。手軽さ・効率化が理由。LM Studio / openrouter / nanoGPT / xaiAPI併用。
- **joycaptionなど**: VLキャプション特化で再現度高い。

## 4. ローカルLLM実行ツール


| ツール | 評価・選定理由 |
|--------|----------------|
| **LM Studio** | Ollamaより楽。model searchで即DL。API有効化。ComfyUI連携やGenerateText経由で利用。MTPや技術的限界で風向き変化の噂も。llama.cppラッパーのためキャッチアップ遅延しがち。 |
| **llama.cpp / llama-server** | Ollamaより推奨。環境をAIに伝えればインストール・パラメータが得られる。直接触る派。 |
| **Ollama** | 不評。gguf createで同一物をコピーしてSSD書き込み仕様が非推奨。性能・炎上（llama.cpp隠蔽・遅さ）の指摘。APIは最初から有効。 |
| **lemonade** | 軽くて速いがシステムプロンプト機能なし。 |

- **運用例**: LM Studio + VS Code + Qwen3.6-27B。Gemma4は日本語優秀だがコーディングはQwen3.6に劣る。日々のルーチンはローカル、大規模はクラウドに骨子を組ませる。Ollama + Qwen3.6で短コンテキストは架空変数リスク、長めなら実用。役割分担（選別・要約はOK、最終実装は危険）を明確化。
- VRAM例: 5080(16GB)+3080(12GB)。

## 5. クラウドLLM・コーディング支援ツール

### ChatGPT Plus / Codex / Pro
- ゲーム開発で使用量枯渇。Pro（約16800円）推奨（リミット大、GPT 5.5/5.6 Proで壁打ちが捗る）。Codexの強み: 言ったことを一発でやる、GitHub連携。
- **選定理由**: カスタムノード・コーディング・構造化データでWeb ChatGPTよりIDE/Codex向き。Plus＋ローカルで完成させてからPro検討の慎重派も。
- Tips: 画像生成ツール起動禁止を毎回指示。WFは一個ずつ聞く。理解負債回避のため全体任せは避け、ノード作成・修正方法を聞く程度が適切。

### その他LLM
- **Gemini**: PCIレーン相談や教師画像作成。
- **Claude / Fable**: 高度なコーディング用途（上位プラン）。
- **deepseek API**: マジで安い・コーディング性能良好（claude opus/sonnet中間）、規制緩い。お試し推奨。openrouter経由。
- **Qwen3.6系（27Bなど）**: ローカルコーディング・エージェント適性が高い。壁打ち相手として運用。

## 6. 動画・3D・その他プラットフォーム

### SCAIL-2
- ダンスなら簡単にキャラ置き換え可能。絡みのあるAVはポーズ検出で躓き厳しい。TikTok転写や1分動画作成例（面倒で続かない場合あり）。
- **選定理由**: ダンス等の置き換えが比較的簡単。

### TRIPO
- 画像から3Dモデル化。ローカル手法に対し月とスッポンレベルの品質差。
- **選定理由**: 圧倒的な品質。

### Civitai
- kreaのトレーニングが対応（速さに言及）。モデル/LoRA配布・DL中心。APIバグ（variants指定不可でfp8しか落ちない）、BEST MATCH不透明、ファイル名衝突などの問題多発。Stability Matrix / Civitai Helperはvariant選択不可。メタデータ認識改善（Comfy標準外ノードも識別）。
- Hugging Face（hf download）: ダウンロード失敗時の確実な手段。

### その他
- KDENLIVE: エロ動画モザイク付け（手軽）。
- zluda: 格闘中に誤削除の事例。
- openrouter: 中華モデルで公式契約より良い提案。

## 選定理由の総合まとめ


| ツールカテゴリ | 主な選定理由 |
|----------------|--------------|
| **ComfyUI + MCP** | 柔軟性・AI支援正確性・int8親和性・直感操作 |
| **Forge Neo** | 速度・INT8対応の手軽さ（ただしUI不満あり） |
| **ai-toolkit / kohya系** | プリセット優秀・高速・Krea2対応・GitHub信頼性 |
| **int8_convrot変換** | サイズ半減・速度/精度向上・公式/主要開発者推奨 |
| **LM Studio / llama.cpp** | 導入しやすさ・Ollamaの不評回避 |
| **Codex / deepseek** | コーディング精度・コスト・リミット |
| **nano-banana / SCAIL-2 / TRIPO / ADDDifT** | 一発再現性・手軽さ・品質差・短時間効果 |
| **git clone (Animergeなど)** | 改行コードエラー回避・バージョン管理・安全性 |

全体傾向として、**ComfyUI中心のワークフロー柔軟性＋int8高速化**が進み、LoRA学習はai-toolkit/kohyaの改良版が活発。ローカルLLMはOllamaからLM Studio/llama.cppへシフト。クラウドはコストとコーディング適性でdeepseekやCodexが推される。ツール選択は「安心感（公式/有名開発者）」「時短・手軽さ」「互換性」が鍵。

必要に応じて投稿番号付き引用や時系列再整理が可能です。

## Web検索による参考情報

モデル名・バージョン・新サービス等についてWeb検索で事実関係を確認した結果をまとめます（2026年7月時点の情報に基づく）。

- **ComfyUIとINT8 ConvRot**: ComfyUI 0.27.0などでネイティブINT8/INT8-ConvRotサポートが導入（PR #14636など、2026年6月頃マージ）。kijai氏やComfy-OrgがKrea2、Z-Image、Qwen-Image-Edit、LTX-2.3などのint8_convrotモデルをHugging Faceで提供。品質-パフォーマンス比が優れる（GGUF Q8に近い品質でFP8 Scaled並み/それ以上の速度）。ネイティブローダーで動作し、カスタムノード不要のケース多数。Kijai氏によると、Krea2の敏感層でint8-convrotが特に有効。[[1]](https://www.reddit.com/r/StableDiffusion/comments/1ukjhag/krea2_int8_convrot_vs_fp8_scaled_in_comfyui_270/)[[2]](https://github.com/Comfy-Org/ComfyUI/issues/14722)[[3]](https://huggingface.co/obsxrver/ComfyUI-Native-INT8_ConvRot)

- **Forge Neo（Haoming02 / sd-webui-forge-classic neoブランチ）**: 個人開発で活発に更新。INT8 ConvRot対応が2026年7月頃コミットされ、リリース版2.27で正式対応予定。ComfyUI機能を流用しつつ軽量WebUIとしてFlux、Qwen、Wanなどをサポート。fp8よりINT8を推す動向。[[4]](https://github.com/Haoming02/sd-webui-forge-classic/blob/neo/README.md)[[5]](https://note.com/hirorohi03/n/n047a8c5f7f8b)

- **ai-toolkit（ostris/ai-toolkit）**: 拡散モデル向けオールインワンLoRA/ファインチューニングスイート。Z-Image、Flux、Krea2などで人気。ワンクリックインストーラやComfyUI推論パリティワークフローが存在。消費者ハードウェア対応を強調。[[6]](https://github.com/ostris/ai-toolkit)

- **kohya_ss / kohya_gui**: bmaltais/kohya_ssがv25.2.2を2026年7月8日頃リリース。Gradio GUIでsd-scriptsをラップ。Krea2向けにmusubi-tuner（kohya-ss）やレシピがHugging Faceで公開。[[7]](https://github.com/bmaltais/kohya_ss)[[7]](https://github.com/bmaltais/kohya_ss)

- **Animerge**: iron-mukakin/Animergeが存在。ADDifT学習にSDPO/MaPO実装を追加（2026年7月頃のコミット）。Animaチェックポイント・LoRA向けGUI。[[8]](https://github.com/iron-mukakin/Animerge)

- **SCAIL-2**: Z.ai（Zhipu AI）リリースのキャラクターアニメーション/置き換えフレームワーク。エンドツーエンドで骨格中間表現をバイパス。ComfyUIワークフロー多数（ダンス、マルチキャラ、クロスアイデンティティ置き換え）。FP16/FP8/GGUF対応。2026年6月頃注目。[[9]](https://teal024.github.io/SCAIL-2/)

- **nano-banana**: Google Gemini系の画像生成/編集機能の通称（Nano Banana 2 / Gemini 3系Flash Imageなど）。高精度テキストレンダリング、キャラ一貫性、編集能力で評価。Google AI StudioやGeminiアプリで利用可能。[[10]](https://aistudio.google.com/models/nano-banana)

- **Qwen3.6**: Alibaba Qwenチームの最新シリーズ（2026年4月頃）。27B denseや35B-A3B MoE。エージェントコーディング・思考保持に強化。LM Studio、Ollama、llama.cppで利用可能。ローカルコーディングで高評価。[[11]](https://huggingface.co/Qwen/Qwen3.6-27B)

- **ComfyUI MCP**: Model Context Protocol対応が進み、公式Comfy Cloud MCPやコミュニティサーバー（joenorton/comfyui-mcp-serverなど）が存在。AIエージェントがComfyUIワークフローを制御可能。2026年6-7月に注目。[[12]](https://github.com/joenorton/comfyui-mcp-server)

- **TRIPO (Tripo3D)**: テキスト/画像から3Dモデル生成サービス。高速・高品質でGLB/STL/OBJエクスポート。シングル/マルチビュー対応。[[13]](https://www.tripo3d.ai/)

- **CivitaiとKrea2**: Krea2関連LoRA・ワークフローが多数投稿。公式TrainツールでKrea2 LoRAトレーニングがベータ対応（2026年5月以降）。ai-toolkitとの連携例多い。APIのvariant問題はコミュニティで議論。[[14]](https://www.krea.ai/blog/public-loras-krea-2-train)

- **deepseek API**: 安価でコーディング適性が高く、OpenAI/Anthropic互換。エージェントツール統合が進む。V4シリーズなど。[[15]](https://api-docs.deepseek.com/)

- **StabilityMatrix**: LykosAI製のマルチプラットフォームパッケージマネージャ。ComfyUI、A1111、Forgeなどをワンクリック管理・更新。[[16]](https://github.com/LykosAI/StabilityMatrix)

- **WD Tagger**: SmilingWolfのWaifuDiffusion Tagger（WD14など）がComfyUIノードとして広く利用。Danbooruタグ生成に特化。[[17]](https://huggingface.co/spaces/SmilingWolf/wd-tagger)

これらのツールは活発に更新されており、特に量子化（INT8 ConvRot）とMCP連携が2026年のトレンドとして確認されました。最新情報はGitHub/Hugging Face/Civitaiで確認を推奨します。
