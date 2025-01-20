"""
Description
Given a 2d-array of dimension N*M and Q queries. In each query four integers x1, y1, x2, y2 is given, you have to find the sum of submatrix with (x1,y1) be the leftmost corner and (x2,y2) be the rightmost corner %10^9+7.

Input Format
The first line contains three space-separated integers N, M, Q where 1<=N, M<=10^3, 1<=Q<=10^6.

Next N lines contains M space-separated integers (-1e9<=Aij<=1e9).
- Next Q lines contains four space separated integers x1, y1, x2, y2 where 1<=x1<=x2<=N, 1<=y1<=y2<=M.

SOLUTION: 2D Prefix sum
# IMP: THE QUERIES ARE ALL 1-BASED

"""
import sys
from collections import deque, defaultdict
from queue import PriorityQueue
from functools import lru_cache 

MOD = (10**9)+7

# IMP: THE QUERIES ARE ALL 1-BASED
def prefix_sum(arr, nr, nc):
    """
    Returns the calculated 2D sum array
    """
    prefix =[[0 for _ in range(nc+1)] for _ in range(nr+1)]
    # calculate prefix sum
    for i in range(1,nr+1):
        for j in range(1,nc+1):
            prefix[i][j] = (arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1])%MOD
    
    return prefix

def rect_sum(prefix_arr, l, r, u, d):
    return (prefix_arr[d][r] - prefix_arr[u-1][r] - prefix_arr[d][l-1] + prefix_arr[u-1][l-1])%MOD


def main():
    nr, nc, q = list(map(int,sys.stdin.readline().split()))
    arr = []
    for _ in range(nr):
        arr.append(list(map(int,sys.stdin.readline().split())))
    
    prefix_arr = prefix_sum(arr, nr, nc)
    
    for _ in range(q):
        x1,y1,x2,y2 = list(map(int,sys.stdin.readline().split()))
        l, r, u, d = y1, y2, x1, x2
        print(rect_sum(prefix_arr, l, r, u, d))

        

        
main()