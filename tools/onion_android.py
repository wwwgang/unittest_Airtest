# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/1/21 3:49 下午
# software: PyCharm
from airtest.core.api import *


class Onion_App():
    def __init__(self, poco):
        self.poco = poco
        pass

    def HuaWei_init(self):
        poco = self.poco
        # 华为的权限始终允许
        poco("com.android.packageinstaller:id/permission_allow_button").wait_for_appearance()
        poco("com.android.packageinstaller:id/permission_allow_button").click()
        # 华为的权限始终允许
        poco("com.android.packageinstaller:id/permission_allow_button").wait_for_appearance()
        poco("com.android.packageinstaller:id/permission_allow_button").click()

    def agree_agreement(self):
        poco = self.poco
        poco("com.yangcong345.android.phone:id/checkBox").wait_for_appearance()
        poco("com.yangcong345.android.phone:id/checkBox").click()
        poco("com.yangcong345.android.phone:id/continueButton").click()

    def login_mobile(self, mobile):
        poco = self.poco
        # 登录
        # 输入手机号
        poco("com.yangcong345.android.phone:id/inputEditText").set_text(mobile)
        # text("18618262234")
        poco("com.yangcong345.android.phone:id/nextButton").click()
        # 输入验证码
        text("1", enter=False)
        text("1", enter=False)
        text("1", enter=False)
        text("1", enter=False)

    def login_account(self, username, password):
        poco = self.poco
        # 登录
        # 账号登录
        poco(text="用户名").click()
        poco(text="请输入用户名或邮箱").set_text(username)
        poco(text="下一步").click()
        poco(text="请输入密码").set_text(password)
        poco(text="下一步").click()

    def login_after_swipe(self):
        poco = self.poco
        # 初始化三图滑动
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").wait_for_appearance()
        poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.yangcong345.android.phone:id/flFragmentContainer").offspring("android.widget.RelativeLayout").child(
            "android.webkit.WebView").offspring("root").child("android.view.View").wait_for_appearance()
        sleep(3)
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
