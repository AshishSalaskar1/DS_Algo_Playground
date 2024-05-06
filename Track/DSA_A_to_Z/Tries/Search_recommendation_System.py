
"""
PROBLEM: Given a vocab and a Search word. Return top-3 (Lexographically sorted) suggestions as each word is being typed
Link: https://leetcode.com/problems/search-suggestions-system/

"""

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = TrieNode()
            cur = cur.child[ch]
        cur.isEnd = True
            
    def print_from_node(self, node, cur_word):
        for ch, tNode in node.child.items():
            self.print_from_node(tNode, cur_word+ch)
        
        if node.isEnd:
            self.prefixes.append(cur_word)
            
    def prefix_search(self, prefix):
        self.prefixes = []
        cur = self.root
        
        for i,ch in enumerate(prefix):
            if i == len(prefix)-1 and cur.isEnd:
                self.prefixes.append(prefix)
                
            if ch not in cur.child:
                return []
            cur = cur.child[ch]
 
        self.print_from_node(cur, cur_word=prefix)
        return self.prefixes
        
class Solution:
    def suggestedProducts(self, products, searchWord):
        # return top3 lexographically
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        
        res = []
        for i in range(len(searchWord)):
            cur_typed_word = searchWord[:i+1]
            res.append(sorted(trie.prefix_search(cur_typed_word))[:3])
        
        return res