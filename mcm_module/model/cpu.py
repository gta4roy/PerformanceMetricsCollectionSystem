import json


class CPU:

    USER = "user"
    IDLE = "idle"
    SYSTEM = "system"

    def __init__(self): 
        self.userPercent = ""
        self.idlePercent =""
        self.systemPercent =""
        
    def setValues(self,userPercent,idlePercent,systemPercent):
        self.userPercent = userPercent
        self.idlePercent = idlePercent
        self.systemPercent = systemPercent

    def getValues(self):
        valuesDict = {}
        valuesDict[CPU.USER] = self.userPercent
        valuesDict[CPU.IDLE] = self.idlePercent
        valuesDict[CPU.SYSTEM] = self.systemPercent
        return valuesDict

    def getJsonValues(self):
        return json.dumps(self.getValues())
