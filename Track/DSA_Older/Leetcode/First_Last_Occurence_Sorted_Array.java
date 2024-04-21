/**

Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

*/
class Solution {
    public int[] searchRange(int[] a, int key) {
        int[] resArray = {-1,-2};
        
        int n = a.length;
        //find min
        int start = 0,end = n-1,mid;
        int firstOcc = -1,lastOcc = -1;
        
        //find first occurence
        while(start <= end){
            mid = start + (end - start) / 2;
            if(a[mid] == key){
                firstOcc = mid;
                end = mid-1;
            }
            
            else if(a[mid] < key)
                start = mid +1 ;
            else 
                end = mid-1;
        }

        
        start = 0;end = n-1;
        
        //find last occurence
        while(start <= end){
            mid = start + (end - start) / 2;
            if(a[mid] == key){
                lastOcc = mid;
                start = mid+1;
            }
            
            else if(a[mid] < key)
                start = mid +1 ;
            else 
                end = mid-1;
        }
        
        resArray[0] = firstOcc;
        resArray[1] = lastOcc;
        
        return resArray;
        
    }
}
