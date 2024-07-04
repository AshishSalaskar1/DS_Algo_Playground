#### Basics

- **Module structure**
  
  - `main` vs `other` packages
    
    - `main` package consists of code which is executed when you do `go run`. You can have multiple files belonging to main package but atleast one needs to have a `main()` method which acts like a starting point of execution
    
    - Packages names other than main are considered util packages, which are being used by some other package or main package somewhere else 
  
  - Generally, you have a`main.go` file which has function`main()` which acts like starting point of your application and is mostly stored in an`cmd` folder. Outside the`cmd `folder you have all your modules/import files.
  
  - `go mod init mod_name` -> consider this as your package.json, it contains the name of your project/package and the go version which you want to use
  
  - **Structure of projects**
    
    - `go.mod` -> contains mod "modname"
    - `cmd/main/main.go` -> you import in your` main.go` as "modname/package_name"
    - `package1/package1.go`,`package2/package2.go`
  
  - Importing external modules
    
    - `go mod tidy` -> Downloads all packages already imported in your codes
    
    - `go get package_name/path` -> Individually downoad each module that you want to import

- **Types**
  
  - **Pass by VALUE or REFERENCE**
    
    - **Passed by Value:** int, float, string, bool, structs
    
    - **Passed by Reference**: slices, maps, channels, pointers, functions
  
  - **Type conversions**: int(), float64(), float32()
    
    - `dest_data_type(src_variable)`<- Assuming src_var can be auto converted to dest_data_type
    
    - **Float -> string**
      
      ```go
      x := 12.23
      // FormatFloat(var, 'float', 2 (precision), 64 (base 64)
      xStr := strconv.FormatFloat(x, 'f', 2, 64)
      ```
      
      xStr2 := fmt.Sprintf("%.2f", x)
      
      ```
      
      ```
    
    - **Int -> String**
      
      ```go
      x := 12
      
      xStr := strconv.Itoa(x, 'f', 2, 64)
      xStr2 := fmt.Sprintf("%d", x)
      ```

- **Variable Basics**
  
  ```go
  var ash int
  ash = 12
  ash := 12 // shorthand but works only within functions
  ```

- **String**
  
  - Types
    
    - **byte**: uint8 char representation
    - **string**: immutable sequence of chars (UTF-8 and logical sequence of runes). Since strings are immutable they can also share memory locations (hello, hello_world, he may share memory blocks for chars)
    - **rune**: int32 char representation, surrounded by single-quote (backticks are used for raw strings where special chars dont loose meaning)
  
  - **Strings are passed by reference**
  
  - Strings are immutable like python, but can be re-assigned
  
  - **String Functions**
    
    - ```go
      s := "ashish"
      
      strings.Contains(s, "a") // true
      strings.HasPrefix(s, "ash") // true
      
      strings.Index(s, "h") 
      strings.Index("ish")
      
      upperS = s.ToUpper() 
      lowerS = s.ToLower()
      
      // Split and Join
      s := "this is an big splitter word"
      
      splitStrings := strings.Split(s, "i") // this returns a slice split with "i" 
      fmt.Println(splitStrings)
      
      fmt.Println(strings.Join(splitStrings,"X")) //returns string: same as "X".join(arr) in python
      ```
  
  - **Special Types**: bool, error, pointers
  
  - **Default Initialization**
    
    - numerical types -`0`
    - bool -`false`
    - string -`""`
    - All others -`nil`
    - aggregate types - each member is set to 0
  
  - **Constants**
    
    - Only numbers, strings and booleans can be constant (Immutable)
    
    - It can be literal or compile-time (You cant set constants on run-time dynamically)
      
      ```go
      const a = 12
      const (
          c1 = 12
          c2 = "1234"
      )
      ```

---

#### Interesting things to note

* **Rune Literals**: rune literals are written with single quotation marks. Its a datatype used to store Unicode Characters (usually only one char/symbol)

* **Go Naming rules**:
  
  * If the name of a variable, function, or type begins with a capital
    letter,`it is considered exported` and can be accessed from packages
    outside the current one. And`its considered unexported` and can be used only in the current file in case its name starts with an lowercase character
  * Generally people use CamelCase in GoLang

