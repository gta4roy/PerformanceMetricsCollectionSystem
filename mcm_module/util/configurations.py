import configparser

def getLogFile():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['MCM_DEFAULT']['logging_file']

def getInterval():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['MCM_DEFAULT']['interval']

def getReadingCount():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['MCM_DEFAULT']['totalreadings']

def getRedisHostName():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['REDIS']['hostname']

def getRedisPort():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['REDIS']['port']