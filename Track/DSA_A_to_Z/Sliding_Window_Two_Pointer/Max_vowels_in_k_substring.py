"""
Problem: Max number vowels in substring
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def maxVowels(self, arr: str, k: int) -> int:
        vowel_count = 0
        res = 0

        for i,x in enumerate(arr):
            if i>=k: # >k so replacement starts
                # check if first element in window was vowel
                if arr[i-k] in "aeiou": # [(0,1,2),3,4] => [0,(1,2,3),4] k=3
                    vowel_count -= 1
            
            if x in "aeiou": # add current element if its vowel
                vowel_count += 1
            res = max(res, vowel_count)
        
        return res