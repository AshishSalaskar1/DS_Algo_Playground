"""
Tries are used to implement a Dictionary
Operations: Insert word, Delete Word, Search Word, Search Prefix words

Leetcode Python Implmentation: https://leetcode.com/problems/word-search-ii/discuss/1122269/Python-Fastest-Implementation-with-Delete-Trie-Node

=> Implementation
- We define a TrieNode. Basically each char of word is stored in a tree form

TrieNode has a array of length 25 (lowercase alphabets only) and an isEnd
1.arr: Contains another TrieNode if this alphabet exists in a word
2.isEnd : True|False based on whether the word ends at this char. it means that one word ends here, but there may be another word which is continuation of this word
isEnd=True doesnt mean Trie ends (for "geek" isEnd(k)=True but it may further have nodes in case of "geeks")

=> Insertion
- Initially the root is a TrieNode with all 25 chars as null
- Iterate over all chars one by one, if TrieNode[char] is null, create a new TrieNode and point TrieNode[char] to the new Node n continue working on that TrieNode.
- If TrieNode[char] exists then just go into that TrieNode n coninue
Basic Idea: Each char is represented as one Node in a Tree. When you reach the leaf_node(all childrens are NULL) or (isEnd=True) at that time u can say you completed a word.

Search

- Initially the root is a TrieNode with all 25 chars as null or {} to support all chars
- Iterate over all chars one by one, if TrieNode[char] is null, create a new TrieNode and point TrieNode[char] to the new Node n continue working on that TrieNode.
- If TrieNode[char] exists then just go into that TrieNode n coninue

"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False
        
    def __str__(self):
        return f"{self.child.keys()}, {self.isEnd}"

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_node = self.root
        for ch in word: 
            if ch not in cur_node.child: # if ch is not a child add it
                cur_node.child[ch] = TrieNode()
            cur_node = cur_node.child[ch] # move to next char and node

        cur_node.isEnd = True # last visited char|node isEnd

    def search(self, word): # exact match of word
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.child: # char not in tree_path
                return False
            cur_node = cur_node.child[ch]
        
        return cur_node.isEnd # We need exact match not substring
        # ex: word to search "real" and in our tree we have "reality", 
        # Here although "real" is substring of "reality" but we did not add word "real" in our Trie

    def print_words_from_node(self, node, cur_word=""):
        for ch, tNode in node.child.items(): # iterate all the nodes
            self.print_words_from_node(tNode, cur_word+ch)

        if node.isEnd: # only print in case 
            self.prefixes.append(cur_word)
        
    def prefix_search(self, prefix_key): # return all words starting with given key
        cur = self.root
        self.prefixes = []
        for i, ch in enumerate(prefix_key): # traverse prefix_key first
            if i == len(prefix_key)-1 and cur.isEnd:  # if prefix itself is a word
                self.prefixes.append(prefix_key)
                
            if ch not in cur.child: # in case prefix doesnt exist
                return []
            cur = cur.child[ch]
        
        self.print_words_from_node(cur,cur_word=prefix_key)
        return self.prefixes