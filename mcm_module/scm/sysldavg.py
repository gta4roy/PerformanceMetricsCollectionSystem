import os
import threading
import psutil
from util.redisconnection import setValueInRedis
from model.loadavg import LoadAvg
import util.logging as log
from time import sleep
from datetime import date
from datetime import datetime
import socket

logger = log.getLogger(__name__)
class SystemLoadAvgFetch(threading.Thread):
    def __init__(self,timeinterval,totalreadings):
        threading.Thread.__init__(self)
        self.timeinterval = timeinterval
        self.totalreadings = totalreadings
        self.fetchCalls = 0

    def fetchLoadAvg(self):
        logger.error("fetching CPU and performance")
        loadAvgReading = os.getloadavg()        
        ldavg = LoadAvg()
        ldavg.onethminute = loadAvgReading[0]
        ldavg.fivethminute = loadAvgReading[1]
        ldavg.fivetheenthminute = loadAvgReading[2]
        ldavg.date = date.today().strftime("%b-%d-%Y")
        ldavg.timestamp = datetime.now().strftime("%H-%M-%S")
        hostname = socket.gethostname()
        keyString = "LOADAVG-"+hostname+"-"+ldavg.date+"-"+ldavg.timestamp
        ldavg.key = keyString
        setValueInRedis(keyString,ldavg.getJsonValues())
        logger.error("Load AVg readings :"+ ldavg.getJsonValues())
        self.fetchCalls+=1
    
    
    def run(self):
        logger.error("Load Avg fetch started ")
        while self.fetchCalls < self.totalreadings:
            self.fetchLoadAvg()
            sleep(self.timeinterval)

        