* **Go Commands**
  
  * `go build file_name`: build execuutable from go files which can then be directly executed
  * `go fmt file_name`: format the code file
  * `go run file_name`: directly execute the go file without building an executable

* **PACKAGES**
  
  * Everything in GO must belong to some package. Every package has a main() function
  
  * Package import cant be cyclical.
  
  * If the name of a variable, function, or type begins with a capital
    letter ,`it is considered exported` and can be accessed from packages
    outside the current one. And`its considered unexported` and can be used only in the current file in case its name starts with an lowercase characte
  
  * You can have variables/constants/functions/structs defined at package level (you cant use shorthand using :=). These get initialized before the main() functions. You can use `func init()` as constructor for initializing package level items

* **Import path vs name**: What you write in import clause is the package name, n what you use in the code is the package name. Both can be different also (same in case of common packages)

* `NULL `is represented in GO as `nil`

* `defer` -> defer keyword indicates to run a function only after outer function completes execution
  
  * ```go
    func main() {
       defer fmt.Println("World")
       fmt.Println("Hello")
    }
    
    // OUTPUT: hello -> world
    ```

---

#### Constants

- You cant use short assigning syntax
- In go your constants must get resovled during compile time -> you can assign constant variable and compute its value entirely during runtime

#### Printing

- `fmt.PrintLn()`
- `fmt.Printf("this is some %v", some_value)`
  - %v -> any value
  - %d -> int
  - %s -> string
  - %f or %.2f -> float with precisions if needed
  - %T -> type of the variable
- `fmt.Sprintf(....)` -> form the print string but assign back to a variable

---

#### IF CONDITION

Syntax

```go
x := get_value(12)
if x > 12 {
    fmt.PrintLn("TRUE")
}

// INIT + Condition
// x can only be used within scope of the if condition
if x := get_value(12); x>12 {
    fmt.PrintLn("TRUE")
}
```

- **SWITCH**
  
  - You dont need a break statement
  
  ```go
  switch x := getValue() ; x {
      case 0,1,2:
          fmt.Println("some")
      case 5,6,7:
          // no logic
      default: 
          fmt.Println("some")
  }
  
  x := 12
  switch {
      case x<12:
          fmt.Println("some")
      case x > 56:
          // no logic
      default: 
          fmt.Println("some")
  }
  ```

---

#### Functions

- Syntax:
  
  1. `func test_fn(x int, y string) float`
     - x,y are inputs and function returns float type
  2. `func test_fn(x int, y string) (float, int)`
     - x,y are inputs and function returns 2 vars -> float and int type

- Function arguments in Go are **`passed-by-value`**

- **Named Return Values**

```go
func add(x int, y int) (float a, float b){
    // It automatically initialises a and b with default zeroed values and returns them at last even if you just write return
    return
}
```

- **Variadic Functions**

```go
func add(nums ...int) (sum int){
    for _, val := range nums {
        sum += val
    }
    return sum
}

func main() {
  fmt.Println(add(1,2,3,4))
}
```

---

#### For Conditionals

```go
for x:=0; x<=10; x++ {
    fmt.Println("The value of x is %v", x)
}

// only check condition is mandatory in the for loop, 
//rest init and post can be written inside like an while loop in case its needed -> but here scope of the variables need to be considered for incrementing and checking the condition
x:=0
for x<=10 {
    fmt.Println("The value of x is %v", x)
    x++
}

// list
arr := []int{1,2,3,4,5}

for index, val := range arr {
    fmt.Println(index, val)
}
```

- **Continue**    
  
  - To continue the outer_loop you need a label set and then do `continue outer_label` (just continue wont work)
    
    ```go
    func main() {
        arr1 := []int{1, 2, 7}
        arr2 := []int{1, 2, 3, 4, 5}
    
        outer:
            for val := range arr1 {
                for item := range arr2 {
                    println("Checking ", item)
                    if val == item {
                        fmt.Printf("val %d found in second arr2\n", val)
                        continue outer
                    }
                }
                fmt.Printf("Element %d not found in arr2", val)
            }
    
    }
    ```

---

#### Pointers

* `&var_name` -> get pointer address

* `*pointer_variable` -> get value at address stored in pointer_variable

