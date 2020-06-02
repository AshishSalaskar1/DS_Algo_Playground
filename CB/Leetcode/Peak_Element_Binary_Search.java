/**
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Follow up: Your solution should be in logarithmic complexity.

*/

class Solution {
    public int findPeakElement(int[] a) {
        int n = a.length;
        if(n==1) return 0;
        if(n==2) return (a[0] > a[1]) ? 0 : 1;
        
        int start = 0,end = n-1,mid;
        
        while(start <= end){
            System.out.println(start+":"+end);
            mid = start + (end - start) / 2;
            
            
            //not first and last
            if(mid > 0 && mid < n-1){
                if(a[mid] > a[mid+1] && a[mid] > a[mid-1])
                    return mid;
                else if(a[mid-1] > a[mid])
                    end = mid-1;
                else
                    start = mid+1;
            }
            
            //if mid is last | first then it has traversed the whole array
            else{
                if(mid == 0)
                    return (a[0] > a[1]) ? 0 : 1;
                
                else if(mid == n-1)
                    return (a[n-1] > a[n-2]) ? n-1 : n-2;
            }
        }
        
        return -1;
    }
}
