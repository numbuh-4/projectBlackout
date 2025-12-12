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
    # def show_all_tables(self):
    #     self.bigBrother.execute("SHOW TABLES")

    #     for x in self.bigBrother:
    #         print(x)
    
            
            
    # def saveScore(self,name):
    #     # i need to call this function when i click return on 
    #     # the save score screen, apart from calling this function I need to pass 
    #     #in the name 
    #     #I then have to save it to the database thats the POINT of this function
    #     #this will be saved into the PLAYERS TABLE
        
    #     sql_query = ("INSERT INTO players (username) VALUES (%s)")
    #     value = (name,)
    #     self.bigBrother.execute(sql_query, value)
    #     self.mydb.commit()
    #     print(f"saved {name} in database successfully")
    # def getName(self):
    #     names = []
    #     query = ("SELECT * FROM project_blackout.players")
    #     self.bigBrother.execute(query)
    #     results = self.bigBrother.fetchall()
    #     for names in results:
    #         print(names[1])
    #         names.append(names[1])
    #     return names
    def saveToLeaderboard(self,name,score,round_died_on):
        # I need a function that accepts name, score, round died
        # then save that to the leaderboard table in project blackout
        # thats all this function is doing
        sql_query = "INSERT INTO leaderboard (username,score, round_died) VALUES (%s, %s,%s)"
        
        value = (name, score, round_died_on)
        self.bigBrother.execute(sql_query, value)
        self.mydb.commit()
        print(f"Saved {name}, Score: {score}, Round: {round_died_on} to leaderboard successfully.")
        
    def fetchingLeaderboard(self):
        #what this function is doing is fetching the last 5 submissions
        # and returning name, score, round died
        # query = ("SELECT id, username, score, round_died, submission_time FROM leaderboard")
        query = """
        SELECT
            username,
            score,
            round_died,
            DATE_FORMAT(submission_time, '%m-%d-%Y') AS formatted_date
        FROM
            leaderboard
        ORDER BY
            score DESC
        LIMIT
            5;
        """
        self.bigBrother.execute(query)
        
        my_result = self.bigBrother.fetchall()
        #↑↑↑↑↑↑↑↑ this returns data as a list of tuples 
        print("LEADERBOARD (last 5 submissions)")
        for row in my_result:
            print(f"User: {row[0]}, Score: {row[1]}, Round Died: {row[2]}, Date: {row[3]}")
            print(row)
        return my_result