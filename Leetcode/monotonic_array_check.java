// Link :  https://leetcode.com/problems/monotonic-array

class Solution {
    public boolean isMonotonic(int[] a) {
        boolean incr = false;
        int n = a.length;
        
        if(n==1) return true;
        
        //incase a[0] nad a[1] are equal
        //[1,1,1,2,3,4]
        int x = 1;
        while(x < n && a[x-1] == a[x])
            x++;
        //[1,1,1,1,1]
        if(x >= n) return true;
        
        if(a[x-1] < a[x])
            incr = true;
        
        if(incr){
            for(int i=0;i<n-1;i++)
                if(a[i] > a[i+1])
                    return false;
            
            return true;
            
        }
        else{
            for(int i=0;i<n-1;i++)
                if(a[i] < a[i+1])
                    return false;
            
            return true;
        }
    }
}
