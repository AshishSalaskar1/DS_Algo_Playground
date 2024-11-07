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



