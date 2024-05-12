class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        res = set()
        for i in range(0, len(arr)-2):
            lo, hi = i+1, len(arr)-1
            ele = arr[i]

            while lo < hi:
                cur = arr[hi] + arr[lo] + arr[i]
                if cur == 0:
                    res.add((arr[i],arr[lo], arr[hi]))
                    lo+=1
                    hi-=1
                elif cur > 0:
                    hi -=1 
                else:
                    lo += 1
        return res