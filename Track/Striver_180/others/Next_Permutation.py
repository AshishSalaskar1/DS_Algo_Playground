"""
## Intuition
There are 3 major observations we can make between a number and its next consecutive permutation
1. There are chances that both have most of starting numbers same - Longest prefix is expected
   - As solution to this, we iterate L<-R and try to find misplaced element such that arr[i]<arr[i-1]
   - Imagine this as ladder which keeps on increasing from L<-R and this element breaks that ladder
   - We know that till arr[i-1] we keep same prefix and then have to replace arr[i] with something on the left
- Why look for ele which is smaller than its next? if arr[i] < arr[i-1] then you can replace arr[i] and there is gauranteed to  be an element greater than arr[i]
  2 1 |5| 4 0 0 -> you cant replace 5 with any num on left and make it bigger 
2 |1| 5 4 0 0  -> since 5>1, its gauranteed that you can make bigger num (not always 5 is picked, you can pick a num >1 but <5 )
  - WHAT IF THERE IS NO BREAKING POINT? The curr arr is the largest permutation and next would be smallest or first permutation. So just reverse the array or sort in asc
2. We want to replace arr[i] such that its only little greater than the current number. So replace it with lowest ele greater than arr[i] in the right side of the array. (Why smallest + greater?  we wnt next consecutive perm not largest)
3. Now array till arr[i] is already greater than arr. Now remaining element on the right side needs to be smallest as possible (Because the arr[:i] is already greater than arr). So reverse the right side arr (or sort acc in ascending order)

"""

## Code
def nextPermutation(arr, n):
    # find breaking point
    break_point = -1
    for i in reversed(range(n-1)):
        if arr[i] < arr[i+1]:
            break_point = i
            break
    
    if break_point == -1:
        return sorted(arr)

    # replace breaking point with smallest greater
    # check from L<-R as from right its an increasing order
    for j in reversed(range(i+1,n)):
        if arr[j] > arr[break_point]:
            arr[j], arr[break_point] = arr[break_point], arr[j]
            break

    # reverse right part after breaking point
    arr = arr[:break_point+1] + sorted(arr[break_point+1:])

    return arr
    
    
arr = [2 ,3 ,1 ,4,5]
arr = [4,3,2,1]
arr = [5 ,6,4,2,1,3]
res = nextPermutation(arr, len(arr))
print(res)