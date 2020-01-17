# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    ''''''
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
        ''''''
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


    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
