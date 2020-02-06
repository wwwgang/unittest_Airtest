# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/5 12:47 下午
# software: PyCharm
__author__ = "yangcong"

from test_case_android import *


class WSTestcase(unittest.TestCase):
    """用户绑定手机号"""

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=android_log_path + '/' + os.path.basename(__file__), devices=android_address)

    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        clear_app('com.yangcong345.android.phone')
        start_app('com.yangcong345.android.phone')

    def test_user_binding_mobile(self):
        """用户绑定手机号"""
        poco = self.poco
        # 绑定手机号前创建账号
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        create_account('autowg' + t, 'w123456')
        # 登录账号
        app = Onion_App(poco)
        app.HuaWei_init()
        app.agree_agreement()
        app.login_account('autowg' + t, "w123456")
        sleep(3)
        if poco("com.yangcong345.android.phone:id/iv_close").exists():
            # 关闭弹窗
            poco("com.yangcong345.android.phone:id/iv_close").click()
        # 切换为小学
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/bottomNavigationView").offspring(
            "com.yangcong345.android.phone:id/itemContainer5").offspring(
            "com.yangcong345.android.phone:id/ivItemIcon").wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/bottomNavigationView").offspring(
            "com.yangcong345.android.phone:id/itemContainer5").offspring(
            "com.yangcong345.android.phone:id/ivItemIcon").click()
        poco(text="我知道了").click()
        poco(text="我的年级").click()
        poco(text="小学").click()
        poco(text="三年级").click()
        # 小学初始化
        app.login_after_swipe()
        sleep(3)
        if poco(text="closeIcon").exists():
            # 关闭弹窗
            poco(text="closeIcon").click()
        General_Assertion_Onion_App(poco).check_login()
        # 绑定手机号
        poco(text="tabIcon 我的课程").click()
        poco(text="绑定手机号").click()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("root").child("android.widget.EditText")[0].set_text(
            get_mobile_csv(mobile_path))
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("root").child("android.widget.EditText")[1].set_text("123456")
        poco("android.widget.Button").click()
        assert_equal(poco(text="选择更多课程").exists(), True, "校验绑定是否成功")

    def tearDown(self) -> None:
        stop_app('com.yangcong345.android.phone')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
