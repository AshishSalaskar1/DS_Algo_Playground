package p1;

import java.io.*;
import java.util.*;


public class Main {
	
	
	static boolean canPlace(int[][] board,int n,int i,int j) {
//		System.out.println("Yp");
		//b[i][j] = 0 : not visited previously
		return (i>=0 && j>=0 && i<n && j<n && board[i][j] == 0);
		
		
	}
	
	static void printBoard(int[][] board,int n) {
		for(int[] i : board) {
			for(int x:i)
				System.out.print(x+"\t");
			System.out.println();
		}
	}
	
	static boolean solveBoard(int[][] board,int n,int move_no,int row,int col) {
//		System.out.println(move_no);
		if(move_no == n*n) {
			printBoard(board, n);
			return true;
		}
		
		int[] rowDir = {2,1,-1,-2,-2,-1, 1, 2};
		int[] colDir = {1,2, 2, 1,-1,-2,-2,-1};
		
		
		//8 possible moves
		for(int i=0;i<8;i++) {
			
			int nextRow = row + rowDir[i];
			int nextCol = col + colDir[i];
			
			if(canPlace(board, n, nextRow, nextCol)) {
				
				board[nextRow][nextCol] = move_no+1;
				
				boolean isNextCorrext = solveBoard(board, n, move_no+1, nextRow, nextCol);
				if(isNextCorrext) return true;
				
				//backtracking step
				board[nextRow][nextCol] = 0;
			}
			
		}
		
		
		return false;
	}
	
    public static void main(String args[]) {
    	
    	Scanner in  = new Scanner(System.in);
    	 int n = in.nextInt();
    	 
    	 int[][] board = new int[n][n];
    	 
    	 //fill src as 1st move
    	 board[0][0] = 1;
    	 
    	 if(solveBoard(board, n, 1, 0, 0))
    		 System.out.println("DONE");
    	 else
    		 System.out.println("NOT POSSIBLE");
    	
    }
}