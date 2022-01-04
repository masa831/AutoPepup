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
[add] options.add_experimental_option('excludeSwitches', ['enable-logging']) 


