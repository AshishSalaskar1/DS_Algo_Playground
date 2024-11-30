"""
Problem: https://leetcode.com/problems/valid-arrangement-of-pairs/?envType=problem-list-v2&envId=eulerian-circuit
Solution: https://liuzhenglaichn.gitbook.io/algorithm/graph/eulerian-path

Detailed Editorial: https://leetcode.com/problems/valid-arrangement-of-pairs/editorial/?envType=problem-list-v2&envId=eulerian-circuit

"""
from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Initialize variables
        graph = defaultdict(list)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        # Build graph, indegree, and outdegree
        for u, v in pairs:
            graph[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1

        # Find the start node
        start = -1
        for node in graph:
            if outdegree[node] - indegree[node] == 1:
                start = node
                break
        if start == -1:
            start = pairs[0][0]

        # Eulerian path using Hoerichers algo
        path = []
        stack = [start]
        while stack:
            node = stack[-1]
            if graph[node]:
                stack.append(graph[node].pop())
            else:
                path.append(stack.pop())


        # def euler(u):
        #     while graph[u]:
        #         v = graph[u].pop()
        #         euler(v)
        #         ans.append([u, v])

        # euler(start)

        # Construct the result in the correct order
        result = []
        for i in range(len(path) - 1, 0, -1):
            result.append([path[i], path[i - 1]])

        return result
