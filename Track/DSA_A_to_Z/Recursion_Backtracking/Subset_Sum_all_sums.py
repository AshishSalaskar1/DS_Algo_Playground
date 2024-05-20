"""
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Example 1:
{5,2,1} -> 0,1,2,3,5,6,7,8
-  [[], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1]

Example 2:
{3,1,2} -> 0,1,2,3,3,4,5,6
-  [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1]]
"""

class Solution:
    def solve(self, i:int, csum:int, arr: list[int]):
        if i<0:
            self.res.add(csum)
            return

        # pick
        self.solve(i-1, csum+arr[i], arr)
        # dont pick
        self.solve(i-1, csum, arr)

    def all_subset_sum(self, arr: list[int]):
        self.res = set()
        self.solve(len(arr)-1, 0, arr)
        print(self.res)

sol = Solution()
arr = [5,2,1]
sol.all_subset_sum(arr)

res = []
arr = [3,1,2]
sol.all_subset_sum(arr)
