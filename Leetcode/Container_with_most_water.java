//Problem Link : https://leetcode.com/problems/container-with-most-water/submissions/

class Solution {
    public int maxArea(int[] height) {
        int res = Integer.MIN_VALUE;
        
        int i = 0;
        int j = height.length - 1;
        
        while(i<j){
            int left = height[i];
            int right = height[j];
            int curArea = (j-i) * Math.min(left,right);
            
            res = Math.max(res,curArea);
            
            if(left < right)
                i++;
            else 
                j--;
        }
        
        return res;
    }
}
