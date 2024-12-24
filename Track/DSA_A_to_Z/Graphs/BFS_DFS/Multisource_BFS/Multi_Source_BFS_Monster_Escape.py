"""
- In a grid you are given `M` monsters and one person `P`. The monsters and person can both move in 4 directions but 1 step a time
- As a person, you find the shortest distance to escape from the grid (Escape = reaching any edge)

1. Once the person finalizes his escape path, all monsters are informed n then they try to block the person from escaping ( All monsters n the person can move one cell at a time)
2. Once you decide n path, you need to follow that. You cant dynamically change after seeing the path of any monsters
3. You need to find the shortest path to escape so that no monster can eat you


MULTI SOURCE BFS - LOGICS
- You ideally club a set of nodes into single huge node (practically done by putting all these nodes into the Queue at start)
- Now, you find shortest dist from ANY OF THESE NODES to some other node/cell in the matrix
- You can say that min_dist from this node to ANY_OF_THOSE_NODES is `dist`. BUT: You cant say which nodes was it exactly out of all those nodes


Example 1: Start -> Escape pairs
=> ANY_OF_THESE_NODES = Escape nodes
- Multi-source on this gives: shortest distance from any start node "S", to any escape node "E"
- Here you can use any escape and you dont have to tell which node you escape from ( this would need you to maintain some kind of a route map)
"""


import sys
from collections import deque

def solve(arr):
    nr, nc = len(arr), len(arr[0])
    monster_q = deque()
    person_q = deque()

    # Initialize distances
    dist_monster = [[-1] * nc for _ in range(nr)]
    dist_person = [[-1] * nc for _ in range(nr)]

    # Directions for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Populate queues and initialize distances
    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == 'M':
                monster_q.append((i, j))
                dist_monster[i][j] = 0
            elif arr[i][j] == 'A':
                # If the person is already on a boundary, they can escape immediately
                if i == 0 or j == 0 or i == nr - 1 or j == nc - 1:
                    return 0, (i, j)
                person_q.append((i, j))
                dist_person[i][j] = 0

    # Multi-source BFS for monsters
    while monster_q:
        r, c = monster_q.popleft()
        for dx, dy in directions:
            nextr, nextc = r + dx, c + dy
            if 0 <= nextr < nr and 0 <= nextc < nc and arr[nextr][nextc] != '#' and dist_monster[nextr][nextc] == -1:
                dist_monster[nextr][nextc] = dist_monster[r][c] + 1
                monster_q.append((nextr, nextc))

    # Single-source BFS for person
    while person_q:
        r, c = person_q.popleft()
        for dx, dy in directions:
            nextr, nextc = r + dx, c + dy
            if 0 <= nextr < nr and 0 <= nextc < nc and arr[nextr][nextc] != '#' and dist_person[nextr][nextc] == -1:
                dist_person[nextr][nextc] = dist_person[r][c] + 1
                person_q.append((nextr, nextc))

    # Check only the escape cells
    min_path = float('inf')
    escape_cell = (-1, -1)

    for i in range(nr):
        # Left boundary
        if dist_person[i][0] != -1 and (dist_monster[i][0] == -1 or dist_person[i][0] < dist_monster[i][0]):
            if dist_person[i][0] < min_path:
                min_path = dist_person[i][0]
                escape_cell = (i, 0)
        # Right boundary
        if dist_person[i][nc - 1] != -1 and (dist_monster[i][nc - 1] == -1 or dist_person[i][nc - 1] < dist_monster[i][nc - 1]):
            if dist_person[i][nc - 1] < min_path:
                min_path = dist_person[i][nc - 1]
                escape_cell = (i, nc - 1)

    for j in range(nc):
        # Top boundary -> check if Person is reachable here + (monster cant reach here OR it needs more time to reach here)
        if dist_person[0][j] != -1 and (dist_monster[0][j] == -1 or dist_person[0][j] < dist_monster[0][j]):
            if dist_person[0][j] < min_path:
                min_path = dist_person[0][j]
                escape_cell = (0, j)
        # Bottom boundary
        if dist_person[nr - 1][j] != -1 and (dist_monster[nr - 1][j] == -1 or dist_person[nr - 1][j] < dist_monster[nr - 1][j]):
            if dist_person[nr - 1][j] < min_path:
                min_path = dist_person[nr - 1][j]
                escape_cell = (nr - 1, j)

    if escape_cell == (-1, -1):
        return float('inf'), (-1, -1)
    return min_path, escape_cell


def main():
    nr, nc = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(nr)]
    min_path, escape_cell = solve(arr)
    if min_path == float('inf'):
        print("NO")
    else:
        print("YES")
        print(min_path)

main()


"""
5 8
########
#M..A..#
#.#.M#.#
#M#..#..
#.######
"""