import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testDB",
  password="12345",
  database="testdb"
)
mycursor = mydb.cursor(dictionary=True)

sql = "DELETE FROM hard_ware  WHERE id>6"
##########################
mycursor.execute(sql)
mydb.commit()
########################

print(mycursor.rowcount, "record delete")