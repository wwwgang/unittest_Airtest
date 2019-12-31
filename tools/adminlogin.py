from config import localstorage_list


class admin_login():
    '''后台登录'''

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        driver = self.driver
        driver.get("http://10.8.8.8/admin10/static/logo.b9b1dd57.png")
        for i in localstorage_list:
            driver.execute_script(
                r'''localStorage.setItem('{}','{}');'''.format(i['key'], i['value'].replace('\\', '\\\\'))
            )
        return driver
