### 抽出された「ツール」に関する話題

ログから、指定されたツール（ComfyUI, A1111, webUI, SUPIR, nano-bananaなど）に該当する話題をすべて抽出。モデル（NAI, Pony, illustrious/リアス/ill/IL, Noobai, FLUX, Wan, Qwen）は除外。Anima, Forge(Neo/reForge), nano-banana, Tagger, ControlNet, Generate Foreverなども生成AIツール/拡張/UIとして扱い抽出。理由が明記されているものは併記。

#### ComfyUI (comfy)
- **258**: ComfyUIのカスタムノードを構築。GPU + モデルで利用可能なアテンションバックエンド（PyTorch SDPA, SageAttention, FlashAttention, xFormers）をベンチマークし、最速のものを自動適用。SDXL/Flux/WAN/LTX-V/Hunyuanなどのアテンションバックエンドルーレットを排除する目的。
- **260**: 上記カスタムノードを導入。Sage Attentionが1.9倍速い。
- **273**: ComfyUIのカスタムノードをわざわざ入れず、WEBサイトで最適組み合わせを知りたい。
- **274**: SageAttentionの生成速度向上（PyTorch SDPA比1.9倍速いが、KSamplerの一部処理のみ。全体では10-20%程度の差）。
- **324**: ComfyUIの構造は「剥き出しのエンジンとパーツ」を自分で組み上げる。A1111/SDXLと違い、Apple製品のような調整不要の簡単さがない。
- **421**: ComfyUIでanima生成時のサンプラー設定がほったらかし可能（forgeneoと違い起動時初期化されない）。
- **432**: ComfyUIでhires.fix相当のWFを組む場合、latent(nearest-exact) vs 画像(ESRGANなど)のノード/WFが異なる。bilinearの理由不明。R-ESRGAN 4x+ Anime6B/4x-UltraSharp使用。

#### A1111 / Forge系 (A1111派生UI: reForge, Forge Neo, easyreforge, Generate Forever)
- **276**: easyreforgeからforgeneoに移行で生成速くなったが、Generate ForeverがWindowsロック状態で止まる。設定対策？
  - **280**: 過去に複数回話題。公式Github(Haoming02)に報告要望のみ。
  - **281**: Generate Foreverはブラウザ上で完了検知→生成ボタン連打のローテク。タブスリープで死ぬ。chrome discardsでスリープ防止？
  - **289**: chrome拡張でissue対応様子見。
- **381**: forgeneoでprompt-all-in-one使えない？
  - **385**: 既出（過去スレ★623）。
- **396**: forgeneoに入れた良いアドオン？ reforgeのものを片っ端から？
  - **398**: Forge Neo専用アドオンなし。reForgeのものを入れるが、A1111/Forge機能削除やgradio 3→4で動かないもの多し。
  - **400**: プロンプトスペル修正、civitaihelper、wildcard対応アドオンがあれば十分。
- **414**: forgenéoにTagger入れると物故割れ。
  - **417**: torch互換ライブラリが原因で永遠に直らず。
  - **431**: Forge Classic/Neoでdeepbooru削除済みのためWD Tagger動かず。tensorflow/protobufバージョンの衝突で起動不能。tensorflow/tensorboard削除で起動。pip freeze > requirements.txtでバックアップ推奨。
  - **418**: TaggerはLoRA作り用。スタンドアロン版使用。
- **422**: forgeneoでanimaサンプラー初期化される。presetで選べば初期選択？
  - **424**: forgeneoでもpresetで初期サンプラー選べる。

#### nano-banana (NanoBanana, nanobanana2, QwenImageEdit)
- **264**: ControlNet使用で良し、NanoBanana/QwenImageEditでほぼ完璧。プロンプト単独使用は今時少ない。
- **320**: ナノバナナで生成上限きちゃった。回数少なくなった？
  - **324**: 2リリース同時で無料がpro誘導レベルにケチに。
- **337**: nanobanana2で生成後、proで生成し直す面倒。
- **338**: 毎回proスタート。

#### その他のツール
- **Anima**（画像生成ツール/UIとして頻出）:
  - **249/253/255/272/316/333/335/341/382/383/399/421/422/434/443/445/446**: Animaでプロンプト自動生成/Qwen3.5使用試行（テキストエンコーダー互換不可、エラー発生）。SDXL hires-fix時自然言語→danbooruタグ変換便利だが遅い。T5埋め込み次元一致もアダプタ必要。LLM大型化無駄（T5ボトルネック）。日本語FT可能？
  - **395**: Anima出力→アップスケーラ→SDXL i2iでhires。
- **ControlNet**:
  - **264**: ControlNet使用でだいたい良い。
- **Tagger (WD14tagger, deepbooru)**:
  - **255/339/356**: Florence2+Tagger複合プロンプトが良い。wd14taggerでSDXL十分（LLMより）。矛盾修整可能だがデノイズ調整次第。
- **SUPIR**: 該当なし。
- **その他（Perplexity, seedance, Irodori-TTSなど）**:
  - **245**: パープレ（Perplexity）にブラウザ不具合調査させ、ESETブラウザ保護機能特定（2時間解決）。
  - **334/344/346**: seedance2.0動画生成。日本不可/有料/クレカ恐い。litmediaで有料試用も男割り多発。
  - **373/377/378/397/403/429**: Irodori-TTS/Emoji-TTS（LoRA/LoHa/LoKr学習、faster-whisper pip install、uv sync仮想環境）。
  - **394**: A1111 img2imgでhires.fix使えず（SD upscaleは別）。ComfyUI WF難しい。

これでログ内の全ツール関連話題を網羅。理由明記のものは太字で強調。モデル話題（Qwen/Anima内でもモデル部分）は除外済み。