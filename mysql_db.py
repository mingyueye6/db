# coding: utf-8

import pymysql

db = pymysql.connect(
        host="118.24.155.213",
        user="xiaochengfu_test",
        passwd="JRLDACGaHMGwdbFc",
        db="xiaochengfu_test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

cur = db.cursor()  # 创建游标对象

cur.close()
db.close()