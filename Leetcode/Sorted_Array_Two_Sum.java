//Problem Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
    public int[] twoSum(int[] a, int sum) {
        int i = 0, j=a.length-1;
        
        int curSum = 0;
        
        while(i < j){
            
            curSum = a[i] + a[j];
 
            
            if(curSum == sum)
                return new int[]{++i,++j};
          
            if(curSum < sum)
                i++;
            else
                j--;
            
        }
        
        return new int[]{i+1,j+1};
    }
}
