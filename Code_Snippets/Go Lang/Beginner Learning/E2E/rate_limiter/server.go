package main

import (
	"log"
	"net"
	"sync/atomic"
	"time"
)

func main() {
	li, err := net.Listen("tcp",":8000")
	if err != nil {
		log.Fatal("could not create server: ", err)
	}

	// maintain no_of_conenctions
	var nConnections int32
	const maxConnections = 3

	// while loop to listen to requests
	for {
		conn, err := li.Accept()
		if err != nil {
			continue
		}

		// added 1 connection
		nConnections++

		go func (con net.Conn)  {
			defer func ()  {
				_ = con.Close()
				atomic.AddInt32(&nConnections,-1) // same thing as wg.Done()
			}()


			// max connections are reached dont take any more
			if atomic.LoadInt32(&nConnections) > maxConnections {
				return
			}


			// simulate heavy work
			time.Sleep(time.Second)
			_, err := conn.Write([]byte("success"))
			if err != nil {
				log.Fatalf("could not write to connection: %v", err)
			}

		}(conn)
		
	}


}