#### Basics

- **Module structure**
  - `go mod init mod_name` -> consider this as your package.json, it contains the name of your project/package and the go version which you want to use
  - Generally, you have a `main.go` file which has function `main()` which acts like starting point of your application and is mostly stored in an `cmd` folder. Outside the `cmd `folder you have all your modules/import files
  - **Structure of projects**
    - `go.mod` -> contains mod "modname"
    - `cmd/main/main.go` -> you import in your` main.go` as "modname/package_name"
    - `package1/package1.go`, `package2/package2.go`
- **Types**
  - **Type conversions**: int(), float64(), float32()
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

      - numerical types - `0`
      - bool - `false`
      - string - `""`
      - All others - `nil`
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
    letter, `it is considered exported` and can be accessed from packages
    outside the current one. And `its considered unexported` and can be used only in the current file in case its name starts with an lowercase character
  * Generally people use CamelCase in GoLang
* **Go Commands**

  * `go build file_name`: build execuutable from go files which can then be directly executed
  * `go fmt file_name`: format the code file
  * `go run file_name`: directly execute the go file without building an executable
* **All functions and methods start with Capital letter**
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
  -
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

* Syntax: `var arrName [n]data_type`
* Go arrays are fixed in size and size is fixed when they are being declared. Solution -> use `SLICES`

```go
func main() {
  var arr [3]int
  fmt.Println(arr)

  // Array literals
  arr1 := [3]int{1,2,3}
  fmt.Println(arr1)

  // iterating using for range loop
  for idx, value := range arr1 {
      fmt.Println(idx, value)
  }
}
```

#### Slices

- Syntax: `var mySlice []data_type` -> `arr = make([]data_type, size)` OR `mySlice := make([]data_type, size)`
- Same as arrays but size isnt specified while declaring

```go
func main() {
  arr := make([]int, 2)
  fmt.Println(arr)
  
  arr1 := []int{1,2,3}
  fmt.Println(arr1)
  
  // append returns new object 
  arr1 = append(arr1, 123)
  fmt.Println(arr1)
}
```

#### Maps

- Syntax: `myMap :=  make(map[key_type]value_type)` or `myMap := map[key_type]value_type{}`
- Maps are unordered collection of key,value pairs. So when printed in a for range loop, the order printed maybe different from what you have entered the keys as

```go
func main() {
  myMap := map[string]int{}
  myMap["ashish"]=1
  myMap["hello"]=2
  fmt.Println(myMap) // map[ashish:1 hello:2]
  
  // deleting an entry
  delete(myMap, "ashish")
  fmt.Println(myMap) // map[hello:2]
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

**Type Definitions**

- Define your own Custom types. Generally done on package level, so that you can use your new type in the entire code rather than in function scope only.

```go
type personType struct {
    name string
    age int
    height float32
}

func main() {
    var myPerson personType
    fmt.Println(myPerson.name, myPerson.age, myPerson.height)
  
    // using struct literals
    myPerson2 := personType{name: "ashish", age:20, height: 12}
    fmt.Println(myPerson2)
}
```

---



### Useful Functions

* `strings.NewReplacer` -> string replace
* `reflect.TypeOf` -> returns data type of the object
* `bufio.NewReader(os.Stdin)` -> `input, error = reader.ReadString('\n')`: read everything user has typed until the separator that u pass, here its \n or newline
* `strconv.ParseFloat()` -> string or integer to float
