package main

import "fmt"

type dob struct {
	day   int
	month int
	year  int
}

type personType struct {
	name   string
	age    int
	height float32
	dob    // equivalent of saying dob dob
}

// RECEIVER FUNCTIONS (Consider this as class methods)
func (p personType) print() string {
	return p.name + fmt.Sprintf("%d", p.age) + fmt.Sprintf("%.2f", p.height)
}

// Here p is passedByValue -> So you cant update it
func (p personType) updateName(newName string) {
	p.name = newName
}

// Update using Pointer
func (pointerToPerson *personType) udpateNamePtr(newName string) {
	// set the value of person.nam
	(*pointerToPerson).name = newName
}

func main() {
	fmt.Println("HELLO WORLD...")

	p := personType{name: "ashish", age: 20, height: 12}
	p.updateName("harry")
	fmt.Printf("%v\n", p) // {name: "ashish", age:20, height: 12}

	personPointer := &p
	personPointer.udpateNamePtr("harry")
	fmt.Printf("%+v\n", p) // {name: "ashish", age:20, height: 12}

	p.udpateNamePtr("hermoine")
	fmt.Printf("%+v\n", p) // {name: "ashish", age:20, height: 12}
}
