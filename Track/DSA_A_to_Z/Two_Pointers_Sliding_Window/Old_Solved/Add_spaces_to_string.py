"""
Problem: https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03

SOLUTION:
- Have 3 pointers -> strp, spacep and resp
- resp = [""]*(n+nspace)

"""
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # spaces arrays is sorted here
        s = list(s)
        n, nspace = len(s), len(spaces)
        res = [""]*(n+nspace)

        strp, spacep, resp = 0,0,0
        while strp<n and spacep<nspace:
            # you str-pointer is less that the space index -> just put the char in res
            if strp<spaces[spacep]:
                res[resp] = s[strp]
                strp += 1
            # you reach the space index -> put a space in res, increment space pointer
            elif strp == spaces[spacep]:
                spacep += 1
                res[resp] = " "
    
            resp += 1

        while strp<n:
            res[resp] = s[strp]
            resp += 1
            strp += 1
        
        return "".join(res)

        