"""
Problem: https://leetcode.com/problems/subsets/description/

BIT MANIPULATION APPROACH
- If arr has N elements, then it has 2^N elements in powerset
- Iterate 2^n, options such that in each you PICK/DONT pick elements

[5,6,7] => n = 3 (1 --> 2^3)

0 - 0 0 0 (0 at 0,1,2 => dont pick 5,6,7) => []
1 - 0 0 1 (0 at 0,1 and 1 at 2 => dont pick 5,6, pick 7) => [7]
2 - 0 1 0 
3 - 0 1 1
4 - 1 0 0
5 - 1 0 1
6 - 1 1 0
7 - 1 1 1

(Here if set=pick, dont pick)

TRICKS:
- 2^n = (1<<n)
- Check if i'th bit is set = [X & (1<<i) != 0]
"""

class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        start, end = 0, (1<<n) # 0 -> 2^n
        res = []
        
        for x in range(start,end):
            cur_res = []
            for i in range(n):
                # check if i'th bit is set or not
                if x&(1<<i) != 0:
                    cur_res.append(arr[i])
            
            res.append(cur_res)

        return res

        