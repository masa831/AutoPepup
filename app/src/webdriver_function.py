import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from app.src.parameter import WebdriverParameter as Param


def check_login_success(webdriver):
    """check_login_success (function)

    ログインに成功したかを判定する関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        boolean: ログイン成功フラグ(True：成功、False：失敗)。
    """
    content_xpath = Param.HOME_CONTENT_XPATH
    content_text = Param.HOME_CONTENT_TEXT

    meta = webdriver.find_element_by_xpath(content_xpath)
    if meta.get_attribute('content') == content_text:
        return True
    return False


def access_login_url(webdriver):
    """access_login_url (function)

    ログインページにアクセスする関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        boolean: 既にログインしているか(True：ログイン中、False：未ログイン)。
    """
    url = Param.HOME_URL

    webdriver.get(url)
    time.sleep(Param.WAIT_TIME_SEC)

    return check_login_success(webdriver)


def run_login(webdriver, address, password):
    """run_login (function)

    ログインを実施する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        address ([type]): [description]
        password ([type]): [description]

    Returns:
        boolean: ログイン成功フラグ(True：成功、False：失敗)。
    """
    email_xpath = Param.LOGIN_EMAIL_XPATH
    pass_xpath = Param.LOGIN_PASS_XPATH
    commit_xpath = Param.LOGIN_COMMIT_XPATH

    webdriver.find_element_by_xpath(email_xpath).send_keys(address)
    webdriver.find_element_by_xpath(pass_xpath).send_keys(password)

    webdriver.find_element_by_xpath(commit_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)

    return check_login_success(webdriver)


def access_mileage_url(webdriver):
    """access_mileage_url (function)

    マイレージのページにアクセスする関数。

    Args:
        webdriver (selenium.driver): webドライバ。
    """
    url = Param.MILLAGE_URL

    webdriver.get(url)
    time.sleep(Param.WAIT_TIME_SEC)


def select_month(webdriver, month_date):
    """select_month (function)

    プルダウンで月移動を実施する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        month_date (string): [YYYY/MM]の文字列。
    """
    select_xpath = Param.MONTH_SELECT_BOX_XPATH
    pulldown_format = Param.MONTH_PULLDOWN_FORMAT
    pulldown = pulldown_format.format(month_date)

    # 「過去の記録を見る」のエレメントを取得
    box_element = webdriver.find_element_by_xpath(select_xpath)
    select_element = Select(box_element)
    # 移動先の月を選択
    select_element.select_by_value(pulldown)
    time.sleep(Param.WAIT_TIME_SEC)


