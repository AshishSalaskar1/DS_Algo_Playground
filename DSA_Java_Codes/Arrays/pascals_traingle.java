package p1;

import java.util.*;
import java.io.*;

class Main {
	//n : No of lines
	static void pascalTriangle(int n) {
		int[][] a = new int[n+1][n+1];
		
		for(int i=1;i<=n;i++) {
			for(int j=0;j<i;j++) {
				if(j==0 || j==i)
					a[i][j] = 1;
				else
					a[i][j] = a[i-1][j-1] + a[i-1][j];
			}
		}
		
		for(int[] x : a) {
			for(int y : x) {
//				if(y==0) continue;
				System.out.print(y+" ");
			}
			System.out.println();
		}
	}
	
    public static void main(String args[] ) {
    		Scanner in = new Scanner(System.in);
    		
    		pascalTriangle(5);
    		
        }

}
