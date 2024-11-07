
"""
         10(1)
       /       \
   20(2)       8(8)
   /    \      /  \
5(3)   1(4)   9(9) 10(10)
      /  |  \
   8(5) 5(6) 12(7)

"""
class Tree:
    def __init__(self, n, arr) -> None:
        self.n = n+1
        self.adj = [[] for _ in range(n+1)]
        self.val = arr

    def euler_dfs(self, node, parent):
        
        self.time += 1 # IMP
        self.intime[node] = self.time
        self.path.append(node)
        self.subtreesum.append(self.val[node])

        for child in self.adj[node]:
            if child != parent:
                self.euler_dfs(child, node)

        self.time += 1 # IMP
        self.outtime[node] = self.time
        self.path.append(node)
        self.subtreesum.append(-self.val[node])


    def euler_tour(self, root):
        self.intime = [0]*self.n
        self.outtime = [0]*self.n
        self.time = 0
        self.subtreesum = []

        self.path = [-1]

        self.euler_dfs(root, -1)



#       0   1   2  3  4  5  6  7   8  9  10
arr = [-1, 10, 20, 5, 1, 8, 5, 12, 8, 9, 10]

edges = [(1,2),(1,8),(2,3),(2,4),(4,5),(4,6),(4,7),(8,9),(8,10)]

tree = Tree(len(arr), arr)

for u,v in edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)

tree.euler_tour(1)


print(list(range(tree.n)))
print(tree.val)
print(tree.intime)
print(tree.outtime)
print(tree.path)
print(list(range(len(tree.path))))
print(tree.subtreesum)


"""
INDEX: [0,  1,   2, 3,  4, 5, 6, 7,  8,  9,  10, 11]
VALS:  [-1, 10, 20, 5,  1, 8, 5, 12, 8,  9,  10, -1]
IN:    [0,   1,  2, 3,  5, 6, 8, 10, 14, 15, 17,  0]
OUT    [0,  20, 13, 4, 12, 7, 9, 11, 19, 16, 18,  0]

TIME FRAME:
[0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
[-1, 1, 2, 3, 3, 4, 5, 5, 6, 6,  7,  7,  4,  2,  8,  9,  9, 10, 10, 8,   1] # THESE ARE NODE INDEXES


OBSERVATIONS:
- Is node `i` an ancestor of `j`: 
    If node `j` lies in subtree of node `i`.  then (intime[j],outtime[j]) lies within (intime[i],outtime[i])
- All ancestors of `i`
    - Consider this as intervals (in,out) for each node is plotted
    - Ancestors of `i`, is all the intervals that intime[i] cuts 

"""




