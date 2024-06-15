"""
PROBLEM: Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close

Strings are close if (can you create string b from a using these 3 operations)
1) They are same
2) They can be made same with some reordering
3. They can be made same by relacing any ch1 <=> ch2 
    - You repalce all occurences of ch1->ch2 and ch2->ch1
    - This can be done ANY number of times

SOLUTION:
- https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/4561223/beats-99-46-users-c-java-python-javascript-explained
- https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/935920/c-short-and-simple-o-n-solution/?envType=study-plan-v2&envId=leetcode-75

INTUITION:
1) They are same: 
    - False if set(w1)!=set(w2) [remember you cant add new chars]
2) They can be made same with some reordering
    - Counter(w1) == Counter(w2)
    - Both chars and their occurences are to be same
3. They can be made same by relacing any ch1 <=> ch2
    - Make sure the sorted occurences are same
    - keys dont matter, since you are swapping anyways

"""

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cmap = {}        
        n1, n2 = len(word1), len(word2)

        if n1 != n2:
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if c1 == c2:
            return True
        
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        print(c1.items(),"\n",c2.items())
        return sorted(c1.values()) == sorted(c2.values())

        

"""
cabbba => a:2, b:3, c:1
abbccc => a:1, b:2, c:3
"""
        