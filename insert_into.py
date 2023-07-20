import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmoy",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql_command="""
               INSERT INTO Manager(name,age,roll)
               VALUES ("Tanmoy",20,18)
                 
            """
mycursor.execute(sql_command)
mydb.commit()