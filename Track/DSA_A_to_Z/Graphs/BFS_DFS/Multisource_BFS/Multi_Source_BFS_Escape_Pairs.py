"""
Example 1: Start -> Escape pairs
=> ANY_OF_THESE_NODES = Escape nodes
- Multi-source on this gives: shortest distance from any start node "S", to any escape node "E"
- Here you can use any escape and you dont have to tell which node you escape from ( this would need you to maintain some kind of a route map)
"""
from collections import deque

def solve(arr):
    nr, nc = len(arr), len(arr[0])
    escape_q = deque()
    start_end_maps = {}

    # Multi source BFS on all escapes 
    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == "E":
                escape_q.append((i,j,0))
            elif arr[i][j] == "S":
                start_end_maps[(i,j)] = float("inf")
    
    
    vis = set()
    while len(escape_q) != 0:
        i,j,dist = escape_q.popleft()
        vis.add((i,j))
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nextr, nextc = i+dx, j+dy
            if nextr>=0 and nextc>=0 and nextr<nr and nextc<nc and arr[i][j]!="X" and (nextr,nextc) not in vis:
                if (nextr,nextc) in start_end_maps:
                    start_end_maps[(nextr,nextc)] = min(dist+1,start_end_maps[(nextr,nextc)])
                escape_q.append((nextr,nextc,1+dist))
    
    return start_end_maps

arr = [
	["0","0","0","X","E"],
    ["X","S","0","X","0"],
    ["S","0","0","X","0"],
    ["0","X","0","0","0"],
    ["0","0","0","0","0"],
    ["0","X","E","X","0"],
    ["0","X","X","0","S"],
    ["0","X","0","E","0"],
    ["S","0","0","0","0"],
]

res = solve(arr)
print(res)