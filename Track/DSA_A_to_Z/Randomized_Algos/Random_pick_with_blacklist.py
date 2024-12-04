"""
Problem: https://leetcode.com/problems/random-pick-with-blacklist/description/?envType=problem-list-v2&envId=randomized

Solution: https://leetcode.com/problems/random-pick-with-blacklist/solutions/144624/java-o-b-o-1-hashmap/?envType=problem-list-v2&envId=randomized 
"""
from typing import List
import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        blacklist = set(blacklist)
        self.valid_n = n - len(blacklist)
        last = n - 1
        self.blacklist_replace = {}

        # Map blacklisted indices to valid indices
        for x in blacklist:
            if x < self.valid_n:  # Only need to handle numbers < valid_n
                while last in blacklist:
                    last -= 1
                self.blacklist_replace[x] = last
                last -= 1

    def pick(self) -> int:
        rindex = random.randint(0, self.valid_n - 1)
        return self.blacklist_replace.get(rindex, rindex)  # Return mapped value if exists, otherwise the index itself
