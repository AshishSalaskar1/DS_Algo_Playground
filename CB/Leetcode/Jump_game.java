// Problem Link : https://leetcode.com/problems/jump-game

class Solution {
    public boolean canJump(int[] a) {
        int maxReach = a[0];
        
        if(a.length <= 1)
            return true;
        
        for(int i=0;i<a.length;i++){
            //present jump is 0 and you cant reach next index via previous max jumps
            if(maxReach <= i && a[i] == 0)
                return false;
            
            //update max
            maxReach = Math.max(maxReach,i+a[i]);
            
            //you can reach end
            if(maxReach >= a.length-1)
                return true;
        }
        
        return false;
    }
}
