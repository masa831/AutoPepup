from datetime import datetime

from app.src.webdriver_setting import create_webdriver
from app.src.parse_event_message import ParseEventMessage
from app.src.date_generator import DateGenerator
from app.src.random_generator import RandomGenerator
from app.src import webdriver_function as wf
from app.src.parameter import AutoRecordMileageParameter as Param

from app.src import common_variables as common


class AutoRecordMileage:
    """AutoRecordMileage (class)

    わくわくマイレージ自動入力を取りまとめるクラス。

    Attributes
        parse_message (ParseEventMessage): イベントメッセージをParseするクラスインスタンス。
        webdriver (selenium.driver): webドライバ。

    """

    def __init__(self):
        self.parse_message = ParseEventMessage()
        self.webdriver = None

    def login_pepup(self, address, password):
        """login_pepup (method)

        PepUpのログイン処理をを実施する関数。

        Args:
            address (string): ログインアドレス。
            password (string): ログインパスワード。
        """
        # ログインサイトにアクセス
        wf.access_login_url(self.webdriver)

        # 未ログインの場合は、ログインを実施
        if not wf.check_login_success(self.webdriver):

            # ログイン実施 & ログイン成功/失敗判定
            if not wf.run_login(self.webdriver, address, password):
                error_message = ('\n'
                                 '■ログイン情報\n'
                                 '　Pepupへのログインに失敗しました\n'
                                 '　メールアドレス、パスワードに誤りがあるかもしれません\n'
                                 '\n'
                                 '　また、「私はロボットではありません」のチェックボックスは突破できません\n'
                                 '　チェックボックスが出ている際は、一度手動でのチェックをお願いします')
                common.error_log.add_error_log(error_message)

        # ログイン成功時はわくわくマイレージにアクセス
        if wf.check_login_success(self.webdriver):
            wf.access_mileage_url(self.webdriver)

    def record_value(self, date_list, mileage_name, mileage_id, generator):
        """record_value (method)

        わくわくマイレージの値入力項目の自動入力を実施するメソッド。

        Args:
            date_list (list of dict): マイレージ内の日付ボタン押下用の日付情報。
            mileage_name (string): マイレージ名。
            mileage_id (int): マイレージID。
            generator (RandomGenerator): 乱数生成器

        Returns:
            list of string: 出力結果格納リスト]を返却。
        """
        header = '● Item : {}'.format(mileage_name)
        result_logs = [header]

        # 今月、前月の順に処理を実施
        for date_item in date_list:
            # 入力月の移動
            wf.select_month(self.webdriver, date_item['Month'])
            # 入力月に対する結果ログ
            month_logs = []

            # 日付情報に基づいてデータを入力
            for date in date_item['Datelist']:

                date_str = date['Date']
                week_id = date['Week']['Id'] + 1
                day_id = date['Day']['Id'] + 1

                # 指定月に入力項目があるかを確認し、無ければログを格納してループを抜ける
                if not wf.check_mileage(self.webdriver,
                                        mileage_id,
                                        week_id,
                                        day_id):
                    # 入力項目が無いというメッセージをログに格納
                    date_tmp = datetime.strptime(date_str, '%Y/%m/%d')
                    date_msg = date_tmp.strftime('%Y/%m/ALL')
                    month_logs.append('{} : <Empty>'.format(date_msg))
                    break

                # 日付ボタンをクリック
                wf.click_day(self.webdriver, mileage_id, week_id, day_id)

                # すでにPepupに入力が入っている場合:歩数と睡眠時間が一定値を超えているかを確認
                if (wf.get_textbox(self.webdriver) != ''):
                    # 歩数入力が8000以下の場合はテキストボックスの入力値をリセット
                    if( (mileage_name == 'StepInput') and int(wf.get_textbox(self.webdriver)) < 8000 ):
                        wf.reset_textbox(self.webdriver)
                
                    # 睡眠時間が6以下の場合はテキストボックスの入力値をリセット
                    if( (mileage_name == 'SleepInput') and float(wf.get_textbox(self.webdriver)) < 6.0 ):
                        wf.reset_textbox(self.webdriver)
            
                #  現在の入力がない場合、入力値を生成して入力
                if (wf.get_textbox(self.webdriver) == ''):
                    text = str(generator.generate_rand_value())
                    wf.set_textbox(self.webdriver, text)
                    # メッセージを格納
                    month_logs.append('{} - Input [{}]'.format(date_str, text))
                # 現在の入力がある場合は、キャンセルをクリック
                else:
                    wf.click_textbox_cancel(self.webdriver)

            # 月のログが空(既に全日入力済み)の場合、入力済みのメッセージを格納
            if not month_logs:
                date_tmp = datetime.strptime(date_str, '%Y/%m/%d')
                date_meg = date_tmp.strftime('%Y/%m/ALL')
                month_logs.append('{} : <Already Input>'.format(date_meg))

            # 返却用変数に月のログをスタック
            result_logs.extend(month_logs)

        return result_logs

    def record_checkbox(self, date_list, mileage_name, mileage_id):
        """record_checkbox (method)

        わくわくマイレージのチェック項目の自動入力を実施するメソッド。

        Args:
            date_list (list of dict): マイレージ内の日付ボタン押下用の日付情報。
            mileage_name (string): マイレージ名。
            mileage_id (int): マイレージID。

        Returns:
            list of string: 出力結果格納リスト]を返却。
        """
        header = '● Item : {}'.format(mileage_name)
        result_logs = [header]

        # 今月、前月の順に処理を実施
        for date_item in date_list:
            # 入力月の移動
            wf.select_month(self.webdriver, date_item['Month'])
            # 入力月に対する結果ログ
            month_logs = []

            # 日付情報に基づいてデータを入力
            for date in date_item['Datelist']:

                date_str = date['Date']
                week_id = date['Week']['Id'] + 1
                day_id = date['Day']['Id'] + 1

                # 指定月に入力項目があるかを確認し、無ければログを格納してループを抜ける
                if not wf.check_mileage(self.webdriver,
                                        mileage_id,
                                        week_id,
                                        day_id):
                    # 入力項目が無いというメッセージをログに格納
                    date_tmp = datetime.strptime(date_str, '%Y/%m/%d')
                    date_msg = date_tmp.strftime('%Y/%m/ALL')
                    month_logs.append('{} : <Empty>'.format(date_msg))
                    break

                # 日付ボタンをクリック
                wf.click_day(self.webdriver, mileage_id, week_id, day_id)

                # チェックボックスかラジオボックスかを判定
                check_type = wf.get_checkbox_type(self.webdriver)

                # チェックボックスの入力処理を実施
                if check_type == 'CheckBox':
                    # 初回入力時の判別フラグ
                    is_init_check = True
                    for idx in range(wf.get_checkbox_num(self.webdriver)):
                        # チェック済みの場合はスキップ
                        if not wf.check_checkbox(self.webdriver, idx):
                            continue
                        # 初回入力時、メッセージに日付を格納
                        if is_init_check:
                            month_logs.append('{}'.format(date_str))
                            is_init_check = False
                        # メッセージを格納
                        text = wf.get_checkbox_text(self.webdriver, idx)
                        month_logs.append(' - Checked [{}]'.format(text))
                    # ダイアログを閉じる
                    wf.click_checkbox_close(self.webdriver)

                # ラジオボックスの入力処理を実施
                elif check_type == 'RadioBox':
                    # 未チェックの場合は、チェックを実施
                    if wf.check_radiobox(self.webdriver):
                        # メッセージを格納
                        text = wf.get_radiobox_text(self.webdriver)
                        month_logs.append('{} - Checked [{}]'.format(date_str,
                                                                     text))
                        wf.click_radiobox_record(self.webdriver)
                    # 入力済みの場合は、そのまま閉じる
                    else:
                        wf.click_radiobox_close(self.webdriver)

            # 月のログが空(既に全日入力済み)の場合、入力済みのメッセージを格納
            if not month_logs:
                date_tmp = datetime.strptime(date_str, '%Y/%m/%d')
                date_meg = date_tmp.strftime('%Y/%m/ALL')
                month_logs.append('{} : <Already Input>'.format(date_meg))

            # 返却用変数に月のログをスタック
            result_logs.extend(month_logs)

        return result_logs

    def auto_record(self, event_message, app_param):
        """auto_record (method)

        わくわくマイレージ自動入力を実施するメソッド。

        Args:
            event_message (string):
                Lineのチャットで送信されたメッセージ。
            app_param (dict):
                開発環境とブラウザ表示の設定。
                ・'is_prod_env'
                    True : AWS Lambdaで動かすための設定を行う
                    False: ローカル環境で動かすための設定を行う
                ・'is_browser_hidden'
                    True : ブラウザの表示設定を非表示にする
                    False: ブラウザの表示設定を表示にする
                    ('is_prod_env'がTrueの場合は、強制的にFalseになる)

        Returns:
            string: 自動入力実施の結果ログ
        """
        # 入力のParse処理
        message = self.parse_message.parse_event_message(event_message)
        if common.error_log.error_flg:
            return common.error_log.pop_error_message()

        # ドライバと自動入力処理クラスのを用意
        self.webdriver = create_webdriver(param=app_param)

        # ログイン処理
        common.line_msg.push_message('PepupLogin Process Now')
        self.login_pepup(message.address, message.password)
        if common.error_log.error_flg:
            return False, common.error_log.pop_error_message()

        # マイレージ内の日付ボタン押下用のDate情報を用意
        date_generator = DateGenerator()
        date_list = date_generator.generate_date_list()

        # メッセージ格納リスト
        ack_results = []

        # 各種マイレージの入力を実施
        for mileage_type in Param.MILEAGE_TYPE_LIST:

            # 歩数の自動入力
            if (mileage_type['Type'] == 'step') and message.is_step:
                mileage_name = mileage_type['Name']
                mileage_id = mileage_type['Id']
                common.line_msg.push_message(mileage_name + ' Process Now')

                step_generator = RandomGenerator(message.step_min,
                                                 message.step_max,
                                                 1)
                results = self.record_value(date_list,
                                            mileage_name,
                                            mileage_id,
                                            step_generator)
                if len(results) > 0:
                    ack_results.append('')
                ack_results.extend(results)

            # 睡眠時間の自動入力
            elif (mileage_type['Type'] == 'sleep') and message.is_sleep:
                mileage_name = mileage_type['Name']
                mileage_id = mileage_type['Id']
                common.line_msg.push_message(mileage_name + ' Process Now')

                sleep_generator = RandomGenerator(message.sleep_min,
                                                  message.sleep_max,
                                                  0.1)
                results = self.record_value(date_list,
                                            mileage_name,
                                            mileage_id,
                                            sleep_generator)
                if len(results) > 0:
                    ack_results.append('')
                ack_results.extend(results)

            # 各種チェックボックスの自動入力
            elif (mileage_type['Type'] == 'check') and message.is_check:
                mileage_name = mileage_type['Name']
                mileage_id = mileage_type['Id']
                common.line_msg.push_message(mileage_name + ' Process Now')

                results = self.record_checkbox(date_list,
                                               mileage_name,
                                               mileage_id)
                if len(results) > 0:
                    ack_results.append('')
                ack_results.extend(results)

        # ブラウザを閉じる
        self.webdriver.quit()

        # 取得した結果ログを文字列に変換して返却
        ack_message = '\n'.join(ack_results)
        return ack_message
