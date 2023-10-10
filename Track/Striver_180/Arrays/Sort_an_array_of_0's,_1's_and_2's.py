## DNF Algorithm
def sort012(arr, n) :
    zero_ptr = 0
    two_ptr = n-1
    cur = 0

    while cur <= two_ptr:
        if arr[cur] == 0:
            arr[cur], arr[zero_ptr] = arr[zero_ptr], arr[cur]
            cur += 1
            zero_ptr += 1
        elif arr[cur] == 2:
            arr[cur], arr[two_ptr] = arr[two_ptr], arr[cur]
            two_ptr -= 1
        else:
            cur += 1
    
    return arr