/**
Given a positive integer n, 
generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

*/

class Solution {
    public int[][] generateMatrix(int n) {
        if(n == 0) return new int[0][0];
        
        int[][] a = new int[n][n];
        
        int count = 1;
        
        int rStart = 0, rEnd = n-1;
        int cStart = 0, cEnd = n-1;
        
        while( (rStart <= rEnd) && (cStart <= cEnd) ){
            
            for(int i=cStart; i<=cEnd; i++)
                a[rStart][i] = count++;
            
            rStart++;
            
            for(int i=rStart; i<=rEnd; i++)
                a[i][cEnd] = count++;
            
            cEnd--;
            
            if(rStart <= rEnd){
                for(int i=cEnd; i>=cStart; i--)
                    a[rEnd][i] = count++;
                
                rEnd--;
            }
            
            if(cStart <= cEnd){
                for(int i=rEnd; i>= rStart; i--)
                    a[i][cStart] = count++;
                
                cStart++;
            }
            
        }
        
        return a;
    }    
}
    
    
