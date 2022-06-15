import mysql.connector
def Mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="testDB",
        password="12345",
        database="testdb"
        )
    return mydb
    
class getData:
    def getDataSelect(ID):
         mydb = Mysql()
         mycursor = mydb.cursor(dictionary = True)
         
         sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)
         
         mycursor.execute(sql)
         data = mycursor.fetchall()
         return data
    
    def getDataInsert(name, hw_name, status, value):
        mydb = Mysql()
        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO hard_ware (name, hw_name, status, value) VALUES ('{}', '{}', '{}', {})".format(name, hw_name, status, value)

        mycursor.execute(sql)
        mydb.commit()
        data= mycursor.lastrowid
        return data

    def getDataUpdate(ID, status, value):
        mydb = Mysql()
        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}', value = {} WHERE ID = {}".format(status,value,ID)
        
        mycursor.execute(sql)
        mydb.commit()
        data= mycursor.lastrowid
        return data
    
    def getDataDelete(ID):
        mydb = Mysql()
        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM hard_ware WHERE ID = {}".format(ID)
        
        mycursor.execute(sql)
        mydb.commit()
        data= mycursor.lastrowid
        return data

