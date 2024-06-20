"""
PROBLEM: Evaluate Division
https://leetcode.com/problems/evaluate-division/

- You are given list of a/b=c values.
- Now you are given list of new pairs for which you need to find x/y

=> SOLUTION:
Cases in new queries
1. a/b = either of these are not seen -> return -1
2. a/a = a is seen then return 1
3. a/c = a and c both are seen then return (a/x2)*(x2/x3)*....*(xn/c) 

GRAPH REPRESENTATION
- a/b = a -(a/b)-> b
- b/a = a <-(b/a)- a

-> Let say you get new query- x/y
- Check if both x and y are seen,
- x/y = DFS from x to y (multiply each path val to get final)

Example:
INPUT: a/b=1, b/c=2, c/d=6
a->b = 1, b->a=1
b->c=2, c->b=0,5
c->d=6, d->c=0.16666

QUERY: a/d
DFS(a->d) => (a->b) * (b->c) * (c->d)
          => 1 * 2 * 6 = 12
    
a/b * b/c = a/c * c/d = a/c = 12
"""

from collections import deque
class Solution:
    def dfs(self, adj: dict[str, list], src: int, dest:int) -> int:
        q = [(src,1)]
        vis = set([src])

        while len(q) != 0:
            node, pathval = q.pop()
            for nbr,wt in adj[node]:
                if nbr not in vis:
                    if nbr == dest: # you reached destination
                        return pathval*wt
                    q.append( (nbr,pathval*wt) )
                    vis.add(nbr)
        
        return -1.0 # cant reach destination


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        adj = {}
        for i in range(len(equations)):
            val = values[i]
            [u,v] = equations[i]
            
            variables.add(u)
            variables.add(v)
            adj[u] = [*adj.get(u,[]),(v,val)] # a/b = val 
            adj[v] = [*adj.get(v,[]),(u,1/val)] # b/a = 1/val

        res = []
        for [x,y] in queries:
            if x not in variables or y not in variables:
                res.append(-1)
            elif x==y:
                res.append(1)
            else:
                src,dest = x,y
                res.append(self.dfs(adj, src, dest))
        
        return res
                
