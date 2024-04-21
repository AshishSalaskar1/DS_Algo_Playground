class Solution {
    public int[][] transpose(int[][] a) {
        int m = a.length;
        int n = a[0].length;
        
        int[][] res = new int[n][m];
        
        for(int i =0;i<m;i++)
            for(int j=0;j<n;j++)
                res[j][i] = a[i][j];

        return res;
    }
}
