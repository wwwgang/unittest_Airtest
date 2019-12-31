# -*- encoding=utf8 -*-
__author__ = "yangcong"

from airtest.core.api import *

from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from airtest.cli.parser import cli_setup
import unittest
from config import chromedrive_path, log_path, verification_code
from tools.adminlogin import admin_login
import os
