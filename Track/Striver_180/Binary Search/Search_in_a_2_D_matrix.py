"""
1. Start from top-right cell (consider this as mid in binary search)
2. If mid > target ==> move left (you need smaller values)
3. If mid < targer ==> move down (you need bigger values)
"""

def matrix_search(arr, target):
    nr = len(arr)
    nc = len(arr[0])
    
    # start of at top right
    i,j = 0, nc-1
    while i>=0 and i<nr and j>=0 and j<nc:
        print(f"Checking {i}-{j}")
        val = arr[i][j]
        if val == target:
            return True
        elif val > target: # move left
            j -= 1
        else: # move bottom
            i += 1
    
    return False
            


arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix_search(arr, 10))