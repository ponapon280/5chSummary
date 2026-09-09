## 生成AI関連ツール話題 抽出レポート

### ComfyUI関連

**ComfyUIのAttention系ノード**
- comfy kitchen attentionアプデとblock sparse attention実装により、RTX40xxや50xxのattention周りが改善。sageより品質・スピードともに良く感じるとの感想(241)。
- block sparseノードにメモリリークがあったが、今朝(9:33のコミット)のアプデで修正された。低vram環境でstepが進むとvramが溢れOOMになっていたのが解消(252, 255)。
- Block Sparse AttentionのselectionをSol-Attnからtop-k(SLA)に変更したら、不自然に変化していた固定背景が変化しなくなった。不自然変化の原因はSol Attentionだった可能性(319)。
- 作画崩れを直したい場合はstep値ではなく、Block Sparse Attentionノードのselectionをtop-kにし、keep percentの値を20まで上げると良い。step値を変えると別物になるため推奨しない(395)。
- ノード名について、後ろに(top-k)と付いているノードを使っている人もおり、Sol attenのように類似名ノードが多数存在する(291)。
- sage attentionを起動オプションに入れると何かの画像生成機能がしなくなる現象があった(251)。Qwen Imageでsageのせいで真っ黒画像が生成されることはあるが、背景だけ真っ黒になることはないとの反論(254, 256)。

**ComfyUIのVAE関連**
- Fast VAEかTRT VAEでVAEの処理を軽くする提案(241)。
- TRT VAEを使用したが、VAEのint8convrotと速度があまり変わらなかった。生成サイズが大きい方が恩恵を感じられるかも(243)。
- TRT VAEの精度はFP16であり、int8 convと速度が変わらないならTRT VAEの方がお得。環境によってはTRT VAEがint8 conv使用Fast VAEより少し遅いためTRTを使用(246)。

**ComfyUIのアップスケール関連**
- Comfy-OrgのNvidia_RTX_Nodes_ComfyUIは速度優先だが品質はイマイチ(415)。
- ComfyUIネイティブのSeedVR2は高品質だがかなり重い(415)。
- 0.4mp -> 1.0mp(2step)でかなりの時間節約になる手法がある(425)。

**ComfyUIのワークフロー・テンプレート**
- H3のcomfyui公式テンプレートにマルチフレーム参照テンプレートが新たに追加され、T2V, I2V, Ref2Vと計4つになった(354)。

### その他のツール・サービス関連

**irodoriTTS / irodori anime**
- irodoriTTSの出力ファイル名にseed値、リファレンスファイル名、セリフを追加するようGrokに依頼して実装してもらった(232)。
- irodoriでaudioを渡して秒数を測り、口パクを合わせるノードを作成してもらった(294)。
- TTS-v4.1-Animeは絵文字での反応が良くなっており、ささやきなどがより分かりやすく出る傾向(328)。

**ChatGPT / Codex**
- ChatGPTのUIが雑で、F5で更新しないとファイルダウンロードできない不具合が放置されている。Codexでまとめてログを消す方法があると言いながら実際にはできない(303)。
- CodexにKrea2のLoraをマージさせて疑似ターボ化しINT8に自動でするUIを作成した。ステップ8のCFG1で問題なく生成できている(399)。
- Codexを使用する気起きず使用量は常に100%。パソコンの中を触らせるのが怖いという声(245)。

**Topaz Video / Topaz AI**
- 最強動画アプスケはたぶんTopaz Videoだが、月額60ドルのサブスクのため手が出せないという声(422)。
- 古いTopazの恒久ライセンスを持っているが最新版は違うのか、買い切りがないのは辛いとの声(423)。
- 画質向上アプスケはクラウドサービスのTopaz AI Astra2が良い。ローカルでは何時間もかかるとの情報(431)。

**Blender / MCP**
- BlenderにMCPが実装されたのはGWのとき。fableで操作させる事例がよく見られた。チャッピーとastraの性能を合わせ技でブレイクスルー(287)。

**RX9**
- RX9でノイズを取って音声を使用している(408)。

**civitai / civarchive**
- civitaiの画像ランダム解析失敗で一生他人に表示されないバグは致命的(289)。
- civitaiで検索するよりcivarchiveで検索して移動した方がいい(358)。

**Krea3 / Krea2**
- Krea3は限定イベント後に動きがない。Krea2で数コマ作れば4コマ漫画を動画化できるかもしれない(354)。

**MiniMax H3のツール的使い方**
- MiniMax H3で音声入力して生成するのが楽しい(404)。
- MMH3のi2vで開始と終了画像を同一にしてループ動画作成すると、最後0.5秒くらい静止画になる(388)。
- 箱先生がMinimaxH3用のNegPiPを出している(405)。
- minimaxの純正アップスケーラーがまだ出ていない(414)。