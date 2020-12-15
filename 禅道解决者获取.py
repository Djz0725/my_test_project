"""
@file: 禅道解决者获取
@author: DJZ
@time: 2020/12/15
@desc
"""

import requests
import json

account = "djz"
password = "q19980603.123"

global account_cache
account_cache = ""

def login():
    user = {'account': account, 'password': password}
    s = requests.Session()
    s.post('http://sz1card1.5upm.com/user-login.html', data=user)

    return s

def get_user_account():
    ss = login()

    global account_cache
    if account_cache == "":
        account_cache = ss.get("http://sz1card1.5upm.com/company-browse-0-bydept-id-110-200-1.json").json()
        users = json.loads(account_cache["data"])["users"]
    else:
        users = json.loads(account_cache["data"])["users"]

    result = ""
    for user in users:
        if user["realname"] == "sss":
            result = user["account"]
            return result

    if result == "":
        account_cache = ss.get("http://sz1card1.5upm.com/company-browse-0-bydept-id-110-200-1.json").json()
        users = json.loads(account_cache["data"])["users"]

        for user in reversed(users):
            if user["realname"] == "欧阳文":
                result = user["account"]
                return result

if __name__ == "__main__":
    account = get_user_account()

    print(account)