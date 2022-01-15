
import threading
from scm.syscpu import SystemCPUFetch
import util.logging as log
import util.configurations as config

logger = log.getLogger(__name__)
class SystemCallModule(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        logger.error("System Call Module Initialised ")
        self.readingInterval= config.getInterval()
        self.totalReadings = config.getReadingCount()
        self.cpufetchThread =SystemCPUFetch(int(self.readingInterval),int(self.totalReadings))
        self.cpufetchThread.start()
        self.cpufetchThread.join()
