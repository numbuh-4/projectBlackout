import mysql.connector
#library that allows an application
#to communicate with a MySQL database

from settings import *
class db_connect:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = DATABASE_USER,
            password = DATABASE_PASSWORD,
            database = 'project_blackout',
        )
        #an object used to execute SQL queries and iterate over the results
        self.bigBrother = self.mydb.cursor()
    def confirm_connection(self):
        if self.mydb.is_connected():
            print("connected to project_blackout")
            
        else:
            print("there is an error")
    def show_all_tables(self):
        self.bigBrother.execute("SHOW TABLES")

        for x in self.bigBrother:
            print(x)
    def get_data(self):
        query = ("SELECT name FROM enemy_types")
        self.bigBrother.execute(query)
        results = self.bigBrother.fetchall()
        for names in results:
            print(names[0])
    def enemies_info(self):
        pass