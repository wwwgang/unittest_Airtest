# -*- encoding=utf8 -*-
__author__ = "yangcong"

from test_case_web import *


class WSTestcase(unittest.TestCase):
    '''招生计划'''

    @classmethod
    def setUpClass(cls) -> None:
        if not cli_setup():
            auto_setup(__file__, logdir=log_path + '/' + os.path.basename(__file__))

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_add_plan(self):
        ''' 添加招生计划'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        admin_login(driver).login()
        driver.get("http://10.8.8.8/admin5/configure/admission")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div/div/div/div[2]/span", "xpath",
                            "校验进入招生计划管理")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th",
            "xpath", "校验表单“序号”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[2]/span/div/span",
            "xpath", "校验表单“招生计划名称”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[3]/span/div/span",
            "xpath", "校验表单“班型”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[4]/span/div/span",
            "xpath", "校验表单“招生开始时间”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[5]/span/div/span",
            "xpath", "校验表单“招生结束时间”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[6]/span/div/span",
            "xpath", "校验表单“是否付费”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[7]/span/div/span",
            "xpath", "校验表单“当前状态”")
        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/thead/tr/th[8]/span/div/span",
            "xpath", "校验表单“操作")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button", "xpath",
                            "校验“新建”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li/a",
                            "xpath", "校验“分页-上一页”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[2]/a",
                            "xpath", "校验“分页第一页”")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[3]/a",
                            "xpath", "校验“分页-下一页”")
        # 点击新建按钮
        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/button").click()
        # 班级类型选择免费版
        driver.find_element_by_xpath("//*[@id=\"classType\"]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[7]").click()
        # 是否付费选择否
        driver.find_element_by_xpath("//input[@value='1']").click()
        # 输入招生计划名称
        t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("//input[@placeholder='请输入有效的招生计划名称']").send_keys(
            "自动化测试" + t1)
        # 输入招生开始时间
        driver.find_element_by_xpath("//*[@id=\"startTime\"]/div/input").click()
        t2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div/input").send_keys(
            t2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a[3]").click()
        # 输入招生结束时间
        driver.find_element_by_xpath("//*[@id=\"endTime\"]/div/input").click()
        t3 = datetime.datetime.fromtimestamp(time.time() + 86400).strftime("%Y-%m-%d %H:%M:%S")
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[1]/div/input").send_keys(
            t3)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a[3]").click()
        # 选择平均分班
        driver.find_element_by_xpath("//*[@id=\"classRules\"]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/ul/li[2]").click()
        # 关联招生主页1
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span").click()
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        # 保存
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[8]/div/div/span/button[1]").click()

        def check_save_istrue(driver, t1, t2, t3):
            '''判断新建招生计划三个时间是否存在页面中'''
            pro_status = driver.page_source
            if t1 in pro_status and t2 in pro_status and t3 in pro_status:
                return True
            else:
                return False

        # 断言数据添加是否成功
        assert_equal(check_save_istrue(driver, t1, t2, t3), True, '通用断言：验证添加数据是否成功')

    def test_view_plan(self):
        '''查看招生计划'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin5/configure/admission")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        driver.assert_exist(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/button",
            "xpath", "校验是否存在查看按钮")
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/button").click()

        def check_is_not_null(driver):
            # 招生计划标题
            a = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/h2[1]").text.split("：", 1)[1]
            # 招生计划ID
            b = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div[1]/span").text.split("：",
                                                                                                                   1)[1]
            # 最后修改时间
            c = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div[2]/span").text.split("：",
                                                                                                                   1)[1]
            # 最后修改人
            d = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[1]/div[3]/span").text.split("：",
                                                                                                                   1)[1]
            # 状态
            e = driver.find_element_by_xpath(
                "/html/body/div/div/section/section/main/div/div[2]/div/div/div/div[2]/div[1]/span/span").text.split(
                "：", 1)[0]
            # 班级类型
            f = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div[2]/span").text.split("：",
                                                                                                                   1)[1]
            # 是否付费
            g = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div[3]/span").text.split("：",
                                                                                                                   1)[1]
            # 招生开始时间
            h = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[3]/div[1]/span").text.split("：",
                                                                                                                   1)[1]
            # 招生结束时间
            i = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[3]/div[2]/span").text.split("：",
                                                                                                                   1)[1]
            # 分班逻辑
            j = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[4]/div[1]/span").text.split("：",
                                                                                                                   1)[1]
            # 介绍页详情ID
            k = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div[4]/div[2]/span").text.split("：",
                                                                                                                   1)[1]
            # 招生链接
            l = driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/p[1]").text.split("：", 1)[1]
            assert_not_equal(a, '', '招生计划标题不为空')
            assert_not_equal(b, '', '招生计划ID不为空')
            assert_not_equal(c, '', '最后修改时间不为空')
            assert_not_equal(d, '', '最后修改人不为空')
            assert_not_equal(e, '', '状态不为空')
            assert_not_equal(f, '', '班级类型不为空')
            assert_not_equal(g, '', '是否付费不为空')
            assert_not_equal(h, '', '招生开始时间不为空')
            assert_not_equal(i, '', '招生结束时间不为空')
            assert_not_equal(j, '', '分班逻辑不为空')
            assert_not_equal(k, '', '介绍页详情ID不为空')
            assert_not_equal(l, '', '招生链接不为空')

        check_is_not_null(driver)

    def test_add_plan_list(self):
        '''删除添加招生细则'''
        driver = self.driver
        driver.maximize_window()
        # admin登录
        login = admin_login(driver)
        login.login()
        driver.get("http://10.8.8.8/admin5/configure/admission")
        # 通用断言
        ass = general_assertion_admin(driver)
        ass.check_title_admin()  # '通用断言：验证标题是否存在"洋葱数学-小学"'
        ass.check_url_admin()  # '通用断言：验证域名是否存在"http://10.8.8.8"'
        ass.check_page_source_admin()  # '通用断言：验证页面中是否存在"测试环境"'
        ass.check_user_info_admin()  # "通用断言：验证页面右上角是否存在'用户头像'" 和 "通用断言：验证页面右上角是否存在'登录用户名'"
        ass.check_onion_info_admin()  # "通用断言：验证页面左上角是否存在'洋葱logo图'" 和 '通用断言：验证页面左上角是否存在"洋葱数学-小学"'

        # 切换分页展示为100
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[5]/div[1]/div/div').click()
        driver.find_element_by_xpath(
            '/html/body/div/div/section/section/main/div/div[2]/div/div/div/div/div/div/ul/li[5]/div[3]/div/div/div/ul/li[4]').click()

        for i in range(1, 101):
            # 序号
            a = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[{}]/td[3]'.format(
                    i)).text
            # 是否付费
            b = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[{}]/td[6]'.format(
                    i)).text
            # 招生计划名称
            c = driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[{}]/td[2]'.format(
                    i)).text
            # if a == '春季班' and b == '付费' and '自动化测试' in c:
            if '自动化测试' in c:
                j = i
                break

        # 点击春季班&&付费的查看
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[{}]/td[8]/button".format(
                j)).click()

        # 删除所有细则
        # for i in range(1,21):
        #     try:
        #         driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[6]/div/div/div/div/div/table/tbody/tr/td[9]/button[2]').click()
        #         driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        #     except Exception as e:
        #         break

        def get_plan_list_count():
            '''获取当前细则条数'''
            for i in range(1, 21):
                try:
                    a = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[6]/div/div/div/div/div/table/tbody/tr[{}]/td[1]'.format(
                            i)).text
                except Exception as e:
                    count = i
                    break
            return count

        # 获取当前细则条数：
        num1 = get_plan_list_count()
        # 点击新建
        driver.find_element_by_xpath("/html/body/div/div/section/section/main/div/div[2]/div/div/div/button").click()
        # 点击招生年级和版本
        driver.find_element_by_xpath("//*[@id=\"gradePublisherId\"]/div/div").click()
        # 选择三年级人教版
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[1]").click()
        # 点击关联课程
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[2]/div[2]/div/span/div/button").click()
        # 选择课程列表中第一条数据
        driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span").click()
        # 点击保存
        driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        # 添加班级
        driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[3]/div[2]/div/span/div/button").click()
        # 关联班级第一个
        driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input").click()
        # 关联班级第二个
        # driver.find_element_by_xpath(
        #     "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/span/label/span/input").click()
        # 点击确定
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        # 删除一个关联班级
        # driver.find_element_by_xpath(
        #     "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[7]/button").click()
        # 因测试环境字样挡住元素，将屏幕向上滚动
        web_scroll(driver).scroll_top()
        try:
            # 关联商品
            driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div[2]/div/span/div/button").click()
            # 选择第一个商品
            driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span/label/span/input').click()
            # 点击确定
            driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/div[3]/button[2]").click()
        except:
            pass
        # 点击保存
        try:
            driver.find_element_by_xpath(
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div[5]/div/div/span/button[1]').click()
        except:
            driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div/div/form/div[6]/div/div/span/button[1]").click()

        # 获取当前细则条数
        num2 = get_plan_list_count()

        def check_plan_list_num():
            if int(num1) + 1 == int(num2):
                return True
            else:
                return False

        assert_equal(check_plan_list_num(), True, "校验是否添加细则成功")

        # 因测试环境字样挡住元素，将屏幕向上滚动
        web_scroll(driver).scroll_top()

        # 删除第一条细则
        driver.find_element_by_xpath('/html/body/div/div/section/section/main/div/div[2]/div/div/div/div[6]/div/div/div/div/div/table/tbody/tr/td[9]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]').click()

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
