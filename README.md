# autoPepup

## 環境

環境名：WsPepup

使用環境：pip

## chromedriverのバージョンについて

手順
1.以下のコマンドでバージョンを検索する
conda search -c conda-forge python-chromedriver-binary=107*

2.pipでアップデートする　←この対応が必要かよくわからん、、
pip install chromedriver-binary==107.0.5304.62.0

3.chromedriver.exeのバージョンも合わせる
<https://chromedriver.chromium.org/downloads>

## 変更履歴

***

### 2023/05/01  プログラムが異常終了

原因：webdriver_function.pyの103行目の'box_element = webdriver.find_element_by_xpath(select_xpath)'の
xpathが変更されていたことで遷移ができずにエラー
過去の記録を見ると日付ボタンのパスを修正

メモ：xpathを確認する方法
Webサイトを開き、XPathを取りたい要素を右クリックしてメニューの「検証」をクリック
デベロッパーツールが起動するので、改めてXPathを取りたい要素を右クリックして「Copy」→「Copy XPath」をクリック
これで、クリップボードにXPathがコピーされます
<https://aprico-media.com/posts/7777#:~:text=%E3%81%BE%E3%81%9A%E3%81%AFWeb%E3%82%B5%E3%82%A4%E3%83%88%E3%82%92%E9%96%8B%E3%81%8D,XPath%E3%81%8C%E3%82%B3%E3%83%94%E3%83%BC%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82>

修正後：/html/body/div[1]/div/div[2]/div/main/div/div[3]/select

修正前：/html/body/div[1]/div/div[2]/div/div[2]/div/div[{}]/div[2]/div[1]/div[2]/div[2]/div[{}]/div[{}]/button
修正後：/html/body/div[1]/div/div[2]/div/main/div/div[5]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/button

### 2022/01/04 プログラムが異常終了する現象に遭遇

原因：webdriver_function.pyの103行目の'elect_element.select_by_value(pulldown)'の
pulldownに正しくない入力値が入っていたため

現状：'/scsk_mileage_campaigns/2022/01'
理想：'/scsk_mileage_campaigns/2022/1'

対処：month_dateには現状'2022/0x'となっているのを'2022/x'に修正する
date_generator.py 34行目を変更
'Month': date.strftime('%Y/%m') → 'Month': date.strftime('%Y/%m').replace('/0','/')

追加変更：webdriver_setting.py 55行目を変更
コンソールに出てくる余計なメッセージを消去。
ただし、重要なエラーメッセージも非表示される可能性もあるため、要注意

以下を追加

```python
options.add_experimental_option('excludeSwitches', ['enable-logging'])
```

### 20221105

URLの変更により、不具合が発生
auto_record_mileage.pyの以下の処理が意図通りの動きではない
if wf.check_login_success(self.webdriver):

下記変更により、バグは解消
HOME_CONTENT_TEXT = "Pep Up（ペップアップ）"
→HOME_CONTENT_TEXT = "ホーム - Pep Up(ペップアップ)"

+α　不要なファイルや処理を整理

## Memo

### conda pip の違い

参考URL
<https://yurufuwadiary.com/conda-or-pip>

### Pyreverse & graphviz

<https://makutsueeken5.hatenablog.com/entry/2019/02/13/145049>

<https://progzakki.sanachan.com/program-lang/python/how-to-generate-image-of-class-structure/>

<https://qiita.com/kenichi-hamaguchi/items/c0b947ed15725bfdfb5a>

### pyside6 sampleCode

<https://rikoubou.hatenablog.com/entry/2022/04/29/115254>

### Pythonアプリ化Memo 20221230記

GUI参考URL
<https://qiita.com/nanako_ut/items/b5393363b9e21d6342ea#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E9%81%B8%E6%8A%9E>

<https://maasaablog.com/development/backend/python/4279/>

アプリ起動時　コンソール画面を非表示
<https://genchan.net/it/programming/python/4183/>

アプリ化
<https://umano-ie.com/python-desktop-application/>

コマンドメモ(pyinstaller)
pyinstaller AutoPepup_gui.py -D -F -w --clean --icon=AutoPepup.ico  --name AutoPepup --hidden-import='C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\PySide6' --debug all

pyinstaller AutoPepup_gui.py -D -F --clean -i=AutoPepup.ico  --add-data='.\\log\\pepuplog.txt;\\log\\' --name AutoPepup --hidden-import='C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\PySide6' --debug all

pyinstaller AutoPepup_gui.py -D --clean -i=AutoPepup.ico --name AutoPepup --hidden-import='C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\PySide6' --hidden-import='C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\chromedriver_binary' --hidden-import='C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\selenium' --debug all

パッケージパス
'C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\chromedriver_binary'
'C:\\Users\\zeroc\\anaconda3\\envs\\WsPepup\\lib\\site-packages\\PySide6'

.specファイルに足すといいかも？
a.datas += [('pepuplog.txt', '.\\log\\pepuplog.txt', 'DATA')]

## 後で試したいこと

webdriverについて、
<https://teratail.com/questions/367515>

```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
```

## 現状のApp化時に生じているエラー

・logフォルダが含まれないため、エラー。手動で配置するとエラーは解消される
・上記を解消後はchromedriverのエラーが出ている状態
→chromedriver_binaryを指定してインポートするか、driverManagerを使用してみるか
