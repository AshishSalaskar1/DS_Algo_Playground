"""
Problem: https://leetcode.com/problems/longest-duplicate-substring/?envType=problem-list-v2&envId=rolling-hash

Solution:
-  Simple Double Hash
- Check for max_k using binary search
"""
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
    

class Solution:
    def check_duplicate_k(self, s, k):
        n = len(s)
        seen_hashes = set()
        for i in range(n-k+1):
            start, end = i, i+k-1
            cur_hash = self.hsh.get_hash(start, end)
            if cur_hash in seen_hashes:
                return True, s[start:end+1]
            # if k==2:
            #     print(start, end, s[start:end+1], cur_hash )
            seen_hashes.add(cur_hash)

        return False, ""
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        self.hsh = DoubleHasher(s)
        

        lo,hi = 0, n-1
        final_res = ""
        while lo<=hi:
            mid = lo + (hi-lo)//2
            res_flag,res = self.check_duplicate_k(s, mid)
            if res_flag is True:
                if len(res) > len(final_res): 
                    final_res = res
                lo = mid+1
            else:
                hi = mid-1
        
        return final_res