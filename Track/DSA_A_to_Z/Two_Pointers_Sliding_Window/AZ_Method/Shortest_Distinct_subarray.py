"""
Description
Given an array of N integers, find the length of the smallest sub-array that contains all the distinct elements of the array.
"""

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  ndistinct = len(set(arr))

  res = n
  l,r = 0, -1
  hmap = {}

  while r<n:
    while r+1<n and len(hmap)<ndistinct:
      r += 1
      hmap[arr[r]] = hmap.get(arr[r],0)+1
    
   
    if len(hmap) == ndistinct:
      res = min(res, r-l+1)
    # print(l,r,hmap,res)

    if l>r:
      l += 1
      r = l-1
    else:
      hmap[arr[l]] -= 1
      if hmap[arr[l]] == 0:
        hmap.pop(arr[l])
      l += 1
  
  print(res)










