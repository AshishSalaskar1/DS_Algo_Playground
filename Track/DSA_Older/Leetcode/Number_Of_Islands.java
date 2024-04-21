//Problem Link: https://leetcode.com/problems/number-of-islands/

class Solution {
    static int row,col;
    
    static void doWork(char[][] grid,int i,int j){
        if(i<0 || j<0 || i>=row || j>=col || grid[i][j] == '0' )
            return;
        
        grid[i][j] = '0';
        
        doWork(grid,i,j+1);
        doWork(grid,i-1,j);
        doWork(grid,i,j-1);
        doWork(grid,i+1,j);
    }
    
    public int numIslands(char[][] grid) {
        
        if(grid.length == 0 ) return 0;
        
         row = grid.length;
         col = grid[0].length;
        
        
        
        int count = 0;
        
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j] == '1'){
                    count++;
                    doWork(grid,i,j);
                }
            }
        }
        
        return count;
        
        
    }
}
