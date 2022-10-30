
# import datetime
import subprocess
# from selenium import webdriver
# from app import version
from app.src.auto_record_mileage import AutoRecordMileage
from app.src.date_generator import DateGenerator
# from app.src.error_log_storage import ErrorLogStorage
from app.src.parameter import AutoRecordMileageParameter
from app.src.random_generator import RandomGenerator
from app.src.webdriver_setting import create_webdriver
from app.src.private_parameter import PrivateParameter



#日時を取得
date = DateGenerator()
date_list = date.generate_date_list()
datelist = date.generate_date_list_20d()

# 実行開始
# インスタンス作成
mileage = AutoRecordMileage()
typelist = AutoRecordMileageParameter()
privateInfo = PrivateParameter()

# ウェブドライバー設定
# ブラウザ非表示
mileage.webdriver = create_webdriver(param={'is_browser_hidden': True})
# ブラウザ表示 debug用
# mileage.webdriver = create_webdriver(param={'is_browser_hidden': False})


print('処理を開始します')
# ログイン処理
mileage.login_pepup(privateInfo.MY_MAIL_ADDRESS,privateInfo.LOGIN_PASS)

# test code
# tmp = mileage.webdriver.find_element_by_xpath(Param.HOME_CONTENT_XPATH)
# print(tmp)

# 歩数、睡眠時間入力用乱数設定
val_step_random = RandomGenerator(10000,11000,1)
val_sleep_random = RandomGenerator(7.0,7.2,0.1) #固定値入力に対応していない可能性あり

# 歩数、睡眠時間入力値設定(固定値)
# val_step_random = 11000
# val_sleep_random = 7.5

# 自動入力
try:
    print('歩数を入力中....')
    mileage.record_value(date_list,typelist.MILEAGE_TYPE_LIST[0]['Name'],typelist.MILEAGE_TYPE_LIST[0]['Id'],val_step_random)
    print('睡眠時間を入力中....')
    mileage.record_value(date_list,typelist.MILEAGE_TYPE_LIST[1]['Name'],typelist.MILEAGE_TYPE_LIST[1]['Id'],val_sleep_random)
    print('チェック[睡眠]を入力中....')
    mileage.record_checkbox(date_list,typelist.MILEAGE_TYPE_LIST[2]['Name'],typelist.MILEAGE_TYPE_LIST[2]['Id'])
    print('チェック[アルコール]を入力中....')
    mileage.record_checkbox(date_list,typelist.MILEAGE_TYPE_LIST[3]['Name'],typelist.MILEAGE_TYPE_LIST[3]['Id'])
    print('チェック[食生活]を入力中....')
    mileage.record_checkbox(date_list,typelist.MILEAGE_TYPE_LIST[4]['Name'],typelist.MILEAGE_TYPE_LIST[4]['Id'])
    print('チェック[その他]を入力中....')
    mileage.record_checkbox(date_list,typelist.MILEAGE_TYPE_LIST[5]['Name'],typelist.MILEAGE_TYPE_LIST[5]['Id'])
except:
    mileage.webdriver.quit()
    print('自動入力中にエラーが発生しました')
else:
    # ブラウザを閉じる
    mileage.webdriver.quit()
    print('処理が終了しました')

