# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''分销活动'''

    @classmethod
    def setUpClass(cls) -> None:
        # 日志路径
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        # self.driver = WebChrome(chromedrive_path, chrome_options=chrome_options)
        # self.driver.set_window_size(2560, 1440)
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_course(self):
        '''活动设置新增商品'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/course/list")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")


    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
