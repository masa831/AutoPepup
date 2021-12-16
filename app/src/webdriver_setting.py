from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chromedriver_binaryを実行して、パスを通す
try:
    __import__('chromedriver_binary')
except ImportError:
    pass


def create_webdriver(param={'is_prod_env': False, 'is_browser_hidden': False}):
    """create_webdriver (function)

    WebDriverを作成する関数。
    初期化時に入力するparam引数によって、AWS Lambdaでの動作設定と
    ローカル環境での動作設定を切り替えられる。

    Args:
        param (dict, optional):
            開発環境とブラウザ表示の設定。
            ・'is_prod_env'
                True : AWS Lambdaで動かすための設定を行う。
                False: ローカル環境で動かすための設定を行う。
            ・'is_browser_hidden'
                True : ブラウザの表示設定を非表示にする。
                False: ブラウザの表示設定を表示にする。
                ('is_prod_env'がTrueの場合は、強制的にFalseになる)
            Defaults to {'is_prod_env': False, 'is_browser_hidden': False}.

    Returns:
        selenium.webdriver: webドライバ
    """

    options = Options()

    # AWS Lambda setting
    is_prod_env = param.get('is_prod_env')
    if (is_prod_env is not None) and (is_prod_env is True):
        # Lamda Layerに追加したパスを指定する
        executable_path = '/opt/headless/bin/chromedriver'
        options.binary_location = '/opt/headless/bin/headless-chromium'
        # Hidden setting
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--single-process")
        options.add_argument('--disable-dev-shm-usage')

    # Local env setting
    else:
        executable_path = 'chromedriver'
        # Hidden setting
        is_browser_hidden = param.get('is_browser_hidden')
        if (is_browser_hidden is not None) and (is_browser_hidden is True):
            options.add_argument('--headless')

    # Create web driver
    driver = webdriver.Chrome(executable_path=executable_path, options=options)
    return driver
