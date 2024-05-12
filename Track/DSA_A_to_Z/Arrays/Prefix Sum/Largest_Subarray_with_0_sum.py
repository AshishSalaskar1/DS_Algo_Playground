def longest_sb_zero_sum(arr):
  n = len(arr)
  csum = 0
  max_len = 0
  hmap = {}

  for i,x in enumerate(arr):
    csum += x
    
    if csum == 0:
      max_len = max(max_len, i+1)
    elif csum in hmap:
      max_len = max(max_len, i-hmap[csum])
    else:
      hmap[csum] = i
  
  return max_len