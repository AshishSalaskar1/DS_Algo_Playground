/**

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

*/

class Solution {
    
    static int binSearch(int[] a,int sum,int start,int end){
        
        int mid;
        
        while(start <= end){
            mid = start + (end - start) /2;
            
            if(a[mid] == sum) return mid;
            
            else if(a[mid] < sum)
                start = mid +1;
            else 
                end = mid -1 ;
        }
        
        return -1;
    }
    public int search(int[] a, int target) {
        int n = a.length;
        
        
        int start = 0,end = n-1,mid=0,prev,next;
        
        while(start <= end){
            mid = start + (end - start) /2;
            prev = (mid + n - 1) % n; // handle if mid = 0
            next = (mid +1 ) % n;
            
            
            int ele = a[mid];
            if(ele < a[prev] && ele < a[next])
                break;
            
            else if(ele >= a[0])
                start = mid +1 ;
            else 
                end = mid - 1;
        }
        
        int minIndex = mid;
        
        System.out.println(minIndex);
        
        return Math.max(binSearch(a,target,0,minIndex-1),
                        binSearch(a,target,minIndex,n-1));
    
            
    }
}
