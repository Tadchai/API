import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testDB",
  password="12345",
  database="testdb"
)
mycursor = mydb.cursor(dictionary=True)

sql = "INSERT INTO hard_ware (name,hw_name,status,value) VALUES('A2','servo','off',0.00)"
##########################
mycursor.execute(sql)
mydb.commit()
########################
ID = mycursor.lastrowid
#print('ID :' +str(ID))
print(f"ID : {ID}")
print(mycursor.rowcount, "record inserted")
