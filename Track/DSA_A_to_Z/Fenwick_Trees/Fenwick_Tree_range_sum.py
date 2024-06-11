"""
PROBLEM: Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/?envType=problem-list-v2&envId=5vezxjhm

=> BIT/Fenwick Tree: https://leetcode.com/discuss/general-discussion/1093346/introduction-to-fenwick-treebinary-indexed-treebit

SOLUTION:
- BIT is always 1-Based indexed

- Fenwick is great only when array mutates (updates happen frequently)
- Otherwise PREFIX SUM is best
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums) 
        self.bits = [0]*(self.n+1) # 1-Based Index
        self.nums = nums # 0-Based Index
        
        for i in range(self.n): # add all numbers first
            self.update_bit(i, self.nums[i]) 
    
    def update_bit(self, idx, val):
        # idx (0 based) => convert to 1 based
        idx += 1
        while idx <= self.n:
            self.bits[idx] += val
            idx += (idx & -idx)
    
    def get_sum(self, idx: int) -> int:
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= (idx & -idx) # RSB unset/set
        
        return res

    def update(self, index: int, val: int) -> None:
        # you already have arr[i] set -> unset that and then add
        # update(i+1, -arr[i]) => update(i+1, val) ==> update(i+1, val-arr[i])
        diff = val  - self.nums[index]
        self.nums[index] = val
        self.update_bit(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right) - self.get_sum(left-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)