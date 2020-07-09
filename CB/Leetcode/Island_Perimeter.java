class Solution {
    
    int[][] arr;
    int m,n;
    int res;
    


    
    void check(int i,int j){
        if( i<0 || j<0 || i>=m || j>=n || arr[i][j] == 0)
        {
            res++;
            return;
        }
        
        if( arr[i][j] == -1)    return;
        
        arr[i][j] = -1;
        
         
        check(i+1,j);
        check(i,j+1);
        check(i-1,j);
        check(i,j-1);
        
        
    }
    
    public int islandPerimeter(int[][] grid) {
         arr = grid;
         m = arr.length;
         n = arr[0].length;
        
        res = 0;
        
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(arr[i][j] == 1)                   
                {
                     check(i,j);
                     break;
                }
               

        
        return res;
    }
}

// Without Global Variable
class Solution {
    
    int[][] arr;
    int m,n;

    
    int check(int i,int j){
        if( i<0 || j<0 || i>=m || j>=n || arr[i][j] == 0)
            return 1;
        
        if( arr[i][j] == -1)
            return 0;
        
        arr[i][j] = -1;
          
        return check(i+1,j) + check(i,j+1) + check(i-1,j) + check(i,j-1);   
    }
    
    public int islandPerimeter(int[][] grid) {
        arr = grid;
        m = arr.length;
        n = arr[0].length;

        
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(arr[i][j] == 1)                   
                     return check(i,j);

        return res;
    }
}
