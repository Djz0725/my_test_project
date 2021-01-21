"""
@file: 数据库查询
@author: DJZ
@time: 2021/01/08
@desc
"""

import pymysql

conn = pymysql.connect(host='10.10.12.14',port=6606,user='tech_djz',passwd='95!2ff3#1',database='ops')
cursor = conn.cursor()
cursor.execute("select t2.address, t2.state, t2.description, t1.backup_link from wildebeest_index t1 left join wildebeest_detail t2 on t1.id=t2.parent_id where t1.task_id= 'e62d83ed-5189-11eb-b26a-9e53acb44e7c' AND t2.address is not null")
result = cursor.fetchall()
conn.commit()
cursor.close()

print(result)