"""
PROBLEM
You are given a n-ary tree rooted at 1 and each node has some val.

1. If you pick a Node then you cant pick its child
2. If you dont pick node, then you can either pick or not pick its child

We need to find the max sum you can make?

INTUITION
- This is similar to House robber. You cant rob adjcaent houses. 
- You solve that using DP

SOLUTION HERE: SIMILAR, but on Trees


            3(1)
          /   \
         4(2)  5(3)
       /   \     \
      1(4)  3(5)  1(6)

BEST HERE: Pick (2) and (3) = 9

"""

class TreeDP:
    def __init__(self, n, arr):
        self.n = n
        self.val = arr
        self.adj = [[] for _ in range(n+1)]
        # [N+1][2] => [n][1] = pick nth node, [n][0] = dont pick nth node
        self.dp = [[0 for _ in range(2)] for _ in range(n+1)]
    
    def indfs(self, node, par):
        # CONSIDER THESE ARE LEAF NODE - BASE CASES
        # if this was the leaf node, you can either pick/not pick
        self.dp[node][1] = self.val[node] # node is picked
        self.dp[node][0] = 0 # node is not picked

        for child in self.adj[node]:
            if child != par:
                self.indfs(child, node) # this will calculate all the lower child values 

                # picked this node, you cant pick child node 
                self.dp[node][1] += self.dp[child][0] 
                # didnt pick this node, you can either pick child or not 
                self.dp[node][0] += max(self.dp[child][0], self.dp[child][1])  
    
    

arr = [-1, 3, 4, 5, 1, 3, 1]
edges = [(1,2),(1,3),(2,4),(2,5),(3,6)]

tree = TreeDP(10, arr)

for u,v in edges:
    tree.adj[u].append(v)
    tree.adj[v].append(u)


tree.indfs(1,-1)

# max_res from node=1, by either picking or not picking
ans = max(tree.dp[1][0], tree.dp[1][1])
print(ans) # 9



