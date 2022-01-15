import json


class LoadAvg:

    ONEMINUTH = "min_1"
    FIVEMINUTH = "min_5"
    FIVETINTHMINUTH = "min_15"
    TIMESTAMP = "time"
    DATE = "date"
    KEY = "KEY"

    def __init__(self): 
        self.onethminute = ""
        self.fivethminute =""
        self.fivetheenthminute =""
        self.timestamp = ""
        self.date = ""
        self.key = ""
    
    def getValues(self):
        valuesDict = {}
        valuesDict[LoadAvg.ONEMINUTH] = self.onethminute
        valuesDict[LoadAvg.FIVEMINUTH] = self.fivethminute
        valuesDict[LoadAvg.FIVETINTHMINUTH] = self.fivetheenthminute
        valuesDict[LoadAvg.TIMESTAMP] = self.timestamp
        valuesDict[LoadAvg.KEY] = self.timestamp
        valuesDict[LoadAvg.DATE] = self.date
        return valuesDict

    def getJsonValues(self):
        return json.dumps(self.getValues())
