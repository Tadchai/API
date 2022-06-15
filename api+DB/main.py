import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from action import Action
app = FastAPI()

class chagnePassword(BaseModel):
    ID: Optional[int]
    username: Optional[str]
    password: Optional[str]

@app.get("/hw/update_StatusAndValue_hw")
async def hw_update_StatusAndValue_hw(ID,status,value):
    data = Action.updateStatusAndValueHW(ID,status,value)
    return data

@app.post("/chang_pasword")
async def chang_pasword(user: chagnePassword):
    data = Action.changePassword(user)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.40.116", port=8000)