
"""
Question: There are n cities and m edges connected by some number of flights. You are given an array of flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost price. You have also given three integers src, dst, and k, and return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


INTUITION
- Normal Dijkstras + PQ wont work => Q with (stops,udist,node)
- "k" stops means k+1 nodes visited (0->1->2 : 2 stops)


- Why PriorityQueue (udist, node, stops) will fail: Because it might happen that we arrive at some node at a  lesser distance but number of stops taken can be more and hence we can't move further to destination. (it will prioritize dist but ignore stops)
- PQ (stops, udist, node) will work, but since we add stops incrementally QUEUE can also suffice (THIS IS LIKE BFS, STEPS INCREASE + 1 when added)


Good Question: Why to store udist in Q when we can get it from dist[v]
- MISCONCEPTION: we can save some space in the queue nd do queue<pair<stop,node>>  coz distance is already obtainable from dis[ ], so why maintain it specifically in the queue?

Short Ans: 
- In queue the udist is path till "u" coming from a certain path
- If you take dist[u] it will be shortest till now, wont count this new path. Who knows this path is better

ANS: no coz in the queue we store the distance coming from a specific parent node ie a particular path , nd that path is used for further exploration when we take it out of the queue nd consider that paths distance ...but there can be other paths as well...dis[ ] can't maintain the paths, it just stores the path with minimum distance, which may not guarantee the path with least stops(which is our top priority)...hence we have to maintain the instance of the distance of a particular node in the queue


"""

# THIS DOESNT WORK --> TLE
class Solution:
    def create_adj(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
        
        return adj

    def findCheapestPrice(self, V: int, flights: List[List[int]], src: int, dest: int, k: int) -> int:
        q = []
        dist = [float("inf") for _ in range(V)]
        dist[src]=0
        adj = self.create_adj(V, flights)

        q.append((0, 0, src)) # (stops, dist, node)

        while len(q) != 0:
            ustops, udist, u = q.pop(0)
            for v, wt in adj[u]:
                # k and not K=1 why? k stops means k+1 nodes visited (0->1->2 : 2 stops)
                if ustops<=k and udist+wt < dist[v]:
                    dist[v] = udist+wt 
                    q.append((ustops+1, udist+wt, v))
        
        return dist[dest] if dist[dest] != float("inf") else -1


# WORKING SOLUTIOn
"""
WHY IT WORKS?
Bellman Ford: You allow V-1 iterations/hops. Ideally means you want to allow each node to connect to all possible nodes

HERE -> You limit it to K
THAT MEANS: You are allowing only K hops/flights. Now each of them minimized will add up to minimized cost too


"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, K: int) -> int:
        INF = float('inf')
        cost = [INF] * n
        cost[src] = 0

        # Allow up to K + 1 flights (i.e., K stops)
        for _ in range(K + 1):
            tmp = cost[:]  # snapshot of current best costs
            for u, v, w in flights:
                if cost[u] != INF and cost[u] + w < tmp[v]:
                    tmp[v] = cost[u] + w
            cost = tmp

        return -1 if cost[dst] == INF else cost[dst]
