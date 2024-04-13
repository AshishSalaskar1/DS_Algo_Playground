"""
PROBLEM
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1
Constraints:
 - You need to pick each element

SOLUTION:
- At each iteration you either pick a element or not
- Dont check target<0, becaause it can be geniune case (remaining arr=[1,1], target=-2, YOU CAN STILL MAKE IT)

"""

class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.dp = {}

    # n = 1-based index
    def target_sum(self, n, target):
        if (n,target) in self.dp:
            return self.dp[(n,target)]

        # no coins 
        if n==0:
            return 1 if target==0 else 0

        res =  self.target_sum(n-1, target+self.arr[n-1]) + self.target_sum(n-1, target-self.arr[n-1])
        self.dp[(n,target)] = res

        return res


def targetSum(arr, target) -> int:
    sol = Solution(arr)
    return sol.target_sum(n=len(arr), target=target)