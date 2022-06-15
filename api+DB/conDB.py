import mysql.connector
def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="testDB",
        password="12345",
        database="testdb",
    )
    return mydb
class Con:
    def getHWByID(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def updateStatusAndValueHW(ID,status,value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware SET status = '{}', value = {} WHERE id = {}".format(status,value,ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

class Con2:
    def getUser(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM user WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def changePassword(user):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE user SET username ='{}',password = '{}' WHERE id = {}".format(user.username,user.password,user.ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True