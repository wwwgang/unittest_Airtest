# -*- encoding=utf8 -*-
__author__ = "yangcong"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from airtest.cli.parser import cli_setup
import unittest
from config import chromedrive_path, log_path

if not cli_setup():
    # auto_setup(__file__, logdir="/Users/yangcong/Desktop/log", devices=[
    #         "Android:///",
    # ])
    auto_setup(__file__, logdir=log_path)


class WSTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver = WebChrome(chromedrive_path)
        self.driver.implicitly_wait(20)

    def test_1(self):
        driver = self.driver
        driver.get("https://yangcong345.com/#/studentPage")
        driver.find_element_by_xpath("//span[@title='登录']").click()
        driver.assert_exist("//*[@id=\"normal\"]/button", "xpath", "进入登录页")

    def test_2(self):
        raise '1111'
        print('test2')

    def tearDown(self) -> None:
        self.driver.close()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


auto_setup(__file__)

# generate html report
# from airtest.report.report import simple_report
#
# print(log_path)
# simple_report(__file__, logpath=log_path,logfile='log.txt',output='log.html')
