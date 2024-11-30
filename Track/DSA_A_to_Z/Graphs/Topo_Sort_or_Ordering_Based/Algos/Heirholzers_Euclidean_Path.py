"""
PROBLEM: https://leetcode.com/problems/reconstruct-itinerary/

SOLUTION: https://leetcode.com/problems/reconstruct-itinerary/solutions/3576873/using-eulerian-circuit


EULERIAN PATH: Path such that you start at a node and then be able to visit all nodes exactly once (some questions allow to-fro movements also)
EULERIAN CIRC

DOCS: https://leetcode.com/problems/valid-arrangement-of-pairs/editorial/?envType=problem-list-v2&envId=eulerian-circuit

Step 1: CHECK IF THERE IS AN EULERIAN PATH: https://liuzhenglaichn.gitbook.io/algorithm/graph/eulerian-path
Step 2: Check if if there is any Eulerian Circuit
Step 3: Print the EULERIAN PATH using Hierholzer’s Algorithm

SOLUTIONS:
- This problem is solution of EULERIAN PATH using Hierholzer’s Algorithm.
- Here the starting node is "JFK", we are not bothered about ending node and you can visit nodes more than once

Hierholzer’s Algorithm
- Start from a node lets say "u" ( you already know that if u start at "u", you will form a Euclerian Path)
- Visit all nodes you can go from current node
    - if there are neighboring nodes -> add those to stack
    - if all nodes are exhausted, push stack.top() to the path -> means you have reached the final node (DEST NODE)
- The path is a stack, DEST_NODE is at bottom and SRC_NODE is at top
    - So result = REVERSE(path)

"""

from collections import deque, defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        

        # reversing is needed since you need smallest order (but reverse since your path taken as src<-dest)
        for node in adj:
            adj[node].sort(reverse=True)
        
        start = "JFK"
        path, stack = [], [start]
        while stack:
            cur = stack[-1]
            if adj[cur]:
                stack.append(adj[cur].pop())
            else: # this is the last destination in this path
                path.append(stack.pop())
        
        return path[::-1]
        



        