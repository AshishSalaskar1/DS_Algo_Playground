
"""
== Link
https://www.codingninjas.com/codestudio/problems/intersection-of-2-arrays_1082149

arr1 = [1, 2, 2, 2, 3, 4]
arr2 = [2, 2, 3, 3]
res  = [2, 2, 3]
"""

def intersetion_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []

    i,j = 0,0
    while i<n1 and j<n2:
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        # ele in arr1 in smaller and you want bigger one to make both equal
        elif arr1[i]<arr2[j]: 
            i += 1
        # ele in arr2 is smaller and you want arr2 ele bigger so that they become equal
        else:
            j += 1
    
    return res



arr1 = [1, 2, 2, 2, 3, 4]
arr2 = [2, 2, 3, 3]
print(intersetion_arrays(arr1, arr2))
 