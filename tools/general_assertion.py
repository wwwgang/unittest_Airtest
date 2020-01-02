from airtest.core.api import *


class general_assertion_admin():
    def __init__(self, driver):
        self.driver = driver

    def check_title_admin(self):
        driver = self.driver

        def check_title_admin_d(driver):
            pro_status = driver.title
            status = '洋葱数学-小学'
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_title_admin_d(driver), True, '通用断言：验证标题是否存在"洋葱数学-小学"')
        return driver

    def check_url_admin(self):
        drive = self.driver

        def check_url_admin_d(driver):
            pro_status = driver.current_url
            status = 'http://10.8.8.8'
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_url_admin_d(drive), True, '通用断言：验证域名是否存在"http://10.8.8.8"')
        return drive

    def check_page_source_admin(self):
        driver = self.driver

        def check_page_source_admin_d(driver):
            pro_status = driver.page_source
            status = '测试环境'
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_page_source_admin_d(driver), True, '通用断言：验证页面中是否存在"测试环境"')
        return driver

    def check_user_info_admin(self):
        driver = self.driver
        driver.assert_exist(
            "//img[@src='https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png']", "xpath",
            "通用断言：验证页面右上角是否存在'用户头像'")
        driver.assert_exist("//*[@id=\"root\"]/div/section/section/header/div/div/span/span[2]", "xpath",
                            "通用断言：验证页面右上角是否存在'登录用户名'")

        return driver

    def check_onion_info_admin(self):
        driver = self.driver
        driver.assert_exist("//img[@src='/admin10/static/logo.b9b1dd57.png']", "xpath", "通用断言：验证页面左上角是否存在'洋葱logo图'")

        def check_onion_info_admin(driver):
            pro_status = driver.find_element_by_xpath("//*[@id=\"logo\"]/a/h1").text
            status = '洋葱数学-小学'
            if status in pro_status:
                return True
            else:
                return False

        driver.find_element_by_xpath("//*[@id=\"root\"]/div/section/section/header/div/span").click()
        assert_equal(check_onion_info_admin(driver), True, '通用断言：验证页面左上角是否存在"洋葱数学-小学"')
        return driver
