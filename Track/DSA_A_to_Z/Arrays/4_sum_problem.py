class Solution:
    def threeSum(self, arr: List[int], target) -> List[List[int]]:
        n = len(arr)
        res = set()
        
        for i in range(n-2):
            val = arr[i]
            
            lo =  i+1
            hi = n-1
            while lo<hi:
                c_sum = val + arr[lo] + arr[hi]
                if c_sum == target:
                    res.add((val, arr[lo], arr[hi]))
                    lo += 1
                    hi -=1
                elif c_sum > target:
                    hi -= 1
                else:
                    lo += 1
        return res
        
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = set()
        arr = sorted(arr)
        
        for i in range(len(arr)-3):
            x = arr[i]
            rem_target = target-x
            temp_res = self.threeSum(arr[i+1:], rem_target)
            
            for tup in temp_res:
                res.add((x,*tup))
        return res
        
            
        
    # [1 | 2,3,4,5] -> make results unique -> all elements must be unique?