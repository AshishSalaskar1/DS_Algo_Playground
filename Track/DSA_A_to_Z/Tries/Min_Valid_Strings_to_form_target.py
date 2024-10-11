"""
Problem: https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/
Solution: https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/solutions/5788470/dp-bhi-lagega-trie-bhi-lagega-aaiye-bc-dekhte-hai-maza-aaega/

INTUITION:
-> BRUTE FORCE
- start at index i -> check all possible prefixes which start from i -> pick each solve other part
words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

i = 0
susbtrings which start at i and are prefixes of words: [a, aa]

i = 1 -> picked "a" => next options ("a","abc")
i = 2 -> picked "aa" => next options ("bcd")


SOLUTION:
fn(i) -> min words needed to make the target from index [i:n]

dp(idx):
 res = INF
 - check max string from idx -> n
    if its a prefix -> consider current word taken ends here + dp(i) # here i is length of prefix taken
    root = root.childs[ch]
 - At any point if not there in Trie -> break (no prefix till here means further also you wont find a prefix)
 - We check for each possible prefix and not the longest one at each iteration (Try all possible combinations)

"""
class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isend = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.childs:
                root.childs[ch] = TrieNode()
            root = root.childs[ch]
        
        root.isend = True

class Solution:
    @cache
    def dp(self, idx: int, trie_root: TrieNode) -> float:
        """
            This means substrings have been created upto 0...i (including i) 
        """
        if idx == self.n: # string already created till i (including i) 
            return 0 
        
        res = float("inf")
        root = trie_root

        for i in range(idx, self.n):
            ch = self.target[i]
            if ch not in root.childs:
                break

            root = root.childs[ch]
            solve_after = self.dp(i+1, trie_root)

            # why 1? you are ending your substring word here so 1 + (later dp solutions)
            if solve_after != float("inf"):
                res = min(res, 1 + solve_after) 
            
        return res

    def minValidStrings(self, words: List[str], target: str) -> int:
        if set(target) == "a":
            return 1
            
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        self.n = len(target)
        self.target = target

        min_ways = self.dp(0, trie.root)
        # print(min_ways)
        return -1 if min_ways == float("inf") else min_ways
        
        