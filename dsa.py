def upper_bound(arr, key):
    n = len(arr)
    lo,hi = 0,n-1
    res = n

    while lo<=hi:
        mid = lo+(hi-lo)//2
        if arr[mid] > key:
            res = mid
            hi = mid-1
        else:
            lo = mid+1
    
    return res


def check(arr1, arr2, x, k):
    # print(f"Checking for k={k} and x={x}")
    less_or_equal_k_count = 0
    for val in arr1:
        # print(val, x-val,upper_bound(arr2, x-val) )
        less_or_equal_k_count += upper_bound(arr2, x-val)
    
    return less_or_equal_k_count >= k


def solve(a, b, k):
    """
    Return the `k` smallest number in `c` ( just index wise, not distinct)
    """
    if len(a) > len(b): # just that you perform bin_search on longer array repeatedly
        a,b = b,a

    a.sort()
    b.sort()
    lo, hi = a[0]+b[0], a[-1]+b[-1]
    res = hi

    while lo<=hi:
        mid = lo+(hi-lo)//2
        if check(a, b, mid, k):
            res = mid
            hi = mid-1
        else:
            lo = mid+1
    
    return res

a = [1,2,3]
b = [4,5,6]
# c = [5,6,6,7,7,7,8,8,9]
k = 6
print(solve(a,b,k))