"""
Problem: Subsequence sum after capping
https://leetcode.com/problems/subsequence-sum-after-capping-elements/


SOLUTION: Classic Bitset DP to find subset sum with some Optimizations
1. If subset sum=k, you just stop there
2. You dont need to check subset sum<=k, Hence always set bits > k as 0 
    - bitset &= (1<<(k+1))-1 [00000000001[k]111111]
    - This sets all bits after `k` as 1, and only those are considered in bitset

"""
class Solution:
    def subsequenceSumAfterCapping(self, arr: List[int], k: int) -> List[bool]:
        res = []
        n = len(arr)

        for cap in range(1, n+1):
            bitset = 1 # subset sum 0 is possible
            for x in arr:
                bitset |= bitset<<min(x,cap)
                if bitset & (1<<k) > 0: # target sum is reachable
                    break
                # You need to check subset sum <= k
                bitset &= (1<<(k+1))-1
                
            
            res.append(bitset & (1<<k) > 0)
        
        return res
            

