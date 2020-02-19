# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''资源管理'''

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

    def test_add_banner(self):
        '''添加banner'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/resources/banner")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 点击新建
        # sleep(1000)
        driver.find_element_by_xpath('//button[@class="ant-btn antd-pro-pages-resources-styles-customBtn ant-btn-primary"]').click()
        # banner名称
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="bannerName"]').send_keys('自动化测试' + t)
        # banner图片
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[2]/div[2]/div/span/span/div[1]/span/input').send_keys(
            admin_web_images + '/Banner@2x.png')
        # 开始时间
        driver.find_element_by_xpath('//*[@id="startTime"]/div').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t)
        driver.find_element_by_xpath('//a[@class="ant-calendar-ok-btn"]').click()
        # 结束时间
        driver.find_element_by_xpath('//*[@id="endTime"]/div').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t)
        driver.find_element_by_xpath('//a[@class="ant-calendar-ok-btn"]').click()
        # 跳转链接
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div[2]/div/span').click()
        driver.find_element_by_xpath('//*[@id="redirectUrl"]').send_keys('http://10.8.8.8/admin10')
        # 点击提交
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[6]/div/div/span/button[2]').click()

    def test_add_popup(self):
        '''添加弹窗'''
        driver = self.driver
        driver.maximize_window()  # 窗口最大化
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin10/resources/popup")  # 进入首页
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'
        # 点击新建
        driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/button').click()
        # 弹窗名称
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="bannerName"]').send_keys('自动化测试' + t)
        # 弹窗图片
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[2]/div[2]/div/span/span/div[1]/span/input').send_keys(
            admin_web_images + '/希尔瓦娜斯.jpg')
        # 开始时间
        driver.find_element_by_xpath('//*[@id="startTime"]/div').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t)
        driver.find_element_by_xpath('//a[@class="ant-calendar-ok-btn"]').click()
        # 结束时间
        driver.find_element_by_xpath('//*[@id="endTime"]/div').click()
        driver.find_element_by_xpath('//input[@class="ant-calendar-input "]').send_keys(t)
        driver.find_element_by_xpath('//a[@class="ant-calendar-ok-btn"]').click()
        # 跳转链接
        driver.find_element_by_xpath('//*[@id="redirectUrl"]').click()
        driver.find_element_by_xpath('//*[@id="redirectUrl"]').send_keys('http://10.8.8.8/admin10')
        # 弹窗场景
        driver.find_element_by_xpath('//*[@id="popScene"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()
        # 弹出次数
        driver.find_element_by_xpath('//*[@id="popFrequency"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()
        # 点击提交
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[8]/div/div/span/button[2]').click()

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
