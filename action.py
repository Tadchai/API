from conDB import Con as C
#c = Con
class Action :
    def delete_hardware():
        data  = C.get_hardware()
        return data
    
    def update_hardware(ID,status):
        t  = C.update_hardware(ID,status)
        if(t == True):
            data = C.select_hardware(ID)
        else:
            data ={"error": True}
        return data
    
    def select_hardware(ID):
        data  = C.select_hardware(ID)
        return data
    
    def insert_hardware(name,hw_name):
        ID = C.insert_hardware(name,hw_name)
        if(ID):
            data = C.select_hardware(ID)
        else:
            data ={"error": True}
        return data
    
    def delete_hardware():
        t  = C.delete_hardware()
        if(t == True):
            data = C.get_hardware()
        else:
            data ={"error": True}
        return data  
    