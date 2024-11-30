"""
PROBLEM: https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/descriptio

SOLUTION:
- dp[i] = num of steps needed to travel from 0 -> i
- incoming_edges[i] = all nodes which have edge and reach i

- for each src,dest query:
    - Add incoming_edges[dest].append(src)
    - Iterate through [dest,N]:
        - Update dp[i] by visiting all its incoming edges

Optimization Required: 
- You calculate for each incoming edge, which can be repititive
- You cant just iterate on the [src,dest] connection since a prev connection might affect the ahead paths

"""
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []

        # dp[i] = num of steps needed to travel from 0 -> i
        dp = list(range(n))
        incoming_paths = [set([i-1]) for i in dp] # each node has one incoming node from previous_node (EXCEPT 0)
        incoming_paths[0] = []

        for [src, dest] in queries:
            incoming_paths[dest].add(src)
            # for [dest,N] for each node, iterate all its possible incoming edges
            for i in range(dest, n):
                for prev_node in incoming_paths[i]: # check all the incoming edges for the node i
                    dp[i] = min(dp[i], dp[prev_node]+1 )
            
            res.append( dp[n-1] )
        
        return res



        

        



        
        