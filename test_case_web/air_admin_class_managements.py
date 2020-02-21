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
        self.driver = WebChrome(chromedrive_path, chrome_options=chrome_options)
        self.driver.set_window_size(2560, 1440)
        # self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_class(self):
        ''' 创建班级'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin10/class/class-list")
        # 通用断言
        ass = General_Assertion_Admin(driver)
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
        # *截止招生时间2332800
        t1 = datetime.datetime.fromtimestamp(time.time() + 2332800).strftime("%Y-%m-%d %H:%M:%S")

        driver.find_element_by_xpath('//*[@id="stopTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[1]/div/input').send_keys(t1)
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *开课时间2419200
        t2 = datetime.datetime.fromtimestamp(time.time() + 2419200).strftime("%Y-%m-%d %H:%M:%S")

        driver.find_element_by_xpath('//*[@id="startTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div[1]/div/input').send_keys(t2)
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *完课时间2505600
        t3 = datetime.datetime.fromtimestamp(time.time() + 2505600).strftime("%Y-%m-%d %H:%M:%S")

        driver.find_element_by_xpath('//*[@id="endTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[1]/div/input').send_keys(t3)
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *过期时间2592000
        t4 = datetime.datetime.fromtimestamp(time.time() + 2592000).strftime("%Y-%m-%d %H:%M:%S")

        driver.find_element_by_xpath('//*[@id="invalidTime"]/div/input').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[1]/div/input').send_keys(t4)
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[2]/div[3]/span/a[3]').click()
        # *是否邮寄
        driver.find_element_by_xpath('//*[@id="isPost"]/label[1]/span[1]/input').click()
        # 老师微信
        driver.find_element_by_xpath('//*[@id="wxManagmentId"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[11]/div/div/div/ul/li[1]').click()
        # 点击保存
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[14]/div/div/span/button').click()

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
        driver.get("http://10.8.8.8/admin10/class/class-list")
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索已创建班级
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
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/span/div/label[1]/span[1]/input').click()
        # 输入用户手机号
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/div/div/ul/li/div/input').send_keys(
            '18618262234')
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/div/div/div/ul/li/div/input').send_keys(
            Keys.ENTER)
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/button').click()

        def check_add_user_istrue():
            pro_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody').text
            log('pro_status:' + str(pro_status))
            print('pro_status:' + str(pro_status))
            if '18618262234' in pro_status:
                return True
            else:
                return False

        assert_equal(check_add_user_istrue(), True, "校验添加用户是否成功")

    def test_del_class(self):
        ''' 失效班级'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin7/class/class-list")
        # 通用断言
        ass = General_Assertion_Admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 搜索已创建班级
        driver.find_element_by_xpath('//*[@id="name"]').send_keys('自动化测试-王刚')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/button[1]').click()

        # 获取未失效班级
        def get_class_text():
            class_list = []
            t = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody').text
            t = t.split('\n')
            class_temp = []

            flag = 0
            for i in t:
                class_temp.append(i)
                if flag == 5:
                    class_list.append(class_temp.copy())
                    class_temp.clear()
                    flag = 0
                    continue
                flag += 1

            for i in class_list:
                if '有效' in i:
                    i.append(int(class_list.index(i)) + 1)
                    return i

        class_list = get_class_text()
        # 点击失效
        class_num1 = class_list[6]
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[{}]/td/a[2]'.format(
                class_num1)).click()
        # 失效原因
        driver.find_element_by_xpath('//*[@id="classInvalidReason"]/div/div').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[3]').click()
        # 点击确定
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()

        def check_del_class(class_list):
            '''校验失效班级是否成功'''
            class_info_list = str(class_list[1]).split(' ')
            class_name = str(class_info_list[0]) + ' ' + str(class_info_list[1])
            driver.find_element_by_xpath('//*[@id="name"]').clear()
            driver.find_element_by_xpath('//*[@id="name"]').send_keys(class_name)
            driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/button[1]').click()
            class_status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody/tr/td[9]/div/span[2]').text
            if '失效' in class_status:
                return True
            else:
                return False

        assert_equal(check_del_class(class_list), True, '校验是否失效成功')

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
