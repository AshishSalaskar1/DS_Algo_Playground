import sys
from collections import deque, defaultdict
from queue import PriorityQueue
from functools import lru_cache 

def lcs(s1, s2, s3):
    dp = {}
    n1, n2, n3 = len(s1), len(s2), len(s3)
    for i in range(n1+1):
        for j in range(n2+1):
            for k in range(n3+1):
                dp[(i,j,k)] = 0
    
    res = 0
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            for k in range(1,n3+1):
                if s1[i-1]==s2[j-1]==s3[k-1]:
                    dp[(i,j,k)] = 1+dp[(i-1,j-1,k-1)]
                else:
                    dp[(i,j,k)] = max(
                        dp[(i-1,j,k)],
                        dp[(i,j-1,k)],
                        dp[(i,j,k-1)],
                    )
    
    return dp[(n1,n2,n3)]

def main():
    for _ in range(int(sys.stdin.readline())):
        s1,s2,s3 = list(map(str,sys.stdin.readline().split()))
        print(lcs(s1,s2,s3))
        
main()