import pymysql

#创建数据库链接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='db2')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# # pymysql默认开启事物
# cursor.execute("UPDATE person SET email='qq.com' WHERE nid=6")
# cursor.execute("UPDATE person SET email='qq.com' WHERE nid=6")

#动态执行SQL语句 ： 防止SQL注入

row = cursor.callproc('proc_sql',('select * from person where nid > ?',6,))
selc = cursor.fetchall()
print(selc)
conn.commit()
cursor.close()
conn.close()


