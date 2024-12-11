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


class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        target = 0
        arr = sorted(arr)
        res = []
        
        #  [-1,0,1,2,-1,-4] -> [-4, -1, -1, 0, 1, 2]
        
        for i in range(n-2):
            if i!=0 and arr[i]==arr[i-1]: # if same ele was seen before ignore (why i-1? sorted array)
                continue
            val = arr[i]
            
            lo =  i+1
            hi = n-1
            while lo<hi:
                c_sum = val + arr[lo] + arr[hi]
                if c_sum == target:
                    res.append((val, arr[lo], arr[hi]))
                    
                    # [0,1,lo=2,2,2,3,4,5,6,hi=6,7] let say you got needed ans=6, then next you need lo=3, hi=5
                    while lo<hi and arr[lo]==arr[lo+1]: # increment until lo is not same as ans
                        lo += 1
                    while lo<hi and arr[hi]==arr[hi-1]: # increment until hi is not same as ans
                        hi -= 1
                    
                    lo += 1
                    hi -=1
                elif c_sum > target:
                    hi -= 1
                else:
                    lo += 1
        return res