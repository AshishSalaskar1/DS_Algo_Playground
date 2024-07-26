"""
PROBLEM: https://leetcode.com/problems/minimum-length-of-string-after-operations/


SOLUTION: https://leetcode.com/problems/minimum-length-of-string-after-operations/solutions/5506872/count-frequency-of-each-character/

- If count of any char is ODD (len-1 deletions)
- If count of any char is EVEN (len-2 deletions)

"""

from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        vocab = defaultdict(int)
        for i,ch in enumerate(s):
            vocab[ch] += 1
        
        remove_count = 0
        for ch, count in vocab.items():
            if count%2 == 1: # ODD
                remove_count += count-1
            else: # EVEN
                remove_count += count-2
        print(remove_count)
        return n - remove_count