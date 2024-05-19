"""
=> PROBLEM: https://leetcode.com/problems/burst-balloons/
- You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

- If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
- If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.


SOLUTION:
=> Does equal partition work? NO
- [2,3,1,5,8,10] -> lets say you burst bubble 1 first -> profit = 3*1*5 = 15 
- Now 2 subproblems become : [2,3] [5,8,10]
- Now in case you burst 3 then you still need rigth value from subproblem2 (it can 5, or 8,10 in case 5 also is burst)

DP INTUITION:
- f(i, j) -> in this given range(inclusive) which baloon can be burst last, 2-nd last, 3rd last and so on
    - i-1, j+1 must represent value by bursting baloons on right and left
    - Padd  with 1 (for base case i.e picking last balloon)
    - last_ele: i -> j:
        - If t
        - cost = arr[i-1] * arr[last_ele] * arr[j+1] 
                 + solve(i, last_ele-1)
                 + solve(last_ele+1, j)

=> Last burst: [3,1,5,8]
- you can burst any [3],[1],[5],[8]
- In any case since this is the only balloon, cost = 1 * arr[i] * 1 (THATS WHY YOU PAD WITH 1s)

=> Second Last burst -> assume [3] was burst first
- possibilities are 
    [1,3] => 1 * burst_res[3] (burst_res[3] = 3 |that was the only one left)
    [5,3] => 5 * burst_res[3] (burst_res[3] = 3 |that was the only one left)
    [8,3] => 8 * burst_res[3] (burst_res[3] = 3 |that was the only one left)
- Here you can say for each possible idx: IDX
    best_cost(IDX) = BURST_RES_FROM_LEFT * arr[IDX] * BURST_RES_FROM_RIGHT
    best_cost(IDX) = arr[i-1] * arr[IDX] * arr[j+1]

"""
class Solution:
    @cache
    def solve(self, i, j):
        if i>j:
            return 0
        
        best_cost = float("-inf")
        for last_ele in range(i,j+1): # you can take all elements as last
            cost = self.arr[i-1] * self.arr[last_ele] * self.arr[j+1] \
                   + self.solve(i, last_ele-1) \
                   + self.solve(last_ele+1, j) # these are 2 second last burst balloons - ASSUMU FROM START
            best_cost = max(best_cost, cost)
        
        return best_cost

    def maxCoins(self, nums: List[int]) -> int:
        self.arr = [1, *nums ,1]
        return self.solve(1,len(nums))
        