def click_day(webdriver, millage_id, week_id, day_id):
    """click_day (function)

    日付ボタンのクリックを実施する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        millage_id (int): 入力項目のID。
        week_id (int): 週のID(カレンダーの行インデックス)。
        day_id (int): 日にちのID(カレンダーの列インデックス)。
    """
    day_xpath_format = Param.DAY_BUTTON_XPATH_FORMAT
    day_xpath = day_xpath_format.format(millage_id, week_id, day_id)

    webdriver.find_element_by_xpath(day_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def get_textbox(webdriver):
    """get_textbox (function)

    テキストボックスに入力されているテキストを取得する関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        string: テキストボックスに入力されているテキスト。
    """
    input_xpath = Param.INPUT_TEXTBOX_XPATH

    # テキストボックスのelement取得
    textbox_elem = webdriver.find_element_by_xpath(input_xpath)
    # 現在の入力値を取得
    value_text = textbox_elem.get_attribute('value')
    time.sleep(Param.WAIT_TIME_SEC)

    return value_text

#------------------------------------------------------------
def reset_textbox(webdriver):
    """reset_textbox (function)

    テキストボックスに入力されているテキストを消去し空欄にする関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    """
    input_xpath = Param.INPUT_TEXTBOX_XPATH
    done_xpath = Param.INPUT_DONE_BUTTON_XPATH

    # テキストボックスのelement取得し、テキストをクリアする
    textbox_elem = webdriver.find_element_by_xpath(input_xpath)
    textbox_elem.clear()
    time.sleep(Param.WAIT_TIME_SEC)

    # 記録ボタンをクリック(Doneを押した後にCancelを押してマイレージページに遷移する)
    webdriver.find_element_by_xpath(done_xpath).click()
    
#------------------------------------------------------------

def set_textbox(webdriver, input_text):
    """set_textbox (function)

    テキスト入力項目のダイアログのテキストボックスに値を入力する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        input_text (string): 入力するテキスト。
    """
    input_xpath = Param.INPUT_TEXTBOX_XPATH
    done_xpath = Param.INPUT_DONE_BUTTON_XPATH

    # テキストボックスのelement取得し、テキストを入力
    textbox_elem = webdriver.find_element_by_xpath(input_xpath)
    textbox_elem.send_keys(input_text)
    time.sleep(Param.WAIT_TIME_SEC)

    # 記録ボタンをクリック(Doneを押した後にCancelを押してマイレージページに遷移する)
    webdriver.find_element_by_xpath(done_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def click_textbox_cancel(webdriver):
    """click_textbox_cancel (function)

    テキスト入力項目のダイアログのキャンセルボタンを押す関数。

    Args:
        webdriver (selenium.driver): webドライバ。
    """
    cancel_xpath = Param.INPUT_CANCEL_BUTTON_XPATH

    # キャンセルボタンをクリック
    webdriver.find_element_by_xpath(cancel_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def get_checkbox_num(webdriver):
    """get_checkbox_num (function)

    ダイアログに表示されたチェックボックスの個数をカウントする関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        int: チェックボックス数。
    """
    list_xpath = Param.CHECK_CHECKBOX_LIST_XPATH

    checkbox_list = webdriver.find_elements_by_xpath(list_xpath)
    checkbox_num = len(checkbox_list) - 1
    return checkbox_num


def check_checkbox(webdriver, index):
    """check_checkbox (function)

    未入力のチェックボックスにチェックを入れる関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        index (int): 上から何番目のチェックボックスか。

    Returns:
        boolean: 入力実施フラグ(True：入力実施、False：入力済み)。
    """
    check_attr = Param.CHECK_ATTRIBUTE
    check_xpath_format = Param.CHECK_CHECKBOX_XPATH_FORMAT
    check_xpath = check_xpath_format.format(index + 1)

    # チェックボックスのelement取得
    checkbox_elem = webdriver.find_element_by_xpath(check_xpath)
    time.sleep(Param.WAIT_TIME_SEC)

    # 未チェックのチェックボックスにチェックを入れる
    if checkbox_elem.get_attribute(check_attr) is None:
        checkbox_elem.click()
        time.sleep(Param.WAIT_TIME_SEC)
        return True

    return False


def check_radiobox(webdriver):
    """check_radiobox (function)

    未入力のラジオボタンにチェックを入れる関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        boolean: 入力実施フラグ(True：入力実施、False：入力済み)。
    """
    radio_attr = Param.RADIO_ATTRIBUTE
    list_xpath = Param.RADIO_CHECKBOX_LIST_XPATH
    radio_xpath_format = Param.RADIO_CHECKBOX_XPATH_FORMAT

    radiobox_list = webdriver.find_elements_by_xpath(list_xpath)

    # 入力済みであるかを確認
    for idx in range(len(radiobox_list)):
        radio_xpath = radio_xpath_format.format(idx + 1)
        radiobox_elem = webdriver.find_element_by_xpath(radio_xpath)
        time.sleep(Param.WAIT_TIME_SEC)

        # 入力済みの場合は、Falseを返す
        if radiobox_elem.get_attribute(radio_attr) is not None:
            return False

    # 入力済みでない場合、チェックボックスにチェックを入れる
    radio_xpath = radio_xpath_format.format(1)
    webdriver.find_element_by_xpath(radio_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)

    return True


def get_checkbox_type(webdriver):
    """get_checkbox_type (function)

    チェックボックスかラジオボックスかを判定する関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        string: タイプ文字列(CheckBox：チェックボックス、RadioBox：ラジオボック、空文字：その他）。
    """
    check_xpath = Param.CHECK_CHECKBOX_LIST_XPATH
    radio_xpath = Param.RADIO_CHECKBOX_LIST_XPATH

    checklist = webdriver.find_elements_by_xpath(check_xpath)
    radiolist = webdriver.find_elements_by_xpath(radio_xpath)

    # 閉じるボタンを含めないため、-1している
    check_num = len(checklist) - 1
    radio_num = len(radiolist)

    if check_num > 0:
        return 'CheckBox'
    elif radio_num > 0:
        return 'RadioBox'
    return ''


def get_checkbox_text(webdriver, index):
    """get_checkbox_text (function)

    チェックボックスに記載されているテキストを取得する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        index (int): 上から何番目のチェックボックスか。

    Returns:
        strin: チェックボックスに記載されているテキスト。
    """
    text_xpath_format = Param.CHECK_CHECKBOX_TEXT_XPATH_FORMAT
    text_xpath = text_xpath_format.format(index + 1)

    checktext_elem = webdriver.find_element_by_xpath(text_xpath)
    return checktext_elem.text


def get_radiobox_text(webdriver):
    """get_radiobox_text (function)

    ラジオボタンに記載されているテキストを取得する関数。

    Args:
        webdriver (selenium.driver): webドライバ。

    Returns:
        string: ラジオボタンに記載されているテキスト。
    """
    text_xpath_format = Param.RADIO_CHECKBOX_TEXT_XPATH_FORMAT
    text_xpath = text_xpath_format.format(1)

    radiotext_elem = webdriver.find_element_by_xpath(text_xpath)
    return radiotext_elem.text


def click_checkbox_close(webdriver):
    """click_checkbox_close (function)

    チェック項目のタイアログの閉じるボタンを押す関数。

    Args:
        webdriver (selenium.driver): webドライバ。
    """
    list_xpath = Param.CHECK_CHECKBOX_LIST_XPATH
    close_xpath_format = Param.CHECK_CLOSE_BUTTON_XPATH_FORMAT

    checklist = webdriver.find_elements_by_xpath(list_xpath)
    close_button_idx = len(checklist)

    close_xpath = close_xpath_format.format(close_button_idx)
    webdriver.find_element_by_xpath(close_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def click_radiobox_record(webdriver):
    """click_radiobox_record (function)

    ラジオボタン項目のタイアログの更新ボタンを押す関数。

    Args:
        webdriver (selenium.driver): webドライバ。
    """
    record_xpath = Param.RADIO_RECORD_BUTTON_XPATH

    webdriver.find_element_by_xpath(record_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def click_radiobox_close(webdriver):
    """click_radiobox_close (function)

    ラジオボタン項目のタイアログの[閉じる]ボタンを押す関数。

    Args:
        webdriver (selenium.driver): webドライバ。
    """
    close_xpath = Param.RADIO_CLOSE_BUTTON_XPATH

    webdriver.find_element_by_xpath(close_xpath).click()
    time.sleep(Param.WAIT_TIME_SEC)


def check_mileage(webdriver, millage_id, week_id, day_id):
    """check_mileage (function)

    マイレージIDに対応する入力項目が存在するかを確認する関数。

    Args:
        webdriver (selenium.driver): webドライバ。
        millage_id (int): 入力項目のID。
        week_id (int): 週のID(カレンダーの行インデックス)。
        day_id (int): 日にちのID(カレンダーの列インデックス)。

    Returns:
        boolean: 入力項目存在フラグ(True：あり、False：なし)。
    """
    day_xpath_format = Param.DAY_BUTTON_XPATH_FORMAT
    day_xpath = day_xpath_format.format(millage_id, week_id, day_id)

    try:
        # 日付ボタンの有無から入力項目があるかを判定
        webdriver.find_element_by_xpath(day_xpath)
        time.sleep(Param.WAIT_TIME_SEC)
    except NoSuchElementException:
        return False

    return True
