# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_android import *
import logging


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=[
                "Android://127.0.0.1:5037",
            ])

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        stop_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')
        sleep(15)

    def test_login(self):
        poco = self.poco

        try:
            poco(text="一年级").click()
        except Exception as e:
            log(e)
        try:
            poco(text="二年级").click()
        except Exception as e:
            log(e)
        try:
            poco(text="三年级").click()
        except Exception as e:
            log(e)
        try:
            poco(text="四年级").click()
        except Exception as e:
            log(e)
        try:
            poco(text="五年级").click()
        except Exception as e:
            log(e)
        try:
            poco(text="六年级").click()
        except Exception as e:
            log(e)

        poco(text="小学").click()
        poco(text="五年级").click()

    def tearDown(self) -> None:
        stop_app('com.yangcong345.android.phone')

    @classmethod
    def tearDownClass(cls) -> None:
        pass

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="/Users/yangcong/Desktop/andlog")

# unittest.main()
