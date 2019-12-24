import unittest
from config import case_path,report_path
from HtmlTestRunner import HTMLTestRunner
from html_outfile import html_outfile

testunit = unittest.TestSuite()

discover = unittest.defaultTestLoader.discover(case_path, pattern='air*.py', top_level_dir=None)
for test_suite in discover:
    for test_case in test_suite:
        testunit.addTests(test_case)


with open(report_path,'w') as f:
    runner=HTMLTestRunner(stream=f)
    result= runner.run(testunit)

html_outfile()

