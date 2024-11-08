# Rolling Hashes

Time Complexity:
- Hash Creation: O(n)
- Subsequent queries are almost O(1)

💡 PRIME IDEA: Can you somehow represent strings as a number => N then hash it for checking



# Intuition Behind Algo

## Representation of strings as number
- Assume you have a `Base-K` number system. (where k>26)
- You will replace a=1,b=2... and then place get their value by using normal number system logic

Example:
- k=31
- s=abc


abc = [1 x 31<sup>2</sup>] + [2 x 31<sup>1</sup>] + [3 x31<sup>0</sup>] = 961 + 62 + 3 = 1026<br><br>


=> HASH(abc) = 1026

**Note**: 
- Since the final val can grow extremely huge => Use a number for mod (10^9 +7)
- Best if `k` and `mod` are both prime numbers

## Hashes of substring
- Lets say you have a string `S` you also need to find the hashes of `substrings` of S in Linear time

### 1. Pre-Processing
**Use Prefix Sum Equivalent**


0 1 2 3 4 4 <br>
a b c d e f<br>

(* Here, a means val(a) = ord(a)+1 = 1 *)

hash(0) = a      = a ( because ak<sup>0</sup> = a) <br>
hash(1) = ab     = ak<sup></sup>  + b<br>
hash(2) = abc    = ak<sup>2</sup> + bk  + c<br>
hash(3) = abcd   = ak<sup>3</sup> + bk<sup>2</sup> + ck  + d<br>
hash(4) = abcde  = ak<sup>4</sup> + bk<sup>3</sup> + ck<sup>2</sup> + dk  + e<br>
hash(5) = abcdef = ak<sup>5</sup> + bk<sup>4</sup> + ck<sup>3</sup> + dk<sup>2</sup> + ek + f<br><br>

**Observation**: `hash[i] = (hash[i-1] * k) + val(s[i]) `
- So we build this just like we build prefix sum and keep on storing


### 2. Finding hashes of substrings

HASH(2,4) = HASH(cde) = ck<sup>2</sup> + dk + e

HASH(4) = ak<sup>4</sup> + bk<sup>3</sup> + c<sup>2</sup> + dk  + e <br>
HASH(1) = ak  + b <br>

- Till 1, has was `ak+b`
- Now from `l-1` (1) => `r`(4) you kept on multiplying `k` (This multiplication is extra since here it was hash from 0->i)
- To remove this extra `k` multiply => **`HASH(l-1) * k^(l-r+1)`** (Basically its k^(number of elements in between l->r)) 

HASH(4) = ak<sup>4</sup> + bk<sup>3</sup> + ck<sup>2</sup> + dk  + e<br>
HASH(1) * k<sup>3</sup> = ak<sup>4</sup>  + bk<sup>3</sup><br>

HASH(4) - HASH(1) = (ak<sup>4</sup> + bk<sup>3</sup> + ck<sup>2</sup> + dk  + e) - ( ak<sup>4</sup>  + bk<sup>3</sup>)
                  = ck<sup>2</sup> + dk  + e<br>

### FINAL FORMULAE ⚡💀

``0-based indexing``<br>
1. **HASH[i] = (HASH[i-1] \* K) + val(s[i])**
2. **HASH[l,r] = HASH[r] - HASH[l-1] \* K<sup>(r-l+1)</sup>**
3. **REV_HASH[l,r] = HASH[l-1] - HASH[r] \* K<sup>(r-l+1)</sup>**<br>


``1-based indexing`` <- Actually Used<br>
1. **HASH[i] = (HASH[i-1] \* K) + val(s[i-1])**
2. **HASH[l,r] = HASH[r+1] - HASH[l] \* K<sup>(r-l+1)</sup>**
3. **REV_HASH[l,r] = HASH[l] - HASH[r+1] \* K<sup>(r-l+1)</sup>**
(This is Considering 1-based indexing)


#  Implementation

- While precomputing  we calculate 2 things
     1. `hash` -> Normal hash value for [0 -> i]
     2. `rev_hash` -> Hash value for [i <- n+1]
     3. `pow` -> simple K<sup>i</sup>
        - We also calculate this since we may need K<sup>0</sup> -> K<sup>n</sup> (for our range based calculation)
- **Here out precomputes are 1-based, String is 0 based**
```py
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
            num = ord(s[i-1]) + 1 # you want to map a:1, b:2 ...

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


s = "abcabc"
print(s)
hsh = Hasher(s, 31, (10**8)+7)

print(hsh.get_hash(0,2)) # |abc|abc => 97347
print(hsh.get_hash(1,3)) # a|bca|bc => 98337
print(hsh.get_hash(3,5)) # abc|abc| => 97347


s = "racecar"
print(s)
hsh = Hasher(s, 31, (10**8) + 7)

forward_hash = hsh.get_hash(0, len(s) - 1)
reverse_hash = hsh.get_rev_hash(0, len(s) - 1)

print("Forward Hash:", forward_hash)
print("Reverse Hash:", reverse_hash)
```

## FINDING PATTERNS
```py
def find_pattern(s, p):
    ns, np = len(s), len(p)

    shash = Hasher(s, 31, (10**8)+7)
    phash = Hasher(p, 31, (10**8)+7)

    pat_hash_val = phash.get_hash(0,np-1) #  O(1)

    res = []
    for i in range(0, ns-np+1):
        cur_hash = shash.get_hash(i,i+np-1) # O(1)
        if cur_hash == pat_hash_val: # O(1)
            res.append( (i,i+np-1) )
    
    return res


s = "sadbutsad"
p = "sad" 

print(find_pattern(s,p))
        
```

