"""
https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/submissions/1712509329/
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
            if ch not in cur.childs:
                cur.childs[ch] = TrieNode()
            cur = cur.childs[ch]
        
        cur.end = True
    
    def search(self, target):
        cur = self.root
        for ch in target:
            if ch not in cur.childs:
                return False
            cur = cur.childs[ch]
        
        return cur.end

class Solution:

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        trie = Trie()
        for word in startWords:
            trie.add(sorted(list(word)))

        res = 0
        for word in targetWords:
            word = sorted(list(word))
            for i in range(len(word)):
                if trie.search(word[:i]+word[i+1:]):
                    res += 1
                    break
        
        return res
  
                
                
                
            

