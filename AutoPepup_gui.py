#-*- coding:utf-8 -*-
import sys, threading, re
from copy import deepcopy
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import main_GUI


class Form(QDialog):
    """ GUIクラス
    """

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Widgetsの設定(タイトル、固定横幅、固定縦幅)
        self.setWindowTitle("Pepup Auto")
        self.setFixedWidth(400)
        self.setFixedHeight(300)

        # 導入部
        init_layout = QHBoxLayout()
        self.init_edit = QLineEdit("") # テキスト入力
        init_layout.addWidget(QLabel("[Description] Automation for Pepup's input item"), 1)

        # タイトル
        title_layout = QHBoxLayout()
        self.title_edit = QLineEdit("") # テキスト入力
        title_layout.addWidget(QLabel("[Result Message]"), 1)

        # ログ表示部分
        self.text_layout = QVBoxLayout()
        self.textbox = QListView()
        self.text_list = QStringListModel()
        self.text_layout.addWidget(QLabel("[Result Message]"), 1)
        self.textbox.setModel(self.text_list)
        self.text_layout.addWidget(self.textbox)

        # プログレスバー部分
        pb_layput = QHBoxLayout()
        self.pb = QProgressBar()
        self.pb.setFixedWidth(370)
        self.pb.setTextVisible(False)
        pb_layput.addWidget(self.pb)

        # ボタン部分(start)
        run_layout = QHBoxLayout()
        self.run_button = QPushButton("start")
        self.run_button.clicked.connect(self.run_log)
        run_layout.addWidget(QLabel(""), 2)
        run_layout.addWidget(self.run_button, 1)
        run_layout.addWidget(QLabel(""), 2)

        # ボタン部分(exit)
        exit_layout = QHBoxLayout()
        self.exit_button = QPushButton("exit")
        self.exit_button.clicked.connect(self.close)
        exit_layout.addWidget(QLabel(""), 2)
        exit_layout.addWidget(self.exit_button, 1)
        exit_layout.addWidget(QLabel(""), 2)

        # ボタンを横並べにする
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(QLabel(""), 1)
        menu_layout.addWidget(self.run_button, 1)
        menu_layout.addWidget(QLabel(""), 1)
        menu_layout.addWidget(self.exit_button, 1)
        menu_layout.addWidget(QLabel(""), 1)

        # レイアウトを作成して各要素を配置
        layout = QVBoxLayout()
        layout.addLayout(init_layout)
        layout.addLayout(self.text_layout)
        layout.addLayout(pb_layput)
        layout.addLayout(menu_layout)

        # レイアウトを画面に設定
        self.setLayout(layout)

        # ログスレッドクラスの準備
        self.lp = LogThread()
        self.lp.log_thread.connect(self.show_log)  # シグナルスロットの接続
        self.lp.finished.connect(self.show_result) # スレッドが終了した際の処理の接続


    def run_log(self):
        # ログプロセスを実行する
        # GUIを非活性にする
        self.set_all_enabled(False)
        # プログレスバーの開始
        self.pb.setMinimum(0)
        self.pb.setMaximum(0)
        # ログプロセスを実行する
        self.lp.start()


    def show_log(self, log):
        # 書き込み中の進捗をGUIに表示する
        log_list = self.text_list.stringList()
        log_list.append(str(log))
        self.text_list.setStringList(log_list)
        self.textbox.scrollToBottom()


    def show_result(self):
        # 結果を表示する
        QMessageBox.information(self, "終了", "終了しました。")
        # プログレスバーの停止
        self.pb.setMinimum(0)
        self.pb.setMaximum(100)
        self.set_all_enabled(True) # GUIの表示を戻す


    def set_all_enabled(self, flg):
        # GUIの有効/無効を設定する
        self.run_button.setEnabled(flg)

class LogThread(QThread):
    """ ログファイルを読み取るクラス
    """
    log_thread = Signal(str)
    log_file_path = "./log/pepuplog.txt"
    read_flg = False


    def __init__(self, parent=None):
        """ コンストラクタ
        """
        QThread.__init__(self, parent)


    def __del__(self):
        # Threadオブジェクトが削除されたときにThreadを停止
        self.wait()

    def run(self):
        # 標準出力の出力先をファイルにする
        sys.stdout = open(self.log_file_path, "w")

        # ログファイルを読み取るスレッドを開始
        self.read_flg = True
        read_thread = threading.Thread(target=self.read_log)
        read_thread.setDaemon(True)
        read_thread.start()

        try:
            # 別ファイルのprintする処理を開始
            main_GUI.MainTask()

        except Exception as e:
            print(e)
        finally:
            # 標準出力を元に戻す
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.read_flg = False


    def read_log(self):
        # 書き込み時のログファイルを読込み差分の行をSignalのemitに設定する関数
        old_lines = list()
        new_lines = list()

        while self.read_flg:
            with open(self.log_file_path, "r", encoding="utf-8") as f:
                sys.stdout.flush() # このflushの記述がないと処理途中でログ出力されない

                # listなので書き換えられないようdeepcopy
                new_lines = deepcopy(f.readlines())
                old_size = len(old_lines)
                new_size = len(new_lines)

                if  old_size < new_size:
                    # 差分の行をSignalで値を渡す
                    for i in range(old_size, new_size):
                        self.log_thread.emit(new_lines[i].replace("\n",""))
                    old_lines = deepcopy(new_lines)


if __name__ == '__main__':
    # Qtアプリケーションの作成
    app = QApplication(sys.argv)

    # フォームを作成して表示
    form = Form()
    form.show()

    # 画面表示のためのループ
    sys.exit(app.exec())
