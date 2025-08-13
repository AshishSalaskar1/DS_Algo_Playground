# Bit Manipulation Cheatsheet

Patterns
- Counting bits (popcount), set/clear/test kth bit
- Is power of two: x>0 and x&(x-1)==0
- Lowbit: x&-x (Fenwick trick)
- XOR tricks: unique number, swap, missing/duplicate pair patterns

Masks
- Subset iteration: for m in range(1<<n): ...
- For each bit i: (m>>i)&1

Utilities
- Extract last set bit: x & -x
- Turn off last set bit: x & (x-1)

Refs
- Leetcode bits study guide in repo root README

# Bit Manipulation Cheatsheet (verbatim)

XOR from L to R (from Bit Manipulation/XOR_from_L_to_R.py)
```python
def XOR_1_to_n(n):
    if n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    elif n%4 == 3:
        return 0
    return n

def XOR_range(l,r):
    return XOR_1_to_n(l-1) ^ XOR_1_to_n(r)
```

Power set via bitmasking (from Bit Manipulation/Power_set.py)
```python
class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        start, end = 0, (1<<n) # 0 -> 2^n
        res = []
        
        for x in range(start,end):
            cur_res = []
            for i in range(n):
                # check if i'th bit is set or not
                if x&(1<<i) != 0:
                    cur_res.append(arr[i])
            
            res.append(cur_res)

        return res
```

Minimum flips to make a OR b equal to c (from Bit Manipulation/Flip_bits_to_make_AorB_C.py)
```python
class Solution:
    def minFlips2(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(31):
            # i'th bit of c is 1
            if (c >> i) & 1:
                flips += ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0
            # i'th bit of c is 0
            else:
                flips += (a >> i) & 1
                flips += (b >> i) & 1
        return flips
```

Divide two integers without *, /, % (from Bit Manipulation/Divide_numbers.py)
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        sign = 1
        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0):
            sign = -1
        
        num, den = abs(dividend), abs(divisor)
        quotient = 0

        while num >= den:
            power = 0
            while num >= (den<<(power+1)):
                power += 1
            
            quotient += 1<<power
            num -= (den<<power)

        if quotient == (1<<31) and sign==1:
            return (1<<31)-1
        elif quotient == (1<<31) and sign==-1:
            return -1*(1<<31)
        
        return sign*quotient
```

---

## 🗺️ Quick map
- 🧮 Bit twiddling basics
- 🧰 Power-of-two, popcount, submask iteration
- 🧷 Mask tricks for subsets/powerset

## ✅ Study checklist
- [ ] Operator precedence guarded with parentheses?
- [ ] Signed shifts avoided when risky?
- [ ] Indices/bounds safe in bit loops?
