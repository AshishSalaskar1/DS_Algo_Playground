package p1;

import java.util.*;
import java.io.*;

class Main {
	static int[][] a ;
	static int[][] res ;
	static int n,pow;
	
	// saveIn = a*b 
	static void mul(int[][] A,int[][] B,String saveIn) {
		int[][] mulRes = new int[n][n];
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				mulRes[i][j] = 0;
				for(int k=0;k<n;k++)
					mulRes[i][j] += A[i][k] * B[k][j]; 
			}
		}
		
		if(saveIn.equals("res")) {
			res = mulRes.clone();
		}
		else {

			a = mulRes.clone();
		}
	}
	
	static void printArr(int [][] arr) {
		for(int[] i : arr) {
			for(int j : i) {
				System.out.print(j+" ");
			}
			System.out.println();
		}
	}
	
    public static void main(String args[] ) {
    		Scanner in = new Scanner(System.in);
    		
    		n = in.nextInt();
    		pow = in.nextInt();
    		
    		a = new int[n][n];
    		res = new int[n][n];
    		
    		//res = 1
    		//here res = Identity matrix of size N
    		for(int i=0;i<n;i++)
    			for(int j=0;j<n;j++)
    			{
    				a[i][j] = in.nextInt();
    				if(i == j) res[i][j] = 1;
    				else res[i][j] = 0;
    			}


    		while(pow > 0) {
    			if(pow%2 != 0) {
    				mul(a,res,"res");
    				pow--;
    			}
    			else {
    				mul(a,a,"a");
    				pow = pow / 2;
    			}
    			
    		}
    		
    		printArr(res);
    		
    		
        }

}