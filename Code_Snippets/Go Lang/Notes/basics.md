### Constants
- You cant use short assigning syntax
- In go your constants must get resovled during compile time -> you can assign constant variable and compute its value entirely during runtime


### Printing
- `fmt.PrintLn()`
- `fmt.Printf("this is some %v", "some_value)`
    - %v -> any value
    - %d -> int
    - %s -> string
    - %f or %.2f -> float with precisions if needed
- `fmt.Sprintf(....)` -> form the print string but assign back to a variable

### IF CONDITION
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

### Functions
- Syntax: 
  1. `func test_fn(x int, y string) float`
     - x,y are inputs and function returns float type
  2. `func test_fn(x int, y string) (float, int)`
      - x,y are inputs and function returns 2 vars -> float and int type

- Named Return Values
```go
func add(x int, y int) (float a, float b){
    // It automatically initialuses

    return
}

```