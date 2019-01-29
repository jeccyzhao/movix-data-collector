import pymysql
from common.constants import *

class DatabaseConnection(object):
    def __init__(self, database, host=DB_DEFAULT_HOST, port=DB_DEFAULT_PORT, user=DB_DEFAULT_USER, password=DB_DEFAULT_PASSWORD, charset=DB_DEFAULT_CHARSET):
        self.database = database
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.charset  = charset 
        self.connected = False
        self.connect()
    
    def connect(self):
        if not self.connected:
            self.conn = pymysql.connect(
                database = self.database,
                host = self.host,
                user = self.user,
                password = self.password,
                charset = self.charset,
                cursorclass = pymysql.cursors.DictCursor
            )
            self.connected = True
            self.cursor = self.conn.cursor()
    
    def execute(self, sql, params=[]):
        if not self.connected:
            raise Exception("Connection is closed..")
        self.cursor.execute(sql, params)
        self.conn.commit()
    
    def query(self, sql, params=[]):
        if not self.connected:
            raise Exception("Connection is closed..")
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def disconnect(self):
        if self.connected:
            self.cursor.close()
            self.conn.close()
            self.connected = False