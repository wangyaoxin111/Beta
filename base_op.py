import pymssql
import traceback


class SQL(object):

    def __init__(self,host,user,password,database):
        self.conn = pymssql.connect(host,user,password,database)
        self.cursor = self.conn.cursor()

    def create_table(self,sql):
        self.cursor.execute(sql)
        print('数据库创建成功')

    def insert_data(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def update_date(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print(traceback.format_exc())
            self.conn.commit()

    def delete_date(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print(traceback.format_exc())
            self.conn.commit()

    def select_data(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.cursor.close()
        self.conn.close()



