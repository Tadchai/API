import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="testDB",
  password="12345",
  database="testdb"
)
mycursor = mydb.cursor(dictionary = True)

sql = "SELECT * FROM hard_ware"
#"SELECT - FROM - WHERE id ={}".format(ID)
#ID = mycursor.lastrowid
#################################
mycursor.execute(sql)
data = mycursor.fetchall()
#################################
#for x in data:
  #print(x)
#x = data[0][1]
#print(x)
print(data)
for item in data:
    print(f"ID: {item['id']}")
    print(f"name: {item['name']}")
    print(f"hw_name: {item['hw_name']}")
    print(f"status: {item['status']}")
    print(f"value: {item['value']}")