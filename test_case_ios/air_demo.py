# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_ios import *


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=ios_log_path + '/' + os.path.basename(__file__), devices=ios_address)

    def setUp(self) -> None:
        self.poco = iosPoco()

    def test_login(self):
        poco = self.poco

        poco("小学").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other").child("Other").child("Other").child("Other").offspring("WebView").child("Other").child(
            "Other").child("Other").offspring("洋葱数学 —— 创造让孩子着迷的学习世界").child("Other")[4].child("Other")[0].child(
            "Other")[1].click()
        poco("小学").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other").child("Other").child("Other").child("Other").offspring("WebView").child("Other").child(
            "Other").child("Other").offspring("洋葱数学 —— 创造让孩子着迷的学习世界").child("Other")[4].child("Other")[0].child(
            "Other")[1].click()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
