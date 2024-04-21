/**

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

*/

class Solution {
    public boolean searchMatrix(int[][] a, int target) {
        
        int m = a.length;
        if(m==0) return false;
        int n = a[0].length;
        
        
        //initially place at top-right
        int i = 0;
        int j = n-1;
        
        while( i>=0 && j>=0 && i<m && j <n){
            if(a[i][j] == target)
                return true;
            
            //go down : as going on left will only have less values
            else if(a[i][j] < target)
                i++;
            
            else
                j--;
        }
        
        return false;
        
        
    }
}
