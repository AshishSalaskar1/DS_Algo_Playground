"""
PROBLEM: https://leetcode.com/problems/subsets-ii/submissions/
- Given an integer array nums that may contain duplicates, return all possible 
subsets
- The solution set must not contain duplicate subsets. Return the solution in any order.


SOLUTION: Backtracking + Front partition (same as COMBINATION SUM II)
- Can be done using pick/dont pick approach, but you need extra DS to eliminate duplicates
- SORT ELEMENTS (to make finding duplicates easy)
- f(i) -> subsets you can make starting from i (including i)
    - res.append(cur) <- add every subset you make (no need to wait till you reach the end)
    - for j: i -> n:
        if j is not first element and is a duplicate:
            1. add arr[j] to cur
            2. solve(j+1)
            3. pop arr[j] from cur (BACKTRACK)

"""

class Solution:
    def solve(self, i:int, arr: list[int]):
        """
        Subsets you can create starting from i
        """
        self.res.append(self.cur[:].copy())

        for j in range(i, len(arr)):
            # dont allow duplicates -> but pick first one of duplicates
            if j != i and arr[j] == arr[j-1]:
                continue
            
            self.cur.append(arr[j]) # you pick j^th element
            self.solve(j+1, arr)
            self.cur.pop() # backtrack after picking

    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        self.res = []
        self.cur = []

        arr = sorted(arr)
        self.solve(0, arr)
        return self.res
