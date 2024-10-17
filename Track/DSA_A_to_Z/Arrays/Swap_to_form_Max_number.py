"""
PROBLEM: https://leetcode.com/problems/maximum-swap

INTUITION:
1) For each digit, find the largest digit which is greater than the current
2) In case multiple digits are max are greater than cur, pick the left most (since we want to make largest)
    96000999999 => 99000999996 is best
3) Then iterate LEFT => RIGHT, whichever first satisfies (1) => SWAP n return res

APPROACH 1:
- LEFT <- RIGHT iterate and store both the idx,val of max_val_after_i
- Iterate LEFT -> RIGHT, first val having val<max_val_after_i => SWAP and return res

APPROACH 2:
- Make a dict, (val:i) => Duplicates vals will get overriden n last you remain with last occurence (this auto fulfills (2) in intuition)
- Iterate LEFT -> RIGHT
    - fillNum: Iterate 9 -> nums[i] (Try fillling max number i.e till nums[i])
        - Check if fillNum is present in val-idx-dict AND val-idx-dict[i] > i

"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, list(str(num))))
        n = len(nums)
        val_idx_map = {x:i for i,x in enumerate(nums)}

        for i in range(n-1):
            for fillVal in range(9,nums[i],-1):
                if fillVal in val_idx_map and val_idx_map[fillVal]>i:
                    nums[i], nums[val_idx_map[fillVal]] =nums[val_idx_map[fillVal]], nums[i]
                    return int("".join(map(str,nums)))
        
        return num

    def maximumSwap1(self, num: int) -> int:
        nums = list(map(int, list(str(num))))
        n = len(nums)
        max_after = [0]*n
        max_after_idx = [0]*n

        max_after[-1] = -1
        max_after_idx[-1] = -1
        max_found = nums[-1]
        max_found_idx = n-1

        for i in reversed(range(n-1)):
            max_after[i] = max_found
            max_after_idx[i] = max_found_idx

            if nums[i] > max_found:
                max_found = nums[i]
                max_found_idx = i
        
        for i in range(n-1):
            if nums[i] < max_after[i]:
                nums[i], nums[max_after_idx[i]] = nums[max_after_idx[i]], nums[i]
                return int("".join([str(x) for x in nums]))

        return num



"""

99000008888888

"""