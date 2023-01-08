import json
import os
import random

class World:
    
    def __init__(self):
        print("A world action has been done")

    def AddInstance(self,Type,FilePath,posx,posy):
        RID = random.randint(0,9999999999)
        data = {"Type": Type, "ID": RID,"FilePath": FilePath,"POSX": posx,"POSY": posy}
        WFile = open("WFile__" + RID + ".json", "w+" )
        with WFile as wf:
            json.dump(data,wf,indent=4)

#getters

    def GetType(self,id):
        WFile = open("WFile__" + id + ".json", "r+" )
        with WFile as f:
            data = json.load(f)
            return data["Type"]

    def GetFilePath(self,id):
        WFile = open("WFile__" + id + ".json", "r+" )
        with WFile as f:
            data = json.load(f)
            return data["FilePath"]

    def GetPOSX(self,id):
        WFile = open("WFile__" + id + ".json", "r+" )
        with WFile as f:
            data = json.load(f)
            return data["POSX"]

    def GetPOSY(self,id):
        WFile = open("WFile__" + id + ".json", "r+" )
        with WFile as f:
            data = json.load(f)
            return data["POSY"]

# setters
    def SetPOSX(self,id):
        WFile = open("WFile__" + id + ".json","r+")
        with UFile as f:
            data = json.load(f) # Selectionne le fichier
            data['POSX'] = value # Change la valeur
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate()

    def SetPOSY(self,id):
        WFile = open("WFile__" + id + ".json","r+")
        with UFile as f:
            data = json.load(f) # Selectionne le fichier
            data['POSY'] = value # Change la valeur
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate()

    def DeleteInstance(self,id):
        WFile = ("WFile__" + id + ".json","r+")
        os.remove(WFile)


    