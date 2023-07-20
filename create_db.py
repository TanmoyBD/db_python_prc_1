import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmoy"
)

mycursor = mydb.cursor()

db_name = "mydatabase"

create_db_sql = "CREATE DATABASE " + db_name
drop_db_sql = "DROP DATABASE " + db_name

mycursor.execute(create_db_sql)
#mycursor.execute(drop_db_sql)



