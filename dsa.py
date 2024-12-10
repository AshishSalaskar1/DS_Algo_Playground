def solve(arr:list[int]) -> int:
    n = len(arr)
    lo,hi = 0,n-1
    res = float("inf")

    while lo<=hi:
        mid = lo + (hi-lo)//2
        res = min(res, arr[mid])
        if arr[lo] <= arr