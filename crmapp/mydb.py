import mysql.connector

dataBase = mysql.connector.connect(
    user='root', 
    passwd='root123',
    host='localhost',
    
)


cursor =dataBase.cursor()

cursor.execute("CREATE DATABASE elderco")
print("Alldone")