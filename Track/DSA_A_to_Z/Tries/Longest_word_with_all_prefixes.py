"""
PROBLEM: https://takeuforward.org/plus/dsa/tries/problems/longest-word-with-all-prefixes

Given a string array nums of length n. A string is called a complete string if every prefix of this string is also present in the array nums. Find the longest complete string in the array nums.
If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None" (without quotes).

Examples:
1. Input : nums = [ "n", "ni", "nin", "ninj" , "ninja" , "nil" ]
    Output : ninja
    Explanation : The word "ninja" is the longest word which has all its prefixes present in the array.

2.  Input : nums = [ "ninja" , "night" , "nil" ]
    Output : None
    Explanation : There is no string that has all its prefix present in array. So we return None.

"""
class TrieNode:
    def __init__(self):
        self.childs = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.childs: cur.childs[ch] = TrieNode()
            cur = cur.childs[ch]
        cur.end = True
    
    def is_all_prefix(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.childs: return False
            cur = cur.childs[ch]

            # WHY HERE N NOT DIRECTLY in 36? self.root is like NULL NODE
            if not cur.end: return False     
        return cur.end         

class Solution:
    def completeString(self, words):
        trie = Trie()
        for word in words: trie.add(word)

        words = sorted(words, key=lambda x:(-len(x),x))    
        
        res = []
        for word in words:
            if trie.is_all_prefix(word) is True: return word
        
        return "None"
