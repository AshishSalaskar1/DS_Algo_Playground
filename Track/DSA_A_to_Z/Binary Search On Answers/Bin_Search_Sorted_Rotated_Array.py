"""
BINARY SEARCH IN SORTED+ROTATED ARRAY WITHOUT DUPLICATES
[4,5,6,7,0,1,2]

SOLUTION:
- In sorted+rotated array if you take any mid, its sure that either LEFT or RIGHT parts are sorted
- Take any index, you will see either LEFT or RIGHT side are sorted
- Iterate same way as BIN_SEARCH
 - if arr[mid] == target <- RESULT

 - if arr[lo]<=arr[mid] <- LEFT SIDE IS SORTED
    Now you need to search within this itself for BIN SEARCH
    1. if target in [lo,mid] -> search in this left part
    2. if targer not in [lo,mid] -> search in right part

 - if arr[mid]<=arr[hi] <- RIGHT SIDE IS SORTED
    Now you need to search within this itself for BIN SEARCH
    1. if target in [mid,hi] -> search in this RIGHT part
    2. if targer not in [mid,hi] -> search in LEFT part (not present in right)


WITH DUPLICATES
- It fails in only 1 case 
=> [1,0,1,1,1]
arr[lo] == arr[mid] == arr[hi]
- In this case just ignore lo and hi => lo++ and h--
- You already check if arr[mid] == target, so ur lo and hi and can never contain result

"""

class SolutionWithDuplicates:
    def search(self, arr: List[int], target: int) -> bool:
        lo,hi = 0, len(arr)-1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if arr[mid] == target:
                return True
            elif arr[lo] == arr[mid] == arr[hi]:
                lo += 1
                hi -= 1
            elif arr[lo]<=arr[mid]: # LEFT PART SORTED -> you can only bin search in this
                if arr[lo] <= target <= arr[mid]: # bin search on left sorted array (present within this)
                    hi = mid-1
                else:
                    lo = mid+1 # left is sorted, but your key cant be present here -> Search in right side
            else: # RIGHT PART SORTED arr[mid]<=arr[hi]
                if arr[mid] <= target <= arr[hi]:
                    lo = mid+1 # present in right -> BIN SEARCH ON RIGHT
                else:
                    hi = mid-1 # RIGHT SORTED, but not in right range 

        return False
        


class SolutionWithoutDuplicates:
    def search(self, arr: List[int], target: int) -> int:
        lo,hi = 0, len(arr)-1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if arr[mid] == target:
                return mid
            elif arr[lo]<=arr[mid]: # LEFT PART SORTED -> you can only bin search in this
                if arr[lo] <= target <= arr[mid]: # bin search on left sorted array (present within this)
                    hi = mid-1
                else:
                    lo = mid+1 # left is sorted, but your key cant be present here -> Search in right side
            else: # RIGHT PART SORTED arr[mid]<=arr[hi]
                if arr[mid] <= target <= arr[hi]:
                    lo = mid+1 # present in right -> BIN SEARCH ON RIGHT
                else:
                    hi = mid-1 # RIGHT SORTED, but not in right range 

        return -1

        