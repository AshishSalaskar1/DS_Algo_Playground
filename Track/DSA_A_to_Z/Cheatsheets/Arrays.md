# Arrays Cheatsheet (verbatim snippets from repo)

Kadane’s Algorithm (from Arrays/Kadane's_Algorithm.py)
```python
## Code - Subarray Sum
def maxSubarraySum(arr, n):
    csum = arr[0]
    max_sum = arr[0]
    for x in arr[1:]:
        csum = max(csum+x,x)
        max_sum = max(csum, max_sum)
    
    return 0 if max_sum<0 else max_sum

## Code - Print Subarray Sum
def printMaxSubarraySum(arr, n):
    """
    Return the max_subarray sum along with the range of those elements
    Here you have to pick some ele, empty subarray is not a solution
    """
    start, end = 0, 0
    max_start, max_end = 0, 0
    csum = arr[0]
    max_sum = arr[0]
    for i, x in enumerate(arr[1:]):
        # check whats your curr start, end
        if csum+x > x: # you include cur ele
            end += 1
        else: # dont include cur ele
            start, end = i,i
        csum = max(csum+x,x)
        
        if csum > max_sum: # cur start,end is better for max
            max_start, max_end = start, end
        max_sum = max(csum, max_sum)
    
    print(sum(arr[max_start:max_end+1]))
    return max_sum, max_start, max_end
```

Next Permutation (from Arrays/Next_Permutation.py)
```python
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
```

Sort 0/1/2 (DNF) (from Arrays/Sort_an_array_of_0's,_1's_and_2's.py)
```python
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
```

Stock Buy and Sell (from Arrays/Stock_Buy_and_Sell.py)
```python
## You can buy and sell any number of time
## Sell at each profit peak that you can get

def maximumProfit(arr):
    res = 0
    n = len(arr)
    
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            res += (arr[i+1]-arr[i])
    
    return res

## You can only buy and sell once
- The max profit you can earn by selling at index `x` : `arr[x]` - `min_cost_before_i`

def maximumProfit(arr):
    res = 0
    min_till_now = float('inf')

    for x in arr:
        # max profit by selling at this day
        res = max(res, x-min_till_now)

        # check if min changes
        min_till_now = min(min_till_now, x)
    
    return res
```

See more in Arrays folder: Majority Element (Boyer–Moore variants), Merge two sorted arrays (variants), Pascal’s Triangle, Leaders, etc.

---

## 🗺️ Quick map
- 📈 Kadane (max subarray)
- 🔀 Next Permutation
- 🎯 DNF sort (0/1/2)
- 💹 Stock buy/sell variants

## ✅ Study checklist
- [ ] Kadane variant for all-negative arrays?
- [ ] Next permutation: find pivot, swap, reverse suffix?
- [ ] DNF: low/mid/high transitions straight?
- [ ] Stock variant: single vs multiple transactions clarified?
