package rat_maze;

public class Rat_in_Maze {
	
	static void printPath(int[][] path) {
		int len = 0;
		int n = path.length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
					if(path[i][j] == 1) len++;
					System.out.print(path[i][j]+" ");
			}
			System.out.println();
		}
		
		System.out.println("Path length: "+len+"\n");
		
	}
	
	static void visitPath(int x,int y,int[][] maze,int[][] path) {
		int m = maze.length;
		int n = maze[0].length;
		
		if((x == m-1) && (y == n-1)) {
			path[x][y] = 1;
			printPath(path);
			return;
		}
		
		if(x<0 || y<0 || x>m-1 || y>n-1 || maze[x][y]==0 || path[x][y] == 1)
			return;
		
		path[x][y] = 1;
		
		//traverse top,bottom.left,right
		visitPath(x-1, y, maze, path);
		visitPath(x+1, y, maze, path);
		visitPath(x, y-1, maze, path);
		visitPath(x, y+1, maze, path);
		
		//Backtrack make curPoint unvisited as all posibilities are explored
		path[x][y] = 0;
	}
	
	static void ratInMaze(int[][] maze) {
		int[][] path = new int[maze.length][maze[0].length];
		
		visitPath(0, 0, maze, path);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] maze = new int[][] {
			{1 , 1 , 0},
			{0, 1, 1},
			{0, 1, 1}
		};
		
		ratInMaze(maze);

	}

}

