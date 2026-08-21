# 🆕 新規トピック（前回からの差分）
### 生成AI関連ツールレポート（ログ抽出に基づく）
- 純粋なツール・ワークフロー・最適化機能・補助アプリに焦点を当て、速度向上・低スペック対応・操作性・相性などの選定理由を記載

### Comfy Kitchen（kitchenattn / Sol-Attn実装、comfy-kitchen Attention）
- ComfyUI向けGPUカーネルライブラリ（C++/CUDA・ROCm最適化）で、Sage Attentionの代替として速度向上と品質改善を期待
- Spectrumや低ステップLoRA以外でも時間短縮を実感し、Sage Attention以外を使わなくなった事例あり

### Krea2
- Krea.ai提供の画像生成ツール（自然言語プロンプト対応、リアル・アニメ両対応）
- MiniMax H3との相性が良く、pony+LTXから画質向上、自然言語プロンプトが通りやすくidentity editで衣装・表情差分作成に強い

### 動画編集・後処理ツール
- DaVinci Resolveは高機能レンダリング（暗転問題はGPU設定で解決）
- 代替としてYMM4（UIが優しくモザイク処理向き）、Aviutl（機能性高）、Kdenlive（使いやすいが調整制限あり）を挙げる
- モザイク処理などの簡易性・UIの使いやすさを重視し、DaVinciの高機能さより用途次第でYMM4などを推奨

### その他の補助ツール・アプリ
- 自作プロンプト管理アプリ（インストール不要ポータブル版）でプロジェクト別管理・コピー機能によりメモ帳管理の煩雑さを解消
- Qwenシリーズ（LLM）をプロンプト作成・システムプロンプト用途に活用し、thinking ON/OFFで挙動制御（H3向けガイド読み込みやNSFW/年齢配慮の微調整に有効）
- Antigravity IDEをコード関連作業の代替として言及
- RVCを音声生成用途として言及

### 選ばれている主な理由の全体まとめ
- 速度・安定性としてComfy Kitchen、Attention最適化、ComfyUI更新を挙げる
- 相性・操作性としてKrea2 + MiniMax H3、自然言語プロンプト、公式テンプレートの信頼性を挙げる

### Web検索による参考情報
- Krea2はKrea.aiのテキスト-to-イメージモデル（2026年6月リリース）で美観重視・自然言語対応、Turbo版は高速生成、オープンウェイト版も提供
- 情報は2026年8月時点の公開情報に基づき、利用時は最新ドキュメント・GitHubを確認すること

---
# 元の本文
**生成AI関連ツールレポート（ログ抽出に基づく）**

ログから抽出された**モデル名（anima、NAI、FLUX、Wan、LTX、H3本体など）を除外**し、純粋なツール・ワークフロー・最適化機能・補助アプリに焦点を当ててまとめました。ツールが選ばれている主な理由（速度向上、低スペック環境対応、操作性、相性など）も可能な限り記載しています。

### 1. ComfyUI（および関連カスタムノード・ワークフロー）
ComfyUIは生成AIワークフローの主流ツールとして定着。ノードベースの設計によりカスタムノードの開発・組み合わせが容易で、複雑なパイプライン構築や最新機能への高速対応が可能。

- **選ばれている理由**:
  - ノード単位の柔軟性と拡張性が高く、他のUIでは難しい複雑ワークフローが組める。
  - 新機能（特にMiniMax関連）への「爆速対応」。
  - 公式テンプレートのVRAM/メモリ管理が優秀で、低スペック環境でも安定。
  - 更新（最新版）だけで生成速度が大幅向上（例: 36秒→22秒）した事例あり。
  - 将来的な持続的開発・資金調達を評価する声も。

**Comfy Kitchen（kitchenattn / Sol-Attn実装、comfy-kitchen Attention）**  
ComfyUI向けのGPUカーネルライブラリ（C++/CUDA・ROCm最適化）。行列演算やconvrot用のint8対応など。Sage Attentionの代替として注目され、速度向上と品質改善が期待される。

- **選ばれている理由**: Spectrumや低ステップLoRA以外でも明確な時間短縮を実感。Sage Attention以外を使わなくなった事例あり。将来的なComfyUI進化を期待して移行検討。

**その他のComfyUI関連設定・ノード**:
- `--fast-disk` / pinned memory: RAM使用量を大幅削減（40GB近く節約例）し、低スペック（RAM32GB、RTX 4060Ti/5070Tiクラス）でもContext Loopや長尺生成を可能に。
- VRAM節約ノード（Clear VRAM、chunk系）、Latent管理、Portable版推奨、カスタムノード最小化。
- Comfy MCP: リモート操作のレスポンス向上。
- RTX Video Super Resolutionノード: 低解像度運用時の画質補完。
- ref2v / リファレンス画像サイズ設定（match → max）: 原寸取り込みで画質有利。

**理由のまとめ**: 速度・安定性・低スペック耐性。公式テンプレート止まりで十分なケースが多く、GGUF化にこだわって失敗する事例を避けるため。

