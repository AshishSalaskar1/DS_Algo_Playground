"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 
"""

class Solution:
    def findCircleNum(self, arr: List[List[int]]) -> int:
        n = len(arr) 
        vis = set()
        provinces = 0

        for i in range(n):
            cur_root = i
            if cur_root in vis: # if this node isnt visited then count+1
                continue
            
            provinces += 1

            q = [i]
            while len(q) != 0:
                cur = q.pop(0)
                for j in range(n):
                    if arr[cur][j] == 1 and j not in vis:
                        vis.add(j)
                        q.append(j)
        
        return provinces