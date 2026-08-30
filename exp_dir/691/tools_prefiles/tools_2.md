## 生成AI関連「ツール」話題 抽出レポート

### ComfyUI

- **最新版アップデートの互換性**: ComfyUI最新にしたら使えないノードが出るかどうかの質問（レス234）
- **メモリ削減オプション**: 起動オプションに「--disable-pinned-memory」を入れるだけで使用メモリが減り、生成時間も変わらないという報告（レス259）。ただし検証により生成時間は1,2割増えるとの指摘あり（レス297、302）。さらに「--fastdisk」を併用している場合はメモリを使わずSSDからVRAMへロードするため、「--disable-pinned-memory」の有無で生成時間が変わらない可能性との分析（レス304）。生成でメモリ限界近くまで消費する場合はpinned memoryを切った方が良いが、SSDの寿命には変えられないという見解（レス305）
- **LoraLoader関連の修正**: カスタムノードの制約があり使いづらかったオリジナル版に対し、現状のComfyUIのUNet/DiT構造に合わせたもの（末尾_comfy版）は標準構造に合わせているため使える可能性があるとの報告（レス258）。実際に動かしたがダメだったとの報告（レス269）。その後、標準LoraLoaderでAcc-Loraを動かすための修正として「git fetch origin pull/15908/head:pdd-fix && git checkout pdd-fix」を実行したら動いたとの報告（レス278）

### H3 optimizations（高速化ツール）

- **SageAttention環境での効果**: SageAttention環境でLimiterとMemory OptimizationとSparse Attentionをデフォルト設定でつなげたら、主張通りSageAttentionオンリーから生成時間が半分になり、VRAMが5GB空いたとの報告。Sparse Attentionは劣化を伴うが、VRAMカツカツ勢ならLimiterとMemory Optimizationは入れておいた方が良いとの推奨（レス243）
- **速度比較**: H3 optimizationsをデフォルト値で試したところ、速度はSol attn + SLAと同じくらいとの報告（レス250）

### フリートークン（LLM推論ソフト）

- **動作報告**: フリートークンをインストールしたが、3060では31Bの一番小さいモデルすら動作しなかった。llamaで設定を弄り回して4.5t/sまで到達したが、3060ではここら辺が限界かとの報告（レス293）
- **使い方の指摘**: フリートークンはMoEだけが早くなるツールであり、26B-A4Bのようなモデルを選ぶべき。Denseモデルを使うなら別のエンジンを使った方が良く、beellamaでkvキャッシュ量子化をkvarn4にするとかなり良いとのアドバイス（レス312）

### beellama（LLM推論エンジン）

- フリートークンの代替として言及。Denseモデルを使う場合に推奨され、kvキャッシュ量子化をkvarn4にするとかなり良いとの報告（レス312）

### venice / fal（生成プラットフォーム）

- venice、falにMiniMax H3 Maxが来ているが、高速生成以外にメリットがないかとの感想（レス245）

### 選ばれている理由のまとめ

- **ComfyUI（--disable-pinned-memory）**: 使用メモリが減り、グラボが燃えない対策になるため（レス259）。ただし生成時間は1,2割増える代价がある（レス297）
- **H3 optimizations（Limiter + Memory Optimization）**: 生成時間を半分にし、VRAMを5GB空けられるため。VRAMカツカツ環境で有効（レス243）
- **beellama**: Denseモデル使用時にフリートークンより適しており、kvキャッシュ量子化で良好な結果が得られるため（レス312）