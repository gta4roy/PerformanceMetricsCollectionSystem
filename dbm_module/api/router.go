package api

import (
	"dbm_module/log"
	"net/http"
	"time"

	"github.com/gorilla/mux"
)

type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

type Routes []Route

const (
	BaseURL = "/api/v1/dbm"

	HealthChecURL = "/health"

	getAllSysCPUKeys = BaseURL + "/getsyscpukeys"

	getALLSysLoadAvgKeys = BaseURL + "/getsysloadavgkeys"

	getPerfValues = BaseURL + "/getperfvalues/{key}"
)

var routes = Routes{
	Route{
		"HealthCheck", "GET", HealthChecURL, handlerGetHealth,
	},
	Route{
		"getAllSysCPUKeys", "GET", getAllSysCPUKeys, handlerGetAllSysCPUKeys,
	},
	Route{
		"getAllSysLOADAVGKeys", "GET", getALLSysLoadAvgKeys, handlerGetALLSysLoadAvgKeys,
	},
	Route{
		"getPerfValues", "GET", getPerfValues, handlerGetPerfValues,
	},
}

func logger(inner http.Handler, name string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		inner.ServeHTTP(w, r)
		log.Trace.Println("%s %s 5s %s", r.Method, r.RequestURI, name, time.Since(start))
	})
}

func NewRouter() *mux.Router {
	router := mux.NewRouter().StrictSlash(true)
	for _, route := range routes {
		var handler http.Handler
		handler = route.HandlerFunc
		handler = logger(handler, route.Name)
		router.Methods(route.Method).Path(route.Pattern).Name(route.Name).Handler(handler)
	}
	return router
}
