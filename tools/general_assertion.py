from airtest.core.api import *


class general_assertion_admin():
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        driver = self.driver

        def check_title(driver):
            pro_status = driver.title
            status = '洋葱数学-小学'
            if status in pro_status:
                return True
            else:
                return False

        assert_equal(check_title(driver), True, '验证标题')
