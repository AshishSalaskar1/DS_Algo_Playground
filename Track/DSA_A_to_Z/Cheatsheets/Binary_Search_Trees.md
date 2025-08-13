# Binary Search Trees Cheatsheet

Invariants
- Left < node < right (value-based); duplicates policy must be defined

Ops
- Insert: recurse by value and attach where None
- Search: recurse/iterate by comparing value
- Delete: leaf, one-child, two-children (swap with inorder successor/predecessor then delete)

Traversal uses
- Inorder yields sorted order; iterator with stack simulates

Problems
- Validate BST by range (min,max) constraints
- Recover swapped nodes by finding two anomalies in inorder
- Kth smallest via inorder or augmented counts
- Merge two BSTs by inorders + merge; or simultaneous iterators
- Two-sum in BST via two iterators (asc and desc)

Edge cases
- Duplicates handling consistent across ops
- Skewed trees (tail recursion depth)

# Binary Search Trees Cheatsheet (verbatim snippets)

LCA in BST (from Binary Search Trees/LCA_in_BST.py)
```python
class Solution:
    
    def LCA(self, node, p, q):
        if node is None:
            return None

        if node.val > p.val and node.val > q.val:
            return self.LCA(node.left, p, q)
        elif node.val < p.val and node.val < q.val:
            return self.LCA(node.right, p, q)
        else: # SPLIT POINT 
            return node
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.LCA(root, p, q)
```

BST Iterator (inorder and reverse) (from Binary Search Trees/BST_Iterator.py)
```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_all_left(root)
    
    def push_all_left(self, node: TreeNode):
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right is not None: # if right subtree is not empty
            self.push_all_left(next_node.right)
        return next_node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
```

Reverse order variant (from same file)
```python
class BSTIterator:
    def __init__(self, root: Optional[TreeNode], reverse: bool = False):
        self.stack = []
        self.reverse = reverse
        self.push_all_left(root)

    def push_all_left(self, node: TreeNode):
        cur = node
        while cur:
            self.stack.append(cur)
            if self.reverse is True:
                cur = cur.right
            else:
                cur = cur.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right is not None:
            if self.reverse:
                self.push_all_left(next_node.left)
            else:
                self.push_all_left(next_node.right)
        return next_node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
```

See more in folder: Insert, Delete, Recover Swapped, Valid BST, Kth Smallest, Merge 2 BSTs, Two Sum in BST.

---

## 🗺️ Quick map
- 🌲 BST properties and invariants
- 🧭 LCA in BST using value ordering
- 🔁 BST iterators (inorder/reverse)

## ✅ Study checklist
- [ ] Strictly enforce left<root<right (or define duplicate policy)?
- [ ] Iterator invariants: stack represents path to next element?
- [ ] Edge cases: empty tree, single node, skewed trees.
