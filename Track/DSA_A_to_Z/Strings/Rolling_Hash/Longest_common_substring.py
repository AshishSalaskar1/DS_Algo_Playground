"""

Longest Common Substring but using Rolling Hash
"""


class Hasher:
    def __init__(self, s, k, modprime) -> None:
        self.n, self.k, self.modprime = len(s), k, modprime

        self.hash = [0]*(self.n+1)
        self.pow = [0]*(self.n+1)

        self.pow[0] = 1

        for i in range(1,self.n+1):
            self.hash[i] = ((self.hash[i-1]*self.k) + ord(s[i-1]) + 1) % self.modprime
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
             self.h2.get_hash(l,r)
        )


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
    

s1 = "ashishsomeashish"
s2 = "some"
print(longest_common_substring(s1, s2))

s1 = "ashishsomeashish"
s2 = "ashishsome"
print(longest_common_substring(s1, s2))