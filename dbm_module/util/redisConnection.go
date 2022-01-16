package util

import (
	"fmt"
	"log"

	"github.com/gomodule/redigo/redis"
)

func GetRedisConnection() redis.Conn {

	redisHostStr := GetProperty(RedisHost)
	redisPortStr := GetProperty(RedisPort)

	conn, err := redis.Dial("tcp", redisHostStr+":"+redisPortStr)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf(" Redis Connected Succussfully ")
	return conn
}

func GetALLRedisKeys(conn redis.Conn, prefixKey string) []string {

	keys, err := redis.Strings(conn.Do("KEYS", prefixKey+"*"))
	if err != nil {
		log.Fatal(err)
	}
	for _, key := range keys {
		fmt.Println(key)
	}
	return keys
}

func GetRedisValue(conn redis.Conn, key string) string {

	key, err := redis.String(conn.Do("GET", key))
	if err != nil {
		log.Fatal(err)
	}
	return key
}
