package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"sync"
)

func main() {
	total, max := 10, 3
	var wg sync.WaitGroup
	for i := 0; i < total; i += max {
		limit := max

		// in case limit < remaining_elements (you have lesser elements than u can process)
		if i+max > total {
			limit = total - i
		}

		wg.Add(limit) // add max items you can push
		for j := 0; j < limit; j++ {
			go func(j int) {
				defer wg.Done()

				// send to server
				conn, err := net.Dial("tcp", ":8000")
				if err != nil {
					log.Fatalf("could not dial: %v", err)
				}

				// read response sent from TCP server - SUCCsESSS
				bs, err := io.ReadAll(conn)
				if err != nil {
					log.Fatalf("could not read from conn: %v", err)
				}
				if string(bs) != "success" {
					log.Fatalf("request error, request: %d", i+1+j)
				}

				fmt.Printf("request %d: success\n", i+1+j)
			}(j)
		}
		wg.Wait()
	}
}