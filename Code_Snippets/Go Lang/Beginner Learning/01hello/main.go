package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// if varName starts with Capital -> public variable
	var username string = "ahsish"

	// available data types - uint8|16|32, int8|16|32, float32|64, byte, rune, complex
	fmt.Printf("The username is %T \n", username)
	fmt.Println("HELLO FROM GOLANG")

	//default values and aliases - automatically fills with default values baded on type giving
	var defaultInt int32
	fmt.Println((defaultInt))

	//implicit -> if you dont tell what datatype but directly assign
	// 		   -> it automatically picks up datatype of assingning, later you cant change that
	var tempStr = "ASHISH"
	fmt.Println((tempStr))
	//tempStr = 123 // gives error as tempstr is defined as string

	//no-var or WALRUS operator
	// not allowed outside the methods in gloval variables
	count := 100
	fmt.Println((count))

	// CONSTANTS
	const LoginToken = "ashish"

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
