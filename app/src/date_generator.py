import datetime
from app.src.parameter import DateGeneratorParameter as Param


class DateGenerator:
    """date_generator (class)

    マイレージ内の日付ボタン押下用の情報を取得するクラス。

    """

    def __init__(self):
        pass

    def generate_month_date_list(self, date):
        """generate_month_date_list (method)

        月のDate情報を生成するメソッド。
        指定日時の月の日付リストを作成する。
        指定日時より未来の日にちは、day_existをFalseとして辞書に格納する。

        Args:
            date (datetime): 指定日時。

        Returns:
            dict:
                月の情報(Month)と、各日日付の情報(Datalist)を格納した辞書。
        """
        # 時刻を取得
        curr_date = datetime.datetime(date.year, date.month, 1)
        
        # 日時リストを取得
        date_dict = {
            'Month': date.strftime('%Y/%m'),
            'Datelist': []
        }

        week_id = 0

        # 今現在の月を超えた、もしくは未来の日付になったらループを抜ける
        while (date.month == curr_date.month and
               date.day >= curr_date.day):

            # 日時、日にちID(カレンダー位置)、曜日、経過した日時かどうか、を取得
            date_str = curr_date.strftime('%Y/%m/%d')
            day_id = curr_date.weekday()
            weekday = Param.WEEKDAY_LABEL_LIST[day_id]

            # 辞書にデータを格納
            info = {
                'Date': date_str,
                'Week': {'Id': week_id},
                'Day': {'Id': (day_id + 1) % 7, 'DayOfWeek': weekday}
            }
            date_dict['Datelist'].append(info)

            # 週のID（第何週か）を計算
            curr_date = curr_date + datetime.timedelta(days=1)
            if ((curr_date.weekday() + 1) % 7) == 0:
                week_id += 1

        return date_dict

    def generate_week_date_list(self, date):
        """generate_week_date_list (method)

        週のDate情報を生成するメソッド。
        指定日時の週の日付リストを作成する。
        指定日時より未来の日にちは、day_existをFalseとして辞書に格納する。

        Args:
            date (datetime): 指定日時。

        Returns:
            dict:
                月の情報(Month)と、各日日付の情報(Datalist)を格納した辞書。
        """
        # 時刻を取得
        #curr_date = datetime.datetime(date.year, date.month, 1)
        curr_date = datetime.datetime.now() - datetime.timedelta(days = 10)
        # 日時リストを取得
        date_dict = {
            'Month': date.strftime('%Y/%m'),
            'Datelist': []
        }

        week_id = 0

        # 今現在の月を超えた、もしくは未来の日付になったらループを抜ける
        while (date.month == curr_date.month and
               date.day >= curr_date.day):

            # 日時、日にちID(カレンダー位置)、曜日、経過した日時かどうか、を取得
            date_str = curr_date.strftime('%Y/%m/%d')
            day_id = curr_date.weekday()
            weekday = Param.WEEKDAY_LABEL_LIST[day_id]

            # 辞書にデータを格納
            info = {
                'Date': date_str,
                'Week': {'Id': week_id},
                'Day': {'Id': (day_id + 1) % 7, 'DayOfWeek': weekday}
            }
            date_dict['Datelist'].append(info)

            # 週のID（第何週か）を計算
            curr_date = curr_date + datetime.timedelta(days=1)
            if ((curr_date.weekday() + 1) % 7) == 0:
                week_id += 1

        return date_dict

    def generate_date_list(self):
        """generate_date_list (method)

        マイレージ内の日付ボタン押下用のDate情報を用意するメソッド。

        Returns:
            list of dict:
                先月と今月の日付情報をまとめた配列。
                配列の要素は、月の情報(Month)と各日付の情報(Datalist)を格納した辞書が格納される。
                各日付の情報(Datalist)は、['Date', 'Week', 'Day']をキーと持つ辞書のリスト。
        """
        # 現在の時刻を取得
        now_date = datetime.datetime.now()
        # 昨日の日時を取得　→　こっちを基準にする
        dt_yesterday = now_date - datetime.timedelta(days = 1)
        # 本月の日程を取得
        date_list = []
        curr_date_dict = self.generate_month_date_list(dt_yesterday)
        #curr_date_dict = self.generate_month_date_list(now_date)
        #curr_date_dict = self.generate_week_date_list(now_date)
        date_list.append(curr_date_dict)
        # 入力締め切り前なら、前月の日程を取得
        if now_date.day < Param.INCLUDE_LAST_MONTH_THRESH_DAY:
            prev_date = datetime.datetime(now_date.year, now_date.month, 1)
            prev_date = prev_date - datetime.timedelta(days=1)
            prev_date_dict = self.generate_month_date_list(prev_date)
            #prev_date_dict = self.generate_week_date_list(prev_date)
            date_list.append(prev_date_dict)

        return date_list
