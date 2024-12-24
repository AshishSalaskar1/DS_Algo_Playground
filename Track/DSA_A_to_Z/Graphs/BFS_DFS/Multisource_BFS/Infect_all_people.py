"""
Description
Your city is having people infected with a virus. The city in which you live is represented as a grid consisting of n rows and m columns. Cells containing 2 are the cells where the people infected with the virus are present and the cells having 1 are the cells having people not yet infected with the virus. There are certain empty cells which are represented by 0. The infected people in a unit time can infect all their adjacent cells, i.e, if they are present at cell [i, j] they can infect cells [i-1, j], [i+1, j], [i, j-1] and [i, j+1]. The virus cannot pass through empty cells. Your task is to print the minimum time in which all the people are infected with the virus. If the virus cannot infect everyone, print -1.

Input Format
The first line contains two integers n and m  — the number of rows and columns, respectively.
The following n lines contain m integers each, the j-th element in the i-th line is the number written in the j-th cell of the i-th row.

Output Format
Print the minimum time in which everyone can be infected or -1 if everyone cannot be infected.
"""
import sys
from collections import deque

def solve(arr, nr, nc):
    healthy_set = set()
    infect_q = deque()

    for i in range(nr):
        for j in range(nc):
            if arr[i][j] == 2:  # Infected cell
                infect_q.append((i, j, 0))
            elif arr[i][j] == 1:  # Healthy cell
                healthy_set.add((i, j))

    vis = set()
    # Multi-source BFS on infections
    while infect_q:
        r, c, dist = infect_q.popleft()

        # Mark as visited
        vis.add((r, c))

        # If this cell was healthy, remove it from the set
        if (r, c) in healthy_set:
            healthy_set.remove((r, c))

        # If all healthy cells are infected
        if not healthy_set:
            return dist

        # Spread infection to neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextr, nextc = r + dx, c + dy
            if (
                0 <= nextr < nr and 0 <= nextc < nc and
                arr[nextr][nextc] !=0 and  # Only spread to healthy cells
                (nextr, nextc) not in vis
            ):
                infect_q.append((nextr, nextc, dist + 1))
                vis.add((nextr, nextc))  # Mark as visited immediately

    # If there are still healthy cells left, return -1
    return -1


def main():
    nr, nc = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(nr)]
    print(solve(arr, nr, nc))

main()
