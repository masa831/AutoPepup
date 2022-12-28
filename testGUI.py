import sys
import os
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
from main_GUI import MainTask


# アプリケーション（GUI）クラス
class Application(tk.Frame):
    DEBUG_LOG = True
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""

    def create_widgets(self):
        # ペインウィンドウ
        # PanedWindow
        ##  orient : 配置（vertical or horizontal）
        ##  bg : 枠線の色
        # pack
        ##  expand ：可変（True or False(固定)
        ##  fill : スペースが空いている場合の動き（tk.BOTH　縦横に広がる）
        ##  side ：　配置する際にどの方向からつめていくか（side or top ・・・）
        pw_main = tk.PanedWindow(self.master, orient='horizontal')
        pw_main.pack(expand=True, fill = tk.BOTH, side="left")
        pw_left = tk.PanedWindow(pw_main, bg="cyan", orient='vertical')
        pw_main.add(pw_left)
        pw_right = tk.PanedWindow(pw_main, bg="gray", orient='vertical')
        pw_main.add(pw_right)

        # フレーム
        ##  bd ：ボーダーの幅
        ##  relief ：フレームの枠の形
        fm_select = tk.Frame(pw_left, bd=2, relief="ridge")
        pw_left.add(fm_select)
        fm_select_R = tk.Frame(pw_right, bd=2, relief="ridge")
        pw_right.add(fm_select_R)


        label_fpath = tk.Label(fm_select_R, text="実行結果表示", width=20)
        label_fpath.grid(row=0, column=0, padx=2, pady=2)

        # text
        ## witdh ：入力する文字数
        ## wrap：長い行の折り返し方法（tk.CHAR: 文字単位で折り返す or tk.NONE: 折り返ししない or ・・・）
        text_log = tk.Text(fm_select_R, height=20, width=60, wrap=tk.CHAR)
        text_log.grid(row=1, column=0, padx=2, pady=2)

        # ラベル
        ## padx , pady ：外側の横、縦の隙間
        label_fpath = tk.Label(fm_select, text="Pepup自動入力[Menu]", width=20)
        ## ラベルを配置
        label_fpath.grid(row=0, column=0, padx=2, pady=2)

        # ボタン
        ## columnspan ：　何列に渡って配置するか
        ## rowspan ：　何行に渡って配置するか
        # ボタンイベントに引数を渡す
        btn_start = tk.Button(fm_select, text="処理開始", command=lambda:self.btn_start(text_log), width=20)
        btn_start.grid(row=1, column=0, sticky=tk.W + tk.E, padx=2, pady=10)

        btn_exit = tk.Button(fm_select, text="終了", command=lambda:self.btn_exit(), width=20)
        btn_exit.grid(row=2, column=0, sticky=tk.W + tk.E, padx=2, pady=10)

        # ボタン追加時のコード　rowの位置に注意すること
        # btn_tool_1 = tk.Button(fm_select, text="処理開始", command=lambda:self.btn_ivent("test1"), width=20) 
        # btn_tool_1.grid(row=3, column=0, sticky=tk.W + tk.E, padx=2, pady=10)

    def btn_start(self,text_log):
        MainTask()
        file_object = open('log/AppLog.txt','r', encoding='utf-8')
        file_result = file_object.read()
        text_log.insert(tk.END,file_result)

    def btn_exit(self):
        self.master.destroy()

# 実行
root = tk.Tk()
myapp = Application(master=root) # インスタンス作成
myapp.master.title("My Application") # タイトル
myapp.master.geometry("600x350") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()