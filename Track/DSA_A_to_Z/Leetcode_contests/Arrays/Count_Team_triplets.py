"""
PROBLEM: https://leetcode.com/problems/count-number-of-teams

SOLUTION:
https://leetcode.com/problems/count-number-of-teams/solutions/565479/python-97-98-simple-logic-and-very-detailed-explanation/?envType=daily-question&envId=2024-07-29

LOGIC:
- Lets say at given index `i` you have these 4 counts
    1. lg: no of elements on LEFT GREATER than cur
    2. ls: no of elements on LEFT SMALLER than cur
    3. rg: no of elements on RIGHT GREATER than cur
    4. rs: no of elements on RIGHT SMALLER than cur
- Calculate num ways
    1. Ways in increasing order = LS*RG
        - Ex: [1,2] 5 [6,7] => [1,5,6],[1,5,7],[2,5,6],[2,5,7]
        - Why we didnt consider 1,2,6 -> that would have already been added while i=2
    2. Ways in decreasing order = LG*RS
    Note: 
        - Here you assume that cur_ele is always picked (rest u pick one each from LEFT and RIGHT)
    - COUNT += (LS*RG) + (LG*RS)

"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i in range(n):
            lg, ls, rg, rs = 0,0,0,0

            # left subarray
            for j in range(i):
                if rating[j] > rating[i]:
                    lg += 1
                if rating[j] < rating[i]:
                    ls += 1
        
            # right subarray
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    rg += 1
                if rating[j] < rating[i]:
                    rs += 1
                
            res += (ls*rg) + (lg*rs)
            
        return res