// Problem Link: https://leetcode.com/problems/trapping-rain-water/


class Solution {
    public int trap(int[] a) {
        int n = a.length;
        
        if(n==0) return 0;
        
        int[] lMax = new int[n];
        int[] rMax = new int[n];
        
        lMax[0] = a[0];
        rMax[n-1] = a[n-1];
        for(int i=1;i<n;i++)
            lMax[i] = Math.max(a[i],lMax[i-1]);
        
        for(int i=n-2;i>=0;i--)
            rMax[i] = Math.max(a[i],rMax[i+1]);
        
        for(int x : lMax)
            System.out.print(x+" ");
        
        System.out.println();
    
        for(int x : rMax)
            System.out.print(x+" ");
         
        int res = 0;
        for(int i=0;i<n;i++){
            res += Math.min(lMax[i],rMax[i]) - a[i];
        }
        
        return res;
    }
}
