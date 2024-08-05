"""
PROBLEM: https://cses.fi/problemset/result/10090975/
"""

import sys
sys.setrecursionlimit(300000)  # Increase the recursion limit
 
class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
 
 
def euler_tour(node, parent, graph, values, entry, exit, tour, timer):
    timer[0] += 1
    entry[node] = timer[0]
    tour[timer[0]] = values[node]
    
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        euler_tour(neighbor, node, graph, values, entry, exit, tour, timer)
    
    exit[node] = timer[0]
 
 
def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    q = int(data[idx + 1])
    idx += 2
    
    values = [0] * (n + 1)
    for i in range(1, n + 1):
        values[i] = int(data[idx])
        idx += 1
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        graph[a].append(b)
        graph[b].append(a)
    
    queries = []
    for _ in range(q):
        query = data[idx]
        s = int(data[idx + 1])
        if query == '1':
            x = int(data[idx + 2])
            queries.append((1, s, x))
            idx += 3
        else:
            queries.append((2, s))
            idx += 2
    
    entry = [0] * (n + 1)
    exit = [0] * (n + 1)
    tour = [0] * (2 * n + 1)
    timer = [0]
    
    euler_tour(1, -1, graph, values, entry, exit, tour, timer)
    
    fenwick_tree = FenwickTree(2 * n)
    for i in range(1, n + 1):
        fenwick_tree.update(entry[i], values[i])
    
    result = []
    for query in queries:
        if query[0] == 1:
            s, x = query[1], query[2]
            current_value = tour[entry[s]]
            delta = x - current_value
            tour[entry[s]] = x
            fenwick_tree.update(entry[s], delta)
        else:
            s = query[1]
            result.append(fenwick_tree.range_query(entry[s], exit[s]))
    
    print('\n'.join(map(str, result)))
 
 
if __name__ == "__main__":
    main()