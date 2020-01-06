# -*- encoding=utf8 -*-
__author__ = "yangcong"

import shutil, os
from config import rm_log, rm_logs, rm_reports_txt
from tools.make_file import make_file


def del_file():
    # 删除log&*.log&reports&report.txt
    try:
        shutil.rmtree(rm_log)
    except Exception as e:
        print(e)
    try:
        for log in rm_logs:
            try:
                shutil.rmtree(log)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    try:
        os.remove(rm_reports_txt)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    del_file()
    make_file()