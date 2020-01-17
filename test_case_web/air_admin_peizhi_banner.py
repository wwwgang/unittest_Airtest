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

    #查询
    def test_chaxun(self):
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
        # 点击资源配置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[4]/div[1]").click()
        # 点击banner管理
        driver.find_element_by_xpath("//*[@id=\"/resources$Menu\"]/li[1]").click()
        #选择状态
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[2]").click()
        #选择时间
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/span[3]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div/input").send_keys("2020-02-02 00:00:00")
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/span[4]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").send_keys("2020-02-20 00:00:00")

    # 查看
    def test_chakan(self):
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
        # 点击资源配置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[4]/div[1]").click()
        # 点击banner管理
        driver.find_element_by_xpath("//*[@id=\"/resources$Menu\"]/li[1]").click()
        # 点击查看按钮
        driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/button[1]").click()

    # 编辑
    def test_bianji(self):
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
        # 点击资源配置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[4]/div[1]").click()
        # 点击banner管理
        driver.find_element_by_xpath("//*[@id=\"/resources$Menu\"]/li[1]").click()
        #点击编辑
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/button[2]").click()
        # 输入招生计划名称
        driver.find_element_by_id("bannerName").send_keys("bannerTest")
        # 上传图片
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div[2]/div/span/span/div[1]/span/input").send_keys(
            admin_web_images+"/Banner@2x.png")
        # 选择开始时间
        driver.find_element_by_xpath("//*[@id=\"startTime\"]/div/input").click()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div").click()
        # 选择结束时间
        driver.find_element_by_xpath("//*[@id=\"endTime\"]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").send_keys(
            "2020-01-02 00:00:00")
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a[3]").click()
        # time.sleep(1000)
        # 输入跳转链接
        driver.find_element_by_id("redirectUrl").send_keys(
            "http://test.yangcong345.com/xs-h5/activity/agent-school?from=test&planId=171&publisherType=rj")
        # 点击提交
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[9]/div/div/span/button[2]").click()

    # 下线
    def test_xiaxian(self):
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
        # 点击资源配置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[4]/div[1]").click()
        # 点击banner管理
        driver.find_element_by_xpath("//*[@id=\"/resources$Menu\"]/li[1]").click()
        #点击下线
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/button[3]").click()
        #time.sleep(2000)
        #点击取消
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[1]").click()
        # 点击下线
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/button[3]").click()
        #点击确定
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]").click()

    #新建
    def test_xinjian(self):
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
        #以下可修改
        #点击左上角
        # 点击资源配置
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/aside/div/ul/li[4]/div[1]").click()
        # 点击banner管理
        driver.find_element_by_xpath("//*[@id=\"/resources$Menu\"]/li[1]").click()
        #新建
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button").click()
        #输入招生计划名称
        driver.find_element_by_id("bannerName").send_keys("bannerTest")
        #上传图片
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[2]/div[2]/div/span/span/div[1]/span/input").send_keys(admin_web_images+"/banner-primary-spring-festival.png")
        #选择开始时间
        driver.find_element_by_xpath("//*[@id=\"startTime\"]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div").click()
        #选择结束时间
        driver.find_element_by_xpath("//*[@id=\"endTime\"]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").send_keys("2020-01-02 00:00:00")
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a[3]").click()
        #time.sleep(1000)
        #输入跳转链接
        driver.find_element_by_id("redirectUrl").send_keys("http://test.yangcong345.com/xs-h5/activity/agent-school?from=test&planId=171&publisherType=rj")
        #点击保存
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[6]/div/div/span/button[2]").click()


    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
