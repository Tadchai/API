import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testDB",
  password="12345",

)
print(mydb)
# <mysql.connector.connection.MySQLConnection object at 0x0000027BD56BC040>