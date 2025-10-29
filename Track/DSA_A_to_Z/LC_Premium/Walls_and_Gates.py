"""
You are given an m x n grid rooms initialized with these three possible values.



1) -1: A wall or an obstacle.
2) 0: A gate.
3) INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


Example 1:
Input: rooms = [
 [2147483647,-1,0,2147483647],
 [2147483647,2147483647,2147483647,-1],
 [2147483647,-1,2147483647,-1],
 [0,-1,2147483647,2147483647]
]

Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

SOLUTION:
- BRUTE: Iterate every cell, if its a EMPTY ROOM -> RUN BFS(i,j -> nearest exit gate). 
    -TC: O(num_empty_rooms)*O(BFS)  = O(nr*nc)*O(nr*nc)

- OPTIMIZED: Multi-source BFS
    - You need nearest dist to a empty from any gate
    - Put all gates into queue and run BFS -> the empty room you reach first will be the nearest gate for that


"""


from collections import deque, defaultdict
class Solution(object):
    def wallsAndGates(self, arr):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # Your code goes here

        nr, nc = len(arr), len(arr[0])

        q = deque()
        vis = set()
        for i in range(nr):
            for j in range(nc):
                if arr[i][j] == 0:
                    q.append((i, j, 0 )) # <row, col, steps_needed_to_reach_gate>
                    vis.add((i,j))
        
        while q:
            r,c,steps = q.popleft()

            if arr[r][c] == 2147483647:
                arr[r][c] = steps
            
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nextr, nextc  = r+dx, c+dy

                if nextr>=0 and nextc>=0 and nextr<nr and nextc<nc and arr[nextr][nextc]!=-1 and (nextr,nextc) not in vis:
                    q.append((nextr, nextc, steps+1))
                    vis.add((nextr, nextc))
        
        return arr