"""
Best Solution Video: https://www.youtube.com/watch?v=MfAEfhyD1oM

Problem: https://cses.fi/problemset/result/10853335/

You are given a rooted tree consisting of n nodes. The nodes are numbered 1,2,\ldots,n, and node 1 is the root. Each node has a value.
Your task is to process following types of queries:

change the value of node s to x
calculate the sum of values in the subtree of node s


SOLUTION:


"""
from sys import setrecursionlimit
from collections import defaultdict
 
setrecursionlimit(10**6)
 
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
 
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += (idx & -idx)
 
    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum
 
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
 
class SubtreeQuery:
    def __init__(self, n, node_values, edges):
        self.n = n
        self.values = node_values
        self.adj = defaultdict(list)
        self.start = [0] * (n + 1) # You use 1-based indexing for nodes also (NOT NEEDED)
        self.end = [0] * (n + 1)
        self.euler = []
        self.fenwick_tree = FenwickTree(n)
        self._build_tree(edges)
        self._euler_tour(1, -1, [0])
 
        # Initialize Fenwick Tree with initial values
        for i in range(n):
            self.fenwick_tree.update(self.start[i + 1] + 1, node_values[i])
 
    def _build_tree(self, edges):
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
 
    def _euler_tour(self, node, parent, pos):
        self.euler.append(node)
        self.start[node] = pos[0]
        pos[0] += 1
        for neighbor in self.adj[node]:
            if neighbor != parent:
                self._euler_tour(neighbor, node, pos)
        self.end[node] = pos[0] - 1
 
    def update_value(self, s, x):
        delta = x - self.values[s - 1]
        self.values[s - 1] = x
        self.fenwick_tree.update(self.start[s] + 1, delta)
 
    def subtree_sum(self, s):
        left = self.start[s] + 1
        right = self.end[s] + 1
        return self.fenwick_tree.range_query(left, right)

import sys
with open('Subtree_Queries_IN.txt', 'r') as file:
    sys.stdin = file
    
    # Read input
    data = list(sys.stdin.readline().split())
    print(data)
    n, q = int(data[0]), int(data[1])
    values = list(map(int, sys.stdin.readline().split()))
    print(n, values)
    
    # Edges of the tree
    edges = []
    for _ in range(n - 1):
        data = list(map(int, sys.stdin.readline().split()))
        u, v = int(data[0]), int(data[1])
        edges.append((u, v))
    
    # Initialize SubtreeQuery object
    subtree_query = SubtreeQuery(n, values, edges)
    
    # Process queries
    output = []
    for _ in range(q):
        data = list(map(int, sys.stdin.readline().split()))
        query_type = data[0]
        if query_type == 1:
            s, x = int(data[1]), int(data[2])
            subtree_query.update_value(s, x)
        elif query_type == 2:
            s = int(data[1])
            result = subtree_query.subtree_sum(s)
            output.append(result)
    
    # Print all outputs
    print('\n'.join(map(str, output)))