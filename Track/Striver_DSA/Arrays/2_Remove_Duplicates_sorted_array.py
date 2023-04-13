# == Question
# [1,1,2,2,2,3,3] -> output(k)=3 [[1,2,3,_,_,_,_]
# If there are k elements after removing the duplicates,then first k elements of the arr must be final result. 
# It does not matter what you leave beyond the first k elements.
# == Link
# https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-sorted-array_1102307
# == Articles:
# 
# == Explain
# 

def removeDuplicates(arr,n):
    if n==1:
        return 1

    unique_ptr = 0
    for i in range(1,n):
        # if x==unique_ptr (its a duplicate of last seen unique number)
        # just skip, we dont want to replace anything
        if arr[i] == arr[unique_ptr]:
            continue
        # we got a unique num, unique_ptr++ and replace 
        else:
            unique_ptr += 1
            arr[unique_ptr] = arr[i]

    return unique_ptr+1




arr = [1 ,2 ,2 ,3 ,3 ,3 ,4 ,4 ,5,5 ]
k = removeDuplicates(arr,10) # ANS=5
print(k, arr)