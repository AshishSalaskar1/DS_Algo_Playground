"""
PROBLEM
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

INTUITION:
- Given string of length "L", the min replacements to be made so that all chars are same = L - (freq of most occuring element)
- Logic: AABABBA : {A:4, B:3} => replace all 3 Bs with A 
- So min operations needed for this string = 7-4=3

- You are given at most "k" replace operations
- left, right = 0,0
- right++ and update freq
    - cur_str = arr[left:right]
    - You need len(cur_str) - max_freq replacements to make as chars as same, but we are allowed at most "k" replacements
    - if len(cur_str) - max_freq > k [SLIDING WINDOW]
        - left++ and update freq until len(cur_str) - max_freq > k [SLIDING WINDOW]
    - right ++



"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0,0
        cmap = {}
        res = 0

        while left<=right and left<n and right<n:
            cmap[s[right]] = cmap.get(s[right],0) + 1

            maxFreq = max(cmap.values())
            while right-left+1 - max(cmap.values()) > k: # SLIDE WINDOW from left
                cmap[s[left]] = cmap.get(s[left])-1
                left += 1
            
            res = max(res, right-left+1)
            right += 1
        
        return res

        