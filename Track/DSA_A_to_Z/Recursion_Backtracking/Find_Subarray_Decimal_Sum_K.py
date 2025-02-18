"""
Problem: Find the Punishment Number of an Integer
Link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/?envType=daily-question&envId=2025-02-15


SUB_PROBLEM:
- Given a decimal number in string format, split it into contigous subarrays and join them
- 💡arr=100, target=10 -> 10+0 = 10 TRUE

i, num = 9, "81"  # 8 + 1
i, num = 10, "100"  # 10 + 0
i, num = 36, "1296"  # 1 + 29 + 6

"""
from functools import lru_cache

def is_punishment_number(idx, cur_taken, cur_sum, target, arr):
    if idx == len(arr):
        # Add the last segment (cur_taken) to cur_sum before comparison
        if cur_taken:
            cur_sum += int(cur_taken)
        return cur_sum == target

    # Option 1: Continue taking characters into cur_taken
    if is_punishment_number(idx + 1, cur_taken + arr[idx], cur_sum, target, arr):
        return True

    # Option 2: Stop taking and process the current cur_taken
    if cur_taken:  # Only proceed if cur_taken is not empty
        if is_punishment_number(idx + 1, arr[idx], cur_sum + int(cur_taken), target, arr):
            return True

    return False

class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            if is_punishment_number(0, "", 0, i, str(i**2)):
                print(i,i**2)
                res += i**2
        
        return res
        Push