# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_android import *


class WSTestcase(unittest.TestCase):
    """app登录"""

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=android_address)

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        clear_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')

    def test_login_mobile(self):
        """验证码登录"""
        poco = self.poco
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_mobile("18618262234")
        app.login_after_swipe()
        General_Assertion_Onion_App(poco).check_login()

    def test_login_account(self):
        """账号登录"""
        poco = self.poco
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_account("banner1", "y123456")
        app.login_after_swipe()
        General_Assertion_Onion_App(poco).check_login()

    def tearDown(self) -> None:
        stop_app('com.yangcong345.android.phone')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
