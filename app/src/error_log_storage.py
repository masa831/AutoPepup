import traceback


class ErrorLogStorage:
    """ ErrorLogStorage (class)

    エラーログ保管用クラス。

    Attributes
        error_flg (boolean):
            エラーログの有無フラグ。
            Trueの場合は、何かしらのエラーログがスタックされている。
            Falseの場合は、エラーログは保管されていない。
        __error_log_list (list of string):
            エラーログ格納配列。
    """

    def __init__(self):
        self.error_flg = False
        self.__error_log_list = []

    def add_error_log(self, log_msg):
        """add_error_log (method)

        エラーログを格納するメソッド。

        Args:
            log_msg (srting): 格納するエラーログ。
        """
        if not self.error_flg:
            # 初回時のみ、エラーログのタイトルを格納する
            self.__error_log_list.append('下記入力で不備があります')

        # 改行文字で分割
        split_log_msg = log_msg.split('\n')
        # ログを格納
        self.__error_log_list.extend(split_log_msg)
        self.error_flg = True

    def add_stacktrace(self):
        """add_stacktrace (method)

        Tracebackのエラー内容を格納するメソッド。

        """
        self.__error_log_list.append(traceback.format_exc())
        self.error_flg = True

    def pop_error_message(self):
        """pop_error_message (method)

        エラーログ格納リストからエラーメッセージを作成するメソッド。
        エラーメッセージ作成後は、現在保管しているエラーログを消去する。

        Returns:
            string: 作成したエラーメッセージ。
        """
        # エラーメッセージ作成
        error_msg = '\n'.join(self.__error_log_list)
        # エラーログをpopし、フラグを折る
        self.error_flg = False
        self.__error_log_list = []

        return error_msg
