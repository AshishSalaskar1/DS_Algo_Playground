"""
PROBLEM: https://leetcode.com/problems/vowels-game-in-a-string/description/
"""

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum([1 for x in s if x in "aeiou"]) > 0

        lcount, rcount = [0]*len(s), [0]*len(s)
        
        count = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                count += 1
            lcount[i] = count
        
        count = 0
        for i in reversed(range(len(s))):
            if s[i] in "aeiou":
                count += 1
            rcount[i] = count

        if lcount[-1]%2 == 1:
            return True
        
        # print(lcount)
        # print(rcount)

        for i in reversed(range(len(s)-1)):
            if lcount[i]%2 == 1:
                # print(f"BREAKING AT: {i}, {lcount[i]}, {rcount[i]}")
                if rcount[i+1]%2 == 0:
                    return False
                else:
                    return True
                
        
                
                

        