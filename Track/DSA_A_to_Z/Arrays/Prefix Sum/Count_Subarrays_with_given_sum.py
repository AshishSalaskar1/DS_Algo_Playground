def count_subarray_sum_target(arr, target):
    hmap = {0:1} # consider initial csum as 0
    count = 0
    csum = 0
    
    for x in arr:
        csum += x
        
        if csum-target in hmap:
            count += hmap[csum-target]
        
        # If you have already seen this cur_sum ,that means
        # there are 2 ways to form sum in case any result uses cur_sum
        hmap[csum] = hmap.get(csum,0)+1
        
        # in longest_subarray_target we dont include csum if already seen. Why?
        # because we need longest, n earliest seen csum, longer the answer subarray
        
    return count