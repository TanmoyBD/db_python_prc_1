import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmoy",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql_command=  """
                 UPDATE manager
                 SET name = "jhon"
                 WHERE roll = 18;   
              """
mycursor.execute(sql_command)
mydb.commit()