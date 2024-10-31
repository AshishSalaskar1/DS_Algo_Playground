## Trees (Not BINARY TREES, more like graphs)

- Here we assume trees are given in graph representation. Like src->dest (not in Node, root format)
- `adj[i]=j` -> `i` is the **node index**, and indicates an edge from **node-i to node-j**
- `val[i]=some_val` -> in case the tree nodes store some value (like string or number)
- 💡 No concept of Pre, Post or In order since we dont have any ordering amongst children. Just like graph

<br><br>
**Note**:
- **Node indexes** cant be repeating. Consider them as graph nodes
- Values of nodes however can repeat. It can be any arbitary value
- **Binary Tree - Node Class to this form**
- Possible easily if `node.val` are always unique (which often is not true)
<br><br>
- While doing `DFS` we precompute metaData like `Depth`, `SubtreeNodeCount`, `Parent`, `isLeaf`
- Here, 1 in considered as root. Same thing can be done in BFS also , but you cant get `SubtreeNodeCount` easily
  ```python
  class Tree:
      def __init__(self, n) -> None:
          self.adj = [list() for _ in range(n+1)] # DONT DO [list()]*n
          self.par = [0]*(n+1)
          self.val = [0]*(n+1)
          self.depth = [0]*(n+1)
          self.isLeaf = [False]*(n+1)
          self.nChild = [0]*(n+1)
          self.subTreeSum = [0]*(n+1)

      def dfs(self, node, parent, depth):
          self.depth[node] = depth
          self.par[node] = parent

          self.nChild[node] = 0
          self.subTreeSum[node] = 1
          for child in self.adj[node]:
              if child!=parent:
                  self.nChild[node] += 1
                  self.dfs(child, node, depth+1)
                  self.subTreeSum[node] += self.subTreeSum[child]

          if self.nChild[node] == 0:
              self.isLeaf[node] = False

  tree = Tree(10)
  tree_edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9)]

  for u,v in tree_edges:
      tree.adj[u].append(v)
      tree.adj[v].append(u)

  tree.dfs(1,0,1)
  ```
