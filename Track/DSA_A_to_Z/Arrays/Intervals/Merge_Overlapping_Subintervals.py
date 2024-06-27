def mergeIntervals(arr):
    res = []
    n = len(arr)
    arr = sorted(arr)
    
    # always add first interval
    res.append(arr[0])
    
    for x in arr[1:]:
        cur_start, cur_end = x[0], x[1]
        prev_start, prev_end = res[-1][0], res[-1][1]
        
        if cur_start <= prev_end: # cur interval can be extended
            res[-1][1] = cur_end
        else: # cur interval cant be extended
            res.append(x)
    return res
    


intervals=[[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

mergeIntervals(intervals)