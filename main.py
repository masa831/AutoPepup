import time
from app.src.auto_record_mileage import AutoRecordMileage
from app.src.date_generator import DateGenerator
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

start = time.time()

# ウェブドライバー設定
# ブラウザ非表示
mileage.webdriver = create_webdriver(param={'is_browser_hidden': True})
# ブラウザ表示 debug用
# mileage.webdriver = create_webdriver(param={'is_browser_hidden': False})

print('[start process]')
# ログイン処理
mileage.login_pepup(privateInfo.MY_MAIL_ADDRESS,privateInfo.LOGIN_PASS)

# 歩数、睡眠時間入力用乱数設定
val_step_random = RandomGenerator(10000,11000,1)
val_sleep_random = RandomGenerator(7.0,7.5,0.1) #固定値入力に対応していない可能性あり

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
    print('[An error has occurred]')
else:
    # ブラウザを閉じる
    mileage.webdriver.quit()
    print('[process is succesful]')

process_time = time.time() - start
print("Execution time is {:.4g}[s]".format(process_time))
