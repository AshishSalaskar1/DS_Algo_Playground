
"""
== Link
KEEP DUPLICATES
https://takeuforward.org/data-structure/union-of-two-sorted-arrays/
https://www.codingninjas.com/codestudio/problems/intersection-of-2-arrays_1082149

DONT KEEP DUPLICATES
-> extra conditions
1. if arr1[i] == arr2[j] -> only insert one
2. for every insert into res also check is previously_inserted_ele == cur_to_be_inserted

"""

def ninjaAndSortedArrays(arr,arr2,m,n):
    """
    NOT OPTIMAL SOLUTION
    Optimal Sol: https://www.codingninjas.com/codestudio/problem-details/ninja-and-sorted-arrays_1214628
    """
    arr1 = [x for x in arr if x!=0]
    n1 = len(arr1)
    n2 = len(arr2)
    res = []

    i,j = 0,0

    while i<n1 and j<n2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1


    # one is used another remaining
    if i<n1:
        for x in range(i,n1):
            res.append(arr1[x])
    if j<n2:
         for x in range(j,n2):
            res.append(arr2[x])
    
    return res



arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
print(merge_sorted_arrays(arr1,arr2))
 


