# Math Cheatsheet

Count numbers not special in range [l, r] (from Math/Special_Nums_Primes.py)
```python
import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(math.sqrt(r+1))
        isprime = [True]*(n+1)
        isprime[0] = isprime[1] = False

        for i in range(2, int(math.sqrt(n))+1):
            if isprime[i]:
                for j in range(i*2, n+1, i):
                    isprime[j] = False


        special_nums = 0
        for i in range(2, n+1):
            if isprime[i] and l<=i*i<=r:
                special_nums += 1

        return (r-l+1)-special_nums
```

---

## 🗺️ Quick map
- 🔢 Number theory (gcd/lcm, sieve)
- 🎲 Combinatorics (nCk mod p)
- ⚡ Fast exponentiation

## ✅ Study checklist
- [ ] Inverse computation method valid (prime vs non-prime mod)?
- [ ] Sieve bounds and memory okay?
- [ ] Overflow/precision issues (when in other languages) considered?
