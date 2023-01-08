import json
import os

class Users:
    def __init__(self):
        print("A db action has been started")

    def AddUser(self,name,Role):
        UFile = open(("UFile__" + name + ".json"),"w+")
        data = {"Name": name,"Role": Role,"Science": 0,"O2": 20}
        with UFile as write_file:
            json.dump(data, write_file)
# setters
    def O2(self,user,value):
        UFile = open("UFile__" + user + ".json","r+")
        with UFile as f:
            data = json.load(f) # Selectionne le fichier
            data['O2'] = value # Change la valeur
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate()

    def Science(self,user,value):
        UFile = open("UFile__" + user + ".json","r+")
        with UFile as f:
            data = json.load(f) # Selectionne le fichier
            data['Science'] = value # Change la valeur
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate()
# getters

    def GetRole(self,user):
        UFile = open("UFile__" + user + ".json","r+")
        with UFile as f:
            data = json.load(f)
            return data["Role"]

    def GetScience(self,user):
        UFile = open("UFile__" + user + ".json","r+")
        with UFile as f:
            data = json.load(f)
            return data['Science']
    
    def GetO2(self,user):
        UFile = open("UFile__" + user + ".json","r+")
        with UFile as f:
            data = json.load(f)
            return data['O2']


    def DeleteUser(self,name):
        os.remove("UFile__"+name +".json")
        print("User : " + name + " Has been deleted")

    





