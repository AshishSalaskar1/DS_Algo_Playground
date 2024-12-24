"""
Description
You have been given a grid of size N x N. Each cell is either empty (.) or occupied (#). Size of each cell is 1 x 1. In the connected component, you can reach any cell from every other cell in the component by repeatedly stepping to adjacent cells in the north, south, east, and west directions. 
Your task is to find the area and perimeter of the connected component having the largest area. The area of a connected component is just the number of '#' characters that are part of it. If multiple connected components tie for the largest area, find the smallest perimeter among them.

Input Format
The first line of input contains N, and the next N lines describe the grid. At least one '#' character will be present.

Output Format
Please output one line containing two space-separated integers, the first being the area of the largest connected component, and the second being its perimeter. If multiple connected components tie for the largest area, print the one which has the smallest perimeter among them.
"""
def visit(i, j, r, grid, region, area):
    to_visit = [(i, j)]
    while to_visit:
        i, j = to_visit.pop()
        if region[i][j] != 0 or grid[i][j] == '.':
            continue
        region[i][j] = r
        area[r] += 1
        to_visit.append((i - 1, j))
        to_visit.append((i + 1, j))
        to_visit.append((i, j - 1))
        to_visit.append((i, j + 1))


def find_perimeters(N, region, grid):
    perimeter = [0] * (N * N)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            r = region[i][j]
            if r == 0:
                continue
            if region[i - 1][j] == 0:
                perimeter[r] += 1
            if region[i + 1][j] == 0:
                perimeter[r] += 1
            if region[i][j - 1] == 0:
                perimeter[r] += 1
            if region[i][j + 1] == 0:
                perimeter[r] += 1
    return perimeter


def main():
    N = int(input())  # Read N (size of grid)
    grid = [['.'] * (N + 2) for _ in range(N + 2)]  # Pad grid with '.'
    region = [[0] * (N + 2) for _ in range(N + 2)]  # Pad region map with 0's
    area = [0] * (N * N)  # Store area of each region
    perimeter = [0] * (N * N)  # Store perimeter of each region

    # Reading the grid
    for i in range(1, N + 1):
        s = input().strip()
        for j in range(1, N + 1):
            grid[i][j] = s[j - 1]

    R = 0  # Region counter
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if grid[i][j] == '#' and region[i][j] == 0:
                R += 1
                visit(i, j, R, grid, region, area)

    perimeter = find_perimeters(N, region, grid)

    # Find the region with the largest area, and if there are ties, with the smallest perimeter
    best_a, best_p = 0, float('inf')
    for i in range(1, R + 1):
        if area[i] > best_a or (area[i] == best_a and perimeter[i] < best_p):
            best_a = area[i]
            best_p = perimeter[i]

    print(best_a, best_p)


if __name__ == "__main__":
    main()
