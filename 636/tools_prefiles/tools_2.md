### 抽出されたツール関連話題（モデル除外）

ログ全体から、生成AI関連の「ツール」（ComfyUI/comfy、webUI、Forge Neo、easy reforge、OpenClaw、rgthreeカスタムノード、Tiled SEGS、sam3、detailer、Python-Embed、ffmpegなど）に関する言及をすべて抽出。モデル（anima、illustrious/リアス、Wan、Qwen-Imageなど）関連は除外。Qwenシリーズの画像生成以外（LLM/テキストエンコーダー関連）は抽出。ツール選定理由が明記されているものは強調。

#### 237
- **Python-Embed**, **ffmpeg**  
  uv使わずPython-Embedを使ってセットアップするので何もない状態で動くはず。README.txtに書き忘れたけどffmpegが音声分析キャプションに必要なようなのでffmpegも入る。

#### 306, 311, 314, 315, 322, 326, 328
- **Python (バージョン3.10.6/3.13/3.12/3.13.12)**  
  新しいグラボに換装するのにこれまでずっと脳死でPython3.10.6で止まってたんやけど今安定版は何入れればええのん（>>306）。どのツールを使うかによるわ（>>311）。  
  **easy reforge**, **forge neo**, **comfy (ComfyUI)**  
  4070tiから5080tiの買い替えで**画像はeasy reforgeずっと使ってるからforge neoを使いたい**、wan動画もcomfyで遊んでる（>>314）。**Forge Neoはセットアップ時にvenvの仮想環境を作ってそっちに自動でPythonを入れてくれるから、システムにはPythonを入れる必要すらない**と思うで。ComfyUIも（venvじゃなくてembedded pythonやけど）同様（>>326）。**forge neoならREADMEに3.13.12推奨**と書いてるから悩む必要なんてない（>>328）。  
  **選定理由**: easy reforgeは継続使用（グラボ換装後も）。Forge Neo/ComfyUIはPython自動セットアップ（venv/embedded）でシステムPython不要のため便利。Pytorch Ver依存でグラボ指定（50XX系）で安定（>>315,322）。

#### 319, 323, 327, 329
- **ComfyUI**, **fast groups muter (rgthreeカスタムノード)**  
  comfyuiの**fast groups muter(rgthree)のオンオフのやつ並び替え**したいんやがどうすればええんや？（>>319）。プロパティで出来ないっけ？（>>323）。**propertiesのsortでcustom alphabetを選んで、その下のcustomSortAlphabetにグループ名を並べたい順をカンマで区切って書けばできる**よ（>>327）。

#### 333, 338
- **OpenClaw**  
  OpenClawの開発者が**READMEに書いてあることを質問してくる人が急に増えて困惑してる**っていってたの思い出す（>>333）。**OpenClawは情報秘匿マンにはマジでおすすめ出来ない**というか、秘匿すればするほど後出しすればするほど事故る確率が爆速で上がっていくンゴね（>>338）。

#### 341
- **ConfyUI (ComfyUIのタイポ)**  
  ConfyUIで**3DカメラUI導入**出来たわ。

#### 380
- **Tiled SEGS**  
  **Tiled SEGS経験したら離れられなくなった**わ。

#### 396
- **sam3**, **detailer**  
  **ハイヤー！するかsam3でdetailer**するかどっちなんや。

#### 411, 414, 415
- **Qwen3.5 (非画像生成LLM)**  
  非検閲**Qwen3.5**をイジってて思った。数百b以上のモデルなら出るのかもしれんが、手元にあるようなものじゃ微妙（>>411）。**gemma4は明らかにエロ小説の語彙力ええ**で（>>413比較）。**31bのheretic**やな。まあ**qwen3.5とかの同程度のモデル比**での話やね（>>414,415）。

#### 427, 432, 435
- **qwen_3_06b (テキストエンコーダー、非画像生成)**  
  AnimaのCLIPを**qwen_3_06bの検閲なしに差し替える**メリットってあるのか？（>>427）。**Wan2.2の時も同じくテキストエンコーダーを無検閲にしてる**のがあって試してみたけど結局プロンプト→出力はDiffusion model側で決まるから意味なくね？（>>432）。**標準のqwen_3_06bと無検閲版？で画像生成モデルに渡される情報にどんな差が出るん**やろか（>>435）。

### 補足
- ツール選定理由が明確なものは太字強調（例: Forge Neo/ComfyUIのPython自動化、easy reforgeの継続性）。
- クラウドサービス（Kling, seedance, runway）はローカル志向の文脈で言及あるが、ツール定義（ComfyUI等ローカルツール中心）に該当せず抽出除外。
- LLM全般（Gemini, chatGPT, Claude等）は生成AIツールとして曖昧のため除外（Qwen非画像のみ抽出）。
- 合計抽出レス: 約20件（ツール言及集中箇所）。重複/文脈ツールのみリスト化。