class AutoRecordMileageParameter:
    """AutoRecordMileageParameter (parameter)

    AutoRecordMileageParameterクラスのパラメータ。

    """
    # 自動入力用パラメータ(Idの値を利用して、各種マイレージにアクセスする)
    MILEAGE_TYPE_LIST = [
        {'Name': 'StepInput',    'Type': 'step',  'Id': 4},     # 歩数入力
        {'Name': 'SleepInput',   'Type': 'sleep', 'Id': 5},     # 睡眠入力
        {'Name': 'SleepCheck',   'Type': 'check', 'Id': 6},     # 睡眠チェック
        {'Name': 'AlcoholCheck', 'Type': 'check', 'Id': 7},     # アルコールチェック
        {'Name': 'DietCheck',    'Type': 'check', 'Id': 8},     # 食生活チェック
        {'Name': 'OtherCheck',   'Type': 'check', 'Id': 9}      # その他のチェック
    ]


class DateGeneratorParameter:
    """DateGeneratorParameter (parameter)

    DateGeneratorクラスのパラメータ。

    """
    INCLUDE_LAST_MONTH_THRESH_DAY = 10
    WEEKDAY_LABEL_LIST = ['Monday', 'Tuesday', 'Wednesday',
                          'Thursday', 'Friday', 'Saturday', 'Sunday']


class WebdriverParameter:
    """WebdriverParameter (parameter)

    webdriver_function.pyファイルで使用するパラメータ。

    """
    # 待機時間[秒]
    #WAIT_TIME_SEC = 0.5
    WAIT_TIME_SEC = 0.1
    
    # ----------------------------------------------------------------------------------------------------
    # ログイン関連
    # ----------------------------------------------------------------------------------------------------
    # ページURL
    HOME_URL = 'https://pepup.life/users/sign_in'
    MILLAGE_URL = "https://pepup.life/scsk_mileage_campaigns"

    # ログインページのコンテンツ名(=ページタイトル)
    HOME_CONTENT_TEXT = "Pep Up（ペップアップ）"

    LOGIN_EMAIL_XPATH = "//input[@name='user[email]']"
    LOGIN_PASS_XPATH = "//input[@name='user[password]']"
    LOGIN_COMMIT_XPATH = "//input[@name='commit']"
    HOME_CONTENT_XPATH = "//html/head/meta[5]"
    MILLAGE_LINK_XPATH = "//a[@href='/scsk_mileage_campaigns']"

    # ----------------------------------------------------------------------------------------------------
    # 月選択のプルダウン関連
    # ----------------------------------------------------------------------------------------------------
    MONTH_SELECT_BOX_XPATH = ("//html/body/div[1]/div/div[2]/div/div[2]"
                              "/div/div[3]/select")
    MONTH_PULLDOWN_FORMAT = '/scsk_mileage_campaigns/{}'

    # ----------------------------------------------------------------------------------------------------
    # 日付ボタン
    # ----------------------------------------------------------------------------------------------------
    DAY_BUTTON_XPATH_FORMAT = ("/html/body/div[1]/div/div[2]/div/div[2]"
                               "/div/div[{}]/div[2]/div[1]/div[2]/div[2]"
                               "/div[{}]/div[{}]/button")

    # ----------------------------------------------------------------------------------------------------
    # テキスト入力関連
    # ----------------------------------------------------------------------------------------------------
    INPUT_TEXTBOX_XPATH = ("//html/body/div[4]/div[3]/div[2]/form/input")
    INPUT_CANCEL_BUTTON_XPATH = ("//html/body/div[4]/div[3]/div[2]/form"
                                 "/div/button[2]")
    INPUT_DONE_BUTTON_XPATH = ("//html/body/div[4]/div[3]/div[2]/form/"
                               "div/button[1]")

    # ----------------------------------------------------------------------------------------------------
    # チェック入力関連
    # ----------------------------------------------------------------------------------------------------
    CHECK_ATTRIBUTE = "checked"
    CHECK_CHECKBOX_LIST_XPATH = ("//html/body/div[4]/div[3]/div[3]/div")
    CHECK_CHECKBOX_XPATH_FORMAT = ("//html/body/div[4]/div[3]/div[3]/"
                                   "div[{}]/label/input")
    CHECK_CHECKBOX_TEXT_XPATH_FORMAT = ("//html/body/div[4]/div[3]/div[3]"
                                        "/div[{}]/label")
    CHECK_CLOSE_BUTTON_XPATH_FORMAT = ("//html/body/div[4]/div[3]/div[3]"
                                       "/div[{}]/button")

    # ----------------------------------------------------------------------------------------------------
    # ラジオボックス入力関連
    # ----------------------------------------------------------------------------------------------------
    RADIO_ATTRIBUTE = "checked"
    RADIO_TITLE_TEXT_XPATH = ("//html/body/div[4]/div[3]/div[2]/div[2]")
    RADIO_CHECKBOX_LIST_XPATH = ("//html/body/div[4]/div[3]/div[2]"
                                 "/form/div[1]")
    RADIO_CHECKBOX_XPATH_FORMAT = ("//html/body/div[4]/div[3]/div[2]/"
                                   "form/div[1]/div[{}]/input")
    RADIO_CHECKBOX_TEXT_XPATH_FORMAT = ("//html/body/div[4]/div[3]/div[2]"
                                        "/form/div[1]/div[{}]/label")
    RADIO_RECORD_BUTTON_XPATH = ("//html/body/div[4]/div[3]/div[2]/form"
                                 "/div[2]/button[1]")
    RADIO_CLOSE_BUTTON_XPATH = ("//html/body/div[4]/div[3]/div[2]/form"
                                "/div[2]/button[2]")
