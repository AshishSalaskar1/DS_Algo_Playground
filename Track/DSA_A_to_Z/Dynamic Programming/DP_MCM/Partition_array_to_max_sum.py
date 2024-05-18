from functools import cache
class Solution:
    @cache
    def solve(self, start, k):
        if start == self.n:
            return 0

        max_res = float("-inf")
        max_ele = float("-inf")
        part_length = 0
        for end in range(start, start+k):
            if end >= self.n:
                break
            part_length += 1
            max_ele = max(max_ele, self.arr[end])
            res = (part_length*max_ele) + self.solve(end+1, k)
            max_res = max(max_res, res)
        
        return max_res


    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.arr = arr
        self.n = len(arr)
        return self.solve(0, k)

        