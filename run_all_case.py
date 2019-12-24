import unittest
from config import case_path, report_path, rm_log, rm_logs
from HtmlTestRunner import HTMLTestRunner
from html_outfile import html_outfile
import shutil

# 删除log和*.log文件夹
try:
    shutil.rmtree(rm_log)
except Exception as e:
    print(e)
print(rm_logs)
try:
    for log in rm_logs:
        shutil.rmtree(log)
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
    runner = HTMLTestRunner(stream=f)
    result = runner.run(testunit)

# 输出test_case报告
html_outfile()
