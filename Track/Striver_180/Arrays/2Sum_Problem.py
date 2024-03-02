def read(n: int, arr: [int], target: int) -> str:
    arr = sorted(arr)
    lo, hi = 0, n-1
    
    while lo < hi:
        psum = arr[lo] + arr[hi]
        
        if psum == target:
            return "YES"
        elif psum > target:
            hi -= 1 
        else:
            lo += 1
            
    return "NO"