## CHECK PALINDROME
- For any string `S` we want to find if its palindrome: `h.get_hash(0,len(s))` == `h.get_rev_hash(0,len(S))`
- Lets say you want to check if particular substring is palindrome: `h.get_hash(i,j)` == `h.get_rev_hash(i,j)`

## Double Hashing
💡 **Use Double Hashing whenever you are dealing with substrings, possibilities**. In case of linear traversal then its not needed

- We use a `base-k` number system and then a `modprime` number to not let values go too high
- But, there maybe a case where Different strings can give same hash value for a `base-k` + `modprime` combination (VERY VERY LESS CHANCES THOUGH)

💡**Solution: Use 2 hashers**<br>
- Here you will have 2 hashers, `h1` and `h2` having same string `s` but different `base-k` + `modprime` values
- This will return a tuple of hash_values when called, You will compare tuples now
  
**Reasoning why this works**: Even if `h1` gave same hash for 2 different strings then we are sure that `h2` will give different hash values. And since you compare (h1.hash, h2.hash) together it will not be equal
```py
class DoubleHasher:
    def __init__(self, s) -> None:
        self.s = s
        self.h1 = Hasher(s, 31, (10**8)+7)
        self.h2 = Hasher(s, 47, (10**8)+21)
    
    def get_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_hash(l,r),
             self.h1.get_hash(l,r)
        )
    
    def get_rev_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_rev_hash(l,r),
             self.h1.get_rev_hash(l,r)
        )

s = "racecar"
print("DOUBLE HASH", s)
hsh = DoubleHasher(s)

forward_hash = hsh.get_hash(0, len(s) - 1)
reverse_hash = hsh.get_rev_hash(0, len(s) - 1)

print("Forward Hash:", forward_hash)
print("Reverse Hash:", reverse_hash)

```


# PROBLEMS
☀️ Wherever you see SUBSTRING then you can use hashes + some sort of BS (Hard for Sub-Sequences)

## Binary Search + Rolling Hashing
- Use binary search on answers concept + rolling hash to calculate some logic

### Longest Common Substring
💡 Can be easily done using DP in O(n<sup>2</sup>). But who needs easier solutions :P

- s1 = "ashishsomeashish"
- s2 = "some"
<br>

- Here, we know that at max the LCS can be of size `min(n1,n2)`
1. So consider lo=0, hi=min(n1,n2)
2. generate hashes for all subtrings of size `mid` from both s1 and s2 (This is done in O(n) time since we have range hashes already computed)
3. If any hashes generated from `s1` and `s2` for `mid` size subtrings match => then LCS is possible -> serach  in right space since we need largest
4. Else, if no hashes match, look for smaller lenghts on left size of search space

```python
def hashes_of_all_k_substrings(hasher, size):
    n = len(hasher.s)
    hashes = set()
    for i in range(0,n-size+1):
        hashes.add( hasher.get_hash(i,i+size-1) )
    return hashes


def longest_common_substring(s1, s2):
    n1, n2 = len(s1), len(s2)
    h1, h2 = DoubleHasher(s1), DoubleHasher(s2)
    lcs = min(n1, n2)
    res = 0

    lo,hi = 0, lcs
    while lo<=hi:
        mid = lo + (hi-lo)//2

        s1_hashes = hashes_of_all_k_substrings(h1, mid)
        s2_hashes = hashes_of_all_k_substrings(h2, mid)


        if len(s1_hashes.intersection(s2_hashes)) > 0: # there is common substring of size = mid, we want bigger
            lo = mid+1
            res = max(res, mid)
        else:
            hi = mid-1
    
    return res
```

### Longest Palindromic Substring

💡 Again!!! Can be easily done using DP in O(n<sup>2</sup>). But who needs easier solutions :P

- Same logic as Longest Common Substring, but you **cant use binary search here**
- **WHY?** Lets say there is no palindromic substring of size `k` doesnt mean that you cant have palindromic substrings of size > `k`

```plaintext
Ex: babad
size=2 -> there is no PalindromicSubstring => IN BS you will then seach in [0,1] (BUT THIS IS WRONG)
size=3 -> there is PalindromicSubstring = aba
```

```python
def is_k_substring_palindrome(hasher, size):
    n = len(hasher.s)
    for i in range(0, n - size + 1):
        if hasher.get_hash(i, i + size - 1) == hasher.get_rev_hash(i, i + size - 1):
            return True  # Found a palindromic substring of the given size
            # return hasher.s[i: i + size] # in case you want to print
    return False


def lps(s):
    hasher = DoubleHasher(s)

    for size in range(len(s),-1,-1):
        if is_k_substring_palindrome(hasher, size):
            return size

```


### Min chars to add at end/start such that the resultant string is palindrome
1. **Min Chars add at start**
    1. 💡Find longest palindrome substring starting for 0
    2. If you have this palindrome [0,k] then since [0,k] is already a palindrome, 
        you will add reverse of remanining items to front
    3. res = reverse(s[k+1:n]) + s

2. **Min Chars add at end**
    1. 💡Find longest palindrome substring ending at n-1
    2. If you have this palindrome [k,n-1] then since [k,n-1] is already a palindrome, 
        you will add reverse of remanining items to end
    3. res = s + reverse(s[0:k-1]) 