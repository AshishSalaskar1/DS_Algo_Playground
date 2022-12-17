package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var username string = "ahsish"
	fmt.Printf("The username is %T \n", username)
	fmt.Println("HELLO FROM GOLANG")

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter some number")
	input, _ := reader.ReadString('\n') // read till \n in encountered

	numInput, err := strconv.ParseFloat(strings.TrimSpace(input), 64)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Added 1 to number: ", numInput+1)
	}

	fmt.Println("The value that you have read is: ", numInput)
}
