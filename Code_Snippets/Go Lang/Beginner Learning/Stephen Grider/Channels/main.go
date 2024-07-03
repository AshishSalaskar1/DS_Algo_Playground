package main

import (
	"fmt"
	"log"
	"net/http"
)

func checkSite(site_url string, ch chan string) {
	res, err := http.Get(site_url)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%v --> %v \n", site_url, res.StatusCode)
	ch <- fmt.Sprintf("Site %v has status code as %d", site_url, res.StatusCode)
}

func unbufferedChannel() {
	ch := make(chan string) // Creating an unbuffered channel

	sites := []string{
		"https://google.com",
		"https://go.dev",
		"https://github.com",
	}

	fmt.Println("EXECUTION STARTS")

	for _, site := range sites {
		go checkSite(site, ch)
	}

	for i := 0; i < len(sites); i++ {
		x := <-ch
		fmt.Println("Received from channel:", x)
	}

	// Hangs infintely, since its expected a 4th value, but we put only 3
	x := <-ch
	fmt.Println("Received from channel:", x)

}

func main() {
	ch := make(chan string, 2) // Creating an unbuffered channel

	sites := []string{
		"https://google.com",
		"https://go.dev",
		"https://github.com",
	}

	fmt.Println("EXECUTION STARTS")

	for _, site := range sites {
		go checkSite(site, ch)
	}

	for i := 0; i < len(sites); i++ {
		x := <-ch
		fmt.Println("Received from channel:", x)
	}

	x := <-ch
	fmt.Println("Received from channel:", x)
}
