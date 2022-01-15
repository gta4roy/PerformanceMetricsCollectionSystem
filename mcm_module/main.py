from scm.systemcallmodule import SystemCallModule
import  util.logging as log
logger = log.getLogger(__name__)

def main():
    logger.error("--MCM Module Started ")
    print("---MCM Module Started---")
    scmThread = SystemCallModule()
    scmThread.start()
    scmThread.join()
    logger.error('Exit')

if __name__ == "__main__":
    main()
