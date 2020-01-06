# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_1(self):
        driver = self.driver
        driver.maximize_window()

        # admin登录
        login = admin_login(driver)
        login.login()

        driver.get("http://10.8.8.8/admin10/configure/admission")

        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div/div/div/div[2]/span", "xpath",
                            "校验进入招生计划管理")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th",
            "xpath", "校验表单“序号”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[2]/span/div/span",
            "xpath", "校验表单“招生计划名称”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[3]/span/div/span",
            "xpath", "校验表单“班型”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[4]/span/div/span",
            "xpath", "校验表单“招生开始时间”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[5]/span/div/span",
            "xpath", "校验表单“招生结束时间”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[6]/span/div/span",
            "xpath", "校验表单“是否付费”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[7]/span/div/span",
            "xpath", "校验表单“当前状态”")

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[8]/span/div/span",
            "xpath", "校验表单“操作")

        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button", "xpath",
                            "校验“新建”")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
