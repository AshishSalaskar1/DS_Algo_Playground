// Link : https://leetcode.com/problems/house-robber/

class Solution {
    

    
    public int rob(int[] a) {

        int n = a.length;
        
        
        int[] DP = new int[n+1];
        
        if(n==0) return 0;
        if(n==1) return a[0];
        if(n==2) return Math.max(a[0],a[1]);
        
        DP[0] = a[0];
        DP[1] = Math.max(a[0],a[1]);
        
        for(int i=2;i<n;i++)
            DP[i] = Math.max(a[i]+DP[i-2],DP[i-1]);
        
        return DP[n-1];
        
    }
}
