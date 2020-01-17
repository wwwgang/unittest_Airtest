# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''班级管理'''

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_class(self):
        ''' 创建班级'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/class/class-list")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 点击创建班级
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[1]/button').click()

        # 输入班级名称
        t = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(t + '-自动化测试-王刚')
        # 输入备注
        driver.find_element_by_xpath('//*[@id="description"]').send_keys('自动化测试' + t)
        # 关联课程
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/div[2]/div/span/a').click()
        # 点击课程类型名称
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div').click()
        # 选择人教版
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
        # 点击教材版本
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div').click()
        # 选择四年级上
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[7]').click()
        # 点击搜索按钮
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div[4]/button').click()
        # 选择第一个课程
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/label/span[1]/input').click()
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        # 点击开课年级
        driver.find_element_by_xpath('//*[@id="grade"]/div/div').click()
        # 选择四年级
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[4]').click()
        # 点击班级类型
        driver.find_element_by_xpath('//*[@id="type"]/div/div').click()
        # 选择免费版
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[9]').click()
        # 输入班级容量
        driver.find_element_by_xpath('//*[@id="studentCount"]').clear()
        driver.find_element_by_xpath('//*[@id="studentCount"]').send_keys('200')
        # *截止招生时间

        driver.find_element_by_xpath('//*[@id="stopTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[1]/div/input').send_keys(t)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *开课时间
        driver.find_element_by_xpath('//*[@id="startTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div[1]/div/input').send_keys(t)
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *完课时间
        driver.find_element_by_xpath('//*[@id="endTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[1]/div/input').send_keys(t)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *过期时间
        driver.find_element_by_xpath('//*[@id="invalidTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[1]/div/input').send_keys(t)
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *是否邮寄
        driver.find_element_by_xpath('//*[@id="isPost"]/label[1]/span[1]/input').click()
        # 老师微信
        driver.find_element_by_xpath('//*[@id="wxManagmentId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul/li[1]').click()
        # 点击保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[13]/div/div/span/button').click()

        # 搜索以创建班级
        driver.find_element_by_xpath('//*[@id="name"]').send_keys(t + '-自动化测试-王刚')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/button[1]').click()

        def check_add_class_istrue():
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody').text
            if (t + '-自动化测试-王刚') in pro_status:
                return True
            else:
                return False

        assert_equal(check_add_class_istrue(), True, "校验添加班级是否成功")

    def test_add_user(self):
        ''' 添加用户'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/class/class-list")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索以创建班级
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试-王刚')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/button[1]').click()
        # 点击第一条班级查看
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/a[1]').click()
        # 切换至新标签
        driver.switch_to_new_tab()
        # 点击新增用户
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/button[1]').click()
        # 点击选择用户渠道
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/span/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[contains(text(),\'小学内部-手动添加\')]').click()
        # 手动输入手机号码
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/span/div/label[1]/span[1]/input').click()
        # 输入用户手机号
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/span/div/div/div/ul/li/div/input').send_keys(
            '18618262234')
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/span/div/div/div/ul/li/div/input').send_keys(
            Keys.ENTER)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/button').click()

        def check_add_user_istrue():
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody').text
            if '18618262234' in pro_status:
                return True
            else:
                return False

        assert_equal(check_add_user_istrue(), True, "校验添加用户是否成功")

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
