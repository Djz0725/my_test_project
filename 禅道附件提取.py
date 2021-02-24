"""
@file: demo
@author: DJZ
@time: 2021/01/25
@desc
"""

import requests
import json

account = "djz"
password = "q19980603.123"

attachment = []
attachments_name = []

def login():
    user = {'account': account, 'password': password}
    s = requests.Session()
    s.post('http://sz1card1.5upm.com/user-login.html', data=user)

    return s

def get_attach():
    ss = login()
    result = ss.get("http://sz1card1.5upm.com/task-view-25788.json").json()
    data = json.loads(result["data"]).get("task").get("files")
    print(data)
    for i in data.keys():
        print(i)
        attach = "http://sz1card1.5upm.com" + data.get(f"{i}").get("webPath")
        attachment_name = data.get(f"{i}").get("title")
        attachment.append(attach)
        attachments_name.append(attachment_name)

    return attachment,attachments_name

if __name__ == "__main__":
    attachments = get_attach()
    for i in reversed(attachments):
        print(i)
    print(attachments)
    print(attachments_name)