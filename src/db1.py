# __Desc__ = 从数据库中导出数据到excel数据表中
import xlwt
import pymysql


class MYSQL:
    def __init__(self):
        pass

    def __del__(self):
        self._cursor.close()
        self._connect.close()

    def connectDB(self):
        """
        连接数据库
        :return:
        """
        try:
            self._connect = pymysql.Connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='test',
                charset='utf8'
            )
            return 0
        except:
            return -1

    def export(self, table_name, output_path):
        self._cursor = self._connect.cursor()
        count = self._cursor.execute('select * from '+table_name)
        # print(self._cursor.lastrowid)
        print(count)
        # 重置游标的位置
        self._cursor.scroll(0, mode='absolute')
        # 搜取所有结果
        results = self._cursor.fetchall()
        # 获取MYSQL里面的数据字段名称
        fields = self._cursor.description
        workbook = xlwt.Workbook()
        # 注意: 在add_sheet时, 置参数cell_overwrite_ok=True, 可以覆盖原单元格中数据。
        # cell_overwrite_ok默认为False, 覆盖的话, 会抛出异常.
        sheet = workbook.add_sheet('table_'+table_name, cell_overwrite_ok=True)
        # 写上字段信息
        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])
        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results)+1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row-1][col])
        workbook.save(output_path)


if __name__ == '__main__':
    mysql = MYSQL()
    flag = mysql.connectDB()
    if flag == -1:
        print('数据库连接失败')
    else:
        print('数据库连接成功')
        mysql.export('employee', 'E:/test_input.xls')
