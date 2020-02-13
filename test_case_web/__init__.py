# -*- encoding=utf8 -*-
__author__ = "yangcong"

from airtest.core.api import *

from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from airtest.cli.parser import cli_setup
import unittest
from config import chromedrive_path, log_path, verification_code, admin_web_images, onionsToken, shadowToken
from tools.admin_login import admin_login
from tools.web_scroll import web_scroll
import os
from tools.general_assertion import General_Assertion_Admin
import datetime
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
