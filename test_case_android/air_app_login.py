# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_android import *
import logging


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=android_address)

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        clear_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')

    def test_login(self):
        # 验证码登录
        poco = self.poco
        # 华为的权限始终允许
        poco("com.android.packageinstaller:id/permission_allow_button").wait_for_appearance()
        poco("com.android.packageinstaller:id/permission_allow_button").click()
        # 华为的权限始终允许
        poco("com.android.packageinstaller:id/permission_allow_button").wait_for_appearance()
        poco("com.android.packageinstaller:id/permission_allow_button").click()
        # 洋葱的同意并允许
        poco("com.yangcong345.android.phone:id/checkBox").wait_for_appearance()
        poco("com.yangcong345.android.phone:id/checkBox").click()
        poco("com.yangcong345.android.phone:id/continueButton").click()
        # 登录
        # 输入手机号
        poco("com.yangcong345.android.phone:id/inputEditText").click()
        text("18618262234")
        poco("com.yangcong345.android.phone:id/nextButton").click()
        # 输入验证码
        text("1", enter=False)
        text("1", enter=False)
        text("1", enter=False)
        text("1", enter=False)
        # 初始化三图滑动
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("root").child("android.view.View").wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").swipe([-0.8, -0.1])
        sleep(3)
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").swipe([-0.8, -0.1])
        sleep(3)
        poco(text="goods").wait_for_appearance()
        poco(text="goods").click()

        poco(text="tabIcon 我的").wait_for_appearance()
        poco(text="tabIcon 我的").click()
        user_name = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].exists()
        assert_equal(user_name, True, "用户名是否存在")

    def tearDown(self) -> None:
        stop_app('com.yangcong345.android.phone')

    @classmethod
    def tearDownClass(cls) -> None:
        pass

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="/Users/yangcong/Desktop/andlog")

# unittest.main()
