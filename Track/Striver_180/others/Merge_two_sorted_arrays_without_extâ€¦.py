"""
1. Do without extra space and m+n = total
## Without extra space
-Intution:
  - We know that `arr1` must contain all the smaller ele and `arr2` must have larger ele
  1. Whats the ele in `arr1` having max chance of going in `arr2`? Last ele -> since its largest in `arr1`
  2. Whats the ele in `arr2` having max chance of going in `arr1`? first ele -> since its smallest in `arr2`
- Solution:
  1. pointer1: arr1[last] : start<--end
  2. pointer2: arr2[0] : start-->end
  3. sort and return both arr1 and arr2
"""

def merge_inplace(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    
    p1, p2 = n1-1, 0
    
    while p1>=0 and p2<n2:
        if arr1[p1] >= arr2[p2]: # higher ele must go in arr2
            arr1[p1], arr2[p2] = arr2[p2],arr1[p1]
            
        p1 -= 1
        p2 += 1
        
        print(arr1, arr2, sep="\n")
        # else: # smaller ele goes in arr1 | already in place
        
    
    print(arr1, arr2, sep="\n")
    


arr1= [1,4,8,10] 
arr2 = [2,3,9]
# print(merge_inplace(arr1, arr2))

# expected
# arr1[] = [1 2 3 4]
# arr2[] = [8 9 10]

arr1= [1,3,5,7] 
arr2 = [0,2,6,8,9]
print(merge_inplace(arr1, arr2))
# expected
# arr1[] = [0 1 2 3]
# arr2[] = [5 6 7 8 9]

2. Same but -> arr1 has enough space to hold M+N (extra spaced in m1 are left as 0s)
- BRUTE FORCE
  - remove all 0s padded in arr1. Merge arr1, arr2 in res[] and return res, arr2

- OPTIMAL: No extra space
## Without extra space
Solution: https://leetcode.com/problems/merge-sorted-array/solutions/3436053/beats-100-best-c-java-python-and-javascript-solution-two-pointer-stl/
def merge_inplace(arr1, arr2, n1, n2):
  n_last = len(arr1)-1 # includes 0s
  i,j = n1-1, n2-1 
  
  while j>=0:
    # arr1 can deplete first but arr2 cant deplete first
    # even in first n1 times we pick from arr1, still n_last has n2 places left
    if i>=0 and arr1[i]>=arr2[j]:
      arr1[n_last] = arr1[i] # dont worry about swapping -> n_last we directly replace
      i -= 1
    else:
      arr1[n_last] = arr2[j]
      j -= 1
    n_last -= 1

  return arr1