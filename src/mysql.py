import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3306,
    db="test"
)  # 打开数据库连接
db_cursor = connection.cursor()  # 使用cursor()方法创建一个游标对象cursor
db_cursor.execute("select version()")  # 使用execute()方法执行sql查询
data = db_cursor.fetchone()  # 使用fetchone()方法获取单条数据
print("database version:%s" % data)


# 查询数据
sql = "SELECT nickname,id FROM love_user WHERE id >= %d "
data = (1,)
db_cursor.execute(sql % data)
for row in db_cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', db_cursor.rowcount, '条数据')

connection.close()  # 关闭数据库连接
