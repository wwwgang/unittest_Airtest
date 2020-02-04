# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/4 1:37 下午
# software: PyCharm
__author__ = "yangcong"

from test_case_android import *


class WSTestcase(unittest.TestCase):
    """切换年级"""

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=android_address)

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        clear_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')

    def test_primarySchool_allCourse_change_class(self):
        """小学年级之间切换"""
        poco = self.poco
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_account("banner1", "y123456")
        app.login_after_swipe()
        General_Assertion_Onion_App(poco).check_login()
        # 全部课程页面右上角切换年级
        poco(text="tabIcon 全部课程").click()
        '''小学'''
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="一年级").click()

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="二年级").click()

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="三年级").click()

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="四年级").click()

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="五年级").click()

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="六年级").click()

        yangcongIcon = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.widget.Image").exists()
        assert_equal(yangcongIcon, True, "判断洋葱icon是否存在")

    def test_primarySchool_allCourse_change_juniorHighSchool_class(self):
        """小学和初中相互切换"""
        poco = self.poco
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_account("banner1", "y123456")
        app.login_after_swipe()
        General_Assertion_Onion_App(poco).check_login()

        poco(text="tabIcon 全部课程").click()
        # 小学切换
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="小学").click()
        poco(text="六年级").click()
        # 切换为中学
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[0].click(focus=(0.1, 0.1))
        poco(text="初中").click()
        poco(text="七年级").click()
        # 切换为小学
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/bottomNavigationView").offspring(
            "com.yangcong345.android.phone:id/itemContainer5").child("android.widget.FrameLayout").wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/bottomNavigationView").offspring(
            "com.yangcong345.android.phone:id/itemContainer5").child("android.widget.FrameLayout").click()
        poco(text="我知道了").click()
        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="三年级").click()

        yangcongIcon = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.widget.Image").exists()
        assert_equal(yangcongIcon, True, "判断洋葱icon是否存在")

    def test_my_change_class(self):
        """我的页面年级切换"""
        poco = self.poco
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_account("banner1", "y123456")
        app.login_after_swipe()
        General_Assertion_Onion_App(poco).check_login()
        # 全部课程页面右上角切换年级
        poco(text="邀请有奖").wait_for_appearance()
        # 这里总会点到我的班级，目前观察原因是分销入口载入过慢，所以先使用结构树寻找
        # poco(text="我的年级").click()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.view.View")[6].click()
        poco(text="小学").click()
        poco(text="一年级").click()

        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="二年级").click()

        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="三年级").click()

        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="四年级").click()

        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="五年级").click()

        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="六年级").click()

        poco(text="tabIcon 全部课程").click()
        yangcongIcon = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("mainContent").child("android.widget.Image").exists()
        assert_equal(yangcongIcon, True, "判断洋葱icon是否存在")

    def tearDown(self) -> None:
        stop_app('com.yangcong345.android.phone')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
