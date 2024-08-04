"""
PROBLEM: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02
SOLUTION:
- Min exchanges to bring 1s together = min subarray containing all 1s (number of 0s in tht subarray is ANS)

Alternate thinking: if number of 1s is n_ones, then window_size = n_ones
- Now check for all subarrays for size window_size (sliding window)
- Count number of Os (RES) => BUT here we keep count of ones and at last do WINDOW_SIZE-MAX_ONES
0,1,0,1,1,0,0 - n_ones=3

|0,1,0|,1,1,0,0 => you need 2 replacements (1 ones)
0,|1,0,1|,1,0,0 => you need 1 replacements (2 ones)
0,1,|0,1,1|,0,0 => you need 1 replacements (2 ones)
0,1,0,|1,1,0|,0 => you need 1 replacements (2 ones)
0,1,0,1,|1,0,0| => you need 2 replacements (1 ones)

- New statement: Find the subarray of size=n_ones having maximimum number of ones (More the number of ones, lesser 0s, lesser exchanges)
Handling circular = consider 2 arrays joins - auto handled
- [1,1,0,0,1] [1,1,0,0,1] = [1,1,0,0,1 , 1,1,0,0,1]
- U can use extra space to concat OR use MOD operator and run upto 2N
"""

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window_size = sum(nums)
        if window_size <= 1:
            return 0
    
        cur_ones =  sum(nums[:window_size])
        max_ones = cur_ones
        l,r = 0,window_size

        while l<=r and r<2*n:
            if nums[l%n] == 1:
                cur_ones -= 1
            if nums[(r)%n] == 1:
                cur_ones += 1
            
            l += 1
            r += 1
            max_ones = max(cur_ones, max_ones)
        
        return window_size - max_ones

        

       

            


