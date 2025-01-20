"""
You are given an array of N integers. Find the longest subarray with distinct characters.

"""

def solve(arr,n):
    res = 0
    l,r = 0, -1
    hset = set()

    while r<n:
        while r+1<n and arr[r+1] not in hset:
            r += 1
            hset.add(arr[r])
        
        res = max(res, len(hset))

        if l>r:
            l += 1
            r = l-1
        else:
            hset.remove(arr[l])
            l += 1
    return res


for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  print(solve(arr,n))










