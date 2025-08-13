# Tries Cheatsheet (verbatim)

Trie implementation with insert, search, and prefix search (from Tries/Implement_Trie.py)
```python
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
```

Delete operation scaffolding (from Tries/Trie_Delete_operation.py)
```python
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
        
# has_no_children, delete_util, and delete methods outline:
# def has_no_children(self, node):
#     for child in node.child.values():
#         if child is not None:
#             return False
#     return True 
# 
# def delete_util(self, root, word, i):
#     if root is None:
#         return None
#     if i == len(word):
#         root.isEnd = True
#         if self.has_no_children(root):
#             root = None
#         return root
#     ch = word[i]
#     root.child[ch] = self.delete_util(root.child[ch], word, i+1)
#     if self.has_no_children(root) and not root.isEnd:
#         del roo
#     return root
# 
# def delete(self,word):
#     self.root = self.delete_util(self.root, word,0)
```

---

## 🗺️ Quick map
- 📚 Insert/search/prefix
- 🧹 Delete scaffolding
- 🔡 Variants (char/bitwise)

## ✅ Study checklist
- [ ] End-of-word flags vs path existence understood?
- [ ] Prefix search returns only full words?
- [ ] Deletion handles shared prefixes safely?
