"""
- Calculate prefix and suffix products with one catch:
    - anywhere csum=0, make it 1 (so that it doesnt affect next products)
    - this will assume that you are starting new prefix-product from next element
    [-2, 0, -1] => [-2, 0, 0] (usual prefix product)
                => [-2, 0, -1] (using this approach)

- Iterate each point
    res = max(prefix[i], suffix[i], res) <- 0 case already handled
"""

class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        prefix, suffix = [0]*n,[0]*n

        csum = 1
        for i in range(n):
            csum = csum*arr[i]
            prefix[i] = csum
            if csum == 0:
                csum = 1
        csum = 1
        for i in reversed(range(n)):
            csum = csum*arr[i] 
            suffix[i] = csum

            if csum == 0:
                csum = 1

        res = float("-inf")
        print(prefix)
        print(suffix)
        for i in range(0,n):
            res = max([prefix[i],suffix[i],res])
        return res
        

"""
[2,3,-2,4]
"""