* Data type of pointers -> *float32, *int....

* ```go
  func test_pointers() {
      a, b := 12, "ashish"
      aPtr, bPtr := &a, &b // pointers to a, b
      fmt.Println(reflect.TypeOf(aPtr)) // *int
      fmt.Println(reflect.TypeOf(bPtr)) // *string
  
      fmt.Println(aPtr, *aPtr) // 0xc20070, 12
      fmt.Println(bPtr, *bPtr) // 0xc14270, ashish
  
      // change value at ptr
      *bPtr = "hello_test"
      fmt.Println(bPtr, *bPtr) // 0xc00009e230, hello_test
  }
  ```
- **Returning pointers from functions:**
  
  - In Go, you can also return a pointer to a variable that’s local to a function. Even though that variable is no longer in scope, as long as you still have the pointer, Go will ensure you can still access the value.

---

### Data Structures

#### Arrays

* Syntax:`var arrName [n]data_type`
* Go arrays are fixed in size and size is fixed when they are being declared. Solution -> use`SLICES`
* **Passed by copy/value**
* **Arrays are mostly use as some type of constants**
* len() function is available

```go
func main() {
  var arr [3]int
  fmt.Println(arr)

  // Array literals
  arr1 := [3]int{1,2,3}
  fmt.Println(arr1)

  arr2 = arr1 // arr2 stores a copy of arr1

  // iterating using for range loop
  for idx, value := range arr1 {
      fmt.Println(idx, value)
  }
}
```

#### Slices

- Syntax:`var mySlice []data_type` ->`arr = make([]data_type, size)` OR`mySlice := make([]data_type, size)`
- **Array**: `[n]date_type `| Slice: `[]data_type`
- Same as arrays but size isnt specified while declaring
- **Slices are passed by reference**
- `make()`-> generally you cant read from nil data structures, so make creates the memory for that and initializes

```go
func main() {
  arr := make([]int, 2)
  fmt.Println(arr)

  arr1 := []int{1,2,3}
  fmt.Println(arr1)

  arr2 = arr1 // both point to the same address

  // append returns new object 
  arr1 = append(arr1, 123)
  fmt.Println(arr1)

  // arrays vs slice declaration
  array := []int{1, 2, 3}
  slice := [...]int{1, 2, 3}
}
```

#### Maps

- Syntax:`myMap :=  make(map[key_type]value_type)` or`myMap := map[key_type]value_type{}`
- Maps are unordered collection of key,value pairs. So when printed in a for range loop, the order printed maybe different from what you have entered the keys.
- If key not present in map, it returns empty nil/0
- **Passed by reference**

```go
func main() {
  myMap := map[string]int{} //cant be used
  myMap := make(map[string]int)
  myMap["ashish"]=1
  myMap["hello"]=2
  myMap["zero"=0]
  fmt.Println(myMap) // map[ashish:1 hello:2]

  // accesing values
  a1 := myMap["zero"] //0, present but val=0
  a2 := myMap["ZERO"] //0, not_present so 0
  a3, ok = myMap["zero"] // 0, true
  a4, ok = myMap["ZERO"] // 0, false

  // deleting an entry
  delete(myMap, "ashish")
  fmt.Println(myMap) // map[hello:2]

  // map literals
  var m = map[string]int{
      "ash":1, "ben": 2  
  }
}

func usingOk(){
    // print the values for keys u want to check
    var m = map[string]int{
        "ash": 1,
        "ben": 2,
    }

    reqKeys := []string{"ash", "ben", "some"}
    for _, key := range reqKeys { // iterate through splice created
        if value, ok := m[key]; ok { // set 2 temp vars val, ok -> if ok=True {} else {}
            fmt.Printf("Key %v was found in map with value %v\n", key, value)
        } else {
            fmt.Printf("Key %v was not found in map \n", key)
        }
    }


}
```

#### Structs

* Made up of multiple data types

```go
func main() {
  var myStruct struct{
      name string
      age int
      height float32
  }

  myStruct.name = "ashish"
  fmt.Println(myStruct.name, myStruct.age, myStruct.height)
}
```

- **Struct Tags**

