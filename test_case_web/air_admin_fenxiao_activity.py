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

    #新增商品
    def test_jichusehzhi(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 以下可编辑
        #点击分销活动
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[6]/div[1]").click()
        #点击活动设置
        #sleep(1000)
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[6]/ul/li[1]").click()
        #选择时间
        sleep(3)
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/span/span/div/input").clear()
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/span/span/div/input").click()
        # sleep(1000)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]/div/input").click()
        # driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/span/span/div/input").clear()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a').click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[1]/div/input").send_keys("2020-02-02 00:00:00")
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/span/span/div/input").click()
        #driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div/input").send_keys("2020-02-30 00:00:00")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a[3]").click()
        #点击提交
        #sleep(1000)
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/span/button").click()
        #点击取消
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/button[1]").click()
        #点击提交
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/span/button").click()
        #点就确定
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/button[2]").click()
    #删除
    def test_delete(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 以下可编辑
        #点击分销活动
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[6]/div[1]").click()
        #点击活动设置
        #sleep(1000)
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[6]/ul/li[1]").click()
        #点击下线
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/span").click()
        #点击取消
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[1]").click()
        #点击下线
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/span").click()
        #点击确定
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[1]]").click()
    #风控金额
    def test_fengkongjine(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 以下可编辑
        #点击分销活动
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[6]/div[1]").click()
        #点击活动设置
        #sleep(1000)
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[6]/ul/li[1]").click()
        #输入第一档风控
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[1]/div[2]/div/span/span/span/input").clear()
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[1]/div[2]/div/span/span/span/input").send_keys("200")
        #输入第二档风控
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div/span/span/span/input").clear()
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div/span/span/span/input").send_keys("300")
        #点击提交
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[3]/div/div/span/button").click()
    #添加商品
    def test_add_goods(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 以下可编辑
        #点击分销活动
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[6]/div[1]").click()
        #点击活动设置
        #sleep(1000)
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[6]/ul/li[1]").click()
        #点击新增商品按钮
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/button").click()
        #选择商品
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/span/label/span/input").click()
        #点击确定
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]").click()
    #开启入口
    def test_rukou(self):
        driver = self.driver
        driver.maximize_window()  # 窗口最大化

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 以下可编辑
        #点击分销活动
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[6]/div[1]").click()
        #点击活动设置
        #sleep(1000)
        driver.find_element_by_xpath("/html/body/div/div/section/aside/div/ul/li[6]/ul/li[1]").click()
        #开启入口
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[4]/div[2]/button").click()

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
