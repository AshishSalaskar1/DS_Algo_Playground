package sudoku;


public class Sudoku {

	static boolean isSafe(int[][] b,int row,int col,int val) {
		int N = b.length;
		//row
		for(int i=0;i<N;i++)
			if(b[row][i] == val)
				return false;
		
		//col
		for(int i=0;i<N;i++)
			if(b[i][col] == val)
				return false;
		
		//sub-grid
		int k = (int) Math.sqrt(N);
		int m = (row/k)*k;
		int n = (col/k)*k;
		
		
		for(int i=m;i<m+k;i++)
			for(int j=n;j<n+k;j++)
				if(b[i][j] == val)
					return false;
		
		return true;
	}
	
	static boolean solveSudoku(int[][] board) {
		int N = board.length;
		
		int row=-1,col=-1;
		boolean isEmpty = true;
		
		//check if all cells are filled ie !=0
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				if(board[i][j] == 0) {
					row = i;
					col = j;
					isEmpty = false;
					break;
				}
			}
			if(!isEmpty) break;
		}
		
		//if empty -> board is solved
		if(isEmpty) return true;
		
		//Fill numbers 1->N in unfilled row,col found above
		for(int num=1;num<=N;num++) {
			if(isSafe(board,row,col,num)) {
				//add num if adding it is safe
				board[row][col] = num;
				
				//consider next row
				if(solveSudoku(board)) return true;
				//if next row causes false -> backtrack and make state 0
				else board[row][col] = 0;
			}
		}
		
		
		return false;
	}
 	
	static void printBoard(int[][] a) {
		
		for(int i=0;i<a.length;i++) {
			for(int j=0;j<a.length;j++) {
				System.out.print(a[i][j]+" ");
			}
			System.out.println();
		}
		
	}
	
	public static void main(String[] args) {
		
		int[][] board = new int[][] 
				{ 
						{3, 0, 6, 5, 0, 8, 4, 0, 0}, 
						{5, 2, 0, 0, 0, 0, 0, 0, 0}, 
						{0, 8, 7, 0, 0, 0, 0, 3, 1}, 
						{0, 0, 3, 0, 1, 0, 0, 8, 0}, 
						{9, 0, 0, 8, 6, 3, 0, 0, 5}, 
						{0, 5, 0, 0, 9, 0, 6, 0, 0}, 
						{1, 3, 0, 0, 0, 0, 2, 5, 0}, 
						{0, 0, 0, 0, 0, 0, 0, 7, 4}, 
						{0, 0, 5, 2, 0, 6, 3, 0, 0} 
				}; 
				
		
		if (solveSudoku(board)) 
		{ 
			printBoard(board);
		} 
		else
		{ 
			System.out.println("No solution"); 
		}
		

	}

}

