package nqueens;

public class NQueens {
	
	//check up row, and up diagonals
	//no need for down bcoz recursion gets filled top to bottom row
	static boolean isSafe(int[][] board,int i,int j,int n){
		
		//up rows
		for(int row=0;row<i;row++) {
			if(board[row][j] == 1)
				return false;
		}
		
		//up right diagonal
		int x = i;
		int y = j;
		
		while(x>=0 && y<n) {
			if(board[x][y] == 1)
				return false;
			x--;
			y++;
		}
		
		//up left diagonal
		x = i;
		y = j;
				
		while(x>=0 && y>=0) {
			if(board[x][y] == 1)
					return false;
			x--;
			y--;
		}
		
		return true;	
	}
	
	//check by placing queen in each row
	static boolean nQueens(int[][] board,int i,int n) {
		
		if(i == n)
		{
			for(int x=0;x<n;x++) {
				for(int y=0;y<n;y++)
				{
					if(board[x][y] == 1)
						System.out.print("Q ");
					else
						System.out.print("_ ");
				}
				System.out.println();
			}
			
			System.out.println();
			
			//make false to print all possible ones
			//make true to print first possible one
			return false;
			
		}
		
		for(int j=0;j<n;j++) {
			if(isSafe(board, i, j, n)) {
				//place queen
				board[i][j] = 1;
				
				boolean canFillNextRow = nQueens(board, i+1, n);
				
				if(canFillNextRow)
					return true;
				
				//cant fill next row which means i,j placing was wrong
				//so backtrack
				board[i][j] = 0;
				
				
			}
		}
		
		return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 4;
		
		int[][] board = new int[n][n];
		
		nQueens(board, 0, n);

	}

}

