from ast import And
import json
import redis
import configurations as config

def getRedisConnection():     
    redisHostName = config.getRedisHostName()
    redisPort = config.getRedisPort()
    r = redis.Redis(host=redisHostName,port=redisPort,password='')
    return r

def setValueInRedis(key,value):
    redisConnection = getRedisConnection()
    redisConnection.set(key,value)

def getValue(key):
    redisConnection = getRedisConnection()
    value = redisConnection.get(key)
    dictValue = json.loads(value)
    return dictValue