"""
SOLUTION 1: TLE
- for left: 0->n:
    - freq = {s[left]: 1}
    - for right: left+1 -> n:
        freq[s[right]] += 1
        if isvalid(freq): # contains a,b,c
            res += (n-right) # if (l,r) is valid, anything after r is also valid string
            break

- Gives TLE, since its O(N*N)

SOLUTION 2: Better
- At any point "i", if you know string ending here is valid (a,b,c are all present)
- The the valid string starts from min(recent_a, recent_b, recent_c) since it should contain all 3, 
  so it starts from most recent seen occurence and min of it
0 1 2 3 4 5
a b c a b c

=> at [2], abc are all found => whats the exact valid string = abc  = [0:2]
=> at [3], abc are all found => whats the exact valid string = bca = [1:3]
-> Now that we know exact string is min(recent_a/b/c) -> i, any chars before the starting are also valid (you add anything but abc are already there)
-> So number of valid strings ending at "i" = min(recent_a, recent_b, recent_c) + 1
0 [1 2 3] 4 5
a [b c a] b c -> there are index[b]+1 chars before start of this valid string

"""

class Solution:
   
        
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        recent_a, recent_b, recent_c = -1, -1, -1

        for i, x in enumerate(s):
            if x=="a":
                recent_a = i
            if x=="b":
                recent_b = i
            if x=="c":
                recent_c = i

            if recent_a + recent_b + recent_c >= 3: # some valid string ends here
                res += min(recent_a, recent_b, recent_c) + 1
        
        return res




