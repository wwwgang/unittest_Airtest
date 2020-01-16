# unittest_Airtest      

## web ui自动化
### (unittest+airtest+html-testRunner+airtest-selenium+selenium)  

`使用环境`  

推荐：python3.6.5  

`使用说明：`     

1、安装依赖  pip install -r requirments.txt  

2、在tools中换上自己的Chromedriver  `下载地址:`http://npm.taobao.org/mirrors/chromedriver/  

3、在test_case_web中编写case，case文件名要求为air*.py,可以借助airtestIDE进行录制，复制粘贴其中脚本代码    

4、执行run_all_web_case.py即可运行test_case中的所有以air_*.py文件的case   

5、跑完case后，执行export_web_report.py生成测试报告  

6、在reports.html中可查看unittest报告 

7、在__init__.log中存在log.html可查看全部case的airtest报告   

8、在项目根目录下，会生成对应case的单py文件的airtest报告，测试报告仍为log.html  

## android ui 自动化       
### (unittest+airtest+poco+html-testRunner)     

`使用说明`  

1、安装依赖  pip install -r requirments.txt  

2、使用airtestIDE连接手机，自动安装必要软件，`安卓连接常见问题`：https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/

3、在config中存在android_address参数为android设备地址，如有线连接请忽略此步骤，无线连接请配置，例：Android://127.0.0.1:5037/10.254.60.1:5555，`详情阅读`https://airtest.doc.io.netease.com/IDEdocs/device_connection/1_android_phone_connection/#3     

4、在test_case_android中编写case，case文件名要求为air*.py,可以借助airtestIDE进行录制，复制粘贴其中脚本代码 

5、跑完case后，执行export_android_report.py生成测试报告  

6、在__init__.log中存在log.html可查看全部case的airtest报告   

7、在项目根目录下，会生成对应case的单py文件的airtest报告，测试报告仍为log.html  

chomd +x /Users/yangcong/PycharmProjects/unittest_Airtest/venv/lib/python3.6/site-packages/airtest/core/android/static/adb/mac/adb

## ios ui 自动化       
### (unittest+airtest+poco+html-testRunner)  