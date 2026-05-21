"""
Problem: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2026-05-21


SOLUTION 1: String matching
OPTIMAL: Simple Tries
"""
class TrieNode:
    def __init__(self):
        self.val = None
        self.childs = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s: str) -> None:
        cur = self.root

        for ch in s:
            if ch not in cur.childs:
                cur.childs[ch] = TrieNode()
            cur = cur.childs[ch]
        
    def getLongestPrefix(self, s: str) -> int:
        res = 0
        cur = self.root

        for ch in s:
            if ch not in cur.childs:
                return res
            
            cur = cur.childs[ch]
            res += 1
        
        return res
        


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for x in arr1:
            trie.insert(str(x))
        
        res = 0
        for x in arr2:
            res = max(res, trie.getLongestPrefix(str(x)))
        
        return res