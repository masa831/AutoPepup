# autoPepup

## 履歴

***

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

### chromedriverのバージョンについて

以下のコマンドでバージョンアップロードする
conda install -c conda-forge python-chromedriver-binary=98.0.4758.80
conda install -c conda-forge python-chromedriver-binary=107.0.5304.88
※オプション -c conda-forge は有償のパッケージ以外も対象にしてくれる

以下のコマンドでバージョンを検索する
conda search -c conda-forge python-chromedriver-binary=107*

pip install chromedriver-binary==107.0.5304.62.0

### conda pip の違い

参考URL
<https://yurufuwadiary.com/conda-or-pip>

### chromedriverについて

適宜バージョンは更新する必要あり
<https://chromedriver.chromium.org/downloads>
※ただし、現状ではなぜかchrome-binaryでないと動かない可能性あり

### Pyreverse & graphviz

<https://makutsueeken5.hatenablog.com/entry/2019/02/13/145049>

<https://progzakki.sanachan.com/program-lang/python/how-to-generate-image-of-class-structure/>

<https://qiita.com/kenichi-hamaguchi/items/c0b947ed15725bfdfb5a>

### pyside6 sampleCode

<https://rikoubou.hatenablog.com/entry/2022/04/29/115254>
