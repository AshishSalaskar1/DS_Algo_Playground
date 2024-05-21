class Solution:
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        max_index_reachable = 0+arr[0]

        for i in range(1,n): 
            # you could never have reached this index
            if max_index_reachable < i:
                return False

            # you can either come here (i+arr[i]) or else just jump from other previous node
            max_index_reachable = max(max_index_reachable, arr[i]+i) 

            # from this index, you can the end directly
            if max_index_reachable >= n:
                return True
        
        return True



    def canJumpClassicDP(self, arr: List[int]) -> bool:
        n = len(arr)
        dp = [False for _ in range(n)]

        dp[n-1] = True

        for i in reversed(range(n-1)):
            k = arr[i]
            for j in range(i+1, i+k+1):
                if j>=n:
                    break
                dp[i] = dp[i] or dp[j]
                if dp[i] is True:
                    break
        
        return dp[0]


        