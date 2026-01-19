"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

    def _search(self, node: TrieNode, word: str) -> bool:
        # Base case
        if not word:
            return node.is_end

        ch = word[0]

        if ch != ".":
            if ch not in node.children: return False
            return self._search(node.children[ch], word[1:])
        else:
            # Wildcard: try all children
            for child in node.children.values():
                if self._search(child, word[1:]): return True
            return False
