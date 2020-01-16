# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''客服消息'''
    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_create_reply(self):
        ''' 创建回复'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/configure/customer-message")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        driver.assert_exist("//div[@aria-selected='true']", "xpath", "验证是否存在'关键词回复'")
        driver.assert_exist("//button[@type='button']", "xpath", "验证是否'创建回复'")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/thead/tr/th/span/div/span",
            "xpath", "验证表单中是否分存在'规则名称'")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/thead/tr/th/span/div/span",
            "xpath", "验证表单中是否存在'关键字")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/thead/tr/th[3]/span/div/span",
            "xpath", "验证表单中是否存在'回复内容'")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span",
            "xpath", "验证表单中是否存在'更新时间'")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span",
            "xpath", "验证表单中是否存在'应用小程序'")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/div/table/tbody/tr/td[6]/span/a",
            "xpath", "验证表单中第一行是否有'编辑'操作按钮")
        # 点击创建回复
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/button").click()
        t1 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        # 输入规则名称
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试' + t1)
        t2 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        # 输入关键字
        driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('自动化测试' + t2)
        # 文字
        driver.find_element_by_xpath('//*[@id="addMsg"]/label[1]').click()
        # # 图片
        # driver.find_element_by_xpath('//*[@id="addMsg"]/label[2]').click()
        # # 超链接
        # driver.find_element_by_xpath('//*[@id="addMsg"]/label[3]').click()
        # 输入回复内容
        t3 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="textMsg"]').send_keys('自动化测试' + t3)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        # 输入内容详情
        # 选择应用范围
        driver.find_element_by_xpath('//*[@id="accounts"]/label[1]/span[1]/input').click()
        # 点击保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/form/div[6]/div/div/span/button').click()

        def check_name(driver):
            pro_status = driver.page_source
            boole_status = False
            l = [t1, t2]
            for i in l:
                if i in pro_status:
                    continue
                else:
                    break
            else:
                boole_status = True
            return boole_status

        assert_equal(check_name(driver), True, "校验规则中是否含有创建成功的规则名称")

    def test_search_customer_news(self):
        ''' 查找自动化测试'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/configure/customer-message")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 查找"自动化测试"
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            "自动化测试")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            Keys.ENTER)
        driver.assert_exist(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span/a[1]',
            'xpath', "验证表单中是否有编辑按钮")

    def test_change_customer_news(self):
        '''更改自动化测试'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/configure/customer-message")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 查找"自动化测试"
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            "自动化测试")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            Keys.ENTER)
        # 点击第一条编辑
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span/a[1]').click()
        # 修改规则名称
        t1 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="name"]').clear()
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试改' + t1)
        # 修改关键词
        t2 = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="keyword"]').clear()
        driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('自动化测试改' + t2)
        # 点击保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/form/div[6]/div/div/span/button').click()

        def check_name(driver):
            pro_status = driver.page_source
            boole_status = False
            l = [t1, t2]
            for i in l:
                if i in pro_status:
                    continue
                else:
                    break
            else:
                boole_status = True
            return boole_status

        assert_equal(check_name(driver), True, "校验规则中是否含有创建成功的规则名称")

    def test_del_customer_news(self):
        '''删除自动化测试'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/configure/customer-message")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 查找"自动化测试"
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            "自动化测试")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span/input').send_keys(
            Keys.ENTER)
        # 获取即将要删除的规则名称
        news_name = driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[1]').text
        # 点击删除
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span/a[2]').click()
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        def check_del_isture():
            if not news_name in driver.page_source:
                return True
            else:
                return False

        assert_equal(check_del_isture(), True, "校验是否删除成功")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
