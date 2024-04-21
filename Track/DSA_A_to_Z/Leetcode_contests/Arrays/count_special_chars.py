"""
https://leetcode.com/contest/weekly-contest-394/problems/count-the-number-of-special-characters-ii/
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        pos = {}
        for i,x in enumerate(word):
            if x in pos:
                pos[x].append(i)
            else:
                pos[x] = [i]
        
        arr = set(word)
        res = set()
        for x in arr:
            if x.upper() == x: # uppercase
                if x.lower() in pos: # match present
                    print(x, pos[x.lower()])
                    for lower_pos in pos[x.lower()]:
                        greater_found = False
                        if lower_pos > pos[x][0]: # small > first capital
                            greater_found = True
                            break
                    if greater_found is False:
                        res.add(x.lower())
                    
                            
        return len(res)