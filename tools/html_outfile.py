import os
import glob
import re
import shutil
from config import logs_path, cases_path, out_files, airtest_result, case_path, log_path, android_cases_path, \
    android_case_path,ios_cases_path,ios_case_path


def html_outfile(py_path, log_root_path, out_file):
    os.system(
        'airtest report {} --log_root {} --outfile {} --lang zh --plugin airtest_selenium.report poco.utils.airtest.report --export .'.format(
            py_path, log_root_path, out_file))


def son_logs():
    # 查分报告输出
    for c in cases_path:
        for l in logs_path:
            try:
                if re.search('air(.*?).py', l).group() == re.search('air(.*?).py', c).group():
                    html_outfile(c, l, out_files)
            except Exception as e:
                print(e)
                continue
            continue


def dad_logs():
    # 拆报告输出
    jpgs = []
    file = open(airtest_result + '/log.txt', 'a')
    for l in logs_path:
        log = glob.glob(l + '/' + '*.txt')
        with open(log.pop(), 'r') as f:
            file.write(f.read())

        for j in glob.glob(l + '/*.jpg'):
            jpgs.append(j)
    file.close()
    for j in jpgs:
        try:
            shutil.copy(j, airtest_result)
        except Exception as e:
            print(e)
    html_outfile(case_path + '/__init__.py', log_path + '/__init__.py', out_files)


def android_son_logs():
    # 拆分报告输出
    for c in android_cases_path:
        for l in logs_path:
            try:
                if re.search('air(.*?).py', l).group() == re.search('air(.*?).py', c).group():
                    html_outfile(c, l, out_files)
            except Exception as e:
                print(e)
                continue
            continue


def android_dad_logs():
    # 总报告输出
    jpgs = []
    file = open(airtest_result + '/log.txt', 'a')
    for l in logs_path:
        log = glob.glob(l + '/' + '*.txt')
        with open(log.pop(), 'r') as f:
            file.write(f.read())

        for j in glob.glob(l + '/*.jpg'):
            jpgs.append(j)
    file.close()
    for j in jpgs:
        try:
            shutil.copy(j, airtest_result)
        except Exception as e:
            print(e)
    html_outfile(android_case_path + '/__init__.py', log_path + '/__init__.py', out_files)


def ios_son_logs():
    # 拆分报告输出
    for c in ios_cases_path:
        for l in logs_path:
            try:
                if re.search('air(.*?).py', l).group() == re.search('air(.*?).py', c).group():
                    html_outfile(c, l, out_files)
            except Exception as e:
                print(e)
                continue
            continue


def ios_dad_logs():
    # 总报告输出
    jpgs = []
    file = open(airtest_result + '/log.txt', 'a')
    for l in logs_path:
        log = glob.glob(l + '/' + '*.txt')
        with open(log.pop(), 'r') as f:
            file.write(f.read())

        for j in glob.glob(l + '/*.jpg'):
            jpgs.append(j)
    file.close()
    for j in jpgs:
        try:
            shutil.copy(j, airtest_result)
        except Exception as e:
            print(e)
    html_outfile(ios_case_path + '/__init__.py', log_path + '/__init__.py', out_files)
