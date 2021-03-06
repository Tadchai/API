from fastapi import FastAPI
import uvicorn
from action import Action as A
app = FastAPI()

@app.get("/get_hardware")
def get_hardware():
    data = A.get_hardware()
    return data

@app.get("/update_hardware")
def update_hardware(ID,status):
    data = A.update_hardware(ID,status)
    return data

@app.get("/select_hardware")
def select_hardware(ID):
    data = A.select_hardware(ID)
    return data

@app.get("/insert_hardware")
def insert_hardware(name,hw_name):
    data = A.insert_hardware(name,hw_name)
    return data

@app.get("/delete_hardware")
def delete_hardware():
    data = A.delete_hardware()
    return data

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Myname")
def Myname():
    data = 'TAD'
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name(name,last_name):
    data = name +' '+ last_name
    return data

@app.get("/input_name_3")
def input_name(name,last_name):
    
    data = "{} {}".format(name,last_name)
    return data

@app.get("/V")
def V(S,T):
    V = float(S)/float(T)
    data ="V = {:.2f}".format(V)
    return data

@app.get("/R")
def R(R1,R2,R3):
    R_P = ((1/float(R1))+(1/float(R2))+(1/float(R3)))**-1
    R_S = float(R1)+float(R2)+float(R3)
    data ="Rรวมขนาน = {:.2f} Rรวมอนุกรม = {:.2f}".format(R_P,R_S)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)   
