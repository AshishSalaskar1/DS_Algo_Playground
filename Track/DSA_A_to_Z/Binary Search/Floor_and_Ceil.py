def bin_search_floor(arr, key):
    """
    - Return key if it exists
    - Else return largest element < key (NEAREST TO KEY FROM LEFT)
    """
    lo,hi = 0, len(arr)-1
    res = -1

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if arr[mid] <= key:
            res = arr[mid]
            lo = mid + 1
        else:
            hi = mid-1

    return res

def bin_search_ceil(arr, key):
    """
    - Return key if it exists
    - Else return smallest element > key (NEAREST TO KEY FROM RIGHT)
    """
    lo,hi = 0, len(arr)-1
    res = -1

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if arr[mid] >= key:
            res = arr[mid]
            hi = mid-1
        else:
            lo = mid+1

    return res


arr = [1,3,5,7,8,9,12,15,16,20]
print(bin_search_floor(arr, 17))
print(bin_search_ceil(arr, 17))
