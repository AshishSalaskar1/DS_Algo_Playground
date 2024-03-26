#### ### Basic Concepts

- **Basics**    
  
  1. **XOR**:     
     
     - (0,0) and (1,1) = 0, (0,1) and (1,0) = 1 
     
     - Even number of 1s -> 0, Odd number of 1s -> 1
  
  2. AND: 0 and X = 0, 1 and 1 = 1
  
  3. OR: 1 or X = 1
  
  4. Right Shift: >> ---> divided by 2 | 13>>i = 13/2^i
  
  5. Left Shift: >> --> multiplied by 2 | 13>>i = 13 * 2^i

- **Compliment** -> How to make `x` -> `-x`
  
  1. Invert bits in `x`
  
  2. Add 1 to `x` 
  
  **Important Property**: `X` & `-X` = Last set bit of X (value of rightmost bit)

- 

- **Basic Problems**
  
  1. Even or odd: 
     
     - Number is even if its last bit is not set
     
     - If (num & 1) == 0 -> EVEN
  
  2. Extract `i`th bit
     
     - `x` AND `1<<i`  == 0 then UNSET else SET
  
  3- Set and Unset `i`th bit
     
     - Set:  `x` OR (`1<<i`)
     
     - Unset: `x` AND inverse(`1<<i`)

#### References

- Aryan Mittal Playlist: [Complete BIT MANIPULATION Intuition Building by Aryan - YouTube](https://www.youtube.com/playlist?list=PLEL7R4Pm6EmCLLeXClTK9TalPIrfE7XIe)

- Striver: [Bit Manipulation Playlist | Language Independent Course - YouTube](https://www.youtube.com/playlist?list=PLgUwDviBIf0rnqh8QsJaHyIX7KUiaPUv7)


