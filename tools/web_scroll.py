import time


# 若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
# js = "var q=document.getElementById('id').scrollTop=100000"
# driver.execute_script(js)
# time.sleep(3)


class web_scroll():
    '''控制浏览器上下滚动'''
    def __init__(self, driver):
        self.driver = driver

    def scroll_top(self):
        # 将滚动条移动到页面的顶部
        driver = self.driver
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(3)

    def scroll_bottom(self):
        # 将滚动条移动到页面的底部
        driver = self.driver
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        time.sleep(3)
