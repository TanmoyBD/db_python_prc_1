import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmoy",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql_command="""
               CREATE TABLE Manager(
                  name varchar(20),
                  age int,
                  roll int
               );
            """
mycursor.execute(sql_command)