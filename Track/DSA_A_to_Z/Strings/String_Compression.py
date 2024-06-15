"""
Compress Strings: https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

Solution: https://leetcode.com/problems/string-compression/solutions/3245804/clean-codes-full-explanation-two-pointers-c-java-python3

"""
class Solution:
    def compress(self, arr: List[str]) -> int:
        n = len(arr)
        ans_end, i= 0, 0

        while i<n:
            cur_letter = arr[i]
            count = 0
            while i<n and arr[i] == cur_letter: # find all same chars as current
                i += 1
                count += 1
            
            # replace the counts in the array
            arr[ans_end] = cur_letter
            ans_end += 1

            if count > 1: # if count=1, just update char and not count
                for x in str(count): # in case > 10 it should be "a","1","12"
                    arr[ans_end] = x
                    ans_end += 1
        
        return ans_end # no need of -1 (since its already ahead by 1, due to ans_end+1)


        