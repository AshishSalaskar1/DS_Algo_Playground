package main

import (
	"context"
	"fmt"

	"github.com/go-redis/redis/v8"
)

var Ctx = context.Background()

func CreateClient(dbNo int) *redis.Client {
	rdb := redis.NewClient(&redis.Options{
		Addr:     "127.0.0.1:6379",
		Password: "",
		DB:       dbNo,
	})

	return rdb
}

func main() {

	rdb := CreateClient(0)
	err := rdb.Set(Ctx, "e92c04", "https://github.com/", 0).Err()
	if err != nil {
		fmt.Println(err)
	}

	val, _ := rdb.Get(Ctx, "e92c04").Result()
	fmt.Println("val: ", val)

	defer rdb.Close()
}
