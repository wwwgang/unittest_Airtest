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
        self.driver = WebChrome(chromedrive_path, chrome_options=chrome_options)
        self.driver.set_window_size(2560, 1440)
        # self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_change_activity_time(self):
        '''活动起止时间'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/activities/config")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 清空活动起止时间
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/span/span/div/i[2]').click()
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]/div/div/span/span/div/i[2]').click()
        # 开始时间
        t1 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[1]').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # 结束时间
        t2 = datetime.datetime.fromtimestamp(time.time() + 86400).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[2]').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # 提交并确认
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/button[2]').click()

        def check_submit():
            pro_status = driver.page_source
            status = '修改活动时间成功'
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_submit(), True, '校验是否修改成功')

    def test_add_goods(self):
        '''新增商品'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/activities/config")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 点击新增商品
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[2]/button').click()
        # 选中第一个商品
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input').click()
        # 确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()

    def test_del_goods(self):
        '''删除商品'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/activities/config")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 删除第一个商品
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/span').click()
        # 确认删除
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()

    def test_app_entrance(self):
        '''app入口开关'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/activities/config")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        def check_take_button():
            status = 'APP-我的入口'
            pro_status = driver.page_source
            if status in pro_status:
                return True
            else:
                return False

        # 第一次点击
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[4]/div[2]/button').click()
        assert_equal(check_take_button(), True, '校验app我的入口按钮状态是否改变')
        sleep(5)
        # 第二次点击
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[4]/div[2]/button').click()
        check_take_button()
        assert_equal(check_take_button(), True, '校验app我的入口按钮状态是否改变')

    def test_change_entrance(self):
        '''风控金额'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/activities/config")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 第1档风控金额
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[1]/div[2]/div/span/span/span/input').clear()
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[1]/div[2]/div/span/span/span/input').send_keys(
            '150')
        # 第2档风控金额
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div/span/span/span/input').clear()
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[2]/div[2]/div/span/span/span/input').send_keys(
            '350')
        # 点击提交
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[4]/div/form/div[3]/div/div/span/button').click()

        def check_submit():
            status = '修改风控金额成功'
            pro_status = driver.page_source
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_submit(), True, '修改风控金额是否成功')

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
