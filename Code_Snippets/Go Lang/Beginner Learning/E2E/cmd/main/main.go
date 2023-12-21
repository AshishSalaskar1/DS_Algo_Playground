package main

import (
	"fmt"
	"golang-basics/hello"
	"strings"
)


func main() {
	hello.SayHello()

	s := "this is an big splitter word"

	splitStrings := strings.Split(s, "i") // this returns a slice split with "i" 
	fmt.Println(splitStrings)

	fmt.Println(strings.Join(splitStrings,"X")) //returns string: same as "X".join(arr) in python
}