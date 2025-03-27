import os
from collections import defaultdict

def convert_files_to_urls(base_url='https://ponapon280.github.io/5chSummary/'):
    # ファイルをフォルダごとに整理
    folder_files = defaultdict(list)

    # カレントディレクトリのサブディレクトリを走査
    for folder in os.listdir('.'):
        # ディレクトリのみを処理
        if os.path.isdir(folder) and folder != '.git':
            # フォルダ内のファイルを走査
            for filename in os.listdir(folder):
                # .mdファイルのみ処理
                if filename.endswith('.md'):
                    # URLに変換
                    url = f"{base_url}{folder}/{filename.replace('.md', '.html')}"
                    # ファイル名（拡張子なし）をリンクテキストとして使用
                    link_text = os.path.splitext(filename)[0]
                    folder_files[folder].append((link_text, url))

    # README.mdを書き込みモードで開く
    with open('README.md', 'w', encoding='utf-8') as readme:
        # ヘッダーを書き込む
        readme.write('# File List\n\n')

        # フォルダごとに折りたたみ可能な形式で出力
        for folder, files in sorted(folder_files.items()):
            readme.write(f'<details>\n')
            readme.write(f'<summary>{folder}</summary>\n\n')
            
            for link_text, url in sorted(files):
                readme.write(f'- [{link_text}]({url})\n')
            
            readme.write('</details>\n\n')

    print('ファイルリストをマークダウンリンクに変換してREADME.mdに書き出しました。')

# スクリプトを実行
if __name__ == '__main__':
    convert_files_to_urls()