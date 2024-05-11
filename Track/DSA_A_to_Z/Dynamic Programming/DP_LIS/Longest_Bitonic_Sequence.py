"""
PROBLEM: Longest Bitonic Sequence [Not strictly]
LBS can be (NOT STRICT HERE)
    1. All increasing -> LIS
    2. All decreasing -> LDS
    3. All Increase -> pivot point -> All Decrease


SOLUTION: LIS+LDS
- LIS[i]: Longest increasing subsequence including elements [0,i]
- LDS[i]: Longest decreasing subsequence including elements [i,n]
- At each index i,
    LBS = LIS[i] + LDS[i] - 1 
    - You pick increasing elements till i
    - You pick decreasing elements after i
    - -1 because you include `i`th element in both LDS and LIS


"""

class Solution:
    def LIS(self, arr):
        n = len(arr)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        
        for i in range(1,n):
            maxlen = 1
            for j in range(0,i):
                if arr[j] < arr[i]:
                    maxlen = max(maxlen, 1+dp[j])
                    
            dp[i] = maxlen 
        
        return dp
    
    def LDS(self, arr):
        n = len(arr)
        dp = [0 for _ in range(n)]
        dp[n-1] = 1
        
        for i in reversed(range(0,n-1)):
            maxlen = 1
            for j in range(i+1,n):
                if arr[j] < arr[i]:
                    maxlen = max(maxlen, 1+dp[j])
                    
            dp[i] = maxlen 
        
        return dp
        

        
    def LongestBitonicSequence(self, n : int, arr : List[int]) -> int:
        lis = self.LIS(arr)
        lds = self.LDS(arr)

        
        res = 0
        for i in range(n):
            res = max(res, lis[i]+lds[i]-1)
        
        return res
