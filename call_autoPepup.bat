%echo off
rem このファイルの配置フォルダをカレントにする
pushd %0\..
rem 画面をクリア
cls
rem 仮想環境をActivateするための特殊なバッチファイルを起動
call C:\Users\zeroc\anaconda3\Scripts\activate.bat
rem 仮想環境をActivate
call activate WsPepup
rem pythonスクリプトを実行
rem (旧コマンド) python C:\Users\zeroc\work\autoPepup\main.py
C:\Users\zeroc\anaconda3\envs\WsPepup\python.exe C:\Users\zeroc\work\autoPepup\AutoPepup_gui.py
