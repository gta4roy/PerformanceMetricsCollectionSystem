import threading
from scm.syscpu import SystemCPUFetch
import util.logging as log

logger = log.getLogger(__name__)
class SystemCallModule(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        logger.error("System Call Module Initialised ")
        self.cpufetchThread =SystemCPUFetch(2,100)
        self.cpufetchThread.start()
        self.cpufetchThread.join()
