@echo off
setlocal enabledelayedexpansion

REM README.mdをクリアする
echo. > README.md

REM ファイルリストを取得してURLに変換して書き込む
echo # File List >> README.md
echo. >> README.md

for /d %%D in (*) do (
    if "%%D" neq ".git" (
        for %%F in (%%D\*) do (
            set "filename=%%F"
            set "url=https://ponapon280.github.io/5chSummary/!filename:.md=.html!"
            echo - !url! >> README.md
        )
    )
)

echo ファイルリストをURLに変換してREADME.mdに書き出しました。
pause