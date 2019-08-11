#!/usr/bin/python
# -*- coding: UTF-8 -*-

# PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中是使用mysqldb。
# import MySQLdb
import pymysql

#打开数据库连接
db = pymysql.connect(host="119.23.232.23",user="root",password="root",db="springbootest",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

#1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from test"
try:
    cur.execute(sql)     #执行sql语句

    results = cur.fetchall()    #获取查询的所有记录

    # print("id" , "name","password")
    # #遍历结果
    # for row in results :
    #     id = row[0]
    #     name = row[1]
    #     password = row[2]
    #     print(id,name,password)

    print("result",results)
except Exception as e:
    raise e
finally:
    db.close()    #关闭连接