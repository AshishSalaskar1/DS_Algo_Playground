class Solution {
    public int threeSumClosest(int[] a, int sum) {
        Arrays.sort(a);
        int minDiff = Integer.MAX_VALUE;
        int res = 0;
        int n = a.length;
        
        for(int i=0;i<n;i++){
            int curEle = a[i];
            
            int l=0,r=n-1,diff=0,curSum=0;
            
            while( l < r){
                if( l == i){ l++;continue;}
                if( r == i){ r--; continue;}
                
                curSum = curEle + a[l] + a[r];
                
                diff = Math.abs(curSum - sum);
                if(diff < minDiff){
                    minDiff = diff;
                    res = curSum;
                }
                
                if(curSum > sum) r--;
                else l++;
            }
        }
        
        return res;
    }
}
