from re import A
import mysql.connector

def conDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="testDB",
    password="12345",
    database="testdb",
    )
    return mydb

class Con:
    def get_hardware():
        mydb =conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    
    def select_hardware(ID):
        mydb =conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def insert_hardware(name,hw_name):
        mydb =conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware(name,hw_name,status,value) VALUES ('{}','{}','OFF',0)".format(name,hw_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        return ID
    
    def update_hardware(ID,status):
        mydb =conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status,ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
        
    def delete_hardware():
        mydb =conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hard_ware WHERE id =(SELECT MIN(id) FROM hard_ware)"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
        
