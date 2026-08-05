**抽出結果（ツール関連のみ）**

### ComfyUI関連の話題・Tips
- **ComfyUIの環境構築・運用**
  - ポータブル版と通常版の違い（ポータブル版はSage Attention導入でエラーが出やすいため、セットアップし直すケースあり）
  - シンボリックリンク使用時のトラブル（親フォルダ名変更後にLoRA-Managerが古いパスをキャッシュしていてエラーログが出る）
  - LoRA-Managerのキャッシュ削除方法（`C:\Users\AppData\Local\loramanager`フォルダ削除で解決）

- **Sage Attentionの導入**
  - `python -m pip install triton-windows` + `sageattention-2.2.0.whl`のインストール
  - startup argsに `--enable-triton-backend --use-sage-attention` を追加
  - 導入理由：生成速度向上（3060環境で30s/it → 23s/itに短縮）

- **irodori-TTS関連**
  - ComfyUI-irodori-ttsがv4非対応でGPU起動しない問題
  - 解決方法：`pip uninstall torch torchvision torchaudio` → 特定index-urlで再インストール
  - 理由：v4対応のため

- **ノード・ワークフロー関連**
  - latentアプスケノードの使用感（ltx向けではないため微妙）
  - ref2v / fl2va / i2vのワークフロー切り替え（first_frameノードのバイパスでt2v/i2vを切り替える手法）
  - LoRA-Managerがcheckpointのハッシュ計算でエラーを出すケース

- **メモリ・パフォーマンス関連**
  - DynamicVramの挙動（共有GPUに溢れる仕様として認識）
  - メモリ増設の必要性（4070tiS + 96GB構成でも不足を感じる声）

### 選ばれている理由が明記されているもの
- **Sage Attention**：速度向上のため（特に3060環境で体感できる差が出た）
- **ComfyUI（通常版）**：カスタムノードやSage Attentionの安定性が高いため（ポータブル版より推奨される流れ）
- **ref2vワークフロー**：LoRAなしでもある程度のクオリティが出せるため（「LoRAいらんなこれ」という声）

モデル名（FLUX, Wan, anima, minimax, LTXなど）や性能比較自体は除外しています。