from app.src import common_variables as common


class Message:
    """Message (class)

    parse後のメッセージを格納しておく構造体クラス。

    Attributes
        address (string): ユーザアドレス。
        password (string): パスワード。

        is_step (boolean): 歩数自動入力の実施フラグ。
        is_sleep (boolean): 睡眠時間自動入力の実施フラグ。
        is_check (boolean): チェック自動入力の実施フラグ。

        step_min (int): 歩数の最大値(乱数生成に使用)。
        step_max (int): 歩数の最小値(乱数生成に使用)。
        sleep_min (float): 睡眠時間の最大値(乱数生成に使用)。
        sleep_max (float): 睡眠時間の最小値(乱数生成に使用)。
    """

    def __init__(self):

        self.address = None
        self.password = None

        self.is_step = False
        self.is_sleep = False
        self.is_check = False

        self.step_min = None
        self.step_max = None
        self.sleep_min = None
        self.sleep_max = None


class ParseEventMessage:
    """ParseEventMessage (class)
    入力されたイベントメッセージのParseを担当するクラス。

    Attributes
        parse_message (Message): parse後のメッセージ格納変数。
    """

    def __init__(self):
        self.parse_message = Message()

    def __string2numeric(self, str, type):
        """__string2numeric (method)

        数値文字列の確認および変換後の数値を取得するメソッド。

        Args:
            str (string):
                数値への変換対象の文字列。
            type (class):
                変換する数値の型。
                例えば、int や floatなど。

        Returns:
            type:
                数値変換後の情報。
                変換失敗時は、Noneとなる。
        """
        try:
            num_value = type(float(str))
        except ValueError:
            return None

        return num_value

    def __store_address_param(self, address, message):
        """__store_address_param (method)

        アドレスをパラメータに格納するメソッド。

        Args:
            address (string): アドレス文字列。
            message (string): アドレス含むメッセージ文字列 (今回は未使用)。
        """
        # エラーチェック無し (ログイン時のエラーは別クラスでチェックする)
        self.parse_message.address = address

    def __store_password_param(self, password, message):
        """__store_password_param (method)

        パスワードをパラメータに格納するメソッド。

        Args:
            password (string): パスワード文字列。
            message (string): パスワード含むメッセージ文字列 (今回は未使用)。
        """
        # エラーチェック無し (ログイン時のエラーは別クラスでチェックする)
        self.parse_message.password = password

    def __store_step_value_param(self, value, message):
        """__store_step_value_param (method)

        歩数値をパラメータに格納するメソッド。

        Args:
            value (string): 歩数文字列。
            message (string): 歩数含むメッセージ文字列。
        """
        value_item = value.split('-')

        # スカラ指定のエラーチェック
        if len(value_item) == 1:
            num_value = self.__string2numeric(value_item[0], int)
            if num_value is not None:
                self.parse_message.is_step = True
                self.parse_message.step_max = num_value
                self.parse_message.step_min = num_value
            else:
                common.error_log.add_error_log('')
                common.error_log.add_error_log('■数値エラー｜{}'.format(message))
                common.error_log.add_error_log(
                    '　[{}]が数値になっていません'.format(value))

        # 範囲指定のエラーチェック
        elif len(value_item) == 2:
            num_1_value = self.__string2numeric(value_item[0], int)
            num_2_value = self.__string2numeric(value_item[1], int)

            if (num_1_value is not None) and (num_2_value is not None):
                if num_1_value <= num_2_value:
                    self.parse_message.step_min = num_1_value
                    self.parse_message.step_max = num_2_value
                else:
                    self.parse_message.step_min = num_2_value
                    self.parse_message.step_max = num_1_value

                self.parse_message.is_step = True

            else:
                if num_1_value is None:
                    # 空白文字かどうかでNG内容を変える
                    if not value_item[0]:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■構文エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[-]による範囲指定の記載法に不備があります')
                    else:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■数値エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[{}]が数値になっていません'.format(value_item[0]))

                if num_2_value is None:
                    # 空白文字かどうかでNG内容を変える
                    if not value_item[1]:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■構文エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[-]による範囲指定の記載法に不備があります')
                    else:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■数値エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[{}]が数値になっていません'.format(value_item[1]))

        else:
            common.error_log.add_error_log('')
            common.error_log.add_error_log('■構文エラー｜{}'.format(message))
            common.error_log.add_error_log('　[-]による範囲指定の記載法に不備があります')

    def __store_sleep_value_param(self, value, message):
        """__store_sleep_value_param (method)

        睡眠時間値をパラメータに格納するメソッド。

        Args:
            value (string): 睡眠時間文字列。
            message (string): 睡眠時間含むメッセージ文字列。
        """
        value_item = value.split('-')

        # スカラ指定のエラーチェック
        if len(value_item) == 1:
            num_value = self.__string2numeric(value_item[0], float)
            if num_value is not None:
                self.parse_message.is_sleep = True
                self.parse_message.sleep_max = num_value
                self.parse_message.sleep_min = num_value
            else:
                common.error_log.add_error_log('')
                common.error_log.add_error_log('■数値エラー｜{}'.format(message))
                common.error_log.add_error_log(
                    '　[{}]が数値になっていません'.format(value))

        # 範囲指定のエラーチェック
        elif len(value_item) == 2:
            num_1_value = self.__string2numeric(value_item[0], float)
            num_2_value = self.__string2numeric(value_item[1], float)

            if (num_1_value is not None) and (num_2_value is not None):
                if num_1_value <= num_2_value:
                    self.parse_message.sleep_min = num_1_value
                    self.parse_message.sleep_max = num_2_value
                else:
                    self.parse_message.sleep_min = num_2_value
                    self.parse_message.sleep_max = num_1_value

                self.parse_message.is_sleep = True

            else:
                if num_1_value is None:
                    # 空白文字かどうかでNG内容を変える
                    if not value_item[0]:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■構文エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[-]による範囲指定の記載法に不備があります')
                    else:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■数値エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[{}]が数値になっていません'.format(value_item[0]))

                if num_2_value is None:
                    # 空白文字かどうかでNG内容を変える
                    if not value_item[1]:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■構文エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[-]による範囲指定の記載法に不備があります')
                    else:
                        common.error_log.add_error_log('')
                        common.error_log.add_error_log(
                            '■数値エラー｜{}'.format(message))
                        common.error_log.add_error_log(
                            '　[{}]が数値になっていません'.format(value_item[1]))

        else:
            common.error_log.add_error_log('')
            common.error_log.add_error_log('■構文エラー｜{}'.format(message))
            common.error_log.add_error_log('　[-]による範囲指定の記載法に不備があります')

    def __store_check_param(self, check, message):
        """__store_check_param (method)

        チェック入力の有無をパラメータに格納するメソッド。

        Args:
            check (string):
                チェック入力の有無。
                ["あり"]もしくは["なし"]の文字列。
            message (string):
                チェック入力の有無を含むメッセージ文字列。
        """
        if check == 'あり':
            self.parse_message.is_check = True
        elif check == 'なし':
            self.parse_message.is_check = False
        else:
            common.error_log.add_error_log('')
            common.error_log.add_error_log('■記載ミス｜{}'.format(message))
            common.error_log.add_error_log('　[あり/なし]のどちらにして下さい')

    def parse_event_message(self, message):
        """parse_event_message (method)
        入力メッセージをParseしてパラメータ辞書に変換するメソッド。

        Args:
            message (string): Lineのチャットで入力されたメッセージ。

        Returns:
            Message: parse後のメッセージ情報。
        """
        # パラメータ格納変数を初期化する
        self.parse_message = Message()

        # 各種入力項目確認用データ格納配列
        item_list = [
            {'Label': 'メールアドレス', 'Event': self.__store_address_param},
            {'Label': 'パスワード', 'Event': self.__store_password_param},
            {'Label': '歩数', 'Event': self.__store_step_value_param},
            {'Label': '睡眠時間', 'Event': self.__store_sleep_value_param},
            {'Label': 'チェック', 'Event': self.__store_check_param}
        ]
        # ラベル情報のみ抽出
        item_labels = [item['Label'] for item in item_list]

        # メッセージを1行ごとにParseする
        lines = message.split('\n')
        for line in lines:
            # メッセージ内にキーの文字列があるかを確認
            enable_flgs = [item_label in line for item_label in item_labels]
            match_count = enable_flgs.count(True)

            # 一致するキーが1つある場合
            if match_count == 1:
                # キーとパラメータの区切り文字[:]がない場合はm構文エラーとする
                tokens = line.split(':', 1)
                if len(tokens) <= 1:
                    # 構文エラー
                    common.error_log.add_error_log('')
                    common.error_log.add_error_log('■構文エラー｜{}'.format(line))
                    common.error_log.add_error_log('　[:]の記載法に不備があります')
                else:
                    # パラメータ抽出
                    item_index = enable_flgs.index(True)
                    item = item_list[item_index]
                    item['Event'](tokens[1], line)

            # 一致するキーが2つ以上ある場合は、構文エラーとする
            elif match_count > 1:
                common.error_log.add_error_log('')
                common.error_log.add_error_log('■構文エラー｜{}'.format(line))
                common.error_log.add_error_log('　メッセージの記載法に不備があります')

        # メッセージ内にパラメータ項目が無い場合は、NGとする
        if (not self.parse_message.is_step and
                not self.parse_message.is_sleep and
                not self.parse_message.is_check):
            common.error_log.add_error_log('')
            common.error_log.add_error_log('■構文エラー｜入力チャット全体')
            common.error_log.add_error_log('　自動入力する項目が指定されていません')

        return self.parse_message
