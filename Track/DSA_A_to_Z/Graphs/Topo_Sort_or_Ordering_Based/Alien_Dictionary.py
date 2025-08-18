# Input: N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output: b d a c

# Input: N = 3, K = 3
# dict = {"caa","aaa","aab"}

"""
Intuition behind getting order:
    - Compare between two subsequent strings, first char mismatch means bcoz of this char s1 came earlier than s2
    - So char1 -> char2 (char2 comes after char1)
    
Toposort:
    - Run simple topo sort on these adjacency list

When you cant create dict
1. s2 comes after s1, but len(s2)>len(s1) - this doesnt make any sense 
2. Edge case -> in case some char does have any dependency (it becomes single island in the graph) -> just add it before topo sort order
   Ex: k=5, so for sure you need to have a,b,c,d,e ( `e` may not be part of any edge, simply put it, indegree==0, will be added to topo sort first)
   - Why needed? Your answer dict should have first "K" alphabets, doesnt matter if they dont appear in the edges

IMPORTANT NOTE:
- DONT USE `defaultdict` -> since in that case you wont be able to account "e":[] <or might be used also>
"""


from collections import defaultdict
from queue import deque

class Solution:
    def alien_dict(self, dictionary: list[str], K):
        adj = {}
        indegree = {}


        adj = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(1, len(dictionary)):
            prevw, curw = dictionary[i-1], dictionary[i]
            for j in range(min(len(prevw), len(curw))):
                if prevw[j] != curw[j]:
                    adj[prevw[j]].append(curw[j])
                    indegree[curw[j]] += 1
                    break
        
        return adj, indegree


    def findOrder(self, dictionary, N, K):
        adj, indegree = self.get_adj(dictionary, K)
        q = deque()

        for node in adj.keys():
            if indegree[node]  == 0:
                q.append(node)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        
        return "".join(res)
 
       



sol = Solution()

arr = ["baa","abcd","abca","cab","cad"]
N = len(arr)
k = 4 # no of alphabets in the dictionary
print(sol.alien_dict(arr, k))

arr = ["caa","aaa","aab"]
N = 3
K = 3 # no of alphabets in the dictionary
print(sol.alien_dict(arr, k))
