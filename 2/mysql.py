#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import uuid
# pymysql的用法与MySQLdb完全相同, MySQQLdb 不支持 python3.5 用 pymysql 代替
import pymysql
pymysql.install_as_MySQLdb()

def gene_code(count, length):
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
        if len(result) == count:
            break
        return result

def save_to_mysql(num_list):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='',port=3306)
    cur = conn.cursor()
    sql_create_database = 'create database if not exists activecode_db'
    cur.execute(sql_create_database)

    conn.select_db("activecode_db")
    sql_create_table = 'create table if not exists active_codes(active_code char(32))'
    cur.execute(sql_create_table)

    cur.executemany('insert into active_codes values(%s)', num_list)

    conn.commit()
    cur.close()
    conn.close()

code_num = gene_code(200, 20)
#print code_num
save_to_mysql(code_num)