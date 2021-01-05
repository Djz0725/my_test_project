"""
@file: 数据库数据监测
@author: DJZ
@time: 2020/12/31
@desc
"""

import re
import pymysql
import sys

count = 0
fail_count_total1 = 0
fail_count_total2 = 0
fail1 = []
fail2 = []
fail = []

with open(sys.argv[4],'r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        if i.startswith("REPLACE"):
            count += 1
            pattern = re.compile(r'`.*`\(`.*`')
            result = pattern.findall(i)[0].split("`")
            database = result[1]
            table = result[3]
            first_filed = result[5]
            pattern = re.compile(r"\('.*?'")
            result = pattern.findall(i)[0].split("'")
            value = result[1]

            try:
                conn = pymysql.connect(host=sys.argv[1], port=int(sys.argv[3]), user="mysqldiff",
                                       passwd="zZC8gtq3oySh")
                cursor = conn.cursor()
                cursor.execute(f"select * from {database}.{table} where {first_filed} = '{value}';")
                res1 = cursor.fetchall()
                conn.commit()
                cursor.close()
                conn.close()
                if len(res1) == 0:
                    fail1.append(value)
                    fail_count_total1 += 1
                    continue
            except Exception as err1:
                print(err1)

            try:
                conn = pymysql.connect(host=sys.argv[2], port=int(sys.argv[3]), user="mysqldiff",
                                       passwd="zZC8gtq3oySh")
                cursor = conn.cursor()
                cursor.execute(f"select * from {database}.{table} where {first_filed} = '{value}';")
                res2 = cursor.fetchall()
                conn.commit()
                cursor.close()
                conn.close()
                if len(res2) == 0:
                    fail2.append(value)
                    fail_count_total2 += 1
            except Exception as err2:
                print(err2)
        else:
            pass

print("实例1查询失败的id有：",fail1,f"\n一共有{fail_count_total1}个")
print("实例2查询失败的id有：",fail2,f"\n一共有{fail_count_total2}个")
print("查询总次数为：",count)
