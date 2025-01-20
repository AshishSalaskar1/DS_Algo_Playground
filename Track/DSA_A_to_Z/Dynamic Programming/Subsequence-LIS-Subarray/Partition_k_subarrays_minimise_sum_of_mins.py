"""
PROBLEM:
- Given a array you need to partition this into `k` non-empty subarrays 
- Such that SUM OF ( min of each partition) <- This is minimized

Ex: [1,3,2,5,4], k = 3
Res = 6 -> [1], [3], [2,5,4] = 1+3+2 = 6

  0  1  2  3  4
[ 1, 3, 2, 5, 4]

"""
from functools import lru_cache




class Solution:
    @lru_cache(None)
    def solve(self, i, npartitions):
        print(i, npartitions)
        # splitting into more than needed partitions
        if npartitions < 0:
            return float("inf")
        
        # Base case: all indexes use up
        if i == -1:
            return 0 if npartitions==0 else float("inf") 
        
        # Initialize variables
        cur_res = float("inf")
        cur_min = float("inf")
        
        # Iterate backward to explore partitions
        for j in range(i, -1, -1):
            cur_min = min(cur_min, self.arr[j])  # Update current partition minimum
            # You have picked "j", remnainig is 0->(j-1)
            cur_res = min(cur_res, cur_min + self.solve(j - 1, npartitions - 1))  # Recursive call
        
        print(i, npartitions, cur_res)
        return cur_res

    def min_sum_partition(self, arr, k):
        self.arr = arr
        self.n = len(arr)
        
        return self.solve(self.n - 1, k)



# sol = Solution()
# arr = [1,3,2,5,4] # 6 [1][3][2 5 4]
# k = 3 # res = 6
# print(sol.min_sum_partition(arr,k))

# sol = Solution()
# arr = [10, 20, 30, 40, 50] # 60 [10, 20, 30] and [40, 50]
# k = 2 
# print(sol.min_sum_partition(arr,k))

sol = Solution()
arr = [5, 1, 3, 2, 8, 7, 4] # 7 [5], [1, 3, 2], and [8, 7, 4].
k = 3
print(sol.min_sum_partition(arr,k))


# sol = Solution()
# arr = [1, 2, 3, 4, 5] # 15 [1], [2], [3], [4], [5].
# k = 5
# print(sol.min_sum_partition(arr,k))
