class Solution {
    public int maxSubArray(int[] nums) {
        int maxSF = nums[0];
        int curMax = nums[0];
        
        int x;
        for(int i=1;i<nums.length;i++){
            x = nums[i];
            
            curMax = Math.max(x, curMax+x);
            
            maxSF = Math.max(maxSF,curMax);
        }
        
        return maxSF;
    }
}
