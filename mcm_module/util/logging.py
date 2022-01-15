import logging
import util.configurations as config


def getLogger(name):

    logger = logging.getLogger(name)
    logFileName = config.getLogFile()
    f_handler = logging.FileHandler(logFileName)
    #f_handler.setLevel(logging.DEBUG)

    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.info("Logging initialised")
    return logger
