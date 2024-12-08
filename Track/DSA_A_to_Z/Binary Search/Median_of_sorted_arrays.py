class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1+n2

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        # size of left half of combined + Sorted array
        left_size = (n1+n2+1)//2 # handle odd values (Ceil) 

        # mid1: how many first `n` elements will be pick from nums1 
        # mid2: how many first `n` elements will be pick from nums2
        # mid1+mid2 = left (you want to take these and make left part of SORTED+COMBINED array)
        lo, hi = 0, n1

        while lo<=hi:
            mid1 = lo + (hi-lo)//2 # first `n` elements taken from first list 
            mid2 = left_size - mid1 # you need mid1+mid2=left_size

            # set the left and right pointers
            l1 = nums1[mid1-1] if mid1-1>=0 else float("-inf")
            l2 = nums2[mid2-1] if mid2-1>=0 else float("-inf")
            r1 = nums1[mid1] if mid1 < n1 else float("inf")
            r2 = nums2[mid2] if mid2 < n2 else float("inf") 

            # you could succesful partition the arrays into equal parts => RETURN
            if l1<=r2 and l2<=r1: # this selection is correct
                if n % 2 == 1: # odd number in left -> median:max of this sorted part
                    return max(l1, l2)
                else: # (max of left part + min of right part)/2 
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
            elif l1 > r2:
                hi = mid1-1
            else:
                lo = mid1+1
        
        return 0