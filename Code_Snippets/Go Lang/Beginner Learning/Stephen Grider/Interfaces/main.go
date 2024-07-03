package main

import "fmt"

type EnglishBot struct{}
type SpanishBot struct{}

func (eb EnglishBot) getGreeting() string {
	// some complex logic to fetch greeting specific to English
	return "Hello World..."
}

func (eb SpanishBot) getGreeting() string {
	// some complex logic to fetch greeting specific to Spanish
	return "Hola Mundo..."
}

/*
- ASSUME getGreeting() functions have some language specific code and cant be merged
1. You want a printGreeting() method with just calls getGreeting() method of each bot
2. This is method which takes bots as arguments (NOT RECEIVER METHOD)

Go doesnt support METHOD OVERLOADING
- You CANT HAVE functions with SAME NAME BUT DIFFERENT SIGNATURES

func printGreeting(eb EnglishBot) {
	fmt.Println(eb.getGreeting())
}
func printGreeting(sb SpanishBot) {
	fmt.Println(sb.getGreeting())
}

GIVES ERROR
*/

/*
SOLUTION: INTERFACES

Here we mean that, any type in this package having method getGreeting() and returns string is a subclass of interface Bot
*/
type Bot interface {
	getGreeting() string
}

func printGreeting(b Bot) {
	fmt.Println(b.getGreeting())
}

// Interface extending another interface
// This means that this needs to have all methods defined in Reader and Writer Interface
type FileSystem interface {
	Reader
	Writer
}

type Reader interface {
	readDataStream(string) []byte
}
type Writer interface {
	writeDataStream([]byte) string
}

/*
EQUIVALENT:
type FileSystem interface {
	readDataStream(string) []byte
	writeDataStream([]byte) string
}
*/

func main() {

	eb := EnglishBot{}
	sb := SpanishBot{}

	printGreeting(eb)
	printGreeting(sb)

}
