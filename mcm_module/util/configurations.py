import configparser

def getLogFile():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['MCM_DEFAULT']['logging_file']