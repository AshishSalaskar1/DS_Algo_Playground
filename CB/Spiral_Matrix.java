package p1;
	
import java.util.*;
import java.io.*;
	
	
class Main {	
	static void spiralPrint(int[][] a) {
		int sRow = 0,eRow = a.length-1;
		int sCol = 0,eCol = a[0].length-1;
		
		while(sRow <= eRow && sCol <= eCol) {
			//right to left
			for(int i=sCol; i<=eCol; i++)
				System.out.print(a[sRow][i]+" ");
			sRow++;
			
			//right-top to right-bottom
			for(int i=sRow; i<=eRow; i++)
				System.out.print(a[i][eCol]+" ");
			eCol--;
			
			//right bottom to left bottom
			if(sRow <= eRow) {
				for(int i=eCol;i>=sCol;i--)
					System.out.print(a[eRow][i]+" ");
			}
			eRow--;
			
			//left btm to top
			if(sCol <= eCol) {
				for(int i=eRow;i>= sRow;i--)
					System.out.print(a[i][sCol]+" ");
			}
			sCol++;
			
//			sRow++;eRow--;
//			sCol++;eCol--;
		}
	}
	public static void main(String args[] ) throws IOException{
		  int[][] a = {
				  {1,2,3,4},
				  {14,15,16,5},
				  {13,20,17,6},
				  {12,19,18,7},
				  {11,10,9,8}
		  };
		  
		  int[][] b = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
		  spiralPrint(b);
	}
}
	
