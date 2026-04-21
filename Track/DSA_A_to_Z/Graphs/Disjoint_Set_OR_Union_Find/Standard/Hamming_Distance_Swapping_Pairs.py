"""
https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/?envType=daily-question&envId=2026-04-21


LOGIC:
- If nodes are in one component -> then they are transitive which means you can replace any one with any other one

STEPS
- Somehow find all connected nodes -> Either DSU or DFS
- For each group
    - Count the frequency of each nodes(indexes) -> their values in source
    - Count the frequency of each nodes(indexes) -> their values in target
    - Diff you see is the hamming distance 
    - WHY ONLY INDEX? We need values n not index itself

"""
from collections import defaultdict

class DSU:
    def __init__(self):
        self.par = {}
        self.size = {}

    def find_par(self, u: int):
        # Some node that you didnt union -> add it separately
        if u not in self.par:
            return u

        if u == self.par[u]:
            return u

        self.par[u] = self.find_par(self.par[u])
        return self.par[u]

    def union(self, u:int, v: int ):
        for node in [u,v]:
            if node not in self.par:
                self.par[node] = node
                self.size[node] = 1

        upu = self.find_par(u)
        upv = self.find_par(v)

        if upu == upv: # already belong to same component
            return


        if self.size[upu] < self.size[upv]: # if size(u) < size(v) -> attach comp(u) to v
            self.par[upu] = upv
            self.size[upv] += self.size[upu]
        else: # if size(v) < size(u) -> attach component of v to u
            self.par[upv] = upu
            self.size[upu] += self.size[upv]



class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = DSU()
        n = len(source)
        for u,v in allowedSwaps:
            uf.union(u,v)
        
        # gather nodes in each component
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find_par(i)].append(i)

        ans = 0

        for idxs in groups.values():
            freq = defaultdict(int)
            for i in idxs: freq[source[i]] += 1

            for i in idxs:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1

        return ans
