# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''课程管理'''

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

    def test_add_course(self):
        '''添加课程'''
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
        # 点击创建课程
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/button').click()
        # 输入课程名称
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试' + t)
        # 年级学期选择四年级上册
        driver.find_element_by_xpath('//*[@id="semesterId"]/div').click()
        # sleep(1000)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[7]').click()
        # 教材版本选择人教版
        driver.find_element_by_xpath('//*[@id="publisherId"]/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
        # 解锁方式选择天解锁
        driver.find_element_by_xpath('//*[@id="unlockMode"]/div').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()
        # 预计上课时间增加1天
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[4]/div/div[1]/span[1]').click()
        # 支持多题型
        driver.find_element_by_xpath('//*[@id="isMultiProblems"]/label[1]/span[1]/input').click()
        # 继续添加
        # sleep(1000)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div/div/div/div/div/div/table/tbody/tr/td[9]/button[1]').click()
        # 课程内容选择
        # 选择系统课程
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()
        # 选择小学阶段
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[1]').click()
        # 选择学期
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[3]/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[7]').click()
        # 选择人教版
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div[4]/div').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/ul/li[1]').click()
        # 点击筛选
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/button').click()
        ul = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/ul')
        spans = ul.find_elements_by_xpath('//span[@class="ant-tree-checkbox"]')
        for span in spans:
            span.click()
        # 点击保存
        driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        # 点击保存
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        # 查询创建的课程
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试' + t)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[1]/div/div/div/form/div[2]/div/div/div/div/span/button[1]').click()

        def check_add_course():
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody').text
            status = '自动化测试' + t
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_add_course(), True, '校验是否添加课程成功')

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
