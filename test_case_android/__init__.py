from airtest.core.api import *
from airtest.cli.parser import cli_setup
from config import android_log_path,android_address
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from tools.onion_android import Onion_App
from tools.general_assertion import General_Assertion_Onion_App