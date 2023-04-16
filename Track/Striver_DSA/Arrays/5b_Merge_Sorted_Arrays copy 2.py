
"""
== Link
https://www.codingninjas.com/codestudio/problems/ninja-and-sorted-arrays_1214628

You are given 2 arrays out of which first one has enough size to contain merged array
Extra space is padded with 0 in arr1
arr1 = [1,2,3,0,0,0]
arr2 = [1,7,8,10]
==> arr1 = [1,1,3,7,8,10]
"""

def merge_sorted_arrays_into_arr1(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res_ptr = 0

    i,j = 0,0

    while i<n1 and j<n2 and res_ptr<n1:
        if arr1[i] < arr2[j]:
            arr1[res_ptr] = arr1[i]
            res_ptr += 1
            i += 1
        else:
            arr1[res_ptr] = arr2[j]
            res_ptr += 1
            j += 1

    print(arr1,i,j)
    # one is used another remaining
    if i<n1:
        for x in range(i,n1):
            arr1[res_ptr] = arr1[x]
    if j<n2:
         for x in range(j,n2):
            arr1[res_ptr] = arr2[x]
    
    return arr1



arr1 = [1,2,3,0,0,0]
arr2 = [7,8,10]
print(merge_sorted_arrays_into_arr1(arr1, arr2))
 