import json


class CPU:

    USER = "user"
    IDLE = "idle"
    SYSTEM = "system"
    TIMESTAMP = "time"
    DATE = "date"
    KEY = "KEY"

    def __init__(self): 
        self.userPercent = ""
        self.idlePercent =""
        self.systemPercent =""
        self.timestamp = ""
        self.date = ""
        self.key = ""
        
    def setValues(self,userPercent,idlePercent,systemPercent,timestamp,date):
        self.userPercent = userPercent
        self.idlePercent = idlePercent
        self.systemPercent = systemPercent
        self.timestamp = timestamp
        self.date = date

    def getValues(self):
        valuesDict = {}
        valuesDict[CPU.USER] = self.userPercent
        valuesDict[CPU.IDLE] = self.idlePercent
        valuesDict[CPU.SYSTEM] = self.systemPercent
        valuesDict[CPU.TIMESTAMP] = self.timestamp
        valuesDict[CPU.KEY] = self.key
        valuesDict[CPU.DATE] = self.date
        return valuesDict

    def getJsonValues(self):
        return json.dumps(self.getValues())
