"""
INPLACE: https://leetcode.com/problems/reverse-words-in-a-string/solutions/4884894/best-explanation-with-photos-without-extra-space-beats-100-in-time-95-in-space/

O(1) : Not inplace: https://github.com/KnowledgeCenterYoutube/LeetCode/blob/master/151_Reverse_Words_in_String
"""

class Solution:
    def reverse(self, s: list[str], start: int, end: int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        # Convert string to list of characters for in-place modification
        s = list(s)
        n = len(s)

        # Step 1: Reverse the entire string
        self.reverse(s, 0, n - 1)

        left = 0
        right = 0
        i = 0

        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            if i == n:
                break  # to stop index going out of bounds

            # Process the current word
            if right != 0:
                s[right] = ' '
                right += 1

            left = right
            while i < n and s[i] != ' ':
                s[right] = s[i]
                right += 1
                i += 1

            # Reverse the current word
            self.reverse(s, left, right - 1)
        
        # Resize to remove any extra space at the end
        s = s[:right]
        return ''.join(s)
        