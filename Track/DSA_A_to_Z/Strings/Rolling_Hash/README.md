# Rolling Hashes

Time Complexity:
- Hash Creation: O(n)
- Subsequent queries are almost O(n)

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
hash(2) = abc    = ak<sup>2</sup> + bk>  + c<br>
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

1. **HASH[i] = (HASH[i-1] * K) + val(s[i])**
2. **HASH[l,r] = HASH[r] - HASH[l-1] * K<sup>(r-l+1)</sup>
(This is Considering 0-based indexing)**


#  Implementation

- While precomputing  we calculate 2 things
     1. `hash` -> Normal hash value
     2. `pow` -> simple K<sup>i</sup>
        - We also calculate this since we may need K<sup>0</sup> -> K<sup>n</sup> (for our range based calculation)
- **Here out precomputes are 1-based, String is 0 based**
```py
class Hasher:
    def __init__(self, s, base_system, modnum) -> None:
        self.n = len(s)
        self.k = base_system
        self.p = modnum # needs to be prime

        self.hash = [0]*(self.n+1) # 1-BASED
        self.pow = [0]*(self.n+1) # 1-BASED

  

        self.hash[0] = 0 
        self.pow[0] = 1
        for i in range(1, self.n+1):
            num = ord(s[i-1]) + 1 # you want to map a:1, b:2 ...

            #h[i] = h[k-1]*k + val(s[i])
            self.hash[i] = ((self.hash[i-1]*self.k) + num ) % self.p# hash(upto i-1) * k + num(s[i])
            
            # just keep on multiplying k to get k^i
            self.pow[i] = (self.pow[i-1]*self.k) % self.p # pow(upto i-1)*i 
        
    
    def get_hash(self, l, r): # 0-Indexed
        # hash[r] - ( hash[k] * k^(r-l) )
        res =  (self.hash[r+1] - (self.hash[l] * self.pow[r-l+1])) % self.p
        return res % self.p


s = "abcabc"
hsh = Hasher(s, 31, (10**8)+7)

print(hsh.get_hash(0,2)) # |abc|abc => 97347
print(hsh.get_hash(1,3)) # a|bca|bc => 98337
print(hsh.get_hash(3,5)) # abc|abc| => 97347
```

**FINDING PATTERNS**
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
        
``