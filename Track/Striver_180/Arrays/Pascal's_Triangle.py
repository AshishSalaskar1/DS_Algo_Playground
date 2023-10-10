"""
## Extreme Brute Force
- Each row = sum of index, index-1 from last row
- Start and ends are 1
- num of elements/columns in each row = row_number (1- based indexing)

## Find element in pascals triangle at position (row,col)
- ele at row,col = (row-1)C(col-1)


## Finding NCR faster
- nCr = n! / (n-r)!r! 
- 6C2 = 6! / (4!) 2! OR (6*5)/2!  [basically nr has numbers mulitiplied as many as r]
- TC: `O(r)` as we are doing at max `r` multiplications 
- Code tips: Dont calculate nr and dr separately instead do together. But in dr start multiplying from 1*2*.....r
"""


## Code for finding at loc row,col
def ncr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return int(res)
    
def get_pascals_ele(row, col):
    return ncr(row-1,col-1)
    
print(get_pascals_ele(3,2))