- In Go, the strings within backticks in a struct definition are known as struct tags. These tags provide metadata about the struct fields, often used for purposes such as serialization, validation, or ORM mapping.

```go
package main

type request struct {
  URL         string        `json:"url"`
  CustomShort string        `json:"short"`
  Expiry      time.Duration `json:"expiry"`
}

type response struct {
  URL             string        `json:"url"`
  CustomShort     string        `json:"short"`
  Expiry          time.Duration `json:"expiry"`
  XRateRemaining  int           `json:"rate_limit"`
}
```

- In the below example, the struct tags are used for JSON serialization. Here's a breakdown of what each tag means:

-  **`json:"url"`**: This tag specifies that the `URL` field in the struct should be serialized to/from JSON with the key `url`.

- **`json:"short"`**: This tag specifies that the `CustomShort` field in the struct should be serialized to/from JSON with the key `short`.

- **`json:"expiry"`**: This tag specifies that the `Expiry` field in the struct should be serialized to/from JSON with the key `expiry`.

- **`json:"rate_limit"`**: This tag specifies that the `XRateRemaining` field in the struct should be serialized to/from JSON with the key `rate_limit`.

- These tags are used by the JSON marshaling and unmarshaling functions in Go's `encoding/json` package. When you convert a struct to JSON (marshaling) or from JSON (unmarshaling), these tags help to map struct fields to JSON object keys and vice versa.

#### **Type Definitions**

- Define your own Custom types. Generally done on package level, so that you can use your new type in the entire code rather than in function scope only.

```go
type dob struct {
    day int
    month int
    year int
}


type personType struct {
    name string
    age int
    height float32
    dob // equivalent of saying dob dob
}

// It can be a primitive datatype as well
type deckOfCards []string // deck = ["Spade 1", "Ace 2"....]

// RECEIVER FUNCTIONS (Consider this as class methods)
func (p personType) print() string {
    return p.name + fmt.Sprintf("%d", p.age) + fmt.Sprintf("%.2f", p.height)
}

// Here p is passedByValue -> So you cant update it
func (p personType) udpateName(newName str) {
    p.name = newName
}

// Update using Pointer
func (pointerToPerson *personType) udpateNamePtr(newName str) {
    // set the value of person.nam
    (*pointerToPerson).name = newName
}

func testUpdateName() {

    p := personType{name: "ashish", age:20, height: 12}
    p.updateName("harry") 
    fmt.Printf("%+v",p) // {name: "ashish", age:20, height: 12}

    personPointer := &p
    personPointer.udpateNamePtr("harry")
    fmt.Printf("%+v",p) // {name: "harry", age:20, height: 12}

    // Go auto converts receivers to its object ptr even if not specified
    // U passed object, but receiver expects ptr (IT AUTO CONVERTS)
    p.udpateNamePtr("hermoine")
    fmt.Printf("%+v",p) // {name: "hermoine", age:20, height: 12}

}

func main() {
    var myPerson personType
    fmt.Println(myPerson.name, myPerson.age, myPerson.height)

    // using struct literals
    myPerson2 := personType{name: "ashish", age:20, height: 12}
    myPerson2 := personType{"ashish",20,12} // pass by position

    fmt.Println(myPerson2) // ashish 20 12
    fmt.Printf("%+v",myPerson2) // {name: ashish, age: 20, height: 12}

    // Calling receiver functions
    myPerson2.print() // ashish 20 12
}
```

#### Interfaces

- Interfaces are `reverse implicit` in Go. 
  
  - In other languages, you define interfaces and then each class implements it
  
  - Here, you define interface and automatically all structs that meet this interface definition are considered to have implemented this interface

```go
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

func main() {

    eb := EnglishBot{}
    sb := SpanishBot{}

    printGreeting(eb)
    printGreeting(sb)

}
```

- **Interfaces can extend other interfaces also**
  
  ```go
  package main
  
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
  ```

---

### Useful Functions

* `strings.NewReplacer` -> string replace
* `reflect.TypeOf` -> returns data type of the object
* `bufio.NewReader(os.Stdin)` ->`input, error = reader.ReadString('\n')`: read everything user has typed until the separator that u pass, here its \n or newline
* `strconv.ParseFloat()` -> string or integer to float

