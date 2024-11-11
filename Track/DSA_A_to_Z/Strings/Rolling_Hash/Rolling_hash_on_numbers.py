
class Hasher:
    def __init__(self, s, k, modprime) -> None:
        self.n, self.k, self.modprime = len(s), k, modprime

        self.hash = [0]*(self.n+1)
        self.pow = [0]*(self.n+1)

        self.pow[0] = 1

        for i in range(1,self.n+1):
            self.hash[i] = ((self.hash[i-1]*self.k) + s[i-1]) % self.modprime
            self.pow[i] = (self.pow[i-1]*self.k)  % self.modprime

    
    def get_hash(self, l, r):
        return (self.hash[r+1] - (self.hash[l]*self.pow[r-l+1]) )  % self.modprime


class DoubleHasher:
    def __init__(self, s) -> None:
        self.s = s
        self.h1 = Hasher(s, 151, (10**8)+7)
        self.h2 = Hasher(s, 181, (10**8)+21)
    
    def get_hash(self, l, r) -> (int, int):
        return (
            self.h1.get_hash(l,r),
             self.h1.get_hash(l,r)
        )



arr = [1,2,1,2,3,1,2]
hsh = Hasher(arr, (10**8)+7, (10**8)+21)

print(hsh.get_hash(0,1))
print(hsh.get_hash(2,3))
print(hsh.get_hash(5,6))