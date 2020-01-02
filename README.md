# unittest_Airtest      

## web ui自动化
### (unittest+airtest+poco+html-testRunner+airtest-selenium+selenium)  

`使用环境`  

推荐：python3.6.5  

`使用说明：`     

1、安装依赖  pip install -r requirments.txt  

2、在tools中换上自己的Chromedriver  `下载地址:`http://npm.taobao.org/mirrors/chromedriver/  

3、执行run_all_case.py即可运行test_case中的所有以air_*.py文件的case   

4、跑完case后，执行export_web_report.py生成测试报告  

5、在test_case中编写case可以借助airtestIDE进行录制，复制粘贴其中脚本代码    

6、在reports.html中可查看unittest报告 

7、在__init__.log中存在log.html可查看全部case的airtest报告

8、在项目根目录下，会生成对应case的单py文件的airtest报告，测试报告仍为log.html