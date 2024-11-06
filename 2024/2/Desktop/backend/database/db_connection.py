import mysql.connector
from mysql.connector import errorcode

class DBConnection:
    def __init__(self, config):
        self.config = config
        self.cnx    = None
        
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            print("Connected to db")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("There's something wrong with the user or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.cnx = None
            
    def disconnect(self):
        if self.connect:
            self.cnx.close()
            print("Connection has ended")