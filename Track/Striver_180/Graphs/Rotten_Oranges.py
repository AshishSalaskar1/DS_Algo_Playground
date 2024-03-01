"""
Link: https://www.codingninjas.com/studio/problems/rotting-oranges_701655
You have been given a grid containing some oranges. Each cell of this grid has one of the three integers values:

Value 0 - representing an empty cell.
Value 1 - representing a fresh orange.
Value 2 - representing a rotten orange.
Every second, any fresh orange that is adjacent(4-directionally) to a rotten orange becomes rotten.
Your task is to find out the minimum time after which no cell has a fresh orange. If it's impossible to rot all the fresh oranges then print -1.

Sample Input 1:
3 3
2 1 1
1 1 0
0 1 1
Sample Output 1:
4
Explanation of Sample Input 1:
Minimum 4 seconds are required to rot all the oranges in the grid as shown below.

SOLUTION: BFS level order traversal on each rotten
- Initially run add all rotten ones to Q -> It automaitically works as parallel BFS
- Along with (i,j) also store time -> at what time did this orange get rotten
- At last, if all are 2s returns max_time, else return -1

"""

def minTimeToRot(arr, nr, nc):
    q = [] #((i,j),time_step))
    max_time_taken = 0

    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == 2:
                q.append( ((i,j),0) )

    while len(q) != 0:
        cur_index, cur_time = q.pop(0)
        # print(cur_index, cur_time)
        max_time_taken = max(max_time_taken, cur_time)
        x,y = cur_index

        xdelta = [0,1, 0,-1]
        ydelta = [1,0,-1, 0]
        for xd, yd in zip(xdelta, ydelta):
            x2, y2 = x+xd, y+yd
            if x2<nr and y2<nc and x2>=0 and y2>=0:
                if arr[x2][y2] == 1:
                    q.append( ((x2,y2), cur_time+1) )
                    arr[x2][y2] = 2

    # check if -1 case
    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == 1:
                return -1

    return max_time_taken

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
minTimeToRot(grid, len(grid), len(grid[0]))