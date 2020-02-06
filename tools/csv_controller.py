# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/6 11:46 上午
# software: PyCharm
import csv


def get_mobile_csv(filename):
    # 获取csv中数据
    mobile = []
    with open(filename) as fp:
        content = csv.DictReader(fp)
        for i in content:
            mobile.append(
                {
                    'mobile': i.get('mobile'),
                    'status': i.get('status')
                }
            )
    # 获取可用的手机号
    mobile_temp = ''
    for i in mobile:
        if i.get('status') is '1' or i.get('status') is '':
            mobile_temp = i
            break
    if mobile_temp == '':
        raise Exception('mobile.csv中无可用手机号')
    # 更新该手机号为不可用状态
    mobile_temp.update({'status': 0})
    mobile_index = mobile.index(mobile_temp)
    mobile[mobile_index] = mobile_temp
    # 重写如到csv中
    with open(filename, 'w') as fp:
        head = ['mobile', 'status']
        writer = csv.DictWriter(fp, fieldnames=head)
        writer.writeheader()
        writer.writerows(mobile)
    # 返回一个可用手机号
    return mobile_temp.get('mobile')


if __name__ == '__main__':
    from config import mobile_path

    mobile = get_mobile_csv(mobile_path)
    print(mobile)
