"""
PROBLEM: https://leetcode.com/problems/count-of-smaller-numbers-after-self

nums = [5,2,6,1]
res = [2,1,1,0]
- res[i] = how many elements are greater than nums[i] on the right side of it (nums[i+1]...nums[n-1])

INTUTION:
- Sort element and store their index in original array
- In segment tree - you represent all the original indexes of the array. 1 means there is one element placed here
- We place the element from lo->hi in value n their indexes such that, 
    number_elements > cur_element and on right side = QUERY(IDX->N)
- Lets say you are at (val,idx). Since we process smaller to larger, you would have placed 1 on the index of elements smaller than val

DRY RUN INTUITION
- Sort elements and maintain there indexes
arr = [(5, 0), (2, 1), (6, 2), (1, 3)]
sorted = [(1, 3), (2, 1), (5, 0), (6, 2)]

- Now, here you see that smallest element is first - along with its idx in original array
- Initially assume you didnt pick any element, st_arr = [0,0,0,0]
1. (1, 3)
    - res[3] = st.query(3,n) = 0 (res= [0,0,0,0])
    - st.update(3,1) 
    - st_arr = [0,0,0,1]
2. (2, 1)
    - res[1] = st.query(1,n) = 1 (res= [0,1,0,0])
    - st.update(1,1) 
    - st_arr = [0,1,0,1]
3. (5, 0)
    - res[0] = st.query(0,n) = 2 (res= [2,1,0,0])
    - st.update(0,1) 
    - st_arr = [1,1,0,1]
4. (6, 2)
    - res[2] = st.query(2,n) = 1 (res= [2,1,1,0])
    - st.update(2,1) 
    - st_arr = [1,1,1,1]

res= [2,1,1,0]

Why, list of (val,idx) and not {val: i}?
- The numbers in arr can be duplicates also
"""


class ST:
    def __init__(self,n):
        self.st = [0]*(4*n+1)
        self.n = n
    
    def update(self, i, l, r, loc, val):
        if loc<l or loc>r:  return 
        if l==r:
            self.st[i] += val
            return
        
        mid = (l+r)//2
        self.update(2*i,l,mid,loc,val)
        self.update(2*i+1,mid+1,r,loc,val)
        self.st[i] = self.st[2*i] + self.st[2*i+1]
    
    def query(self, i, l, r, ql, qr):
        if l>qr or r<ql:    return 0
        if ql<=l<=r<=qr:    return self.st[i]

        mid = (l+r)//2
        return self.query(2*i,l,mid,ql, qr)+self.query(2*i+1,mid+1,r,ql, qr)
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_map = [(val,i) for i,val in enumerate(nums)]
        n = len(sorted_map) + 2

        queries = sorted(sorted_map)

        st = ST(n)
        res = [0]*len(nums)
        for val, org_arr_idx in queries:
            res[org_arr_idx] = st.query(1,0,n-1,org_arr_idx,len(nums))
            st.update(1,0,n-1,org_arr_idx,1)
        
        return res
