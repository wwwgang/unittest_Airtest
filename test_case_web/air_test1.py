# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))
        pass

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_1(self):
        driver = self.driver
        driver.maximize_window()
        # admin登录
        login = admin_login(driver)
        driver = login.login()
        driver.get("http://10.8.8.8/admin10/")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
