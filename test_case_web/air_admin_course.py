# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *



class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 日志路径
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_1(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin8/") #进入首页
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/header/div/span").click()#点击导航栏
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li/div").click()
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[1]/ul/li[2]/a").click()
        t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("//input[@placeholder='请输入课程名称']").click()#点击课程
        driver.find_element_by_xpath("//input[@placeholder='请输入课程名称']").send_keys("测试创建课程"
        + t1) #填写课程名称
        driver.find_element_by_xpath("/html/body/div[1]/div/section/section/main/div/div[2]/div/div/div/form/div[2]/div/div[2]/div/span/div/div/div/div").click() #点击选择年级框
        driver.find_element_by_xpath("//li[@title='三年级上册']").click() #选择三年级
        driver.find_element_by_xpath("/html/body/div[1]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/div/div[2]/div/span/div/div/div/div").click()#点击选择教材版本框
        driver.find_element_by_xpath("//div[@title='人教版']").click() #选择人教版
        driver.find_element_by_xpath("/html/body/div[1]/div/section/section/main/div/div[2]/div/div/div/form/div[4]/div/div[2]/div/span/div/div/div/div").click()#点击解锁方式
        driver.find_element_by_xpath("//div[@title='天解锁']").click() #选择天解锁
        driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("2") #选择添加天数
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[7]/div/div/div/div/div/div[2]/div/div").click() #点击任意位置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[7]/div/div/div/div/div/div/table/tbody/tr/td[9]/button").click()#点击继续添加
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div").click()#点击课程选择
        driver.find_element_by_xpath("//li[@aria-selected='false']").click() #选择系统课
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div").click()#点击选择框
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[2]").click() #选择中学阶段
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div").click()#点击选择框
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li[1]").click() #选择小学阶段
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div").click()#点击选择框
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/ul/li[5]").click() #选择小学阶段







        # driver.get("http://10.8.8.8/admin8/course/create")


        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
