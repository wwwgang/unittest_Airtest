# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/10 6:33 下午
# software: PyCharm
from tools.schedules import run_web_case
import schedule

schedule.every(10).minutes.do(run_web_case())
