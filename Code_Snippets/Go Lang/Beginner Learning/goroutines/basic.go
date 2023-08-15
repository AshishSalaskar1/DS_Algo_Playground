package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

var wg sync.WaitGroup // pointer
var mutex sync.Mutex // pointer

var statusCodeResults =  []string{}

func checkSite(site_url string) {
	// wg.Done only after checkSite completes execution
	defer wg.Done()

	res, err := http.Get(site_url)
	if err != nil{
		log.Fatal(err)
	}

	fmt.Printf("%v --> %v \n", site_url, res.StatusCode)

	// use mutex to lock in case multiple goroutines try to access same memory address
	mutex.Lock()
	statusCodeResults = append(statusCodeResults,site_url)
	mutex.Unlock()
}

func main() {
	sites := []string{
		"https://google.com",
		"https://go.dev",
		"https://github.com",
	}

	fmt.Println("EXECUTION STARTS")

	for _, site_url := range sites {
		go checkSite(site_url)
		wg.Add(1) //add one go routine to wait group
	}

	
	wg.Wait()
	fmt.Println("FINAL LIST", statusCodeResults)
}
