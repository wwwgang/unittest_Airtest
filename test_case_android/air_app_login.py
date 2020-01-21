# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_android import *


class WSTestcase(unittest.TestCase):
    '''app登录'''

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=android_address)

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        clear_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')

    def test_login_mobile(self):
        '''验证码登录'''
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
        poco("com.yangcong345.android.phone:id/inputEditText").set_text("18618262234")
        # text("18618262234")
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

    def test_login_account(self):
        '''账号登录'''
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
        # 账号登录
        poco(text="用户名").click()
        poco(text="请输入用户名或邮箱").set_text("banner1")
        poco(text="下一步").click()
        poco(text="请输入密码").set_text("y123456")
        poco(text="下一步").click()
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
