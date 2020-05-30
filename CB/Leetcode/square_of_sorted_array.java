// https://leetcode.com/problems/squares-of-a-sorted-array

/**
[-8,-1,0,3,5]
  i	   j
[0 0 0 0 0 ]
i=8 ; j = 5
[0 0 0 0 64] a[i++] = 1
i = 1 j = 5
[0 0 0 25 64] a[j--] = 3 
*/

class Solution {
    

    public int[] sortedSquares(int[] a) {
        
        int n = a.length;
        int[] res = new int[n];
        
        int i = 0, j = n-1;
        
        for(int x=n-1; x >=0; x--){
            if(Math.abs(a[i]) > Math.abs(a[j])){
                 res[x] = Math.abs(a[i]*a[i]);
                 i++;
            }
            else{
                res[x] = Math.abs(a[j]*a[j]);
                j--;
            }
               
        }
        
        return res;
    }
}
