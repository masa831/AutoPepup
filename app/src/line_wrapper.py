from linebot.models import TextSendMessage
from logging import getLogger


logger = getLogger('Log').getChild('line_push_message')


class LineWrapper:
    """LineWrapper (class)

    LineのPushメッセージを出力する処理用のクラス。
    [line_bot_api]もしくは[send_line_id]の値によって、Lineプッシュ通知かlog出力を切り替えることができる。

    Attributes
        line_bot_api (LineBotApi): LineBotApiのオブジェクト。
        send_line_id (string): LineのユーザID。
    """

    def __init__(self, line_bot_api=None, send_line_id=None):
        self.line_bot_api = line_bot_api
        self.send_line_id = send_line_id
        """__init__ (method)

        LineWrapperクラスの初期化メソッド。
        [line_bot_api]もしくは[send_line_id]が未設定の場合は、log出力となる。
        [line_bot_api]もしくは[send_line_id]の値によってが未設定の場合は、log出力に切り替える。

        Args:
            line_bot_api (LineBotApi):
                LineBotApiのオブジェクト。
                Noneの場合、log出力に切り替える。
                Defaults to None.
            send_line_id (string):
                LineのユーザID。
                Noneの場合、log出力に切り替える。
                Defaults to None.
        """

    def push_message(self, message):
        """push_message (method)

        Lineのプッシュメッセージを通知する。
        [line_bot_api]もしくは[send_line_id]が未設定の場合は、log出力に切り替える。

        Args:
            message (string): 送信メッセージ
        """
        if (self.line_bot_api is not None) and (self.send_line_id is not None):
            self.line_bot_api.push_message(
                self.send_line_id,
                TextSendMessage(text=message))
        else:
            logger.info(message)
