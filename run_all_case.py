# -*- encoding=utf8 -*-
__author__ = "yangcong"

import unittest
from config import case_path, report_path, rm_log, rm_logs, rm_reports_txt
from html_outfile import html_outfile
import shutil
from tools import HTMLTestRunner_PY3

# 删除log&*.log&reports&report.txt
try:
    shutil.rmtree(rm_log)
except Exception as e:
    print(e)
try:
    for log in rm_logs:
        shutil.rmtree(log)
except Exception as e:
    print(e)
# try:
#     shutil.rmtree(rm_reports)
# except Exception as e:
#     print(e)
try:
    shutil.rmtree(rm_reports_txt)
except Exception as e:
    print(e)

# 创建存储test_case容器
testunit = unittest.TestSuite()

# 将test_case添加至容器
discover = unittest.defaultTestLoader.discover(case_path, pattern='air*.py', top_level_dir=None)
for test_suite in discover:
    for test_case in test_suite:
        testunit.addTests(test_case)

# 执行unittest任务输出report.txt和test_report
with open(report_path, 'w') as f:
    # 原版报告
    # runner = HTMLTestRunner(stream=f)
    # 优化版报告
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title='自动化测试报告', description='自动化测试报告')
    result = runner.run(testunit)

# 输出test_case报告
html_outfile()
