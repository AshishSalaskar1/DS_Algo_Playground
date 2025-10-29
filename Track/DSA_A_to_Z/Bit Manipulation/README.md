# Bit Manipulation Practice
### Reference Formulae

- `MOST IMPORTANT`: You can **NEVER SAY SOME BIT_OPS == 1** | Its **!=0**
    
- General Trends to look out for
    - `AND` always `decreases` the number
    - `OR` always `increases` the number
    - `XOR` helps in `flipping` certain bit ( XORing that bit with 1<<i -> flips bit at i)
- COMMON OPERATIONS
    - `i` Bit Ops
        - **SET Bit**: `n | (1<<i)`
        - **UNSET Bit**: `n & ~(1<<i)`
        - **Check if bit it set**: `n & (1<<i)` == 0 then UNSET, if 1 then SET
        - **Toggle Bit**: `n ^ (1<<i)`
    - **Negative of number**: `-n` = `flip_bits(n)+1` # 1s compliment + 1
        - Flip bits: `not n` = `~n`
        - 💡 If LEFTMOST_BIT is 1 -> then the number is NEGATIVE
    - **Even/Odd**: `n&1 == 0` 0(even) | 1(odd) # Check if LSB is set or not
    - **Power of 2**: `n & (n-1) == 0` 0(YES) | 1(NO) 💡 EXCEPT for 0 doesnt work
        - Logic: If `n` is power of 2, it will only have 1 set bit. And `n-1` will have all bits after that set bit as 1. So `n & n-1` == 0 if there was only set bit
        - Ex: 8=1000, 7=0111, 1000 & 0111 = 0
    - **Divide/Multiply**: 
        - Divide by 2<sup>i</sup> = `n >> i` # LEFT SHIT
        - Multiple by 2<sup>i</sup> = `n << i` # RIGHT SHIFT
    - **Remove last/right most set bit**: `n -= (n & -i)`
    - **Set first k bits**: `mask = (1 << k) - 1`
