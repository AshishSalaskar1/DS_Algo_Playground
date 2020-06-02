/**
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
*/


class Solution {
    public int findMin(int[] a) {
        int n = a.length;
        
        if(n==1) return a[0];
        
        int start = 0, end = n-1,mid;
        int prev,next;
        
        while(start <= end){
            mid = start + (end - start) / 2;
            prev = (mid +n -1) % n;
            next = (mid +1) % n;
            
            int ele = a[mid];
            
            if(ele < a[prev] && ele < a[next])
                return ele;
            else if(ele >= a[0])
                start = mid +1 ;
            else
                end = mid - 1;
        }
        
        //no pivot found means array is already sorted
        return a[0];
    }
}
