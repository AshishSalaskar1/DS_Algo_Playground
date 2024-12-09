"""
LOWER BOUND = number on the immediate left of the given Target (ot it can be target itself)
Upper BOUND = number on the immediate right of the given Target (ot it can be target itself)

"""

def upper_bound(arr: list, target: int) -> int:
    def convert(mid: int) -> int:
        return 1 if arr[mid]>=target else 0

    n = len(arr)
    lo,hi = 0,n-1
    res = -1

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if convert(mid) == 1: # move left
            res = mid
            hi = mid-1
        else:
            lo = mid+1

    return arr[res]

def lower_bound(arr: list, target: int) -> int:
    def convert(mid: int) -> int:
        return 1 if arr[mid]<=target else 0

    n = len(arr)
    lo,hi = 0,n-1
    res = -1

    while lo<=hi:
        mid = lo + (hi-lo)//2
        if convert(mid) == 1: # move right
            res = mid
            lo = mid+1
        else:
            hi = mid-1

    return arr[res]



arr = [1,2,4,5,10,14,15,18,20]
target = 10
print(upper_bound(arr, target))
print(lower_bound(arr, target))

target = 6 # UPPER: 10, LOWER: 5
print(upper_bound(arr, target))
print(lower_bound(arr, target))
