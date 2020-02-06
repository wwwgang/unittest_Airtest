# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/2/5 3:12 下午
# software: PyCharm
import requests
from config import Authorization, ShadowAuthorization
import logging


def create_account(username, password):
    '''后台创建账号'''
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Authorization': Authorization,
        'ShadowAuthorization': ShadowAuthorization,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://backstage-test.yc345.tv:8081',
    }
    user = []
    if type(username) is str:
        user.append(username)
    elif type(username) is list:
        for u in username:
            user.append(u)
    json = {
        "userList": user,
        "role": "student",
        "password": password
    }
    url = 'http://backstage-test.yc345.tv:3003/api/user'
    r = requests.post(url=url, json=json, headers=headers)
    r_json = r.json()
    successCount = r_json.get('successCount')
    if successCount:
        logging.warning('注册成功,账号:'+str(user)+',密码:'+str(password)+',返回结果:'+str(r_json))
        return True
    else:
        raise Exception(r_json)
