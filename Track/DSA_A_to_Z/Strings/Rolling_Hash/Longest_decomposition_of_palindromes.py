"""
Link: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/?envType=problem-list-v2&envId=rolling-hash

SOLUTION
- Here we follow GREEDY approach
- Starting at lo=0, hi=n-1 => we try to make palindromic substrings from start, end of size=1 
- Because best case is you have n palindromic substrings, each of size 1 (aaaaa)

ALGO ==>
1. Initialization: left and right are set at the two ends of the string, and count keeps track of the number of chunks.
2. While Loop: The loop continues until left surpasses right
    - Hash Comparison: For each substring length, we compute hashes for the substring starting at left and the substring ending at right.
    - Chunk Formation: If the hashes match, it means we’ve found a palindromic chunk.
        1. If the current chunk is not the last single center chunk, increment count by 2 (indicating matched chunks on both sides).
        2. If this is the center chunk (when left + length - 1 >= right - length + 1), increment count by only 1
    - Pointer Update: Move left and right inward by the length of the matched chunk, then reset length to 1.
    - Increase Chunk Length: If the hashes don’t match, increment length to check the next possible chunk length.


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
             self.h1.get_hash(l,r)
        )

class Solution:
    def longestDecomposition(self, s: str) -> int:
        hasher = DoubleHasher(s)

        n = len(s)
        substr_count = 0
        lo, hi = 0, n-1

        substr_len = 1 # best case is you split into palindromes of size 1

        while lo<=hi:
            left_hash = hasher.get_hash(lo,lo+substr_len-1)
            right_hash = hasher.get_hash(hi-substr_len+1, hi)

            if left_hash == right_hash:
                # two words overlap thats means its single string - else 2 palindromes
                if lo+substr_len-1 < hi-substr_len+1:
                    substr_count += 2
                else: # ashish -> lo=0,hi=5 -> you will find hashes equal for sub_len = 6 (entire string) [BUT THIS WILL OVERLAP -> hence only palindrome word]
                    substr_count += 1
                
                # adjust left right pointers based on the 1/2 palindromes you have chosen
                lo += substr_len
                hi -= substr_len

                substr_len = 1 # next words will again be of size=1 in best case
            else:
                substr_len += 1
            
        return substr_count

        