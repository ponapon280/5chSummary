**抽出されたツール関連話題（モデル関連は除外）**

- **ComfyUI（comfy）ワークフロー / ノード活用**
  - 2段階・3段階生成（通常モデル→turbo切替、hiresfix代替としての等倍i2i＋latent処理）のWF構築
  - turbo LoRAのオンオフ切替をスイッチノードやグループ分けで簡略化（CFG/ステップ一括切替、KSampler複数用意回避）
  - rgthree系ノード（Context Big、Fast Groups Muter、Groups Muter）の使用
    - 理由：モデル・ステップ・CFGをまとめて扱える、使わないグループをミュートして画面整理・動作軽量化
  - LoRA Block filter master系ノードの探し方・接続方法
  - shift値1活用時の多段階生成（構図出し→低denoise修正→ディテール調整）
  - Latent直接処理 vs 一度image化してから処理の比較検証
  - sageattentionの導入（エラー多発で苦戦）

- **WebUI / Forge / Forge Neo**
  - Forge Neo移行後のアップスケーラー問題（ScuNETが期待通りに動かない）
  - プリセット切替拡張の利用（設定切り替え簡略化）
  - 理由：Forge時代に愛用していたScuNETなどの互換性確認のため

- **アップスケーラー**
  - ScuNET（Forge時代からの愛用、RealESRGAN_x4plus_anime_6Bや2x_StarSample_V2.0_HQとの比較）
  - RealESRGAN / StarSample系との相性検証

- **学習・LoRA作成ツール**
  - Animarge（階層カット学習の簡易さ、デフォルト設定で十分）
  - LECO / iLECO実装（Anima向け魔改造、階層学習対応）
  - sd-scripts（Anima正規キー対応のための修正）
  - Anima Lora factory
  - LoRA自動作成マシーン（自作ツール）

- **その他ツール**
  - Copainter（ポーズ変換精度の高さ）
  - Irodori（音声メタデータ読み込み機能）
  - negpip（negative promptの効果向上目的でturbo併用時）

**特に選ばれている理由が明記されていたもの**
- ComfyUI：ノード分岐の柔軟性（turbo切替、hiresfix代替、グループミュートによる整理）
- rgthreeノード：複数パラメータの一括管理とグループ制御
- Animarge：階層学習が簡単でキャプション自然言語対応も良い
- Forge Neo：プリセット切替拡張との組み合わせ

**Qwenシリーズ関連**：該当なし

## Web検索による参考情報
- **Forge Neo**：Stable Diffusion WebUIの派生版の一つ。アップスケーラーの初期搭載が少なく、ユーザーが手動追加する必要がある仕様。
- **rgthree-comfy**：ComfyUI向け人気カスタムノード集。Groups Muter / Context Big などが含まれる。
- **Animarge**：ComfyUI向けLoRA学習支援ツール（階層適用・ブロックフィルタ系）。
- **sageattention**：ComfyUI向け高速化（attention最適化）拡張。環境依存でエラーが出やすい。
- **Irodori**：ローカルTTSツールの一つ（音声メタデータ扱い機能あり）。
- **LECO / iLECO**：LoRA編集・概念消去系学習手法。Anima（DiT系）では挙動がSDXL時代と異なる場合がある。