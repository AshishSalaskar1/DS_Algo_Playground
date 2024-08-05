"""
PROBLEM: Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/?envType=problem-list-v2&envId=5vezxjhm

Pepcoding explaination: https://www.youtube.com/watch?v=pTg7NezkV28

=> BIT/Fenwick Tree: https://leetcode.com/discuss/general-discussion/1093346/introduction-to-fenwick-treebinary-indexed-treebit

SOLUTION:
- BIT is always 1-Based indexed
- Fenwick is great only when array mutates (updates happen frequently)
- Otherwise PREFIX SUM is best
- When to use, given array n queries where you need to find sum(start,end). But elements can get updated also

LOGIC:
- Fenwick tree is 1-indexed
- Replacing a value = INCREMENTING/DECREMENTING existing value (NO CONCEPT OF REPLACING)
- fenwick[idx] stores = sum of last `k` elements (idx, idx-1, idx-2 .... idx-k)
    where `k` = value of last set bit of `idx`

  Example: fenwick[6] stores sum of last 2 elements ie fenwick[6] = nums[6]+nums[5]
  - 6 = 0110 = Last set bit = 0010 = 2 

- UPDATE_BIT: Keep on adding last set bit until you exceed n [IDX += IDX & -IDX]
- GET_SUM: keep on unsetting the last set bit until you reach 0 [IDX -= IDX & -IDX]

- Remember: WE increment idx in get_sum and update functions automatically


UPDATE_BIT(idx, delta) # here val is the delta to + or - from existing
    - Go on adding the last set bit to idx until its > n
    - You will keep on going upwards

    idx += 1
    while idx <= self.n:
        fenwick[idx] += delta 
        idx += (idx & -idx) # RSB set

    - (idx & -idx) gives u only the last set bit (011110 => 000010)
    - idx + (idx & -idx) => UNSETS THE LAST SET BIT


GET_SUM(idx) -> returns sum of items from start till idx
    - Go on unsetting the last set bit and summing up values
    - You will always keep on going down

    idx += 1
    res = 0
    while idx > 0:
        res += fenwick[idx]
        idx -= (idx & -idx) # RSB unset

    return res

    - (idx & -idx) gives u only the last set bit (011110 => 000010)
    - idx - (idx & -idx) => UNSETS THE LAST SET BIT

SUM_OF_RANGE(start, end)
    - return GET_SUM(right) - GET_SUM(LEFT-1)  # Why left-1, because you need to include left and right also

REPLACE_VAL(idx, val)
    - UPDATE_BIT(idx, -nums[idx]) -> UPDATE_BIT(idx, val) [you set prev value to 0 and then set new value]
    - UPDATE_BIT(idx, -nums[idx]) + UPDATE_BIT(idx, val) = UPDATE_BIT(idx, nums[idx]-val)


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
            idx += (idx & -idx) # RSB set
    
    def get_sum(self, idx: int) -> int:
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= (idx & -idx) # RSB unset
        
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


