"""
LOWER BOUND = first element in array >= x -> num elements < x
Upper BOUND = first element in array > x -> num elements <=x

"""

def upper_bound(arr: list, target: int) -> int:
    def convert(mid: int) -> int:
        return 1 if arr[mid]>target else 0

    n = len(arr)
    lo,hi = 0,n-1
    res = n

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if convert(mid) == 1: # move left
            res = mid
            hi = mid-1
        else:
            lo = mid+1

    return res

def lower_bound(arr: list, target: int) -> int:
    def convert(mid: int) -> int:
        return 1 if arr[mid]>=target else 0

    n = len(arr)
    lo,hi = 0,n-1
    res = n

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if convert(mid) == 1: # move left
            res = mid
            hi = mid-1
        else:
            lo = mid+1
    return res



arr = [1,2,4,5,10,14,15,18,20]
target = 10
print(upper_bound(arr, target), arr[upper_bound(arr, target)])
print(lower_bound(arr, target), arr[lower_bound(arr, target)])
print()

target = 6 # UPPER: 10, LOWER: 5
print(upper_bound(arr, target), arr[upper_bound(arr, target)])
print(lower_bound(arr, target), arr[lower_bound(arr, target)])