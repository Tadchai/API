from xmlrpc.client import boolean
from conDB import Con, Con2


class Action:
    def updateStatusAndValueHW(ID,status,value):
        boolean = Con.updateStatusAndValueHW(ID,status,value)
        if boolean:
            data = Con.getHWByID(ID)
        else:
            data = {"error": True}
        return data

    def changePassword(user):
        boolean = Con2.changePassword(user)
        if(boolean):
            data = Con2.getUser(user.ID)
            return data
        else:
            data = {"error": True,}
            return data
