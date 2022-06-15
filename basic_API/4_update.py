import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testDB",
  password="12345",
  database="testdb"
)
mycursor = mydb.cursor(dictionary=True)

sql = "UPDATE hard_ware SET status ='on' WHERE name= 'A2'"
##########################
mycursor.execute(sql)
mydb.commit()
########################

print(mycursor.rowcount, "record update")