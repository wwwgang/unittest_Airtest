# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''微信管理'''

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_wechat(self):
        ''' 添加微信号'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/wechatManage/wechat")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 点击新增微信
        driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/button').click()
        # 输入微信账号
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/input').send_keys(
            '自动化测试' + t)
        # 输入微信昵称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input').send_keys(
            '自动化测试' + t)
        # 输入微信二维码
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/span/div[1]/span/input').send_keys(
            admin_web_images + '/wechat_qrcode.jpeg')
        # 点击保存
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        # 搜索添加后的数据
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div/span/span/input').send_keys(
            '自动化测试' + t)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div/span/span/input').send_keys(
            Keys.ENTER)

        def check_add_wechat_istrue():
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody').text
            if '自动化测试' + t in pro_status:
                return True
            else:
                return False

        assert_equal(check_add_wechat_istrue(), True, "校验添加微信是否成功")

    def test_del_wechat(self):
        ''' 失效微信号'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/wechatManage/wechat")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索添加后的数据
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div/span/span/input').send_keys(
            '自动化测试')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div/span/span/input').send_keys(
            Keys.ENTER)
        # 获取第一个微信号
        a = driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
        # 失效第一个微信号
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()

        def check_del_wechat_istrue():
            # 获取表单中所有text,切割，遍历，校验是否为已失效
            b = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/table/tbody').text
            c = str(b).split('\n')
            for i in c:
                if a in i:
                    if '已失效' in i:
                        return True
                    else:
                        return False
                else:
                    continue

        assert_equal(check_del_wechat_istrue(), True, "校验是否删除成功")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
