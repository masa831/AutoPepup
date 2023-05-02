from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# chromedriver_binaryを実行して、パスを通す
try:
    __import__('chromedriver_binary')
except ImportError:
    pass


def create_webdriver(param={'is_browser_hidden': False}):
    """create_webdriver (function)

    WebDriverを作成する関数。
    初期化時に入力するparam引数によって、ブラウザ表示/非表示を切り替えられる。

    Args:
        param (optional):
            ブラウザ表示の設定。
            ・'is_browser_hidden'
                True : ブラウザの表示設定を非表示にする。
                False: ブラウザの表示設定を表示にする。
                ('is_prod_env'がTrueの場合は、強制的にFalseになる)
            Defaults to {'is_prod_env': False, 'is_browser_hidden': False}.

    Returns:
        selenium.webdriver: webドライバ
    """

    options = Options()

    # Local env setting

    executable_path = 'chromedriver' # 場合によっては、絶対パスで指定する
    # Hidden setting
    is_browser_hidden = param.get('is_browser_hidden')
    if (is_browser_hidden is not None) and (is_browser_hidden is True):
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #コンソールに出てくる余計なメッセージを消去

    # Create web driver
    driver = webdriver.Chrome(executable_path=executable_path, options=options)
    return driver
