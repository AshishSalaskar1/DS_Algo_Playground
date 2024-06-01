class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        left_high = [0]*n
        right_high = [0]*n
        
        left_high[0] = arr[0]
        right_high[-1] = arr[-1]
        
        # Highest bar on left
        for i in range(1,n):
            left_high[i] = max(arr[i], left_high[i-1])
            
        # Highest bar on right
        for i in reversed(range(n-1)):
            right_high[i] = max(arr[i], right_high[i+1])
            
        res = 0
        # Max water each step can hold
        for i in range(n):
            res += min(left_high[i], right_high[i]) - arr[i]
        
    
        return res
        