### 2. MiniMax H3関連ComfyUIワークフロー・機能
- **Context Loop**: 既存動画の続きを自然に生成・繋げる機能（シーン追加、Approve&continue対応）。VRAM/RAM使用量が変わらないため無限延伸可能。
- **Extender**: Context Loopより扱いやすいという評価。
- **Upscaler / Refiner / Latent Upscale**: 高解像度時の時間短縮目的（LTX技術転用などで改善）。
- **その他Tips**: i2v/r2vの使い分け、カメラ固定、Turboステップ比較。

- **選ばれている理由**: 5〜15秒動画の繋ぎやすさ、安定性、相性（特にKrea2との組み合わせで細部向上）。

### 3. Krea2
Krea.aiが提供する画像生成ツール/モデル（自然言語プロンプト対応、リアル・アニメ両対応）。

- **選ばれている理由**: MiniMax H3との相性が非常に良く、pony+LTXから数段階画質を引き上げ。プロンプトが自然言語（日本語）で通りやすい。identity editは衣装・表情差分作成に強い（動きはH3に譲る使い分け）。

### 4. 動画編集・後処理ツール
- **DaVinci Resolve**: 高機能レンダリング（暗転問題はGPU設定で解決）。
- **代替**: YMM4（UIが優しくクリック中心でモザイク処理向き）、Aviutl（機能性高）、Kdenlive（使いやすいが調整制限あり）。

- **選ばれている理由**: モザイク処理などの簡易性・UIの使いやすさ。DaVinciは高機能だが「めんどくさすぎる」ため、用途次第でYMM4などを推奨。

### 5. その他の補助ツール・アプリ
- **自作プロンプト管理アプリ**: インストール不要ポータブル版。プロジェクト別管理・コピー機能。理由: メモ帳管理の煩雑さを解消。
- **Qwenシリーズ（LLM）**: プロンプト作成・システムプロンプト用途。thinking ON/OFFで挙動制御（OFFで爆速、ONで賢くなる）。H3向けプロンプトガイド読み込みやNSFW/年齢配慮の微調整に有効。
- **Gemini / ChatGPT / Claude / aistudio**: ComfyUIワークフロー作成やエラー解決の補助。aistudioはエロ用途でBANリスク低減。
- **Antigravity IDE**: コード関連作業の代替として言及。
- **RVC**: 音声生成（過去の文脈）。
- **LM Studio**: Qwenのthinkingモード制御。

**選ばれている主な理由の全体まとめ**:
- **速度・安定性**: Comfy Kitchen、Attention最適化、ComfyUI更新。
- **低スペック耐性**: RAM32GB/中スペックGPUでも実用化（--fast-disk、pinned memory、VRAM節約ノード）。
- **相性・操作性**: Krea2 + MiniMax H3、natural languageプロンプト、公式テンプレートの信頼性。
- **実用性**: 差分作成・長尺生成・メモリ管理の容易さ。

---

## Web検索による参考情報
- **Comfy Kitchen (comfy-kitchen Attention)**: Comfy-Org公式の高速カーネルライブラリ（CUDA/Trition/HIP対応）。ComfyUIリポジトリにマージされ、Sage Attentionの代替として速度向上と品質改善が報告されている（2026年8月頃のReddit・YouTube・GitHub情報）。--use-ck-attentionフラグや専用ノードで利用可能。[[1]](https://www.reddit.com/r/StableDiffusion/comments/1vl8wqw/comfyui_comfykitchen_attention_speed_up/)[[2]](https://github.com/Comfy-Org/comfy-kitchen)
- **Krea2 (Krea 2)**: Krea.aiのテキスト-to-イメージモデル（2026年6月リリース）。美観重視で自然言語プロンプト対応、Turbo版は高速生成。オープンウェイト版も提供され、Krea.aiプラットフォームで利用可能。[[3]](https://www.krea.ai/)[[4]](https://venturebeat.com/technology/enterprise-grade-ai-image-generation-in-2-seconds-is-here-krea-2-raw-and-turbo-available-as-open-weights-under-custom-license)
- **MiniMax H3関連ComfyUIワークフロー（Context Loopなど）**: ComfyUI公式テンプレートやコミュニティノード（例: ComfyUI-MiniMaxH3-Contex-Loop）でT2V/I2V/R2Vや長尺延伸をサポート。ネイティブステレオオーディオ対応のオープンウェイトモデルとしてComfyUIでネイティブ統合が進んでいる。[[5]](https://github.com/ethanfel/ComfyUI-MiniMaxH3-Contex-Loop)[[6]](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- **ComfyUIメモリ機能（--fast-disk / pinned memory）**: ComfyUIの起動オプション/メモリ管理機能。--fast-diskはディスクバックド読み込みを優先し、pinned memoryはCPU-GPU転送高速化に寄与。低RAM環境でのモデルロード・長尺生成を支援。[[7]](https://docs.comfy.org/development/comfyui-server/startup-flags)[[8]](https://www.instasd.com/post/comfyui-vram-offloading-guide)

（上記は2026年8月時点の公開情報に基づく。実際の利用時は最新ドキュメント・GitHubを確認してください。）
