"""
 Classical Solution
- At each step check if csum+x is greater or x is greater
"""

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
    
    
arr = [1 ,2 ,7 ,-4 ,3 ,2 ,-10 ,9,1] # res = 11
print(maxSubarraySum(arr, len(arr)))