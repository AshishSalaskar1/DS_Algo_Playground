
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

class DoubleHasher:
    def __init__(self, s) -> None:
        self.s = s
        self.h1 = Hasher(s, 151, (10**8)+7)
        self.h2 = Hasher(s, 181, (10**8)+21)
    
    def get_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_hash(l,r),
             self.h2.get_hash(l,r)
        )
    
    def get_rev_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_rev_hash(l,r),
             self.h2.get_rev_hash(l,r)
        )

s = "abcabc"
print(s)
hsh = Hasher(s, 151, (10**8)+7)

print(hsh.get_hash(0,2)) # |abc|abc => 97347
print(hsh.get_hash(1,3)) # a|bca|bc => 98337
print(hsh.get_hash(3,5)) # abc|abc| => 97347


s = "racecar"
print(s)
hsh = Hasher(s, 151, (10**8) + 7)

forward_hash = hsh.get_hash(0, len(s) - 1)
reverse_hash = hsh.get_rev_hash(0, len(s) - 1)

print("Forward Hash:", forward_hash)
print("Reverse Hash:", reverse_hash)


s = "abcabacbc"
print(s)
hsh = Hasher(s, 151, (10**8)+7)

forward_hash = hsh.get_hash(2,6)
reverse_hash = hsh.get_rev_hash(2,6)

print("Forward Hash:", forward_hash)
print("Reverse Hash:", reverse_hash)

# USING DOUBLE HASH
s = "racecar"
print("DOUBLE HASH", s)
hsh = DoubleHasher(s)

forward_hash = hsh.get_hash(0, len(s) - 1)
reverse_hash = hsh.get_rev_hash(0, len(s) - 1)

print("Forward Hash:", forward_hash)
print("Reverse Hash:", reverse_hash)
