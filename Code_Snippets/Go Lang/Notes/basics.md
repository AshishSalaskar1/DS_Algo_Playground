##### Interesting things to note

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

##### Constants

- You cant use short assigning syntax
- In go your constants must get resovled during compile time -> you can assign constant variable and compute its value entirely during runtime

##### Printing

- `fmt.PrintLn()`
- `fmt.Printf("this is some %v", some_value)`
  - %v -> any value
  - %d -> int
  - %s -> string
  - %f or %.2f -> float with precisions if needed
- `fmt.Sprintf(....)` -> form the print string but assign back to a variable

##### IF CONDITION

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

##### Functions

- Syntax:

  1. `func test_fn(x int, y string) float`
     - x,y are inputs and function returns float type
  2. `func test_fn(x int, y string) (float, int)`
     - x,y are inputs and function returns 2 vars -> float and int type
- Function arguments in Go are **`passed-by-value`**
- Named Return Values

```go
func add(x int, y int) (float a, float b){
    // It automatically initialises a and b with default zeroed values and returns them at last even if you just write return
    return
}

```

###### For Conditionals

```go
for x:=0; x<=10; x++ {
    fmt.Println("The value of x is %v", x)
}

// only check condition is mandatory in the for loop, rest init and post can be written inside like an while loop in case its needed -> but here scope of the variables need to be considered for incrementing and checking the condition
x:=0
for x<=10 {
    fmt.Println("The value of x is %v", x)
    x++
}

```

###### Pointers

* `&var_name` -> get pointer address
* `*pointer_variabl`e -> get value at address stored in pointer_variable
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
  - In Go, it’s okay to return a
    pointer to a variable that’s local to a function. Even though that variable is
    no longer in scope, as long as you still have the pointer, Go will ensure you
    can still access the value.

###### Useful Functions

* `strings.NewReplacer` -> string replace
* `reflect.TypeOf` -> returns data type of the object
* `bufio.NewReader(os.Stdin)` -> `input, error = reader.ReadString('\n')`: read everything user has typed until the separator that u pass, here its \n or newline
* `strconv.ParseFloat()` -> string or integer to float
