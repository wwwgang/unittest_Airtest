# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/10 6:09 下午
# software: PyCharm

import time, sched
from tools.dingTalk import send_dingTalk_msg
from run_all_web_case import run_web_case

s = sched.scheduler(time.time, time.sleep)


def task():
    run_web_case()
    send_dingTalk_msg()


def perform(inc):
    s.enter(inc, 1, perform, (inc,))
    task()


def main(inc=60*60*2):
    s.enter(0, 0, perform, (inc,))
    s.run()


if __name__ == '__main__':
    main()
