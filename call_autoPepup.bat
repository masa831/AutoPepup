%echo off
rem このファイルの配置フォルダをカレントにする
pushd %0\..
rem 画面をクリア
cls
rem pythonスクリプトを実行
python C:\Users\zeroc\work\autoPepup\main.py
rem 実行はウインドウは開いたままにする
pause