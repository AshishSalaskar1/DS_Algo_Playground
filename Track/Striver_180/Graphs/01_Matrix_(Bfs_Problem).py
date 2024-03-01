"""
LINK: https://www.codingninjas.com/studio/problems/distance-of-nearest-cell-having-1-in-a-binary-matrix_1169913

SOLUTION 1: SLOWER:
    - do BFS from each node, first 1 you encounter will the nearest
    - calculate distance and stop any more BFS

SOLUTION 2: FASTER
- Instead of visiting each 0 n finding nearest 1, start from 1 n do BFS. When doing BFS go on updating distances
- Since BFS always visits nearest level, theres no need to maintain a min distance.
  First time u visit a node 0 from 1, u can considered its the nearest 0<->1
"""

def nearest(arr, nr, nc):
    dist = [[0 for _ in range(nc)] for _ in range(nr)]
    q = [] # ( (i,j), distance from src 1 where u started)
    vis = set()

    for i in range(nr):
        for j in range(nc):
            # 1 means its already visited (dist will be 0)
            if arr[i][j] == 1:
                q.append( ((i,j),0) )
                vis.add((i,j))

    while len(q) != 0:
        curr_cords, cur_dist = q.pop(0)
        x1,y1 = curr_cords
        dist[x1][y1] = cur_dist

        xdelta = [0,1,0,-1]
        ydelta = [1,0,-1,0]

        for xd,yd in zip(xdelta, ydelta):
            x2, y2 = x1+xd, y1+yd
            if x2<nr and y2<nc and x2>=0 and y2>=0 and (x2,y2) not in vis:
                q.append( ((x2,y2), cur_dist+1) )
                vis.add((x2,y2))
                # dist[x2][y2] = cur_dist+1

    return dist



arr = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 0]
]

# desired
# 3 2 1 0
# 2 1 0 0
# 1 0 0 1
#
print(nearest(arr, len(arr), len(arr[0])))