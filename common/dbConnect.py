import pymysql
from interface_1.common.Logs import MyLog as Log
from interface_1.common.Yaml import MyConfig
import logging
class MyDB():
    global host, username, password, port, database, config
    obj=MyConfig()
    host = obj.getData("host")
    username = obj.getData("username")
    password = obj.getData("password")
    port = obj.getData("port")
    database = obj.getData("databasename")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        pass

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
            return self.db
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.connectDB().close()
        print("Database closed!")


if __name__=='__main__':


    sql=MyConfig().getData("sql_query")

    print( MyDB().get_all(MyDB().executeSQL(sql)))
    MyDB().closeDB()