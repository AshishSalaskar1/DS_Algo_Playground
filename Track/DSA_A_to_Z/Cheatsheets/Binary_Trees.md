# Binary Trees Cheatsheet

Traversals
- DFS: preorder, inorder, postorder (iterative stacks or recursion)
- BFS: level-order with queue; zigzag via level parity

Common tasks
- Max depth, diameter (track height and best)
- Balanced check (height=-1 sentinel on imbalance)
- LCA classic (recursive: return node if match; bubble up non-null children)
- Path sums (root-to-leaf sums; path existence)
- View problems (top/bottom/left/right using BFS columns)

Transformations
- Serialize/deserialize (level-order with None markers)
- Build from traversals (pre+in, post+in)

Edge cases
- Null roots; single node
- Repeated values: for LCA, node identity vs value

# Binary Trees Cheatsheet (verbatim snippets)

LCA Classic (from Binary Trees/LCA_Classic.py)
```python
class Solution:

    def solve(self, root: TreeNode, p, q):
        if root is None or root.data in set([p.data,q.data]):
            return root
        
        left, right = self.solve(root.left,p,q), self.solve(root.right,p,q)
        
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root

    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        return self.solve(root, p,q)
```

See folder for diameter, serialize/deserialize, symmetry, max width, views, etc.

---

## 🗺️ Quick map
- 🌳 Traversals (DFS/BFS)
- 🔗 LCA (general tree)
- 🧠 Recursion patterns and base cases

## ✅ Study checklist
- [ ] Null checks in recursion at top?
- [ ] Combine-left-right results consistently?
- [ ] Depth/height computed with correct base?
