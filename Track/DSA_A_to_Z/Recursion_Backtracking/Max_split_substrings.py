"""
PROBLEM: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

SOLUTION:
=> GREEDY FAILS
- Pick each char, if its not seen (FOR SURE PICK IT)
- In case cur char is seen, find smallest substring from s[cur : cur+1 -> n] which is not seen and add

This fails for "aba" -> greedy will pick "a", "b" and then "a" is already seen which cant be added
-> second pick must have been "ba" and not just "b" [HERE GREEDY FAILS]

BACKTRACKING
=> At each index try picking all substrings from itself s[i] to s[i : j=i+1 -> n]
- Whichever substring is not seen, add to hset => check answer => remove from hset [BACKTRACK STEP]

"""


class Solution:
    def solve(self, i):
        if i>=self.n:
            return 0

        max_ways = float("-inf")
        for j in range(i,self.n):
            cur_substr = self.s[i:j+1]
            if cur_substr not in self.seen: # if this substring isnt seen => add it then backtrack later
                self.seen.add(cur_substr) 
                cur_ways = 1 + self.solve(j+1)  # +1, because you are chosing string s[i,j] inclusive
                max_ways = max(max_ways, cur_ways) 
                self.seen.remove(cur_substr)

        return max_ways

    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        self.seen = set()
        return self.solve(0)
        

        