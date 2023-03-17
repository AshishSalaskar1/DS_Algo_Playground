package main

import (
	"fmt"
	"time"
)

func main() {
	presentTime := time.Now()
	fmt.Println(presentTime)
	fmt.Println(presentTime.Format("01-02-2006 15:04:05 Monday"))

	createdDate := time.Date(2020, time.June, 10, 12, 12, 0, 0, time.UTC)
	fmt.Println("My created date: ", createdDate)
}

// BUILDING
// go env -> check GOENV env_variable to get which OS its building
// go build or GOOS="linux" go build
