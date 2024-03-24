"""
Link: https://www.codingninjas.com/studio/problems/replace-%E2%80%98o%E2%80%99-with-%E2%80%98x%E2%80%99_630517

Problem: In a matrix given X and O, and island of O -> surrounded all sides by X and not edges
Find such islands of O and replace them with X

SOLUTION 1
- Whenever u find O do BFS, and keep track of all nodes you are visiting (all these nodes will have O)
- During BFS if i,j go out-of-bounds => not island since u hit the edge of grid
- In case u hit bounds, still continue BFS and visit all nodes of that pseudo-island
- If you never hit bounds => is_island=True => Mark all nodes u visited as part of BFS with 'X'


SOLUTION 2 -> EASIER (no tracking of elements needed):
- You know that only boundary islands are not valid
- Iterate all 4 boundaries and do BFS wherever u find 0 -> all these visited nodes should are not actual islands
- Other than these visited islands mark all others O with X

IMPROVEMENT in SOLUTION 2:
- instead for NxM for loop and if to find boundaries -> only iterate 4 boundaries
- This will need 2 FOR Loops -> range(nr) and range(nc)
"""

class Solution1:

    def do_bfs(self, i, j):
        # print(i,j)
        q = [(i,j)]
        cur_stack = []
        self.vis.add((i,j))
        is_island = True

        while len(q) != 0:
            x1,y1 = q.pop(0)
            cur_stack.append((x1,y1))

            xdelta=[0,1,0,-1]
            ydelta=[1,0,-1,0]
            for xd, yd in zip(xdelta, ydelta):
                x2, y2 = x1+xd, y1+yd
                if x2<0 or y2<0 or x2>=self.nr or y2>=self.nc:
                    # if u know this is not island, still do BFS to visit all n keep them
                   is_island = False
                elif self.arr[x2][y2] == 'O' and (x2,y2) not in self.vis:
                    q.append((x2,y2))
                    self.vis.add((x2,y2))

        # only udpate with X if its a island
        if is_island:
            for i,j in cur_stack:
                self.arr[i][j] = "X"



    def replaceOWithX(self, arr, nr, nc):
        self.arr = arr
        self.nr = nr
        self.nc = nc
        self.vis = set()

        for i in range(nr):
            for j in range(nc):
                if self.arr[i][j] == 'O' and (i,j) not in self.vis:
                    self.do_bfs(i,j)

        return self.arr

def solution2(arr, nr, nc):
    vis = set()

    for i in range(nr):
        for j in range(nc):
            # boundary traversal only
            if i==0 or j==0 or i==nr-1 or j==nc-1:
                if arr[i][j] == 'O' and (i,j) not in vis:
                    # DO BFS
                    vis.add((i,j))
                    q = [(i,j)]
                    while len(q) != 0:
                        x1,y1 = q.pop(0)

                        xdelta=[0,1,0,-1]
                        ydelta=[1,0,-1,0]
                        for xd, yd in zip(xdelta, ydelta):
                            x2, y2 = x1+xd, y1+yd
                            if x2>=0 and y2>=0 and x2<nr and y2<nc and arr[x2][y2]=='O' and (x2,y2) not in vis:
                                q.append((x2,y2))
                                vis.add((x2,y2))

    # all nodes visited -> not island => REMAINING 0 islands are valid ones
    for i in range(nr):
        for j in range(nc):
            if (i,j) not in vis and arr[i][j] == 'O':
                arr[i][j] = 'X'
    return arr



arr = [
    ['X', 'X', 'O', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'O', 'X'],
    ['O', 'X', 'X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'O', 'X'],
    ['X', 'O', 'O', 'X', 'X', 'O']
]

sol = Solution1()
res1 = sol.replaceOWithX(arr, len(arr), len(arr[0]))
print(res1)

res2 = solution2(arr, len(arr), len(arr[0]))
print(res2)

print(res1 == res2)