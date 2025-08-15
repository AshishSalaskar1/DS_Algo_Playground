"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.


IMP CONSIDERATIONS:
1. You can have self edges
2. You can have >1 edge between u,v | one of each color
3. You can visit any node any number of times, given you mantain the adjacent color rule
   - Ex: 0 -B-> 1 -------
   - Here assume, you take some loopy way and come join back to 1. You can ONLY visit back with a "RED" edge. 
   - If you come with "B" then  0 -B-> 1 (---adjacent_trips--) -B-> 1  [ VIOLATES]
   - You can come with "R" then 0 -B-> 1 (---adjacent_trips--) -R-> 1  [ DOESNT VIOLATES]

INTUITION:
- From (3) its clear that you can visit each node 2 times at max (once with incoming "red" edge and another time with "blue" incoming edge)
- CONSIDER (NODE_INDEX, INCOMING_EDGE_COLOR) as 2 NODES LOGICALLY


IMP CASE:
n=5
red = [ (0,1), (1,2), (2,3), (3,4)]
blue = [ (1,2), (2,3), (3,1)]
  
       0 1 2 3 4
ANS = [0,1,2,3,7]

"""

from queue import deque
from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adjr, adjb = defaultdict(list), defaultdict(list)

        for u,v in redEdges: adjr[u].append(v)
        for u,v in blueEdges: adjb[u].append(v)
        dist = [float("inf") for _ in range(n)]

        q = deque()
        q.append((0,-1, 0)) # (node, incoming_edge_color, dist) => ideally you can visit same node via 2 colors
        seen = set()
        # seen.add((0,"red"),(0,"blue"))

        while len(q) > 0:
            node, prev_edge_color, cur_dist = q.popleft()
            dist[node] = min(dist[node], cur_dist)

            if prev_edge_color == "red" or prev_edge_color == -1:
                for v in adjb[node]:
                    if (v,"blue") not in seen:
                        q.append((v,"blue",cur_dist+1))
                        seen.add((v,"blue"))
            if prev_edge_color == "blue" or prev_edge_color == -1:
                for v in adjr[node]:
                    if (v,"red") not in seen:
                        q.append((v,"red",cur_dist+1))
                        seen.add((v,"red"))
        
        return [x if x!=float("inf") else -1 for x in dist]
                

