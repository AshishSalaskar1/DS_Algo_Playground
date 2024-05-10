"""
PROBLEM: Given a string s, find the length of the longestsubstring without repeating characters.

INTUITION:
L = 0, R = keep on incrementing 
1. If char[R] was already seen
- L[a]bc[a]bcbb - you are a(second one)
- Now ur L becomes index(a)+1 => aL[b]ca[b]cbb2z

Note: index[x]+1 ONLY IF index[x]+1 > L
- Example: abL[b]R[a] -> now index[a]=0, dont do L=1 (bba - b repeats)
2. char[R] not seen => index(x) = i
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        hmap = {}
        l,r = 0,0
        maxlen = 0

        while r<n:
            x = s[r] # char on right
            if x not in hmap: # char never seen
                hmap[x] = r 
            else: # char previously seen -> change L
                if hmap[x] >= l: # occurence[x] was only after LEFT (not before - abba)
                    l = hmap[x]+1 # you can pick substring after LEFT
                hmap[x] = r # update location
            maxlen = max(maxlen, r-l+1) 
            r += 1
        
        return maxlen
            



