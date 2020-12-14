"""
@file: test
@author: DJZ
@time: 2020/11/20
@desc
"""

# import requests
# import json
#
# account = "djz"
# password = "q19980603.123"
#
# global account_cache
# account_cache = ""
#
# def login():
#     user = {'account': account, 'password': password}
#     s = requests.Session()
#     s.post('http://sz1card1.5upm.com/user-login.html', data=user)
#
#     return s
#
# def get_user_account():
#     ss = login()
#
#     global account_cache
#     if account_cache == "":
#         account_cache = ss.get("http://sz1card1.5upm.com/company-browse-0-bydept-id-110-200-1.json").json()
#         users = json.loads(account_cache["data"])["users"]
#     else:
#         users = json.loads(account_cache["data"])["users"]
#
#     result = ""
#     for user in users:
#         if user["realname"] == "sss":
#             result = user["account"]
#             return result
#
#     if result == "":
#         account_cache = ss.get("http://sz1card1.5upm.com/company-browse-0-bydept-id-110-200-1.json").json()
#         users = json.loads(account_cache["data"])["users"]
#
#         for user in reversed(users):
#             if user["realname"] == "欧阳文":
#                 result = user["account"]
#                 return result
#
# if __name__ == "__main__":
#     account = get_user_account()
#
#     print(account)

# import pymysql
# import json
#
# conn = pymysql.connect(host="192.168.2.165", port=3306,user="geek", passwd="123456",database="ops")
#
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# sql = "select name from babel_project;"
#
# cursor.execute(sql)
#
# res = cursor.fetchall()
#
# cursor.close()
# conn.close()
#
# pro_dict = {}
# # pro_list=[]
# # # print(len(res))
# # # print(res[0].get("name"))
#
# # for i in range(len(res)):
# #     pro_list.append(res[i].get("name"))
# for i in range(len(res)):
#     pro_dict[f"{i}"] = res[i].get("name")
#
# print(json.dumps(pro_dict))

# import requests
# # import json
#
# account = "djz"
# password = "q19980603.123"
# #
# # global account_cache
# # account_cache = ""
#
# def login():
#     user = {'account': account, 'password': password}
#     s = requests.Session()
#     s.post('http://sz1card1.5upm.com/user-login.html', data=user)
#
#     return s
#
# def story_close():
#     ss = login()
#
#     data = dict(closedReason="done", duplicateStory="", childStories="", comment="")
#
#     res = ss.post("http://sz1card1.5upm.com/story-close-21038.json",data=data)
#
#     return res
#
# if __name__ == "__main__":
#     res = story_close()
#
#     print(res)

# att = {'url': 'https://pro-cs.kefutoutiao.com/tid44157/%E5%85%85%E5%80%BC%E5%B0%8F%E7%A5%A8%E6%8E%92%E7%89%88_1606358102_1606358102066_519ed9.docx?OSSAccessKeyId=bPexlr6MCcadDhfu&Expires=1637905713&Signature=%2FRHyNTLUg6aowp3uEE0IdOJXlXQ%3D',
#        'file_name': '充值小票排版_1606358102_1606358102066_519ed9.DDD',
#        'file_size': 13712}
#
# filename = att.get("file_name").split(".")[-1].lower()
# suffix = filename[1]
#
# print(filename)
# # print(filename)
# # print(suffix)

import pymysql
import json
import datetime

str = "select * from babel_log WHERE types != '' "

user = ''

project_name = 'Agent'

if user:
    str = str + f"and user = '{user}' "

if project_name:
    str = str + f"and project_name = '{project_name}' "

str = str + ";"

print(str)

conn = pymysql.connect(host="192.168.2.165", port=3306,user="geek", passwd="123456",database="ops")

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# sql = "select name from babel_project;"

cursor.execute(str)

res = cursor.fetchall()

cursor.close()
conn.close()

print(res)

my_dict = {}

for i in range(len(res)):
    my_dict[i] = res[i].get("project_name")
print(my_dict)
# #     # my_list.append(my_dict[i])
# #     create_time = my_dict[i].get("create_time").strftime("%Y-%m-%d %H:%M:%S")
# #     update_time = my_dict[i].get("update_time").strftime("%Y-%m-%d %H:%M:%S")
# #     my_dict[i]["create_time"] = create_time
# #     my_dict[i]["update_time"] = update_time
#     # print(create_time)
# create_time = res[0].get("create_time").strftime("%Y-%m-%d %H:%M:%S")
# update_time = res[0].get("update_time").strftime("%Y-%m-%d %H:%M:%S")
# res[0]["create_time"] = create_time
# res[0]["update_time"] = update_time
#
# print(res)

# import re
# # from bs4 import BeautifulSoup
#
# my_html = '''
# <p>附件:
#     <ul id=udesk_attachments'>
#         <li><a href='https://pro-cs.kefutoutiao.com/tid44157/%E6%B5%8B%E8%AF%95_1607051996_1607051996097_b95dcb.png?OSSAccessKeyId=bPexlr6MCcadDhfu&Expires=1638588003&Signature=Lmux0QmU0RruKsQYeXiSkHQcy9Y%3D' download='测试_1607051996_1607051996097_b95dcb.png'>测试_1607051996_1607051996097_b95dcb.png</a></li>
#         <li><a href='https://pro-cs.kefutoutiao.com/tid44157/%E6%B5%8B%E8%AF%95_1607052000_1607052000292_a3d28d.docx?OSSAccessKeyId=bPexlr6MCcadDhfu&Expires=1638588003&Signature=ZFFqWNckfAvImbA7fE%2FpBB0vw48%3D' download='测试_1607052000_1607052000292_a3d28d.docx'>测试_1607052000_1607052000292_a3d28d.docx</a></li>
#     </ul>
# </p>
# '''
# compile_rule=re.compile(r"<a.*?href=https://|http://.*? ")
#
# url_list=re.findall(compile_rule, my_html)
#
# print(url_list)
#
# for i in url_list:
#     print()

# soup = BeautifulSoup(my_html)
# tags = soup.find_all("p")
# new_list = []
# for tag in tags:
#     new_dict = {}
#     new_dict["url"] = tag.ul.li.a
#     new_list.append(new_dict)
#
# # print(new_dict)
# print(new_list)