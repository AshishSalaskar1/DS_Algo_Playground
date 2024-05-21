class Solution:
    def jump(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [float('inf') for _ in range(n)]
        
        dp[n-1] = 0
        for i in reversed(range(n-1)):
            if arr[i] == 0:
                dp[i] = float('inf')
                continue
                
            max_jump = i+arr[i]
            
            if max_jump >= n-1:
                dp[i] = 1
            else:
                dp[i] = float('inf')
                for j in range(i+1,max_jump+1):
                    dp[i] = min(dp[i], 1+dp[j])
                    
        print(dp)
        return dp[0]
            
        
        # dp[0] = 0
        # for i in range(1,n):
        #     for j in range(i):
        #         max_jump = j+arr[j]
        #         if max_jump>=i and arr[j]!=float('inf'):
        #             dp[i] = min(dp[i],1+dp[j])
        # # print(dp)
        # return dp[-1]
        

        