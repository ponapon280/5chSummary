# なんJ AI画像生成スレッド（なんJNVA部） Z-Image Turbo (ZIT) 関連議論 統合レポート

## 1. スレッド全体概要
- **対象ログ範囲**: 235〜1000レス（約700レス、複数日分）。なんJのAI画像生成コミュニティ（主にStable Diffusion系ユーザー）が、Alibabaの新モデル**Z-Image Turbo (ZIT, 6Bパラメータ)**の登場を熱く議論。
- **主なトピック**: ZITの高速生成・低VRAM優位性、LoRA学習検証、プロンプト構造化技法、NSFW/エロ適性、ハードウェア制約、ComfyUI/Forge Neoツール活用、動画生成。中国AI（Qwen/Ovis）の競争力とSDXL/Flux/Ponyからの移行論が中心。
- **コミュニティ傾向**: ローカル環境ユーザー（RTX 3060/4070ti/5090想定）が試行錯誤中心。興奮ムード（「軽いは正義」「次期覇権」）だが、Baseモデル/エロFT公開待ちで現実的。zuntan氏復帰が盛り上がり要因。エロNSFW生成報告多め、Tips共有活発だが「秘伝」気味。
- **全体ムード**: ポジティブ（爆速普及象徴）vs. 課題（エロ弱、低スペック時間長、VRAM格差）。CivitaiでZIT LoRA急増中。

## 2. ZITの評価と強み・課題
- **強み**:
  - 速度/軽量: フルHD/4-9step高速（SDXL比2.4倍）、VRAM6-12GBで推論可。テキストエンコーダー賢く、構造化プロンプト（Markdown/リスト/- --記法）で位置/複数キャラ（5人並べOK）抜群。
  - 例: `- in the kitchen - a girl -- very short brown hair... -- on the left` → 指示通り再現率10/10。
  - 指/髪/背景再現性高、日本語/自然言語対応◎。
- **課題**:
  - Turbo版LoRA適用でグチャグチャ（蒸留モデル不向き）、Base/Edit公開待ち推奨。
  - エロ/NSFW弱（乳首/性器/パンツ描写劣化、白塗り肌）。イラスト/二次FT待ち。


  | 比較 | 速度 | 画質 | LoRA適性 | NSFW |
  |------|------|------|----------|------|
  | ZIT Turbo | ◎ (4-9step) | ○ (顔/エロ弱) | △ (Base待ち) | △ (Detailer要) |
  | SDXL | ○ | ○ | ◎ | ○ |
  | Flux.1/2 | △ | ◎ | - | △ |
  | Pony/リアス/Illustrious | - | ◎ (エロ) | ◎ | ◎ |

- **Sampler Tips**: res_multistep/simple（リアル寄り）、dpmpp_sde+ddim_uniform+Steps12-15+CFG5-7（白塗り回避）。DFloat11圧縮でVRAM3GB減。

## 3. LoRA学習検証結果
コミュニティが数日で高速検証。ai-toolkit/musubi-tuner（kohya後継）活用。タグ+自然言語キャプション推奨（詳細不要、VLM的賢さ）。


| 環境/VRAM | データセット | ステップ/時間 | 結果 |
|-----------|--------------|---------------|------|
| 4070ti SUPER (16GB) | 8枚, Danbooruタグ | デフォルト | 30分弱, 標準速度 |
| 5090/5070ti (16GB) | 60枚/5枚, タグ+NL | 2400/1000step | 1時間, 特徴再現↑ |
| 3060 (12GB) | 未詳 | 3000step | 6時間 (SDXL比遅いが可) |
| 8GB (4bit量子化) | XL素材 | 500step | 1時間, 低スペック可 |

- **VRAM要件**: 学習13-16GB（12GBオフロード/量子化可、8GB確認）。Batch↑で高速化。
- **ツール比較**:


  | ツール | 利点 | 欠点 |
  |--------|------|------|
  | ai-toolkit | 高速/楽, NL OK | 容量食う (30GB DL) |
  | musubi-tuner | BlockSwap, Base対応予定 | - |


- **注意**: Turboで画風LoRAはピンボケ/過学習早い。Base公開で作り直し。AdamW/ScheduleFree+cosine/LRで1h→30min。

**キャプションTips**: Qwen3-VL-8B-NSFW-Caption-V4.5（4bit/sdpa指定、markdown露骨NSFW用）。嘘対策: 具体指示。自然言語優位。

## 4. 生成/NSFW/動画技法ハイライト
- **プロンプト**: Markdown/JSON有効。複数キャラLoRA同時可（重複NG）。`(huge breasts:1.5)`無効→自然記述（「gigantic」など）。
- **NSFWテク**:
  - おまんこ/膜: pussy_yolo11s+threshold0.2/Detailer, miaomiao realskin v11+LoRA。
  - 顔フラット/体リアル分離、3P表情制御。ちんこ/ふたなりLoRA先行。シリコンボディ/プニプニ肌追求。
  - 中文優位、版権（WAI-Illustrious/NoobAI系）混ぜで改善。
- **動画生成**: PainterLongVideo（Native専用、FrameOverlap/逆再生）、WAN2.2+MMAudio/SmoothMix/EasyWan（step4-6調整、Q4限界）、StadyDancer（長尺OK）。リップシンク: Ovi/s2v+CFGブースト。

## 5. ハードウェア/インストール議論
- **要件**:


  | 用途 | 推奨VRAM |
  |------|----------|
  | 推論 | 6-12GB |
  | LoRA作成 | 15-24GB |
  | 高品質/FT | 24GB+ |


- **GPU/メモリ**: 3060/1660Ti可（最低環境）。5090待ち、DDR5暴騰（AI需要/中国制裁）。中古博打注意。
- **最適化**: fp8_e4m3fn/DFloat11（43GB→20GB減）、Flash Attention2（whl簡単）。ComfyUI WF共有/D2-nodes削除で安定。Forge Neo/Zuntan EasyImageEdit便利。

## 6. 他モデル/コミュニティ動向
- **オススメ代替**: Illustrious v15（構図安定、wai派生）、Hassaku/NoobAI Obsession、Pony奇数版、リアス（エロ継続派）。
- **中国AI優位**: Alibaba/Zuntan復帰祭り。大学連携/公開積極性絶賛も、エロ規制/セキュリティ懸念。
- **ツール進化**: ComfyUI必須（WF/D&D再現）、StabilityMatrix注意（環境壊れ）。
- **トレンド**: ZIT実写即移行、二次エロ保留。エロLoRA/Civitai急増、低スペック層獲得。「ゲームエンド」毎週論。

## 7. 将来展望と示唆
- **期待**: Base/Edit/エロFT（3月？Pony/リアス並み）、QIE2511/Flux2エロチューン、kohya実装。
- **課題**: LoRA秘伝非公開、VRAM格差、規制回避。
- **推奨アクション**:
  1. ai-toolkitでTurbo LoRA作成→Base待ち。
  2. 構造化プロンプト/Qwen-VL即活用。
  3. 低VRAM: 量子化/DFloat11検証、ComfyUI入門。
  4. GPU/メモリ今買え（高騰加速）。
- **総評**: ZITは速度/汎用で革命的、低参入障壁でボリューム層沸かすが、エロ最適化待ちの過渡期。中国勢台頭で勢力図変動、次スレ（★600）でBase/NSFW爆発予想。詳細ログ（>>63,74,231,774等）参考に。

この統合レポートは重複削除・エッセンス抽出。コミュニティの試行錯誤を凝縮。追加深掘り歓迎。