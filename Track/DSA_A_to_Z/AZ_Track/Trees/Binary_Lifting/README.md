# Binary Lifting


## Why you need Binary Lifting
Lets say you have a data structure which holds only the next item in its memory. But you have each of the elements directly accessible (Ex: stored in a hashmap)
Ex: LinkedList having `n` nodes, each node stores the next node details. But you have a hash map with all nodes stored such that u can return it

**Task**: Return the `k`th node after a given node lets say `x`. You have huge number of such queries lets say `Q` (Q - 10^6, K - close to N)
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
queries: (2,4) -> 6 (4th element after 2)

**Normal Logic 1: Brute Force**
- For every query `node`,`k`. Start at `node` and then using `k` node.next operations reach `k`
- TC: O(Q*K) => O(QN)
- SC: O(1)


**Normal Logic 2: PreCompute**
- PreStep: For each node `node` calculate all the `k` possible next elements and keep then stored already
- premap = HashMap <Node, HashMap<k, Node> > (For each node you calculate all possible `k`s from `node`)
- For every query `node`,`k`. Return premap[node][k]
- TC: PreStep=O(N*N) Query=O(1)
- SC: O(N*N)

**Mentos Zindagi logic: BINARY LIFTING**
TC and SC: O(QlogN)

## Binary Lifting
- To reach `k` elements after `node`, what if we only have to do at max `logn` jumps/moves?
- We always move from `node` to next `2^i`th node

**PreCompute Step**
- `lift[node][i]` = `2^i`th node after/before `node`
- For each `node` you calculate `lift[node][i]` where `i`:0->19 (2^0 -> 2^19=10^6)

- Compute `next` for each node i.e `lift[node][0]` = parent[node]
- `lift[node][i]` = lift[`lift[node][i-1]`][i-1]

    Example:
    - Moving from node to 2^2 = moving from node to 2^1 + from there move 2^1<br>
        node -> 2^1 = 2 : half = lift[node][i-1]<br>
        half -> 2^1 = 2: final = lift[half][i-1]<br>
    - Moving from node to 2^3 = moving from node to 2^2 + from there move 2^2<br>
        node -> 2^2 = 4 : half = lift[node][i-1]<br>
        half -> 2^2 = 4 : final = lift[half][i-1]<br>
    - So ideally, you each 2^i can be split into node->2^(i-1) and the another 2^(i-1) from there
    Ex: 2^3 = 8 => First 2^2=4 steps from node , then another 4 steps
<br><br>
- **Conclusion**: Given any node `node` you can move in increments of 2 (1,2,4,8...). This gives you `logN` traversal time instead of `N` in older approach

**Query Stage**
- Lets say you want to move `k` steps after `node` but **YOU CAN ONLY MOVE IN iterations of 2 power**
- Solution: **Move according to binary representation of k**

    Ex 1: k=11 <br>
    11 = 1011 <br
    1(8) -> 0(4) -> 1(2) -> 1(1) <br>
    lift[node][3] -> lift[lift[node][3]][1] ->  lift[lift[lift[node][3]][1]][0]

<br><br>
# Applications of binary lifting
## 1. LCA
1. PreCompute your `lift` array: lift = len(nodes) X 19 (we want to store 2^0 to 2^19 for each node)
2. Also, calculate your `depth` array

**LCA Logic** - LCA(u,v)
1. Make sure both nodes are at same level. If not, keep on lifting the larger one untill both are at same level
- In this process of making both levels same, if u==v, then return u (u is ancestor of v)

2. Now try picking the max_jump/k such that `lift[u][i]` != `lift[v][i]`
Why? If you check ancestral chain, from root -> LCA it will have same nodes, then from LCA onwards path changes

3. End of (2) you will be at the highest(lowest level) nodes `u`,`v` such that every levels above them are SAME
- LCA = parent[u] or parent[v] == lift[u][0]

```py

from collections import deque

class Tree:
    def __init__(self, n) -> None:
        self.adj = [list() for _ in range(n+1)] # DONT DO [list()]*n
        self.lift = [[0 for _ in range(20)] for _ in range(n+1)]
        self.val = [0]*(n+1)
        self.depth = [0]*(n+1)

    def dfs(self, node, parent, depth):
        self.depth[node] = depth
        self.lift[node][0] = parent

        # lift from 0->19 : 2^0 -> 2^19 (2^19 is approx equal to 10^6)
        for i in range(1,20):
            self.lift[node][i] = self.lift[self.lift[node][i-1]][i-1]

        for child in self.adj[node]:
            if child!=parent:
                self.dfs(child, node, depth+1)

    def lca(self, u, v):
        print(u,v)
        # make sure depth of u>v =>
        if self.depth[u]<self.depth[v]: u,v= v,u
        print(u,v)

        # bring both nodes to same level/depth = Lift U (since its longer)
        diff_depth = self.depth[u] - self.depth[v]
        for i in range(19,-1,-1):
            # check if ith bit is set in diff_depth
            if diff_depth & (1<<i):
                u = self.lift[u][i] # lift by i, i=bit set

        print("AFTER LEVEL",u,v)
        # in case after reducing level you see both co-incide
        if u==v:    return u

        # lift both by 2^19->2^0 and stop when u!=v
        for i in range(19,-1,-1):
            # if both vals are same, means this loc is before the LCA
            if self.lift[u][i] != self.lift[v][i]:
                u = self.lift[u][i]
                v = self.lift[v][i]

        print("FINAL child of LCA",u,v)
        # now both u,v will be one node below the LCA (at LCA lift[u]==lift[v], so you will be one level below that )
        return self.lift[u][0] # lift(u,0) = parent(u)


tree = Tree(10)
tree_edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9)]

for u,v in tree_edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)

tree.dfs(1,0,1)


print(tree.lca(3,7)) # 2
print(tree.lca(3,9)) # 1
print(tree.lca(3,4)) # 2
print(tree.lca(5,9)) # 1
```


## 2. Some Aggregates between nodes `u` and `v`
- Find GCD of all nodes in path between `u` and `v`
- Find Max/Min/Sum of Nodes in path between `u` and `v`


## Docs
- Leetcode ref: https://leetcode.com/discuss/study-guide/4299594/Binary-Lifting-Technique-A-Beginners-Guide/
