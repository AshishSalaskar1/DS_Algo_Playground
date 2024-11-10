"""
Problem: Given a string and a pattern, find all indexes (start, end) where pattern is found in string

s = sadbutsad
p = sad
res = (0,2), (6,8)

SOLUTION:
- Calculate hashes for both and keep them (USE SAME BASE, MODPRIME)

"""



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

            self.hash[i] = ((self.hash[i-1]*self.k) + num ) % self.p# hash(upto i-1) * k + num(s[i])
            self.pow[i] = (self.pow[i-1]*self.k) % self.p # pow(upto i-1)*i 
        
    
    def get_hash(self, l, r):
        # hash[r] - ( hash[k] * k^(r-l) )
        res =  (self.hash[r+1] - (self.hash[l] * self.pow[r-l+1])) % self.p
        return res % self.p

def find_pattern(s, p):
    ns, np = len(s), len(p)

    shash = Hasher(s, 151, (10**8)+7)
    phash = Hasher(p, 151, (10**8)+7)

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
        
