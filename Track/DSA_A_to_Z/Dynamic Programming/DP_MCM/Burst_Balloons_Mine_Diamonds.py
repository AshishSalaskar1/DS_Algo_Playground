class Solution:
    @cache
    def solve(self, i, j):
        if i>j:
            return 0
        
        best_cost = float("-inf")
        for last_ele in range(i,j+1): # you can take all elements as last
            cost = self.arr[i-1] * self.arr[last_ele] * self.arr[j+1] \
                   + self.solve(i, last_ele-1) \
                   + self.solve(last_ele+1, j)
            best_cost = max(best_cost, cost)
        
        return best_cost

    def maxCoins(self, nums: List[int]) -> int:
        self.arr = [1, *nums ,1]
        return self.solve(1,len(nums))
        