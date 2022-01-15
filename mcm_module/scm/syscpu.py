import threading
import psutil
from util.redisconnection import setValueInRedis
from model.cpu import CPU
import util.logging as log
from time import sleep
from datetime import date
from datetime import datetime
import socket

logger = log.getLogger(__name__)
class SystemCPUFetch(threading.Thread):
    def __init__(self,timeinterval,totalreadings):
        threading.Thread.__init__(self)
        self.timeinterval = timeinterval
        self.totalreadings = totalreadings
        self.fetchCalls = 0

    def fetchCPU(self):
        logger.error("fetching CPU and performance")
        cpuUsageOsReading = psutil.cpu_times_percent()        
        cpu = CPU()
        cpu.idlePercent = cpuUsageOsReading.idle
        cpu.systemPercent = cpuUsageOsReading.system
        cpu.userPercent = cpuUsageOsReading.user
        cpu.date = date.today().strftime("%b-%d-%Y")
        cpu.timestamp = datetime.now().strftime("%H-%M-%S")
        hostname = socket.gethostname()
        keyString = hostname+"-"+cpu.date+"-"+cpu.timestamp
        setValueInRedis(keyString,cpu.getJsonValues())
        logger.error("CPU readings :"+ cpu.getJsonValues())
        self.fetchCalls+=1
    
    
    def run(self):
        logger.error("CPU Fetch Timer started ")
        while self.fetchCalls < self.totalreadings:
            self.fetchCPU()
            sleep(self.timeinterval)

        
