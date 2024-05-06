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
        
def has_no_children(self, node): # check is node as no further children (last node in path)
        for child in node.child.values():
            if child is not None:
                return False
        return True 
    
def delete_util(self, root, word, i):
    # print(f'{word} -> {i}')
    if root is None:
        return None

    if i == len(word): # char is last in word
        print(f'LAST {root}',self.has_no_children(root))
        root.isEnd = True
        if self.has_no_children(root): # no more chars further
            root = None
        return root


    ch = word[i]
    print(f'MID Before {word}-> {word[i]} -> {root.child}')
    root.child[ch] = self.delete_util(root.child[ch], word, i+1)
    print("MID",word[i], root.child,self.has_no_children(root),not root.isEnd)

    if self.has_no_children(root) and not root.isEnd: # check if cur_node after deletion is not needed (no children and its not last of any other word)
        del roo
    return root

def delete(self,word):
    # print("START:", self.root)
    self.root = self.delete_util(self.root, word,0)
    print(self.root.child)
    # print("END: ",self.delete_util(self.root, word,0))
    # print("END:", self.root)