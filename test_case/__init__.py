# -*- encoding=utf8 -*-
__author__ = "yangcong"

from airtest.core.api import *

from airtest_selenium.proxy import WebChrome
from airtest.cli.parser import cli_setup
import unittest
from config import chromedrive_path, log_path

if not cli_setup():
    auto_setup(__file__, logdir=log_path)
