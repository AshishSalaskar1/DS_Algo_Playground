# Strings Cheatsheet

KMP (from Strings/KMP/README.md)
```python
s = "sadbutsad"
p = "sad" 
res = get_kmp_array(f"{p}#{s}") 
print(res)

#       0  1  2  3  4  5  6  7  8  9  10 11 12
#       s  a  d  #  s  a  d  b  u  t  s  a  d
#  [-1, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]

class Solution: #KMP ALGO
    def strStr(self, s: str, p: str) -> int:
        ns, np = len(s), len(p)
        kmp_arr = get_kmp_array(f"{p}#{s}")

        for i in range(np, len(kmp_arr)):
            if kmp_arr[i] == np: # why -2*np-1? -2np (one np before # + # + np till i)
                return (i-2*np-1, i-np-1)

        return -1
```

Rolling Hash (from Strings/Rolling_Hash/README.md)
```python
class Hasher:
    def __init__(self, s, base_system, modnum) -> None:
        self.n = len(s)
        self.k = base_system
        self.p = modnum # needs to be prime

        self.rev_hash = [0]*(self.n+1) # only for REVERSE
        self.hash = [0]*(self.n+1) # 1-BASED
        self.pow = [0]*(self.n+1) # 1-BASED

        self.hash[0] = 0
        self.pow[0] = 1
        for i in range(1, self.n+1):
            num = ord(s[i-1])  - ord('a') + 1 # you want to map a:1, b:2 ...

            #h[i] = h[k-1]*k + val(s[i])
            self.hash[i] = ((self.hash[i-1]*self.k) + num ) % self.p # hash(upto i-1) * k + num(s[i])
            
            # just keep on multiplying k to get k^i
            self.pow[i] = (self.pow[i-1]*self.k) % self.p # pow(upto i-1)*i 

        # only for REVERSE
        self.rev_hash[self.n] = 0
        for i in range(self.n-1, -1, -1):
            num = ord(s[i]) + 1
            self.rev_hash[i] = ((self.rev_hash[i+1]*self.k) + num ) % self.p
        
    
    def get_hash(self, l, r): # 0-Indexed
        # hash[r] - ( hash[l-1] * k^(r-l) )
        res =  (self.hash[r+1] - (self.hash[l] * self.pow[r-l+1])) % self.p
        return res % self.p
    
    def get_rev_hash(self, l, r): # hash of [l<-r]
        # hash[l-1] - ( hash[r] * k^(r-l) )
        res =  (self.rev_hash[l] - (self.rev_hash[r+1] * self.pow[r-l+1])) % self.p
        return res % self.p
```

See README for pattern matching, palindrome checks, longest common substring using binary search + hashing.

---

## 🗺️ Quick map
- 🧵 KMP (LPS/PI table)
- 🧮 Rolling hash / double hash
- 🪞 Palindrome and substring hash tricks

## ✅ Study checklist
- [ ] LPS construction off-by-one free?
- [ ] Hash normalization against negatives?
- [ ] Independent moduli/bases for double hash?
- [ ] Compare ranges by O(1) hash correctly?
