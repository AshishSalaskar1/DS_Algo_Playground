
"""
== Link
https://takeuforward.org/data-structure/union-of-two-sorted-arrays/

== Explain
 - Start traversing from the first occurrence index of Zero 
 - Take 2 variables (i,j), i will be at the first occurrence of zero and j is at i+1 
 - If element at j index is not zero then swap elements at i,j and increment i,j
 - If the element at j index is zero then only increment j.
"""

def move_zeros(arr, n):
    """
    TC: O(n^2)
    SC: O(1)
    """
    for i in range(n):
        # if 0 is found, replace it with next non zero element
        if arr[i] == 0: 
            for j in range(i+1,n):
                if arr[j]!=0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
        print(arr)


def move_zeros_v2(arr, n):
    """
    TC: O(n)
    SC: O(1)
    """
    zero_ptr = -1
    # find location of first zero
    for i in range(n):
        if arr[i]==0:
            zero_ptr = i
            break

    if zero_ptr == -1: #no zeros found
        return arr
    
    cur_ptr = zero_ptr+1
    while cur_ptr<n and zero_ptr<n:
        if arr[cur_ptr] != 0:
            arr[cur_ptr], arr[zero_ptr] = arr[zero_ptr], arr[cur_ptr]
            zero_ptr += 1
        
        # in case cur is also zero -> just cur_ptr++
        cur_ptr += 1

    return arr


arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
move_zeros(arr,len(arr))

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
move_zeros_v2(arr,len(arr))
 