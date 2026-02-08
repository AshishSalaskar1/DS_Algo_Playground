"""
https://leetcode.com/problems/word-search-ii/

BRUTE FORCE:
- At every point run DFS with Backtracking -> generate all words -> check if present

WHY BACKTRACK?
- In DFS once you visit the node you dont visit again, but here we want each path to be visited
   a
  / \
 b   c
 |   |
 e   f

- Normal DFS: a->b->e->c->f
- What we want: a->b->e | a->c->f ....

OPTIMIZATIONS - PRUNING:
- Can you avoid running DFS from each cell? NOOO ( no way to escape this )
- Can you optimize it? YESSS
    - We need someway to prune or stop our DFS
    - How do we do that? We can stop when the string forming is not same as words or exceeding their lengths
    - SOLUTION: USE TRIE PURELY AS LOOKUP FOR PRUNING

SOLUTION:
- Create a Trie and put in all the words
- Run DFS from each node
    - Check if the character matches anything in Trie -> else stop
    - Check if its end of word in Trie --> ADD IN TRIE



"""
from typing import List

class TrieNode:
    def __init__(self):
        self.end = False
        self.childs = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.childs:
                cur.childs[ch] = TrieNode()
            cur = cur.childs[ch]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nr, nc = len(board), len(board[0])
        res = set()         
        trie = Trie()

        for word in words:
            trie.add_word(word)

        def dfs(r: int, c: int, node: TrieNode, curword: str) -> None:
            ch = board[r][c]
            if ch not in node.childs: # PRUNE if TRIE no longer matches
                return
            
            node = node.childs[ch] # you have moved to the next node
            curword += ch

            if node.end:
                res.add(curword)

            seen.add((r, c))

            for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
                newr, newc = r + dx, c + dy
                if 0 <= newr < nr and 0 <= newc < nc and (newr, newc) not in seen:
                    dfs(newr, newc, node, curword)

            seen.remove((r, c))   # backtrack

        for i in range(nr):
            for j in range(nc):
                seen = set()
                dfs(i, j, trie.root, "")

        return list(res)
