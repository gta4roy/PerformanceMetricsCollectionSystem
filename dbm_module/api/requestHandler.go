package api

import (
	"dbm_module/log"
	"dbm_module/util"
	"encoding/json"
	"net/http"
)

func handlerGetHealth(w http.ResponseWriter, r *http.Request) {
	log.Trace.Println("Health Request")
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"status":"UP"}`))
	return
}

func handlerGetAllSysCPUKeys(w http.ResponseWriter, r *http.Request) {
	log.Trace.Println("funcGetAllSysCPUKeys Request")

	redisConnection := util.GetRedisConnection()

	keys := util.GetALLRedisKeys(redisConnection, "CPU")

	for _, v := range keys {
		log.Trace.Println(v)
	}

	responseMap := make(map[string][]string)
	responseMap["KEYS"] = keys

	defer redisConnection.Close()
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)

	json.NewEncoder(w).Encode(responseMap)

}
