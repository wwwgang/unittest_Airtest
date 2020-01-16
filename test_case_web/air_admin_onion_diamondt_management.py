# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''葱钻管理'''

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_increase(self):
        ''' 增加葱钻'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/dimand/manage")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索18618262234手机号
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div/div/span/span/input').send_keys(
            '18618262234')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div/div/span/span/input').send_keys(
            Keys.ENTER)
        local_pro_status = driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]').text

        def get_isAble():
            '''获取可点击的按钮位置'''
            import requests
            headers = {
                'Authorization': onionsToken,
                'ShadowAuthorization': shadowToken,
                'Origin': 'http://10.8.8.8'
            }
            r = requests.get(
                url='https://api-wx-test.yangcong345.com/primary_account/shadow/userCourse?phone=18618262234',
                headers=headers)
            result = r.json().get('result')
            for r in result:
                if r.get('isAble') is True:
                    r.get('className')
                    t = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody').text
                    t = str(t).split('\n')
                    for i in t:
                        if r.get('className') in i:
                            l = t.index(i)
            return l

        button_index = get_isAble()
        # 点击给葱钻
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[{}]/td[5]/button'.format(
                button_index)).click()
        # 增加
        driver.find_element_by_xpath('//*[@id="type"]/label[1]/span[1]/input').click()
        # //*[@id="type"]/label[2]/span[1]/input
        # 葱钻数
        driver.find_element_by_xpath('//*[@id="mount"]').send_keys('0')
        # 备注
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="extra"]').send_keys('自动化测试' + t)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        def check_increase_istrue(local_pro_status):
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]').text
            if int(pro_status) - int(local_pro_status) == 10:
                return True
            else:
                return False

        assert_equal(check_increase_istrue(local_pro_status), True, "校验是否添加葱钻成功")

    def test_cat_back(self):
        ''' 减少葱钻'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/dimand/manage")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索18618262234手机号
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div/div/span/span/input').send_keys(
            '18618262234')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[2]/div/div/div/span/span/input').send_keys(
            Keys.ENTER)
        local_pro_status = driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]').text

        def get_isAble():
            '''获取可点击的按钮位置'''
            import requests
            headers = {
                'Authorization': onionsToken,
                'ShadowAuthorization': shadowToken,
                'Origin': 'http://10.8.8.8'
            }
            r = requests.get(
                url='https://api-wx-test.yangcong345.com/primary_account/shadow/userCourse?phone=18618262234',
                headers=headers)
            result = r.json().get('result')
            for r in result:
                if r.get('isAble') is True:
                    r.get('className')
                    t = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody').text
                    t = str(t).split('\n')
                    for i in t:
                        if r.get('className') in i:
                            l = t.index(i)
            return l

        button_index = get_isAble()

        # 点击给葱钻
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[{}]/td[5]/button'.format(
                button_index)).click()
        # 减少
        driver.find_element_by_xpath('//*[@id="type"]/label[2]/span[1]/input').click()
        # //*[@id="type"]/label[2]/span[1]/input
        # 葱钻数
        driver.find_element_by_xpath('//*[@id="mount"]').send_keys('0')
        # 备注
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="extra"]').send_keys('自动化测试' + t)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        def check_increase_istrue(local_pro_status):
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]').text
            if int(pro_status) - int(local_pro_status) == -10:
                return True
            else:
                return False

        assert_equal(check_increase_istrue(local_pro_status), True, "校验是否添加葱钻成功")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
