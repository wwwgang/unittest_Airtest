# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/10 6:09 下午
# software: PyCharm

import schedule
from tools.dingTalk import send_dingTalk_msg


def run_web_case():
    # -*- encoding=utf8 -*-
    __author__ = "yangcong"

    import unittest
    from config import case_path, report_path

    from tools import HTMLTestRunner_PY3
    from tools.del_file import del_file
    from tools.make_file import make_file

    # 删除log&*.log&report.html
    del_file()
    # 创建log文件夹
    make_file()

    # 创建存储test_case容器
    testunit = unittest.TestSuite()

    # 将test_case添加至容器
    discover = unittest.defaultTestLoader.discover(case_path, pattern='air*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)

    # 执行unittest任务输出report.html
    with open(report_path, 'w') as f:
        # 优化版报告
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title='自动化测试报告', description='自动化测试报告')
        result = runner.run(testunit)

    send_dingTalk_msg()


if __name__ == '__main__':
    schedule.every(10).minutes.do(run_web_case())