### Some Examples

- **Read words from input, and sort based on frequency**
  
  - `sort.data_structure(val, custom_comparator)`
    
    ```go
    func main() {
        type keyValue struct {
            key string
            val int
        }
    
        reader := bufio.NewReader(os.Stdin)
        words := make(map[string]int)
        var pairs []keyValue // slice of keyValue type
    
        fmt.Printf("Enter you sentence: ")
        input, _ := reader.ReadString('\n') // delimit based on new line (ITS A RUNE - SINGLE QUOTES)
    
        for _, scannedWord := range strings.Split(input, " ") { // read all words and add to map
            words[scannedWord]++
        }
    
        // add key,vals to pairs
        for k, v := range words {
            pairs = append(pairs, keyValue{k, v})
        }
    
        // sort by count in decreasing
        sort.Slice(pairs, func(i, j int) bool { // i,j are indexes of item in slice
            return pairs[i].val > pairs[j].val
        })
        fmt.Println("Sorted in decreasing order: ", pairs)
    
    }
    ```

### Concurrency

#### Wait Groups

- Make sure number of times `add()` and `done()` called are same. This may cause a deadlock

- Aways pass `wg` as reference as pointer (Not by value)

- ```go
  package main
  
  import (
      "fmt"
      "log"
      "net/http"
      "sync"
  )
  
  var statusCodeResults = []string{}
  
  func checkSite(site_url string, wg *sync.WaitGroup, mutex *sync.Mutex){} {
    // wg.Done only after checkSite completes execution
    defer wg.Done()
    res, err := http.Get(site_url)
    if err != nil{
        log.Fatal(err)
    }
  
    fmt.Printf("%v --> %v \n", site_url, res.StatusCode)
  
    // use mutex to lock in case multiple goroutines try to access same memory address
    mutex.Lock()
    statusCodeResults = append(statusCodeResults,site_url)
    mutex.Unlock()
  
  }
  
  func main() {
    sites := []string{
       "https://google.com",
       "https://go.dev",
       "https://github.com",
    }
  
    fmt.Println("EXECUTION STARTS")
  
    var wg sync.WaitGroup // pointer
    var mutex sync.Mutex // pointer
  
    for _, site_url := range sites {
        go checkSite(site_url, &wg, &mutex)
        wg.Add(1) //add one go routine to wait group
    }
  
    wg.Wait()
    fmt.Println("FINAL LIST", statusCodeResults)
  
  }
  ```

#### Channels

| Youtube Video Tutorial: https://youtu.be/qyM8Pi1KiiM

**Unbuffered Channels**

- When you create an unbuffered channel, it has a **capacity of zero**. This means that every **send operation** on the channel **blocks** until **another goroutine is ready** to receive the value.

- Likewise, every **receive operation** **blocks** until **another goroutine is ready** to send a value.

- Unbuffered channels ensure that the sender and receiver goroutines are **synchronized**

- <u>Example</u>: *In this example, the main goroutine then blocks at the line* `*<-ch*`*, waiting for a value to be received from the channel. Once the value is received, it is printed to the console. So as soon as one value is pushed into the channel it terminates the program*

```go
/*
Blog: https://medium.com/goturkiye/concurrency-in-go-channels-and-waitgroups-25dd43064d1
*/

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

func main() {
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
```

- **Buffered Channels**

- Buffered channels, on the other hand, have a **specified capacity greater than zero**. This means that they can hold a **certain number of values** before **blocking send operations**. 

- Buffered channels decouple the sender and receiver, allowing for asynchronous communication.

- <u>Example</u>: *In this example, we receive the values from the channel in the order they were sent. Since the channel has a buffer, it doesn't block the send operations.*
  
  ```go
  package main
  
  import "fmt"
  
  func main() {
        ch := make(chan int, 2) // Creating a buffered channel with a capacity of 2
  
        ch <- 1 // Sending the value 1 to the channel
        ch <- 2 // Sending the value 2 to the channel
  
        x := <-ch // Receiving the value from the channel
        fmt.Println(x) // Output: 1
  
        y := <-ch // Receiving the value from the channel
        fmt.Println(y) // Output: 2
  }
  ```
