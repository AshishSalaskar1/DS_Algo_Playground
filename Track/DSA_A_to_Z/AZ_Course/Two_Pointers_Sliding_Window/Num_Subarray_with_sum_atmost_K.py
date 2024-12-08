"""
Description
Given an array of N integers, find the number of subarrays with a sum less than equal to K.
"""


def solve(arr, k):
  n = len(arr)
  l,r = 0, -1
  csum = 0
  res = 0

  while r<n:
    # move right as far as possible
    while r+1<n and (csum+arr[r+1] <= k):
      r += 1
      csum += arr[r]

    res += (r-l+1)
    
    if l>r:
      l += 1
      r = l-1
    else:
      csum -= arr[l]
      l += 1

  return res



arr, k = [1, 2, 3], 5 # 5
arr, k = [3, 2, 1], 6 # 6
arr, k = [2, 1, 0, 4, 5], 0 # 1
arr, k = [1, 2, 3, 0, 1, 5, 2], 6 # 18
arr, k = [1, 0, 1, 1, 10, 2, 3, 7, 5, 9], 10 # 18
