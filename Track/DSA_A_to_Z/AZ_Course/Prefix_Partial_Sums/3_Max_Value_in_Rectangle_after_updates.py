"""
Description
Given a 2d-array of dimension N*M and Q queries. In each query five integers x1, y1, x2, y2, C is given, you have to increase the value of each cell in the submatrix with (x1,y1) be the leftmost corner and (x2,y2) be the rightmost corner by C. Initially the value of all the cell of the 2d-array is 0.

After all the query is performed, print the maximum value present in the 2d-array and the number of the cell with the maximum value.

Input Format
The first line contains three space-separated integers N, M, Q where 1<=N, M<=10^3, 1<=Q<=10^6.

The next Q lines contains five space separated integers x1, y1, x2, y2, C where 1<=x1<=x2<=N, 1<=y1<=y2<=M, -10^9<=C<=10^9.

Output Format
After all the query is performed, print 2 space-separated integers representing the maximum value present in the 2d-array and the number of the cell with the maximum value.

SOLUTION:

"""
import sys
from collections import deque, defaultdict
from queue import PriorityQueue
from functools import lru_cache 

def generate_prefix_sum(arr, nr, nc):
    prefix =  [[0 for _ in range(nc+1)] for _ in range(nr+1)]
    for i in range(1,nr+1):
        for j in range(1, nc+1):
            prefix[i][j] = arr[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]
    
    return prefix

def update_val(arr, l, r, u, d, val):
    arr[u][l] += val
    if r+1 <= len(arr[0]) - 1: # HANDLE BOUNDARY CASES (since you are going ahead and back) = ANOTHER SOL: arr[nr+2][nc+2]
        arr[u][r+1] -= val
    if d+1 <= len(arr) - 1:
        arr[d+1][l] -= val
    if d+1 <= len(arr) - 1 and r+1 <= len(arr[0]) - 1:
        arr[d+1][r+1] += val
    return arr



def main():
    nr, nc, q = list(map(int,sys.stdin.readline().split()))
    arr = [[0 for _ in range(nc+1)] for _ in range(nr+1)]

    for _ in range(q):
        x1,y1,x2,y2, incr_val = list(map(int,sys.stdin.readline().split()))
        l,r,u,d = y1,y2,x1,x2 # 1-based indexing
        arr = update_val(arr, l,r,u,d,incr_val)
    
    # print(*arr, sep="\n")
    # print()
    arr = generate_prefix_sum(arr, nr, nc)
    # print(*arr, sep="\n")
    # NO NEED TO CALCULATE PREFIX SUM -> SINCE INIT WAS 0
    max_val, max_count = float('-inf'), 0
    for i in range(1,nr+1):
        for j in range(1,nc+1):
            x = arr[i][j]
            if x>max_val:
                max_val = x
                max_count = 1
            elif x == max_val:
                max_count += 1
    
    print(max_val, max_count)
        
        
main()