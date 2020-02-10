# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/10 2:37 下午
# software: PyCharm
import os

from flask import Flask, render_template
from tools.html_outfile import son_logs, dad_logs

app = Flask(__name__, template_folder='.')


@app.route('/unittest_report')
def unittest_report():
    return render_template('./report.html')


@app.route('/export_web_report')
def export_wen_report():
    son_logs()
    dad_logs()
    # 未完成
    # 增加闪屏后跳转至目录
    return '<h1>生成airtest测试报告成功</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
