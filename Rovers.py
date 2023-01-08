import json
import os
class Rovers:
    def __init__(self):
        print("Rover's DB action done")
    
    def addRover(self,name,posx,posy):
        RFile = open("RFile__" + name +".json","w+")
        data = {"name": name,"Energy": 50,"POSX":posx,"POSY":posy}
        with RFile as write_file:
            json.dump(data, write_file,indent=4)
# setters
    def SetEnergy(self,name,value):
        RFile = open("RFile__" + name + ".json","r+")
        with RFile as f:
            data = json.load(f)
            data['Energy'] = value # Change la valeur
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate()

    def SetPOSX(self,name,value):
        RFile = open("RFile__" + name + ".json")
        with RFile as f:
            data = json.load(f)
            data['POSX'] = value
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()

    def SetPOSY(self,name,value):
        RFile = open("RFile__" + name + ".json")
        with RFile as f:
            data = json.load(f)
            data['POSY'] = value
            f.seek(0)
            json.dump(data,f,indent = 4)
            f.truncate()

# getters

    def GetEnergy(self,name):
        RFile = open("RFile__" + name + ".json")
        with RFile as f:
            data = json.load(f)
            return data['Energy']

    def GetPOSX(self,name):
        RFile = open("RFile__" + name + ".json")
        with RFile as f:
            data = json.load(f)
            return data['POSX']

    def GetPOSY(self,name):
        RFile = open("RFile__" + name + ".json")
        with RFile as f:
            data = json.load(f)
            return data['POSY']

    def DeleteRover(self,name):
        os.remove("RFile__" + name + ".json")




    

    