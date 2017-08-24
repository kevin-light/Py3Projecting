import pymysql

#创建数据库链接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='db2')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#执行存储过程
row = cursor.callproc('proc_p5',(1,2,3))
#存储过程查询结果
selc = cursor.fetchall()
print(selc)
#获取存储过程的返回
effect_row = cursor.execute("select @_proc_p5_0, @_proc_p5_1, @_proc_p5_2")
#获取存储过程的返回值
result = cursor.fetchone()
print(result)
conn.commit()
cursor.close()
conn.close()


