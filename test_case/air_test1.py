# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_1(self):
        driver = self.driver
        driver.maximize_window()

        # 以下可修改
        driver.get("https://yangcong345.com/#/studentPage")
        driver.find_element_by_xpath("//span[@title='登录']").click()
        driver.find_element_by_id("username").send_keys('18618262234')
        driver.find_element_by_id("password").send_keys('wanggang00')
        driver.assert_exist("//*[@id=\"normal\"]/button", "xpath", "进入登录页")
        driver.assert_exist("//*[@id=\"norsmal\"]/button", "xpath", "测试异常")

    def test_2(self):
        print('test2')

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
